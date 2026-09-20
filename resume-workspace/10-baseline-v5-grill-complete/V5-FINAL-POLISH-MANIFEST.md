# V5 Final Polish Working Manifest

Status: **WORKING — NON-DESTRUCTIVE FINAL POLISH**

Branch: `resume/v5-final-polish`

Base: `resume/v5-grill-complete`

## Scope

本分支允许以下变化：

1. 中国市场 JD 语言统一；
2. AI 味 / 解释型表达转为简历化表达；
3. 新建长期在线主简历 ONLINE-MAIN；
4. 用户在本轮明确补充的新事实，必须先进入 FACT_MASTER / CLAIM_LEDGER，再进入简历。

## Hard Guardrails

- 不删除 V5 已确认事实。
- 不压缩掉 Problem → Signal → Judgment → Action → Trade-off → Result / Verification。
- 不改变 R1–R6 角色定位和证据权重。
- 不擅自改变工作时间、岗位名称、数字口径和 ownership；用户明确确认的职位显示规范化除外，并必须同步 FACT / CLAIM / Timeline。
- 不把团队结果写成个人结果。
- 不把微信部署写成企业微信 / 全渠道部署。
- 不把门店 POC / 实际使用写成长期客户成功、付费、ROI、规模化或 Production SLA。
- 不因中文化删除重要 ATS / 技术关键词。
- ONLINE-MAIN 为派生版本，不反向替代任何 R1–R6 母版。
- 所有 existing V5 文件在统一修改前必须以 diff 方式逐份审查。

## Current Step

当前顺序已冻结为：

1. 文档歧义修复：**COMPLETE**；
2. R1 已按 V5 完整母版原则重新构建，ONLINE-MAIN 已按同一能力链重新派生：**USER REVIEW IN PROGRESS**；
3. BossHunter 优化调用：**BLOCKED UNTIL USER APPROVES RESUME**。

当前 working-candidate source epoch：`FCT-EPOCH-20260920-2EDBC835`。

本轮 10 秒审计只做：
- Bullet 标题改为 JD / HR 扫描词；
- 清理重复“真实”与模型总结腔；
- 将当前 repo 已核验的 Holdout / Eval Harness / Run Integrity / Durable Acceptance / Quality Gate 证据按 Fact → Claim → Resume 顺序进入 R1；
- ONLINE-MAIN 只保留高密度版本，不堆完整工程细节；
- 今宜职位统一显示为“抖音项目代运营”，BD 职责保留在正文；
- R1 项目标题使用实际门店场景 / 问题，不改成方法论标题；
- R1 项目评测 bullet 保持 7 个高价值证据，标题进一步改为评测集设计 / 边界测试 / Bad Case / 版本回归 / Tool Use / 执行轨迹分析 / 自动化回归与 CI；
- R1 电商经历只保留与 Query、数据诊断、验证方法和 0→1 结果最相关的 6 条；
- ONLINE-MAIN 核心能力拆分正式工作证据与个人 Agent 项目证据；
- 人瑞正式职位统一恢复为“评测专家（淘天 Data Agent）”；
- 数字前台明确标识为个人 Agent 项目；
- `Search / Query Intent` 已从 R1 recruiter-facing 表达中移除。

Canonical index / registry 暂不修改；只有用户明确授权 promotion 后才进入 canonical 更新。


## R1 Core Evidence Anchors

后续任何 R1 压缩不得删除以下五类核心价值：评测、沟通、协调、管理、两段 0→1 结果。
朗臻“牙膏电商运营 → 宠物项目运营管理”的成长路径属于高价值主证据，不是可选背景信息。


## New-Media Evidence Anchor

朗臻宠物项目中的“小红书策略 / 新媒体运营”属于 R1 高价值证据：策略、流程、约 5 人团队协同、内容测试、有效 / 爆文方向验证与复刻迭代不得因 10 秒压缩被删除。


## Current R1 Review State

- `R1_REBUILT_FROM_V5_BASELINE = YES`
- `R1_USER_APPROVED = NO`
- `ONLINE_NARRATIVE_RESYNC = COMPLETE_PENDING_USER_REVIEW`
- `BOSSHUNTER = BLOCKED`

当前不得继续用 10 秒审计名义压缩 R1 核心职业证据。
