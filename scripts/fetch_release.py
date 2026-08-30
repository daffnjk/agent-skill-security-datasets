#!/usr/bin/env python3
"""Download one cataloged GitHub Release asset and verify its SHA-256 digest."""

from __future__ import annotations

import argparse
import hashlib
import json
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    catalog = json.loads((ROOT / "catalog.json").read_text(encoding="utf-8"))
    entries = {entry["id"]: entry for entry in catalog["datasets"]}
    if args.dataset not in entries:
        raise SystemExit(f"unknown dataset: {args.dataset}")
    release = entries[args.dataset].get("release")
    if not release:
        raise SystemExit("this entry is source-only; use the upstream URL in its dataset card")

    asset = release["asset"]
    url = release["download_url"]
    expected = release.get("sha256")
    args.output.mkdir(parents=True, exist_ok=True)
    target = args.output / asset
    partial = target.with_suffix(target.suffix + ".part")
    urllib.request.urlretrieve(url, partial)
    digest = hashlib.sha256(partial.read_bytes()).hexdigest()
    if expected and expected != "PENDING_RELEASE" and digest != expected:
        partial.unlink(missing_ok=True)
        raise SystemExit(f"checksum mismatch: expected {expected}, got {digest}")
    partial.replace(target)
    print(f"downloaded {target} sha256={digest}")


if __name__ == "__main__":
    main()

