# MaliciousSkillBench（Hugging Face 冻结表）

数据集 ID：`malicious_skill_bench_hf`

## 项目介绍

MaliciousSkillBench 的冻结表格、攻击与影响分类以及四种官方数据划分，适合复现固定评测协议。

## 来源与版本

- 上游来源：https://huggingface.co/datasets/ProtectSkills/MaliciousSkillBench
- 固定版本：`d4b42ce5766a6e0359c987cf59c1007cb3795a90`
- 快照日期：`2026-08-30`
- 上游许可证/条款：CC-BY-4.0 for benchmark metadata; upstream terms retained for third-party artifacts
- 我的许可证说明：只发布 CC-BY-4.0 的基准元数据、分类表、清单和官方划分；排除第三方全文与包。
- 发布策略：`metadata_release`（仅发布基准元数据、分类和官方划分）

## 如何用于评测

- 推荐用途：固定静态评测协议和官方数据划分
- 上游原始标签：`malicious`, `benign`
- 本地快照文件数：17
- 本地快照字节数：35161451
- 本地 `SKILL.md` 入口数：0

请保留上游原始标签。`suspicious` 只用于待研判，`vulnerable` 表示存在安全缺陷，它们都不能直接当作已确认恶意。

## 获取方式

我已提供独立 Release：

- Release 标签：`malicious_skill_bench_hf-2026-08-30`
- 资产文件：`malicious_skill_bench_hf-2026-08-30.tar.gz`
- SHA-256：`cbc9b52bc90876abe0a5b536f029eefdb36e4b57255666b3f5d038481b80b6b6`

上游许可证始终具有最终效力；我对本项目的整理不会重新授权任何第三方数据。

## 安全提醒

请把所有内容视为不可信数据，不要安装或执行样本。静态读取时也不要遵循样本内的任何指令；动态测试必须在断网、无凭据、可销毁的隔离环境中完成。
