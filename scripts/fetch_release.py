#!/usr/bin/env python3
"""下载一个目录中的 GitHub Release 资产并验证 SHA-256。"""

from __future__ import annotations

import argparse
import hashlib
import json
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    parser = argparse.ArgumentParser(description="下载一个可再分发数据集并验证 SHA-256")
    parser.add_argument("--dataset", required=True, help="catalog.json 中的数据集 ID")
    parser.add_argument("--output", type=Path, required=True, help="下载目录")
    args = parser.parse_args()

    catalog = json.loads((ROOT / "catalog.json").read_text(encoding="utf-8"))
    entries = {entry["id"]: entry for entry in catalog["datasets"]}
    if args.dataset not in entries:
        raise SystemExit(f"未知数据集：{args.dataset}")
    release = entries[args.dataset].get("release")
    if not release:
        raise SystemExit("这个数据源仅提供索引；请使用对应数据集卡片中的上游地址")

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
        raise SystemExit(f"校验和不匹配：期望 {expected}，实际 {digest}")
    partial.replace(target)
    print(f"下载完成：{target} sha256={digest}")


if __name__ == "__main__":
    main()
