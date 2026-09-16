# Source Freeze

## Current fact-master epoch

- Source ID: `FCT-001`
- Current GitHub mirror: `resume-workspace/01-facts/FACT_MASTER_CURRENT.md`
- Source epoch: `FCT-EPOCH-20260916-FE4CB619`
- Git blob SHA: `fe4cb619cccf99f98813f7dec683b8022ff4f2e5`
- Freeze date: `2026-09-16`
- Source currency: `CURRENT`

## Freeze basis

本 epoch 只冻结以下范围：

1. 当前主线中已经确认并持续使用的事实；
2. 用户对朗臻、今宜、人瑞补充和确认的工作上下文、判断逻辑与责任边界；
3. 真实 JD 能力缺口核对后明确确认的评测类目、Badcase 分类、复测、多轮 / Tool / Step / 信息完整性评测、基础 SQL / 查询取数、评测资产、Prompt / System / Tool Instruction、项目排期与方案汇报；
4. 当前主线 Agent Builder 项目的既有事实与部分仓库核验结果；
5. 用户最新明确确认的 Agent 项目交付状态：基于实际落地目标推进，已形成可运行 Demo，当前进行 Demo / POC 交付与上线前验证，等待 ICP 相关认证手续完成后推进正式上线。

明确不采用“旧仓库 / 旧 Claim / 旧快照出现过就自动恢复”的策略。未被当前主线使用、且本轮未明确要求恢复的历史旁支内容，不进入当前事实母版。

本地 `简历母版.docx` 与 GitHub mirror 如存在差异，不自动互相覆盖；后续同步前先以用户最新明确确认的事实校准。

## Previous epochs

### Immediate repository predecessor
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

相对 `FCT-EPOCH-20260916-04094915`，本次仅新增 / 修正 Agent 项目的交付状态与对应边界：

### Agent Builder
- 用户明确确认项目基于实际落地目标推进，不再只作为 Portfolio / Proof App 解释；
- 已形成可运行 Demo；
- 当前进行 Demo / POC 交付与上线前验证；
- 当前上线阻塞项之一为 ICP 相关认证手续；完成后推进正式上线；
- 可对外使用 `Demo / POC Delivery`、`pre-launch`、`上线准备` 等表述；
- 正式上线前不得写 `production live`、规模化真实用户流量；
- 未确认企业采购、付费客户、售前成交、真实客户生产验收或复杂系统集成时，不自动补充。

### PRD 边界
- 该项目已有真实落地目标、场景、Workflow、Boundary 与 Acceptance Context；
- 正式 PRD 尚未作为已完成并核验资产进入事实母版；
- PRD 真正产出前，不写“已完成 PRD / 负责 PRD 交付”。

### Repository vs current delivery status
- 顶层 README 仍保留 synthetic portfolio / proof application 证据口径；
- 该仓库历史 / 文档口径与用户最新确认的当前交付状态分层记录，不用旧 README 自动覆盖最新确认，也不以最新确认反向伪造仓库证据。

## Downstream state

- `CLAIM_LEDGER.md`: 已重新对齐到 `FCT-EPOCH-20260916-FE4CB619`，新增 Demo / POC / pre-launch 与 PRD pending claims。
- `REQUIREMENT_EVIDENCE_MATRIX.md`: 已更新，Demo / POC 不再作为 R2 / R6 的纯缺口。
- `CANONICAL_TIMELINE.md`: 未变化；Timeline Gate 保持 PASS。
- R1–R6：已创建 V6 recruiter re-audit 版本，重新吸收本 epoch 的项目交付状态。
- `APPLICATION_READY = NO`，直到对应 Single-JD、ATS / Render Gate 完成。

## Rebase contract

以后任何事实语义变化：
1. 先确认是否属于当前主线或用户明确新增内容；
2. 未确认的历史旁支不得自动恢复；
3. 用户明确确认后更新 `FACT_MASTER_CURRENT.md`；
4. 创建新 Source Epoch；
5. 做 semantic delta；
6. 更新受影响 Claim Ledger；
7. 重验受影响 Resume artifact；
8. 刷新 `CURRENT_VERSION_INDEX.md` 和 `GATE_REGISTRY.json`。
