# Current Version Index

状态：`CANONICAL CURRENT-STATE INDEX`。本文件是仓库内判断“当前应该读取哪个版本”的唯一入口；历史目录名、README 摘要、各版本 Audit 自述均不能覆盖本索引。

## Repository Lock

- Repository: `wanghanyu654321-cell/jianli`
- Active branch: `resume/baseline-v2-r1-r3`
- Default branch `main`: not current for this resume workflow.

## Source State

- Candidate fact source ID: `FCT-001`
- Current GitHub fact master: `resume-workspace/01-facts/FACT_MASTER_CURRENT.md`
- Current source epoch: `FCT-EPOCH-20260916-D0C724C3`
- Canonical Git blob SHA: `d0c724c31d2742f35a7870fb2f37c93a153cd47a`
- Source currency: `CURRENT`
- Claim Ledger: `resume-workspace/01-facts/CLAIM_LEDGER.md`, rebased to current epoch.
- Canonical Timeline: `resume-workspace/00-source/CANONICAL_TIMELINE.md`, unchanged and active.
- Local `简历母版.docx` is a historical external representation until manually synchronized; it must not silently overwrite the current GitHub epoch.

## Current Resume Artifacts

| role | current artifact | content generation | current state |
|---|---|---|---|
| R1 Agent Eval / LLM Quality | `resume-workspace/06-baseline-v3/R1-Agent-Eval/R1-Agent-Eval.RESUME.md` | V3 editorial rewrite based on pre-2026-09-16 fact set | `PARTIAL_NEEDS_REWRITE` |
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

- Fact master review: `PASS`
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
2. `PROJECT_SELECTION = ROLE_DEPENDENT`: project blocks may be retained, reordered, compressed, replaced by another approved project, or omitted according to role/JD value; projects never replace formal work history.
3. `ROLE FOCUS ≠ EXPERIENCE DELETION`.
4. `ROLE MAY REINTERPRET CAPABILITY. ROLE MAY NOT REWRITE HISTORY.`
5. `SOP` is a possible output of solved recurring problems, not the mandatory endpoint of every Proof Unit.
6. `CONSISTENCY BELONGS TO REASONING LOGIC, NOT TO BULLET SHAPE.` Different problems may use different Proof shapes.
7. Team/business results and personal results must remain scoped separately.
8. Any resume text mutation after semantic claim check requires a new semantic claim check.

## Next Execution Order

`R1–R6 role evidence repartition → role-specific rewrite → per-role Claim Mapping / Career Substance / Recruiter Review → real Single-JD → ATS → final fact parity → render`

当前重写目标不是把六份简历写成六套事实，而是让同一事实池通过不同 Core Proof / Supporting Evidence / Background Breadth 排序形成更高区分度。
