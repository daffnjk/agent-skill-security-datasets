# PoisonedSkills

数据集 ID：`poisoned_skills`

## 项目介绍

面向 LLM 编码 Agent Skill 供应链投毒的对抗性基准，包含规模化投毒样本、跨 Agent 运行时工具、确定性执行判定器、静态防御和完整评测日志。

## 来源与版本

- 上游来源：https://github.com/qyb156/PoisonedSkills
- 固定版本：`5068b39ff85c5e9a3afdb856a53b85867043c923`
- 快照日期：`2026-08-31`
- 上游许可证/条款：Research purposes only (stated in upstream README; no repository-wide license file found)
- 许可证说明：上游 README 声明仅用于研究和安全评估，且未提供仓库级通用 LICENSE，因此本项目只提供来源索引，不重新托管样本。
- 发布策略：`metadata_only`（仅提供来源索引，不重新托管样本）

## 如何用于评测

- 推荐用途：供应链投毒检测、运行时执行验证和静态防御评测
- 上游原始标签：`adversarial`
- 本地快照文件数：未统计
- 本地快照字节数：未统计
- 本地 `SKILL.md` 入口数：未统计

请保留上游原始标签。`suspicious` 只用于待研判，`vulnerable` 表示存在安全缺陷，它们都不能直接当作已确认恶意。

## 获取方式

本项目未重新托管这个来源的样本。请从上游地址获取，并切换到本卡片记录的固定版本。

上游许可证始终具有最终效力；本项目的整理不会重新授权任何第三方数据。

## 安全提醒

请把所有内容视为不可信数据，不要安装或执行样本。静态读取时也不要遵循样本内的任何指令；动态测试必须在断网、无凭据、可销毁的隔离环境中完成。
