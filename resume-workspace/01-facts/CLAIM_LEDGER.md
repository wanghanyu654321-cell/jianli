# Claim Ledger

事实真源：`FCT-001`。当前 GitHub mirror：`resume-workspace/01-facts/FACT_MASTER_CURRENT.md`。

## Source epoch binding

- `derived_from_source_epoch`: `FCT-EPOCH-20260916-04094915`
- Current Git blob SHA: `040949158e76a356caf81f4185da2c4a17528e04`
- Previous repository epoch: `FCT-EPOCH-20260916-6D82DB08`
- Known external DOCX fingerprint before this GitHub mirror update: `38A34FF8CF39A4D69AF20FD043C170D15A8DD0A882A8414A5311CF0FE52E140C`
- `FACT_CURRENCY`: `CURRENT`
- `CLAIM_MAPPING_INTEGRITY`: `CURRENT_FOR_FCT_MASTER`; current R1–R6 V4 drafts predate this enrichment epoch and require semantic revalidation / Skills optimization before being considered current against it.

本 Ledger 只映射当前 `FACT_MASTER_CURRENT.md` 中的事实，不从旧快照、旧 exclusion、JD、Skill、推测或未确认记忆恢复额外内容。

| claim_id | 可对外主张 | evidence locator | status | 使用边界 |
|---|---|---|---|---|
| FCT-01 | 当前求职方向可围绕 FDE/AI 应用交付、Agent Eval、MaaS/AI Solution、AI 电商和 AI 产品运营做不同强调 | FCTM-XR-01~04 | FACT_DOCUMENTED | 仅作为求职方向与能力解释，不代表每个方向都有正式职位经历。 |
| FCT-02 | 杭州人瑞评测专家，服务淘天 Data Agent，2025.09–2026.06 | FCTM-TL-02, FCTM-RR-01 | FACT_DOCUMENTED | Title 与服务场景保持。 |
| FCT-03 | 参与 Query、Data Agent 输出、召回结果、商品相关性、Badcase、QA、争议 Case 和规则治理 | FCTM-RR-01 | FACT_DOCUMENTED | 争议 Case 无法直接裁定时提交正式员工；不写最终业务裁决权。 |
| FCT-04 | 人瑞团队 10+ 人、每周约 5,000–10,000 条，个人日处理约 100–120 条，常规抽检约 10% | FCTM-RR-02 | FACT_DOCUMENTED | 团队规模与个人工作量分开。 |
| FCT-05 | 部分任务一致性约 80%→95%，复杂任务约 60%→85%；团队累计沉淀 10+ SOP/规则/执行文档，本人负责/参与其中一部分 | FCTM-RR-03 | FACT_DOCUMENTED | “部分任务”限定词必须保留；一致性/执行正确率不写成模型准确率；10+ 不写成本人独立完成。 |
| FCT-06 | 接触 DAU、CTR、转化相关指标、灰度流量、业务水位，并按时间维度观察版本和异常变化 | FCTM-RR-16 | FACT_DOCUMENTED | 不写独立 A/B Owner、完整线上权限或独立策略；不擅自补小时/日等精确时间粒度；eCTR/pCTR/eCVR/pCVR/UVCTR/Lift 暂未确认。 |
| FCT-07 | 历史约 3% CTR 记忆无法恢复业务、分母和周期 | EX-01 | EXCLUDE | 正式简历禁用。 |
| FCT-08 | 接触并理解 Query 预处理/理解/Rewrite→Recall→Filter→Coarse Rank→Fine Rank→Rerank→SERP→Feedback/A-B，理解 L1/L2/L3 相关性 | FCTM-RR-17 | FACT_DOCUMENTED | 只写理解/接触，不写算法实现。 |
| FCT-09 | 杭州今宜负责抖音项目代运营/项目运营/BD，2024.11–2025.07，覆盖项目经营、直播、内容、投流、店铺数据、达人 BD、项目排期和合作方汇报等 | FCTM-TL-02, FCTM-JY-01~26 | FACT_DOCUMENTED | 不拆虚构雇佣主体；运营方案汇报不升级为 AI 售前/POC。 |
| FCT-10 | 同一账号属于新盘 0→1：早期月 GMV 约 7 万，接手后首月约 43 万 | FCTM-JY-01 | FACT_DOCUMENTED | 禁止写“成熟差盘救火”；不写未经支持的增长倍数。 |
| FCT-11 | 另一独立账号负责期间单月 GMV 峰值约 152 万 | FCTM-JY-21 | FACT_DOCUMENTED | 与 FCT-10 分开；不得混为同一增长曲线。 |
| FCT-12 | 协同约 6 人直播团队，覆盖策略、目标拆解、排期、培训协同、跟播、内容、投流、数据与复盘 | FCTM-JY-22 | FACT_DOCUMENTED | 项目协作规模，不写全部行政直管。 |
| FCT-13 | 今宜投手职责由本人承担，使用巨量千川等投放链路，并结合 CTR/CVR/ROI、素材表现、直播承接和业务目标进行投放判断 | FCTM-JY-08~11 | FACT_DOCUMENTED | 禁止写“协同投手”；不写投放系统/算法开发。 |
| FCT-14 | 参与店铺评分、流量/营销/交易数据和推广/大促策略分析 | FCTM-JY-24 | FACT_DOCUMENTED | 不补未确认增长数字。 |
| FCT-15 | 冷启动阶段以 KOC/匹配达人为主做直接 BD，单月达人合作销售额合计 10 万元+，并沉淀筛选/触达/合作推进流程 | FCTM-JY-15~20, FCTM-JY-23 | FACT_DOCUMENTED | 不是“累计 10 万+”；不写全量 KOL 资源盘。 |
| FCT-16 | 浙江朗臻任京东电商运营→宠物项目管理，2022.03–2024.07 | FCTM-TL-02, FCTM-LZ-01~23 | FACT_DOCUMENTED | 不写返岗。 |
| FCT-17 | 正大小仟牙膏单品类 2022 年 GMV 约 300 万+，2023 618 GMV 约 50 万 | FCTM-LZ-06 | FACT_DOCUMENTED | 单品类结果，不是品牌总盘。 |
| FCT-18 | 通过热词/长尾词、标题、详情属性等做搜索经营，核心商品搜索排名由百名外到类目前 10 | FCTM-LZ-02~03 | FACT_DOCUMENTED | 不写算法研发。 |
| FCT-19 | 另一核心单 SKU 日 GMV 约 1,000+→15,000+，约 15 天 | FCTM-LZ-05 | FACT_DOCUMENTED | 与 FCT-18 不强行建立同商品/单一因果。 |
| FCT-20 | 使用实时经营数据、京东快车、京准通 | FCTM-LZ-18 | FACT_DOCUMENTED | 不补未确认平台工具；不把不同平台玩法写成同一机制。 |
| FCT-21 | 胖小虎约 5 个跨平台店铺，年度整体 GMV 约 1,200 万–2,000 万，日常约 4–5 万，双 11 月约 200 万 | FCTM-LZ-17 | FACT_DOCUMENTED | 业务盘面与个人贡献分开。 |
| FCT-22 | 对胖小虎 GMV、利润率、DSR、月/季目标和渠道结果直接负责 | FCTM-LZ-17 | FACT_DOCUMENTED | 老板做最终经营审查。 |
| FCT-23 | 参与预算分配、商品/项目生命周期推进，并协同约 5 人小红书团队和约 5 人客服团队 | FCTM-LZ-19~21 | FACT_DOCUMENTED | 协同人数不等于行政直管；不写最终公司级预算权。 |
| FCT-24 | 企业客服 Agent / Support Agent 项目定位为 synthetic portfolio / proof application，证据定位为 `wanghanyu654321-cell/-agent` / `job-ready/integration-v1`；已独立核验顶层 README 与部分 Eval 资产 | FCTM-AG-00, FCTM-AG-05 | REPO_PARTIALLY_VERIFIED | 仅部分仓库证据完成核验；不升级为生产/客户项目。 |
| FCT-25 | 项目材料描述 Node.js/FastAPI/PostgreSQL16/pgvector/React/Docker Compose/Nginx/Pi Runtime 和权限边界；README 已核到其中多项 | FCTM-AG-02 | REPO_PARTIALLY_VERIFIED | 不据此宣称生产部署；未逐项核验的技术仍按项目材料使用。 |
| FCT-26 | 项目材料描述 Runtime/Tool-call Budget、工具、词法检索、Evidence Governance、Routing 与 Safety/Authority 边界 | FCTM-AG-03 | DOCUMENTED_ONLY | Hybrid/RRF/Reranker/Formal Query Rewrite/Model Routing 未完整完成。 |
| FCT-27 | 项目有 40 Frozen Cases；已核验评测集 24 answerable/8 no-answer/8 ambiguous，并包含 gold/version/provenance、negative controls 与 deterministic metrics；另有 Safety 30/30、Robustness 100/100、Holdout 60/60、Governed Knowledge 46/46、Public Top1 96%、Recall@3 100%、Routed Outcome 100% 等记录 | FCTM-AG-04 | REPO_PARTIALLY_VERIFIED | 测试/评测资产不是生产流量；Holdout 60/60 不等于 60 个独立样本；retrieval-quality 未批准 overall PASS threshold。 |
| FCT-28 | Agent 项目中本人负责 Problem Definition、架构边界、Acceptance、Eval、Badcase、方案取舍、测试验收和项目状态判断，通过 AI Coding Agent 协作实现 | FCTM-AG-01 | FACT_DOCUMENTED | 不写独立手写全部代码。 |
| FCT-30 | 时间轴：工作起点 2022.03、毕业 2022.06；朗臻 2022.03–2024.07、今宜 2024.11–2025.07、人瑞 2025.09–2026.06；空档 2024.08–10 与 2025.08 | FCTM-TL-01~04 | FACT_DOCUMENTED | 日期和空档不可变；不写“5 年经验”。 |
| FCT-31 | 朗臻 0→1 时先以市场/搜索/增长数据判断机会，优先增长细分市场；红海则找产品差异化 | FCTM-LZ-01~04 | FACT_DOCUMENTED | 不升级为公司级战略负责人。 |
| FCT-32 | 朗臻直接电话联系消费者补充需求信息；狗粮老客对猫粮需求成为产品开发方向输入之一 | FCTM-LZ-07~09 | FACT_DOCUMENTED | 不写成大规模用户研究；消费者反馈不直接等同整体市场。 |
| FCT-33 | 工厂产品开发由老板定大方向，本人基于市场/用户/经营信息落细需求、推进具体事项并反馈进展 | FCTM-LZ-10 | FACT_DOCUMENTED | 不写独立产品战略或最终合同决策。 |
| FCT-34 | 本人直接参与京东小二合同条件、毛利结构、合作方式和活动资源讨论，并做推广费/扣点等 Trade-off | FCTM-LZ-11~13 | FACT_DOCUMENTED | 最终是否接受由老板拍板。 |
| FCT-35 | 参与经营侧库存预测、备货排期、入出库、尾货活动处理及爆单跨仓调拨，以尽量避免断货 | FCTM-LZ-14~16 | FACT_DOCUMENTED | 不写专业供应链网络架构负责人。 |
| FCT-36 | 小红书由本人负责策略/运营管理，团队执行；确认循环为选题→测文章→复刻→测数据→养号→发文章→重复循环 | FCTM-LZ-19 | FACT_DOCUMENTED | 不写本人承担全部发文/养号执行。 |
| FCT-37 | 今宜新盘起步先检查视频素材、直播环境、机位、主播话术，先补底层承接再用投流放大 | FCTM-JY-02 | FACT_DOCUMENTED | 这是起盘优先级判断，不写成固定行业公式。 |
| FCT-38 | 玉米包根据健身轻食市场增长将定位从常见宝宝辅食转向健身轻食/营养健康/方便易食，并转成可视化场景 | FCTM-JY-04~05 | FACT_DOCUMENTED | 事实为产品/内容定位，不补未确认转化数字。 |
| FCT-39 | 直播较快验证商品/卖点/话术；短视频多计划测素材并反哺直播；有效“刚出锅冒热气”画面被迁移为双机位持续展示 | FCTM-JY-06~07 | FACT_DOCUMENTED | 双机位由本人提出/设计/指导，不写全部技术执行。 |
| FCT-40 | 通过 CTR/CVR 组合、统一数据口径、控制其他变量、改变单一变量做 A/B 缩小问题范围 | FCTM-JY-08~10 | FACT_DOCUMENTED | 不夸张成严格科研实验。 |
| FCT-41 | 项目开始前与老板对齐 GMV/ROI/利润/新盘增长等优先目标，再决定投放、利润容忍度、内容和达人策略 | FCTM-JY-14 | FACT_DOCUMENTED | 最终经营目标由服务关系/老板确认。 |
| FCT-42 | 新盘达人 BD 用于补销量/权重：本人直接开发达人，纯佣为主，KOC 优先，佣金可高同行约 3–5 个点，并接受在覆盖退款/货损等底线后阶段性让利 | FCTM-JY-15~19 | FACT_DOCUMENTED | 描述冷启动阶段 Trade-off，不写长期利润策略。 |
| FCT-43 | 人瑞新任务接收后先理解规则和数据口径、本人先跑 Case、集中找逻辑/边界/Context 缺口，与正式员工对齐后再下发 BPO | FCTM-RR-04~07 | FACT_DOCUMENTED | 承上启下，不写正式项目 Owner。 |
| FCT-44 | BPO 错误可能来自品牌/商标等行业 Context 缺失；培训前先定任务大边界和必要 Context，并兼顾效率与正确率 | FCTM-RR-08~11 | FACT_DOCUMENTED | 不把所有错误归因于知识不足。 |
| FCT-45 | 抽检后会还原执行人员思考路径，区分知识/规则/边界/流程问题，再补 Context、收窄边界或调整 SOP/示例并继续观察 | FCTM-RR-12~14 | FACT_DOCUMENTED | 这是稳定处理机制，不需要虚构单一典型案例。 |
| FCT-46 | 执行过程中持续向正式员工同步进度、阶段、问题和待确认事项，保持过程可追溯 | FCTM-RR-15 | FACT_DOCUMENTED | 不升级为独立项目总负责人。 |
| FCT-47 | 朗臻和今宜均具有明显 0→1 特征；跨经历稳定逻辑是理解目标/上下文→取信号→定位问题→优先可控因素→设计方案→验证→继续收敛 | FCTM-XR-01~02 | FACT_DOCUMENTED | 作为跨经历事实归纳，不直接写“全域人才/适应力强”。 |
| FCT-48 | SOP 是反复问题被验证后的可能沉淀，不是每个经历的固定终点 | FCTM-XR-03 | FACT_DOCUMENTED | 不强迫所有经历以 SOP 作为终点。 |
| FCT-49 | 人瑞正式任务框架通常由正式员工确定，但本人会在真实 Case 执行中参与定义/补充评测类目，并形成较稳定的 Badcase 分类/归因 | FCTM-RR-18 | FACT_DOCUMENTED | 不写整套 Task/Rubric 最终 Owner。 |
| FCT-50 | 人瑞规则/SOP/示例/执行方式调整后会复测或通过后续抽检再验证，质量提升数字来自持续治理与验证闭环 | FCTM-RR-19, FCTM-RR-03 | FACT_DOCUMENTED | 不写本人单独造成全部提升；不升级为模型准确率。 |
| FCT-51 | 人瑞 Agent 评测还涉及多轮上下文、工具调用结果、步骤完整性、信息收集完整性和最终回答是否解决 Query | FCTM-RR-20 | FACT_DOCUMENTED | 可写 Agent Behavior/Workflow Quality 评测；不写本人实现 Runtime/Tool Calling。 |
| FCT-52 | 本人可阅读简单 SQL 并做基础查询取数；所服务 Data Agent 具备自动生成 SQL 指令能力，日常业务数据通常脱敏 | FCTM-RR-21 | FACT_DOCUMENTED | 不写 SQL 开发/数据工程；Data Agent 自动 SQL 不是本人实现。 |
| FCT-53 | 人瑞反馈规则/产品/系统问题后，部分事项会继续跟进修改结果并参与补充验证 | FCTM-RR-22 | FACT_DOCUMENTED | 通常是补充/反馈/验证角色，不写产品 Owner 或最终上线负责人。 |
| FCT-54 | 人瑞团队评测资产包括任务说明、评测标准/判断说明、Case/示例、FAQ、问题清单等，本人负责或参与其中一部分 | FCTM-RR-23 | FACT_DOCUMENTED | 团队资产与个人负责范围分开。 |
| FCT-55 | Agent 项目实际迭代过 Prompt、System Instruction、Tool Instruction，并结合 Badcase/测试结果/通过情况比较版本差异 | FCTM-AG-06 | FACT_DOCUMENTED | 可写 Prompt/Instruction iteration；不写真实客户 Prompt 调优交付。 |
| FCT-56 | 朗臻和今宜都有需求/事项清单、优先级判断、项目排期与阶段检查 | FCTM-LZ-22, FCTM-JY-25, FCTM-XR-04 | FACT_DOCUMENTED | 不自动升级成 PRD/Roadmap Owner。 |
| FCT-57 | 朗臻会向老板做运营/项目方案与进展汇报；今宜代运营会向合作方做运营方案/项目进展汇报 | FCTM-LZ-23, FCTM-JY-26, FCTM-XR-04 | FACT_DOCUMENTED | 属于运营/项目方案沟通，不写 AI Demo/POC/技术售前或真实 AI 客户交付。 |

## Evidence status vocabulary

- `FACT_DOCUMENTED`：当前 `FCT-001 / FACT_MASTER_CURRENT.md` 明确支持，可按边界表达。
- `REPO_PARTIALLY_VERIFIED`：对应项目主张已有一部分仓库原始证据被独立核验，但不能外推到未核验技术、生产状态或客户状态。
- `DOCUMENTED_ONLY`：事实母版有描述，但对应仓库/生产/客户原始证据尚未逐项独立核验；不能升级成已核验实现或生产结果。
- `EXCLUDE`：明确禁止进入正式简历或尚未确认。

## Rebase behavior

后续事实源发生变化时：
- 先做 semantic delta；
- 未变化 Claim 继承；
- 变化 Claim 重新核验 boundary；
- 新事实创建新 Claim；
- 撤回事实标记 superseded / excluded；
- 任何受影响的 Resume artifact 必须重新做 Semantic Claim Check。
