# Source Freeze

## Current canonical source epoch

- Source ID: `FCT-001`
- Canonical repository representation: `resume-workspace/01-facts/FACT_MASTER_CURRENT.md`
- Source epoch: `FCT-EPOCH-20260916-D0C724C3`
- Canonical Git blob SHA: `d0c724c31d2742f35a7870fb2f37c93a153cd47a`
- Canonicalization date: `2026-09-16`
- Source currency: `CURRENT`

## Canonicalization basis

本 epoch 将以下内容合并为当前 GitHub 事实母版：

1. 此前 `FCT-001 / 简历母版.docx` 已确认事实；
2. 仓库前一冻结 epoch 的 Claim；
3. 用户在 2026-09-16 对朗臻、今宜、人瑞新增上下文和责任边界的逐项确认；
4. 用户明确要求将确认后的事实母版补入 GitHub。

从本 epoch 起，GitHub 工作流读取 `FACT_MASTER_CURRENT.md` 作为当前 FCT-001 canonical representation。本地 `简历母版.docx` 若尚未手工同步，属于此前外部表示，不得覆盖当前 epoch 已确认事实。

## Historical source epochs

### Immediate external predecessor
- Known external DOCX epoch: `FCT-EPOCH-20260915-38A34FF8`
- SHA256: `38A34FF8CF39A4D69AF20FD043C170D15A8DD0A882A8414A5311CF0FE52E140C`
- Note: included the clarified FCT-15 wording `单月达人合作销售额合计 10 万元+`; later 2026-09-16 conversation added substantial context not yet represented by that external fingerprint.

### Previous repository freeze
- Epoch: `FCT-EPOCH-20260913-7EAA096A`
- SHA256: `7EAA096A7220DE0609E3AACAEA656B4CEEFB006D1419FA01BC07E97FFFCDDDEB`
- Status: `SUPERSEDED`

### Older history
- SHA256: `B31C7EC90FFEB48B023E43C37CBACB08817A562B3A42C1148B34DFE3BA4FB6E1` — `SUPERSEDED`
- SHA256: `037FB4FA3B77157F5DBE201971E3962241DC897FCAF39DC903897A327518528D` — `SUPERSEDED`

## Semantic delta in 2026-09-16 epoch

Major confirmed changes include:

- Langzhen: 0→1 market-first decision logic; keyword trend as market signal; consumer calls; dog-food→cat-food product input; factory requirement detailing; direct JD xiaoer contract/gross-margin discussion; promotion-fee vs fixed-commission trade-off; activity goods/value negotiation; inventory planning, tail-stock clearance and cross-warehouse transfer; Xiaohongshu strategy/management boundary; Tmall 引力魔方 usage/contact.
- Jinyi: 7w→43w corrected to new-account 0→1 growth, not mature-account rescue; content/internal capability before traffic amplification; corn-bun repositioning to fitness/light-meal; visual scene design; live/video test loop; dual-camera design; direct media-buying responsibility; CTR/CVR diagnosis; controlled-variable A/B habit; business-goal alignment with owner; influencer cold-start strategy, direct BD, pure-commission and +3–5pt commission trade-off; monthly influencer sales 10w+.
- Renrui: upstream-document interpretation/alignment; self-run before distribution; pre-delivery logic/context gap detection; BPO hidden-context discovery; boundary-first training; efficiency + correctness; execution mental-model root cause; QA→rule/context/workflow feedback; progress/risk traceability; time-based business metric observation.
- Cross-role: Langzhen/Jinyi 0→1 characteristic and stable problem-solving logic recorded as interpretation layer; SOP explicitly not forced as every Proof Unit endpoint.
- Pending metric names: eCTR/pCTR/eCVR/pCVR/UVCTR/Lift remain unconfirmed and excluded from formal claims.

## Downstream state after freeze

- `CLAIM_LEDGER.md`: rebased to this epoch.
- `CANONICAL_TIMELINE.md`: unchanged; timeline gate remains PASS.
- Existing R1–R3 Resume artifacts: require semantic revalidation/rewrite against this epoch.
- R4–R6: future rewrite must derive from this epoch.
- Agent project remains `DOCUMENTED_ONLY / REPO_NOT_VERIFIED`.
- `APPLICATION_READY = NO` until role baseline revalidation plus Single-JD/ATS/render gates as applicable.

## Rebase contract

For any future semantic fact change:
1. obtain explicit user confirmation;
2. update `FACT_MASTER_CURRENT.md`;
3. assign a new Source Epoch using the new canonical Git blob fingerprint;
4. diff semantic claims;
5. update only affected Claim Ledger entries;
6. revalidate affected Resume artifacts;
7. refresh `CURRENT_VERSION_INDEX.md` and `GATE_REGISTRY.json`.
