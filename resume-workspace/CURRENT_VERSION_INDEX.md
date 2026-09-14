# Current Version Index

状态：`CANONICAL CURRENT-STATE INDEX`。本文件是仓库内判断“当前应该读取哪个版本”的唯一入口；历史目录名、README 摘要、各版本 Audit 自述均不能覆盖本索引。

## Repository Lock

- Repository: `wanghanyu654321-cell/jianli`
- Active branch: `resume/baseline-v2-r1-r3`
- Baseline commit at governance review: `d01d06e08cc17a9ae88c4ca5ba5eef4aacd99c93`
- Default branch `main`: not current for V2/V3 resume review.

## Source State

- Candidate fact source: `FCT-001` / local `简历母版.docx`
- Last repository-frozen fingerprint: `7EAA096A7220DE0609E3AACAEA656B4CEEFB006D1419FA01BC07E97FFFCDDDEB`
- Last frozen source epoch: `FCT-EPOCH-20260913-7EAA096A`
- Current source currency: `STALE_PENDING_REBASE`
- Reason: R1 V3 audit records a later local FCT-001 fingerprint change after the last repository freeze; timeline anchors remained unchanged, but non-timeline changes were not rebased into the repository.
- Until rebase completes, artifacts derived from `FCT-EPOCH-20260913-7EAA096A` are valid as historical grounded artifacts but are not current enough for `APPLICATION_READY`.

## Current Resume Artifacts

| role | current artifact | content generation | current state |
|---|---|---|---|
| R1 Agent Eval / LLM Quality | `resume-workspace/06-baseline-v3/R1-Agent-Eval/R1-Agent-Eval.RESUME.md` | V3 editorial rewrite | `PARTIAL` |
| R2 Business FDE / AI Delivery | `resume-workspace/05-baseline-v2/R2-Business-FDE/R2-Business-FDE.RESUME.md` | V2 | `PARTIAL` |
| R3 AI Commerce | `resume-workspace/05-baseline-v2/R3-AI-Commerce/R3-AI-Commerce.RESUME.md` | V2 | `PARTIAL` |

## Superseded / Historical Paths

- `resume-workspace/03-baselines/`: historical role blueprints; `SUPERSEDED` for current resume review.
- `resume-workspace/master/MASTER_FULL.md`: historical pipeline index; `SUPERSEDED` as current fact authority.
- `resume-workspace/04-status/PIPELINE_STATUS.md`: historical status snapshot; `SUPERSEDED`.
- `resume-workspace/05-baseline-v2/R1-Agent-Eval/`: superseded by R1 V3 for recruiter-facing R1 review, retained for comparison/audit.
- `resume-workspace/05-baseline-v2/BASELINE_V2_STATUS.md`: historical/transition status document; it is not the canonical current-state registry.

## Downstream Eligibility

- Role-family review: `ALLOWED`
- Editorial rewrite: `ALLOWED`
- Source-sensitive factual additions: `BLOCKED_PENDING_REBASE`
- Single-JD tailoring: `BLOCKED` until a real JD exists and source rebase is current
- Final ATS: `NOT_RUN`
- Final Render: `NOT_RUN`
- Application Ready: `NO`

## Governance Invariants

1. `FULL CAREER HISTORY = HARD INVARIANT`: all three formal work experiences remain present with canonical company names, role paths, dates and reverse chronology.
2. `PROJECT_SELECTION = ROLE_DEPENDENT`: project blocks may be retained, reordered, compressed, replaced by another approved project, or omitted according to role/JD value; projects never replace formal work history.
3. `ROLE FOCUS ≠ EXPERIENCE DELETION`.
4. `FACT SAFETY ≠ RESUME QUALITY`.
5. A `PASS` status is invalid unless the gate name is explicit.
6. Any resume text mutation after a semantic claim check requires semantic claim re-check before content freeze.

## Next Execution Order

`Source Rebase → affected Claim Ledger revalidation → current-state registry refresh → R1 Career Substance / Editorial Rewrite → R1 Recruiter Review → R2 V3 → R3 V3 → real Single-JD → ATS → final fact parity → render`.
