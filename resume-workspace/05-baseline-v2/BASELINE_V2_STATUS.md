# Baseline V2 Status

| Role | Status | Length target | Claim mapping | Repo evidence | Main gap |
|---|---|---|---|---|---|
| R1 Agent Eval / LLM Quality | PARTIAL | 1.5–2 pages after standard rendering | Rebuilt map; semantic and timeline gates recorded | None; Agent project remains documented-only | Private name/contact injection; Python/SQL/automated evaluation not in FACT |
| R2 Business FDE / AI Delivery | PARTIAL | 1.5–2 pages after standard rendering | Rebuilt map; semantic and timeline gates recorded | None; Agent project remains documented-only | Private name/contact injection; customer delivery, Demo/POC and interface evidence |
| R3 AI Commerce | PARTIAL | 1.5–2 pages after standard rendering | Rebuilt map; semantic and timeline gates recorded | None; Agent project remains documented-only | Private name/contact injection; Merchant Agent and production AI Commerce evidence |

## SOURCE_REBASE_STATUS

- Fact source: `FCT-001` / local `简历母版.docx`; document version `V3`.
- Old fingerprint: `B31C7EC90FFEB48B023E43C37CBACB08817A562B3A42C1148B34DFE3BA4FB6E1` (`SUPERSEDED`).
- New fingerprint: `7EAA096A7220DE0609E3AACAEA656B4CEEFB006D1419FA01BC07E97FFFCDDDEB`.
- Fact source reread: `YES`; fresh `DER-001` extraction recorded 646 paragraphs, 0 tables, 601 lines.
- Claim Ledger rebuilt: `YES`; R1/R2/R3 Claim Maps rebuilt with explicit timeline claims; audits rebuilt with Timeline Gate.

## CANONICAL_TIMELINE_GATE

- Graduation: `2022.06`
- Career start: `2022.03`
- Renrui: `2025.09–2026.06`
- Jinyi: `2024.11–2025.07`
- Langzhen: `2022.03–2024.07`
- Timeline consistency across R1/R2/R3: `PASS`
- Timeline gap preservation: `PASS` (`2024.08–2024.10`; `2025.08`)
- Graduation-before/after-work relation: `USER_CONFIRMED_VALID` (`WORK_START_BEFORE_GRADUATION = VALID_USER_CONFIRMED_FACT`)
- Standard reverse chronology across all three resumes: `PASS`
- Whole-repository old-date scan: `COMPLETED`; historical old-date occurrences remain only in files explicitly marked `STATUS: SUPERSEDED` and are not valid current inputs.

## BASELINE_V2_GATE

`PARTIAL`

Timeline canonicalization is complete and all three current baselines share the same factual dates and gaps. The gate remains `PARTIAL` because private name/contact injection is pending, the cited Agent repository is unavailable for verification, and final ATS/rendering has not been run.

## Baseline ATS sanity

Text-level sanity checks pass: single-column headings, conventional section names, plain bullets, consistent dates, no tables or images, and no final ATS-pass claim. This is not the final ATS audit.

## Acceptance-policy note

`REVIEW_ACCEPTANCE_POLICY.md`, `CANONICAL_TIMELINE.md` and `SOURCE_FREEZE.md` are present on the current branch.

## Scope stop

This round canonicalizes the local fact source, source freeze, timeline invariant, Claim Ledger and source-sensitive baseline artifacts. Older `03-baselines/`, `master/` and pipeline status snapshots are marked `SUPERSEDED` and retained for audit history. No Single-JD Tailoring, final ATS, DOCX/PDF resume generation or automatic application is performed.
