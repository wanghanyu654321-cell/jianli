# Current Version Index

状态：`CANONICAL CURRENT-STATE INDEX`。本文件是仓库内判断“当前应该读取哪个版本”的唯一入口；历史目录名、README 摘要、各版本 Audit 自述均不能覆盖本索引。

## Repository Lock

- Repository: `wanghanyu654321-cell/jianli`
- Active branch: `resume/baseline-v2-r1-r3`
- Default branch `main`: not current for this resume workflow.

## Source State

- Candidate fact source ID: `FCT-001`
- Current GitHub fact master mirror: `resume-workspace/01-facts/FACT_MASTER_CURRENT.md`
- Current source epoch: `FCT-EPOCH-20260916-04094915`
- Current Git blob SHA: `040949158e76a356caf81f4185da2c4a17528e04`
- Source currency: `CURRENT`
- Claim Ledger: `resume-workspace/01-facts/CLAIM_LEDGER.md`, rebased to current epoch.
- Canonical Timeline: `resume-workspace/00-source/CANONICAL_TIMELINE.md`, unchanged and active.
- Fact-master scope: `CURRENT MAINLINE FACTS + USER-CONFIRMED CONTEXT ONLY`；旧快照 / 旧 Claim / 历史旁支不得自动恢复。
- Local `简历母版.docx` 与 GitHub mirror 如有差异，不自动互相覆盖，先按用户最新明确确认的事实校准。

## Current Resume Artifacts

R1–R6 V4 仍位于 `resume-workspace/07-baseline-v4/`，但它们写于上一事实 epoch `FCT-EPOCH-20260916-6D82DB08`。当前事实母版经过真实 JD 能力缺口核对后新增了直接证据，并修正了两处旧表达，因此六份 V4 draft 现在都需要重新做 Skills 优化与 Semantic Claim Check，不能视为与当前事实源完全同步。

| role | current artifact | content generation | current state |
|---|---|---|---|
| R1 Agent Eval / LLM Quality | `resume-workspace/07-baseline-v4/R1-Agent-Eval/R1-Agent-Eval.RESUME.md` | V4 pre-enrichment draft | `DRAFT_NEEDS_REVALIDATION_AFTER_FACT_ENRICHMENT` |
| R2 Business FDE / AI Delivery | `resume-workspace/07-baseline-v4/R2-Business-FDE/R2-Business-FDE.RESUME.md` | V4 pre-enrichment draft | `DRAFT_NEEDS_REVALIDATION_AFTER_FACT_ENRICHMENT` |
| R3 AI Commerce | `resume-workspace/07-baseline-v4/R3-AI-Commerce/R3-AI-Commerce.RESUME.md` | V4 pre-enrichment draft | `DRAFT_NEEDS_REVALIDATION_AFTER_FACT_ENRICHMENT` |
| R4 AI Product Ops / Intelligent Service | `resume-workspace/07-baseline-v4/R4-AI-Product-Ops/R4-AI-Product-Ops.RESUME.md` | V4 pre-enrichment draft | `DRAFT_DIRECTION_NOT_FINAL_AND_NEEDS_REVALIDATION` |
| R5 Agent Solution / Prompt Engineering | `resume-workspace/07-baseline-v4/R5-Agent-Solution/R5-Agent-Solution.RESUME.md` | V4 pre-enrichment draft | `DRAFT_DIRECTION_NOT_FINAL_AND_NEEDS_REVALIDATION` |
| R6 MaaS / AI Solution / Pre-sales | `resume-workspace/07-baseline-v4/R6-AI-Solution/R6-AI-Solution.RESUME.md` | V4 pre-enrichment draft | `DRAFT_NEEDS_REVALIDATION_AFTER_FACT_ENRICHMENT` |

## Current Fact Enrichment Impact

本 epoch 对岗位族的主要影响：

- **R1**：新增评测类目补充、Badcase 分类、规则修改后复测、Agent 多轮 / Tool / Step / 信息完整性评测、基础 SQL / 查询取数、评测资产类型，以及 Agent Eval repo 证据；
- **R2**：新增朗臻 / 今宜的需求清单、优先级、项目排期、阶段检查和方案汇报证据；
- **R3**：新增更完整的项目推进证据和基础 SQL / Data Agent 数据背景；
- **R4**：新增“问题反馈 → 修改跟进 → 再验证”、评测类目 / 资产和执行者 Context 证据，更适合继续验证 AI 产品质量运营 / 场景运营方向；
- **R5**：新增 Prompt / System / Tool Instruction 迭代，以及更结构化的 Frozen Eval Asset 仓库证据；
- **R6**：新增运营方案汇报、项目排期和多方方案沟通证据，但仍不得升级为真实 AI Demo / POC / 售前成交经验。

同时需要从旧 Resume draft 中清理：
- 未确认的 `天猫引力魔方`；
- 未明确确认的“按小时 / 日”时间粒度。

## Superseded / Historical Paths

- `resume-workspace/03-baselines/`: historical role blueprints; superseded for current resume review.
- `resume-workspace/05-baseline-v2/`: historical V2 role baselines.
- `resume-workspace/06-baseline-v3/`: prior R1 V3 artifact.
- `resume-workspace/master/MASTER_FULL.md`: historical pipeline index; not current fact authority.
- `resume-workspace/04-status/PIPELINE_STATUS.md`: historical status snapshot.
- Prior Source Epochs remain audit history only.

## Downstream Eligibility

- Fact master scope review: `PASS`
- Source currency: `PASS`
- Claim Ledger currentness: `PASS`
- Timeline gate: `PASS`
- R1–R6 V4 draft parity with current epoch: `BLOCKED_PENDING_REVALIDATION`
- Per-role Semantic Claim Mapping: `NOT_RUN_FOR_CURRENT_EPOCH`
- Skills optimization / recruiter-oriented refinement: `NEXT`
- R4 / R5 direction confirmation: `PENDING`
- Single-JD tailoring: `BLOCKED` until selected role baseline is revalidated against the current epoch and a real JD is frozen
- Final ATS: `NOT_RUN`
- Final Render: `NOT_RUN`
- Application Ready: `NO`

## Governance Invariants

1. `FULL CAREER HISTORY = HARD INVARIANT`: all three formal work experiences remain present with canonical company names, role paths, dates and reverse chronology.
2. `CURRENT FACT MASTER SCOPE = CURRENT MAINLINE + USER-CONFIRMED CONTEXT`；不得因旧快照 / 旧 Claim 自动恢复历史旁支。
3. `PROJECT_SELECTION = ROLE_DEPENDENT`: project blocks may be retained, reordered, compressed or omitted according to role/JD value; projects never replace formal work history.
4. `ROLE FOCUS ≠ EXPERIENCE DELETION`.
5. `ROLE MAY REINTERPRET CAPABILITY. ROLE MAY NOT REWRITE HISTORY.`
6. `SOP` is a possible output of solved recurring problems, not the mandatory endpoint of every Proof Unit.
7. `RESUME DESENSITIZATION = PRESERVE REASONING, HIDE REPLICABLE IMPLEMENTATION DETAIL`：保留问题、判断、方案类型和结果，不展开内部规则、完整操作顺序、阈值、话术或可直接复刻的执行 recipe。
8. Team/business results and personal results must remain scoped separately.
9. Any fact-source epoch change invalidates prior resume fact-parity status until the affected artifact is revalidated.
10. Any resume text mutation after semantic claim check requires a new semantic claim check.

## Next Execution Order

`Skills review / optimization on current epoch → per-role Claim Mapping → Career Substance / Recruiter Review → R4/R5 direction confirmation → role baseline convergence → real Single-JD → ATS → final fact parity → render`

当前目标：不再扩写未经确认的事实；下一步基于 `FCT-EPOCH-20260916-04094915` 对 R1–R6 做 Skills 优化，并把本轮新增证据正确分配到不同岗位族。
