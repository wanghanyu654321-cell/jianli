# Resume Governance — Always Apply

This rule applies to every task in this repository.

Before reviewing, editing, generating, auditing, tailoring, rendering, or changing resume-related files:

1. Read `resume-workspace/CURRENT_VERSION_INDEX.md`.
2. Read `resume-workspace/GATE_REGISTRY.json`.
3. Run `python scripts/resume_governance_preflight.py`.
4. If preflight fails, do not edit resume artifacts and do not claim completion.
5. Then read `SOURCE_FREEZE.md`, `CANONICAL_TIMELINE.md`, `ROLE_BASELINE_WRITING_MODULE.md`, `REVIEW_ACCEPTANCE_POLICY.md`, and the task-specific artifact.

Never infer the current resume from a path name, directory number, README summary, old Audit, old Status file, chat history, or model memory.

Current-state authority:
- `CURRENT_VERSION_INDEX.md` = human-readable current version truth.
- `GATE_REGISTRY.json` = machine-readable current gate/status truth.

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

At task completion, rerun preflight and report branch, source epoch, source currency, affected artifacts, affected gates, semantic-change status, claim-recheck status, and Application Ready status.
