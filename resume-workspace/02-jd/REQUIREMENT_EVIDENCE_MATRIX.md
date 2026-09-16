# Requirement Evidence Matrix

JD 真源：`JD-001`（`JD母版.docx`）。证据真源：`FCT-001` 与 `CLAIM_LEDGER.md`。以下是岗位族基线阶段的要求映射；它不是某一条真实 JD 的最终匹配，也不产生伪精确匹配百分比。

当前映射已重基于：`FCT-EPOCH-20260916-FE4CB619`。

| role family | JD_SOURCE requirements | direct evidence | transferable / project evidence | gap or blocker | baseline decision |
|---|---|---|---|---|---|
| R1 Agent Eval / LLM Quality | Eval design、Case/Dataset、QA、Badcase、Metrics、Data Quality、Regression、Root Cause；P1 的 Agent/RAG/Tool/Trajectory | FCT-02–FCT-08、FCT-43–FCT-54；含评测类目补充、Badcase 分类、修改后复测、多轮/Tool/Step/信息完整性评测、基础 SQL/查询取数、评测资产类型 | FCT-24–FCT-28、FCT-55、FCT-58；Agent Eval 资产已有部分 repo 核验，且当前服务 Demo / POC 与上线前验证 | Python 实际工作使用未确认；正式自动评测平台 Owner / 自动化评测工程、生产流量 Eval 仍无直接工作证据 | Core baseline，主投方向；Demo/POC 使 Eval→Delivery 链更完整 |
| R2 Business FDE / AI Delivery | 场景发现、需求定义、Solution、Workflow、Integration、Eval、Acceptance、Badcase、客户培训 | FCT-12–FCT-15、FCT-21–FCT-23、FCT-33–FCT-35、FCT-41–FCT-46、FCT-50、FCT-53、FCT-56–FCT-58 | FCT-24–FCT-28、FCT-55 提供 Agent 边界、Prompt/Instruction、Eval / Acceptance；FCT-58 提供直接 Demo / POC Delivery 与 pre-launch | 正式 production Go-live、真实企业客户验收主体、CRM/ERP/WMS 等客户系统集成仍未确认 | Core baseline；已经有直接 Demo/POC Delivery，不再把 POC 作为纯缺口 |
| R3 AI Commerce | Merchant/Category、Search/Query/Relevance、GMV、CTR/CVR/ROI、Marketing、Seller、Service、SOP | FCT-09–FCT-23、FCT-31–FCT-42、FCT-52、FCT-56–FCT-57 | FCT-02–FCT-08、FCT-43–FCT-54 提供 Data Agent、Query/Relevance、SQL/数据背景；FCT-24–FCT-28、FCT-58 为 Agent Demo/POC 补充 | Merchant Agent / Commerce Agent 的生产业务结果、商家 AI 正式上线 Owner 未明示 | Core baseline；AI 侧可信度增强，但核心仍是完整 Commerce 经营证据 |
| R4 AI Product Ops / Agent Product / Intelligent Service | Customer Need、Dialogue/Scenario、Knowledge/Prompt、Launch、QA、Data Diagnosis、Badcase、Optimization | FCT-03–FCT-06、FCT-32–FCT-33、FCT-38–FCT-40、FCT-43–FCT-54、FCT-56、FCT-58 | FCT-24–FCT-28、FCT-55 的客服 Agent、Prompt/Instruction、Evidence、Eval 设计；FCT-58 提供实际落地、Demo/POC、pre-launch；FCT-59 记录 PRD 为待补资产 | 正式 PRD 尚未完成/核验；Roadmap Owner、正式上线后用户/产品指标与完整生命周期 Owner 仍缺 | Core baseline；定位可从纯 Quality Ops 扩展到 AI Product Ops / Agent Product，但暂不强写传统 PM Owner |
| R5 Prompt / Agent Solution | Customer Problem、Scenario、Prompt/Knowledge/Workflow、Eval、Tuning、SOP/Standard | FCT-43–FCT-55、FCT-58，尤其 FCT-51、FCT-54、FCT-55、FCT-58 | FCT-24–FCT-28 已有部分 repo 核验，包含 Tool/Evidence/Authority/Eval 及 Frozen Case 结构；Demo/POC 说明这些能力进入交付验证 | 深工程栈、生产 Agent 运维、企业客户 Prompt 调优与 SLA 仍无直接证据 | Core baseline；已具 Prompt/Instruction + Eval + Demo/POC 的完整项目证据链 |
| R6 AI Solution / Solution Consultant / Agent Delivery | Customer Need、Qualification、Solution、Demo/POC、Technical Communication、Delivery Handoff、Business Result | FCT-12–FCT-15、FCT-20–FCT-23、FCT-33–FCT-35、FCT-41–FCT-42、FCT-56–FCT-58 | FCT-24–FCT-28、FCT-55 提供技术 / Agent Boundary 与 Acceptance；FCT-58 直接补足 Demo / POC Delivery 与 pre-launch | 未确认真实企业客户 POC 甲方/验收主体、商机资格判断、投标/采购、AI 成交、正式 production Go-live、复杂企业系统集成 | Core baseline；Demo/POC 不再是缺口，岗位定位从 transition 进一步收敛到业务型 AI Solution / Agent Delivery |
| R7 Agent Application Engineer | Workflow、Task Decomposition、Tool Calling、Memory、Prompt、RAG、API/Plugin、Multi-Agent；工程岗还要求 LangGraph/LlamaIndex/Redis/Milvus 等 | FCT-24–FCT-28、FCT-55、FCT-58 提供部分 Agent/Prompt/Eval/POC 证据；FCT-52 只有基础 SQL/查询取数 | 项目已有 Demo/POC 和部分仓库核验，但本人实现边界仍是 Problem Definition / Trade-off / Eval / Acceptance + AI Coding Agent 协作 | 底层工程实现、生产 Agent、LangGraph/LlamaIndex/Redis/Milvus 等直接证据不足 | 继续作为 Stretch；Demo/POC 不等于工程深度达标 |

## Common capability classification

- `DIRECT_EVIDENCE`：当前 Fact Master 中明确出现的评测、业务经营、数据分析、SQL 基础使用、项目推进、方案汇报、SOP / 评测资产、跨团队协同、Prompt / Instruction iteration，以及 Agent Demo / POC Delivery / pre-launch。
- `TRANSFERABLE_EVIDENCE`：电商经营与搜索/相关性经验迁移到 AI Commerce、FDE、Product Ops 和 Solution Communication；必须标明迁移关系。
- `PROJECT_EVIDENCE`：Agent Builder 中 Problem Definition、Boundary、Tool/Evidence/Authority、Eval、Frozen Cases、Prompt/Instruction iteration、Demo/POC 与上线准备；部分 Eval / README 证据已 `REPO_PARTIALLY_VERIFIED`，当前交付状态由用户明确确认，但仍不是生产流量或企业客户成交证据。
- `PENDING_ASSET`：正式 PRD；项目具备真实产品上下文，但 PRD 尚未作为已完成资产核验。
- `EXPRESSION_GAP`：可以由措辞、模块顺序、证据排序和岗位关键词改善的缺口。
- `EVIDENCE_GAP`：事实源仍没有明确给出 Python 实际工作使用、正式企业客户采购/成交、复杂企业系统集成、产品上线后指标闭环、生产 Agent 工程运维等证据。
- `REAL_GAP/HARD_BLOCKER`：R7 的工程深度要求；另有单条 JD 可能要求的学历、年限、特定技术栈和真实在招状态，必须等单条 JD 冻结后判断。

## Current interpretation after Demo / POC status update

本轮最重要的变化是：`Demo / POC` 已从 R2 / R6 的缺口变为直接项目证据，R4 / R5 也因此获得更强的实际落地链路。真正剩余的硬缺口被重新收窄到 production Go-live、企业客户成交/验收、复杂系统集成、正式 PRD / Roadmap、上线后产品指标和深工程实现。
