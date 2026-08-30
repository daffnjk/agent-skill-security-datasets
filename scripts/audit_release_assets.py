#!/usr/bin/env python3
"""检查发布归档中的路径穿越、链接、设备文件和可执行权限。"""

from __future__ import annotations

import argparse
import tarfile
from pathlib import Path, PurePosixPath


def audit(path: Path) -> int:
    count = 0
    with tarfile.open(path, "r:gz") as archive:
        for member in archive:
            count += 1
            normalized = PurePosixPath(member.name)
            assert not normalized.is_absolute(), f"absolute path: {member.name}"
            assert ".." not in normalized.parts, f"path traversal: {member.name}"
            assert member.isfile(), f"non-regular member: {member.name}"
            assert member.mode & 0o111 == 0, f"executable mode: {member.name}"
    return count


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("asset_dir", type=Path)
    args = parser.parse_args()
    archives = sorted(args.asset_dir.glob("*.tar.gz"))
    assert archives, "no release archives found"
    total = 0
    for archive in archives:
        count = audit(archive)
        total += count
        print(f"归档检查通过：{archive.name}，{count} 个普通不可执行文件")
    print(f"检查完成：{len(archives)} 个归档，{total} 个文件")


if __name__ == "__main__":
    main()
