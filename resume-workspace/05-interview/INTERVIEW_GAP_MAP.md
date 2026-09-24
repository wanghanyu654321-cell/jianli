# Interview Gap Map

更新时间：2026-09-24

## 结论

这批面试题验证了当前学习主线的方向：**先吃透真实 `-agent` POC，再补 JD 高频缺口，不要为每一道面经临时改项目。**

当前 `-agent` main 已演进到：Pi Agent Runtime、企业权限/业务状态、PostgreSQL、Governed RAG、FastAPI/pgvector、Harness/Eval、Durable Acceptance、AgentProfile、Public HTTPS、Live WeCom、DeepSeek bounded real-provider eval。

但这批题里有大量“他人项目/特定技术栈”问题，必须明确区分“会解释”与“做过”。

## P0 — 当前项目直接相关，第一阶段必须防守

### M2 Runtime & Context
- Agent Loop / Pi vs Product-owned Runtime
- AgentProfile vs SupportAgentRuntime
- Session 恢复与新旧会话边界
- Tool / Skill 加载与权限暴露
- Budget / Timeout / Abort / Fallback
- Event 监听与 Audit
- Context / Prompt / Skill / Session 的职责区别

### M3 Enterprise & Business
- Identity / Tenant / Store / Capability
- Ticket / Handoff / Idempotency
- Durable Business Truth
- PostgreSQL、事务、并发、副作用状态
- Request correlation / durable acceptance
- WeCom dedupe / routing / business state

### M4 Knowledge & Retrieval
- 知识库治理、Evidence Admission
- lexical/vector 两种现有路径
- FastAPI / pgvector
- Node canonical reconciliation
- Chunk / embedding / query / retrieval eval
- 注意：当前项目 **没有 BM25 + Vector Hybrid、RRF、Cross-Encoder reranker**，不能回答成“项目里用了”。

### M5 Harness & Eval
- Case / Suite / Config / Runner / Measurement
- Integrity vs Quality Eval
- Safety / Robustness / Holdout
- Badcase → Regression
- Durable Acceptance
- 业务指标、过程指标、稳定性、错误归因、人工裁决
- 这是用户过往 Eval 经历与当前 Agent 工程连接最强的模块

### M6 Delivery & Debugging
- Docker / Compose / CI
- HTTPS / Nginx / TLS
- Live WeCom
- Request debugging
- Logs / Linux / network boundary
- 外部服务失败如何定位

### M7 Code Ownership
- TS / Python / SQL
- trace HTTP → Runtime → Tool → DB/RAG
- 独立小改与小 bug 修复
- 面试现场打开代码解释

## P1 — 市场高频缺口，第二阶段补到“会设计/会映射”，不能冒充做过

- MCP vs Function Calling
- Multi-Agent 适用条件、Supervisor、冲突合并、单/多 Agent 对照评测
- LangGraph / LangChain 最小架构
- K8s
- Production Observability（Metrics / Tracing / Cost）
- Long-term Memory / Context Compression
- Human Approval Workflow / HITL
- Production Data Flywheel
- 基于 Eval + 人工确认的 Skill/Policy 自改进闭环
- Rate Limit / Circuit Breaker / Queue
- Local model deployment 基本排障

## P2 — 特定技术栈/高级专项，后续按岗位需求学习

以下不是当前 `-agent` 已实现能力：
- BM25 + Vector Hybrid
- RRF
- Cross-Encoder reranker
- Milvus 架构
- Redis + MySQL 双写/Checkpointer
- Lease / Fencing Token
- LangGraph checkpoint-specific persistence
- 多 Agent 并行代码审查 Supervisor
- 本地大模型完整部署栈

遇到这类题的回答口径：
1. 先明确“当前项目没有这样实现”；
2. 说明当前项目对应方案；
3. 再讲如果需要该能力会如何设计与验收。

## P3 — 通用基础，独立准备，不污染 Agent 主课程

- MySQL 索引
- Redis 缓存策略
- 分布式锁
- TCP/UDP
- 栈/堆
- 高频算法
- 大文件 Top-K

这些必须补，但采用独立短时训练，不把它们塞入 M2–M6。

## 这批题对学习计划的实际调整

不改变冻结的 M1–M8 顺序，只增加面试验收项：

- **M2 结束 Gate**：能讲 Agent Loop、Session、Skill、AgentProfile、Fallback、Event/Audit。
- **M3 结束 Gate**：能解释权限、幂等、Durable Truth、并发/重复副作用。
- **M4 结束 Gate**：能讲当前真实 RAG，并能明确解释“为什么项目没有 Hybrid/RRF/reranker，若加如何验证”。
- **M5 结束 Gate**：能回答评测集构建、覆盖、Badcase、人工裁决、自动化、回归、指标选择。
- **M6 结束 Gate**：能处理部署、日志、Linux、HTTP/网络、渠道错误的排障问法。
- **M7 结束 Gate**：能打开真实代码完成定位/修改。
- **M8**：集中补 MCP / Multi-Agent / LangGraph / K8s / Memory 等高频缺口。

## 对简历的直接反馈

这批题说明简历里任何技术名词都会被沿链路深挖。后续简历只保留：
- 可以给出真实文件/流程/证据的能力；
- 可以解释设计取舍与边界的能力；
- 可以复现数字来源的指标。

不应因为面经高频就把 BM25、RRF、Cross-Encoder、Milvus、Multi-Agent、LangGraph 等未实现项写成项目事实。
