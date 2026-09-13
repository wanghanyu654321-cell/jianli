# Requirement Evidence Matrix

JD 真源：`JD-001`（`JD母版.docx`）。证据真源：`FCT-001` 与 `CLAIM_LEDGER.md`。以下是岗位族基线阶段的要求映射；它不是某一条真实 JD 的最终匹配，也不产生伪精确匹配百分比。

| role family | JD_SOURCE requirements | direct evidence | transferable / project evidence | gap or blocker | baseline decision |
|---|---|---|---|---|---|
| R1 Agent Eval / LLM Quality | Eval design、Case/Dataset、QA、Badcase、Metrics、Data Quality、Regression、Root Cause；P1 的 Agent/RAG/Tool/Trajectory | FCT-02–FCT-06、FCT-08、FCT-28 | FCT-24–FCT-27 为项目材料描述，当前 `DOCUMENTED_ONLY` | Python/SQL/自动评测没有在事实源中明确；仓库未核验 | Core baseline，主投方向 |
| R2 Business FDE / AI Delivery | 场景发现、需求定义、Solution、Workflow、Integration、Eval、Acceptance、Badcase、客户培训 | FCT-03、FCT-06、FCT-12–FCT-15、FCT-21–FCT-23、FCT-28 | FCT-24–FCT-27 覆盖 Agent 边界、验收和评测设计（项目证据） | 客户交付、接口文档、CRM/ERP/WMS 未被事实源确认 | Core baseline，强调业务型 FDE |
| R3 AI Commerce | Merchant/Category、Search/Query/Relevance、GMV、CTR/CVR/ROI、Marketing、Seller、Service、SOP | FCT-09–FCT-23，尤其 FCT-10、11、13、15、17–23 | FCT-24–FCT-27 可作 Agent 业务对象映射，但不是电商生产 Agent | Merchant Agent/API Workflow 直接经验未明示 | Core baseline，和 R1/R2 同级 |
| R4 AI Product Ops / Intelligent Service | Customer Need、Dialogue/Scenario、Knowledge/Prompt、Launch、QA、Data Diagnosis、Badcase、Optimization | FCT-03–FCT-08、FCT-12–FCT-15、FCT-28 | FCT-24–FCT-27 的客服 Agent、知识/安全/评测设计 | 对话流程上线、客服机器人产品 Owner 经历未确认 | Core baseline，保守使用“评测/质量/场景运营” |
| R5 Prompt / Agent Solution | Customer Problem、Scenario、Prompt/Knowledge/Workflow、Eval、Tuning、SOP/Standard | FCT-03、FCT-06、FCT-12、FCT-15、FCT-28 | FCT-21–FCT-27 有 Runtime/RAG/Tool/Authority/Safety/Eval 设计材料 | 正式客户方案、Prompt 调优交付没有直接工作经历 | Core baseline，项目与 SOP 并列 |
| R6 MaaS / AI Solution / Pre-sales | Customer Need、Qualification、Solution、Demo/POC、Technical Communication、Delivery Handoff、Business Result | FCT-12–FCT-15、FCT-20–FCT-23、FCT-28 | FCT-24–FCT-27 可支撑 POC/技术边界的项目叙述 | 售前、Demo、POC、商机资格判断未被事实源直接确认 | Core supplementary baseline，避免写成售前成交经验 |
| R7 Agent Application Engineer | Workflow、Task Decomposition、Tool Calling、Memory、Prompt、RAG、API/Plugin、Multi-Agent；工程岗还要求 LangGraph/LlamaIndex/Redis/Milvus 等 | FCT-24–FCT-28 仅有项目材料描述；FCT-03/FCT-08 有评测与搜索理解 | 项目中明确 Runtime、Tool、RAG、Safety、Eval；仓库未核验 | JD_MASTER 将其标为 Stretch；底层工程栈和生产实现证据不足 | 不生成岗位族基线；只保留 Gap/学习清单 |

## Common capability classification

- `DIRECT_EVIDENCE`：FCT-02–FCT-23、FCT-28 中直接出现的评测、业务经营、数据分析、项目推进、SOP、跨团队协同。
- `TRANSFERABLE_EVIDENCE`：电商经营与搜索/相关性经验迁移到 AI Commerce、FDE 和产品运营；必须标明迁移关系。
- `PROJECT_EVIDENCE`：FCT-24–FCT-27，当前只能写项目材料描述或测试集结果，不能升级为生产实现。
- `EXPRESSION_GAP`：可以由措辞、模块顺序和关键词排序改善的缺口。
- `EVIDENCE_GAP`：事实源没有明确给出 Python/SQL、客户交付、售前 Demo/POC、正式上线 Owner 等证据。
- `REAL_GAP/HARD_BLOCKER`：R7 的工程深度要求；另有单条 JD 可能要求的学历、年限和真实在招状态，必须等单条 JD 冻结后判断。
