# Source Index

## Current governance notice

- `FACT_SOURCE_OF_TRUTH` = `FCT-001`。
- 当前 GitHub mirror = `resume-workspace/01-facts/FACT_MASTER_CURRENT.md`。
- Current source epoch = `FCT-EPOCH-20260916-6D82DB08`。
- Current Git blob SHA = `6d82db084b0bef7ec1967982ebb36213942fd571`。
- `SOURCE_CURRENCY = CURRENT`。
- 当前 GitHub 事实母版只保存“当前主线已确认事实 + 用户明确补充确认的新上下文”；不会因为旧仓库、旧 Claim、旧快照里出现过某内容就自动恢复。
- 本地 `简历母版.docx` 与 GitHub mirror 如存在差异，不自动互相覆盖；先以用户最新明确确认的事实校准。
- Known external DOCX fingerprint before this mirror update: `38A34FF8CF39A4D69AF20FD043C170D15A8DD0A882A8414A5311CF0FE52E140C`。
- Previous repository epoch = `FCT-EPOCH-20260916-D0C724C3`。
- `JD_SOURCE_OF_TRUTH` = `JD-001`，唯一岗位市场源；不能替代真实 Single-JD。
- `CLAIM_LEDGER` = `resume-workspace/01-facts/CLAIM_LEDGER.md`，当前绑定 `FCT-EPOCH-20260916-6D82DB08`。
- `CANONICAL_TIMELINE` = `resume-workspace/00-source/CANONICAL_TIMELINE.md`。
- `SOURCE_FREEZE` = `resume-workspace/00-source/SOURCE_FREEZE.md`。
- `CURRENT_VERSION_INDEX` = `resume-workspace/CURRENT_VERSION_INDEX.md`。
- `GATE_REGISTRY` = `resume-workspace/GATE_REGISTRY.json`。
- `ROLE_BASELINE_WRITING_MODULE` = `resume-workspace/00-source/ROLE_BASELINE_WRITING_MODULE.md`。

## Confirmed sources

| source_id | representation | path | type | authority | purpose | current note |
|---|---|---|---|---|---|---|
| FCT-001 | FACT_MASTER_CURRENT.md | `resume-workspace/01-facts/FACT_MASTER_CURRENT.md` | FACT | Current GitHub mirror | 当前主线候选人事实、责任边界、数字口径、工作逻辑、项目状态 | `CURRENT`；只收录当前主线和用户明确确认的新上下文。 |
| FCT-001-EXT | 简历母版.docx | 本地源文件（未上传） | FACT | External representation | 事实母版本地表示 | 与 GitHub mirror 如有差异，需用户确认后同步，不能自动覆盖。 |
| JD-001 | JD母版.docx | 本地源文件（未上传） | JD | Highest for market requirements | 岗位族、Core/Stretch、能力矩阵、关键词 | 不能替代单条真实 JD。 |
| POL-001 | ROLE_BASELINE_WRITING_MODULE | `resume-workspace/00-source/ROLE_BASELINE_WRITING_MODULE.md` | POLICY | User instruction | 岗位族结构、证据优先级、写作约束 | 不产生候选人事实。 |
| INS-001 | RESUME_BUILD_PIPELINE_V2 | 用户提供的本地规则附件（未上传） | SUPPORT | User instruction | 来源隔离、职责分工、停止条件 | 不产生事实。 |
| INS-002 | Resume Output & Tailoring Rules | 用户提供的本地规则附件（未上传） | SUPPORT | User instruction | Master / Role Baseline / Single-JD 输出规则 | 不产生事实。 |
| SKL-001/002/003 | Resume Skills / manifests | 本地安装资源 | SKILL | Operational | 工作流、审查职责 | 不产生事实。 |

## Repository evidence status

企业客服 Agent / Support Agent 的工程项目继续保持 `DOCUMENTED_ONLY / REPO_NOT_VERIFIED`。事实母版中出现技术栈、测试结果或设计边界，不等于仓库实现或生产状态已经独立核验。

## Source resolution rule

1. 当前 GitHub 工作流读取 `FCT-001 / FACT_MASTER_CURRENT.md`；但该文件不得从旧快照、旧 Claim 或未确认记忆自动扩张事实范围。
2. `CANONICAL_TIMELINE.md` 与 FCT-001 的时间轴必须一致；时间线冲突时 `TIMELINE_GATE = FAIL`。
3. JD 只能产生岗位要求、能力矩阵和关键词，不产生候选人事实。
4. Skill / Policy 只产生流程约束，不产生候选人事实。
5. 新事实进入 FCT-001 前必须由用户明确确认；模糊回忆只保留在待确认区，不得自动升级。
6. FCT-001 每次发生语义变化都创建新的 Source Epoch；旧 epoch 保留为历史证据。
7. Source Rebase 必须先做 semantic delta，再更新 Claim Ledger 和受影响 Resume artifact。
8. Role 可以重新解释能力、改变证据排序与展开深度，但不得改写历史：`ROLE MAY REINTERPRET CAPABILITY. ROLE MAY NOT REWRITE HISTORY.`

当前结论：事实母版已清理到“当前主线 + 明确确认上下文”范围；现有 R1–R6 artifact 仍需按当前 epoch 重写 / 重验。
