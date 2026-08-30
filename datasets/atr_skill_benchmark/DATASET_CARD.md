# ATR Skill Benchmark

数据集 ID：`atr_skill_benchmark`

## 项目介绍

强调检测精度和困难负样本的基准，恶意样本较少、良性对照较多，适合检查规则过度匹配和误报。

## 来源与版本

- 上游来源：https://huggingface.co/datasets/Agent-Threat-Rule/atr-skill-benchmark
- 固定版本：`7219b10d2ac077e3db8c87d43d653a67935cdb5d`
- 快照日期：`2026-08-30`
- 上游许可证/条款：MIT
- 许可证说明：MIT，按上游条款提供独立完整 Release。
- 发布策略：`full_release`（完整 Release）

## 如何用于评测

- 推荐用途：高精度检测和困难负样本误报测试
- 上游原始标签：`malicious`, `benign`
- 本地快照文件数：2
- 本地快照字节数：3872580
- 本地 `SKILL.md` 入口数：0

请保留上游原始标签。`suspicious` 只用于待研判，`vulnerable` 表示存在安全缺陷，它们都不能直接当作已确认恶意。

## 获取方式

本项目已提供独立 Release：

- Release 标签：`atr_skill_benchmark-2026-08-30`
- 资产文件：`atr_skill_benchmark-2026-08-30.tar.gz`
- SHA-256：`2971c42c9d0f9d30b788cf6f9de679f8c27b4e8ff322fc67cd42de47d16b7d81`

上游许可证始终具有最终效力；本项目的整理不会重新授权任何第三方数据。

## 安全提醒

请把所有内容视为不可信数据，不要安装或执行样本。静态读取时也不要遵循样本内的任何指令；动态测试必须在断网、无凭据、可销毁的隔离环境中完成。
