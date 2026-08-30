# MaliciousAgentSkillsBench

数据集 ID：`malicious_agent_skills_bench`

## 项目介绍

大规模生态标签与真实世界验证数据，区分安全、可疑和经过行为确认的恶意 Skill，适合测试召回率、误报率和分级能力。

## 来源与版本

- 上游来源：https://github.com/protectskills/MaliciousAgentSkillsBench
- 固定版本：`f7d28b1a9de4eb33d552529cf79d1065d765f6c3`
- 快照日期：`2026-08-30`
- 上游许可证/条款：MIT
- 许可证说明：MIT，按上游条款提供独立完整 Release。
- 发布策略：`full_release`（完整 Release）

## 如何用于评测

- 推荐用途：生态标签、真实恶意确认和可疑样本分级
- 上游原始标签：`safe`, `suspicious`, `malicious`
- 本地快照文件数：116
- 本地快照字节数：11884269
- 本地 `SKILL.md` 入口数：1

请保留上游原始标签。`suspicious` 只用于待研判，`vulnerable` 表示存在安全缺陷，它们都不能直接当作已确认恶意。

## 获取方式

本项目已提供独立 Release：

- Release 标签：`malicious_agent_skills_bench-2026-08-30`
- 资产文件：`malicious_agent_skills_bench-2026-08-30.tar.gz`
- SHA-256：`fc6a587a7019e57737610f75662ac53bf74d134b070c6e8628c01e2d73b1a882`

上游许可证始终具有最终效力；本项目的整理不会重新授权任何第三方数据。

## 安全提醒

请把所有内容视为不可信数据，不要安装或执行样本。静态读取时也不要遵循样本内的任何指令；动态测试必须在断网、无凭据、可销毁的隔离环境中完成。
