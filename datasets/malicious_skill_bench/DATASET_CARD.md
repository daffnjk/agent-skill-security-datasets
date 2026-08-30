# MaliciousSkillBench（GitHub 源）

数据集 ID：`malicious_skill_bench`

## 项目介绍

面向 Agent Skill 静态恶意检测的综合基准，包含恶意与良性身份、攻击分类、元数据及第三方来源包，适合主检测能力和误报率评测。

## 来源与版本

- 上游来源：https://github.com/ProtectSkills/MaliciousSkillBench
- 固定版本：`893afd609be22a2dfac5a2b94bbebb4eeb99515e`
- 快照日期：`2026-08-30`
- 上游许可证/条款：CC-BY-4.0 for benchmark metadata; upstream terms retained for third-party artifacts
- 我的许可证说明：基准元数据采用 CC-BY-4.0；第三方包继续适用各自上游条款。
- 发布策略：`metadata_only`（仅提供来源索引，不重新托管样本）

## 如何用于评测

- 推荐用途：静态检测、包级检测和良性误报对照
- 上游原始标签：`malicious`, `benign`
- 本地快照文件数：34082
- 本地快照字节数：345281849
- 本地 `SKILL.md` 入口数：7526

请保留上游原始标签。`suspicious` 只用于待研判，`vulnerable` 表示存在安全缺陷，它们都不能直接当作已确认恶意。

## 获取方式

我没有重新托管这个来源的样本。请从上游地址获取，并切换到本卡片记录的固定版本。

上游许可证始终具有最终效力；我对本项目的整理不会重新授权任何第三方数据。

## 安全提醒

请把所有内容视为不可信数据，不要安装或执行样本。静态读取时也不要遵循样本内的任何指令；动态测试必须在断网、无凭据、可销毁的隔离环境中完成。
