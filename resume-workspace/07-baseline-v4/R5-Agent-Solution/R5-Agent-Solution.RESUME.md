# [姓名]

[LOCAL_ONLY_CONTACT]

## Target Role

**Agent Solution / Prompt Engineering / Agent Application**

## Professional Summary

具备从真实 Customer Problem / Scenario 出发设计 Agent Workflow 与工程机制的作品实践，并有真实 Data Agent 质量治理经验作为业务侧支撑。

数字前台 Agent 使用 **Node.js、FastAPI、PostgreSQL / pgvector、React、Docker** 等技术环境，围绕线上接待、私域线索与预约意向承接、RAG / Knowledge、Prompt / Instruction、Tool Calling、Authority、轻 CRM 业务状态、Runtime、Integration 与 Eval 解决具体 Failure Mode。技术组件不是独立展示项，而是服务于“为什么会错、怎么修、怎么验证”的完整工程链。

在人瑞 Data Agent 工作中进一步积累 Query、Recall、Relevance、规则转译、执行人员 mental model、复杂 Badcase 和边界收敛经验；能够从实际执行错误反推规则 / Context / Workflow 问题。此前电商经历提供 Search、用户需求、商品语义和业务结果背景，使 Agent Solution 不脱离真实业务场景。

## Core Competencies

**Agent / RAG**  
RAG｜Retrieval｜Knowledge｜Evidence Governance｜pgvector

**Prompt / Workflow**  
Prompt｜System Instruction｜Tool Instruction｜Workflow｜Tuning

**Tool / Integration**  
Tool Calling｜Authority｜API｜Node.js｜FastAPI｜PostgreSQL｜Docker

**Eval / Quality Gate**  
Badcase｜Eval｜Regression｜Acceptance Harness｜Integration Gate

## Selected Project

### 数字前台 Agent｜场景驱动的 Agent Application Engineering

**项目背景：** 面向小型门店 / 服务型商家的线上第一接待与私域承接场景，产品被收敛为一条明确业务链：**在线接待 → Knowledge / FAQ 回复 → 私域线索与预约意向承接 → 轻 CRM Booking / 状态留痕 → Ticket / Handoff → 人工跟进**。项目目标不是实现一个通用对话 Demo，更不是扩展为全能数字员工，而是让 Agent 真正进入受控数字前台 Workflow；因此工程设计围绕几个真实问题展开：**检索到的信息能不能用、模型有没有权执行、预约 / Ticket 等业务状态有没有真实发生、Instruction 应该改哪一层、候选方案是否满足 Runtime 与稳定性约束。**

**技术环境：** Node.js｜FastAPI｜PostgreSQL 16｜pgvector｜React｜Docker Compose

- **RAG / Evidence：** “检索得到”不等于“当前业务可以回答”。Retrieval 只产生 Candidate Evidence，再结合 tenant / store、Status / Version 及 ambiguity 完成 Answer Authorization；无可靠 Evidence 或无法唯一判断时 fallback。
- **Tool Calling / Authority：** 模型负责理解和提出动作，但 Tool Calling 与服务端 Identity、Scope、Capability 分离，防止 Prompt / LLM 输出直接获得业务授权。
- **Durable Business State：** Booking、Ticket / Handoff 等操作只有真实持久化并完成 scoped read-back 后才确认成功，解决模型文本中的“已完成”与真实系统状态不一致的问题。
- **Prompt / Instruction Tuning：** 实际迭代 Prompt、System Instruction 与 Tool Instruction，但先根据 Badcase 区分失败来自 Instruction、Knowledge / RAG、Tool、Routing 还是 Workflow，再修改对应层。
- **Runtime Trade-off：** 候选 Semantic Selector 经真实调用发现延迟无法满足既定 Runtime Budget，因此未强行进入主链；Database 权限、Provider Timeout 等问题同样区分实现缺陷、架构约束和环境阻塞后再处理。
- **API / Integration：** 通过 HTTP、Node ↔ FastAPI、PostgreSQL / pgvector、权限隔离、业务持久化和 Docker 验证跨服务 Workflow，而不只证明局部代码或 UI 可运行。
- **Eval / Quality Gate：** Frozen Cases、Regression 与 Acceptance Harness 用于验证 Prompt / RAG / Tool / Workflow 修改是否破坏已有 Agent 行为，使工程迭代具备固定质量门槛。

**场景价值：** 将数字前台业务中的具体 Failure Mode 转成对应工程机制，并用 Integration 与 Eval 判断方案是否真正成立；当前已形成可运行 Demo，处于 Demo / POC 与上线前验证阶段。

## Work Experience

### 杭州人瑞网络科技有限公司｜评测专家｜服务淘天 Data Agent｜2025.09–2026.06

- **Data Agent Quality：** 参与 Query、Data Agent 输出、Recall 和商品相关性评测，长期处理正常 Case、歧义 Case 及复杂 Badcase，对 Agent 输出质量和业务相关性建立实际判断经验。
- **规则 → 可执行 Instruction：** 承接上游业务规则后，结合真实 Case 判断是否存在定义不清、Context 缺失或边界过宽等问题，再将复杂要求转成下游可执行的规则和判断标准。
- **Context Management：** 发现一些质量偏差实际来自行业知识或业务 Context 缺失，因此会针对当前任务补充必要背景，同时控制信息范围，避免执行人员因 Context 过多扩大判断空间。
- **Mental Model / Root Cause：** 对错误 Case 不只看最终结果，也关注执行人员如何理解任务、在哪一步发生偏差，再判断需要调整规则、Context、示例还是执行流程。
- **Boundary Convergence：** 当规则解释空间导致执行偏差时，会推动缩小可自由判断范围、补充必要例外和 Case，并通过后续 QA 持续观察。
- **质量结果：** 单项任务下游 BPO 执行人数 **10+ 人**，每周处理约 **5,000–10,000 条任务**；累计沉淀 **10+ 份 SOP / 规则 / 执行文档**，部分任务一致性约 **80% → 95%**，复杂任务约 **60% → 85%**。
- **Search / Agent Context：** 接触 Query 理解 / Rewrite、Recall、Filter、排序和 SERP 等链路，并使用 L1/L2/L3 相关性分级进行判断。

### 杭州今宜商贸有限公司｜抖音项目代运营 / 项目运营 / BD｜2024.11–2025.07

- **业务需求与方案验证：** 新盘项目中先从业务目标、产品定位、内容和转化链路判断核心问题，再通过数据和实际执行持续验证不同方案。
- **信息表达设计：** 根据产品定位将抽象卖点转化为更明确的内容和视觉表达，并根据短视频和直播反馈调整信息呈现方式；这一经历提供了真实“用户如何理解信息”的业务背景。
- **数据反馈：** 本人承担投流工作，结合 **CTR、CVR、ROI**判断不同内容、流量和承接方案的效果，并通过对比验证进一步缩小问题。
- **0→1 结果：** 同一新盘账号月 GMV 从早期约 **7 万**提升至后续首月约 **43 万**；协同约 **6 人直播团队**完成策略、内容、投流和复盘。

### 浙江朗臻网络科技有限公司｜京东电商运营 → 宠物项目管理｜2022.03–2024.07

- **Query / Search Context：** 长期基于搜索热词、长尾词和商品属性理解用户需求与商品匹配关系，推动核心商品搜索排名由百名外提升至 **细分类目前 10**。
- **业务需求理解：** 结合市场、搜索和消费者反馈判断产品机会，并将真实用户需求反馈到产品开发，为 Agent Solution 提供真实业务需求分析背景。
- **问题定位：** 商品经营中通过实时数据判断流量、点击、转化、商品和链接问题，再选择不同解决方案；形成“先定位问题，再选择工具 / 方案”的工作习惯。
- **项目 Context：** 后续负责约 **5 个跨平台店铺**，对 GMV、利润率、DSR 和渠道结果承担直接责任，并协同内容、客服、供应链、平台和工厂等不同角色推进项目。

## Education

[LOCAL_ONLY_EDUCATION]  
毕业时间：**2022.06**