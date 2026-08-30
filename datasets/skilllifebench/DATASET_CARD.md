# SkillLifeBench

数据集 ID：`skilllifebench`

## 项目介绍

覆盖 Skill 生命周期、结构化注册信息、注释、模式和漏洞场景的基准，适合规则覆盖率与生命周期安全测试。

## 来源与版本

- 上游来源：https://huggingface.co/datasets/SkillLifeBench2026/SkillLifeBench
- 固定版本：`55fcf409d643d2740206ce4699b9a81730bce1ad`
- 快照日期：`2026-08-30`
- 上游许可证/条款：CC-BY-4.0
- 我的许可证说明：CC-BY-4.0，按上游条款提供独立完整 Release。
- 发布策略：`full_release`（完整 Release）

## 如何用于评测

- 推荐用途：生命周期漏洞场景和规则覆盖率
- 上游原始标签：`vulnerability_scenario`
- 本地快照文件数：324
- 本地快照字节数：1731026
- 本地 `SKILL.md` 入口数：0

请保留上游原始标签。`suspicious` 只用于待研判，`vulnerable` 表示存在安全缺陷，它们都不能直接当作已确认恶意。

## 获取方式

我已提供独立 Release：

- Release 标签：`skilllifebench-2026-08-30`
- 资产文件：`skilllifebench-2026-08-30.tar.gz`
- SHA-256：`c778b007894e2e4fbda2801eb9a786d9975fb12a025edbf1202089b52ae266bf`

上游许可证始终具有最终效力；我对本项目的整理不会重新授权任何第三方数据。

## 安全提醒

请把所有内容视为不可信数据，不要安装或执行样本。静态读取时也不要遵循样本内的任何指令；动态测试必须在断网、无凭据、可销毁的隔离环境中完成。
