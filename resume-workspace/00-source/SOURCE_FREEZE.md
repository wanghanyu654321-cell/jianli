# Source Freeze

## Current fact-master epoch

- Source ID: `FCT-001`
- Current GitHub mirror: `resume-workspace/01-facts/FACT_MASTER_CURRENT.md`
- Source epoch: `FCT-EPOCH-20260916-04094915`
- Git blob SHA: `040949158e76a356caf81f4185da2c4a17528e04`
- Freeze date: `2026-09-16`
- Source currency: `CURRENT`

## Freeze basis

本 epoch 只冻结以下范围：

1. 当前主线中已经确认并持续使用的事实；
2. 用户在 2026-09-16 对朗臻、今宜、人瑞补充和确认的工作上下文、判断逻辑与责任边界；
3. 用户在真实 JD 能力缺口核对中明确确认的新事实，包括评测类目、Badcase 分类、修改后复测、多轮 / Tool / Step / 信息完整性评测、基础 SQL / 查询取数、修改后跟进验证、评测资产类型、Prompt / System / Tool Instruction 迭代、项目排期与方案汇报；
4. 当前主线 Agent Builder 项目的既有事实，以及 2026-09-16 已独立查看仓库后能够确认的部分 Eval 资产结构与项目边界。

明确不采用“旧仓库 / 旧 Claim / 旧快照出现过就自动恢复”的策略。未被当前主线使用、且本轮未明确要求恢复的历史旁支内容，不进入当前事实母版。

本地 `简历母版.docx` 与 GitHub mirror 如存在差异，不自动互相覆盖；后续同步前先以用户最新明确确认的事实校准。

## Previous epochs

### Immediate repository predecessor
- Epoch: `FCT-EPOCH-20260916-6D82DB08`
- Git blob SHA: `6d82db084b0bef7ec1967982ebb36213942fd571`
- Status: `SUPERSEDED_BY_JD_EVIDENCE_ENRICHMENT`
- Reason: 真实 JD 能力核对后，用户确认了多项此前未完整进入事实母版的直接证据，并完成 Agent Eval 资产的部分仓库核验。

### Earlier repository epoch
- Epoch: `FCT-EPOCH-20260916-D0C724C3`
- Status: `SUPERSEDED_BY_SCOPE_CLEANUP`
- Reason: 首次 GitHub 母版迁移时混入了旧快照范围假设和未在本轮确认的旁支 exclusion；后续 epoch 已清理。

### External DOCX fingerprint before GitHub context supplement
- Epoch: `FCT-EPOCH-20260915-38A34FF8`
- SHA256: `38A34FF8CF39A4D69AF20FD043C170D15A8DD0A882A8414A5311CF0FE52E140C`
- Note: 包含已确认的 `单月达人合作销售额合计 10 万元+` 口径；2026-09-16 后续又补充了大量工作上下文。

### Earlier repository freeze
- Epoch: `FCT-EPOCH-20260913-7EAA096A`
- SHA256: `7EAA096A7220DE0609E3AACAEA656B4CEEFB006D1419FA01BC07E97FFFCDDDEB`
- Status: `SUPERSEDED`

## Semantic delta in current epoch

相对 `FCT-EPOCH-20260916-6D82DB08`，本次新增 / 修正：

### 人瑞 Data Agent
- 明确：正式任务框架通常由正式员工确定，但本人会在真实 Case 中参与定义 / 补充评测类目；
- 补充：存在稳定 Badcase 分类 / 归因；
- 补充：规则、SOP、示例或执行方式修改后会做复测 / 后续抽检验证，现有一致性改善数字来自持续治理与验证闭环；
- 补充：评测范围还包括多轮上下文、工具调用结果、步骤完整性、信息收集完整性和最终回答是否解决 Query；
- 补充：本人可阅读简单 SQL、做基础查询取数；所服务 Data Agent 具备自动生成 SQL 指令能力，日常数据通常脱敏；
- 补充：问题反馈后部分事项会继续跟进修改结果并参与补充验证，但通常是补充 / 反馈 / 验证角色；
- 补充：团队评测资产包括任务说明、评测标准 / 判断说明、Case / 示例、FAQ、问题清单等，本人负责 / 参与其中一部分；
- 修正：`10+ SOP / 规则 / 执行文档` 明确为团队累计沉淀规模，本人负责 / 参与其中一部分；
- 修正：时间趋势只保留“按时间维度”，删除此前未明确确认的“小时 / 日”精确粒度。

### Agent Builder
- 用户确认项目实际迭代过 Prompt、System Instruction、Tool Instruction，并结合 Badcase / 测试结果 / 通过情况比较版本差异；
- 已独立查看 `wanghanyu654321-cell/-agent` / `job-ready/integration-v1` 的顶层 README 与 `evals/job-ready-rag`；
- 核验 40 Cases 的 `24 answerable / 8 no-answer / 8 ambiguous` 结构、gold / expected version / provenance、negative controls 与 deterministic metrics；
- 保留项目自身声明的限制：retrieval-quality threshold 未独立批准，不声称 overall PASS；项目仍是 synthetic portfolio / proof application，不升级为生产 / 客户项目；
- 因此项目证据状态由统一 `REPO_NOT_VERIFIED` 收窄为“部分 Eval / README 证据 `REPO_PARTIALLY_VERIFIED`，其余未逐项核验内容仍按文档边界使用”。

### 朗臻 / 今宜
- 两段经历均补充需求 / 事项清单、优先级判断、项目排期和阶段检查；
- 朗臻补充面向老板的运营 / 项目方案与进展汇报；
- 今宜补充代运营场景下向合作方做运营方案 / 项目进展汇报；
- 明确上述内容属于运营 / 项目 Delivery 与 Stakeholder Communication，不升级为 PRD / Roadmap Owner、AI Demo / POC 或真实 AI 客户交付。

### 清理
- 朗臻平台工具中移除未被用户确认的 `天猫引力魔方`；
- 当前 Fact Master 仍不包含水果生鲜创业项目、悦客 AI Coach、九米六业务等未要求进入当前主线的历史旁支。

## Downstream state

- `CLAIM_LEDGER.md`: 已重新对齐到 `FCT-EPOCH-20260916-04094915`。
- `CANONICAL_TIMELINE.md`: 未变化；Timeline Gate 保持 PASS。
- R1–R6 V4 drafts: 写于上一 epoch，事实层新增内容会影响 R1/R2/R3/R4/R5/R6 的证据选择与措辞，需重新做 Skills 优化和 Semantic Claim Check。
- `APPLICATION_READY = NO`，直到对应 Role Baseline、Single-JD、ATS / Render Gate 完成。

## Rebase contract

以后任何事实语义变化：
1. 先确认是否属于当前主线或用户明确新增内容；
2. 未确认的历史旁支不得自动恢复；
3. 用户明确确认后更新 `FACT_MASTER_CURRENT.md`；
4. 创建新 Source Epoch；
5. 做 semantic delta；
6. 更新受影响 Claim Ledger；
7. 重验受影响 Resume artifact；
8. 刷新 `CURRENT_VERSION_INDEX.md` 和 `GATE_REGISTRY.json`。
