# 简历项目完整上下文交接文档｜2026-09-20

> 用途：给后续 ChatGPT / Codex / Hermes / 其他 Agent 或新会话做**无损上下文交接**。  
> 本文保留可复用的决策轨迹、理由、被否决方案、事实边界、当前仓库状态与下一步执行逻辑；不依赖模型私有思维链。  
> 核心目标：**不漂移、不丢事实、不因某个新需求破坏原有完整性。**

---

## 0. 接手者先读这段

这个项目已经经历过多轮“写简历 → 发现压缩过度 → 恢复完整事实 → 建事实治理 → 做六个岗位母版 → Grill 审计 → 真实门店 POC → 中国市场语言微调 → 在线主简历”演进。

接手时不要重新设计体系，不要从聊天记忆重写简历。

**必须先读取仓库中的权威文件，再做任何修改。**

读取顺序：

1. `resume-workspace/01-facts/FACT_MASTER_CURRENT.md`
2. `resume-workspace/01-facts/CLAIM_LEDGER.md`
3. `resume-workspace/10-baseline-v5-grill-complete/V5-FINAL-POLISH-MANIFEST.md`
4. `resume-workspace/10-baseline-v5-grill-complete/V5-FINAL-POLISH-AUDIT.md`
5. `resume-workspace/10-baseline-v5-grill-complete/CHINA-JD-TERMINOLOGY.md`
6. `resume-workspace/10-baseline-v5-grill-complete/V5-FINAL-FULLTEXT.md`
7. 如需要修改某个角色，再读取对应 R1–R6 的独立 `.RESUME.md`

任何“我记得之前是这样”都不能覆盖仓库权威文件。

---

# 1. 用户的核心定位

用户自己明确过：

> “我本身就不是一个专业的工程师，我的优势能力强在能力可迁移可适应复杂化环境。0-1都有结果，有一定的管理能力。”

当前长期定位：

**复杂环境适应能力 + 能力迁移 + 0→1 推进并取得结果 + 一定项目 / 团队管理能力 + 能深入理解 AI / Agent 技术边界，但不是纯 SWE。**

这句话是整个简历体系的底层解释。

不要把用户改造成：
- 纯软件工程师；
- 纯产品经理；
- 纯售前；
- 纯电商运营；
- 只有个人 Demo 的 AI 求职者。

真正价值在于：

**真实业务经验 → Data Agent 正式评测经历 → Agent 项目真实部署 / POC → 把业务、质量、交付、产品和工程理解连接起来。**

---

# 2. 当前求职方向优先级

## 第一主线：R1｜AI 评测 / Agent 评测 / 大模型质量

这是最直接的正式 AI 工作证据。

核心证据：
- 淘天 Data Agent 正式评测经历；
- Query / 召回 / 商品相关性；
- Agent 输出、多轮上下文、工具调用结果、步骤完整性；
- QA、争议 Case、Bad Case；
- 规则验证、执行标准转化；
- 10+ BPO；
- 每周约 5,000–10,000 条任务；
- 约 10% 抽检；
- 10+ SOP / 规则 / 执行文档；
- 部分任务一致性约 80%→95%；
- 复杂任务约 60%→85%；
- 开放题高低分答案 / Layer / Path 对比；
- 结构化 Trace / 轨迹评测方法理解；
- Agent 项目中的冻结测试、负向测试、回归、验收。

## 第二主线：R2｜FDE / AI 解决方案交付 / AI 项目交付

真实微信部署 + 实体门店 POC + 实际使用以后，R2 原来最大缺口被明显补上。

当前连续链路：

**需求分析 → 方案设计 → 系统集成 → 微信部署 → 实体门店 POC → 实际使用**

核心价值不是“有一个 AI Demo”，而是：
- 从业务问题出发；
- 定义范围；
- 识别约束；
- 设计方案；
- 做系统集成；
- 做权限 / 业务状态；
- 做验收 / 回归；
- 接真实微信入口；
- 到实体本地生活门店 POC；
- 门店开始实际使用。

## 第三层：R3 / R4

### R3｜智能电商 / AI 电商 / 电商产品与运营
正式 Commerce 证据很强，是稳定可投方向。

### R4｜AI 产品运营 / 智能服务产品运营
依靠用户 / 场景洞察、数据诊断、产品定位、MVP、优先级、真实反馈做迁移，但正式 PM title 仍不是事实。

## 选择性方向：R5 / R6

### R5｜Agent 应用 / AI 应用工程 / Agent 解决方案
工程能力是证明，不是主身份。不能包装成成熟 SWE / 高并发生产工程师。

### R6｜AI 解决方案 / AI 售前 / 解决方案顾问
真实 POC 使方向比早期更强，但还没有企业采购 / 商业成交 / 长期付费闭环。

---

# 3. ONLINE-MAIN 的角色

用户需要一份**长期在线、不能针对每个 JD 随意替换的主简历**。

当前 ONLINE-MAIN 第一视觉已经收敛为：

**AI 评测 / Agent 评测｜FDE / AI 解决方案交付｜AI 应用 / AI 产品运营**

核心原则：

1. 第一主轴是 AI 评测；
2. 第二主轴是 FDE / AI 解决方案交付；
3. AI 应用 / AI 产品运营放第三层；
4. 电商经历不是背景噪声，而是证明 0→1、经营判断、商业理解与复杂项目推进；
5. R5 工程能力只作为“能深入落地”的证明，不抢主身份。

ONLINE-MAIN 是**派生版本**，不能反向替代或压缩 R1–R6 母版。

---

# 4. 当前 GitHub / 版本状态

Repository：

`wanghanyu654321-cell/jianli`

当前工作分支：

`resume/v5-final-polish`

Base：

`resume/v5-grill-complete`

当前 compare 状态：
- status: `ahead`
- ahead_by: `56`
- behind_by: `0`
- merge base: `ab2d58a5a57429ff960285557a433fc6345869e5`

**重要：当前 final-polish 还不是 canonical。**

没有做：
- Canonical promotion；
- CURRENT_VERSION_INDEX 更新；
- 合并回原 branch；
- PR / merge。

冻结 V4 仍不可破坏。

## 当前事实 Epoch

`FCT-EPOCH-20260920-DE68CC7D`

FACT blob：

`de68cc7d3ca981e411864f4968300c5056247f6d`

CLAIM_LEDGER 当前文件 SHA：

`5fe4894786cc622d5d893cd724424befcce44fd9`

## 当前最终审阅文件

- `V5-FINAL-FULLTEXT.md`
  - SHA: `b0a6f20527aa784acc2264f206222b9a65f1bf37`
- `V5-FINAL-POLISH-MANIFEST.md`
  - SHA: `a4adc6294ebe0f44ff86e3ab27758f58c8b93205`
- `V5-FINAL-POLISH-AUDIT.md`
  - SHA: `67a11ea09c1b7c35c315921f127be9693583ae87`
- `CHINA-JD-TERMINOLOGY.md`
  - SHA: `71eb4817b666e27f1cc6c27f5928273620a78987`

当前角色文件 SHA：

- ONLINE-MAIN: `fbb4d988518273e8f68549e68e782dd23853edea`
- R1: `f4dc3ea1864ea60672cd004aecf4caf2fb2da80c`
- R2: `a4674929aeafba9e0e9132178e0a444e1b3f1851`
- R3: `a28256e86dd8e126213439410b69406b5f047c20`
- R4: `233d517a1a787bde15de1991a344c3829785f896`
- R5: `c5185cae8e3751ac6431d152c8299df6e4897bb4`
- R6: `a03cc3d43064ee7be7c18ac9843c5e6ad68990c8`

如果这些 SHA 变化，必须先重新读取再继续，不要沿用本文中的旧快照。

---

# 5. 事实治理体系

执行优先级：

`FACT_MASTER_CURRENT > CLAIM_LEDGER > V5 Role Resume > China JD Terminology > JD Tailoring`

任何 Skill、JD、外部模型、BossHunter、Codex、Hermes 都没有权覆盖事实源。

## 新事实进入简历的唯一流程

**用户确认事实 → FACT_MASTER_CURRENT → CLAIM_LEDGER → R1–R6 / ONLINE → Claim Check → Audit**

绝不能：
- 先改简历；
- 再倒推事实；
- 因为 JD 需要就补能力；
- 因为 ATS 需要就编关键词。

---

# 6. 不可破坏的事实边界

## 微信 / POC

已确认：
- 微信真实部署；
- 实体本地生活门店 POC 已完成；
- 门店开始在接待场景中实际使用。

不能自动推出：
- 已完成企业微信部署；
- 全渠道部署；
- 长期留存；
- 持续付费；
- 商业成交；
- ROI；
- GMV / CVR / 效率提升；
- 多门店规模化复制；
- 高并发；
- Production SLA；
- 长期 On-call；
- production-calibrated retrieval quality；
- Hosted Embedding production PASS；
- 正式签署 POC 验收文件。

## PRD

目前：
- 有实际产品上下文；
- 有 Target User / 用户旅程 / Scope / Non-goals / Workflow / Acceptance 等结构；
- 正式 PRD 尚未确认为已完成并核验资产。

因此不得写：
- “完成正式 PRD”；
- “独立负责 PRD 交付”。

## 团队结果 / 个人结果

必须持续区分：
- 团队 / 项目 GMV；
- 本人负责变量；
- 协同团队规模；
- 最终决策权。

不得把：
- 团队结果写成个人单点造成；
- 协同 6 人写成行政管理 6 人；
- 10+ SOP 写成本人独立写 10+；
- 平台合同最终拍板写成本人决策。

## 禁用数字

历史“约 3% CTR”因分母、周期和业务口径无法恢复，正式简历禁用。

---

# 7. 人瑞｜杭州人瑞网络科技有限公司

时间：

`2025.09–2026.06`

正式方向：

Data Agent 评测。

## 已确认核心事实

- Query；
- Data Agent 输出；
- 召回结果；
- 商品相关性；
- 多轮上下文；
- 工具调用结果；
- 步骤完整性；
- 信息收集完整性；
- 最终回答是否解决 Query；
- Bad Case；
- QA；
- 争议 Case；
- 规则治理；
- 灰度 / A/B；
- DAU、CTR、转化、业务水位；
- Search 链路；
- L1 / L2 / L3 相关性。

规模：
- 下游 BPO 10+ 人；
- 每周约 5,000–10,000 条任务；
- 个人日处理约 100–120 条（Fact 中有，V5 多数版本没有使用）；
- 常规约 10% 抽检；
- 累计参与 10+ SOP / 规则 / 执行文档；
- 部分任务一致性约 80%→95%；
- 复杂任务约 60%→85%。

## 稳定工作机制

新任务：
1. 理解规则 / 数据口径；
2. 本人先跑 Case；
3. 找定义 / 逻辑 / 边界 / Context 缺口；
4. 与正式员工完成必要对齐；
5. 转为下游 BPO 判断标准、案例和培训内容；
6. 放量；
7. QA / 抽检；
8. Bad Case；
9. 还原执行人员理解路径；
10. 区分知识 / 规则 / 边界 / 流程问题；
11. 修改说明 / Context / SOP / 示例；
12. 再复测 / 抽检。

这就是 R1、R2、R4、R6 的核心可迁移能力来源。

---

# 8. 新增的 AI 评测事实｜FCT-61~64

这是 final-polish 阶段新增的重要事实，不能遗漏。

## FCT-61｜开放题评测

开放题往往没有唯一标准答案。

实际方法包括：
- 结合既有指标；
- 选高分 / 低分答案；
- 对比不同 Layer / Path；
- 观察关键节点差异；
- 包括意图、工具选择、工具结果、异常处理；
- 将稳定差异沉淀为后续可执行判断规则。

边界：
- 不写“统一 Gold Path”；
- 不写“本人建立完整自动轨迹裁决系统”。

## FCT-62｜结果指标 vs 轨迹评测

简单结果指标可以来自埋点，例如：
- 首 Token 延迟；
- 工具调用数量；
- KV Cache 等。

轨迹评测需要结构化 Trace 暴露：
- 意图；
- 规划 / 决策节点；
- 工具选择；
- 工具结果；
- 错误处理。

重要边界：
**这里的“规划 / 决策节点”指框架暴露的结构化过程信息，不是模型私有思维链。**

不得写：
- 本人实现了完整 Trace 平台；
- 可读取模型隐式思维链。

## FCT-63｜路径评测

开放题轨迹评测关注：
- 关键节点；
- 路径可比性 / 相似度；
- 细粒度错误。

明显问题：
- 工具执行错误。

更隐性的差异：
- 工具选择。

边界：
- GSB 缩写具体含义仍未确认；
- 不写唯一标准轨迹。

## FCT-64｜Langfuse

已确认：
- 理解 Langfuse 在 Agent 可观测、Trace、埋点和评分反馈中的用途。

未确认：
- 人瑞实际接入；
- 数字前台实际接入；
- 本人搭建 Langfuse 评测平台。

所以正式简历当前**不能写“使用 Langfuse 搭建评测平台”**。

---

# 9. 今宜｜杭州今宜商贸有限公司

时间：

`2024.11–2025.07`

性质：
抖音代运营兼职。

核心事实：
- 新盘 0→1；
- 同一账号早期月 GMV 约 7 万；
- 接手首月约 43 万；
- 本人直接承担巨量千川投流；
- CTR / CVR / ROI；
- 内容 / 直播 / 投流联动；
- 玉米包从常见宝宝辅食表达转向健身轻食 / 营养健康；
- 短视频验证后迁移直播；
- 双机位方案参与设计；
- 达人 / KOC 冷启动；
- 本人直接筛选 / 触达 / BD；
- 达人合作单月销售额合计 10 万+；
- 协同约 6 人直播团队；
- 与老板对齐 GMV / ROI / 利润 / 新盘增长等优先目标。

另有一个独立账号单月 GMV 峰值约 152 万已经进入 Fact / Claim，但当前 V5 有意没有使用。不要未经用户再次决定就突然放回主简历。

---

# 10. 朗臻｜浙江朗臻网络科技有限公司

时间：

`2022.03–2024.07`

岗位：

电商运营 → 宠物项目运营管理。

核心事实：
- 市场优先的 0→1；
- 搜索需求 / 关键词判断市场机会；
- 核心商品搜索排名百名外 → 细分类目前 10；
- 另一核心 SKU 日 GMV 约 1,000+ → 15,000+；
- Fact 中约 15 天，V5 多用“接手首月内”保守表达；
- 约 5 个跨平台店铺；
- 业务年度整体 GMV 约 1,200 万–2,000 万；
- 对 GMV、利润率、DSR、月 / 季目标、渠道结果直接负责；
- 小红书约 5 人协同；
- 客服约 5 人协同；
- 京东平台合同 / 毛利 / 活动资源 / 推广费 / 扣点 Trade-off；
- 供应 / 库存 / 大促 / 跨仓；
- 消费者反馈；
- 工厂 / 产品开发协作。

边界：
- 老板负责产品大方向；
- 重大合同 / 商业条件最终由老板确认；
- 用户负责需求落细、项目推进和反馈；
- 不写独立公司级产品战略 Owner。

---

# 11. 教育与时间轴

- 毕业：2022.06；
- 开始工作：2022.03。

不要擅自把 2022.03–2022.06 写成：
- 实习；
- 兼职；
- 校招；
- 提前转正。

工作时间：
- 朗臻：2022.03–2024.07
- 今宜：2024.11–2025.07
- 人瑞：2025.09–2026.06

空档：
- 2024.08–2024.10
- 2025.08

不要写“5 年工作经验”。

---

# 12. 数字前台 Agent｜产品定位

统一名称：

**数字前台 Agent**

不要改成“数字员工”。

## 原始业务问题

很多实体 / 本地生活 / 服务型商家：
- 线下有人工接待；
- 微信 / 私域有流量；
- 但线上第一接待不稳定。

核心问题不是“CRM 太重”。

真正起点：

**私域流量已经存在，但用户进来以后不一定有人及时接住。**

第一阶段价值：

**先补线上第一接待空白，让用户意识到“有人接得住我”，承接咨询与预约 / 线索意向，再让私域流量继续流转。**

## 主业务链

**微信 / 私域入口 → 第一接待 → 知识库 / FAQ → 预约 / 服务 / 线索意向 → 必要轻量业务状态 → Ticket / 人工接管 → 人工跟进**

## 明确非目标

第一阶段不做：
- 完整 CRM；
- 全能数字员工；
- 全自动客服；
- 深营销自动化；
- 多 Agent 炫技。

以后只有真实门店需求持续出现时，才考虑：
- 服务提醒；
- 定时触达；
- 私域促活。

---

# 13. 数字前台 Agent｜架构与技术原则

高层结构：

**Channel / WeChat Adapter → Identity Mapping → Message In/Out → Core Runtime**

核心逻辑：

**Evidence → Agent Decision → Authority → Business State → Handoff → Eval**

未来：
- 企业微信主要换 Channel / Identity Adapter；
- CRM / 业务系统主要通过 Business Tool / Adapter；
- 核心 Runtime 尽量保持稳定。

## 五条核心原则

1. **Retrieval ≠ Answer Authorization**
2. **LLM Proposal ≠ Server Authorization**
3. **Tool Call ≠ Durable Business Success**
4. **Bad Case Fixed ≠ Version Improved**
5. **More Complex Tech ≠ Better Solution**

中国简历正文中不一定用英文哲学句，但底层 reasoning 必须保留。

## 具体机制

### RAG / Evidence
检索只产生候选知识 / 候选证据。

还要检查：
- tenant；
- store；
- status；
- version；
- ambiguity。

0 个有效：
- 拒答 / 转人工。

唯一有效：
- 可回答。

多个歧义：
- fail closed / 拒答 / 转人工。

### 权限
Agent 可提出动作，服务端负责最终：
- identity；
- membership；
- capability；
- scope；
- permission；
- write authorization。

### 业务动作验收
不能把“模型说成功”或“Tool 被调用”当成成功。

成功链路：

**权限检查 → 写入 → 持久化 → scoped read-back / 按权限回读 → 验收**

### Runtime
历史约束：
- max turns 4；
- tool calls 6；
- overall 10s；
- per-tool 2s。

### Semantic Selector
做过真实模型测试。

历史延迟：
- 30 次调用；
- P50 约 7.35s；
- P95 约 16.67s。

由于不符合当前同步 Runtime 预算，所以没有进入主路径。

核心 reasoning：
**技术更复杂不等于当前产品位置成立。**

---

# 14. Agent Eval / Harness

## 40 Frozen Cases

当前：
- 24 Answerable；
- 8 No-answer；
- 8 Ambiguous。

这只是：
**早期 bounded behavior baseline。**

不是：
- production distribution；
- 真实门店流量比例；
- 稳定线上 benchmark。

## Negative Controls

包括：
- tenant / store isolation；
- 未批准知识；
- 失效 / retired 版本；
- 歧义 / 无唯一合法候选。

## Root Cause

推荐层级：

- 没正确信息 → Retrieval / Knowledge；
- 信息存在但不能用 → Evidence Governance；
- 模型判断对但动作没发生 → Tool / Authority / Persistence；
- 单步正常但流程错 → Routing / Workflow；
- 底层正常、行为仍偏 → Prompt / Instruction。

## Measurement Integrity

必须区分：
- Agent Quality；
- Measurement Integrity。

测试系统本身也可能因为：
- Dataset；
- Config；
- Corpus Drift；
- Completion State；
- Missing / Duplicate；
产生 False-PASS。

---

# 15. R1–R6 的定位规则

## R1
正式 AI 评测主线。
不把项目写成模型训练 / 算法研发。

## R2
FDE / AI Delivery 主线。
重点是业务问题 → 方案 → 集成 → POC → 使用。
不写成熟企业级长期 Delivery / SLA。

## R3
正式 Commerce 主线。
Agent 项目只是 AI Commerce / Merchant Agent 迁移证据。
不能让个人项目盖过正式电商经营。

## R4
AI 产品运营迁移线。
可写产品需求结构、MVP、优先级、迭代、真实反馈。
不写正式 PM title / PRD Owner。

## R5
工程证明线。
重点：Failure Mode → Mechanism → Validation → Trade-off。
不包装成成熟 SWE。

代码层强表述如 reservation / transaction、cancellation / late-event isolation，如以后需要强化，最好先做代码核验。

## R6
解决方案 / 售前迁移线。
重点：客户问题、方案沟通、业务技术翻译、POC。
不写成熟采购成交 / 商务 Close / 长期付费客户。

---

# 16. 中国市场语言规则

本轮 final-polish 的核心不是删内容，而是降低阅读成本。

原则：
- 中文 JD 常用词优先；
- 行业高频英文 / 缩写保留；
- 技术词证明能力，不主导整句语法；
- 不删除 reasoning；
- 把解释句改成动作句。

推荐结构：

**业务问题 / 信号 → 判断 → 动作 → 结果 / 验证**

保留：
- AI
- Agent
- Data Agent
- FDE
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
- TypeScript / Node / React / Python / FastAPI / Docker

默认中文化：
- Context → 业务上下文；
- Evidence → 知识依据 / 证据；
- Workflow → 业务流程；
- Handoff → 人工接管 / 转人工；
- Tool Calling → 工具调用；
- Authority → 权限控制 / 服务端授权；
- Frozen Cases → 冻结测试集；
- Negative Controls → 负向测试；
- Regression → 回归测试；
- Acceptance Harness → 验收测试框架；
- Root Cause → 根因分析。

Bullet 标题：
- 短；
- 负责 10 秒扫描；
- 不重复整句；
- 不堆“真实 + 门店 + POC + 使用 + 验收”等长标题。

---

# 17. “AI 味”处理规则

禁止为了“更像人写”而把 reasoning 删掉。

只改表达。

例：

AI 味：
> Badcase Fixed ≠ Version Improved

简历化：
> 问题修复后执行回归测试，同时检查正常回答、无答案、歧义和权限边界是否出现退化。

AI 味：
> 本质上承担的是从抽象业务要求到执行方案的翻译。

简历化：
> 将上游业务规则拆解为下游可执行的判断标准、案例和培训内容。

AI 味：
> 不把 POC 扩大包装成长期稳定运行。

简历化：
> 已完成微信部署与实体门店 POC，并开始实际使用；长期稳定性、规模化复制和业务效果仍待持续验证。

---

# 18. 母版原则

用户已经明确：

> “V4 是完整母版。压缩发生在具体 JD 投递版，不发生在母版。”

以及：

> “在最少的字数中完成最高的信息密度和完整性。”

以及：

> “脱敏 ≠ 删除 reasoning。脱敏 = 保留 reasoning，隐藏 implementation detail。”

以及：

> “粗体标题负责 10 秒筛选，正文负责证明能力。”

以及：

> **V5 should be “V4 + Grill”, not “V4 → 更短”.**

因此：

**母版完整性优先于简短。**

具体 JD 才压缩。

---

# 19. ResumeSkills 研究结论

研究过：

`https://github.com/Paramchoudhary/ResumeSkills`

README 曾写 20 Skills，但目录当时实际有 22 个。

不是整套照搬。

最终适合我们的求职执行层：

1. JD Analyzer
2. Resume Quantifier
3. Career Changer Translator
4. Resume Tailor
5. Resume Bullet Writer
6. ATS + Formatter
7. Version / Application Manager
8. Interview Prep + Portfolio Case Study

## Quantifier 的最终规则

用户明确认为 Quantifier 在中国市场是必须品，因为人的记忆会遗漏规模信息。

我们接受它，但用途定义为：

**事实恢复工具，不是数字生成工具。**

它应该追问：
- 多少人；
- 多大规模；
- 多久一次；
- 一周 / 月多少；
- Before / After；
- 金额；
- 时间窗口；
- 最小值 / 区间；
- 哪个是团队结果；
- 哪个是个人控制变量。

状态：

### Confirmed
确定值，可写。

### Bounded / Range
能确认范围，可写范围。

### Unknown
无法恢复，不写。

禁止：
- 为了“量化”估一个用户没确认的结果数字。

---

# 20. ResumeSkills 与事实治理的优先级

所有 Resume Skill 只能：

- 发现遗漏；
- 提问；
- 选择；
- 排序；
- 翻译；
- 压缩；
- 排版；
- 面试准备。

不能：

- 新增事实；
- 编数字；
- 改 title；
- 扩 ownership；
- 把 POC 写成 Production；
- 把 transferable capability 写成 direct experience。

统一规则：

**FACT MASTER / CLAIM LEDGER 永远高于任何 Resume Skill。**

---

# 21. 未来 JD 投递流水线

冻结为：

**V5 母版 / ONLINE → 精确 JD → Must-have 拆解 → Hard Blocker → R1–R6 路由 → 证据选择 → Quantifier 检查 → 10 秒 HR → Tailor → ATS → PDF / 在线投递 → Application Tracker → 面试 Drill**

不要从 JD 直接改母版。

---

# 22. BossHunter｜自动投递系统

研究对象：

`https://github.com/shengjidaguai-china/BossHunter`

BossHunter 不是只有 Runtime。

它本身包含：
- Web Dashboard；
- CLI；
- Python 服务 / 状态机；
- 本地数据库；
- Chrome CDP / 浏览器执行；
- 岗位采集；
- AI 评分；
- ready / filtered 等状态；
- 人工确认；
- 低频发送；
- HR 回复监听；
- 定制简历流程。

所以不需要为了“有桌面控制端”再套 Codex。

---

# 23. BossHunter 架构探索轨迹

我们先后考虑过：

## 方案 A｜原版 BossHunter + DeepSeek
优点：
- 快；
- 成本低；
- 几乎零开发。

缺点：
- 不知道我们的 R1–R6；
- 不知道 Fact / Claim；
- 不能完整利用现有简历治理。

## 方案 B｜BossHunter + DeepSeek + 我们的 Policy / Master
当前综合最优。

## 方案 C｜Codex + BossHunter
优点：
- 推理能力强；
- 可读完整 repo；
- 适合边界 JD。

缺点：
- 多一层；
- 依赖订阅 / 会话；
- 高频处理几十个 JD 能力过剩；
- 链路更复杂。

定位：
**高价值 / 边界 JD 复核器，而不是一线批处理。**

## 方案 D｜Hermes + BossHunter
适合未来：
- 长期驻留；
- 定时；
- autonomous workflow。

但现在会引入：
- memory；
- tool binding；
- scheduler；
- recovery；
- runtime；
- 额外维护。

用户目标是尽快投简历，不是再开发一个 Agent。

所以当前不优先。

## 方案 E｜本地 LLM
隐私最高，但可能在跨岗位迁移判断上过严或过松。

用户履历不是“Java→Java”，而是：
- Commerce；
- Data Agent Eval；
- Agent POC；
向 FDE / Product / Solution / AI Commerce 迁移。

弱模型容易：
- 无同 title 就拒绝；
- 做过 Agent 就全都放行。

目前不值得为了省少量 API 费用牺牲匹配质量。

## 方案 F｜自己重写浏览器投递
没有必要。

BossHunter 已经解决最脆弱的：
- 页面变化；
- Chrome；
- 去重；
- 状态；
- 风控；
- 人工确认；
- 发送；
- 回复监听。

---

# 24. 当前 BossHunter 最优架构

当前收敛方案：

**BossHunter = 求职 Runtime + Dashboard + Browser**

**DeepSeek = 高频廉价推理**

**jianli repo = 唯一事实源**

**OUR_POLICY = 总约束**

**BOSSHUNTER_MASTER = 机器读取的去重事实全集**

**ROLE_INDEX = R1–R6 路由规则**

**Human = 最终投递 Authority**

结构：

```
招聘网站
   ↓
BossHunter collect
   ↓
规则硬筛
   ↓
DeepSeek
   ↑
OUR_POLICY
BOSSHUNTER_MASTER
ROLE_INDEX
   ↓
filtered / ready
   ↓
人工确认
   ↓
BossHunter send
   ↓
HR reply
```

---

# 25. 为什么不让 DeepSeek 直接读六份 V5

R1–R6 正式经历高度重复。

六份全文直接拼接会导致：
- Token 重复；
- 身份混乱；
- 路由不稳定；
- 成本增加。

所以未来应派生：

## BOSSHUNTER_MASTER.md

机器事实全集。

只保留一次：
- 人瑞事实；
- 今宜事实；
- 朗臻事实；
- Agent 项目事实；
- 事实边界。

并可加 Role Tag：

`[R1][R2]`
`[R2][R4][R6]`
`[R3]`
等。

这只是**派生缓存**。

不能变成新的事实源。

---

# 26. BossHunter 需要的 OUR_POLICY

应该压缩我们现有所有规则，而不是把 22 个 ResumeSkills 全部塞进去。

核心内容：

- 事实优先级；
- 禁止虚构；
- 团队 / 个人边界；
- POC / Production 边界；
- JD 拆解；
- Hard Blocker；
- Must-have；
- Quantifier；
- Career Translation；
- Tailor；
- Bullet；
- 10 秒 HR；
- R1–R6 路由。

---

# 27. BossHunter 内置 Agent 的关键技术判断

BossHunter 根目录的 `SKILL.md` 并不会自动让内置 DeepSeek 执行我们的 ResumeSkills。

内置 AI 实际主要通过源码中的固定 Prompt 工作，例如：
- scorer；
- greeter；
- resume。

因此如果使用 BossHunter 内置 DeepSeek，真正需要的是：

**极薄 Policy Injection / Policy Loader**

而不是重新造 Agent。

思路：

```
SCORING_PROMPT
GREETING_PROMPT
RESUME_TAILOR_PROMPT
+
OUR_POLICY
+
BOSSHUNTER_MASTER
```

只做小 patch，不深度 fork。

---

# 28. BossHunter 第一阶段不要做什么

不要：
- 每个 JD 都生成完整简历；
- 100% 自动发；
- 一上来接 Hermes；
- 一上来做复杂 scheduler；
- 一上来做本地大模型；
- 改太多 BossHunter 源码。

第一阶段：

100 JD  
→ 硬筛  
→ DeepSeek Match  
→ ready  
→ 人工确认  
→ 发送

只有：
- 高优先 JD；
- HR 回复；
再生成 JD-specific resume。

---

# 29. Job Matching Frozen Set

正式放量前必须做 30–50 个真实 JD 的人工基准集。

每个 JD 标：
- 应投 / 不应投；
- Route：R1–R6；
- Must-have；
- Hard Gap；
- 为什么；
- 是否边界岗位。

评估重点不是“82 分还是 86 分”，而是：

1. False Pass
2. False Reject
3. Route Error
4. Fact Hallucination

如果失败：

**Bad Case → Root Cause → 修改 Policy / Router → Regression**

不要先换模型。

这和数字前台 Agent 自己的 Eval 方法完全一致。

---

# 30. BossHunter 落地顺序

1. 当前 V5 最终微调完成；
2. 用户确认是否升 canonical / freeze；
3. 本机安装 BossHunter 原版；
4. 先验证 Dashboard / Chrome / collect 正常；
5. 接 DeepSeek API；
6. 验证 BossHunter 原始 AI 流程；
7. 生成：
   - BOSSHUNTER_MASTER.md
   - ROLE_INDEX.md
   - OUR_POLICY.md
   - APPLICATION_TRACKER
8. 做极薄 Policy Loader；
9. 建 30–50 JD Frozen Set；
10. 回归；
11. 小规模真实使用；
12. 稳定后再放量。

Codex / Hermes 都不是第一阶段前置条件。

---

# 31. 数据与账号安全

BossHunter 即使有 throttle / risk control，也不能保证平台绝对不封号。

因此：
- 保留人工确认；
- 低频；
- 遵守发送窗口；
- 遇验证码 / 风控停止；
- 不追求无人值守狂投。

DeepSeek API 会让发送给模型的内容离开本机。

因此机器母版不要包含：
- 手机号；
- 身份证；
- 精确住址；
- 无关隐私。

联系方式在最终本地简历模板阶段合并。

---

# 32. Codex / Hermes 最终定位

## Codex
不是必须控制端。

未来适合：
- 高价值 JD；
- 边界岗位；
- 最终简历复核；
- Git diff；
- 复杂事实 / 技术核验。

## Hermes
未来适合：
- 常驻；
- 定时；
- collect；
- 自动 route；
- 自动 ready。

但 Hermes 不应该拥有独立简历记忆。

任何 Agent 都应该：
- 每次读 repo；
- 不依赖长期记忆。

原则：

**State outside the model.**

---

# 33. GitHub 工程证据

公开工程 Repo：

`wanghanyu654321-cell/-agent`

历史证据：
- pre-ICP source commit: `55182eb11e801b49a5c5564d05acc72207b249f1`
- tree: `68499338168aed05353247ce5196503b7118bcf7`
- main convergence PR #15 merge: `adbee3b2813086a3e4d2274d39af6d939fdb2468`

历史 README / evidence 仍可能保留 synthetic / pre-ICP 口径。

但当前用户确认事实已经是：
- 微信部署；
- 门店 POC；
- 开始实际使用。

这两层不能混为一谈。

**待办：在真正投递前，最好更新 recruiter-facing GitHub README，避免招聘方看到“简历说真实 POC、README 还说 synthetic/pre-ICP”的明显冲突。**

修改前仍要先核实 Repo 当前状态，不要凭历史摘要改。

---

# 34. 监控任务状态

用户以前说过“开始监控”。

创建自动监控时因为：
> active task 已达到 5 个限制

所以**没有成功创建新的职位监控 automation**。

后续不能说“已经在监控”。

---

# 35. 历史岗位 / 薪资研究

之前做过杭州岗位研究和薪资估计，但这是强时效信息。

历史大致方向：
- R1：AI Agent 评测 / 大模型评测；
- R2：AI 交付 / FDE / 解决方案交付；
- R3：AI 产品运营 / 智能电商；
- R4：AI 产品经理 / AI 产品运营；
- R5：Agent 应用开发；
- R6：AI 解决方案 / 售前。

历史杭州中小公司估计区间曾大致落在：
- R1 14–20K，强匹配可能更高；
- R2 POC 前约 13–18K，POC 后可能上移；
- R3 15–22K；
- R4 12–18K；
- R5 12–18K；
- R6 POC 前约 12–18K，POC 后可能上移。

这些都不是当前市场事实。

**任何公司、薪资、在招 JD、岗位状态，必须重新联网检索后再使用。**

---

# 36. 当前 final-polish 做了什么

目的：
1. 中国市场中文 JD 通用语；
2. 降低 AI 味；
3. 新建 ONLINE-MAIN；
4. 保留 reasoning；
5. 不破坏原 V5。

已经执行：
- 中文招聘术语统一；
- 过度英文中文化；
- FDE / AI 评测前置；
- 长解释句变成简历动作句；
- Bullet 标题缩短；
- “真实”重复使用减少；
- 新增开放题 / Path / Trace 评测事实；
- Langfuse 严格保持未接入边界。

完整性审计：
- R1 因新事实新增 2 bullets；
- R2–R6 bullet 数不因中文化减少；
- 原有数字 / 日期 Token 没有因微调丢失。

---

# 37. 当前最后停点

简历正文已经进入 final-polish 后期。

下一步不是重新写。

下一步应按顺序：

## A. 10 秒 HR 第一屏审计
检查：
- 3 秒看懂是谁；
- 10 秒看懂为什么匹配；
- AI 评测 / FDE 是否足够前置；
- 核心硬结果是否出现；
- 第一屏是否过长。

## B. 中国招聘平台字段映射
针对 BOSS / 猎聘 / 智联：
- 求职方向；
- 个人优势；
- 工作职责；
- 项目；
- 技能标签；
- 期望职位。

因为在线平台字段往往不能完整呈现 Markdown Resume，所以要做字段级版本。

## C. 用户确认
确认：
- ONLINE-MAIN；
- R1；
- R2；
- 其余版本。

## D. 再决定是否升 canonical / freeze

用户没有明确说“升 current / canonical / freeze”前：
**不要修改 CURRENT_VERSION_INDEX，不要 merge。**

---

# 38. Anti-Drift Protocol｜最高优先级

这是接手者必须严格执行的。

## 规则 1
任何修改前先 fetch 当前文件。

不要根据本文重建正文。

## 规则 2
新需求优先级提高，不等于旧能力删除。

例如：
“现在重视 FDE / AI 评测”
不等于：
删除电商完整经历、产品能力、工程理解。

## 规则 3
母版不压缩。

压缩发生在：
- JD-specific；
- 平台字段；
- 1–2 页投递版。

## 规则 4
每次修改必须检查副作用。

至少检查：
- 原 bullet 是否消失；
- 数字是否丢失；
- ownership 是否变化；
- 团队结果是否变个人；
- POC 是否升级；
- ATS 关键词是否误删；
- R1–R6 差异是否被统一掉。

## 规则 5
新事实必须先进入 Fact / Claim。

## 规则 6
不凭“更好看”擅自改事实口径。

## 规则 7
ONLINE-MAIN 不覆盖角色母版。

## 规则 8
语言中文化 ≠ 技术降级。

## 规则 9
不要无休止重写母版。

用户时间有限，已经多次明确反感漂移和返工。

## 规则 10
如果不确定，先展示 exact diff，再动。

---

# 39. 每条简历证据的完整思维结构

完整母版中的高价值 bullet 尽量能够回答：

1. Problem
2. Signal
3. Judgment
4. Action
5. Trade-off
6. Proof / Verification
7. JD Link

不需要每条显式写七段。

但不能为了简短，只剩：
> “负责 X，提升 Y。”

用户最大的差异化就是：
**为什么这么判断、为什么这么做、怎么证明。**

---

# 40. 决策演进轨迹

## 阶段 1｜先恢复完整母版
早期最大问题：
压缩会让经历只剩结果，丢失判断与方法。

因此确立：
**V4 完整母版。**

## 阶段 2｜V5 = V4 + Grill
做 Grill Me 后发现：
真正有价值的是隐藏在经历背后的：
- 判断；
- 边界；
- Trade-off；
- 验证。

因此 V5 不是更短，而是更完整。

## 阶段 3｜Agent 项目从 Demo 进入真实门店
用户确认：
- 微信部署完成；
- 实体本地生活门店 POC；
- 开始实际使用。

这改变了角色强弱：
- R2 显著变强；
- R4 / R6 也得到真实交付证据；
- R1 得到真实场景 Eval 输入；
- R3 得到 Merchant / Service Agent 场景；
- R5 得到真实渠道与业务流程证据。

但没有因此升级：
- Production；
- SLA；
- ROI；
- 规模化。

## 阶段 4｜研究 ResumeSkills
结论：
不是让第三方 Skill 改造我们的事实体系，而是把它放到投递执行层。

特别保留 Quantifier，但把它定义为：
**事实恢复，不是估数字。**

## 阶段 5｜研究 BossHunter
最初考虑：
- Codex；
- Hermes；
- 外部 Agent；
- 完全无人值守。

后来发现：
BossHunter 自己已经有：
- Dashboard；
- Runtime；
- Browser；
- State；
- AI；
- 人工确认。

因此不需要额外桌面 Agent 才能工作。

## 阶段 6｜收敛自动投递架构
综合成本 / 时间 / 效率 / 安全 / 稳定 / 性能：

当前最均衡方案：
**BossHunter + DeepSeek + 薄 Policy Overlay + Machine Master + Human Authority**

Codex / Hermes 都不是当前前置。

## 阶段 7｜中国市场 final polish
用户指出：
1. 英文不是中国 JD 通用语言；
2. 需要一份不能频繁更换的在线主简历；
3. AI 味偏重。

因此建立：
- CHINA-JD-TERMINOLOGY；
- ONLINE-MAIN；
- final-polish branch。

随后用户再次提醒：
**FDE 和 AI 评测才是大头。**

因此最终 ONLINE 第一视觉重新收敛：
**AI 评测第一、FDE 第二。**

---

# 41. 当前不可做的事情

除非用户明确要求，不要：

- merge branch；
- 创建 PR；
- 更新 canonical index；
- 删除历史版本；
- 合并 R1–R6；
- 压缩母版；
- 用 JD 反写事实；
- 给 R5 加生产级工程头衔；
- 给 R6 加商业成交；
- 给 R4 加正式 PM / PRD Owner；
- 写 Langfuse 已接入；
- 写企业微信已经部署；
- 写 POC 有 ROI；
- 写 3% CTR；
- 写 5 年经验；
- 写自动职位监控已经开启。

---

# 42. 下一位 Agent 的第一句话应该做什么

不要重新问用户“你的目标是什么”。

直接：

1. 读取当前 final-polish 权威文件；
2. 告诉用户当前停点；
3. 继续做 10 秒 HR 第一屏审计 / 中国平台字段映射；
4. 只提出必要修改；
5. 每个修改给出副作用检查；
6. 用户确认以后再写回。

---

# 43. 可直接给新 Agent 的启动指令

> 你现在接手我的简历项目。不要从零设计，也不要根据聊天印象重写。先读取 jianli repo 的 FACT_MASTER_CURRENT、CLAIM_LEDGER、V5-FINAL-POLISH-MANIFEST、V5-FINAL-POLISH-AUDIT、CHINA-JD-TERMINOLOGY 和 V5-FINAL-FULLTEXT。当前工作分支是 resume/v5-final-polish，尚未升 canonical。我的第一主线是 AI 评测 / Agent 评测，第二主线是 FDE / AI 解决方案交付；R3/R4 是重要迁移，R5/R6 选择性使用。所有修改必须保持 Problem→Signal→Judgment→Action→Trade-off→Verification 的完整性，中文招聘语言优先，不得删除原事实、数字、角色差异或扩大 ownership。微信部署、实体门店 POC 和开始实际使用已经确认，但不代表长期留存、付费、ROI、规模化、Production SLA 或企业微信部署。新事实必须先进入 FACT_MASTER 和 CLAIM_LEDGER，再进入 Resume。当前下一步是 10 秒 HR 第一屏审计和 BOSS/猎聘/智联在线字段映射，不要重新压缩母版。

---

# 44. 最后一句总原则

**我们不是在追求一份“看起来很厉害”的简历，而是在构建一套事实可追溯、能力可迁移、不同 JD 可复用、不会因为模型或会话变化而漂移的求职系统。**

真正长期资产是：

**Fact → Claim → Role Baseline → Online Main → JD Tailor → Application → Interview**

而不是某个模型的记忆。


---

# 25. 2026-09-20 当前执行顺序覆盖｜ANTI-DRIFT OVERRIDE

本节是当前执行顺序的最新明确确认；如与本文件前文的历史探索顺序冲突，以本节为准。

当前冻结顺序：

1. **先修文档歧义**
   - 区分 canonical registry 与 working candidate；
   - 清理旧 epoch / 旧 branch / 旧 repo-verification 状态造成的误导；
   - 对齐 `jianli` 与 `-agent` 的工程证据边界；
   - 不修改 Resume 正文，不做 10 秒 HR 审计，不做 BossHunter 优化。
2. **再做 10 秒 HR / 平台首屏审计**
   - 对象优先为 ONLINE-MAIN + R1；
   - 只处理第一视觉、Bullet 标题、阅读成本、AI 总结腔、最新 Eval 证据密度；
   - 不借审计重构 R1–R6，不压缩母版事实。
3. **最后做 BossHunter 优化调用**
   - 先使用 vanilla BossHunter 当前 Local Agent Tool API；
   - 再用真实 JD Frozen Set 评估 False Pass / False Reject / Route Error / Fact Hallucination；
   - 只针对观察到的失败补 OUR_POLICY / Router，不先 fork 或重写内部 Prompt。

当前阶段：**STEP 2 — 10 秒 HR 审计后的用户复核 / 修订**。STEP 1 文档歧义修复已完成；STEP 3 BossHunter 优化尚未开始，必须等待用户确认当前简历版本。

执行顺序保持不变：只有用户明确确认 STEP 2 的简历版本后，才进入 STEP 3。

## 25.1 Canonical 与 Candidate 的唯一解释

- `CURRENT_VERSION_INDEX.md` / `GATE_REGISTRY.json` = **已晋升 canonical registry**。
- `resume/v5-final-polish` = **更新但尚未晋升的 working candidate**。
- working candidate 当前事实 epoch：`FCT-EPOCH-20260920-78D15E87`。
- candidate 的 `FACT_MASTER_CURRENT.md` / `CLAIM_LEDGER.md` / ONLINE-MAIN / R1–R6 可以比 canonical 更新，但 **newer != promoted**。
- 在用户明确要求 canonical promotion 前，不修改 canonical index / registry。
- V5 / V6 只是历史 artifact 命名，不代表时间顺序；以后判断“最新”使用：
  **source_epoch → artifact_status → promotion_state**。

## 25.1A 当前简历编辑规则补充

- 杭州今宜职位统一对外显示：`杭州今宜商贸有限公司｜抖音项目代运营`；BD / 项目推进继续作为职责证据保留，用于 MaaS / AI 交付方向迁移，不并列进职位标题。
- R1 项目标题必须优先描述**实际场景 / 解决的问题**，不改成“评测方法链”式标题。
- Bullet 标题默认只保留一个主概念；第二概念若只是解释关系，放正文。
- 两个词都是独立 JD 高价值关键词时可保留 `/`，例如 `Regression / Holdout`、`Eval Harness / CI`。
- 电商搜索在 ONLINE-MAIN 用 `搜索增长 / SEO`，在 R1 用 `搜索 Query 理解`。
- CI 只写已有证据支持的 `CI / 持续集成`，不擅自扩成 CI/CD。
- 招聘简历正文不主动列“长期付费 / ROI / Production SLA 未验证”式完整负面清单；这些边界继续保留在 FACT / CLAIM / AUDIT 中，Resume 只避免越界主张。
- ONLINE-MAIN 与 R1 的 recruiter-facing 修改必须同步到 `V5-FINAL-FULLTEXT.md`。
- 用户尚未批准当前版本前，不进入 BossHunter。
- R1 五类不可误删核心：**评测、沟通、协调、管理、两段 0→1 结果**。10 秒审计只能压重复和低价值细节，不得压掉这五类证据。
- 朗臻成长路径必须显式保留：**牙膏品类电商运营 → 宠物项目运营管理 → 约 5 个跨平台店铺 / 年度整体 GMV 约 1,200 万–2,000 万**；同时保留优先级、项目排期、阶段检查、跨团队协调、方案 / 进展汇报。
- 用户的“学习 / 适应能力”通过跨品类、跨渠道、跨岗位责任升级和结果体现，不写空泛人格形容词。
- 今宜产品定位表述聚焦“目标用户 + 核心卖点 + 内容验证 / 迁移”，不再以泛化“需求增长”作为标题逻辑。
- 当前 10 秒审计第二轮：ONLINE-MAIN 个人优势压为两段，核心能力明确拆分“正式 AI 评测 / 质量治理”与“个人 Agent 项目 / 评测工程”。
- R1 recruiter-facing 标题优先使用当前 JD 可直接识别的“评测集、边界测试、Bad Case / 根因归因、版本回归、Tool Use、执行轨迹分析、自动化回归 / CI、Quality Gate”；内部工程词如 Eval Harness 保留在正文，不作为连续标题堆叠。
- R1 电商经历不能只保留搜索 / 数据能力：朗臻的核心高价值证据是从电商运营升级到宠物项目运营管理，必须保留项目经营、目标责任、优先级 / 排期 / 阶段检查、跨团队协调与方案汇报能力；今宜再保留数据诊断 / 产品定位 / 0→1。完整事实继续留在 FACT / CLAIM 和其他 Role Baseline。
- 人瑞所有简历版本统一使用正式职位显示：`评测专家（淘天 Data Agent）`。
- 数字前台统一明确为“个人 Agent 项目”；该来源属性不升级为创业 / commercial customer / 独立手写全部代码。
- 任务周处理量 5,000–10,000 从 ONLINE / R1 首屏与 recruiter-facing 展示移除，不删除事实源。

## 25.2 Agent Repo 与 Resume Fact 的边界

`wanghanyu654321-cell/-agent` 作为工程证据源，可证明仓库内已经实际实现并验证的 Runtime / Authority / Governed Knowledge / Durable State / Eval Harness / Regression / CI / PostgreSQL / FastAPI / pgvector / Docker 等能力。

Resume 的微信部署、实体本地生活门店 POC、开始实际使用等事实，属于经用户确认后进入 FACT MASTER / CLAIM LEDGER 的候选人事实。

两类证据不得互相越权：

- 工程 repo 未独立记录 business POC，不等于可以删除已确认 Resume Fact；
- Resume 有 POC / 实际使用，不等于可以把工程 repo 升级为 commercial customer deployment / Pilot acceptance / Production Ready；
- 普通微信验证、WeCom 工程实现、商业客户验收是三个不同概念，必须分别表达。

## 25.3 BossHunter 当前架构覆盖

前文“BossHunter + DeepSeek + 内部 Policy / Master 注入”保留为历史探索，不再作为默认实施路径。

BossHunter v2.4 已提供 Local Agent Tool API 后，默认架构改为：

```text
BossHunter collect / browser / DB / state / throttle / human-confirmation
        ↓
pending JD
        ↓
External Evaluator
(OUR_POLICY + BOSSHUNTER_MASTER + ROLE_INDEX + current JD)
        ↓
Match / hard gaps / role route / evidence
        ↓
POST evaluation back to BossHunter
        ↓
ready / filtered
        ↓
human confirmation
        ↓
BossHunter send
```

原则：

- BossHunter = execution engine；
- external evaluator = reasoning / policy layer；
- 不先修改 BossHunter 内部 Prompt；
- 不绕过人工确认；
- Frozen Set 先于 Policy 定制；
- BossHunter DB 负责 job lifecycle，`jianli` 负责 candidate fact truth；如需外部状态，只保留薄 `MATCH_LEDGER`，不再复制完整 APPLICATION_TRACKER 状态机。
