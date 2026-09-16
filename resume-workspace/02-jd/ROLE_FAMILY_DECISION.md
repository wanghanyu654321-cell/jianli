# Role Family Baseline Decision

依据 `JD-001` 的七个岗位族、`REQUIREMENT_EVIDENCE_MATRIX.md` 和 `INS-002` 的三层 Resume 规则，当前只生成岗位族基线，不生成公司级投递版。

当前证据判断已重基于：`FCT-EPOCH-20260916-04094915`。

| role family | market status in JD MASTER | evidence posture | decision |
|---|---|---|---|
| R1 Agent Eval / LLM Quality | Core | 直接评测证据最强；新增评测类目、Badcase 分类、修改后复测、多轮/Tool/Step/信息完整性评测、基础 SQL/查询取数；Agent Eval 资产已有部分 repo 核验 | 生成基线；主投方向 |
| R2 Business FDE / AI Delivery | Core | 电商项目管理、需求/优先级/排期/阶段检查、方案汇报、评测治理和 Agent 方案边界形成交叉；仍缺真实 AI 客户交付 | 生成基线；强调业务型 FDE |
| R3 AI Commerce | Core | GMV、搜索、投放、内容、BD、供应链、跨渠道经营证据强；Data Agent / SQL / Query-Relevance 提供 AI/Data 支撑 | 生成基线；核心方向 |
| R4 AI Product Ops / Intelligent Service | Core | 评测质量、执行者 Context、Badcase、反馈→修改→再验证、版本指标与场景流程证据增强；仍无正式产品 Roadmap/上线 Owner | 生成基线；优先验证“AI 产品质量运营 / 场景运营”定位 |
| R5 Prompt / Agent Solution | Core | Agent Problem Definition / Boundary / Eval + Prompt/System/Tool Instruction iteration + Frozen Eval Asset；仍无真实客户 Prompt 交付/生产 Agent Owner | 生成基线；保守边界但直接证据已增强 |
| R6 MaaS / AI Solution / Pre-sales | Core supplementary | 有 B2B 商业沟通、运营方案汇报、项目排期、Agent 技术边界与业务结果素材；仍缺 AI 售前 Demo/POC/成交 | 生成补充基线；避免写成熟售前成交经验 |
| R7 Agent Application Engineer | Stretch | 项目仓库部分核验不改变本人工程责任边界；深工程栈和生产实现证据仍不足 | 不生成岗位族基线；只保留 Gap/学习清单 |

## Naming and use

- Master Resume：完整事实库，允许超过 2 页；真实母版仍是 `FCT-001`。
- Role Baseline Resume：R1–R6 岗位族内容基线，供单条 JD 定制使用。
- 当前 `07-baseline-v4` 写于上一事实 epoch，需要基于 `FCT-EPOCH-20260916-04094915` 做 Skills 优化与语义重验后才能作为当前岗位族基线。
- Single-JD Tailored Resume：只有冻结公司名、岗位名和完整/足够完整的真实在招 JD 后，才建立对应 application artifact 并做 Single-JD tailoring。
