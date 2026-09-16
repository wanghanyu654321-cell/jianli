# Current Version Index

状态：`CANONICAL CURRENT-STATE INDEX`。本文件是仓库内判断“当前应该读取哪个版本”的唯一入口；历史目录名、README 摘要、各版本 Audit 自述均不能覆盖本索引。

## Repository Lock

- Repository: `wanghanyu654321-cell/jianli`
- Active branch: `resume/baseline-v2-r1-r3`
- Default branch `main`: not current for this resume workflow.

## Source State

- Candidate fact source ID: `FCT-001`
- Current GitHub fact master mirror: `resume-workspace/01-facts/FACT_MASTER_CURRENT.md`
- Current source epoch: `FCT-EPOCH-20260916-6D82DB08`
- Current Git blob SHA: `6d82db084b0bef7ec1967982ebb36213942fd571`
- Source currency: `CURRENT`
- Claim Ledger: `resume-workspace/01-facts/CLAIM_LEDGER.md`, rebased to current epoch.
- Canonical Timeline: `resume-workspace/00-source/CANONICAL_TIMELINE.md`, unchanged and active.
- Fact-master scope: `CURRENT MAINLINE FACTS + USER-CONFIRMED CONTEXT ONLY`；旧快照 / 旧 Claim / 历史旁支不得自动恢复。
- Local `简历母版.docx` 与 GitHub mirror 如有差异，不自动互相覆盖，先按用户最新明确确认的事实校准。

## Current Resume Artifacts

| role | current artifact | content generation | current state |
|---|---|---|---|
| R1 Agent Eval / LLM Quality | `resume-workspace/06-baseline-v3/R1-Agent-Eval/R1-Agent-Eval.RESUME.md` | V3 editorial rewrite based on pre-current fact set | `PARTIAL_NEEDS_REWRITE` |
| R2 Business FDE / AI Delivery | `resume-workspace/05-baseline-v2/R2-Business-FDE/R2-Business-FDE.RESUME.md` | V2 | `PARTIAL_NEEDS_REWRITE` |
| R3 AI Commerce | `resume-workspace/05-baseline-v2/R3-AI-Commerce/R3-AI-Commerce.RESUME.md` | V2 | `PARTIAL_NEEDS_REWRITE` |
| R4 AI Product Ops / Intelligent Service | historical baseline only | pre-current fact epoch | `NEEDS_REWRITE` |
| R5 Prompt / Agent Solution | historical baseline only | pre-current fact epoch | `NEEDS_REWRITE` |
| R6 MaaS / AI Solution / Pre-sales | historical baseline only | pre-current fact epoch | `NEEDS_REWRITE` |

## Superseded / Historical Paths

- `resume-workspace/03-baselines/`: historical role blueprints; superseded for current resume review.
- `resume-workspace/master/MASTER_FULL.md`: historical pipeline index; not current fact authority.
- `resume-workspace/04-status/PIPELINE_STATUS.md`: historical status snapshot.
- `resume-workspace/05-baseline-v2/R1-Agent-Eval/`: superseded by R1 V3 for prior recruiter-facing review, but R1 V3 itself now requires current-epoch rewrite/revalidation.
- Prior Source Epochs remain audit history only.

## Downstream Eligibility

- Fact master scope review: `PASS`
- Source currency: `PASS`
- Claim Ledger currentness: `PASS`
- Timeline gate: `PASS`
- Role-family rewrite R1–R6: `ALLOWED`
- Existing role artifact claim parity with current fact epoch: `BLOCKED_PENDING_REWRITE`
- Single-JD tailoring: `BLOCKED` until a real JD exists and selected role baseline is rewritten/revalidated against current fact epoch
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
7. Team/business results and personal results must remain scoped separately.
8. Any resume text mutation after semantic claim check requires a new semantic claim check.

## Next Execution Order

`R1–R6 role evidence repartition → role-specific rewrite → per-role Claim Mapping / Career Substance / Recruiter Review → real Single-JD → ATS → final fact parity → render`

当前重写目标不是把六份简历写成六套事实，而是让同一当前事实池通过不同 Core Proof / Supporting Evidence / Background Breadth 排序形成更高区分度。
