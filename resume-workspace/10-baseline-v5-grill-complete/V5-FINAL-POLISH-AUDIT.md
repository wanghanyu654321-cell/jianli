# V5 Final Polish Integrity Audit

Branch: `resume/v5-final-polish`  
Base: `resume/v5-grill-complete`

## Audit Goal

验证本轮“中国市场语言统一 + 简历化表达 + 用户新确认评测事实补充”没有通过压缩或改写破坏 V5 原有事实、数字和角色结构。

当前事实源：
- `derived_from_source_epoch`: `FCT-EPOCH-20260920-FD7E6D3E`
- FACT blob: `fd7e6d3e311f442eeab20a901dfa57b59bca3e9f`

## Structural Check

| Role | Lines | Bullets | 原 V5 数字 / 日期 Token |
|---|---:|---:|---|
| R1 | 80 → 66 | 26 → 20 | 只压缩 recruiter-facing 展开；Fact/Claim 中原事实与工程证据均保留 |
| R2 | 82 → 82 | 28 → 28 | 无缺失 / 无新增 |
| R3 | 75 → 75 | 25 → 25 | 无缺失 / 无新增 |
| R4 | 81 → 81 | 27 → 27 | 无缺失 / 无新增 |
| R5 | 79 → 79 | 25 → 25 | 无缺失 / 无新增 |
| R6 | 81 → 81 | 27 → 27 | 无缺失 / 无新增 |

R1 本轮进一步做 10 秒审计减法：人瑞由 9 条收敛为 7 条，今宜 5→3；朗臻最终保留 4 条高价值证据，分别覆盖搜索 Query 理解、项目经营管理、跨团队推进、经营问题诊断。删除的是重复/低价值 recruiter-facing 展开，不删除 FACT / CLAIM。项目仍保留 7 条高价值 Eval 证据。

当前新增 / 强化的 Eval 证据：
- 30-case Safety / 100-case Robustness / 60-case Blind Holdout；
- S1 Thin Evaluation Harness / Run Integrity；
- Action Acceptance / Durable State；
- Quality Gate / Version Decision；
- 保留开放题高低分答案、Layer / Path 与结构化 Trace / 轨迹评测。

其中开放题 / Trace 来自用户确认事实；Harness / Holdout / Durable Acceptance / Quality Gate 来自 `-agent` 当前 main 的 repo verification，不是从 JD 或第三方 Skill 推导。

## Fact Governance Delta

本轮已按顺序更新：
1. `FACT_MASTER_CURRENT.md`：保留 FCTM-RR-24~27，并新增 / 更新 FCTM-AG-00、FCTM-AG-04、FCTM-AG-10~12；
2. `CLAIM_LEDGER.md`：更新 FCT-24 / FCT-27，新增 FCT-65~67；随后按用户确认将今宜职位统一为“抖音项目代运营”，并绑定 `FCT-EPOCH-20260920-FD7E6D3E`；
3. R1：正式工作与个人项目证据分层展示；Action Acceptance → Tool Use，Trajectory Eval → 执行轨迹分析，Eval Dataset → 评测集设计，Negative Cases → 边界测试，Eval Harness / CI → 自动化回归 / CI；项目标题保持实际场景并增加“个人 Agent 项目”来源属性；
4. ONLINE-MAIN：个人优势压为两段并前置三类最高价值证据；核心能力明确拆分“正式 AI 评测 / 质量治理”与“个人 Agent 项目 / 评测工程”，避免 CI / Quality Gate 来源混淆；
5. Langfuse 保持边界：当前只确认方法用途，**未写成已实际接入 / 已搭建平台**。

## Language / Reading-Cost Check

额外一致性修复：
- 人瑞正式职位恢复为 `评测专家（淘天 Data Agent）`，ONLINE 与 R1–R6 全部同步；
- R1 删除 `Search / Query Intent`，统一为 `Query 理解 / 相关性`；
- 每周 5,000–10,000 条任务量从 R1 / ONLINE recruiter-facing 展示移除，仍保留在 FACT / CLAIM。


统一执行：
- 中文 JD 常用词优先；
- FDE、AI 评测保持第一视觉；
- POC / RAG / Agent / API 等通用关键词保留；
- Bullet 标题只承担 JD 命中与 HR 扫描，不承担完整 reasoning；
- R1 项目 bullet 已收敛为评测集设计、边界测试、Bad Case / 根因归因、版本回归 / Holdout、Tool Use、执行轨迹分析、自动化回归 / CI；
- “XX 与 XX”类标题优先改为单一主概念；只有两个词均为独立 JD 关键词时保留 `/`；
- 电商搜索在 ONLINE-MAIN 用“搜索增长 / SEO”，在 R1 用“搜索 Query 理解”，按岗位语言表达同一事实；
- “真实”仅在第一次需要区分 Demo / 模拟环境时使用，后续改为门店流程、Case、反馈、状态等具体业务词；
- 事实边界尽量压缩为“已验证 X；Y 待验证”，不写成长篇防御句。

## Guardrail Check

继续保持：
- 微信部署 ≠ 企业微信 / 全渠道部署；
- 门店 POC / 开始实际使用 ≠ 长期客户成功 / 付费 / ROI / 规模化；
- 团队结果与个人贡献分开；
- 正式 PRD 未完成时不写成已完成；
- R5 不升级为纯 SWE / 生产级工程履历；
- R6 不升级为企业采购 / 销售成交履历；
- 结构化 Trace 中的“规划 / 决策节点”不表述为模型私有思维链；
- 未确认实际接入 Langfuse 前，不写“使用 Langfuse 搭建评测平台”。

## Unchanged Governance Assets

未修改：
- `CURRENT_VERSION_INDEX.md`；
- 冻结 V4；
- 历史 V5 / V6；
- 工作时间；
- 正式职位显示口径除今宜外保持不变；今宜已按用户最新确认统一为“抖音项目代运营”，BD 继续作为职责证据保留；
- 原有 GMV / 任务规模 / 一致性 / POC 数字事实。

## Semantic Claim Re-check

本轮 R1 / ONLINE-MAIN 语义变更已逐项回指当前 Claim Ledger：
- Open-ended / Path Eval → FCT-61；
- Trace / Trajectory Eval → FCT-62 / FCT-63；
- 分层 Eval / 100-case Robustness / 60-case Blind Holdout → FCT-27；
- Eval Harness / CI → FCT-65；
- Tool Use / 动作验收 → FCT-66；
- Quality Gate / Version Decision → FCT-67；
- 今宜职位统一显示与 BD 职责边界 → FCT-09；
- 微信部署 / 门店 POC / 使用反馈 → FCT-58 / FCT-60。

未增加未经事实 / repo 证据支持的新 ownership、生产、商业或 Langfuse 落地主张。

## New / Updated Derived Assets

- `CHINA-JD-TERMINOLOGY.md`
- `ONLINE-MAIN/ONLINE-MAIN.RESUME.md`
- `R1-Agent-Eval/R1-Agent-Eval.RESUME.md`
- `V5-FINAL-POLISH-MANIFEST.md`
- `V5-FINAL-FULLTEXT.md`

ONLINE-MAIN 仍是派生在线主简历，不替代 R1–R6。


## R1 Core Evidence Preservation

本轮用户明确要求以下五类核心价值在后续 R1 优化中不得因“10 秒压缩”被误删：
1. 正式 AI / Agent 评测能力；
2. 沟通与规则转译能力；
3. 跨团队协调与项目推进能力；
4. 从执行到项目管理的责任升级；
5. 两段 0→1 有结果经历。

朗臻必须保留成长路径：牙膏品类电商运营 → 宠物项目运营管理 → 约 5 个跨平台店铺 → 业务年度整体 GMV 约 1,200 万–2,000 万，并保留优先级、排期、阶段检查、跨团队协调和项目汇报证据。

“学习能力 / 适应能力”不直接写成空泛自评，而通过跨品类、跨渠道、跨岗位责任升级和可验证结果体现。


## New-Media Evidence Preservation

用户明确要求朗臻宠物项目中的新媒体能力不得因 R1 压缩被删除：
- 负责小红书策略与运营管理；
- 协同约 5 人团队；
- 通过选题 / 内容测试寻找有效或爆文方向；
- 对有效主题和内容结构做复刻、数据验证与迭代；
- 用于证明新媒体运营、流程设计、团队协同与内容方法能力。

今宜“产品定位” recruiter-facing 表述已改为“内容策略 / 卖点验证”，聚焦目标用户、核心卖点、短视频 / 直播验证和有效表达迁移，不再写过细的品类定位描述。
