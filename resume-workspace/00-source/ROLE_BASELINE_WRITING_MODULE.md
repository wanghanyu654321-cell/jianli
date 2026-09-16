# Role Baseline Writing Module

状态：ACTIVE。适用于 R1–R6 岗位族基线简历。

## 1. Core invariants

`ROLE FOCUS ≠ EXPERIENCE DELETION`

`FULL CAREER HISTORY = HARD INVARIANT`

`PROJECT_SELECTION = ROLE_DEPENDENT`

`ROLE MAY REINTERPRET CAPABILITY. ROLE MAY NOT REWRITE HISTORY.`

岗位方向可以改变 Summary、Bullet 强调、证据排序、每段经历的展开深度、项目选择与顺序、Skills / Keyword 强调；岗位方向不得改变公司名称、岗位路径、起止月份、事实边界、数字口径或项目状态。

所有正式 Role Baseline 必须保留三段正式工作经历：人瑞 → 今宜 → 朗臻。Project 不属于职业时间轴不变量，不得用 Project 替代 Work Experience。

## 2. Career History Gate

必须同时满足：
- 三家公司全部存在；
- 公司名称、岗位路径和日期与 `CANONICAL_TIMELINE.md` 一致；
- 标准倒序为人瑞 → 今宜 → 朗臻；
- 时间空档不被填补、隐藏或重新解释；
- 工作早于毕业的事实关系原样保留，不推断工作性质。

任何违反均使 `CAREER_HISTORY_GATE = FAIL`，涉及时间字段时同时触发 `TIMELINE_GATE = FAIL`。

## 3. Career Substance Gate

完整职业史不等于完整职业内容。

每段正式 Work Experience 必须：
- `ROLE_SCOPE_VISIBLE = YES`：招聘方能看懂这一阶段实际负责什么；
- 至少有一个 `SCALE / RESULT / OWNERSHIP / DECISION` 强证据，而不是只剩背景职责；
- `TITLE_SUBSTANCE_CONSISTENCY = PASS`：正文能解释岗位路径；
- 保留真实的判断与责任边界，不把复杂经历压成关键词清单。

整份 Resume 还必须满足：
- `CAREER_PROGRESSION_VISIBLE = YES`：责任范围、问题复杂度、业务/质量/方案能力的演进可以被理解。

不设置固定 Bullet 配额。条数是编辑结果，不能反向驱动内容凑数。

## 4. Fact Pool vs Role Selection

R1–R6 共享一个事实池：`FCT-001 / FACT_MASTER_CURRENT.md`。

岗位族之间允许改变的是：
- 事实优先级；
- 排序；
- 展开深度；
- 岗位术语；
- 项目前后位置；
- Core / Supporting / Background 层级。

不允许改变的是：
- 历史事实；
- 责任边界；
- 数字；
- 团队结果和个人结果归属；
- 项目生产/客户状态；
- 未确认技术和指标。

## 5. Three evidence layers

每个岗位族使用三层证据：

1. `CORE_PROOF`：直接证明目标岗位核心能力，进入 Summary / 前部 Bullet / 高展开区域。
2. `SUPPORTING_EVIDENCE`：与核心能力连接较弱，但能补足方法、场景复杂度、协作、商业判断或可迁移能力。
3. `BACKGROUND_BREADTH`：不是首屏重点，但能保持职业完整性和面试深度。

弱相关 ≠ 删除。只有既不增加岗位判断、也不提供上下文或面试价值时才压缩/删除。

## 6. Proof Unit writing

推荐信息链：
`业务/质量问题 → 个人动作 → 判断/取舍 → 交付/协作动作 → 结果性质 → 个人边界`

但不强迫每条都机械同构。

核心原则：
`CONSISTENCY BELONGS TO REASONING LOGIC, NOT TO BULLET SHAPE.`

产品问题、内容问题、商业谈判、规则治理、Agent Eval 可以使用不同 Proof Shape。

`SOP` 是某些反复问题解决后的沉淀，不是每个 Proof Unit 的必选终点。

强动词必须有相应的决策、交付或结果证据。团队结果不得自动升级为个人结果。

## 7. Career Story Map Boundary

Career Story Map 用于解释不同经历之间可验证的能力连续性，不创造职业选择因果。

允许：
- 朗臻 / 今宜的 0→1 场景体现市场、用户、内容、商业与交付约束下的问题解决；
- 人瑞体现规则理解、Context 转译、QA、Root Cause 和执行链路收敛；
- Agent Builder 体现 Problem Definition、Boundary、Workflow、Eval、Acceptance。

允许归纳稳定逻辑：
`理解目标/上下文 → 获取信号 → 定位问题 → 优先可控因素 → 设计方案 → 验证 → 收敛`

禁止无事实支持的动机因果：
- “因为做过搜索所以决定转型 AI”；
- “为了进入 Agent 行业主动转岗”等。

## 8. R1 Agent Eval / LLM Quality

优先级：
1. 人瑞：Eval、Query/Recall/Relevance、QA、Badcase、Root Cause、规则治理、BPO Context、抽检闭环、一致性与版本指标观察；
2. Agent Builder：Eval Design、Frozen Cases、Acceptance、Evidence/Authority、Regression / Badcase；
3. 朗臻：Search / Query Intent、复杂业务 Context 和数据判断作为补充；
4. 今宜：控制变量、CTR/CVR 诊断、流程复盘作为 Supporting Evidence。

避免：把商业经营结果抢占 Eval 主线；把 Agent 项目写成生产系统。

## 9. R2 Business FDE / AI Delivery

优先级：
1. 朗臻：市场发现、消费者需求、产品需求落细、工厂/平台/供应链协同、商业 Trade-off；
2. 今宜：0→1 目标对齐、定位、内容/投流诊断、跨角色推进、冷启动商业策略；
3. Agent Builder：Problem Definition、Solution Boundary、Workflow、Eval、Acceptance；
4. 人瑞：上游文档→自己跑 Case→对齐→下发→QA 的 Delivery 链路。

招聘方应看到：
`Ambiguous Business Problem → Requirement / Context → Solution → Coordination → Validation / Acceptance`

禁止：无事实支持的真实客户 AI 交付、CRM/ERP/WMS Integration、正式 POC / Go-live。

## 10. R3 AI Commerce

优先级：
1. 朗臻：Market Discovery、Search、产品开发、GMV/利润率/DSR、多店经营、平台商务、供应链；
2. 今宜：新盘 0→1、产品定位、内容实验、双机位、投流、达人冷启动、GMV；
3. 人瑞：电商 Query / 商品相关性 / Data Agent 场景；
4. Agent Project：低到中等 Supporting，按真实 JD 决定。

主线应能覆盖：
`市场/需求 → 产品 → Search/Content → Ads → Store/Live → BD → Supply → Data/Review`

禁止为“AI Commerce”强行给传统经营动作添加 AI 因果。

## 11. R4 AI Product Ops / Intelligent Service

优先级：
1. 人瑞：用户/执行者 Context、规则边界、QA、Root Cause、版本效果、反馈闭环；
2. 今宜：产品定位、用户注意力/内容实验、指标诊断、直播承接；
3. 朗臻：直接消费者沟通、需求验证、产品开发输入、多方协作；
4. Agent Builder：Acceptance / Eval / Workflow 作为产品质量方法补充。

强调：场景、用户/执行者理解、产品反馈、流程优化和指标观察。

## 12. R5 Prompt / Agent Solution

项目可前置，但仍需保留完整正式工作史。

优先级：
1. Agent Builder：Problem Definition、Workflow、Tool/Runtime Boundary、Evidence Governance、Routing、Eval、Acceptance；
2. 人瑞：规则转译、Context、执行 mental model、Badcase、边界收敛；
3. 朗臻/今宜：真实业务需求分析和方案验证，证明 Solution 能落到业务场景。

禁止：把未完成 Hybrid/RRF/Reranker/Formal Query Rewrite/Model Routing 写成完成；不写独立全栈工程实现。

## 13. R6 MaaS / AI Solution / Pre-sales

优先级：
1. 朗臻：京东小二合同/毛利/合作方式、推广费与扣点 Trade-off、工厂需求落细、供应/平台多方约束；
2. 今宜：项目目标对齐、直接 BD、达人合作条件、阶段性利润让渡和冷启动；
3. Agent Builder：Solution Boundary、技术栈理解、Acceptance / Eval、权限和 Evidence；
4. 人瑞：复杂规则解释、进度/风险同步和上下游转译。

可证明真实的 B2B / 商业方案沟通与约束权衡，但不得升级成已有 AI 售前成交、Demo/POC、客户 Go-live 或企业系统集成经验。

## 14. Role-family emphasis guidance

以下只表示方向，不是机械篇幅配额：

| role | Renrui | Jinyi | Langzhen | Agent Project |
|---|---|---|---|---|
| R1 Agent Eval | core | supporting | supporting | core |
| R2 Business FDE | core/supporting | core | core | core |
| R3 AI Commerce | supporting | core | core | background/supporting |
| R4 AI Product Ops | core | core/supporting | supporting | supporting |
| R5 Agent Solution | core | supporting | supporting | core-first |
| R6 MaaS / AI Solution | supporting | core | core | core/supporting |

不得据此推导固定 Bullet 条数。

## 15. Editorial rewrite order

固定顺序：
`Select → Rank → Group → Rewrite → Semantic Claim Check → Compress`

先让证据链成立，再做篇幅压缩。信息密度不等于字数越少越好。

任何语义修改后，之前针对该文本的 Semantic Claim Check 自动失效。

## 16. Recruiter-facing vs Audit language

招聘方正文不放内部审计标签和解释性免责，例如：
- `DOCUMENTED_ONLY / REPO_NOT_VERIFIED`；
- “不表述为……”；
- Claim ID / Gate 状态。

这些留在事实母版、Ledger、Audit 和 Review 文档中。Recruiter-facing Resume 通过措辞自然体现边界。

## 17. Prohibited changes

禁止：
- 删除任意一段正式工作经历；
- 把旧经历压成“其他经历”以隐藏职业史；
- 用项目替代正式工作经历；
- 为匹配岗位修改公司、岗位路径、日期、责任边界或数字口径；
- 把 JD 关键词、Skill 模板或 Career Story 推断写成候选人事实；
- 为满足篇幅规则机械补/删 Bullet；
- 为显得专业而堆叠 taxonomy、AI 术语或未确认技术；
- 把弱相关经历等同于无价值经历；
- 把 0→1 写成空洞人格评价而没有具体起点、判断和建立内容。

## 18. Acceptance criteria

岗位族简历必须同时满足：
- 目标岗位在 15–20 秒内可识别；
- `CAREER_HISTORY_GATE = PASS`；
- `CAREER_SUBSTANCE_GATE = PASS`；
- Core Proof 明显优先，Supporting / Background 不抢主线；
- 同一事实池产生清晰岗位区分度；
- 职业连续性可理解但不制造因果；
- Project 选择服务岗位价值；
- 候选人实际做过的事情不被压扁或改写。

最终原则：
`DIFFERENT EMPHASIS · SAME FACTS · SAME TIMELINE · FULL CAREER HISTORY`
