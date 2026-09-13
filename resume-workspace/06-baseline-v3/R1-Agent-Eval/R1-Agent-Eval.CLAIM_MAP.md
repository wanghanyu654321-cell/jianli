# R1 Agent Eval Baseline V3 Claim Map

本映射从 V3 文案重新建立；V2 Claim Map 不作为替代来源。状态只使用 `FULLY_GROUNDED` 或 `PARTIALLY_GROUNDED`。

| bullet_id | resume location | claim_id | evidence locator | semantic status | grounding note |
|---|---|---|---|---|---|
| V3-S01 | Summary sentence 1 | FCT-02,FCT-03 | DER-001:35-50 | FULLY_GROUNDED | 当前 Title、服务场景和评测范围均来自事实源。 |
| V3-S02 | Summary sentence 2 | FCT-04,FCT-05 | DER-001:51-62 | FULLY_GROUNDED | 团队规模、任务量、一致性变化和文档沉淀保留原限定词。 |
| V3-S03 | Summary sentence 3 | FCT-13,FCT-18 | DER-001:141-167,221-230 | FULLY_GROUNDED | 京东搜索、商品属性、排名优化和 CTR/CVR/ROI 复盘均有事实定位。 |
| V3-C01 | Core competencies / 评测与质量 | FCT-03,FCT-08 | DER-001:39-50,74-84 | FULLY_GROUNDED | Query、召回、相关性、QA、Badcase 与争议裁定来自当前工作事实。 |
| V3-C02 | Core competencies / 标准与治理 | FCT-03,FCT-05 | DER-001:39-50,58-62 | FULLY_GROUNDED | SOP、规则统一、抽检、培训答疑和质量复核有事实支持。 |
| V3-C03 | Core competencies / 数据与业务 | FCT-06,FCT-12,FCT-13,FCT-14 | DER-001:63-71,116-179 | FULLY_GROUNDED | 指标观察、CTR/CVR/ROI、复盘和协作均保留边界。 |
| V3-W01 | 人瑞 bullet 1 | FCT-02,FCT-03 | DER-001:35-50 | FULLY_GROUNDED | Data Agent、Query、召回、商品相关性和标准拆解均有定位。 |
| V3-W02 | 人瑞 bullet 2 | FCT-03 | DER-001:46-50 | FULLY_GROUNDED | Badcase 分类归因和争议提交没有升级为独立裁决权。 |
| V3-W03 | 人瑞 bullet 3 | FCT-04 | DER-001:51-57 | FULLY_GROUNDED | 团队、周任务、个人日处理量和抽检比例原样保留。 |
| V3-W04 | 人瑞 bullet 4 | FCT-03,FCT-05 | DER-001:39-50,58-62 | FULLY_GROUNDED | 一致性结果与 SOP、培训、答疑、规则统一和复核聚类在同一质量治理模块。 |
| V3-W05 | 人瑞 bullet 5 | FCT-06 | DER-001:63-71 | FULLY_GROUNDED | 指标观察写为参与和汇总，没有扩写完整线上权限。 |
| V3-W06 | 今宜 bullet 1 | FCT-12,FCT-13,FCT-14 | DER-001:116-179 | FULLY_GROUNDED | CTR/CVR/ROI、复盘、投流和协作边界清晰。 |
| V3-W07 | 今宜 bullet 2 | FCT-15 | DER-001:180-200 | FULLY_GROUNDED | KOC 分层、合作 SOP 和 10 万+ 销售额来自同一 Claim。 |
| V3-W08 | 朗臻 bullet 1 | FCT-18 | DER-001:221-230 | FULLY_GROUNDED | 仅保留搜索意图、关键词、商品属性和排名证据。 |
| V3-W09 | 朗臻 bullet 2 | FCT-19,FCT-20 | DER-001:231-279 | FULLY_GROUNDED | GMV 数字写明为核心单 SKU 日 GMV，并保留约 15 天口径。 |
| V3-P01 | Agent project bullet 1 | FCT-24,FCT-28 | DER-001:383-397,518-540 | PARTIALLY_GROUNDED | 项目责任来自事实源，但项目仍为 DOCUMENTED_ONLY，未宣称生产交付。 |
| V3-P02 | Agent project bullet 2 | FCT-25,FCT-26 | DER-001:398-494 | PARTIALLY_GROUNDED | 技术词只用于说明测试场景；未升级为已核验系统能力。 |
| V3-P03 | Agent project bullet 3 | FCT-27,FCT-28 | DER-001:495-540 | PARTIALLY_GROUNDED | 测试集结果保留“现有测试集/记录”语境，不写生产流量结果。 |
| V3-E01 | Education marker / graduation month | FCT-30 | DER-001:30-33 | FULLY_GROUNDED | 公开毕业月份 `2022.06`；学校和其他教育字段仍由私有字段注入。 |
| V3-T01 | Timeline / 人瑞 | FCT-02,FCT-30 | DER-001:35-36 | FULLY_GROUNDED | `2025.09–2026.06` 与 canonical timeline 一致。 |
| V3-T02 | Timeline / 今宜 | FCT-09,FCT-30 | DER-001:95-96 | FULLY_GROUNDED | `2024.11–2025.07` 与 canonical timeline 一致。 |
| V3-T03 | Timeline / 朗臻 | FCT-16,FCT-30 | DER-001:201-202 | FULLY_GROUNDED | `2022.03–2024.07` 与 canonical timeline 一致。 |
| V3-T04 | Timeline / graduation | FCT-30 | DER-001:30-33 | FULLY_GROUNDED | 毕业 `2022.06` 与工作起点 `2022.03` 的用户确认关系保留。 |

## Semantic grounding audit

| resume surface | semantic status | review note |
|---|---|---|
| Professional Summary | FULLY_GROUNDED | 三句话分别绑定当前评测工作、规模/结果和京东搜索事实。 |
| Core Competencies | FULLY_GROUNDED | 三组能力均来自 FCT，未从 JD 添加关键词。 |
| Renrui work experience | FULLY_GROUNDED | 五条 bullet 各自有 FCT 映射，数字与限定词完整。 |
| Jinyi work experience | FULLY_GROUNDED | 两条 bullet 只保留对 Agent Eval 有帮助的数据、复盘、SOP 和 KOC 证据。 |
| Langzhen work experience | FULLY_GROUNDED | 两条 bullet 只保留搜索、Query 语境和数据优化结果。 |
| Agent project | PARTIALLY_GROUNDED | 三条 bullet 有事实映射，但项目证据仍为 DOCUMENTED_ONLY。 |
| Education marker | FULLY_GROUNDED | 保留毕业月份 `2022.06`，不对外暴露学校或其他教育字段。 |

结论：V3 每个独立主张均已绑定当前 Claim；对 Agent 项目保留 PARTIALLY_GROUNDED 与 DOCUMENTED_ONLY 边界，没有无依据的升级表达。
