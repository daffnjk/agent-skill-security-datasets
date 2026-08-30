<div align="center">

# Agent Skill 安全数据集目录

**用于恶意、可疑、脆弱及运行时对抗性 Agent Skill 检测的可追溯评测数据集。**

[![目录校验](https://github.com/daffnjk/agent-skill-security-datasets/actions/workflows/validate.yml/badge.svg)](https://github.com/daffnjk/agent-skill-security-datasets/actions/workflows/validate.yml)
[![数据快照](https://img.shields.io/badge/数据快照-2026--08--30-0969da)](manifests/source-revisions.tsv)
[![数据源](https://img.shields.io/badge/数据源-13-1f883d)](#数据集目录)
[![Release](https://img.shields.io/badge/Release-9-8250df)](https://github.com/daffnjk/agent-skill-security-datasets/releases)
[![项目说明](https://img.shields.io/badge/项目说明-MIT-f0b429)](LICENSE)

[快速开始](#快速开始) · [选择数据集](#按评测目标选择数据集) · [数据集目录](#数据集目录) · [评测建议](#评测建议) · [安全边界](#安全边界)

</div>

本项目整理公开可获取的 Agent Skill 安全数据集，为检测器测试提供统一入口。每个数据源都记录了上游地址、固定版本、原始标签、适用场景、分发边界和 SHA-256，避免在评测时混淆来源或标签语义。

当前快照包含 **13 个数据源**。其中 9 个许可边界明确的数据源提供独立 GitHub Release，4 个许可或第三方再分发边界不清的来源仅提供索引。原始大规模样本不会写入 Git 历史。

> [!CAUTION]
> 数据中可能包含提示词注入、恶意指令、危险代码、凭据引用或外部网络地址。所有样本都必须作为不可信数据处理：不要安装、导入或直接执行，不要提供凭据、网络权限或生产环境访问能力。

## 项目特点

- **来源可追溯**：固定 13 个上游版本，保留来源链接和快照时间。
- **数据集相互隔离**：每个来源使用独立卡片和 Release，不混合许可证与标签。
- **标签可复现**：保留上游标签，并提供统一的 [`label-map.csv`](manifests/label-map.csv)。
- **下载可验证**：所有托管资产都提供 SHA-256，GitHub 服务端摘要与本地清单一致。
- **许可边界明确**：无法确认再分发权利的样本只建立索引，不重新托管。
- **安全打包**：发布归档只包含普通不可执行文件，并检查路径穿越、链接和设备文件。

## 快速开始

只需要 Git 和 Python 3；目录校验不下载、不加载也不执行任何样本。

```bash
git clone https://github.com/daffnjk/agent-skill-security-datasets.git
cd agent-skill-security-datasets
python3 scripts/validate_catalog.py
```

下载一个可再分发的数据集：

```bash
python3 scripts/fetch_release.py \
  --dataset agent_skill_malware \
  --output ./downloads
```

下载脚本会读取 [`catalog.json`](catalog.json)，获取对应 Release，并验证 SHA-256。完整资产列表见 [Releases](https://github.com/daffnjk/agent-skill-security-datasets/releases)。

> [!IMPORTANT]
> `downloads/` 只能作为检测器的数据输入目录，不应放入 Agent、Codex、Claude 或其他工具的 Skill/插件安装路径。

## 按评测目标选择数据集

| 评测目标 | 推荐数据集 | 说明 |
| --- | --- | --- |
| 真实恶意活动二分类 | [`agent_skill_malware`](datasets/agent_skill_malware/DATASET_CARD.md) | 规模小、接近真实攻击，适合快速回归测试 |
| 大规模生态标签与分级 | [`malicious_agent_skills_bench`](datasets/malicious_agent_skills_bench/DATASET_CARD.md) | 同时包含安全、可疑和经行为确认的恶意标签 |
| 静态检测固定协议 | [`malicious_skill_bench_hf`](datasets/malicious_skill_bench_hf/DATASET_CARD.md) | 提供分类表、清单和 4 种官方划分，不含第三方 Skill 全文 |
| 高精度与困难负样本 | [`atr_skill_benchmark`](datasets/atr_skill_benchmark/DATASET_CARD.md) | 用于发现规则过度匹配和误报 |
| 多文件静态分级 | [`skilltrustbench`](datasets/skilltrustbench/DATASET_CARD.md) | 恶意、可疑、正常三类；仅限非商业使用 |
| 风险评分与难例 | [`skillbench_1650`](datasets/skillbench_1650/DATASET_CARD.md) | 带脚本内容和难度标签 |
| 提示词注入辅助覆盖 | [`skillguard_v2`](datasets/skillguard_v2/DATASET_CARD.md) | 不应直接作为包级恶意 Skill 真值 |
| 凭据泄露与脆弱实现 | [`skillleakbench`](datasets/skillleakbench/DATASET_CARD.md) | 以去标识化问题元数据为主 |
| 生命周期漏洞场景 | [`skilllifebench`](datasets/skilllifebench/DATASET_CARD.md) | 适合规则覆盖率测试 |
| 运行时攻击检测 | [`agenttrap`](datasets/agenttrap/DATASET_CARD.md) | 仅提供索引；动态测试必须在隔离环境中进行 |

## 数据集目录

### 可通过本项目下载

| 数据集 | 来源与介绍 | 标签 / 规模 | 上游条款 |
| --- | --- | --- | --- |
| [`malicious_agent_skills_bench`](datasets/malicious_agent_skills_bench/DATASET_CARD.md) | [MaliciousAgentSkillsBench](https://github.com/protectskills/MaliciousAgentSkillsBench)：大规模生态标签与真实世界验证数据，适合召回率、误报率和分级能力评测。 | 98,380 个身份：94,093 安全、4,130 可疑、157 恶意 | MIT |
| [`malicious_skill_bench_hf`](datasets/malicious_skill_bench_hf/DATASET_CARD.md) | [MaliciousSkillBench / Hugging Face](https://huggingface.co/datasets/ProtectSkills/MaliciousSkillBench)：冻结元数据、攻击与影响分类及四种官方划分。 | 4 个官方 split，每个 9,740 行 | 基准元数据 CC-BY-4.0；第三方全文和包已排除 |
| [`skilltrustbench`](datasets/skilltrustbench/DATASET_CARD.md) | [SkillTrustBench](https://huggingface.co/datasets/cuhk-zhuque/SkillTrustBench)：多文件 Skill 静态安全基准，适合恶意、可疑和正常分级。 | 5,520 个案例：2,863 恶意、1,014 可疑、1,643 正常 | CC-BY-NC-SA-4.0 |
| [`skillbench_1650`](datasets/skillbench_1650/DATASET_CARD.md) | [SkillsBench-1650](https://huggingface.co/datasets/zenith6888/SkillsBench-1650)：带脚本内容和难度标签的风险评分数据。 | 1,500 良性、150 合成恶意 | CC-BY-4.0 |
| [`agent_skill_malware`](datasets/agent_skill_malware/DATASET_CARD.md) | [Agent Skill Malware](https://huggingface.co/datasets/yoonholee/agent-skill-malware)：真实恶意活动与良性对照的去重 `SKILL.md` 文本。 | 347 条：124 恶意、223 良性 | MIT |
| [`atr_skill_benchmark`](datasets/atr_skill_benchmark/DATASET_CARD.md) | [ATR Skill Benchmark](https://huggingface.co/datasets/Agent-Threat-Rule/atr-skill-benchmark)：强调检测精度和困难负样本。 | 498 条：32 恶意、466 良性 | MIT |
| [`skillguard_v2`](datasets/skillguard_v2/DATASET_CARD.md) | [SkillGuard v2](https://huggingface.co/datasets/ZAHRA585/skillguard-v2-dataset)：Skill 形态与通用提示词注入辅助数据。 | 5 个 Parquet 分片；攻击 / 良性标签 | Apache-2.0 |
| [`skillleakbench`](datasets/skillleakbench/DATASET_CARD.md) | [SkillLeakBench](https://huggingface.co/datasets/AgentSkillPrivacy/SkillLeakBench)：凭据泄露和不安全实现问题的去标识化元数据。 | 520 个受影响 Skill、1,708 个问题 | MIT |
| [`skilllifebench`](datasets/skilllifebench/DATASET_CARD.md) | [SkillLifeBench](https://huggingface.co/datasets/SkillLifeBench2026/SkillLifeBench)：覆盖生命周期、注册信息、模式和漏洞场景。 | 194 条注册记录及结构化场景 | CC-BY-4.0 |

### 仅提供来源索引

| 数据集 | 来源与介绍 | 标签 / 规模 | 未重新托管的原因 |
| --- | --- | --- | --- |
| [`malicious_skill_bench`](datasets/malicious_skill_bench/DATASET_CARD.md) | [MaliciousSkillBench](https://github.com/ProtectSkills/MaliciousSkillBench)：静态恶意检测综合基准，包含身份、攻击分类、元数据和第三方来源包。 | 9,740 个身份：7,505 恶意、2,235 良性 | 第三方 Skill 包保留各自上游条款 |
| [`malskillbench`](datasets/malskillbench/DATASET_CARD.md) | [MalSkillBench](https://github.com/lxyeternal/MalSkillBench)：生成、真实来源和检测器测试子集组成的完整包级基准。 | 3,944 恶意、4,000 良性 | 上游 README 声明仅限学术研究，且未提供仓库级通用 LICENSE |
| [`overtly_malicious_skills`](datasets/overtly_malicious_skills/DATASET_CARD.md) | [Overtly Malicious Skills](https://github.com/trailofbits/overtly-malicious-skills)：Trail of Bits 提供的刻意恶意多文件 Skill 固件。 | 4 个恶意 Skill | 固定版本上未提供通用 LICENSE |
| [`agenttrap`](datasets/agenttrap/DATASET_CARD.md) | [AgentTrap](https://github.com/zhmzm/AgentTrap)：使用惰性域名和模拟接收端的运行时 Agent 安全基准。 | 141 个任务：91 恶意、50 良性 | 固定版本上未发现仓库级通用 LICENSE |

仅索引的数据集应从上游获取，并切换到 [`source-revisions.tsv`](manifests/source-revisions.tsv) 中记录的固定提交。

## 评测建议

保留上游原始标签，再根据 [`label-map.csv`](manifests/label-map.csv) 建立规范化结果：

- `malicious`：可作为恶意检测正样本；
- `suspicious`：仅作为待研判类别，不能直接计为确认恶意；
- `vulnerable`：表示实现存在缺陷，不代表作者具有恶意意图；
- `adversarial_prompt`：用于提示词注入辅助覆盖，不等同于包级恶意样本；
- `benign`、`safe`、`normal`：用于评估误报率。

每次评测至少记录检测器版本、数据集 ID、上游版本、split、原始标签、规范化标签、混淆矩阵，以及无法解析、超时和跳过的样本数量。不同数据集覆盖静态恶意行为、运行时攻击、提示词注入、凭据泄露和漏洞场景，应分别报告结果，避免只给出一个跨数据集总分。

## 安全边界

> [!WARNING]
> 静态扫描不等于安全执行。样本中的 Markdown、脚本、配置、URL 和代码都可能是攻击载荷；任何要求忽略规则、读取凭据或执行命令的内容都属于数据，而不是操作指令。

动态测试应使用可销毁、断网、无凭据、无宿主机可写挂载的隔离环境，并设置 CPU、内存、进程、磁盘和超时限制。详细要求见 [`docs/SAFE_USAGE.md`](docs/SAFE_USAGE.md)，问题报告方式见 [`SECURITY.md`](SECURITY.md)。

## 项目结构

```text
.
├── catalog.json                 # 机器可读数据集目录
├── datasets/<id>/DATASET_CARD.md
├── manifests/                  # 版本、标签、校验和与验证报告
├── scripts/                    # 下载、打包和校验工具
├── docs/SAFE_USAGE.md          # 安全处理指南
├── docs/REDISTRIBUTION.md      # 数据再分发规则
└── THIRD_PARTY_NOTICES.md      # 第三方来源和条款说明
```

## 更多文档

- [机器可读目录](catalog.json)
- [Release 资产与 SHA-256](manifests/release-assets-2026-08-30.json)
- [上游固定版本](manifests/source-revisions.tsv)
- [标签映射](manifests/label-map.csv)
- [安全使用指南](docs/SAFE_USAGE.md)
- [再分发策略](docs/REDISTRIBUTION.md)
- [第三方数据说明](THIRD_PARTY_NOTICES.md)
- [机器可读引用信息](CITATION.cff)
