# V5 Final Polish Integrity Audit

Branch: `resume/v5-final-polish`  
Base: `resume/v5-grill-complete`

## Audit Goal

验证本轮“中国市场语言统一 + 简历化表达 + 用户新确认评测事实补充”没有通过压缩或改写破坏 V5 原有事实、数字和角色结构。

当前事实源：
- `derived_from_source_epoch`: `FCT-EPOCH-20260920-CF6422BF`
- FACT blob: `cf6422bf96d8b19810b9c2526972ce88dd3af3ba`

## Structural Check

| Role | Lines | Bullets | 原 V5 数字 / 日期 Token |
|---|---:|---:|---|
| R1 | 80 → 82 | 26 → 28 | 无缺失 / 无新增 |
| R2 | 82 → 82 | 28 → 28 | 无缺失 / 无新增 |
| R3 | 75 → 75 | 25 → 25 | 无缺失 / 无新增 |
| R4 | 81 → 81 | 27 → 27 | 无缺失 / 无新增 |
| R5 | 79 → 79 | 25 → 25 | 无缺失 / 无新增 |
| R6 | 81 → 81 | 27 → 27 | 无缺失 / 无新增 |

R1 bullet 总数保持不变；本轮不再新增结构，而是对现有项目 bullet 做标题与证据密度升级。

当前新增 / 强化的 Eval 证据：
- 30-case Safety / 100-case Robustness / 60-case Blind Holdout；
- S1 Thin Evaluation Harness / Run Integrity；
- Tool Use / Durable Action Acceptance；
- Quality Gate / Version Decision；
- 保留开放题高低分答案、Layer / Path 与结构化 Trace / 轨迹评测。

其中开放题 / Trace 来自用户确认事实；Harness / Holdout / Durable Acceptance / Quality Gate 来自 `-agent` 当前 main 的 repo verification，不是从 JD 或第三方 Skill 推导。

## Fact Governance Delta

本轮已按顺序更新：
1. `FACT_MASTER_CURRENT.md`：保留 FCTM-RR-24~27，并新增 / 更新 FCTM-AG-00、FCTM-AG-04、FCTM-AG-10~12；
2. `CLAIM_LEDGER.md`：更新 FCT-24 / FCT-27，新增 FCT-65~67，并绑定 `FCT-EPOCH-20260920-CF6422BF`；
3. R1：吸收可直接对外表达的 Holdout / Harness / Action Acceptance / Quality Gate，并将项目 bullet 标题改为 JD / HR 扫描词；
4. ONLINE-MAIN：只保留高密度的 Agent Eval / Regression 表达，不堆完整工程数字；
5. Langfuse 保持边界：当前只确认方法用途，**未写成已实际接入 / 已搭建平台**。

## Language / Reading-Cost Check

统一执行：
- 中文 JD 常用词优先；
- FDE、AI 评测保持第一视觉；
- POC / RAG / Agent / API 等通用关键词保留；
- Bullet 标题只承担 JD 命中与 HR 扫描，不承担完整 reasoning；
- R1 项目标题已收敛为 Eval Dataset、Negative Cases、Regression / Holdout、Tool Use / Action Acceptance、Trace / Trajectory Eval、Eval Harness / Run Integrity、Quality Gate / Version Decision；
- “真实”仅在第一次需要区分 Demo / 模拟环境时使用，后续改为门店流程、Case、反馈、状态等具体业务词；
- 事实边界尽量压缩为“已验证 X；Y 待验证”，不写成长篇防御句。

## Guardrail Check

继续保持：
- 微信部署 ≠ 企业微信 / 全渠道部署；
- 门店 POC / 开始实际使用 ≠ 长期客户成功 / 付费 / ROI / 规模化；
- 团队结果与个人贡献分开；
- 正式 PRD 未完成时不写成已完成；
- R5 不升级为纯 SWE / 生产级工程履历；
- R6 不升级为企业采购 / 销售成交履历；
- 结构化 Trace 中的“规划 / 决策节点”不表述为模型私有思维链；
- 未确认实际接入 Langfuse 前，不写“使用 Langfuse 搭建评测平台”。

## Unchanged Governance Assets

未修改：
- `CURRENT_VERSION_INDEX.md`；
- 冻结 V4；
- 历史 V5 / V6；
- 工作时间；
- 正式职位名称；
- 原有 GMV / 任务规模 / 一致性 / POC 数字事实。

## Semantic Claim Re-check

本轮 R1 / ONLINE-MAIN 语义变更已逐项回指当前 Claim Ledger：
- Open-ended / Path Eval → FCT-61；
- Trace / Trajectory Eval → FCT-62 / FCT-63；
- 分层 Eval / 100-case Robustness / 60-case Blind Holdout → FCT-27；
- Eval Harness / Run Integrity → FCT-65；
- Tool Use / Action Acceptance → FCT-66；
- Quality Gate / Version Decision → FCT-67；
- 微信部署 / 门店 POC / 使用反馈 → FCT-58 / FCT-60。

未增加未经事实 / repo 证据支持的新 ownership、生产、商业或 Langfuse 落地主张。

## New / Updated Derived Assets

- `CHINA-JD-TERMINOLOGY.md`
- `ONLINE-MAIN/ONLINE-MAIN.RESUME.md`
- `R1-Agent-Eval/R1-Agent-Eval.RESUME.md`
- `V5-FINAL-POLISH-MANIFEST.md`
- `V5-FINAL-FULLTEXT.md`

ONLINE-MAIN 仍是派生在线主简历，不替代 R1–R6。
