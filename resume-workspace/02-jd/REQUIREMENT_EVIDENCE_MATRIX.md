# Requirement Evidence Matrix

JD 真源：`JD-001`（`JD母版.docx`）。证据真源：`FCT-001` 与 `CLAIM_LEDGER.md`。以下是岗位族基线阶段的要求映射；它不是某一条真实 JD 的最终匹配，也不产生伪精确匹配百分比。

当前映射已重基于：`FCT-EPOCH-20260916-04094915`。

| role family | JD_SOURCE requirements | direct evidence | transferable / project evidence | gap or blocker | baseline decision |
|---|---|---|---|---|---|
| R1 Agent Eval / LLM Quality | Eval design、Case/Dataset、QA、Badcase、Metrics、Data Quality、Regression、Root Cause；P1 的 Agent/RAG/Tool/Trajectory | FCT-02–FCT-08、FCT-43–FCT-54；其中新增评测类目补充、Badcase 分类、修改后复测、多轮/Tool/Step/信息完整性评测、基础 SQL/查询取数、评测资产类型 | FCT-24–FCT-28、FCT-55；Agent Eval 资产已有部分 repo 核验，含 40 Cases 的 24/8/8 结构、negative controls 与 deterministic metrics | Python 实际工作使用未确认；正式自动评测平台 Owner / 自动化评测工程仍无直接工作证据 | Core baseline，主投方向；当前证据强于上一 epoch |
| R2 Business FDE / AI Delivery | 场景发现、需求定义、Solution、Workflow、Integration、Eval、Acceptance、Badcase、客户培训 | FCT-12–FCT-15、FCT-21–FCT-23、FCT-33–FCT-35、FCT-41–FCT-46、FCT-50、FCT-53、FCT-56–FCT-57 | FCT-24–FCT-28、FCT-55 覆盖 Agent 边界、验收、评测和 Prompt/Instruction iteration | 真实 AI 客户交付、接口文档、CRM/ERP/WMS 客户集成、正式 Go-live 未确认 | Core baseline，强调业务型 FDE；新增项目排期/阶段检查/方案汇报证据 |
| R3 AI Commerce | Merchant/Category、Search/Query/Relevance、GMV、CTR/CVR/ROI、Marketing、Seller、Service、SOP | FCT-09–FCT-23、FCT-31–FCT-42、FCT-52、FCT-56–FCT-57 | FCT-02–FCT-08、FCT-43–FCT-54 提供 Data Agent、Query/Relevance、SQL/数据背景；FCT-24–FCT-28 为 Agent 项目补充 | Merchant Agent / Commerce Agent API Workflow 的生产直接经验未明示 | Core baseline，和 R1/R2 同级；业务端证据仍最完整 |
| R4 AI Product Ops / Intelligent Service | Customer Need、Dialogue/Scenario、Knowledge/Prompt、Launch、QA、Data Diagnosis、Badcase、Optimization | FCT-03–FCT-06、FCT-32–FCT-33、FCT-38–FCT-40、FCT-43–FCT-54、FCT-56 | FCT-24–FCT-28、FCT-55 的客服 Agent、Prompt/Instruction、Evidence、安全/评测设计 | 正式产品 Roadmap / PRD Owner、对话产品上线 Owner、真实客服机器人产品 Go-live 未确认 | Core baseline；更适合验证 AI 产品质量运营 / 场景运营，而非强写传统 PM Owner |
| R5 Prompt / Agent Solution | Customer Problem、Scenario、Prompt/Knowledge/Workflow、Eval、Tuning、SOP/Standard | FCT-43–FCT-55，尤其 FCT-51、FCT-54、FCT-55 | FCT-24–FCT-28 已有部分 repo 核验，包含 Tool/Evidence/Authority/Eval 及 Frozen Case 结构；传统业务经历提供真实需求场景 | 正式客户 Prompt 调优交付、生产 RAG/Agent 上线 Owner、深工程栈仍无直接工作证据 | Core baseline；当前 Prompt/Instruction iteration 已有直接事实，不再只是概念性项目描述 |
| R6 MaaS / AI Solution / Pre-sales | Customer Need、Qualification、Solution、Demo/POC、Technical Communication、Delivery Handoff、Business Result | FCT-12–FCT-15、FCT-20–FCT-23、FCT-33–FCT-35、FCT-41–FCT-42、FCT-56–FCT-57 | FCT-24–FCT-28、FCT-55 可支撑技术/Agent 边界与 Acceptance 的项目叙述 | AI 售前、商机资格判断、Demo、POC、投标、AI 成交和客户 Go-live 未被事实源直接确认 | Core supplementary baseline；可强化 Solution Communication，但必须保留转型边界 |
| R7 Agent Application Engineer | Workflow、Task Decomposition、Tool Calling、Memory、Prompt、RAG、API/Plugin、Multi-Agent；工程岗还要求 LangGraph/LlamaIndex/Redis/Milvus 等 | FCT-24–FCT-28、FCT-55 提供部分 Agent/Prompt/Eval 证据；FCT-52 只有基础 SQL/查询取数 | 项目仓库部分已核验，但本人实现边界仍是 Problem Definition / Trade-off / Eval / Acceptance + AI Coding Agent 协作 | 底层工程实现、生产 Agent、LangGraph/LlamaIndex/Redis/Milvus 等直接证据不足 | 继续作为 Stretch；不因 Prompt/Eval 证据增加而升级为工程主投基线 |

## Common capability classification

- `DIRECT_EVIDENCE`：当前 Fact Master 中明确出现的评测、业务经营、数据分析、SQL 基础使用、项目推进、方案汇报、SOP / 评测资产、跨团队协同、Prompt / Instruction iteration。
- `TRANSFERABLE_EVIDENCE`：电商经营与搜索/相关性经验迁移到 AI Commerce、FDE、Product Ops 和 Solution Communication；必须标明迁移关系。
- `PROJECT_EVIDENCE`：Agent Builder 中 Problem Definition、Boundary、Tool/Evidence/Authority、Eval、Frozen Cases、Prompt/Instruction iteration；其中部分 Eval / README 证据已 `REPO_PARTIALLY_VERIFIED`，但仍不是生产/客户证据。
- `EXPRESSION_GAP`：可以由措辞、模块顺序、证据排序和岗位关键词改善的缺口。
- `EVIDENCE_GAP`：事实源仍没有明确给出 Python 实际工作使用、真实 AI 客户交付、Demo/POC、正式产品上线 Owner、生产 Agent 工程实现等证据。
- `REAL_GAP/HARD_BLOCKER`：R7 的工程深度要求；另有单条 JD 可能要求的学历、年限、特定技术栈和真实在招状态，必须等单条 JD 冻结后判断。

## Current interpretation after JD evidence audit

真实 JD 追问的作用是发现“Fact Master 有没有漏掉已经做过的证据”，而不是把 JD 要求写成候选人事实。本轮已确认并补回的内容，明显降低了 R1/R4/R5 的表达型缺口，但没有消除真实 AI 客户交付、Demo/POC、产品上线 Owner 或深工程实现等硬缺口。
