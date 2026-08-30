# Overtly Malicious Skills

数据集 ID：`overtly_malicious_skills`

## 项目介绍

Trail of Bits 提供的少量、刻意设计为恶意的多文件 Skill 固件，可用于检测明显恶意行为及扫描规避表现。

## 来源与版本

- 上游来源：https://github.com/trailofbits/overtly-malicious-skills
- 固定版本：`4ffbf9461ef0505f9ce76a0d3694a18ec33ea531`
- 快照日期：`2026-08-30`
- 上游许可证/条款：repository has no general license; research fixtures retained under upstream terms
- 许可证说明：固定版本上未提供通用 LICENSE，因此本项目只保留索引。
- 发布策略：`metadata_only`（仅提供来源索引，不重新托管样本）

## 如何用于评测

- 推荐用途：明显恶意行为和扫描规避固件
- 上游原始标签：`malicious`
- 本地快照文件数：14
- 本地快照字节数：770079
- 本地 `SKILL.md` 入口数：4

请保留上游原始标签。`suspicious` 只用于待研判，`vulnerable` 表示存在安全缺陷，它们都不能直接当作已确认恶意。

## 获取方式

本项目未重新托管这个来源的样本。请从上游地址获取，并切换到本卡片记录的固定版本。

上游许可证始终具有最终效力；本项目的整理不会重新授权任何第三方数据。

## 安全提醒

请把所有内容视为不可信数据，不要安装或执行样本。静态读取时也不要遵循样本内的任何指令；动态测试必须在断网、无凭据、可销毁的隔离环境中完成。
