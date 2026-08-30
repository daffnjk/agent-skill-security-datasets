#!/usr/bin/env python3
"""Validate the public catalog without loading or executing dataset samples."""

from __future__ import annotations

import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ALLOWED_POLICIES = {"full_release", "conditional_release", "metadata_release", "metadata_only"}


def main() -> None:
    catalog = json.loads((ROOT / "catalog.json").read_text(encoding="utf-8"))
    release_manifest = json.loads(
        (ROOT / "manifests" / "release-assets-2026-08-30.json").read_text(encoding="utf-8")
    )
    release_assets = {row["dataset_id"]: row for row in release_manifest["assets"]}
    datasets = catalog.get("datasets", [])
    assert catalog.get("schema_version") == "1.0"
    assert datasets, "catalog must contain datasets"

    ids = [entry["id"] for entry in datasets]
    assert len(ids) == len(set(ids)), "dataset IDs must be unique"

    for entry in datasets:
        assert entry["redistribution"] in ALLOWED_POLICIES
        assert entry["source"]["url"].startswith("https://")
        assert len(entry["upstream_revision"]) == 40
        card = ROOT / entry["card"]
        assert card.is_file(), f"missing card: {card}"
        if entry["redistribution"] == "metadata_only":
            assert entry.get("release") is None
        else:
            release = entry.get("release", {})
            assert release.get("tag")
            manifest_row = release_assets[entry["id"]]
            assert release["asset"] == manifest_row["asset"]
            assert release["sha256"] == manifest_row["sha256"]

    expected_release_ids = {
        entry["id"] for entry in datasets if entry["redistribution"] != "metadata_only"
    }
    assert set(release_assets) == expected_release_ids

    with (ROOT / "manifests" / "label-map.csv").open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    known = set(ids)
    unknown = sorted({row["source_id"] for row in rows} - known)
    assert not unknown, f"label map references unknown datasets: {unknown}"

    print(f"validated {len(datasets)} dataset entries and {len(rows)} label mappings")


if __name__ == "__main__":
    main()
