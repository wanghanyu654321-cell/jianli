# Source Index

扫描范围：用户确认的本地对话资料目录（源文件未上传），以及本次工作区的生成物。初始扫描日期：2026-09-13。

## Current governance notice

- `FACT_SOURCE_OF_TRUTH` = `FCT-001`，唯一候选人事实源。
- Repository last frozen source epoch = `FCT-EPOCH-20260913-7EAA096A`。
- Repository last frozen fingerprint = `7EAA096A…CDDDEB`。
- `SOURCE_CURRENCY = STALE_PENDING_REBASE`：R1 V3 Audit 记录在上述 freeze 之后，本地 FCT-001 又发生了非时间轴指纹变化；最新本地 fingerprint 尚未写回仓库。
- `JD_SOURCE_OF_TRUTH` = `JD-001`，唯一岗位市场源；不能替代真实 Single-JD。
- `REPO_EVIDENCE` = 当前工作区未发现与事实母版所引用 GitHub 项目相匹配的本地 checkout；项目相关内容暂按 `DOCUMENTED_ONLY / REPO_NOT_VERIFIED` 处理。
- `CANONICAL_TIMELINE` = `resume-workspace/00-source/CANONICAL_TIMELINE.md`。
- `SOURCE_FREEZE` = `resume-workspace/00-source/SOURCE_FREEZE.md`，现表示“最后一次仓库已知冻结 epoch”，不是最新本地源已完成冻结的声明。
- `CURRENT_VERSION_INDEX` = `resume-workspace/CURRENT_VERSION_INDEX.md`，当前版本唯一入口。
- `GATE_REGISTRY` = `resume-workspace/GATE_REGISTRY.json`，当前 Gate 状态唯一注册表。
- `ROLE_BASELINE_WRITING_MODULE` = `resume-workspace/00-source/ROLE_BASELINE_WRITING_MODULE.md`。
- `SKILL_SOURCE` = `SKL-001`、`SKL-002` 及本地实际 `SKILL.md`；只决定流程与审查职责，不产生候选人事实。

## Confirmed sources

| source_id | filename | path | type | authority | purpose | current note |
|---|---|---|---|---|---|---|
| FCT-001 | 简历母版.docx | 本地源文件（未上传） | FACT | Highest | 候选人事实、责任边界、数字口径、项目状态 | Last repository freeze: `FCT-EPOCH-20260913-7EAA096A`; later local drift recorded; rebase pending. |
| JD-001 | JD母版.docx | 本地源文件（未上传） | JD | Highest for market requirements | 岗位族、Core/Stretch 分层、能力矩阵、关键词与城市用途 | 标题为“JD MASTER V3”；不能替代单条真实 JD。 |
| SKL-001 | 简历Skills安装报告.md | 本地安装报告（未上传） | SKILL | Operational | 来源、固定 commit、入口、依赖、冒烟证据 | 7 组、19 个入口；不是候选人事实。 |
| SKL-002 | resume-skills-source-manifest.json | 本地安装清单（未上传） | SKILL | Operational | 机器可读来源、版本、哈希和安装路径 | 以完整 SHA 固定；不是候选人事实。 |
| SKL-003 | sushen-resume-maker SKILL.md | 本地 Codex Skill 安装（未上传） | SKILL | Operational | Claim Ledger、JD Matrix、事实边界规则 | 只按事实源工作。 |
| INS-001 | RESUME_BUILD_PIPELINE_V2 | 用户提供的本地规则附件（未上传） | SUPPORT | User instruction | 来源隔离、职责分工和停止条件 | 规则文本，不是事实源或 JD 源。 |
| INS-002 | Resume Output & Tailoring Rules | 用户提供的本地规则附件（未上传） | SUPPORT | User instruction | Master、Role Baseline、Single-JD 三层输出与页数 | 规则文本，不是事实源或 JD 源。 |
| POL-001 | ROLE_BASELINE_WRITING_MODULE | `resume-workspace/00-source/ROLE_BASELINE_WRITING_MODULE.md` | POLICY | User instruction | 岗位族简历结构、完整职业履历、证据优先级、项目选择和写作约束 | `PROJECT_SELECTION = ROLE_DEPENDENT`；不产生候选人事实。 |
| DER-001 | 简历母版.txt | local `work/source-extracted/简历母版.txt` | SUPPORT | Derived | 从 FCT-001 派生的文本定位 | Repository Claim Ledger currently maps to last frozen epoch; latest local source rebase pending. |
| DER-002 | JD母版.txt | local `work/source-extracted/JD母版.txt` | SUPPORT | Derived | 从 JD-001 派生，便于行号核验 | 不能取代原 DOCX。 |

## Repository evidence scan

事实源引用 `wanghanyu654321-cell/-agent` 与 `job-ready/integration-v1`。当前记录未发现对应 checkout；同目录其他仓库不能冒充客服 Agent 仓库。因此项目证据仍维持 `DOCUMENTED_ONLY / REPO_NOT_VERIFIED`，除非当前任务明确进入 Repo Verification 阶段。

## Source resolution rule

1. FCT-001 永远高于 DER、Claim Ledger、Resume、聊天上下文和模型记忆。
2. JD-001 只能产生岗位要求、能力矩阵和关键词，不产生候选人事实。
3. Skill / Policy 只产生流程约束，不产生候选人事实。
4. 每次 FCT-001 指纹发生变化都必须创建新的 Source Epoch；旧 epoch 继续保留为历史证据，不得静默覆盖。
5. 下游 artifact 必须能够说明其 `derived_from_source_epoch`；如果 artifact 的 epoch 早于当前本地事实源而 rebase 未完成，则 `FACT_CURRENCY_GATE = BLOCKED`。
6. Source Rebase 必须优先做 semantic delta，再重建受影响 DER / Claim Ledger / Claim Map，避免无差别重写。

当前结论：Canonical Timeline 仍按 V3 Audit 记录保持一致；非时间轴事实源漂移仍待 rebase。
