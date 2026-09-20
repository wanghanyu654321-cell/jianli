# Mandatory Resume Governance Instructions

These instructions apply to the entire repository. They are not optional workflow suggestions.

## 1. Mandatory first-read order

Before reviewing, editing, generating, auditing, tailoring, rendering, or changing any resume-related artifact, read these files in this order:

1. `resume-workspace/CURRENT_VERSION_INDEX.md`
2. `resume-workspace/GATE_REGISTRY.json`
3. `resume-workspace/00-source/SOURCE_FREEZE.md`
4. `resume-workspace/00-source/CANONICAL_TIMELINE.md`
5. `resume-workspace/00-source/ROLE_BASELINE_WRITING_MODULE.md`
6. `REVIEW_ACCEPTANCE_POLICY.md`
7. Only then read the task-specific Resume / Claim Map / Audit / JD artifact.

Do not use README, historical Status files, directory names, filenames, prior chat context, model memory, or old Audit text to override the two current-state truth sources.

## 2. Preflight scope

`python scripts/resume_governance_preflight.py` is a **canonical-registry consistency check**. It validates the branch and state declared by `CURRENT_VERSION_INDEX.md` / `GATE_REGISTRY.json`.

- On the canonical branch, or immediately before/after an authorized canonical promotion, run this preflight and require PASS.
- On an unpromoted working-candidate branch such as `resume/v5-final-polish`, the script is **not** the candidate-state validator because it intentionally rejects a branch that differs from the canonical registry.
- On a working-candidate branch, verify instead: actual branch → `FACT_MASTER_CURRENT.md` → `CLAIM_LEDGER.md` → candidate Manifest / Audit → target artifact. Do not modify the canonical registry merely to make the canonical preflight pass.
- If candidate facts / claims / artifact audit disagree with each other, stop and report the ambiguity before editing resume text.

After candidate work, re-check the candidate Manifest / Audit. Run the canonical preflight only when operating on the canonical state or performing an explicitly authorized promotion.

## 3. Authority boundaries

Current repository state authority:

- `CURRENT_VERSION_INDEX.md`: canonical human-readable **promoted** current-version index.
- `GATE_REGISTRY.json`: canonical machine-readable **promoted** gate/status registry.
- A working-candidate branch may contain newer facts / artifacts without changing either canonical file. Newer candidate != promoted canonical.

Candidate fact authority:

- `FCT-001` / local `简历母版.docx` is the only candidate fact source.
- `JD-001` provides role-market requirements only and never creates candidate facts.
- `CLAIM_LEDGER.md` is derived from a specific frozen source epoch and cannot override a newer FCT-001.

If `source_currency != CURRENT`, do not add source-sensitive factual claims and do not mark any artifact Application Ready.

## 4. No silent drift

Never infer canonical currency from the newest-looking path or filename. Use `CURRENT_VERSION_INDEX.md` for promoted canonical state; use the current branch Manifest / Audit plus source epoch for unpromoted candidate state. V5 / V6 numeric labels are not recency authority.

Never collapse these states:

- Fact currency
- Claim mapping integrity
- Timeline integrity
- Career history
- Career substance
- Recruiter quality
- ATS
- Render

A `PASS` without an explicit gate name is invalid.

Any semantic change to resume text invalidates the prior semantic claim check for the changed text. Re-run semantic claim mapping before content freeze.

## 5. Invariants

- `FULL CAREER HISTORY = HARD INVARIANT`
- `PROJECT_SELECTION = ROLE_DEPENDENT`
- `ROLE FOCUS != EXPERIENCE DELETION`
- `FACT SAFETY != RESUME QUALITY`

All three formal work experiences must remain present with canonical company names, role paths, dates, gaps, and reverse chronology. Projects may be retained, moved, compressed, replaced by another approved project, or omitted according to role/JD value.

## 6. Required completion report

Any final report after repository work must explicitly state:

- repository branch
- canonical branch / promotion state
- current working-candidate source epoch (when applicable)
- canonical source epoch
- source currency
- target artifact(s)
- gates affected
- whether semantic text changed
- whether semantic claim re-check is required/completed
- whether Application Ready remains false/true

If any of these cannot be determined from the current-state truth sources, stop and report the ambiguity instead of guessing.
