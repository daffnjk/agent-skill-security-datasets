# SkillGuard v2 Dataset

数据集 ID：`skillguard_v2`

## 项目介绍

Skill 形态与通用提示词注入训练辅助数据，适合补充提示词攻击覆盖，不应直接等同于恶意 Skill 包真值。

## 来源与版本

- 上游来源：https://huggingface.co/datasets/ZAHRA585/skillguard-v2-dataset
- 固定版本：`da925f6977ae4201906b441b75f9e5a0194acd76`
- 快照日期：`2026-08-30`
- 上游许可证/条款：Apache-2.0
- 许可证说明：Apache-2.0，按上游条款提供独立完整 Release。
- 发布策略：`full_release`（完整 Release）

## 如何用于评测

- 推荐用途：提示词注入辅助训练与检测覆盖
- 上游原始标签：`attack`, `benign`
- 本地快照文件数：6
- 本地快照字节数：72384156
- 本地 `SKILL.md` 入口数：0

请保留上游原始标签。`suspicious` 只用于待研判，`vulnerable` 表示存在安全缺陷，它们都不能直接当作已确认恶意。

## 获取方式

本项目已提供独立 Release：

- Release 标签：`skillguard_v2-2026-08-30`
- 资产文件：`skillguard_v2-2026-08-30.tar.gz`
- SHA-256：`7bf87e251d6e0a0f2763e32d40715e6624985440bf0b8bb07115cbeb74553d1a`

上游许可证始终具有最终效力；本项目的整理不会重新授权任何第三方数据。

## 安全提醒

请把所有内容视为不可信数据，不要安装或执行样本。静态读取时也不要遵循样本内的任何指令；动态测试必须在断网、无凭据、可销毁的隔离环境中完成。
