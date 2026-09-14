# Claim Ledger

事实真源：`FCT-001`（`简历母版.docx`）。本 Ledger 由最后一次仓库已知冻结源派生，不替代原始 DOCX。

## Source epoch binding

- `derived_from_source_epoch`: `FCT-EPOCH-20260913-7EAA096A`
- Frozen source SHA256: `7EAA096A7220DE0609E3AACAEA656B4CEEFB006D1419FA01BC07E97FFFCDDDEB`
- `CLAIM_MAPPING_INTEGRITY`: available for artifacts mapped to this Ledger
- `FACT_CURRENCY`: `STALE_PENDING_REBASE`
- Reason: R1 V3 Audit records a later local FCT-001 fingerprint change after this Ledger was built. Timeline anchors remained unchanged, but non-timeline semantic delta has not been rebased.

因此，本 Ledger 当前可以回答“某个现有 artifact 是否映射到 `FCT-EPOCH-20260913-7EAA096A`”，但不能回答“它是否已经覆盖本地最新 FCT-001 的全部变化”。Source Rebase 完成前，不得基于聊天、JD、Skill 或推测向本 Ledger 新增候选人事实。

## Rebase metadata for this epoch

- Source hash before canonicalization: `B31C7EC90FFEB48B023E43C37CBACB08817A562B3A42C1148B34DFE3BA4FB6E1`
- Source hash after canonicalization: `7EAA096A7220DE0609E3AACAEA656B4CEEFB006D1419FA01BC07E97FFFCDDDEB`
- Previous historical fingerprint: `037FB4FA3B77157F5DBE201971E3962241DC897FCAF39DC903897A327518528D` (`SUPERSEDED`)
- Source reread for this epoch: `YES`
- Document version: `V3`; DER-001 extraction: 646 paragraphs, 0 tables, 601 derived text lines.
- Graduation date: `2022.06`; career start: `2022.03`; `WORK_START_BEFORE_GRADUATION = VALID_USER_CONFIRMED_FACT`.
- Timeline re-read: Langzhen `2022.03–2024.07`; Jinyi `2024.11–2025.07`; Renrui `2025.09–2026.06`.
- Timeline gaps preserved: `2024.08–2024.10` and `2025.08`.
- Cross-role employment overlap: `PASS`.

| claim_id | 可对外主张 | evidence locator | status | 使用边界 |
|---|---|---|---|---|
| FCT-01 | 目标方向覆盖 FDE/AI 应用交付、Agent Eval、MaaS/售前、AI 电商和 AI 产品运营 | DER-001:1-29 | FACT_DOCUMENTED | 作为方向，不等于所有方向都有正式职位经历。 |
| FCT-02 | 在杭州人瑞担任评测专家，服务淘天 Data Agent，2025.09–2026.06 | DER-001:35-50 | FACT_DOCUMENTED | 可写评测专家和服务场景；不改 Title。 |
| FCT-03 | 参与 Data Agent 输出、Query、召回结果和商品相关性评测，组织评测执行、QA、争议处理和汇总 | DER-001:39-50 | FACT_DOCUMENTED | 不能写成独立产品负责人或独立线上策略负责人。 |
| FCT-04 | 团队 10+ 人、每周约 5,000–10,000 条、个人日处理约 100–120 条、抽检约 10% | DER-001:51-57 | FACT_DOCUMENTED | 规模是团队/任务口径；个人贡献只写明确的个人量。 |
| FCT-05 | 部分任务一致性约 80%→95%，复杂任务约 60%→85%，沉淀 10+ SOP/规则/执行文档 | DER-001:58-62 | FACT_DOCUMENTED | “部分任务”限定词必须保留。 |
| FCT-06 | 接触部分 DAU、CTR、转化、灰度流量和业务水位，可参与版本效果观察和问题汇总 | DER-001:63-71 | FACT_DOCUMENTED | 不写完整线上权限、独立 A/B 分桶或独立策略。 |
| FCT-07 | 约 3% CTR 记忆无法恢复业务、分母和周期 | DER-001:72-73 | EXCLUDE | 正式简历和公开项目禁用。 |
| FCT-08 | 理解 Query 预处理/理解/改写→召回→过滤→粗排→精排→重排→SERP→反馈/A/B，使用 L1/L2/L3 相关性分级 | DER-001:74-84 | FACT_DOCUMENTED | “接触并理解”不写成亲自实现搜索链路。 |
| FCT-09 | 在杭州今宜负责抖音项目代运营/项目运营/BD，2024.11–2025.07，覆盖项目经营、直播、投流、素材、店铺、数据、达人 BD、SOP | DER-001:95-101 | FACT_DOCUMENTED | 九米六业务并入今宜，不拆主体。 |
| FCT-10 | 同一账号接手前月 GMV 约 7 万，接手后首月约 43 万 | DER-001:102-108 | FACT_DOCUMENTED | 写绝对值变化；不写未经事实支持的“翻倍”。 |
| FCT-11 | 另一独立账号负责期间单月 GMV 峰值约 152 万 | DER-001:109-115 | FACT_DOCUMENTED | 不能与 FCT-10 混写；618/日常峰值暂不归属。 |
| FCT-12 | 直播项目协同约 6 人，负责策略、目标拆解、排期、培训协同、跟播、投流调整和复盘 | DER-001:116-140 | FACT_DOCUMENTED | 写项目管理/协作，不写 6 人行政直管。 |
| FCT-13 | 使用巨量千川等投放链路，依据 CTR/CVR/ROI 做素材和投放迭代 | DER-001:141-167 | FACT_DOCUMENTED | 不能扩写为平台算法或投放系统开发。 |
| FCT-14 | 参与店铺评分、流量/营销/交易数据和大促策略分析 | DER-001:168-179 | FACT_DOCUMENTED | 只写参与和分析，不补充未给出的增长数字。 |
| FCT-15 | 以 KOC 为主做达人分层和 BD，累计达人合作销售额 10 万+，形成筛选/触达/合作推进 SOP | DER-001:180-200 | FACT_DOCUMENTED | 不能写成全量 KOL 资源或更高销售额。 |
| FCT-16 | 在浙江朗臻任京东电商运营→宠物项目管理，2022.03–2024.07，连续时间 | DER-001:201-204 | FACT_DOCUMENTED | 不写“返岗”。 |
| FCT-17 | 正大小仟牙膏单品类 2022 年 GMV 约 300 万+，2023 618 GMV 约 50 万 | DER-001:205-220 | FACT_DOCUMENTED | 单品类结果，不是品牌总盘。 |
| FCT-18 | 负责搜索热词/长尾词、标题和详情页属性优化，核心商品搜索排名由百名外到类目前 10 | DER-001:221-230 | FACT_DOCUMENTED | 可写搜索优化结果；不写算法研发。 |
| FCT-19 | 核心单 SKU 日 GMV 约 1,000+→15,000+，约 15 天完成 | DER-001:231-236 | FACT_DOCUMENTED | 是日销售额/GMV，不是订单量。 |
| FCT-20 | 使用实时经营数据、京东快车/京准通，协同活动、供应链库存、品牌方和京东小二 | DER-001:237-279 | FACT_DOCUMENTED | 使用“参与/协同”；不补充权限或独立预算权。 |
| FCT-21 | 胖小虎约 5 个跨平台店铺，年度整体 GMV 约 1,200 万–2,000 万，日均约 4–5 万，双十一月约 200 万 | DER-001:280-311 | FACT_DOCUMENTED | 业务规模与本人直接责任分开写。 |
| FCT-22 | 对胖小虎 GMV、利润率、DSR、月/季目标和渠道结果直接负责，老板做最终经营审查 | DER-001:280-292 | FACT_DOCUMENTED | 保留责任边界；不写最终经营决策权。 |
| FCT-23 | 参与预算分配、生命周期项目推进，并协同约 5 人小红书团队和约 5 人客服团队 | DER-001:312-382 | FACT_DOCUMENTED | 是协同人数，不写行政管理。 |
| FCT-24 | 引用 `wanghanyu654321-cell/-agent` 的 `job-ready/integration-v1` 项目，定位为企业客服 Agent Proof App | DER-001:383-397 | DOCUMENTED_ONLY | 当前工作区无对应 checkout，未完成 repo-to-resume 核验。 |
| FCT-25 | 事实源描述 Node.js/FastAPI/PostgreSQL 16/pgvector/React/Docker Compose/Nginx/Pi Runtime 架构与权限边界 | DER-001:398-422 | DOCUMENTED_ONLY | 只能写“项目材料描述/设计与验收负责”；不能据此宣称生产部署。 |
| FCT-26 | 事实源描述 Runtime 预算、工具、词法检索、Evidence Governance 和 Routing 规则 | DER-001:423-494 | DOCUMENTED_ONLY | Hybrid/RRF/Reranker/正式 Query Rewrite/Model Routing 明确未完成。 |
| FCT-27 | 事实源给出 40 Frozen Cases、Safety 30/30、Robustness 100/100、Holdout 60/60、Governed Knowledge 46/46、Public Top1 96%、Recall@3 100%、Routed Outcome 100% | DER-001:495-516 | DOCUMENTED_ONLY | 仅现有测试集结果；不是生产流量结果；需 repo/测试证据后再提升状态。 |
| FCT-28 | 在 Agent 项目中本人负责问题定义、架构边界、验收标准、评测设计、Badcase 归因、方案取舍、测试验收和项目状态判断，并通过 AI Coding Agent 协作完成实现 | DER-001:518-540 | FACT_DOCUMENTED | 对外写 AI Coding Agent 协作完成实现；不写独立手写全部代码。 |
| FCT-29 | 水果生鲜创业项目与悦客 AI Coach 项目当前不进入正式主简历 | DER-001:541-544 | EXCLUDE | 保留为背景事实，除非用户明确解冻。 |
| FCT-30 | 用户确认的不可变时间轴：开始工作 2022.03、毕业 2022.06；朗臻 2022.03–2024.07、今宜 2024.11–2025.07、人瑞 2025.09–2026.06；空档为 2024.08–2024.10 与 2025.08 | DER-001:30-33,35-36,95-96,201-202 | FACT_DOCUMENTED | 日期、先后关系和空档必须原样继承；2022.03–2022.06 的工作关系是用户确认事实，不推断工作性质。 |

## Evidence status vocabulary

- `FACT_DOCUMENTED`：该 frozen epoch 的事实母版明确写出，可按边界表达。
- `DOCUMENTED_ONLY`：该 frozen epoch 的事实母版有描述，但当前没有对应仓库/测试原始证据；不能写成已核验实现或生产结果。
- `EXCLUDE`：该 frozen epoch 的母版明确要求暂不公开或暂不使用。

## Rebase behavior

下一轮 Source Rebase 不默认全量改写本表。应先比较新旧 FCT-001 的 semantic delta：

- 未变化 Claim：继承并更新 `derived_from_source_epoch`；
- 变化 Claim：重新抽取、重新核验 locator / boundary；
- 新增事实：创建新 Claim；
- 删除/撤回事实：标记 superseded / excluded，并追踪受影响 Resume artifact；
- 任何受影响的 Resume text 必须重新 Semantic Claim Check。
