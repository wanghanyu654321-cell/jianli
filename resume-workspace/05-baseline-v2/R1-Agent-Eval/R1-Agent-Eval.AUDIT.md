# R1 Agent Eval Baseline Audit

## 1. Source coverage

- Primary fact source: `FCT-001` / `简历母版.docx`.
- JD source: `JD-001` / `JD母版.docx`.
- Claim source: `resume-workspace/01-facts/CLAIM_LEDGER.md`.
- The resume uses FCT-02–FCT-06, FCT-08, FCT-09–FCT-15, FCT-16–FCT-20, and FCT-24–FCT-30.

## 2. Claim coverage

Every resume bullet is mapped in `R1-Agent-Eval.CLAIM_MAP.md`. Summary, competencies and tool lines also have an explicit map entry.

## 3. Excluded claims

- FCT-07: the unresolved 3% CTR memory is excluded.
- FCT-29: the two explicitly deferred projects are excluded.
- Unresolved account assignment for the 618-day and daily-high figures is excluded.

## 4. Documented-only claims

FCT-24–FCT-27 describe the Agent project and its test-set results. The wording keeps the project context and test-set qualifier. No production traffic, paid customer or production launch claim is made.

## 5. Repo-verified claims

None. The current workspace has no checkout matching the fact source reference `wanghanyu654321-cell/-agent` / `job-ready/integration-v1`.

## 6. Strong verb audit

“参与、维护、负责、推动、结合、定义、设计、组织、形成、协作完成” are supported by the mapped claims. “提升” is used only with the documented consistency and GMV changes. No unsupported seniority, experience-duration, independent-ownership or production-launch wording is used.

## 7. JD-family relevance

The ordering prioritizes Data Agent Eval, Query/Recall/Relevance, QA, Badcase, SOP, task scale, consistency and metrics observation, matching R1 P0/P1 requirements. Search and e-commerce evidence is retained as supporting context.

## 8. Missing evidence

Education, name and contact fields are absent from the canonical fact source. Python/SQL, automated evaluation, LLM-as-a-Judge and production evaluation ownership are not directly supported.

## 9. Baseline ATS sanity

PASS at text-structure level: single-column Markdown structure, conventional headings, plain text bullets, consistent dates and no tables/images. This is not a platform ATS pass.

## 10. Remaining risk

The Agent project remains documented-only until the matching repository or original test evidence is available. Rendered page count is not verified because the local runtime lacks `soffice.exe`.

## Timeline Gate

- Canonical graduation: `2022.06`
- Canonical career start: `2022.03`
- Renrui: `2025.09–2026.06`
- Jinyi: `2024.11–2025.07`
- Langzhen: `2022.03–2024.07`
- Ordering: `PASS`
- Cross-resume consistency: `PASS`
- Gap preservation: `PASS` (`2024.08–2024.10`; `2025.08`)

## Timeline Revalidation

- Fact source hash changed: YES
- Graduation date re-read: YES (`2022.06` present in current fact source)
- Langzhen dates re-read: YES (`2022.03–2024.07`)
- Cross-role date consistency: PASS
- Work-before-graduation note: PRESENT (`WORK_START_BEFORE_GRADUATION = VALID_USER_CONFIRMED_FACT`)
- Employment overlap check: PASS
