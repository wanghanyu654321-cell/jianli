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

## Current Resume Artifacts

当前 R1–R6 已完成基于 `FCT-EPOCH-20260916-04094915` 的 V5 recruiter-oriented rewrite，统一放入 `resume-workspace/08-baseline-v5-recruiter-reviewed/`。本轮已按 15–20 秒初筛、Core Proof 优先、Career Substance、中层脱敏与面试追问风险重新组织内容。

| role | current artifact | current state |
|---|---|---|
| R1 Agent Eval / LLM Quality | `resume-workspace/08-baseline-v5-recruiter-reviewed/R1-Agent-Eval/R1-Agent-Eval.RESUME.md` | `V5_RECRUITER_REVIEWED_BASELINE` |
| R2 Business FDE / AI Delivery | `resume-workspace/08-baseline-v5-recruiter-reviewed/R2-Business-FDE/R2-Business-FDE.RESUME.md` | `V5_RECRUITER_REVIEWED_BASELINE` |
| R3 AI Commerce | `resume-workspace/08-baseline-v5-recruiter-reviewed/R3-AI-Commerce/R3-AI-Commerce.RESUME.md` | `V5_RECRUITER_REVIEWED_BASELINE` |
| R4 AI Product Quality Ops / Intelligent Service | `resume-workspace/08-baseline-v5-recruiter-reviewed/R4-AI-Product-Ops/R4-AI-Product-Ops.RESUME.md` | `V5_RECRUITER_REVIEWED_BASELINE` |
| R5 Agent Solution / Prompt Engineering | `resume-workspace/08-baseline-v5-recruiter-reviewed/R5-Agent-Solution/R5-Agent-Solution.RESUME.md` | `V5_RECRUITER_REVIEWED_BASELINE` |
| R6 AI Solution / Solution Consultant / Pre-sales Transition | `resume-workspace/08-baseline-v5-recruiter-reviewed/R6-AI-Solution/R6-AI-Solution.RESUME.md` | `V5_RECRUITER_REVIEWED_BASELINE` |

Recruiter review：`resume-workspace/08-baseline-v5-recruiter-reviewed/RECRUITER_REVIEW.md`。

## V5 Role Positioning

- **R1**：Data Agent Eval / LLM Quality；突出多轮 / Tool / Step / 信息完整性评测、Badcase taxonomy、Regression、SQL 基础与 Agent Eval Asset。
- **R2**：Business FDE / AI Delivery；突出 Requirement / Context、优先级、排期、多方推进、方案汇报、Acceptance；不冒充真实 AI Go-live。
- **R3**：AI Commerce；突出市场→产品→Search/Content→Ads→BD→Supply→Data，并用 Data Agent / Relevance 补 AI 侧证据。
- **R4**：收敛为 AI Product Quality Ops / Intelligent Service / 场景运营，而不是强写传统 Product Manager Owner。
- **R5**：收敛为 Agent Solution / Prompt + Eval；突出 Prompt/System/Tool Instruction、Evidence/Tool/Routing Boundary、Frozen Cases 与 Regression。
- **R6**：收敛为业务型 AI Solution / Solution Consultant 转型；突出 B2B/Partner 沟通、商业 Trade-off、方案汇报与 Agent Solution Boundary，同时保留无 Demo/POC/成交经验边界。

## Recruiter Review State

- Fact currency: `PASS`
- Career History: `PASS`
- Career Substance: `PASS`
- Role-family recruiter review: `PASS`
- Per-bullet Claim Mapping: `PARTIAL / NOT YET FORMALIZED`
- Single-JD tailoring: `NOT_RUN`
- ATS: `NOT_RUN`
- Render: `NOT_RUN`
- Application Ready: `NO`

V5 的 Recruiter Review 已记录每个岗位族的：15 秒首屏识别、为什么继续看、可能卡住的硬缺口、高概率面试追问，以及该基线适合进入哪类 Single-JD。

## Superseded / Historical Paths

- `resume-workspace/03-baselines/`: historical role blueprints.
- `resume-workspace/05-baseline-v2/`: historical V2 baselines.
- `resume-workspace/06-baseline-v3/`: prior R1 V3.
- `resume-workspace/07-baseline-v4/`: pre-enrichment V4 drafts; superseded by current V5 recruiter-reviewed baselines.
- Prior Source Epochs remain audit history only.

## Governance Invariants

1. `FULL CAREER HISTORY = HARD INVARIANT`：三段正式工作经历必须完整存在并保持时间线。
2. `CURRENT FACT MASTER SCOPE = CURRENT MAINLINE + USER-CONFIRMED CONTEXT`。
3. `ROLE MAY REINTERPRET CAPABILITY. ROLE MAY NOT REWRITE HISTORY.`
4. `ROLE FOCUS ≠ EXPERIENCE DELETION`。
5. `RESUME DESENSITIZATION = PRESERVE REASONING, HIDE REPLICABLE IMPLEMENTATION DETAIL`。
6. Team/business results and personal results remain scoped separately.
7. Project evidence不得升级为生产 / 客户证据。
8. 任何后续语义修改都需要重新做 Claim Check。

## Next Execution Order

`Formal per-role Claim Mapping → freeze real Single-JD → Must-have decomposition → 15s recruiter screen → Direct/Transferable/Project/Gap mapping → Single-JD rewrite → interview probes → ATS → render`

当前不再继续泛化扩写岗位族基线。下一步价值来自真实 Single-JD 的选择与重排。
