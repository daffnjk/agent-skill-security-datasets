# Agent Skill 安全数据集目录

这是我整理并维护的一套 **Agent Skill 安全检测评测数据集目录**。我建立这个项目，是为了方便自己和其他安全研究者以可追溯、可复现的方式测试恶意 Skill 检测引擎，同时避免把来源、标签和许可证不同的数据混在一起。

当前快照日期为 **2026-08-30**，共收录 13 个公开数据源。本地研究快照包含 484,322 个文件和 21,285 个 `SKILL.md` 入口；其中许可允许再分发的内容被整理成 9 个相互独立的 GitHub Release，其余来源只保留索引、固定版本和原站下载说明。

> [!CAUTION]
> 本项目仅用于防御性安全研究。数据中可能包含提示词注入、恶意指令、危险代码、凭据引用或外部网络地址。请把所有样本视为不可信数据：不要安装、导入或直接执行，不要向样本提供凭据、网络权限或生产环境访问能力。

## 我做了什么

- 我记录了每个数据集的原始来源、固定版本、许可证、标签体系和适用场景。
- 我为每个数据集保留独立的数据集卡片和 Release，避免许可证及标签语义互相污染。
- 我统一提供了标签映射，但保留所有上游原始标签，便于复现实验。
- 我只重新托管许可证允许的文件；许可不明确或包含第三方内容的来源只提供索引。
- 我对发布包计算 SHA-256，并检查路径穿越、符号链接、设备文件和可执行权限。
- 整个收集、解压、索引、打包和验证过程均未执行下载到的样本。

## 数据集来源与介绍

下面是当前收录的全部 13 个数据源。“发布方式”表示本项目如何提供数据，不代表我改变了上游许可证。

| 数据集 ID | 来源 | 数据集介绍 | 标签/规模 | 许可证 | 发布方式 |
| --- | --- | --- | --- | --- | --- |
| `malicious_skill_bench` | [ProtectSkills/MaliciousSkillBench](https://github.com/ProtectSkills/MaliciousSkillBench) | 面向 Agent Skill 静态恶意检测的综合基准，包含恶意与良性身份、攻击分类、元数据及第三方来源包。适合主检测能力和误报率评测。 | 9,740 个身份：7,505 恶意、2,235 良性；本地含 7,526 个 Skill 入口 | 基准元数据 CC-BY-4.0；第三方包保留各自条款 | 仅索引；第三方 Skill 包不重新托管 |
| `malicious_skill_bench_hf` | [ProtectSkills/MaliciousSkillBench（Hugging Face）](https://huggingface.co/datasets/ProtectSkills/MaliciousSkillBench) | 上一数据集的冻结表格、攻击/影响分类和四种官方数据划分，适合复现固定评测协议。 | 4 个官方 split，每个 9,740 行 | 基准元数据 CC-BY-4.0 | 发布元数据、分类表、清单和官方划分；排除第三方全文及包 |
| `malskillbench` | [lxyeternal/MalSkillBench](https://github.com/lxyeternal/MalSkillBench) | 完整 Skill 包级恶意检测基准，覆盖生成样本、真实来源样本和检测器测试子集，适合目录级或多文件扫描测试。 | 3,944 恶意、4,000 良性；本地含 8,018 个 Skill 入口 | 上游仓库未发现通用 LICENSE | 仅索引，按固定提交从原站获取 |
| `malicious_agent_skills_bench` | [protectskills/MaliciousAgentSkillsBench](https://github.com/protectskills/MaliciousAgentSkillsBench) | 大规模生态标签与真实世界验证数据，区分安全、可疑和经过行为确认的恶意 Skill，适合测试召回率、误报率和分级能力。 | 98,380 个身份：94,093 安全、4,130 可疑、157 恶意 | MIT | 完整 Release |
| `overtly_malicious_skills` | [trailofbits/overtly-malicious-skills](https://github.com/trailofbits/overtly-malicious-skills) | Trail of Bits 提供的少量、刻意设计为恶意的多文件 Skill 固件，可用于检测明显恶意行为及扫描规避表现。 | 4 个恶意多文件 Skill | 上游仓库未提供通用 LICENSE | 仅索引，不重新托管样本 |
| `agenttrap` | [zhmzm/AgentTrap](https://github.com/zhmzm/AgentTrap) | 运行时 Agent 安全基准，使用惰性域名和模拟数据接收端构造恶意及良性任务，适合沙箱中的动态检测评测。 | 141 个任务：91 恶意、50 良性 | 上游仓库未发现通用 LICENSE | 仅索引，按固定提交从原站获取 |
| `skilltrustbench` | [cuhk-zhuque/SkillTrustBench](https://huggingface.co/datasets/cuhk-zhuque/SkillTrustBench) | 多文件 Skill 静态安全基准，提供恶意、可疑和正常三类样本及完整归档，适合分级检测与多文件分析。 | 5,520 个案例：2,863 恶意、1,014 可疑、1,643 正常 | CC-BY-NC-SA-4.0 | 独立条件式 Release；仅限非商业并遵守相同方式共享 |
| `skillbench_1650` | [zenith6888/SkillsBench-1650](https://huggingface.co/datasets/zenith6888/SkillsBench-1650) | 带脚本内容和难度标签的风险评分数据集，包含合成恶意样本及较大规模良性对照，适合分数校准和难例评测。 | 1,500 良性、150 合成恶意 | CC-BY-4.0 | 完整 Release |
| `agent_skill_malware` | [yoonholee/agent-skill-malware](https://huggingface.co/datasets/yoonholee/agent-skill-malware) | 来自真实恶意活动和良性对照的去重 `SKILL.md` 文本，规模小但接近实际攻击，可用于二分类回归测试。 | 347 条：124 恶意、223 良性 | MIT | 完整 Release |
| `atr_skill_benchmark` | [Agent-Threat-Rule/atr-skill-benchmark](https://huggingface.co/datasets/Agent-Threat-Rule/atr-skill-benchmark) | 强调检测精度和困难负样本的基准，恶意样本较少、良性对照较多，适合检查规则过度匹配和误报。 | 498 条：32 恶意、466 良性 | MIT | 完整 Release |
| `skillguard_v2` | [ZAHRA585/skillguard-v2-dataset](https://huggingface.co/datasets/ZAHRA585/skillguard-v2-dataset) | Skill 形态与通用提示词注入训练辅助数据，适合补充提示词攻击覆盖；不应当直接等同于恶意 Skill 包真值。 | 5 个 Parquet 分片；攻击/良性标签 | Apache-2.0 | 完整 Release，但与包级恶意检测结果分开统计 |
| `skillleakbench` | [AgentSkillPrivacy/SkillLeakBench](https://huggingface.co/datasets/AgentSkillPrivacy/SkillLeakBench) | Agent Skill 凭据泄露和不安全实现问题的去标识化元数据，适合检测硬编码凭据、隐私泄露和修复覆盖。 | 520 个受影响 Skill、1,708 个问题；恶意/脆弱标签 | MIT | 完整 Release；主要是元数据而非 Skill 全文 |
| `skilllifebench` | [SkillLifeBench2026/SkillLifeBench](https://huggingface.co/datasets/SkillLifeBench2026/SkillLifeBench) | 覆盖 Skill 生命周期、结构化注册信息、注释、模式和漏洞场景的基准，适合规则覆盖率与生命周期安全测试。 | 194 条注册记录及结构化场景 | CC-BY-4.0 | 完整 Release |

每个数据集的固定提交、字节数、文件数、入口数量及详细分发边界可在 [`datasets/`](datasets/) 和 [`catalog.json`](catalog.json) 中查看。

## 如何使用

### 1. 克隆并检查目录

```bash
git clone https://github.com/daffnjk/agent-skill-security-datasets.git
cd agent-skill-security-datasets
python3 scripts/validate_catalog.py
```

这一步只校验目录结构、来源记录、标签映射和 Release 清单，不会下载或执行样本。

### 2. 下载一个可以再分发的数据集

```bash
python3 scripts/fetch_release.py \
  --dataset agent_skill_malware \
  --output ./downloads
```

脚本会从本项目的对应 GitHub Release 下载资产，并按照 [`manifests/SHA256SUMS-2026-08-30.txt`](manifests/SHA256SUMS-2026-08-30.txt) 中的值验证 SHA-256。

可下载的数据集 ID：

```text
malicious_agent_skills_bench
malicious_skill_bench_hf
skilltrustbench
skillbench_1650
agent_skill_malware
atr_skill_benchmark
skillguard_v2
skillleakbench
skilllifebench
```

### 3. 获取仅索引的数据集

`malicious_skill_bench`、`malskillbench`、`overtly_malicious_skills` 和 `agenttrap` 不在本项目重新托管样本。请打开对应数据集卡片，按上游地址获取，并切换到 [`manifests/source-revisions.tsv`](manifests/source-revisions.tsv) 记录的固定提交。

### 4. 接入检测器

我建议把下载目录作为检测器的纯数据输入，而不是 Agent 的 Skill 安装目录。至少记录以下字段：

- 检测器名称和版本；
- 数据集 ID 与上游固定版本；
- 官方 split 或自定义划分方式；
- 上游原始标签和规范化标签；
- 真阳性、假阳性、真阴性和假阴性；
- 无法解析、超时或跳过的样本数量。

不要只报告一个跨数据集汇总分数。不同数据集衡量的是静态恶意行为、运行时攻击、提示词注入、凭据泄露或漏洞场景，应该分别报告结果。

## 标签使用原则

我保留上游标签，并在 [`manifests/label-map.csv`](manifests/label-map.csv) 中提供统一映射：

- `malicious`：可作为恶意检测的正样本；
- `suspicious`：只用于待研判队列，不能直接当作已确认恶意；
- `vulnerable`：表示实现存在安全缺陷，不代表作者具有恶意意图；
- `adversarial_prompt`：用于提示词注入辅助覆盖，不等同于包级恶意样本；
- `benign`、`safe`、`normal`：用于评估误报率。

## 安全使用

静态检测场景请参考 [`docs/SAFE_USAGE.md`](docs/SAFE_USAGE.md)。如果确实需要动态执行，应使用一次性、断网、无凭据、无宿主机可写挂载的隔离环境，并设置资源与超时限制。

## 许可证和再分发

本仓库中由我编写的目录、说明和工具脚本使用 MIT License。每个上游数据集继续适用其自己的许可证和署名要求；我没有对第三方数据重新授权。

详细规则见 [`docs/REDISTRIBUTION.md`](docs/REDISTRIBUTION.md) 和 [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md)。如果你发现许可证、来源或归属记录有误，请按 [`SECURITY.md`](SECURITY.md) 中的方式联系我。

## 引用

如果你在论文、报告或产品评测中使用这个目录，请同时引用本项目和你实际使用的上游数据集。机器可读引用信息见 [`CITATION.cff`](CITATION.cff)。

