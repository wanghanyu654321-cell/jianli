# Source Index

## Current governance notice

- `FACT_SOURCE_OF_TRUTH` = `FCT-001`。
- 当前 GitHub canonical representation = `resume-workspace/01-facts/FACT_MASTER_CURRENT.md`。
- Current source epoch = `FCT-EPOCH-20260916-D0C724C3`。
- Canonical Git blob SHA = `d0c724c31d2742f35a7870fb2f37c93a153cd47a`。
- `SOURCE_CURRENCY = CURRENT`。
- 本地 `简历母版.docx` 是 FCT-001 的此前外部表示；2026-09-16 用户明确确认将本轮新增事实补入 GitHub 后，GitHub 工作流以 `FACT_MASTER_CURRENT.md` 为当前事实母版。若本地 DOCX 尚未同步，不得用旧外部副本覆盖当前 epoch 已确认事实。
- Known later external DOCX fingerprint before repository canonicalization: `38A34FF8CF39A4D69AF20FD043C170D15A8DD0A882A8414A5311CF0FE52E140C`。
- Previous repository frozen epoch = `FCT-EPOCH-20260913-7EAA096A`；previous SHA256 = `7EAA096A7220DE0609E3AACAEA656B4CEEFB006D1419FA01BC07E97FFFCDDDEB`。
- `JD_SOURCE_OF_TRUTH` = `JD-001`，唯一岗位市场源；不能替代真实 Single-JD。
- `CLAIM_LEDGER` = `resume-workspace/01-facts/CLAIM_LEDGER.md`，当前绑定 `FCT-EPOCH-20260916-D0C724C3`。
- `CANONICAL_TIMELINE` = `resume-workspace/00-source/CANONICAL_TIMELINE.md`。
- `SOURCE_FREEZE` = `resume-workspace/00-source/SOURCE_FREEZE.md`。
- `CURRENT_VERSION_INDEX` = `resume-workspace/CURRENT_VERSION_INDEX.md`。
- `GATE_REGISTRY` = `resume-workspace/GATE_REGISTRY.json`。
- `ROLE_BASELINE_WRITING_MODULE` = `resume-workspace/00-source/ROLE_BASELINE_WRITING_MODULE.md`。

## Confirmed sources

| source_id | representation | path | type | authority | purpose | current note |
|---|---|---|---|---|---|---|
| FCT-001 | FACT_MASTER_CURRENT.md | `resume-workspace/01-facts/FACT_MASTER_CURRENT.md` | FACT | Highest | 候选人事实、责任边界、数字口径、项目状态 | `CURRENT`；2026-09-16 repository canonicalization。 |
| FCT-001-PREV | 简历母版.docx | 本地源文件（未上传） | FACT_ARCHIVE | Historical upstream representation | 历史事实母版 | 尚未声明已同步当前 GitHub epoch；不得覆盖当前已确认事实。 |
| JD-001 | JD母版.docx | 本地源文件（未上传） | JD | Highest for market requirements | 岗位族、Core/Stretch、能力矩阵、关键词 | 不能替代单条真实 JD。 |
| POL-001 | ROLE_BASELINE_WRITING_MODULE | `resume-workspace/00-source/ROLE_BASELINE_WRITING_MODULE.md` | POLICY | User instruction | 岗位族结构、证据优先级、写作约束 | 不产生候选人事实。 |
| INS-001 | RESUME_BUILD_PIPELINE_V2 | 用户提供的本地规则附件（未上传） | SUPPORT | User instruction | 来源隔离、职责分工、停止条件 | 不产生事实。 |
| INS-002 | Resume Output & Tailoring Rules | 用户提供的本地规则附件（未上传） | SUPPORT | User instruction | Master / Role Baseline / Single-JD 输出规则 | 不产生事实。 |
| SKL-001/002/003 | Resume Skills / manifests | 本地安装资源 | SKILL | Operational | 工作流、审查职责 | 不产生事实。 |

## Repository evidence status

企业客服 Agent / Support Agent 的工程项目继续保持 `DOCUMENTED_ONLY / REPO_NOT_VERIFIED`。事实母版中出现技术栈、测试结果或设计边界，不等于仓库实现或生产状态已经独立核验。

## Source resolution rule

1. 当前 `FCT-001 / FACT_MASTER_CURRENT.md` 高于旧 DER、旧 Claim Ledger、Role Resume、JD、Skill、模型推测和未确认记忆。
2. `CANONICAL_TIMELINE.md` 与 FCT-001 的时间轴必须一致；时间线冲突时 `TIMELINE_GATE = FAIL`。
3. JD 只能产生岗位要求、能力矩阵和关键词，不产生候选人事实。
4. Skill / Policy 只产生流程约束，不产生候选人事实。
5. 新事实进入 FCT-001 前必须由用户明确确认；模糊回忆保留在待确认 / exclude 区，不得自动升级。
6. FCT-001 每次发生语义变化都创建新的 Source Epoch；旧 epoch 保留为历史证据。
7. Source Rebase 必须先做 semantic delta，再更新 Claim Ledger 和受影响 Resume artifact。
8. Role 可以重新解释能力、改变证据排序与展开深度，但不得改写历史：`ROLE MAY REINTERPRET CAPABILITY. ROLE MAY NOT REWRITE HISTORY.`

当前结论：事实源已完成 2026-09-16 GitHub canonicalization；现有 R1–R3 Resume artifact 尚未按新 epoch 完成语义重验，R4–R6 后续重写也必须从当前 FCT-001 生成。
