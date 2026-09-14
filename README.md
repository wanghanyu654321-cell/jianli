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

## Current branch interpretation

The active review branch is `resume/baseline-v2-r1-r3`. The repository default branch `main` does not contain the current V2/V3 working state and must not be used as the source of truth for current resume review.

Current recruiter-facing artifacts are indexed only in `CURRENT_VERSION_INDEX.md`.

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

The last repository-known FCT-001 freeze is `FCT-EPOCH-20260913-7EAA096A` / SHA256 `7EAA096A…CDDDEB`. A later R1 V3 source reread recorded a further non-timeline local fingerprint change. Therefore the repository source currency is currently `STALE_PENDING_REBASE`.

Existing Claim Maps may still demonstrate mapping integrity to the repository Claim Ledger, but they do not prove that the Ledger contains the latest local FCT-001 state. Final application use is blocked until source rebase and affected downstream revalidation complete.

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

- Timeline: `PASS`
- Source currency: `STALE_PENDING_REBASE`
- R1: V3 / recruiter quality and career substance still `PARTIAL`
- R2: V2 / V3 editorial rewrite not yet completed
- R3: V2 / V3 editorial rewrite not yet completed
- Single-JD: `NOT_RUN`
- Final ATS: `NOT_RUN`
- Final Render: `NOT_RUN`
- Application Ready: `NO`
