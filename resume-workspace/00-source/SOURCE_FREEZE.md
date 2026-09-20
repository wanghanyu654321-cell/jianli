# Source Freeze

## Current working-candidate fact-master epoch

- Source ID: `FCT-001`
- Current GitHub mirror: `resume-workspace/01-facts/FACT_MASTER_CURRENT.md`
- Source epoch: `FCT-EPOCH-20260920-02A48ED2`
- Git blob SHA: `02a48ed2191ba2dbf2245be9e1d29bdcdab72a3e`
- Freeze date: `2026-09-20`
- Candidate source currency: `CURRENT`
- Promotion state: `NEWER_UNPROMOTED_CANDIDATE`

This file describes the **working candidate source freeze on `resume/v5-final-polish`**. It does not promote the candidate into the canonical registry. `CURRENT_VERSION_INDEX.md` / `GATE_REGISTRY.json` remain the authority for the last explicitly promoted canonical state until the user authorizes promotion.

## Freeze basis

本 epoch 只冻结以下范围：

1. 当前主线中已经确认并持续使用的事实；
2. 用户对朗臻、今宜、人瑞补充和确认的工作上下文、判断逻辑与责任边界；
3. 真实 JD 能力缺口核对后明确确认的评测类目、Badcase 分类、复测、多轮 / Tool / Step / 信息完整性评测、基础 SQL / 查询取数、评测资产、Prompt / System / Tool Instruction、项目排期与方案汇报；
4. 当前主线 Agent Builder 项目的既有事实与部分仓库核验结果；
5. 用户最新明确确认的 Agent 项目交付状态：已完成微信部署、实体本地生活门店 POC，并开始在接待场景中实际使用；长期稳定性、持续付费、业务 ROI、规模化与 Production SLA 仍未确认；
6. 用户最新明确确认的 Agent Eval 方法：开放题高分 / 低分答案与 Layer / Path 对比、结构化 Trace / 轨迹评测、运行指标与过程评测分层；Langfuse 当前仅确认方法用途，不写成已实际接入。

明确不采用“旧仓库 / 旧 Claim / 旧快照出现过就自动恢复”的策略。未被当前主线使用、且本轮未明确要求恢复的历史旁支内容，不进入当前事实母版。

本地 `简历母版.docx` 与 GitHub mirror 如存在差异，不自动互相覆盖；后续同步前先以用户最新明确确认的事实校准。

## Previous epochs

### Immediate working-candidate predecessor
- Epoch: `FCT-EPOCH-20260920-CF6422BF`
- Git blob SHA: `cf6422bf96d8b19810b9c2526972ce88dd3af3ba`
- Status: `SUPERSEDED_BY_JINYI_TITLE_NORMALIZATION`
- Reason: 用户明确要求杭州今宜职位统一对外显示为“抖音项目代运营”；BD / 项目推进仍保留为职责证据，不再并列进职位标题。

### Earlier working-candidate predecessor
- Epoch: `FCT-EPOCH-20260920-DE68CC7D`
- Git blob SHA: `de68cc7d3ca981e411864f4968300c5056247f6d`
- Status: `SUPERSEDED_BY_LATEST_REPO_EVAL_VERIFICATION`
- Reason: 重新核验 `-agent` 当前 main 后，修正项目 repo ref、确认 100-case robustness / 60-case blind holdout，并新增 Thin Evaluation Harness / Run Integrity / Durable Acceptance / Quality Gate 工程证据。

### Earlier working-candidate predecessor
- Epoch: `FCT-EPOCH-20260916-FE4CB619`
- Git blob SHA: `fe4cb619cccf99f98813f7dec683b8022ff4f2e5`
- Status: `SUPERSEDED_BY_20260920_CONFIRMED_DELIVERY_AND_EVAL_FACTS`
- Reason: 用户进一步确认微信部署 / 门店 POC / 开始实际使用，并补充开放题与轨迹评测方法；新事实先进入 FACT MASTER / CLAIM LEDGER，再进入 ONLINE-MAIN / R1。

### Earlier repository predecessor
- Epoch: `FCT-EPOCH-20260916-04094915`
- Git blob SHA: `040949158e76a356caf81f4185da2c4a17528e04`
- Status: `SUPERSEDED_BY_AGENT_DELIVERY_STATUS_UPDATE`
- Reason: 用户进一步确认当前 Agent 项目不是只用于 Portfolio 展示，而是基于实际落地目标推进，已有 Demo / POC 交付并处于上线准备阶段。

### Earlier repository epoch
- Epoch: `FCT-EPOCH-20260916-6D82DB08`
- Git blob SHA: `6d82db084b0bef7ec1967982ebb36213942fd571`
- Status: `SUPERSEDED_BY_JD_EVIDENCE_ENRICHMENT`

### Earlier repository epoch
- Epoch: `FCT-EPOCH-20260916-D0C724C3`
- Status: `SUPERSEDED_BY_SCOPE_CLEANUP`

### External DOCX fingerprint before GitHub context supplement
- Epoch: `FCT-EPOCH-20260915-38A34FF8`
- SHA256: `38A34FF8CF39A4D69AF20FD043C170D15A8DD0A882A8414A5311CF0FE52E140C`

### Earlier repository freeze
- Epoch: `FCT-EPOCH-20260913-7EAA096A`
- SHA256: `7EAA096A7220DE0609E3AACAEA656B4CEEFB006D1419FA01BC07E97FFFCDDDEB`
- Status: `SUPERSEDED`

## Semantic delta in current epoch

相对 `FCT-EPOCH-20260920-CF6422BF`，本次事实层只发生一项用户明确确认的职位显示口径变化：

### 杭州今宜职位显示
- 对外职位统一为：`杭州今宜商贸有限公司｜抖音项目代运营｜2024.11–2025.07`；
- 项目经营、直播、内容、投流、店铺数据、达人 BD、项目排期和合作方汇报等实际职责继续保留；
- BD 仍可作为 MaaS / AI 交付方向的 transferable evidence；
- 不再将“项目运营 / BD”并列写入职位标题；
- 不因为保留 BD 职责而升级为 AI 售前、商业成交或客户采购经历。

Agent delivery / Eval / Harness / CI 等事实相对上一 epoch 无新增事实，只发生 recruiter-facing 表达优化。

## Downstream state

- `CLAIM_LEDGER.md`: 已重新对齐到 `FCT-EPOCH-20260920-02A48ED2`；既有 Harness / Holdout / Durable Acceptance / Quality Gate 证据保持不变，并新增今宜职位统一显示边界。
- `ONLINE-MAIN` / R1：已吸收当前可对外表达的交付与 Eval 事实。
- R2–R6：保持既有角色差异，不因本次文档消歧或 R1 Eval 增强而重构。
- `CANONICAL_TIMELINE.md`: 未变化；Timeline Gate 保持 PASS。
- `CURRENT_VERSION_INDEX.md` / `GATE_REGISTRY.json`: **本 working-candidate 阶段故意不修改**；等待用户明确 canonical promotion。
- `APPLICATION_READY = NO`；当前仍处于 10 秒 HR 审计后的用户复核 / 修订阶段，BossHunter 优化尚未开始，必须等待用户确认简历版本。

## Rebase contract

以后任何事实语义变化：
1. 先确认是否属于当前主线或用户明确新增内容；
2. 未确认的历史旁支不得自动恢复；
3. 用户明确确认后更新 `FACT_MASTER_CURRENT.md`；
4. 创建新 Source Epoch；
5. 做 semantic delta；
6. 更新受影响 Claim Ledger；
7. 重验受影响 Resume artifact；
8. 刷新 working-candidate Manifest / Audit；只有在用户明确授权 canonical promotion 后，才更新 `CURRENT_VERSION_INDEX.md` 和 `GATE_REGISTRY.json`。
