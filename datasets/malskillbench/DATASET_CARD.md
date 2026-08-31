# MalSkillBench

数据集 ID：`malskillbench`

## 项目介绍

完整 Skill 包级恶意检测基准，覆盖生成样本、真实来源样本和检测器测试子集，适合目录级或多文件扫描测试。

## 来源与版本

- 上游来源：https://github.com/lxyeternal/MalSkillBench
- 固定版本：`06e083125d5ec5dd7a189dfedadfe587a70635b9`
- 快照日期：`2026-08-31`
- 上游许可证/条款：Academic research use only (stated in upstream README; no repository-wide license file found)
- 许可证说明：上游 README 声明仅限学术研究，且未提供仓库级通用 LICENSE，因此本项目不重新托管样本。
- 发布策略：`metadata_only`（仅提供来源索引，不重新托管样本）

## 如何用于评测

- 推荐用途：完整 Skill 包检测和良性误报对照
- 上游原始标签：`malicious`, `benign`
- 本地快照文件数：410124
- 本地快照字节数：5608669262
- 本地 `SKILL.md` 入口数：8018

请保留上游原始标签。`suspicious` 只用于待研判，`vulnerable` 表示存在安全缺陷，它们都不能直接当作已确认恶意。

## 获取方式

本项目未重新托管这个来源的样本。请从上游地址获取，并切换到本卡片记录的固定版本。

上游许可证始终具有最终效力；本项目的整理不会重新授权任何第三方数据。

## 安全提醒

请把所有内容视为不可信数据，不要安装或执行样本。静态读取时也不要遵循样本内的任何指令；动态测试必须在断网、无凭据、可销毁的隔离环境中完成。
