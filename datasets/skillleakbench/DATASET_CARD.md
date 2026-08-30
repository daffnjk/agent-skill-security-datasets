# SkillLeakBench

数据集 ID：`skillleakbench`

## 项目介绍

Agent Skill 凭据泄露和不安全实现问题的去标识化元数据，适合检测硬编码凭据、隐私泄露和修复覆盖。

## 来源与版本

- 上游来源：https://huggingface.co/datasets/AgentSkillPrivacy/SkillLeakBench
- 固定版本：`8264436a0483e2fc1aed84b80e5fde73ea52c3ca`
- 快照日期：`2026-08-30`
- 上游许可证/条款：MIT
- 许可证说明：MIT，按上游条款提供独立完整 Release；内容主要是元数据而非 Skill 全文。
- 发布策略：`full_release`（完整 Release）

## 如何用于评测

- 推荐用途：凭据泄露、脆弱实现和修复覆盖
- 上游原始标签：`vulnerable`, `malicious`
- 本地快照文件数：5
- 本地快照字节数：184019
- 本地 `SKILL.md` 入口数：0

请保留上游原始标签。`suspicious` 只用于待研判，`vulnerable` 表示存在安全缺陷，它们都不能直接当作已确认恶意。

## 获取方式

本项目已提供独立 Release：

- Release 标签：`skillleakbench-2026-08-30`
- 资产文件：`skillleakbench-2026-08-30.tar.gz`
- SHA-256：`4f9de34d84f975582467e6707e8ee39c692cbe9f8a51f9557fd8fa3131ffb1b2`

上游许可证始终具有最终效力；本项目的整理不会重新授权任何第三方数据。

## 安全提醒

请把所有内容视为不可信数据，不要安装或执行样本。静态读取时也不要遵循样本内的任何指令；动态测试必须在断网、无凭据、可销毁的隔离环境中完成。
