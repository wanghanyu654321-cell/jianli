# Resume Engineering Workspace

This repository stores the evidence-bounded resume pipeline outputs prepared on 2026-09-13.

## Mandatory review rule

Before judging whether any resume deliverable is complete or application-ready, read and follow [`REVIEW_ACCEPTANCE_POLICY.md`](REVIEW_ACCEPTANCE_POLICY.md).

Core rule: **first verify whether the actual deliverable satisfies its acceptance gate, then evaluate quality.** Directory names, filenames, pipeline structure, fact governance, or historical chat context are not proof that a resume is complete.

Until they pass the Role Baseline Resume Gate defined in that policy, files under `resume-workspace/03-baselines/` must be treated as `ROLE_BLUEPRINT / PARTIAL` rather than assumed to be finished ~2-page Role Baseline Resumes.

## Contents

- `REVIEW_ACCEPTANCE_POLICY.md` — mandatory repository-first review and completion criteria
- `resume-workspace/00-source/` — source resolution and authority rules
- `resume-workspace/01-facts/` — Claim Ledger
- `resume-workspace/02-jd/` — Requirement × Evidence Matrix and role-family decisions
- `resume-workspace/03-baselines/` — R1–R6 role-family baseline drafts / blueprints and the R7 stretch gap record
- `resume-workspace/04-status/` — pipeline status and verification boundary
- `skill-installation/SOURCES.md` — pinned GitHub sources, licenses, commits and invocation policy

Raw personal DOCX files, local attachments, credentials, environment files and historical workspaces are intentionally not included. The canonical fact and JD sources remain local and are referenced by source ID.

There is no single-company JD in this snapshot, so this repository does not contain a Single-JD Tailored Resume or a final ATS audit. Add one real JD before running the tailoring stage.
