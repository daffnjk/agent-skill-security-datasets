# Agent Skill Security Datasets

A source-traceable catalog and release index for public datasets used to evaluate malicious, suspicious, vulnerable, and runtime-adversarial Agent Skills.

> [!CAUTION]
> This repository is for defensive security research. Some linked release assets contain adversarial instructions or malicious-looking code. Treat every sample as untrusted data: do not install, execute, import, or grant it credentials/network access. See [Safe usage](docs/SAFE_USAGE.md).

## What is published

- A normalized catalog with one card per upstream dataset.
- Frozen upstream revisions, label mappings, and validation results.
- One GitHub Release per redistributable dataset family.
- Source-only acquisition instructions when redistribution rights are unclear.

Raw samples are deliberately excluded from Git history. Release assets remain separated by dataset so licenses, provenance, labels, and evaluation roles are not mixed.

## Snapshot summary

Snapshot: **2026-08-30**

- 13 source entries
- 484,322 indexed files in the local research snapshot
- 21,285 `SKILL.md` entrypoints
- 9 independently packaged release assets
- 4 source-only entries subject to upstream or third-party terms

See [`catalog.json`](catalog.json) and [`datasets/`](datasets/) for exact details. The totals describe the local research snapshot; not every indexed file is redistributed here.

## Quick start

```bash
python3 scripts/validate_catalog.py
python3 scripts/fetch_release.py --dataset agent_skill_malware --output ./downloads
```

`fetch_release.py` downloads only assets listed in the catalog and verifies SHA-256 checksums when a release manifest is available.

## Evaluation guidance

Do not collapse every upstream label into a single positive class without recording the transformation. In particular:

- `malicious` is suitable for positive detection tests.
- `suspicious` is a triage class, not confirmed malicious ground truth.
- `vulnerable` measures unsafe implementation patterns, not malicious intent.
- `adversarial_prompt` is auxiliary prompt-injection coverage, not a package-malware label.
- benign/safe/normal samples should be retained for false-positive measurement.

The canonical mapping is in [`manifests/label-map.csv`](manifests/label-map.csv).

## Releases and redistribution

The repository's own catalog, documentation, and utility scripts are MIT-licensed. Every upstream dataset retains its own license and attribution requirements. A release asset is not relicensed by this repository.

See [Redistribution policy](docs/REDISTRIBUTION.md) and [Third-party notices](THIRD_PARTY_NOTICES.md). If a source is marked `metadata_only`, fetch it from the upstream URL and verify the frozen revision rather than mirroring it.

## Reproducibility

The snapshot is pinned in [`manifests/source-revisions.tsv`](manifests/source-revisions.tsv). Validation evidence is preserved in [`manifests/validation-report.json`](manifests/validation-report.json). No downloaded sample was executed during collection, extraction, indexing, packaging, or validation.

## 中文说明

本仓库用于防御性检测评测。Git 历史仅保存目录、来源、标签和校验信息；可再分发的数据按数据集分别放在 GitHub Releases。许可不明确或包含第三方上游内容的数据只给出来源和固定版本，不重新托管。所有样本都应按不可信输入处理，禁止直接安装或执行。

## Reporting

For accidental secret exposure, unsafe release contents, license concerns, or security issues, follow [`SECURITY.md`](SECURITY.md).

