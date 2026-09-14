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

## 2. Mandatory preflight

Before making any repository change, run:

`python scripts/resume_governance_preflight.py`

If the command exits non-zero, do not modify resume artifacts and do not claim completion. Resolve the governance inconsistency first or report the blocker.

At the end of any task that changes repository files, run the same preflight again.

## 3. Authority boundaries

Current repository state authority:

- `CURRENT_VERSION_INDEX.md`: canonical human-readable current-version index.
- `GATE_REGISTRY.json`: canonical machine-readable current gate/status registry.

Candidate fact authority:

- `FCT-001` / local `简历母版.docx` is the only candidate fact source.
- `JD-001` provides role-market requirements only and never creates candidate facts.
- `CLAIM_LEDGER.md` is derived from a specific frozen source epoch and cannot override a newer FCT-001.

If `source_currency != CURRENT`, do not add source-sensitive factual claims and do not mark any artifact Application Ready.

## 4. No silent drift

Never infer the current artifact from the newest-looking path or filename. Use `CURRENT_VERSION_INDEX.md`.

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
- current source epoch
- source currency
- target artifact(s)
- gates affected
- whether semantic text changed
- whether semantic claim re-check is required/completed
- whether Application Ready remains false/true

If any of these cannot be determined from the current-state truth sources, stop and report the ambiguity instead of guessing.
