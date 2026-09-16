# [姓名]

[LOCAL_ONLY_CONTACT]

## Target Role

**Agent Eval / LLM Quality / AI Quality**

## Professional Summary

现从事淘天 **Data Agent 评测与质量治理**，工作覆盖 Query、召回结果、商品相关性、Data Agent 输出、复杂 Badcase、QA、争议 Case 与规则治理。除完成评测任务外，也承担新任务规则理解与执行准备：先验证规则在真实 Case 中是否具备足够可执行性，再与上级对齐业务口径和判断边界，最终转化为下游团队能够稳定执行的标准。

在质量治理中，更关注“为什么会产生错误”而不只统计错误本身。会结合抽检结果、执行表现和人员反馈区分业务 Context 缺失、规则理解偏差、边界不清或执行方式等不同问题，并推动规则说明、示例、培训和执行流程持续收敛。单项任务下游 BPO 执行人数 **10+ 人**，每周处理约 **5,000–10,000 条任务**，累计沉淀 **10+ 份 SOP / 规则 / 执行文档**；部分任务一致性由约 **80% 提升至 95%**，复杂任务由约 **60% 提升至 85%**。

同时参与执行层灰度桶 / A/B 测试及相关数据取数，结合 DAU、CTR、转化、业务水位等指标观察版本效果和异常变化。数字前台 Agent 作品进一步将 Eval 用于 **Agent 升级与版本判断**：围绕线上接待、私域线索与预约意向承接中的 RAG、Evidence、Tool Calling、Routing、权限与 Agent Behavior 设计 Dataset / Negative Controls，通过 Badcase Attribution 定位应修改 Prompt / Instruction、Retrieval、Tool 还是 Workflow，再用 Regression 判断版本是否真正提升；同时通过 Acceptance Harness 检查评测数据、配置和执行完整性，避免测试本身制造 False-PASS。此前电商经历则补充了 Search / Query Intent、商品语义和真实经营场景，使评测判断能够同时理解模型输出、用户需求和业务 Context。

## Core Competencies

**Eval Design / Quality**  
Eval Design｜Case / Dataset｜QA｜Badcase｜Root Cause｜Metrics｜Data Quality

**Agent / RAG Evaluation**  
Query / Recall / Relevance｜RAG / Evidence｜Tool Calling｜Routing｜Agent Behavior

**Regression / Harness**  
Frozen Cases｜Negative Controls｜Regression｜Holdout｜Acceptance Harness｜Eval Integrity

**Business / Data Context**  
Data Agent｜Search / Query Intent｜基础 SQL / 查询取数｜版本指标观察

## Work Experience

### 杭州人瑞网络科技有限公司｜Data Agent 评测｜2025.09–2026.06

- **Data Agent / Query / Relevance 评测：** 参与 Query、Data Agent 输出、召回结果和商品相关性评测，将业务规则、商品语义和相关性要求落到具体 Case 判断中；单项任务下游 BPO 执行人数 **10+ 人**、每周处理约 **5,000–10,000 条任务**，长期面对普通 Case 与高歧义复杂 Case 并存的质量场景。
- **新任务规则验证与执行转译：** 承接新的业务规则或任务要求后，不直接将上游文档原样交给执行团队，而会先结合真实 Case 验证规则是否存在定义不清、边界过宽、Context 不足或实际场景未覆盖等问题；完成必要对齐后，再将业务要求转化为下游可以稳定执行的判断口径和培训内容。
- **复杂 Badcase / Root Cause：** 对反复出现的评测偏差，不仅记录错误结果，还会结合 Case 特征、执行人员理解和规则本身判断问题主要来自知识背景、规则表达、判断边界还是执行链路；根据原因推动规则补充、示例完善、必要 Context 补充或执行方式调整，避免把所有问题简单归因于“人员不熟练”。
- **QA 与质量闭环：** 常规承担约 **10% 抽检**以及质量复核，通过抽检发现高频分歧和异常模式，并将结果重新反馈到培训、规则和执行流程中；对于可以在现有规则下确定的问题直接推进修正，对无法稳定裁定的争议 Case，则整理核心争议点后提交上级确认。
- **规则治理与质量结果：** 围绕反复出现的执行问题累计沉淀 **10+ 份 SOP / 规则 / 执行文档**，并持续收敛可执行边界；在规则治理、培训和质量复核过程中，部分任务一致性由约 **80% 提升至 95%**，复杂任务一致性由约 **60% 提升至 85%**。
- **准确性与执行成本平衡：** 补充业务 Context 时只保留真正影响判断的信息，在降低理解偏差的同时避免规则过度复杂、增加下游执行成本。
- **上下游协作：** 执行中持续向上级同步任务阶段、已发现问题和待确认项，对规则或业务歧义尽早完成确认，减少批量执行后的返工。
- **版本效果与数据观察：** 参与执行层灰度桶 / A/B 测试，结合 **DAU、CTR、转化、业务水位**等指标进行数据取数和版本效果观察，并汇总异常结果与反馈。
- **搜索 / 推荐链路理解：** 接触并理解 Query 预处理 / 理解 / Rewrite、Recall、Filter、排序、SERP 与反馈等整体链路，并使用 L1/L2/L3 相关性分级参与判断；该背景帮助区分 Query 理解、召回、相关性及后续链路中的不同问题类型。

### 杭州今宜商贸有限公司｜抖音代运营兼职｜2024.11–2025.07

- **新盘 0→1 与问题优先级判断：** 项目处于新盘起量阶段，进入后先从内容素材、直播表现、主播表达和流量承接等环节判断影响增长的主要问题，再确定哪些环节优先调整；经营逻辑并非单纯增加投放，而是先保证基础转化链路具备放量条件。
- **本人直接承担投流与数据诊断：** 使用巨量千川等投放链路，根据 **CTR、CVR、ROI、素材表现和直播承接**判断问题更偏向前端内容、流量匹配还是后端转化，并据此调整投放与运营重点，而不是通过单一指标直接下结论。
- **对比验证与归因：** 当多个因素可能同时影响结果时，会尽量保持数据口径和其他核心条件一致，通过对比不同素材、主播或执行方案进一步缩小问题范围；这类工作形成了较稳定的“提出判断—验证—再调整”的数据分析习惯。
- **产品定位与内容实验：** 结合健身轻食需求增长重新调整玉米包的目标用户和核心卖点，并围绕新定位优化短视频与直播画面表达；短视频中验证出更有效的方向后，再将核心表达迁移到直播场景，并参与双机位直播方案设计。
- **经营结果与团队协作：** 协同约 **6 人直播团队**推进策略、目标拆解、排期、培训协同、跟播、内容、投流和复盘；同一新盘账号月 GMV 从早期约 **7 万**提升至**接手首月约 43 万**。
- **达人冷启动与流程沉淀：** 新盘缺乏历史销量和成熟素材时，直接参与达人筛选、触达和合作推进，以 KOC 和内容匹配度为重要筛选依据，并根据冷启动阶段目标调整合作条件；相关合作 **单月销售额合计 10 万元+**，同时将高频合作环节沉淀为可重复执行流程。
- **经营分析：** 结合店铺、流量、营销和交易数据持续定位商品、内容、流量与转化问题。

### 浙江朗臻网络科技有限公司｜电商运营 → 宠物项目运营管理｜2022.03–2024.07

- **Search / Query Intent：** 单品从 0→1 时，先通过市场数据、搜索需求和关键词增长判断用户需求与竞争环境，再从更细分的搜索需求切入并逐步扩大关键词范围；通过热词 / 长尾词、商品标题和详情页属性等持续优化，推动核心商品搜索排名由百名外提升至 **细分类目前 10**。
- **从搜索数据理解市场需求：** 搜索词不仅被用于优化排名，也被作为市场信号观察细分需求变化和潜在增长方向；该经历形成了从 Query / Keyword 反推用户意图、商品匹配与市场变化的实际业务背景。
- **经营问题诊断：** 商品推广效果不达预期时，会结合实时经营数据区分流量、点击、转化、商品或链接层面的问题，再决定继续优化、调整商品表达还是测试新的产品方向；另一核心单 SKU **接手首月内日 GMV 由约 1,000+ 提升至 15,000+**。
- **用户反馈与需求验证：** 在平台数据之外，也通过直接消费者沟通补充真实使用场景和需求信息，并将其与更广泛的市场 / 搜索数据区分使用；宠物项目中，老客户持续出现的猫粮需求成为产品线扩展方向的输入之一。
- **多店项目经营：** 转入宠物项目运营管理后负责胖小虎约 **5 个跨平台店铺**，对 GMV、利润率、DSR、月 / 季目标和渠道结果直接负责；业务年度整体 GMV 约 **1,200 万–2,000 万**，涉及实时经营数据、京东快车、京准通等工具与渠道。
- **复杂业务协作：** 参与预算分配和商品 / 项目生命周期推进，并协同约 **5 人小红书团队、5 人客服团队**以及供应链、品牌方、京东小二和工厂 / 产品开发侧完成经营任务；这种跨商品、用户、渠道和协作角色的业务 Context，成为后续判断复杂电商 Query / 商品相关性问题的重要背景。

## Selected Project

### 数字前台 Agent｜Eval → Agent Upgrade → Acceptance Harness

**项目背景：** 面向小型门店 / 服务型商家的线上第一接待与私域承接场景，产品被收敛为一条明确业务链：**在线接待 → Knowledge / FAQ 回复 → 私域线索与预约意向承接 → 轻 CRM Booking / 状态留痕 → Ticket / Handoff → 人工跟进**。它不替代完整 CRM，也不扩展为全能数字员工。随着 RAG、Tool 与权限逐步增加，项目需要进一步回答：一次修改究竟有没有让数字前台真正变好，以及用于判断好坏的 Eval 本身是否可信。

- **Eval Design / Dataset：** 将质量判断从最终答案扩展到 RAG Evidence、Routing、Tool / Authority、No-answer、Ambiguous 和权限行为；冻结 **40 个 Cases（24 answerable / 8 no-answer / 8 ambiguous）**，并加入 tenant / store isolation、未批准及失效 Evidence 等 Negative Controls，使“应该回答”和“应该停止”都有明确标准。
- **Badcase / Root Cause：** Eval 失败后不直接调 Prompt，而是区分问题来自 **Prompt / Instruction、RAG / Evidence、Routing、Tool / Authority 还是 Workflow**，再修改对应层；实际迭代 Prompt、System Instruction 与 Tool Instruction，并比较修改前后行为。
- **Regression / Metrics：** 通过 Frozen Cases、Holdout 和固定指标重新检查目标 Badcase，同时验证正常回答、No-answer、歧义及权限边界是否出现 Regression，用于判断修改属于整体提升、局部修复还是表面改善。
- **Eval Integrity / Harness：** 当发现 Case Population 混淆、Measurement 未被真实结果支持时先修 Eval；Acceptance Harness 进一步检查 Case 缺失 / 重复、Config / Corpus Drift、Evidence 变化及 Completion State，降低评测流程产生 False-PASS 的风险。
- **Version Decision：** 将 Eval Metrics、Badcase、Regression 与 Harness Integrity 共同用于阶段性 Acceptance，决定当前版本继续迭代、进入 POC，还是保持 Blocked。

**场景价值：** 不只知道数字前台 Agent 哪里错，还能建立一条 **Eval → Attribution → Modification → Regression → Harness → Version Decision** 的持续升级链路；当前已形成可运行 Demo，处于 Demo / POC 与上线前验证阶段。

## Education

[LOCAL_ONLY_EDUCATION]  
毕业时间：**2022.06**