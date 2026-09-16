# Current Version Index

状态：`CANONICAL CURRENT-STATE INDEX`。本文件是仓库内判断“当前应该读取哪个版本”的唯一入口；历史目录名、README 摘要、各版本 Audit 自述均不能覆盖本索引。

## Repository Lock

- Repository: `wanghanyu654321-cell/jianli`
- Active branch: `resume/baseline-v2-r1-r3`
- Default branch `main`: not current for this resume workflow.

## Source State

- Candidate fact source ID: `FCT-001`
- Current GitHub fact master mirror: `resume-workspace/01-facts/FACT_MASTER_CURRENT.md`
- Current source epoch: `FCT-EPOCH-20260916-FE4CB619`
- Current Git blob SHA: `fe4cb619cccf99f98813f7dec683b8022ff4f2e5`
- Source currency: `CURRENT`
- Claim Ledger: `resume-workspace/01-facts/CLAIM_LEDGER.md`, rebased to current epoch.
- Canonical Timeline: `resume-workspace/00-source/CANONICAL_TIMELINE.md`, unchanged and active.
- Fact-master scope: `CURRENT MAINLINE FACTS + USER-CONFIRMED CONTEXT ONLY`；旧快照 / 旧 Claim / 历史旁支不得自动恢复。

## Current Resume Artifacts

当前 R1–R6 已基于 `FCT-EPOCH-20260916-FE4CB619` 完成 V6 recruiter re-audit，统一放入 `resume-workspace/09-baseline-v6-recruiter-reaudit/`。本轮关键变化是将 Agent 项目最新的 `实际落地目标 → Demo → POC 交付 / 验证 → 上线准备` 状态纳入岗位族证据，同时继续保持 production / customer / commercial 边界。

| role | current artifact | current state |
|---|---|---|
| R1 Agent Eval / LLM Quality | `resume-workspace/09-baseline-v6-recruiter-reaudit/R1-Agent-Eval/R1-Agent-Eval.RESUME.md` | `V6_RECRUITER_REAUDITED_BASELINE` |
| R2 Business FDE / AI Delivery | `resume-workspace/09-baseline-v6-recruiter-reaudit/R2-Business-FDE/R2-Business-FDE.RESUME.md` | `V6_RECRUITER_REAUDITED_BASELINE` |
| R3 AI Commerce | `resume-workspace/09-baseline-v6-recruiter-reaudit/R3-AI-Commerce/R3-AI-Commerce.RESUME.md` | `V6_RECRUITER_REAUDITED_BASELINE` |
| R4 AI Product Ops / Agent Product / Intelligent Service | `resume-workspace/09-baseline-v6-recruiter-reaudit/R4-AI-Product-Ops/R4-AI-Product-Ops.RESUME.md` | `V6_RECRUITER_REAUDITED_BASELINE` |
| R5 Agent Solution / Prompt Engineering | `resume-workspace/09-baseline-v6-recruiter-reaudit/R5-Agent-Solution/R5-Agent-Solution.RESUME.md` | `V6_RECRUITER_REAUDITED_BASELINE` |
| R6 AI Solution / Solution Consultant / Agent Delivery | `resume-workspace/09-baseline-v6-recruiter-reaudit/R6-AI-Solution/R6-AI-Solution.RESUME.md` | `V6_RECRUITER_REAUDITED_BASELINE` |

Recruiter re-audit：`resume-workspace/09-baseline-v6-recruiter-reaudit/RECRUITER_REVIEW.md`。

## V6 Role Positioning

- **R1**：Data Agent Eval / LLM Quality；新增 Demo / POC 上线前验证，使 Eval 与实际 Delivery 链路更完整，但主线不变。
- **R2**：Business FDE / AI Delivery；当前已有直接 Demo / POC Delivery 与 pre-launch 证据，剩余缺口集中在正式 production Go-live、企业客户验收主体和复杂系统集成。
- **R3**：AI Commerce；完整 Commerce 链仍是主证据，Data Agent + Agent Demo / POC 提升 AI 侧可信度，但不写生产 Commerce Agent。
- **R4**：由偏 `AI Product Quality Ops` 扩展为 `AI Product Ops / Agent Product / Intelligent Service`；有实际落地、产品 / Agent Boundary、Acceptance、Demo / POC 与 pre-launch，但正式 PRD 仍是待补资产。
- **R5**：Agent Solution / Prompt + Eval；Prompt/System/Tool Instruction、Evidence/Tool/Routing Boundary、Frozen Cases 与 Demo / POC 构成更完整的落地证据。
- **R6**：由 `Pre-sales Transition` 进一步收敛为 `AI Solution / Solution Consultant / Agent Delivery`；Demo / POC 已不是缺口，硬缺口转为企业客户成交、投标采购、production Go-live 和复杂系统集成。

## Recruiter Review State

- Fact currency: `PASS`
- Career History: `PASS`
- Career Substance: `PASS`
- Role-family recruiter re-audit: `PASS`
- Demo / POC status parity: `PASS`
- PRD status: `PENDING_ASSET`
- Per-bullet Claim Mapping: `PARTIAL / NOT YET FORMALIZED`
- Single-JD tailoring: `NOT_RUN`
- ATS: `NOT_RUN`
- Render: `NOT_RUN`
- Application Ready: `NO`

V6 Recruiter Review 已记录六个岗位族的 15 秒首屏识别、继续阅读理由、最新硬缺口、高概率面试追问和岗位定位变化。

## Superseded / Historical Paths

- `resume-workspace/03-baselines/`: historical role blueprints.
- `resume-workspace/05-baseline-v2/`: historical V2 baselines.
- `resume-workspace/06-baseline-v3/`: prior R1 V3.
- `resume-workspace/07-baseline-v4/`: pre-enrichment V4 drafts.
- `resume-workspace/08-baseline-v5-recruiter-reviewed/`: recruiter-reviewed baselines before Demo / POC delivery status correction; superseded by V6.
- Prior Source Epochs remain audit history only.

## Governance Invariants

1. `FULL CAREER HISTORY = HARD INVARIANT`：三段正式工作经历必须完整存在并保持时间线。
2. `CURRENT FACT MASTER SCOPE = CURRENT MAINLINE + USER-CONFIRMED CONTEXT`。
3. `ROLE MAY REINTERPRET CAPABILITY. ROLE MAY NOT REWRITE HISTORY.`
4. `ROLE FOCUS ≠ EXPERIENCE DELETION`。
5. `RESUME DESENSITIZATION = PRESERVE REASONING, HIDE REPLICABLE IMPLEMENTATION DETAIL`。
6. Team/business results and personal results remain scoped separately.
7. `DEMO / POC / PRE-LAUNCH ≠ PRODUCTION LIVE / CUSTOMER COMMERCIAL DEPLOYMENT`。
8. 正式 PRD 未产出前不得写“已完成 PRD”。
9. 任何后续语义修改都需要重新做 Claim Check。

## Next Execution Order

`Formal per-role Claim Mapping → freeze real Single-JD → Must-have decomposition → 15s recruiter screen → Direct/Transferable/Project/Gap mapping → Single-JD rewrite → interview probes → ATS → render`

对 R4 最有价值的下一证据是正式 PRD；对 R2/R4/R5/R6 最有价值的共同下一证据是 ICP 相关手续完成后的正式上线、真实使用、验收与上线后指标闭环。
