# R1｜Agent Eval / LLM Quality / AI Quality

## 求职方向

**Agent 评测 / LLM 质量 / AI Quality / 模型效果评测**

## 个人总结

具备淘天 **Data Agent 评测与质量治理**实际经历，工作覆盖 Query、召回结果、商品相关性、Data Agent 输出、复杂 Badcase、QA、争议 Case、规则治理及版本效果观察。除完成 Case 判断外，也承担新任务进入执行前的规则理解与验证：先用真实 Case 检查定义是否清楚、Context 是否足够、判断边界是否可执行，再与上级完成必要确认，并转化为下游 BPO 能稳定执行的标准、示例与培训内容。

在质量治理中，更关注**错误为什么发生、应该修改哪一层**，而不只记录错了多少。会结合 Case 特征、执行人员理解路径、规则表达和执行流程，区分业务知识不足、Context 缺失、规则边界过宽或执行方式等问题，再推动规则、示例、培训或流程调整。单项任务下游 BPO **10+ 人**、每周约 **5,000–10,000 条任务**；累计参与沉淀 **10+ 份 SOP / 规则 / 执行文档**，部分任务一致性约 **80%→95%**、复杂任务约 **60%→85%**。

数字前台 Agent 项目进一步把这套能力扩展到 Agent Eval：不只判断最终答案，而是继续检查 **Evidence、Routing、Tool / Authority、业务状态和 Handoff**。通过 Frozen Cases、Negative Controls、Badcase 根因定位、Regression 和 Acceptance Harness 判断一次修改是否真的提升版本，而不是把“修掉一个 Badcase”直接等同于 Agent 变好。

## 核心能力

**Agent 评测与质量治理**  
Eval Design｜Case / Dataset｜QA｜Badcase｜Root Cause｜Quality Governance

**Query / RAG 评测**  
Query / Recall / Relevance｜RAG / Evidence｜No-answer / Ambiguous｜Routing

**回归验证与版本验收**  
Frozen Cases｜Negative Controls｜Holdout｜Regression｜Acceptance Harness

**业务与数据 Context**  
Data Agent｜Search / Query Intent｜基础 SQL / 查询取数｜A/B / 灰度观察

## 工作经历

### 杭州人瑞网络科技有限公司｜Data Agent 评测｜2025.09–2026.06

- **Data Agent / Query / Relevance 评测：** 参与 Query、Data Agent 输出、召回结果和商品相关性评测，将用户意图、商品语义及业务规则落到具体 Case 判断；单项任务下游 BPO **10+ 人**、每周约 **5,000–10,000 条任务**，长期面对普通 Case 与高歧义复杂 Case 并存的质量场景。
- **评测规则验证与标准转译：** 新任务进入执行前，不直接将上游规则原样下发，而先结合真实 Case 检查定义是否清楚、Context 是否足够、边界是否过宽及真实场景是否覆盖；完成必要对齐后，再转化为下游可稳定执行的判断口径、示例和培训内容。
- **Badcase 根因分析：** 对重复偏差不简单归因于“执行人员不熟练”，而结合 Case、人员理解方式与规则本身判断问题来自业务知识、Context、规则表达、判断边界还是执行流程，再分别补充 Context、收窄边界、增加示例或调整执行方式。
- **QA 与争议 Case 处理：** 常规承担约 **10% 抽检**及质量复核，通过抽检识别高频分歧和异常模式；规则内能够稳定判断的问题直接推进修正，无法稳定裁定的争议 Case 则整理核心争议点后提交上级确认。
- **规则治理与质量结果：** 围绕反复出现的问题累计参与沉淀 **10+ 份 SOP / 规则 / 执行文档**，并持续收敛可执行边界；部分任务一致性约 **80%→95%**，复杂任务约 **60%→85%**。
- **准确率与执行成本平衡：** 补充业务 Context 时只保留真正影响判断的信息，避免为降低少量错误不断增加规则复杂度，反而提高下游理解成本和新的歧义空间。
- **版本效果与数据观察：** 参与执行层灰度桶 / A/B 测试及相关取数，结合 **DAU、CTR、转化、业务水位**观察版本变化和异常情况，并整理反馈。
- **Search / Query 链路理解：** 接触 Query 预处理 / 理解 / Rewrite、Recall、Filter、排序、SERP 与反馈链路，并使用 L1/L2/L3 相关性分级参与判断，帮助区分 Query 理解、召回和商品相关性等不同问题。

### 杭州今宜商贸有限公司｜抖音代运营兼职｜2024.11–2025.07

- **数据诊断与问题定位：** 本人直接承担巨量千川投流，根据 CTR、CVR、ROI、素材表现和直播承接判断问题位于前端内容、流量匹配还是后端转化，而不是依赖单一指标下结论。
- **对比验证与归因：** 当素材、主播、直播环境等多个因素同时影响结果时，尽量统一数据口径和其他关键条件，通过对比不同方案进一步缩小问题范围，形成“提出判断 → 验证 → 再调整”的分析习惯。
- **产品定位与内容实验：** 结合健身轻食需求增长调整玉米包目标用户和核心卖点，再通过短视频数据验证表达方向，并将有效表达迁移到直播场景。
- **0→1 项目结果：** 协同约 **6 人直播团队**推进内容、主播、投流和复盘，同一新盘账号月 GMV 从早期约 **7 万提升至接手首月约 43 万**。
- **达人冷启动：** 新盘缺少历史销量和成熟素材时参与达人筛选、触达和合作推进，相关合作单月销售额合计 **10 万元+**。

### 浙江朗臻网络科技有限公司｜电商运营 → 宠物项目运营管理｜2022.03–2024.07

- **Search / Query Intent：** 单品从 0→1 时先通过市场数据、搜索需求和关键词增长判断用户需求及竞争环境，再从更细分的搜索需求切入并逐步扩大关键词覆盖；通过热词 / 长尾词、标题和详情属性持续优化，推动核心商品搜索排名由百名外进入 **细分类目前 10**。
- **搜索数据与用户需求判断：** 搜索词不仅用于流量优化，也作为市场信号观察细分需求变化；结合商品属性和消费者反馈理解用户需求与商品匹配，为后续 Query / Relevance 判断提供真实业务 Context。
- **经营问题诊断：** 商品推广效果不达预期时，结合流量、点击、转化、商品和链接状态判断问题所在，再决定继续优化 Search、调整商品表达还是测试新的产品方向；另一核心 SKU **接手首月内日 GMV 约 1,000+→15,000+**。
- **用户需求与产品反馈：** 平台数据之外也直接联系消费者了解真实使用场景，并与更大范围市场 / 搜索数据区分使用；宠物项目中老客户持续出现的猫粮需求成为产品线扩展输入之一。
- **复杂业务 Context：** 后续负责约 **5 个跨平台店铺**，对 GMV、利润率、DSR 与渠道结果直接负责，并协同内容、客服、供应链、平台和工厂推进经营事项。

## 项目经历

### 数字前台 Agent｜Agent 评测 → 根因分析 → 回归验证 → 版本验收

**项目背景：** 面向小型门店 / 服务型商家的线上第一接待与私域承接。很多实体商家线下已经有人工接待，但微信等私域入口仍存在线上承接空白：重复咨询无人及时处理、预约 / 线索意向容易丢失、异常问题缺乏稳定流转。因此产品先聚焦：

**线上接待 → Knowledge / FAQ → 预约 / 线索意向 → 轻量业务状态 → Ticket / Handoff → 人工跟进。**

随着 Agent 开始进入业务 Workflow，质量问题不再只是“最终答案对不对”，还需要判断：**什么时候应该回答、什么时候必须停止、Tool 是否有权执行、业务动作有没有真的发生，以及修复一个问题后有没有破坏其他行为。**

**技术栈：** TypeScript / Node.js｜React｜Python / FastAPI｜PostgreSQL 16 / pgvector｜Docker Compose｜RAG / Knowledge｜Prompt / Instruction｜Tool Calling｜Agent Runtime｜Eval / Regression / Harness

- **Agent 评测与 Dataset 设计：** 将质量判断从最终答案扩展到 Evidence、Routing、Tool / Authority、No-answer、Ambiguous 和权限行为；冻结 **40 个 Cases（24 Answerable / 8 No-answer / 8 Ambiguous）**，用于同时验证“应该回答”和“应该停止”，不将该比例包装成真实生产流量分布。
- **安全边界与负向测试：** 加入 tenant / store isolation、未批准 Evidence、失效 / retired Evidence 等 Negative Controls，验证“检索到了”不等于“当前有资格回答”；即使技术上检索成功，只要 scope、status、version 或 ambiguity 条件不成立，仍要求 fail closed。
- **Badcase 根因分析：** Eval 失败后不直接调 Prompt，而先判断是否拿到正确 Evidence、Evidence 是否允许使用、Tool / Authority 是否成立、业务动作是否执行、Workflow 是否正确；只有底层链路正常而模型行为选择仍偏差时，才优先调整 Prompt / Instruction。
- **回归验证与版本判断：** 修复目标 Badcase 后重新跑 Frozen Cases / Holdout，同时检查正常回答、No-answer、Ambiguous 和权限边界是否退化，用来区分“整体提升”“局部修复”还是“表面改善”，坚持 **Badcase Fixed ≠ Version Improved**。
- **业务结果验收：** 当发现模型文本或 Tool Call 本身不能证明业务动作真正发生后，将 Ticket / Handoff 等动作的成功标准进一步收紧为 **权限通过 → 状态写入 → 持久化 → scoped read-back → 验收**，避免把“模型说完成”误判为真实完成。
- **评测完整性与 Harness：** 当发现 Case Population、Config / Corpus Drift、Evidence 变化或 Completion State 可能影响结论时，先修 Eval 再判断 Agent；将 Agent Quality 和 Measurement Integrity 分开，降低评测流程本身制造 False-PASS 的风险。
- **版本治理：** 将目标 Case、Regression、Acceptance 与 Harness Integrity 共同用于阶段性版本判断；不同风险类型分别保留自己的 PASS / FAIL 语义，不用单一综合分数掩盖权限、业务状态或安全问题。

**当前状态：** 已形成 Pre-ICP Engineering Baseline；尚不声称真实客户 POC、Production 或真实线上质量指标。
