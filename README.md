# Resume Engineering Workspace

This repository stores an evidence-bounded resume engineering workspace. It separates candidate facts, role-family evidence selection, recruiter-facing resume artifacts, audits and downstream application stages.

## Start here

Before judging whether any resume is current, complete or application-ready, read these files in order:

1. `resume-workspace/CURRENT_VERSION_INDEX.md` — canonical current artifact/version entry point.
2. `resume-workspace/GATE_REGISTRY.json` — canonical current gate state.
3. `REVIEW_ACCEPTANCE_POLICY.md` — mandatory review and acceptance semantics.
4. `resume-workspace/00-source/SOURCE_FREEZE.md` — last repository-known source epoch and source-currency status.
5. The actual current `*.RESUME.md` file being reviewed.

Core rule: **Fact Safety ≠ Resume Quality.** Directory names, filenames, Claim Ledger completeness, pipeline structure, historical Audit files or previous chat context are not proof that a resume is current or recruiter-ready.

## Canonical vs working-candidate interpretation

This repository currently has two intentionally separate state layers:

- **Canonical registry state**: `CURRENT_VERSION_INDEX.md` / `GATE_REGISTRY.json` still point to `resume/baseline-v2-r1-r3`. This remains the last explicitly promoted canonical baseline.
- **Working candidate state**: branch `resume/v5-final-polish` contains the newer, unpromoted candidate facts and recruiter-facing artifacts derived from `FCT-EPOCH-20260920-DE68CC7D`, including `ONLINE-MAIN` and R1–R6 under `resume-workspace/10-baseline-v5-grill-complete/`.

A newer working candidate does **not** become canonical merely because its facts or artifacts are newer. Canonical promotion requires an explicit promotion decision; until then, do not rewrite the canonical registry to point at the candidate.

Version labels such as V5 / V6 are historical artifact names, not a reliable recency ordering. Determine currency from **source epoch + artifact status + promotion state**, not from the numeric version label alone.

## Contents

- `REVIEW_ACCEPTANCE_POLICY.md` — mandatory repository-first review, gate definitions and mutation/recheck rules
- `resume-workspace/CURRENT_VERSION_INDEX.md` — current role artifact paths, source currency and downstream eligibility
- `resume-workspace/GATE_REGISTRY.json` — single machine-readable current gate registry
- `resume-workspace/00-source/` — source authority, source epoch/freeze, canonical timeline and writing policy
- `resume-workspace/01-facts/` — Claim Ledger
- `resume-workspace/02-jd/` — Requirement × Evidence Matrix and role-family decisions
- `resume-workspace/03-baselines/` — historical role blueprints; superseded for current recruiter-facing review
- `resume-workspace/04-status/` — historical pipeline snapshot; superseded as current-state authority
- `resume-workspace/05-baseline-v2/` — V2 R1/R2/R3 artifacts; R2/R3 currently still use V2
- `resume-workspace/06-baseline-v3/` — V3 editorial artifacts; currently contains R1
- `skill-installation/SOURCES.md` — pinned external Skill sources and invocation policy

## Current source status

Do not collapse canonical state and working-candidate state into one source-currency label.

- **Canonical registry**: its source epoch and gate state are whatever `CURRENT_VERSION_INDEX.md` / `GATE_REGISTRY.json` currently declare.
- **Working candidate on `resume/v5-final-polish`**: `FACT_MASTER_CURRENT.md` is current for the candidate branch, and the latest final-polish audit records `derived_from_source_epoch = FCT-EPOCH-20260920-DE68CC7D` with FACT blob `de68cc7d3ca981e411864f4968300c5056247f6d`.

The working candidate may be newer than the canonical registry while still being **unpromoted**. This is a governance state, not source drift. Do not downgrade the candidate to an old `STALE_PENDING_REBASE` state solely because older policy text or historical audits contain that label.

## Core governance invariants

- `FULL CAREER HISTORY = HARD INVARIANT`: 人瑞 → 今宜 → 朗臻 remain present with canonical role paths and dates.
- `PROJECT_SELECTION = ROLE_DEPENDENT`: projects may be kept, reordered, compressed, replaced by another approved project, or omitted according to role/JD value.
- `ROLE FOCUS ≠ EXPERIENCE DELETION`.
- Career History and Career Substance are independent gates.
- Any semantic resume mutation invalidates the previous semantic claim check for the changed text.
- No real Single-JD means no company-level tailoring claim.
- ATS and Render occur after content freeze, not before.

## Privacy and local sources

Raw personal DOCX/PDF files, local attachments, credentials, environment files and generated tool state are intentionally not committed. Public artifacts may contain explicit injection markers such as `[LOCAL_ONLY_CONTACT]` and `[LOCAL_ONLY_EDUCATION]`; missing public private fields do not by themselves make the resume content gate fail.

## Current high-level state

**Canonical registry layer**
- Remains intentionally unmodified until explicit promotion.
- Single-JD / ATS / Render / Application Ready must be read from `CURRENT_VERSION_INDEX.md` and `GATE_REGISTRY.json`.

**Working candidate layer — `resume/v5-final-polish`**
- Fact source: `FCT-EPOCH-20260920-DE68CC7D`.
- `FACT_MASTER_CURRENT.md` and `CLAIM_LEDGER.md` contain the current candidate facts / claims.
- `ONLINE-MAIN` plus R1–R6 in `resume-workspace/10-baseline-v5-grill-complete/` are the current unpromoted recruiter-facing candidate artifacts.
- Final-polish integrity audit: completed for the current candidate artifacts.
- Canonical promotion: **NOT YET PERFORMED**.
- Single-JD tailoring: **NOT RUN for the current application stage**.
- 10-second recruiter audit: **NEXT AFTER DOCUMENT AMBIGUITY CLEANUP**.
- Application Ready: **NO** until the remaining review / tailoring / ATS / render gates are completed as required.
