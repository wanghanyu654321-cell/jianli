# Source Index

扫描范围：用户确认的本地对话资料目录（源文件未上传），以及本次工作区的生成物。扫描日期：2026-09-13。

## Source of Truth

- `FACT_SOURCE_OF_TRUTH` = `FCT-001`，唯一候选人事实源；当前冻结指纹为 `7EAA096A…CDDDEB`。
- `JD_SOURCE_OF_TRUTH` = `JD-001`，唯一岗位市场源。
- `REPO_EVIDENCE` = 当前工作区未发现与事实母版所引用 GitHub 项目相匹配的本地 checkout；项目相关内容暂按 `DOCUMENTED_ONLY / REPO_NOT_VERIFIED` 处理。
- `CANONICAL_TIMELINE` = `resume-workspace/00-source/CANONICAL_TIMELINE.md`，不可变时间轴。
- `SOURCE_FREEZE` = `resume-workspace/00-source/SOURCE_FREEZE.md`，当前源指纹冻结。
- `SKILL_SOURCE` = `SKL-001`、`SKL-002` 及本地实际 `SKILL.md`；只决定流程与审查职责，不产生候选人事实。

## Confirmed sources

| source_id | filename | path | type | modified_time | authority | purpose | notes |
|---|---|---|---|---|---|---|---|
| FCT-001 | 简历母版.docx | 本地源文件（未上传） | FACT | 2026-09-13 21:00 local file time; core property modified 2026-09-13 09:42 UTC | Highest | 候选人事实、责任边界、数字口径、项目状态 | V3；active SHA256 `7EAA096A…CDDDEB`；旧指纹已 SUPERSEDED。 |
| JD-001 | JD母版.docx | 本地源文件（未上传） | JD | 2026-09-13 15:55 local file time;正文更新时间 2026-09-13 | Highest for market requirements | 岗位族、Core/Stretch 分层、能力矩阵、关键词与城市用途 | 标题为“JD MASTER V3”；唯一 JD 母版；不能替代单条真实 JD。 |
| SKL-001 | 简历Skills安装报告.md | 本地安装报告（未上传） | SKILL | 2026-09-13 | Operational | 来源、固定 commit、入口、依赖、冒烟证据 | 7 组、19 个入口；报告记载未找到 0、歧义 0、依赖失败 0。 |
| SKL-002 | resume-skills-source-manifest.json | 本地安装清单（未上传） | SKILL | 2026-09-13 | Operational | 机器可读来源、版本、哈希和安装路径 | 以完整 SHA 固定；不是候选人事实。 |
| SKL-003 | sushen-resume-maker SKILL.md | 本地 Codex Skill 安装（未上传） | SKILL | local install | Operational | 主编排器的 Claim Ledger、JD Matrix、事实边界规则 | 已读取；只按事实源工作。 |
| INS-001 | RESUME_BUILD_PIPELINE_V2 | 用户提供的本地规则附件（未上传） | SUPPORT | 2026-09-13 | User instruction | 规定来源隔离、职责分工和停止条件 | 规则文本，不是事实源或 JD 源。 |
| INS-002 | Resume Output & Tailoring Rules | 用户提供的本地规则附件（未上传） | SUPPORT | 2026-09-13 | User instruction | 规定 Master、Role Baseline、Single-JD 三层输出与页数 | 规则文本，不是事实源或 JD 源。 |
| DER-001 | 简历母版.txt | `work\source-extracted\简历母版.txt` | SUPPORT | 2026-09-13 generated after canonicalization | Derived | 646 paragraphs, 0 tables, 601 lines；从 FCT-001 派生，不能取代原 DOCX。 |
| DER-002 | JD母版.txt | `work\source-extracted\JD母版.txt` | SUPPORT | 2026-09-13 generated | Derived | DOCX 段落/表格抽取，便于行号核验 | 从 JD-001 派生，不能取代原 DOCX。 |

## Repository evidence scan

事实源在 `简历母版.txt:384` 引用 `wanghanyu654321-cell/-agent` 与 `job-ready/integration-v1`。本次仅在用户确认的当前本地资料目录和当前 2026-09-13 工作区内查找，未发现对应 checkout；同目录现有仓库 README 明确是 Seedance 集成项目，不能冒充客服 Agent 仓库。因此未调用 `repo-to-resume`，也未把 README、历史工作区或互联网内容写入事实账本。

## Source resolution result

两份母版均有明确 V3 标题；FCT-001 已写入用户确认的开始工作时间 2022.03 与毕业时间 2022.06。当前 Canonical Timeline 与 Source Freeze 已激活；所有后续简历必须通过 TIMELINE_GATE。
