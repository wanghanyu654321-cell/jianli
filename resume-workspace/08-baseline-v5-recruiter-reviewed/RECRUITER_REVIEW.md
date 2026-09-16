# R1–R6 V5 Recruiter Review

审查基准：`FCT-EPOCH-20260916-04094915`。本文件站在招聘官 / Hiring Manager 的岗位族初筛视角审查，不替代真实 Single-JD 匹配，也不产生伪精确分数。

## 总体审查原则

招聘官在 15–20 秒内通常需要确认四件事：
1. 这个人是否真的做过与岗位核心问题相近的工作；
2. 是否能看到个人动作、判断和结果，而不是岗位关键词堆砌；
3. 转型部分是否有可迁移证据，而不是靠标题包装；
4. 简历里最强的事实是否与岗位 Must-have 对齐。

V5 已统一采用“中层脱敏”：保留问题、判断、方案类型和结果，不展开内部规则、完整执行 recipe、阈值和可直接复制的流程。

---

# R1 Agent Eval / LLM Quality

## 15 秒首屏识别
招聘官应能快速识别：候选人有真实 Data Agent 评测、Query/Recall/Relevance、Badcase、QA、规则治理、Regression 和 Agent 行为评测经验，同时有结构化 Agent Eval 项目资产。

## 为什么会继续看
- 人瑞属于直接工作证据，不是纯项目；
- 有任务规模、抽检比例、一致性变化等量化信息；
- 新增多轮、Tool、Step、信息完整性和最终回答有效性评测后，更接近当前 Agent Eval JD；
- SQL 已从“无证据”变成基础可用能力；
- Agent 项目的 40 Cases、negative controls 和 deterministic metrics 提供结构化 Eval 证据。

## 可能卡住的点
- Python 实际工作使用仍无直接证据；
- 没有正式自动评测平台 Owner / 自动化评测工程经历；
- Agent 项目仍是 proof application，不是生产系统。

## 高概率面试追问
- 80%→95%、60%→85%具体是什么一致性，如何计算；
- 你本人对提升做了哪些贡献；
- Badcase taxonomy 如何形成；
- 多轮 / Tool 行为评测和普通相关性评测差异是什么；
- SQL 能做到什么程度；
- 40 Frozen Cases 如何设计、为什么是 24/8/8。

## 招聘官结论
R1 的证据结构已经成立，后续 Single-JD 主要需要针对 Python、自动评测、Dataset / Rubric、RAG / Tool / Trajectory 等具体 Must-have 调整排序，不需要再重造主线。

---

# R2 Business FDE / AI Delivery

## 15 秒首屏识别
招聘官应能看到：候选人不是纯运营，而是长期做需求澄清、问题优先级、项目推进、多方协作和结果验证，并有 Agent Solution / Acceptance 项目经验。

## 为什么会继续看
- 朗臻和今宜均有需求清单、优先级、排期、阶段检查；
- 有老板 / 合作方方案汇报，不只是后台执行；
- 人瑞体现复杂规则转译和 Delivery 链路；
- Agent 项目补足 Problem Definition、Solution Boundary、Eval / Acceptance。

## 可能卡住的点
- 没有真实 AI 客户 Go-live；
- 没有企业接口文档、CRM/ERP/WMS 客户集成证据；
- 没有正式 AI POC / 客户验收项目。

## 高概率面试追问
- “需求”是怎么来的，谁最终拍板；
- 你如何判断优先级；
- 方案汇报后发生了什么变化；
- 多方冲突时你如何推进；
- Agent 项目为什么不算真实客户交付；
- 如何从运营项目管理迁移到 AI Delivery。

## 招聘官结论
R2 更适合 Business FDE、AI Delivery Ops、AI Solution Delivery 等偏业务和执行落地的岗位；如果 JD 强调现场集成和工程交付，需要非常谨慎匹配。

---

# R3 AI Commerce

## 15 秒首屏识别
招聘官应能看到：候选人有完整 Commerce 链路经验，并且不是单一渠道运营；Search、商品、内容、投流、达人、平台商务、供应链和多店经营都有直接证据，同时具备 Data Agent / Relevance 背景。

## 为什么会继续看
- 朗臻与今宜的业务结果和责任边界都较清晰；
- Search 排名、单 SKU GMV、新盘 GMV、达人销售等结果证据充足；
- 有消费者反馈→产品输入、市场增长→定位调整等较完整的业务判断链；
- 人瑞补充 Query / Relevance / SQL / Agent 场景，形成 AI Commerce 的迁移基础。

## 可能卡住的点
- 没有生产 Merchant Agent / Commerce Agent 直接经验；
- 没有商家 AI 产品正式上线 Owner 证据；
- 如果 JD 偏工程/API Workflow，当前证据不够。

## 高概率面试追问
- 7 万→43 万哪些是个人动作，哪些是团队结果；
- 搜索排名与 GMV 是否为同一商品；
- 如何判断进入某个市场或调整产品定位；
- 供应链和平台商务中你的决策权限；
- 为什么你的电商经验能迁移到 AI Commerce。

## 招聘官结论
R3 是完整度较高的业务型基线。Single-JD 时关键不是继续加经营细节，而是看目标岗位到底偏 Merchant / Search / Marketing / Seller / Agent 哪一侧，再重排证据。

---

# R4 AI Product Quality Ops / Intelligent Service

## 15 秒首屏识别
招聘官应能看到：候选人的直接优势不是传统 PM Roadmap，而是 AI 质量运营、场景运营、执行者 / 用户 Context、Badcase、版本观察和反馈闭环。

## 为什么会继续看
- 人瑞有真实“问题发现→规则 / Context 调整→复测”的闭环；
- 有评测类目、Case、FAQ、问题清单等产品质量运营型资产；
- 有版本指标观察和基础 SQL；
- 今宜 / 朗臻提供真实用户需求、产品表达和项目推进背景；
- Agent 项目补充 Acceptance / Eval / Prompt / Workflow。

## 可能卡住的点
- 没有正式 PRD / Roadmap Owner；
- 没有客服机器人产品 Go-live Owner；
- 没有完整产品生命周期负责人证据。

## 高概率面试追问
- 你和产品经理 / 正式员工的边界是什么；
- 你定义过什么评测类目；
- 哪些反馈真的推动了修改；
- 修改后如何验证；
- 你是否写过 PRD，是否负责版本排期；
- 如何理解 Product Ops 与 QA 的区别。

## 招聘官结论
R4 的正确定位应继续保持“AI Product Quality Ops / Intelligent Service / 场景运营”，不要为了更像 PM 强行写 Roadmap / PRD Owner。真实 JD 若偏产品运营、智能客服运营、AI 质量运营，匹配会比传统 AI PM 更自然。

---

# R5 Agent Solution / Prompt Engineering

## 15 秒首屏识别
招聘官应能看到：候选人不是只会写 Prompt，而是能围绕 Agent Problem Definition、Instruction、Tool / Evidence / Routing Boundary、Eval、Badcase 和 Regression 做完整方案判断。

## 为什么会继续看
- Prompt / System / Tool Instruction 迭代已经是明确事实；
- 40 Frozen Cases 及其结构、negative controls、deterministic metrics 可作为可追问硬证据；
- 人瑞提供真实 Agent / Data Agent 质量场景，不是纯个人项目；
- 商业经历提供真实用户、Search、商品和业务约束背景。

## 可能卡住的点
- 没有正式客户 Prompt 调优交付；
- 没有生产 RAG / Agent 上线 Owner；
- 不具备深工程岗位要求的完整技术栈证据；
- 项目实现使用 AI Coding Agent 协作，面试中必须清楚说明本人负责的设计 / 验收边界。

## 高概率面试追问
- Prompt / System / Tool Instruction 分别改过什么类型的问题；
- 如何判断是 Prompt 问题还是 Retrieval / Tool / Routing 问题；
- Frozen Case 如何避免为了结果调 Case；
- negative controls 为什么重要；
- 你对代码能读到什么程度、哪些部分不是你亲自实现；
- 如果进入真实生产 Agent，你认为还缺什么。

## 招聘官结论
R5 现在更适合 Agent Solution、Prompt / Instruction + Eval、Agent Quality Solution 等岗位，而不是纯工程型 Agent Application Engineer。

---

# R6 AI Solution / Solution Consultant / Pre-sales Transition

## 15 秒首屏识别
招聘官应能看到：候选人有真实 B2B / Partner 沟通、商业条件谈判、方案汇报、多方约束协调，再叠加 Agent Solution / Acceptance 项目能力；但并未伪装成成熟 AI 售前。

## 为什么会继续看
- 京东小二合同 / 毛利 / 资源 Trade-off 是直接商业方案沟通证据；
- 与工厂 / 产品侧存在需求落细和进度推进；
- 今宜有合作方运营方案汇报、达人商务和冷启动条件设计；
- 人瑞补充复杂规则解释和上下游转译；
- Agent 项目提供技术边界和 Eval / Acceptance 语言。

## 可能卡住的点
- 没有 AI 商机资格判断；
- 没有正式 Demo / POC；
- 没有投标、AI 成交或客户 Go-live；
- 没有企业系统集成交付。

## 高概率面试追问
- 你是否真正面对过客户，客户是谁；
- 汇报内容是运营方案还是 AI 技术方案；
- 你在合同 / 毛利讨论中的权限；
- 如何把商业问题翻译成 Agent Solution；
- 如果要做 POC，你会如何定义成功标准；
- 目前离成熟 AI Solution Consultant 还差什么。

## 招聘官结论
R6 应作为“业务型 AI Solution / Solution Consultant 转型”基线使用。真实 JD 若要求成熟售前成交经历，不应通过措辞强行匹配；若偏业务理解、方案沟通、POC 支持和交付协同，则可以继续深挖。

---

# 下一阶段

V5 已完成岗位族层面的 recruiter-oriented rewrite。下一步针对真实 JD 时执行：

`Must-have 拆解 → 15 秒首屏 → Direct / Transferable / Project / Gap → Recruiter doubts → Single-JD rewrite → Interview probes`

在 Single-JD 前，不再通过继续堆事实来“优化”基线；只根据真实岗位要求做证据选择和重排。
