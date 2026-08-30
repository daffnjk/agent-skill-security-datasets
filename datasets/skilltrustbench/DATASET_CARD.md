# SkillTrustBench

数据集 ID：`skilltrustbench`

## 项目介绍

多文件 Skill 静态安全基准，提供恶意、可疑和正常三类样本及完整归档，适合分级检测与多文件分析。

## 来源与版本

- 上游来源：https://huggingface.co/datasets/cuhk-zhuque/SkillTrustBench
- 固定版本：`f90517b7058fdcfea89af114c069fbf973f42bc7`
- 快照日期：`2026-08-30`
- 上游许可证/条款：CC-BY-NC-SA-4.0
- 我的许可证说明：CC-BY-NC-SA-4.0；非商业、署名和相同方式共享条件继续适用。
- 发布策略：`conditional_release`（带许可证附加条件的独立 Release）

## 如何用于评测

- 推荐用途：多文件静态检测和恶意/可疑/正常分级
- 上游原始标签：`malicious`, `suspicious`, `normal`
- 本地快照文件数：37727
- 本地快照字节数：341119821
- 本地 `SKILL.md` 入口数：5595

请保留上游原始标签。`suspicious` 只用于待研判，`vulnerable` 表示存在安全缺陷，它们都不能直接当作已确认恶意。

## 获取方式

我已提供独立 Release：

- Release 标签：`skilltrustbench-2026-08-30`
- 资产文件：`skilltrustbench-2026-08-30.tar.gz`
- SHA-256：`a1970087675a6991788c2624eb6101b72445a7c56b3e1720bd2b97f0add6622f`

上游许可证始终具有最终效力；我对本项目的整理不会重新授权任何第三方数据。

## 安全提醒

请把所有内容视为不可信数据，不要安装或执行样本。静态读取时也不要遵循样本内的任何指令；动态测试必须在断网、无凭据、可销毁的隔离环境中完成。
