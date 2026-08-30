#!/usr/bin/env python3
"""Audit release archives for path traversal, links, devices, and executable modes."""

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
        print(f"audited {archive.name}: {count} regular non-executable members")
    print(f"audited {len(archives)} archives and {total} members")


if __name__ == "__main__":
    main()

