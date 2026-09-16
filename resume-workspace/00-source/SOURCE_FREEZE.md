# Source Freeze

## Current fact-master epoch

- Source ID: `FCT-001`
- Current GitHub mirror: `resume-workspace/01-facts/FACT_MASTER_CURRENT.md`
- Source epoch: `FCT-EPOCH-20260916-6D82DB08`
- Git blob SHA: `6d82db084b0bef7ec1967982ebb36213942fd571`
- Freeze date: `2026-09-16`
- Source currency: `CURRENT`

## Freeze basis

本 epoch 只冻结以下范围：

1. 当前主线中已经确认并持续使用的事实；
2. 用户在 2026-09-16 对朗臻、今宜、人瑞新增上下文和责任边界的明确确认；
3. 当前主线 Agent Builder 项目的既有事实与证据边界；
4. 用户明确要求补入 GitHub 的工作逻辑与事实边界。

明确不采用“旧仓库 / 旧 Claim / 旧快照出现过就自动恢复”的策略。未被当前主线使用、且本轮未明确要求恢复的历史旁支内容，不进入当前事实母版。

本地 `简历母版.docx` 与 GitHub mirror 如存在差异，不自动互相覆盖；后续同步前先以用户最新明确确认的事实校准。

## Previous epochs

### Immediate repository predecessor
- Epoch: `FCT-EPOCH-20260916-D0C724C3`
- Status: `SUPERSEDED_BY_SCOPE_CLEANUP`
- Reason: 首次 GitHub 母版迁移时混入了旧快照范围假设和未在本轮确认的旁支 exclusion；本 epoch 已清理。

### External DOCX fingerprint before GitHub context supplement
- Epoch: `FCT-EPOCH-20260915-38A34FF8`
- SHA256: `38A34FF8CF39A4D69AF20FD043C170D15A8DD0A882A8414A5311CF0FE52E140C`
- Note: 包含已确认的 `单月达人合作销售额合计 10 万元+` 口径；2026-09-16 又补充了大量工作上下文。

### Earlier repository freeze
- Epoch: `FCT-EPOCH-20260913-7EAA096A`
- SHA256: `7EAA096A7220DE0609E3AACAEA656B4CEEFB006D1419FA01BC07E97FFFCDDDEB`
- Status: `SUPERSEDED`

## Semantic delta in current epoch

相对上一 GitHub mirror，本次清理 / 恢复：

- 删除未在本轮确认、仅从旧历史备注带入的今宜未归属 `618 当天约 23 万 / 日常单日约 8 万` exclusion；
- 当前 Fact Master 不包含水果生鲜创业项目、悦客 AI Coach、九米六业务等未要求进入当前主线的历史旁支；
- 移除事实母版中的 Role Baseline 写作政策段，写作政策继续由 `ROLE_BASELINE_WRITING_MODULE.md` 管理；
- 恢复当前主线原本就存在但首次迁移时遗漏的事实：朗臻实时经营数据、预算分配 / 生命周期推进；今宜巨量千川、店铺评分与流量/营销/交易数据及推广 / 大促分析、达人筛选/触达/合作推进流程；
- 小红书策略循环恢复为用户确认的原始逻辑：`选题 → 测文章 → 复刻 → 测数据 → 养号 → 发文章 → 重复循环`；
- 人瑞进度同步只保留用户确认的进度、阶段、问题、待确认事项，不额外加入“风险”主张；
- 朗臻红海策略收紧为用户明确表达的“产品差异化”，不扩写成未确认的定位 / 表达差异化；
- Agent Builder 保留当前主线既有 repository/ref 定位，但继续 `DOCUMENTED_ONLY / REPO_NOT_VERIFIED`。

## Downstream state

- `CLAIM_LEDGER.md`: 已重新对齐到本 epoch；不再包含当前 Fact Master 未收录的历史旁支 exclusion。
- `CANONICAL_TIMELINE.md`: 未变化；Timeline Gate 保持 PASS。
- Existing R1–R6 artifacts: 均需根据当前事实母版重新分配证据并做语义重验 / 重写。
- `APPLICATION_READY = NO`，直到对应 Role Baseline、Single-JD、ATS / Render Gate 完成。

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
