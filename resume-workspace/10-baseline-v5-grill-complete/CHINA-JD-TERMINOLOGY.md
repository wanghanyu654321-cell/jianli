# 中国市场简历术语与表达规范

Status: **V5 FINAL POLISH — NON-DESTRUCTIVE LANGUAGE LAYER**

## 目标

本文件只统一中国招聘市场中的表达方式，不改变事实、证据强度、责任边界或 R1–R6 的定位。

执行优先级：

`FACT_MASTER_CURRENT > CLAIM_LEDGER > V5 母版事实 > 本术语规范 > JD 定制表达`

任何术语替换都不得产生以下副作用：
- 删除原有判断、取舍、验证逻辑；
- 把参与 / 协作升级为独立 Owner；
- 把团队结果改写为个人结果；
- 把微信真实部署写成企业微信 / 全渠道部署；
- 把门店 POC / 开始使用写成长期留存、付费、ROI、规模化或 Production SLA；
- 把项目中的设计 / 验证写成已经完成的生产能力。

## 一、默认表达原则

1. **中文招聘语言优先，行业通用缩写保留。**
2. 第一视觉层优先使用国内 JD 常见词：需求分析、方案设计、项目交付、质量评测、问题定位、回归验证、项目推进、跨团队协作。
3. 技术术语用于证明专业度，不作为整段表达的主语法。
4. 不删除 reasoning，只把“解释句”改成“简历动作句”。
5. 优先使用：`业务问题 / 信号 → 判断 → 动作 → 结果 / 验证`。
6. 避免连续使用“不是……而是……”“本质上……”“进一步……”“不将……包装成……”等解释型句式；事实边界应尽量以正向、简历化方式表达。

## 二、保留英文 / 缩写

以下词在中国 AI / 互联网 JD 中足够通用，可直接保留：

- AI
- Agent
- Data Agent
- RAG
- POC
- API
- SQL
- QA
- SOP
- A/B
- GMV
- ROI
- CTR / CVR
- BD
- CRM
- BPO
- PostgreSQL / pgvector
- TypeScript / Node.js / React / Python / FastAPI / Docker Compose

必要时中英并列一次，后文使用缩写。

## 三、默认中文化词典

| 当前表达 | 中国市场默认表达 | 备注 |
|---|---|---|
| Context | 业务上下文 / 背景信息 | 技术讨论中可保留 Context |
| Evidence | 知识依据 / 证据 | RAG 技术段可写“候选证据” |
| Routing | 路由 / 流程分发 | 简历正文优先“路由” |
| Workflow | 业务流程 / 流程 | 标题中优先中文 |
| Handoff | 人工接管 / 转人工 | 国内客服 / 服务 JD 更常见 |
| Tool Calling | 工具调用 | 保留括号英文仅在技术版必要 |
| Authority | 权限控制 / 服务端授权 | 不单独写 Authority |
| Business State | 业务状态 | |
| Candidate Evidence | 候选知识 / 候选证据 | |
| Frozen Cases | 冻结测试集 | |
| Negative Controls | 负向测试用例 | |
| Holdout | 留出测试集 | 技术版可并列 Holdout |
| Regression | 回归测试 / 回归验证 | |
| Acceptance | 验收 / 验收标准 | |
| Acceptance Harness | 验收测试框架 | |
| Harness | 测试框架 / 验收框架 | |
| Root Cause | 根因分析 | |
| Badcase | 问题案例 / Bad Case | 国内 AI JD 常见 Bad Case，可保留 |
| No-answer | 无答案场景 / 拒答场景 | 按语义选择 |
| Ambiguous | 歧义场景 | |
| Fail closed | 条件不满足时拒答 / 转人工 | 不在非技术第一视觉中直接写 |
| scoped read-back | 按权限范围回读验证 | |
| Agent Runtime | Agent 运行时 | |
| Prompt / Instruction | Prompt / 指令 | |
| Solution | 解决方案 | 标题中文优先 |
| Integration | 系统集成 / 接口集成 | |
| Channel / Identity Adapter | 渠道 / 身份适配层 | R2/R6 技术解释中使用 |
| Business Tool / Adapter | 业务系统接口 / 适配层 | |
| Search | 搜索 | 与 Query 组合时可保留 Search |
| Query | 查询 / 用户意图 / Query | AI/搜索岗位可保留 Query |
| Recall | 召回 | |
| Relevance | 相关性 | |
| Production SLA | 生产环境 SLA | |
| production-calibrated retrieval quality | 真实业务场景下的检索质量 | |
| Real Deployment | 真实部署 | |
| Actual Use | 实际使用 | |
| Scope / Non-goals | 范围 / 非目标 | 产品版中优先中文 |
| Must-have | 核心必需项 / 必备项 | 内部 JD 分析可保留 Must-have |

## 四、标题中文化规则

### R1
默认标题：
**Agent 评测 / 大模型质量 / AI 质量评测**

英文关键词 Agent Eval / LLM Quality 可保留在括号或技能区，不抢第一视觉。

### R2
默认标题：
**AI 解决方案交付 / AI 项目交付 / FDE**

避免第一视觉使用 Business FDE / AI Delivery 全英文。

### R3
默认标题：
**智能电商 / AI 电商 / 电商产品与运营**

### R4
默认标题：
**AI 产品运营 / 智能服务产品运营**

### R5
默认标题：
**Agent 应用 / AI 应用工程 / Agent 解决方案**

R5 仍是选择性方向，不把用户包装成纯 SWE。

### R6
默认标题：
**AI 解决方案 / AI 售前 / 解决方案顾问**

## 五、AI 味重句式的简历化转换

### 1. 解释型
原：
“本质上承担的是从抽象业务要求到具体执行方案之间的翻译。”

改：
“将上游业务规则拆解为下游可执行的判断标准、案例和培训内容。”

### 2. 防御型
原：
“不把 POC 完成扩大解释为长期稳定运行、规模化复制、商业成交或上线后业务指标已经成立。”

改：
“已完成微信真实部署和实体门店 POC，进入实际使用阶段；长期稳定性、规模化复制和业务效果仍在持续验证。”

### 3. 哲学型
原：
“Badcase Fixed ≠ Version Improved。”

改：
“问题修复后执行回归测试，同时检查正常回答、无答案、歧义和权限边界是否出现退化。”

### 4. 过度技术抽象
原：
“Retrieval 只返回 Candidate Evidence，再结合 tenant / store、status / version 和 ambiguity 判断回答、fallback 或转人工。”

改：
“检索结果先作为候选知识，再结合门店范围、知识状态、版本和歧义情况决定回答、拒答或转人工。”

### 5. 过度自我解释
原：
“项目不是从‘我要卖一个 AI Agent’出发，而是先判断业务方真正关心的问题。”

改：
“从门店线上第一接待问题出发，先明确咨询承接、预约 / 线索、异常转人工等核心需求，再确定 Agent 方案范围。”

## 六、数字与结果表达

- 已确认精确值：直接写。
- 已确认范围：写真实范围，例如“每周约 5,000–10,000 条”。
- 团队 / 业务结果：必须明确项目、团队或业务口径，不改写为个人单点贡献。
- 无法确认：不自行估算。
- Quantifier 的用途是发现遗漏数字，不是创造数字。
- 任何新恢复数字在进入简历前必须回写事实治理并确认口径。

## 七、母版与投递版关系

- V5 R1–R6：完整母版，保留 reasoning 和角色差异。
- ONLINE-MAIN：公开在线主简历，取最大公约数，不反向覆盖 R1–R6。
- JD 定制版：允许重排、选择、压缩、关键词对齐；不得新增事实。
- 中文化只改变语言，不降低信息完整度。
