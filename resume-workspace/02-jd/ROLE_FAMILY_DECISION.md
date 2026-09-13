# Role Family Baseline Decision

依据 `JD-001` 的七个岗位族、`REQUIREMENT_EVIDENCE_MATRIX.md` 和 `INS-002` 的三层 Resume 规则，当前只生成岗位族基线，不生成公司级投递版。

| role family | market status in JD MASTER | evidence posture | decision |
|---|---|---|---|
| R1 Agent Eval / LLM Quality | Core | 直接评测证据最强；项目证据需保持 `DOCUMENTED_ONLY` | 生成基线 |
| R2 Business FDE / AI Delivery | Core | 电商项目管理、评测治理和 Agent 方案边界形成交叉 | 生成基线 |
| R3 AI Commerce | Core | GMV、搜索、投放、SOP、跨渠道经营证据强 | 生成基线 |
| R4 AI Product Ops / Intelligent Service | Core | 评测质量、数据诊断、场景流程、客服协同可迁移 | 生成基线 |
| R5 Prompt / Agent Solution | Core | Agent 项目设计/验收 + SOP/业务场景证据 | 生成基线，保守措辞 |
| R6 MaaS / AI Solution / Pre-sales | Core supplementary | 有技术边界与业务结果素材，但缺售前成交的直接证据 | 生成补充基线 |
| R7 Agent Application Engineer | Stretch | 事实源无足够工程实现/生产证据，JD MASTER 明确为 Stretch | 不生成基线 |

## Naming and use

- Master Resume：完整事实库，允许超过 2 页；真实母版仍是 `FCT-001`。
- Role Baseline Resume：下列六个 Markdown 内容基线，目标约 2 页，供单条 JD 定制使用。
- Single-JD Tailored Resume：当前未生成。只有用户提供公司名、岗位名和完整/足够完整的真实 JD 后，才建立 `applications/<company-role>/` 并调用 `resume-tailoring`。
