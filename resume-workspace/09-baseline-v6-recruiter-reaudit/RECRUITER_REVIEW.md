# R1–R6 V6 Recruiter Re-audit

审查基准：`FCT-EPOCH-20260916-FE4CB619`。本轮新增关键事实：企业客服 Agent 项目基于实际落地目标推进，已形成可运行 Demo，当前进行 Demo / POC 交付与上线前验证，等待 ICP 相关手续完成后推进正式上线；正式 PRD 尚未作为已完成资产使用。

本审查站在招聘官 / Hiring Manager 的岗位族初筛视角，不替代真实 Single-JD，也不做伪精确打分。

## 总体判断变化

相对 V5，最大的变化不是“多了一个项目关键词”，而是 Agent 项目的证据性质发生了变化：

- 之前更接近 `proof application / portfolio evidence`；
- 现在可以直接证明 `实际落地目标 → Demo → POC 交付 / 验证 → 上线准备`；
- 但仍不能外推为 `已生产上线 / 规模化真实用户 / 企业采购成交 / 付费客户交付 / 复杂系统集成完成`。

因此 R2、R4、R5、R6 的直接证据明显增强，其中 R4 与 R6 的岗位定位变化最大。

---

# R1 Agent Eval / LLM Quality

## 15 秒首屏识别
招聘官应能快速识别：候选人有真实 Data Agent 评测、Query / Recall / Relevance、Badcase、QA、规则治理、Regression 和 Agent 行为评测经验，同时有结构化 Agent Eval 资产，并且这些资产正在服务一个实际落地目标下的 Demo / POC 项目。

## 为什么会继续看
- 人瑞仍是最强的正式工作直接证据；
- 多轮、Tool、Step、信息完整性与最终回答有效性，使经验更接近 Agent Eval 而非传统标注；
- 有任务规模、抽检比例、一致性变化和复测闭环；
- SQL 已是基础可用能力；
- 40 Frozen Cases、negative controls、deterministic metrics 不再只是 portfolio 装饰，而与 Demo / POC 上线前验证形成更完整的质量链路。

## 仍可能卡住
- Python 实际工作使用仍无直接证据；
- 没有正式自动评测平台 Owner / 自动化评测工程经历；
- 还没有生产流量上的线上 Eval / monitoring 证据。

## 高概率追问
- 80%→95%、60%→85%到底是什么一致性；
- 多轮 / Tool 行为评测如何定义通过；
- 40 Cases 为什么是 24/8/8；
- Demo / POC 上线前哪些 Eval 指标决定可继续推进；
- SQL 能做到什么程度；
- 哪些评测是你本人设计，哪些来自已有规则。

## 招聘官判断
R1 主线已经稳定。新增 Demo / POC 事实主要提升“Eval 是否真的服务交付”的可信度，不改变岗位主定位。

---

# R2 Business FDE / AI Delivery

## 15 秒首屏识别
招聘官现在应能看到：候选人不仅长期做需求澄清、项目优先级、多方推进和结果验证，还已经把一个 Agent 项目推进到可运行 Demo、POC 交付 / 验证和上线准备阶段。

## 为什么会继续看
- 朗臻 / 今宜有真实需求清单、优先级、排期、阶段检查和方案汇报；
- 人瑞证明复杂业务规则如何被翻译成稳定执行链路；
- Agent 项目提供直接的 Problem Definition、Solution Boundary、Workflow、Demo / POC、Eval / Acceptance 证据；
- “Delivery”不再完全依赖传统运营经历做迁移解释。

## 仍可能卡住
- 正式生产 Go-live 尚未完成；
- 真实企业客户、采购流程、客户验收主体尚未确认；
- CRM / ERP / WMS 等客户系统集成仍无直接证据；
- 如果 JD 要求强工程现场集成，仍存在明显差距。

## 高概率追问
- POC 是针对什么真实业务场景；
- Demo 与 POC 的边界分别是什么；
- POC 成功标准是谁定义的；
- 当前为什么被 ICP 手续阻塞；
- 正式上线后如何验收；
- 你负责 Solution / Acceptance，代码实现边界在哪里。

## 招聘官判断
R2 从“业务型 FDE 转型”明显前进到“已有直接 AI Demo / POC Delivery 证据的业务型 FDE”。对于要求 Requirement → Solution → POC → Acceptance 的 JD，竞争力明显提升；对于 Integration-heavy FDE 仍需谨慎。

---

# R3 AI Commerce

## 15 秒首屏识别
招聘官应继续首先看到完整 Commerce 经营链：市场、产品、Search、Content、Ads、BD、平台商务、Supply 与经营结果；Data Agent / Relevance 提供 AI 侧直接背景，Agent Demo / POC 则补充 AI 应用落地能力。

## 为什么会继续看
- 朗臻 / 今宜的业务结果和责任边界清晰；
- Search 排名、单 SKU GMV、新盘 GMV、达人销售都有可追问结果；
- 有消费者需求→产品输入、市场增长→定位调整等判断链；
- 人瑞提供 Query / Relevance / SQL / Agent 场景；
- 当前 Agent 项目已从“项目证明”升级为 Demo / POC 与 pre-launch 证据。

## 仍可能卡住
- 没有生产 Merchant Agent / Commerce Agent 的正式业务结果；
- 没有商家 AI 产品线上规模化使用证据；
- 如果 JD 偏 API / Agent Engineering，证据仍不足。

## 招聘官判断
R3 的主要价值仍来自真实电商深度。新增 Demo / POC 使“AI Commerce”中的 AI 侧更可信，但不能覆盖没有生产 Commerce Agent 经验这一事实。

---

# R4 AI Product Ops / Agent Product / Intelligent Service

## 15 秒首屏识别
招聘官现在应能看到两层直接证据：一层是人瑞的 AI 质量 / 场景运营与反馈闭环；另一层是实际落地 Agent 项目的 Problem Definition、产品 / Agent Boundary、Workflow、Acceptance、Demo / POC 与上线准备。

## 为什么会继续看
- 人瑞有真实“问题发现 → 规则 / Context 调整 → 复测”的质量闭环；
- 有评测类目、Case、FAQ、问题清单等产品质量运营资产；
- 有版本指标观察和基础 SQL；
- 传统业务经历有消费者需求、产品定位、排期和方案汇报；
- Agent 项目不再只是质量方法补充，而是实际落地目标下的产品 / 场景设计与上线前验证。

## 仍可能卡住
- 正式 PRD 尚未作为已完成资产；
- 没有完整 Roadmap Owner / 资源排期 Owner 证据；
- 尚未产生正式上线后的用户反馈、留存、使用率或产品经营指标；
- 还不能把“等待上线”写成“已负责完整产品生命周期”。

## 高概率追问
- 这个 Agent 的目标用户和核心使用场景是什么；
- 你定义了哪些功能边界和验收标准；
- Demo / POC 与正式上线版本差什么；
- 你是否写过 PRD；若没有，现有需求文档是什么形态；
- 上线后的核心产品指标准备看什么；
- 你与研发 / AI Coding Agent 的职责怎么分。

## 招聘官判断
R4 已经不必只守在“AI Product Quality Ops”。当前更合理的岗位区间是：`AI Product Ops / Agent Product / Intelligent Service / AI 产品运营（偏场景与质量）`。如果补出一份真实可追问的 PRD，并完成正式上线与上线后指标闭环，才进一步具备更强的 AI Product Manager 直接证据。

---

# R5 Agent Solution / Prompt Engineering

## 15 秒首屏识别
招聘官应看到：候选人能从业务问题出发处理 Problem Definition、Instruction、Tool / Evidence / Routing Boundary、Eval、Badcase、Regression，并已经将这些能力应用到一个正在 Demo / POC 交付和上线准备的 Agent 项目。

## 为什么会继续看
- Prompt / System / Tool Instruction 迭代是明确事实；
- 40 Frozen Cases 与 negative controls 是结构化硬证据；
- Demo / POC 状态证明这些设计不是纯离线练习；
- 人瑞提供真实 Agent / Data Agent 质量场景；
- 商业经历提供真实业务需求与用户理解背景。

## 仍可能卡住
- 没有生产 RAG / Agent 的线上运维与规模化数据；
- 深工程技术栈仍不足以支撑纯 Agent Engineer 岗；
- 真实企业客户 Prompt 调优、商业 SLA、生产事故治理尚未确认。

## 高概率追问
- Prompt / System / Tool Instruction 分别解决什么问题；
- 如何区分 Prompt、Retrieval、Tool、Routing 问题；
- POC 到上线还差哪些技术 / 产品条件；
- Frozen Case 如何防止为了结果调 Case；
- 实现中哪些代码你能读懂、哪些由 AI Coding Agent 完成。

## 招聘官判断
R5 比 V5 更像真正的 Agent Solution / Prompt+Eval，而不仅是“个人项目里的 Prompt”。但仍不适合包装成深工程 Agent Application Engineer。

---

# R6 AI Solution / Solution Consultant / Agent Delivery

## 15 秒首屏识别
招聘官现在应该直接看到：候选人有长期真实 B2B / Partner 沟通、商业 Trade-off、方案汇报和多方协同，同时已经把一个 Agent Solution 推进到可运行 Demo、POC 交付 / 验证和上线准备阶段。

## 为什么会继续看
- 京东小二合同 / 毛利 / 资源 Trade-off 是直接商业沟通证据；
- 与工厂 / 产品侧有需求落细和项目推进；
- 今宜有合作方方案汇报、商务条件和冷启动策略；
- 人瑞提供复杂规则 / Context 转译；
- Agent 项目提供完整的 Solution Boundary、Demo / POC、Eval / Acceptance 与 pre-launch evidence。

## V5 中已经消失的缺口
- “没有 Demo / POC”不再成立；
- “只有概念型 Agent Solution”也不再成立。

## 仍可能卡住
- 未确认真实企业客户作为 POC 甲方 / 验收主体；
- 没有 AI 商机资格判断、投标、企业采购流程和售前成交结果；
- 正式生产 Go-live 尚未完成；
- 没有复杂企业系统集成交付经验；
- 没有上线后商业结果或客户成功指标。

## 高概率追问
- 这个 Demo / POC 是给谁使用或验证的；
- 为什么它属于 POC，而不是普通 Demo；
- POC 验收标准是什么；
- 当前 ICP 手续与上线的关系是什么；
- 正式上线后谁是用户、怎么衡量成功；
- 你在 Solution、技术实现、交付和商业决策中的边界分别是什么；
- 是否有客户合同、采购或付款。

## 招聘官判断
R6 不再应标记为“Pre-sales Transition + 无 POC”。更准确的定位是：`AI Solution / Solution Consultant / Agent Delivery`。如果目标 JD 要求业务理解、Solution Design、Demo / POC、Acceptance、交付协同，这份证据链已经成立；如果 JD 要求成熟企业售前成交、招投标和大型客户生产落地，则仍属于真实缺口。

---

# 审计后的岗位族边界

| Role | 当前最强直接证据 | 仍需警惕的硬缺口 |
|---|---|---|
| R1 Agent Eval | Data Agent Eval + Agent behavior + Regression + Eval assets | Python / 自动评测工程 / 生产 Eval |
| R2 Business FDE | Requirement + Delivery + Demo/POC + Acceptance | 企业客户集成 / 正式 Go-live / production integration |
| R3 AI Commerce | 全链路电商 + Query/Relevance + AI Demo/POC 补充 | 生产 Commerce Agent |
| R4 AI Product / Ops | 质量闭环 + Agent product boundary + Demo/POC + pre-launch | 正式 PRD / Roadmap Owner / 上线后产品指标 |
| R5 Agent Solution | Prompt/Instruction + Tool/Evidence/Routing + Eval + Demo/POC | 深工程 / 生产 Agent / 企业 SLA |
| R6 AI Solution | 商业沟通 + Solution + Demo/POC + Acceptance + pre-launch | 客户成交 / 投标 / 企业采购 / 复杂集成 / production go-live |

下一步不应该再通过语言把边界往前推。最有价值的新增证据有两个：

1. **真正产出并核验 PRD**：主要增强 R4，也会帮助 R2 / R6；
2. **完成 ICP 后正式上线并记录上线后证据**：包括真实使用场景、用户、验收、线上指标、问题与迭代，这会同时提升 R2 / R4 / R5 / R6。
