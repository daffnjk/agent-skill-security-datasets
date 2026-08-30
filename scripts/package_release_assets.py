#!/usr/bin/env python3
"""Create deterministic, non-executable, per-dataset release archives.

The script reads sample files as bytes. It never imports or executes downloaded content.
"""

from __future__ import annotations

import gzip
import hashlib
import io
import json
import os
import tarfile
from pathlib import Path, PurePosixPath


ROOT = Path(__file__).resolve().parents[1]
CORPUS = ROOT.parents[1] / "datasets" / "malicious-skills-corpus"
OUTPUT = ROOT.parent / "release-assets"
SNAPSHOT = "2026-08-30"

PACKAGES = {
    "malicious_agent_skills_bench": {
        "base": "raw/github/malicious_agent_skills_bench",
        "include": ["LICENSE", "README.md", "data"],
    },
    "agent_skill_malware": {
        "base": "raw/huggingface/agent_skill_malware",
        "include": ["README.md", "skills.jsonl"],
    },
    "atr_skill_benchmark": {
        "base": "raw/huggingface/atr_skill_benchmark",
        "include": ["README.md", "atr-skill-benchmark.jsonl"],
    },
    "skillleakbench": {
        "base": "raw/huggingface/skillleakbench",
        "include": ["README.md", "skills_dataset.csv", "issues.csv", "remediation_summary.csv", "popularity_hardcoded_repos.csv"],
    },
    "skillguard_v2": {
        "base": "raw/huggingface/skillguard_v2",
        "include": ["README.md", "data"],
    },
    "skillbench_1650": {
        "base": "raw/huggingface/skillbench_1650",
        "include": ["README.md", "benign.parquet", "malicious.parquet"],
    },
    "skilllifebench": {
        "base": "raw/huggingface/skilllifebench",
        "include": ["LICENSE", "README.md", "annotations", "registry", "schema", "skills"],
    },
    "skilltrustbench": {
        "base": "raw/huggingface/skilltrustbench",
        "include": ["README.md", "data", "metadata", "benchmark_full_v1.0", "benchmark_full_v1.0.zip"],
    },
    "malicious_skill_bench_hf": {
        "base": "raw/huggingface/malicious_skill_bench_hf",
        "include": ["README.md", "metadata.parquet", "attack_taxonomy.parquet", "impact_taxonomy.parquet", "package_manifest.csv", "schema.json", "source_registry.csv", "structural_families.csv", "splits"],
    },
}


def safe_members(base: Path, selections: list[str]):
    for selection in selections:
        selected = base / selection
        if not selected.exists():
            raise FileNotFoundError(selected)
        paths = [selected] if selected.is_file() else sorted(p for p in selected.rglob("*") if p.is_file())
        for path in paths:
            if path.is_symlink():
                raise RuntimeError(f"refusing symlink: {path}")
            rel = path.relative_to(base)
            if any(part in {".git", "__pycache__"} for part in rel.parts):
                continue
            yield path, rel


def add_bytes(tar: tarfile.TarFile, name: str, payload: bytes) -> None:
    info = tarfile.TarInfo(name)
    info.size = len(payload)
    info.mode = 0o644
    info.uid = info.gid = 0
    info.uname = info.gname = "root"
    info.mtime = 0
    tar.addfile(info, io.BytesIO(payload))


def build(dataset_id: str, config: dict, catalog_entry: dict) -> tuple[Path, str, int]:
    base = CORPUS / config["base"]
    output = OUTPUT / f"{dataset_id}-{SNAPSHOT}.tar.gz"
    if output.exists():
        raise RuntimeError(f"refusing to overwrite existing asset: {output}")
    top = f"{dataset_id}-{SNAPSHOT}"
    with output.open("xb") as raw:
        with gzip.GzipFile(filename="", mode="wb", fileobj=raw, mtime=0) as zipped:
            with tarfile.open(fileobj=zipped, mode="w", format=tarfile.PAX_FORMAT) as tar:
                notice = {
                    "dataset_id": dataset_id,
                    "source": catalog_entry["source"],
                    "upstream_revision": catalog_entry["upstream_revision"],
                    "snapshot_date": SNAPSHOT,
                    "license": catalog_entry["license"],
                    "redistribution": catalog_entry["redistribution"],
                    "safety": "Untrusted defensive-research data. Do not install or execute.",
                }
                add_bytes(tar, f"{top}/NOTICE.json", (json.dumps(notice, indent=2) + "\n").encode())
                card = (ROOT / catalog_entry["card"]).read_bytes()
                add_bytes(tar, f"{top}/DATASET_CARD.md", card)
                for path, rel in safe_members(base, config["include"]):
                    arc = PurePosixPath(top, "data", *rel.parts).as_posix()
                    payload = path.read_bytes()
                    add_bytes(tar, arc, payload)
    digest = hashlib.sha256(output.read_bytes()).hexdigest()
    return output, digest, output.stat().st_size


def main() -> None:
    OUTPUT.mkdir(parents=True, exist_ok=True)
    catalog_path = ROOT / "catalog.json"
    catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
    entries = {entry["id"]: entry for entry in catalog["datasets"]}
    results = []
    for dataset_id, config in PACKAGES.items():
        output, digest, size = build(dataset_id, config, entries[dataset_id])
        entries[dataset_id]["release"]["sha256"] = digest
        results.append({"dataset_id": dataset_id, "asset": output.name, "bytes": size, "sha256": digest})
        print(f"built {output.name} bytes={size} sha256={digest}")

    catalog_path.write_text(json.dumps(catalog, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    manifest = {"snapshot_date": SNAPSHOT, "assets": results}
    manifest_path = OUTPUT / f"release-assets-{SNAPSHOT}.json"
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    checksum_path = OUTPUT / f"SHA256SUMS-{SNAPSHOT}.txt"
    checksum_path.write_text("".join(f"{row['sha256']}  {row['asset']}\n" for row in results), encoding="utf-8")


if __name__ == "__main__":
    main()

