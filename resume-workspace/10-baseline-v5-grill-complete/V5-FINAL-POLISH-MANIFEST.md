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
2. 10 秒 HR / 平台首屏审计（ONLINE-MAIN + R1）：**USER REVIEW / REVISION IN PROGRESS**；
3. BossHunter 优化调用：**BLOCKED UNTIL USER APPROVES RESUME**。

当前 working-candidate source epoch：`FCT-EPOCH-20260920-02A48ED2`。

本轮 10 秒审计只做：
- Bullet 标题改为 JD / HR 扫描词；
- 清理重复“真实”与模型总结腔；
- 将当前 repo 已核验的 Holdout / Eval Harness / Run Integrity / Durable Acceptance / Quality Gate 证据按 Fact → Claim → Resume 顺序进入 R1；
- ONLINE-MAIN 只保留高密度版本，不堆完整工程细节；
- 今宜职位统一显示为“抖音项目代运营”，BD 职责保留在正文；
- R1 项目标题使用实际门店场景 / 问题，不改成方法论标题；
- R1 项目评测 bullet 收敛为 7 个，加入 CI，并同步 ONLINE-MAIN。

Canonical index / registry 暂不修改；只有用户明确授权 promotion 后才进入 canonical 更新。
