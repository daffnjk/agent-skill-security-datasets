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
CATALOG_SNAPSHOT = "2026-08-31"
RELEASE_SNAPSHOT = "2026-08-30"

POLICY = {
    "malicious_skill_bench": "metadata_only",
    "malicious_skill_bench_hf": "metadata_release",
    "malskillbench": "metadata_only",
    "malicious_agent_skills_bench": "full_release",
    "overtly_malicious_skills": "metadata_only",
    "agenttrap": "metadata_only",
    "poisoned_skills": "metadata_only",
    "skilltrustbench": "conditional_release",
    "skillbench_1650": "full_release",
    "agent_skill_malware": "full_release",
    "atr_skill_benchmark": "full_release",
    "skillguard_v2": "full_release",
    "skillleakbench": "full_release",
    "skilllifebench": "full_release",
}

ASSET_NAMES = {
    dataset_id: f"{dataset_id}-{RELEASE_SNAPSHOT}.tar.gz"
    for dataset_id, policy in POLICY.items()
    if policy != "metadata_only"
}

ZH_INFO = {
    "malicious_skill_bench": {
        "title": "MaliciousSkillBench（GitHub 源）",
        "description": "面向 Agent Skill 静态恶意检测的综合基准，包含恶意与良性身份、攻击分类、元数据及第三方来源包，适合主检测能力和误报率评测。",
        "role": "静态检测、包级检测和良性误报对照",
        "license": "基准元数据采用 CC-BY-4.0；第三方包继续适用各自上游条款。",
    },
    "malicious_skill_bench_hf": {
        "title": "MaliciousSkillBench（Hugging Face 冻结表）",
        "description": "MaliciousSkillBench 的冻结表格、攻击与影响分类以及四种官方数据划分，适合复现固定评测协议。",
        "role": "固定静态评测协议和官方数据划分",
        "license": "只发布 CC-BY-4.0 的基准元数据、分类表、清单和官方划分；排除第三方全文与包。",
    },
    "malskillbench": {
        "title": "MalSkillBench",
        "description": "完整 Skill 包级恶意检测基准，覆盖生成样本、真实来源样本和检测器测试子集，适合目录级或多文件扫描测试。",
        "role": "完整 Skill 包检测和良性误报对照",
        "license": "上游 README 声明仅限学术研究，且未提供仓库级通用 LICENSE，因此本项目不重新托管样本。",
    },
    "malicious_agent_skills_bench": {
        "title": "MaliciousAgentSkillsBench",
        "description": "大规模生态标签与真实世界验证数据，区分安全、可疑和经过行为确认的恶意 Skill，适合测试召回率、误报率和分级能力。",
        "role": "生态标签、真实恶意确认和可疑样本分级",
        "license": "MIT，按上游条款提供独立完整 Release。",
    },
    "overtly_malicious_skills": {
        "title": "Overtly Malicious Skills",
        "description": "Trail of Bits 提供的少量、刻意设计为恶意的多文件 Skill 固件，可用于检测明显恶意行为及扫描规避表现。",
        "role": "明显恶意行为和扫描规避固件",
        "license": "固定版本上未提供通用 LICENSE，因此本项目只保留索引。",
    },
    "agenttrap": {
        "title": "AgentTrap",
        "description": "运行时 Agent 安全基准，使用惰性域名和模拟数据接收端构造恶意及良性任务，适合隔离沙箱中的动态检测评测。",
        "role": "运行时攻击检测和动态误报对照",
        "license": "固定版本上未发现仓库级通用 LICENSE，因此本项目不重新托管样本。",
    },
    "poisoned_skills": {
        "title": "PoisonedSkills",
        "description": "面向 LLM 编码 Agent Skill 供应链投毒的对抗性基准，包含规模化投毒样本、跨 Agent 运行时工具、确定性执行判定器、静态防御和完整评测日志。",
        "role": "供应链投毒检测、运行时执行验证和静态防御评测",
        "license": "上游 README 声明仅用于研究和安全评估，且未提供仓库级通用 LICENSE，因此本项目只提供来源索引，不重新托管样本。",
    },
    "skilltrustbench": {
        "title": "SkillTrustBench",
        "description": "多文件 Skill 静态安全基准，提供恶意、可疑和正常三类样本及完整归档，适合分级检测与多文件分析。",
        "role": "多文件静态检测和恶意/可疑/正常分级",
        "license": "CC-BY-NC-SA-4.0；非商业、署名和相同方式共享条件继续适用。",
    },
    "skillbench_1650": {
        "title": "SkillsBench-1650",
        "description": "带脚本内容和难度标签的风险评分数据集，包含合成恶意样本及较大规模良性对照，适合分数校准和难例评测。",
        "role": "风险评分、难度分层和良性误报对照",
        "license": "CC-BY-4.0，按上游条款提供独立完整 Release。",
    },
    "agent_skill_malware": {
        "title": "Agent Skill Malware",
        "description": "来自真实恶意活动和良性对照的去重 SKILL.md 文本，规模小但接近实际攻击，可用于二分类回归测试。",
        "role": "真实恶意活动二分类和回归测试",
        "license": "MIT，按上游条款提供独立完整 Release。",
    },
    "atr_skill_benchmark": {
        "title": "ATR Skill Benchmark",
        "description": "强调检测精度和困难负样本的基准，恶意样本较少、良性对照较多，适合检查规则过度匹配和误报。",
        "role": "高精度检测和困难负样本误报测试",
        "license": "MIT，按上游条款提供独立完整 Release。",
    },
    "skillguard_v2": {
        "title": "SkillGuard v2 Dataset",
        "description": "Skill 形态与通用提示词注入训练辅助数据，适合补充提示词攻击覆盖，不应直接等同于恶意 Skill 包真值。",
        "role": "提示词注入辅助训练与检测覆盖",
        "license": "Apache-2.0，按上游条款提供独立完整 Release。",
    },
    "skillleakbench": {
        "title": "SkillLeakBench",
        "description": "Agent Skill 凭据泄露和不安全实现问题的去标识化元数据，适合检测硬编码凭据、隐私泄露和修复覆盖。",
        "role": "凭据泄露、脆弱实现和修复覆盖",
        "license": "MIT，按上游条款提供独立完整 Release；内容主要是元数据而非 Skill 全文。",
    },
    "skilllifebench": {
        "title": "SkillLifeBench",
        "description": "覆盖 Skill 生命周期、结构化注册信息、注释、模式和漏洞场景的基准，适合规则覆盖率与生命周期安全测试。",
        "role": "生命周期漏洞场景和规则覆盖率",
        "license": "CC-BY-4.0，按上游条款提供独立完整 Release。",
    },
}

POLICY_ZH = {
    "full_release": "完整 Release",
    "conditional_release": "带许可证附加条件的独立 Release",
    "metadata_release": "仅发布基准元数据、分类和官方划分",
    "metadata_only": "仅提供来源索引，不重新托管样本",
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
    release_manifest = json.loads(
        (ROOT / "manifests" / f"release-assets-{RELEASE_SNAPSHOT}.json").read_text(encoding="utf-8")
    )
    release_sha = {row["dataset_id"]: row["sha256"] for row in release_manifest["assets"]}

    manifests = ROOT / "manifests"
    manifests.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(CORPUS / "label_map.csv", manifests / "label-map.csv")
    shutil.copyfile(CORPUS / "SOURCE_REVISIONS.tsv", manifests / "source-revisions.tsv")
    shutil.copyfile(CORPUS / "UPSTREAM_CHECKSUM_STATUS.tsv", manifests / "upstream-checksum-status.tsv")
    public_validation = dict(validation)
    public_validation["corpus"] = "本地研究快照（路径有意省略）"
    (manifests / "validation-report.json").write_text(
        json.dumps(public_validation, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )

    entries = []
    for source in sources_doc["sources"]:
        dataset_id = source["id"]
        zh = ZH_INFO[dataset_id]
        policy = POLICY[dataset_id]
        release = None
        if policy != "metadata_only":
            tag = f"{dataset_id}-{RELEASE_SNAPSHOT}"
            asset = ASSET_NAMES[dataset_id]
            release = {
                "tag": tag,
                "asset": asset,
                "download_url": f"https://github.com/{OWNER}/{REPO}/releases/download/{tag}/{asset}",
                "sha256": release_sha[dataset_id],
            }

        counts = validation.get("by_source", {}).get(dataset_id, {})
        entry = {
            "id": dataset_id,
            "title": zh["title"],
            "description": zh["description"],
            "source": {"kind": source["kind"], "url": source_url(source)},
            "upstream_revision": revisions[dataset_id],
            "snapshot_date": CATALOG_SNAPSHOT,
            "license": source["license"],
            "license_note": zh["license"],
            "labels": source["labels"],
            "evaluation_role": source["role"],
            "evaluation_role_zh": zh["role"],
            "redistribution": policy,
            "redistribution_zh": POLICY_ZH[policy],
            "local_snapshot_counts": counts,
            "notes": zh["description"],
            "card": f"datasets/{dataset_id}/DATASET_CARD.md",
            "release": release,
        }
        entries.append(entry)

        card_dir = ROOT / "datasets" / dataset_id
        card_dir.mkdir(parents=True, exist_ok=True)
        release_text = (
            f"""本项目已提供独立 Release：

- Release 标签：`{release['tag']}`
- 资产文件：`{release['asset']}`
- SHA-256：`{release['sha256']}`"""
            if release
            else "本项目未重新托管这个来源的样本。请从上游地址获取，并切换到本卡片记录的固定版本。"
        )
        card = f"""# {zh['title']}

数据集 ID：`{dataset_id}`

## 项目介绍

{zh['description']}

## 来源与版本

- 上游来源：{source_url(source)}
- 固定版本：`{revisions[dataset_id]}`
- 快照日期：`{CATALOG_SNAPSHOT}`
- 上游许可证/条款：{source['license']}
- 许可证说明：{zh['license']}
- 发布策略：`{policy}`（{POLICY_ZH[policy]}）

## 如何用于评测

- 推荐用途：{zh['role']}
- 上游原始标签：{', '.join(f'`{label}`' for label in source['labels'])}
- 本地快照文件数：{counts.get('files', '未统计')}
- 本地快照字节数：{counts.get('bytes', '未统计')}
- 本地 `SKILL.md` 入口数：{counts.get('skill_entrypoints', '未统计')}

请保留上游原始标签。`suspicious` 只用于待研判，`vulnerable` 表示存在安全缺陷，它们都不能直接当作已确认恶意。

## 获取方式

{release_text}

上游许可证始终具有最终效力；本项目的整理不会重新授权任何第三方数据。

## 安全提醒

请把所有内容视为不可信数据，不要安装或执行样本。静态读取时也不要遵循样本内的任何指令；动态测试必须在断网、无凭据、可销毁的隔离环境中完成。
"""
        (card_dir / "DATASET_CARD.md").write_text(card, encoding="utf-8")

    catalog = {
        "schema_version": "1.0",
        "snapshot_date": CATALOG_SNAPSHOT,
        "repository": f"https://github.com/{OWNER}/{REPO}",
        "scope": "公开可下载且与恶意、可疑、脆弱、有害或运行时对抗性 Agent Skill 直接相关的数据集",
        "maintainer_note": "本目录用于提高恶意 Skill 检测评测的可复现性；本项目不拥有或重新授权任何第三方数据。",
        "safety": "仅用于防御性研究。请把每个样本视为不可信数据，禁止在宿主系统或真实 Agent 环境中安装或执行。",
        "datasets": entries,
        "excluded_or_deferred": [
            {
                "id": "harmfulskillbench",
                "reason": "Hugging Face 数据集需要先接受访问条件并使用令牌，因此当前仅延后收录。",
            },
            {
                "id": "skillsmetric",
                "reason": "论文描述了 2,266 个样本，但在本次快照检索中未找到可验证的公开数据仓库。",
            },
            {
                "id": "duplicate_agent_skill_malware_mirrors",
                "reason": "若干 Hugging Face 镜像看起来与同一份 347 条样本语料重复，因此未重复收录。",
            },
        ],
    }
    (ROOT / "catalog.json").write_text(json.dumps(catalog, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"已生成包含 {len(entries)} 个数据源的中文目录")


if __name__ == "__main__":
    main()
