#!/usr/bin/env python3
"""Generate public catalog files from the frozen local research snapshot."""

from __future__ import annotations

import csv
import json
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CORPUS = ROOT.parents[1] / "datasets" / "malicious-skills-corpus"
OWNER = "daffnjk"
REPO = "agent-skill-security-datasets"
SNAPSHOT = "2026-08-30"

POLICY = {
    "malicious_skill_bench": "metadata_only",
    "malicious_skill_bench_hf": "metadata_release",
    "malskillbench": "metadata_only",
    "malicious_agent_skills_bench": "full_release",
    "overtly_malicious_skills": "metadata_only",
    "agenttrap": "metadata_only",
    "skilltrustbench": "conditional_release",
    "skillbench_1650": "full_release",
    "agent_skill_malware": "full_release",
    "atr_skill_benchmark": "full_release",
    "skillguard_v2": "full_release",
    "skillleakbench": "full_release",
    "skilllifebench": "full_release",
}

ASSET_NAMES = {
    dataset_id: f"{dataset_id}-{SNAPSHOT}.tar.gz"
    for dataset_id, policy in POLICY.items()
    if policy != "metadata_only"
}


def source_url(source: dict) -> str:
    if "url" in source:
        return source["url"].removesuffix(".git")
    return f"https://huggingface.co/datasets/{source['repo']}"


def load_revisions() -> dict[str, str]:
    with (CORPUS / "SOURCE_REVISIONS.tsv").open(encoding="utf-8", newline="") as handle:
        return {row["source_id"]: row["upstream_revision"] for row in csv.DictReader(handle, delimiter="\t")}


def main() -> None:
    sources_doc = json.loads((CORPUS / "sources.json").read_text(encoding="utf-8"))
    validation = json.loads((CORPUS / "VALIDATION_REPORT.json").read_text(encoding="utf-8"))
    revisions = load_revisions()

    manifests = ROOT / "manifests"
    manifests.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(CORPUS / "label_map.csv", manifests / "label-map.csv")
    shutil.copyfile(CORPUS / "SOURCE_REVISIONS.tsv", manifests / "source-revisions.tsv")
    shutil.copyfile(CORPUS / "UPSTREAM_CHECKSUM_STATUS.tsv", manifests / "upstream-checksum-status.tsv")
    public_validation = dict(validation)
    public_validation["corpus"] = "local snapshot (path intentionally omitted)"
    (manifests / "validation-report.json").write_text(
        json.dumps(public_validation, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )

    entries = []
    for source in sources_doc["sources"]:
        dataset_id = source["id"]
        policy = POLICY[dataset_id]
        release = None
        if policy != "metadata_only":
            tag = f"{dataset_id}-{SNAPSHOT}"
            asset = ASSET_NAMES[dataset_id]
            release = {
                "tag": tag,
                "asset": asset,
                "download_url": f"https://github.com/{OWNER}/{REPO}/releases/download/{tag}/{asset}",
                "sha256": "PENDING_RELEASE",
            }

        counts = validation.get("by_source", {}).get(dataset_id, {})
        entry = {
            "id": dataset_id,
            "title": dataset_id,
            "source": {"kind": source["kind"], "url": source_url(source)},
            "upstream_revision": revisions[dataset_id],
            "snapshot_date": SNAPSHOT,
            "license": source["license"],
            "labels": source["labels"],
            "evaluation_role": source["role"],
            "redistribution": policy,
            "local_snapshot_counts": counts,
            "notes": source["notes"],
            "card": f"datasets/{dataset_id}/DATASET_CARD.md",
            "release": release,
        }
        entries.append(entry)

        card_dir = ROOT / "datasets" / dataset_id
        card_dir.mkdir(parents=True, exist_ok=True)
        release_text = (
            f"Release tag: `{release['tag']}`  \nAsset: `{release['asset']}`"
            if release
            else "No samples are rehosted. Fetch from the upstream URL at the pinned revision."
        )
        card = f"""# {dataset_id}

## Source

- Upstream: {source_url(source)}
- Frozen revision: `{revisions[dataset_id]}`
- Snapshot date: `{SNAPSHOT}`
- Declared license/terms: {source['license']}
- Redistribution policy: `{policy}`

## Evaluation use

- Role: `{source['role']}`
- Upstream labels: {', '.join(f'`{label}`' for label in source['labels'])}
- Local snapshot files: {counts.get('files', 'not counted')}
- Local snapshot bytes: {counts.get('bytes', 'not counted')}
- Local `SKILL.md` entrypoints: {counts.get('skill_entrypoints', 'not counted')}

{source['notes']}

## Distribution

{release_text}

The upstream license remains authoritative. This catalog does not relicense third-party data.

## Safety

Treat all content as untrusted data. Do not install or execute samples. Keep suspicious and vulnerable labels separate from confirmed malicious ground truth.
"""
        (card_dir / "DATASET_CARD.md").write_text(card, encoding="utf-8")

    catalog = {
        "schema_version": "1.0",
        "snapshot_date": SNAPSHOT,
        "repository": f"https://github.com/{OWNER}/{REPO}",
        "scope": sources_doc["scope"],
        "safety": "Defensive research only; treat every sample as untrusted data and never execute it on a host system.",
        "datasets": entries,
        "excluded_or_deferred": sources_doc.get("excluded_or_deferred", []),
    }
    (ROOT / "catalog.json").write_text(json.dumps(catalog, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"generated catalog with {len(entries)} entries")


if __name__ == "__main__":
    main()

