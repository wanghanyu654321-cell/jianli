# R5｜Agent 应用 / AI 应用工程 / Agent 解决方案

## 求职方向

**Agent 应用 / AI 应用工程 / Agent 解决方案 / Applied AI**

## 个人总结

具备从真实业务问题出发设计 Agent 业务流程和工程机制的项目实践，并有 Data Agent 质量治理经历作为业务侧支撑。数字前台 Agent 已形成 **Node.js、FastAPI、PostgreSQL / pgvector、React、Docker、Eval / Harness** 的完整应用链路，并已完成微信真实部署与实体本地生活门店 POC，门店开始在真实接待场景中实际使用。项目围绕进入真实业务流程后的几类核心问题展开：

**检索到的信息能不能用、模型有没有权执行、业务动作有没有真的发生、Agent 出错应该修改哪一层、复杂技术方案是否真的满足质量和 Runtime 约束。**

在人瑞工作中积累 Query、召回、相关性、复杂 Badcase、规则转译和边界收敛经验；此前电商经历进一步提供真实用户需求、搜索、商品语义和经营背景，使工程判断优先从业务风险场景和失败原因出发，再选择对应技术方案。

## 核心能力

**Agent 应用与 RAG**  
Agent 运行时｜RAG / 检索｜知识库｜证据治理｜pgvector

**工具调用与业务流程**  
Prompt / 指令｜工具调用｜权限控制｜业务状态｜人工接管

**系统集成与可靠性**  
Node.js｜FastAPI｜PostgreSQL｜Docker｜幂等控制｜超时 / 取消

**评测与工程决策**  
Bad Case 归因｜回归测试｜验收测试框架｜性能与架构取舍

## 项目经历

### 数字前台 Agent｜业务风险场景 → 工程机制 → 微信部署 / POC → 验证

**业务背景：** 面向微信等私域入口的线上第一接待，核心业务链为：

**Knowledge / FAQ → Booking / Service Intent → Durable State → Ticket / 人工接管 → Human**

项目将真实业务风险和失败场景转化为可测试、可部署、可进入真实门店业务流程的工程机制。

**技术栈：** TypeScript / Node.js｜React｜Python / FastAPI｜PostgreSQL 16 / pgvector｜Docker Compose｜RAG / Knowledge｜Prompt / 指令｜工具调用｜Agent 运行时｜Eval / 回归测试 / Harness

- **RAG / 知识边界：** 实现过程中首先遇到的问题是“检索成功并不代表业务上可以回答”。因此 Retrieval 只产生 候选证据，再由 Node 结合 approval、version、tenant / store、source reference 和 ambiguity 决定最终 Answer Authorization；证据 不足或无法唯一判断时 fallback。
- **工具调用 / 权限控制：** 模型负责理解用户意图并提出动作，但 Identity、Membership、Capability、Scope 与最终写权限由服务端决定，避免 Prompt 或模型输出直接获得业务授权。
- **服务边界设计：** Python / FastAPI 被限制为 private 候选证据 service，只负责返回候选 证据，不负责批准 Knowledge、扩大 Scope 或改变业务状态；最终 Authority 保留在拥有 identity、business context 和 persistence 的 Node 主应用侧，避免形成多个权威中心。
- **业务状态与持久化：** Ticket / 人工接管 等业务动作只有完成 **权限检查 → 写入 → 持久化 → scoped read-back** 后才确认成功，解决模型文本中的“已完成”与真实系统状态不一致的问题。
- **幂等与并发控制：** 单纯检查 idempotency key 是否存在无法覆盖并发 race，因此进一步通过 scoped idempotency 和 reservation / transaction 思路处理两个并发请求同时越过检查点的问题，降低重复业务副作用。
- **Timeout 与异常收口：** Runtime 设置 bounded turns / Tool calls 和 timeout；超时不仅意味着 UI 返回失败，还需要通过 cancellation / late-event isolation 防止请求结束后后台继续产生业务动作。
- **RAG 集成与质量边界：** pgvector / FastAPI / Node cross-language integration PASS 只能证明数据和 contract 链路成立，不能证明真实 Query 的 semantic retrieval quality 已通过；Hosted Embedding 和 production-calibrated retrieval acceptance 因此保持独立状态，不用“系统打通”替代“效果已经好”。
- **Badcase 根因分析：** Agent 出错后先判断 Knowledge / 证据、Prompt、路由、Tool、Authority 还是 业务流程，再修改对应层，避免长期使用 Prompt 覆盖底层问题。
- **回归验证与质量门槛：** 冻结测试集、负向测试用例、Holdout、回归测试 和业务结果验收共同用于判断 Prompt / RAG / Tool / 业务流程 修改是否破坏已有行为。
- **性能与架构取舍：** Semantic Selector 做过真实模型、unseen holdout、order robustness 和 latency characterization；历史 30 次调用约 **P50 7.35s、P95 16.67s**，与当前 10s overall / 2s per-tool 同步预算不匹配，因此不进入主路径。结论不是“技术没用”，而是当前使用位置不成立。
- **真实微信部署与门店 POC：** 已完成微信真实部署与实体本地生活门店 POC，门店开始在真实接待场景中实际使用；这证明系统已经从本地 Demo / 集成测试进入真实渠道、真实身份与真实门店 业务流程，但不把“已经真实使用”扩大解释为高并发、长期稳定运行或 生产环境 SLA 已经成立。
- **系统集成与交付验证：** 主干已集成 PostgreSQL、React、Docker、FastAPI / pgvector，并完成微信真实渠道接入与门店 POC；工程验证继续覆盖 clean-runner、migration、restart persistence、权限隔离和核心 业务流程，用来区分“系统能启动”“真实渠道能接入”和“业务动作能被正确验收”三个不同层级。
- **真实使用后的工程验证：** 门店进入实际使用后，后续验证重点转向真实 Query、真实异常、人工接管、状态一致性、超时和依赖失败等现场问题，再将这些问题回收到 Badcase → 根因分析 → 修改层 → 回归测试。当前真实使用时间与样本仍有限，因此不声称已经完成 production-calibrated retrieval、长期可用性或大流量容量验证。

## 工作经历

### 杭州人瑞网络科技有限公司｜Data Agent 评测｜2025.09–2026.06

- **Agent / Data Quality：** 参与 Query、Data Agent Output、召回 和商品 相关性 评测，长期处理正常 Case、歧义 Case 和复杂 Badcase。
- **规则转译与 指令：** 承接复杂规则后，先通过 Case 判断 Context、定义和边界问题，再转化为执行层可理解的标准和判断要求。
- **根因分析与理解路径：** 对错误不仅看结果，也关注执行人员如何理解任务、在哪一步发生偏差，再决定调整规则、Context、示例还是流程。
- **边界收敛：** 对解释空间过大的规则推动收窄判断边界、补充必要例外和 Case，并通过后续 QA 检查稳定性。
- **质量结果：** 单项任务下游 **10+ 人、每周约 5,000–10,000 条**；累计参与沉淀 **10+ 份 SOP / 规则 / 执行文档**，部分任务一致性约 **80%→95%**、复杂任务约 **60%→85%**。
- **Search Context：** 接触 Query Understanding / Rewrite、召回、Filter、Ranking、SERP 等 Search 链路。

### 杭州今宜商贸有限公司｜抖音代运营兼职｜2024.11–2025.07

- **业务问题与方案验证：** 新盘中先从业务目标、产品定位、内容和转化链路判断主要问题，再通过投流数据和真实执行验证不同方案。
- **数据反馈：** 本人承担投流，结合 CTR、CVR、ROI、素材和直播承接缩小问题范围。
- **0→1 与协作：** 同一新盘账号月 GMV 约 **7 万→接手首月约 43 万**，协同约 6 人团队推进策略、内容、主播和投流。

### 浙江朗臻网络科技有限公司｜电商运营 → 宠物项目运营管理｜2022.03–2024.07

- **业务需求与 Search Context：** 长期通过 Search Query、商品属性和用户需求理解商品匹配关系，推动核心商品搜索排名由百名外进入 **细分类目前 10**。
- **问题定位：** 根据经营数据区分流量、点击、转化、商品和链接问题，再选择不同解决方案，形成“先定位问题，再选工具”的工作习惯。
- **复杂业务环境：** 后续负责约 5 个跨平台店铺经营结果，并协同内容、客服、供应链、平台和工厂等多角色推进问题解决。

**当前状态：** 已完成微信真实部署与实体本地生活门店 POC，门店开始实际使用；尚不声称高并发生产验证、长期 On-call / SLA、规模化复制或 真实业务场景下的检索质量 已完成。
