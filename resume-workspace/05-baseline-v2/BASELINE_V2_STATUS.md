# Baseline V2 Status

| Role | Status | Length target | Claim mapping | Repo evidence | Main gap |
|---|---|---|---|---|---|
| R1 Agent Eval / LLM Quality | PARTIAL | 1.5–2 pages after standard rendering | Rebuilt map; semantic audit recorded | None; Agent project remains documented-only | Education/name/contact; Python/SQL/automated evaluation not in FACT |
| R2 Business FDE / AI Delivery | PARTIAL | 1.5–2 pages after standard rendering | Rebuilt map; semantic audit recorded | None; Agent project remains documented-only | Education/name/contact; customer delivery, Demo/POC and interface evidence |
| R3 AI Commerce | PARTIAL | 1.5–2 pages after standard rendering | Rebuilt map; semantic audit recorded | None; Agent project remains documented-only | Education/name/contact; Merchant Agent and production AI Commerce evidence |

## SOURCE_REBASE_STATUS

- Fact source: `FCT-001` / local `简历母版.docx`
- Old fingerprint: `037FB4FA3B77157F5DBE201971E3962241DC897FCAF39DC903897A327518528D`
- New fingerprint: `B31C7EC90FFEB48B023E43C37CBACB08817A562B3A42C1148B34DFE3BA4FB6E1`
- Fact source reread: `YES`; fresh `DER-001` extraction recorded 642 paragraphs, 0 tables, 597 lines.
- Graduation date re-read: `YES`; current source has no graduation date (`GRADUATION_DATE_NOT_PRESENT`).
- Langzhen dates re-read: `YES`; `2022.03–2024.07`.
- Jinyi dates re-read: `YES`; `2024.11–2025.07`.
- Renrui dates re-read: `YES`; `2025.09–2026.06`.
- Work-before-graduation: `NOT_APPLICABLE` because no graduation date is present; no timeline note created.
- Employment overlap: `PASS`; the three intervals are separated by gaps.
- Claim Ledger rebuilt: `YES` from the fresh extraction; no old DER line locator retained.
- R1/R2/R3 Claim Maps rebuilt: `YES`; stale line locators corrected and semantic grounding audits added.
- R1/R2/R3 Audits updated: `YES`; each contains the required Timeline Revalidation block.
- Public education field: `[LOCAL_ONLY_EDUCATION]`; no school or education detail is exposed. `EDUCATION_SOURCE_PRESENT = TRUE` is an audit fact only.
- R3 recruiter order: Renrui → Jinyi → Langzhen, following the factual chronology rule.
- Whole-repository timeline-term scan completed: no unsupported experience-year summary was added; older dates remain only in frozen `master/` and `03-baselines/` artifacts, which are outside this round's explicit allowlist and were left unchanged.

## BASELINE_V2_GATE

`PARTIAL`

The three baselines have recruiter-facing structure, revalidated dates, rebuilt claim maps and separate audits. They remain `PARTIAL` because private education/name/contact injection is pending, the cited Agent repository is not available for verification, and page rendering could not be completed in the current runtime.

## Baseline ATS sanity

Text-level sanity checks pass: single-column headings, conventional section names, plain bullets, consistent dates, no tables or images, and no final ATS-pass claim. This is not the final ATS audit.

## Acceptance-policy note

`REVIEW_ACCEPTANCE_POLICY.md` is present at repository root after syncing the latest `main`.

## Scope stop

This round only re-based source-sensitive content in `05-baseline-v2/` and the required fact ledger. R4–R7 remain unchanged. No Single-JD Tailoring, final ATS, DOCX/PDF rendering or automatic application is performed.
