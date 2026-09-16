# [姓名]

[LOCAL_ONLY_CONTACT]

## Target Role

**Agent Solution / Prompt Engineering / Agent Application**

## Professional Summary

具备以业务问题为起点设计 Agent 行为边界、Workflow、Eval 与 Acceptance 的项目实践，并有真实 Data Agent 质量治理经验作为业务侧支撑。

在企业客服 Agent 项目中负责 **Problem Definition、架构与方案边界、Acceptance Criteria、Eval Design、Badcase Attribution、测试验收和项目状态判断**，关注的不只是 Agent 能否生成答案，而是其在 Evidence 不足、候选不明确、权限受限及异常场景下能否遵守预期行为边界。通过 Frozen Cases、Holdout 和回归测试持续验证方案稳定性。

在人瑞 Data Agent 工作中进一步积累 Query、Recall、Relevance、规则转译、执行人员 mental model、复杂 Badcase 和边界收敛经验；能够从实际执行错误反推规则 / Context / Workflow 问题。此前电商经历提供 Search、用户需求、商品语义和业务结果背景，使 Agent Solution 不脱离真实业务场景。

## Core Competencies

**Agent Solution**  
Problem Definition｜Agent Workflow｜Solution Boundary｜Tool Use｜Routing

**Prompt / Context / Evidence**  
Context Design｜Evidence Governance｜Authority Boundary｜Instruction / Rule Translation

**Eval / Quality**  
Acceptance Criteria｜Case Design｜Frozen Cases｜Holdout｜Regression｜Badcase Attribution

**Business Context**  
Data Agent｜Query / Relevance｜Search｜电商场景｜业务需求理解

## Selected Project

### 企业客服 Agent｜Agent Builder 项目

- **Problem Definition：** 围绕企业客服场景负责问题定义，明确 Agent 需要解决的问题、行为范围和阶段性目标，避免从技术组件出发反向寻找场景。
- **Agent Workflow / Solution Boundary：** 负责架构与方案边界设计，项目涉及 Tool、检索、Evidence、Routing、Runtime Budget 和权限等关键约束，用于明确 Agent 在不同输入和信息状态下的行为范围。
- **Context / Evidence Governance：** 重点关注哪些信息可以作为回答依据、哪些情况证据不足以及何时需要收敛行为，使 Agent 的输出建立在受控 Evidence 和 Authority 范围内，而非无限自由生成。
- **Eval Design：** 负责 Acceptance Criteria 和测试场景设计，覆盖正常任务、异常输入、候选不足、歧义及安全 / 权限等不同类型，评估 Agent 是否在不同条件下保持预期行为。
- **Badcase Attribution：** 对失败结果区分检索、Evidence、Routing、权限或最终行为等不同问题来源，并据此决定继续调整方案、规则还是测试覆盖。
- **Regression：** 沉淀 **40 个 Frozen Cases**作为固定回归基线，同时结合 Holdout 检查后续变化是否破坏已有行为。
- **测试结果：** 当前测试集记录 Safety **30/30**、Robustness **100/100**、Holdout **60/60**、Governed Knowledge **46/46**、Public Top1 **96%**、Recall@3 **100%**、Routed Outcome **100%**。
- **实现协作：** 通过 AI Coding Agent 协作进行实现和 Review，本人重点负责 Problem Definition、Solution Trade-off、Eval / Acceptance、Badcase 分析和项目状态判断。

## Work Experience

### 杭州人瑞网络科技有限公司｜评测专家｜服务淘天 Data Agent｜2025.09–2026.06

- **Data Agent Quality：** 参与 Query、Data Agent 输出、Recall 和商品相关性评测，长期处理正常 Case、歧义 Case 及复杂 Badcase，对 Agent 输出质量和业务相关性建立实际判断经验。
- **规则 → 可执行 Instruction：** 承接上游业务规则后，结合真实 Case 判断是否存在定义不清、Context 缺失或边界过宽等问题，再将复杂要求转成下游可执行的规则和判断标准。
- **Context Management：** 发现一些质量偏差实际来自行业知识或业务 Context 缺失，因此会针对当前任务补充必要背景，同时控制信息范围，避免执行人员因 Context 过多扩大判断空间。
- **Mental Model / Root Cause：** 对错误 Case 不只看最终结果，也关注执行人员如何理解任务、在哪一步发生偏差，再判断需要调整规则、Context、示例还是执行流程。
- **Boundary Convergence：** 当规则解释空间导致执行偏差时，会推动缩小可自由判断范围、补充必要例外和 Case，并通过后续 QA 持续观察。
- **质量结果：** 团队 **10+ 人、每周约 5,000–10,000 条任务**，个人日处理约 **100–120 条**；累计沉淀 **10+ 份 SOP / 规则 / 执行文档**，部分任务一致性约 **80% → 95%**，复杂任务约 **60% → 85%**。
- **Search / Agent Context：** 接触 Query 理解 / Rewrite、Recall、Filter、排序和 SERP 等链路，并使用 L1/L2/L3 相关性分级进行判断。

### 杭州今宜商贸有限公司｜抖音项目代运营 / 项目运营 / BD｜2024.11–2025.07

- **业务需求与方案验证：** 新盘项目中先从业务目标、产品定位、内容和转化链路判断核心问题，再通过数据和实际执行持续验证不同方案。
- **信息表达设计：** 根据产品定位将抽象卖点转化为更明确的内容和视觉表达，并根据短视频和直播反馈调整信息呈现方式；这一经历提供了真实“用户如何理解信息”的业务背景。
- **数据反馈：** 本人承担投流工作，结合 **CTR、CVR、ROI**判断不同内容、流量和承接方案的效果，并通过对比验证进一步缩小问题。
- **0→1 结果：** 同一新盘账号月 GMV 从早期约 **7 万**提升至后续首月约 **43 万**；协同约 **6 人直播团队**完成策略、内容、投流和复盘。

### 浙江朗臻网络科技有限公司｜京东电商运营 → 宠物项目管理｜2022.03–2024.07

- **Query / Search Context：** 长期基于搜索热词、长尾词和商品属性理解用户需求与商品匹配关系，推动核心商品搜索排名由百名外提升至 **类目前 10**。
- **业务需求理解：** 结合市场、搜索和消费者反馈判断产品机会，并将真实用户需求反馈到产品开发，为 Agent Solution 提供真实业务需求分析背景。
- **问题定位：** 商品经营中通过实时数据判断流量、点击、转化、商品和链接问题，再选择不同解决方案；形成“先定位问题，再选择工具 / 方案”的工作习惯。
- **项目 Context：** 后续负责约 **5 个跨平台店铺**，对 GMV、利润率、DSR 和渠道结果承担直接责任，并协同内容、客服、供应链、平台和工厂等不同角色推进项目。

## Education

[LOCAL_ONLY_EDUCATION]  
毕业时间：**2022.06**
