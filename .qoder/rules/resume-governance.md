# Resume Governance — Always Apply

This rule applies to every task in this repository.

Before reviewing, editing, generating, auditing, tailoring, rendering, or changing resume-related files:

1. Read `resume-workspace/CURRENT_VERSION_INDEX.md`.
2. Read `resume-workspace/GATE_REGISTRY.json`.
3. Determine whether the task is operating on promoted canonical state or an unpromoted working-candidate branch.
4. For canonical-state work / authorized promotion, run `python scripts/resume_governance_preflight.py` and require PASS.
5. For an unpromoted candidate branch, do not use canonical branch mismatch as a failure. Verify current branch → `FACT_MASTER_CURRENT.md` → `CLAIM_LEDGER.md` → candidate Manifest / Audit → task artifact instead.
6. Then read `SOURCE_FREEZE.md`, `CANONICAL_TIMELINE.md`, `ROLE_BASELINE_WRITING_MODULE.md`, `REVIEW_ACCEPTANCE_POLICY.md`, and the task-specific artifact.

Never infer the current resume from a path name, directory number, README summary, old Audit, old Status file, chat history, or model memory.

Canonical-state authority:
- `CURRENT_VERSION_INDEX.md` = human-readable promoted canonical version truth.
- `GATE_REGISTRY.json` = machine-readable promoted canonical gate/status truth.

Working-candidate authority:
- current branch + `FACT_MASTER_CURRENT.md` + `CLAIM_LEDGER.md` + candidate Manifest / Audit.
- a newer candidate does not become canonical until explicit promotion.
- V5 / V6 labels are historical names, not recency ordering.

Candidate-fact authority remains local `FCT-001`; repository state files do not create candidate facts.

If source currency is not `CURRENT`:
- do not add source-sensitive facts;
- do not claim Single-JD readiness;
- do not claim ATS completion;
- do not mark Application Ready.

Any semantic resume-text change invalidates the previous semantic claim check for the changed text.

Hard invariants:
- `FULL CAREER HISTORY = HARD INVARIANT`
- `PROJECT_SELECTION = ROLE_DEPENDENT`
- `ROLE FOCUS != EXPERIENCE DELETION`
- `FACT SAFETY != RESUME QUALITY`

At task completion, report branch, promotion state, candidate/canonical source epochs as applicable, source currency, affected artifacts, affected gates, semantic-change status, claim-recheck status, and Application Ready status. Rerun canonical preflight only for canonical-state work or an explicitly authorized promotion.
