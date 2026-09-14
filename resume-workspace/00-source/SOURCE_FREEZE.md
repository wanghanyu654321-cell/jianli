# Source Freeze

## Repository-known frozen source epoch

- Source ID: `FCT-001`
- Canonical source: local `简历母版.docx` (not uploaded to the public repository)
- Document version at last freeze: `V3`
- Frozen source epoch: `FCT-EPOCH-20260913-7EAA096A`
- Frozen SHA256: `7EAA096A7220DE0609E3AACAEA656B4CEEFB006D1419FA01BC07E97FFFCDDDEB`
- Previous SHA256: `B31C7EC90FFEB48B023E43C37CBACB08817A562B3A42C1148B34DFE3BA4FB6E1` — `SUPERSEDED`
- Historical pre-timeline-rebase SHA256: `037FB4FA3B77157F5DBE201971E3962241DC897FCAF39DC903897A327518528D` — `SUPERSEDED`
- Extraction timestamp (UTC): `2026-09-13T13:06:24.697855Z`
- Extraction at this epoch: 646 paragraphs, 0 tables, 601 derived lines

## Current currency status

`SOURCE_CURRENCY = STALE_PENDING_REBASE`

R1 V3 Audit records that a later reread of local `FCT-001` produced a different fingerprint after `FCT-EPOCH-20260913-7EAA096A`. The canonical timeline anchors remained unchanged, but the non-timeline delta has not been rebased into this repository.

Therefore this file no longer means “latest local source is frozen.” It means “last repository-known frozen source epoch.”

Until source rebase completes:

- `CANONICAL_TIMELINE.md` remains active for the unchanged timeline anchors recorded by the V3 audit;
- Claim Ledger / Claim Maps derived from this epoch remain valid as mappings to that frozen epoch;
- `FACT_CURRENCY_GATE = BLOCKED` for final application use;
- no new factual wording should be inferred from chat history, model memory, JD text, Skills, or the existence of later artifacts;
- `APPLICATION_READY = NO`.

## Rebase contract

The next source rebase must:

1. reread the current local `FCT-001`;
2. calculate and record its new SHA256;
3. assign a new source epoch;
4. diff semantic candidate facts against `FCT-EPOCH-20260913-7EAA096A`;
5. rebuild only affected DER / Claim Ledger entries unless the extraction structure itself requires broader regeneration;
6. revalidate affected Claim Maps / Resume text;
7. update `CURRENT_VERSION_INDEX.md` and `GATE_REGISTRY.json`.

Chat history, old snapshots and public derived files can never override `FCT-001`.
