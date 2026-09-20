# Resume Review & Acceptance Policy

本文件是本仓库所有后续 AI / Agent / 人工审查的强制验收规则。

目标：防止“目录结构正确、文件命名正确、事实治理做得好”被误判为“简历成品已经完成”。任何审查都必须先验证实际交付物，再评价内容质量。

## 1. Repository First

当用户要求审查当前简历进度、质量或可投递性时，必须以指定 repository + branch + commit 的实际文件为第一证据源。

禁止仅根据历史聊天、模型记忆、设计方案、文件名、目录名、Status/Audit 自述或生成过程直接判断完成。

当前状态入口：

- `resume-workspace/CURRENT_VERSION_INDEX.md`
- `resume-workspace/GATE_REGISTRY.json`

这两个文件负责**已晋升 canonical state**；各版本 Manifest / Audit 负责说明对应 working candidate artifact 的来源与状态。历史 Audit 不得覆盖 current-state registry；同样，未晋升的 working candidate 也不得被误写成 canonical。

当审查发生在未晋升 working branch（例如 `resume/v5-final-polish`）时，必须同时回答两个问题：
- canonical registry 当前指向什么；
- 当前 branch 上是否存在更新但尚未 promotion 的 candidate。

禁止把“candidate 更新”误判为“canonical 已更新”，也禁止因为 canonical registry 较旧，就把经过当前 Fact / Claim 治理的 candidate 自动降级为旧历史状态。

## 2. Mandatory Review Order

正式评价按以下顺序：

1. 锁定 repository / branch / commit；
2. 读取 `CURRENT_VERSION_INDEX.md` 和 `GATE_REGISTRY.json`；
3. 枚举本次需要评价的实际 Resume artifact；
4. 完整读取实际 Resume 正文；
5. 读取对应 Claim Map / Audit / Policy；
6. 先判断 Source Currency、Fact/Claim、Timeline、Career History、Career Substance 等基础门禁；
7. 再评价 Recruiter Quality；
8. 最后才评价 Single-JD、ATS、Render、Application Ready。

## 3. Fact Safety ≠ Resume Quality

Fact Safety 是硬约束，不是成品质量的替代指标。

以下内容即使通过，也不能单独证明简历成熟：

- Claim Ledger 完整；
- Timeline Gate 通过；
- Claim Map 完整；
- JD Matrix 正确；
- Skill 调度正确；
- 文件/目录齐全。

必须独立评价：

- Source / Fact Currency；
- Claim Mapping Integrity；
- Career History；
- Career Substance；
- Recruiter Quality；
- Single-JD / ATS / Render / Application Readiness。

## 4. Source Epoch and Currency

每个事实冻结版本应拥有 source epoch，但**本 Policy 不再硬编码某一个 epoch 为永久“当前值”**，避免 Policy 自身因后续事实更新而变成新的漂移源。

读取顺序：

1. canonical source epoch / gate state：读取 `CURRENT_VERSION_INDEX.md` 与 `GATE_REGISTRY.json`；
2. working candidate source epoch：读取当前 branch 的 `FACT_MASTER_CURRENT.md`、对应 Manifest / Audit；
3. 如果 candidate 比 canonical 更新但尚未 promotion，状态应表达为 **NEWER_UNPROMOTED_CANDIDATE**，而不是自动写成 `STALE_PENDING_REBASE`；
4. 只有出现未同步的事实变化、Claim Ledger 未重建、或 candidate artifact 未重新 Claim Check 时，才判定真正的 source drift / pending rebase。

因此必须区分：

- **Canonical Currency**：当前正式晋升状态；
- **Candidate Currency**：当前 working branch 的事实 / Claim / artifact 是否自洽；
- **Promotion State**：candidate 是否已经正式晋升。

三者不得合并成一个模糊的“current / stale”标签。

## 5. Gate Vocabulary and Dependency

统一状态：

- `PASS`
- `PARTIAL`
- `FAIL`
- `BLOCKED`
- `NOT_RUN`

`PASS` 必须带完整 Gate 名称。

尤其区分：

- `CLAIM_MAPPING_INTEGRITY_GATE`：Resume 是否映射到当前仓库 Claim Ledger；
- `FACT_CURRENCY_GATE`：该 Claim Ledger 是否来自最新有效 FCT source epoch。

前者可以 PASS，而后者因 Source Drift BLOCKED；禁止再用模糊的单一 `Claim Gate PASS` 掩盖上游失配。

## 6. Role Baseline Resume Gate

Role Baseline 是真实 Single-JD Tailoring 的稳定母稿，不是岗位选材摘要，也不是公司级最终简历。

默认包含：

- Header（私有字段可在公开仓库中使用明确 injection marker）；
- Target Role；
- Professional Summary；
- Core Competencies / Skills；
- Work Experience；
- Selected Project（可选，Role-dependent）；
- Education（私有字段可使用明确 injection marker）；
- 必要时 Tools / Additional Skills。

`Selected Project` 不再是所有 Role Baseline 的硬必选项。

## 7. Career History Gate

`FULL CAREER HISTORY = HARD INVARIANT`。

正式 Role Baseline 必须保留三段工作经历，并与 `CANONICAL_TIMELINE.md` 一致：

- 杭州人瑞网络科技有限公司｜评测专家｜服务淘天 Data Agent｜2025.09–2026.06；
- 杭州今宜商贸有限公司｜抖音项目代运营 / 项目运营 / BD｜2024.11–2025.07；
- 浙江朗臻网络科技有限公司｜京东电商运营 → 宠物项目管理｜2022.03–2024.07；
- Graduation: 2022.06；Career Start: 2022.03；
- 空档：2024.08–2024.10、2025.08。

不得把 2022.03–2022.06 改写成实习、兼职、校招或提前转正。

## 8. Career Substance Gate

三家公司都“出现”并不等于职业内容完整。

每段 Work Experience 必须：

- Role Scope Visible；
- 至少一个 Scale / Result / Ownership 强证据；
- Title–Substance Consistency 通过。

整份 Resume 必须：

- Career Progression Visible。

Career Substance Gate 不规定固定 bullet 数量。不得为了通过 Gate 机械扩写。

## 9. Project Selection Rule

`PROJECT_SELECTION = ROLE_DEPENDENT`。

项目可以根据 Role Family / Single-JD：

- 保留；
- 前置 / 后置；
- 压缩；
- 替换为其他已批准项目；
- 省略。

Project 永远不能替代三段正式 Work Experience。

Agent Project 已进入 repo verification 阶段，工程仓库可以作为 **engineering evidence source** 使用；但工程仓库与候选人事实源承担不同职责。

- 工程仓库可独立证明：Runtime / Authority / Governed Knowledge / Durable State / Eval Harness / Regression / CI / PostgreSQL / FastAPI / pgvector / Docker 等已经被仓库证据支持的工程能力及其失败 / 阻塞边界。
- 微信部署、实体门店 POC、开始实际使用等业务落地事实，只有在 FACT MASTER / CLAIM LEDGER 中已由用户确认时才能进入简历；不能因为工程仓库未独立记录商业场景，就擅自删除或降级这些已确认事实。
- 反过来，工程仓库写明“不声称 commercial customer deployment / Pilot acceptance / Production Ready”时，也不得把简历中的 POC / 实际使用升级成商业客户验收、持续付费、ROI、规模化或 Production SLA。

规则：**repo evidence 负责证明工程实现；FACT / CLAIM 负责治理候选人事实；两者可以互相校验，但不能互相越权。**

## 10. Evidence Priority

Claim Ledger 回答“能不能写”，Evidence Priority 回答“值不值得写”。

推荐使用离散等级：

- `A_CORE_RESULT`
- `B_STRONG_SCOPE`
- `C_SUPPORTING`
- `D_BACKGROUND`
- `X_EXCLUDE`

同时按目标 Role / JD 赋予 `HIGH / MEDIUM / LOW` relevance。禁止使用伪精确小数评分制造客观性幻觉。

## 11. Career Story Boundary

Career Story 用于解释能力连续性，不用于推断人生动机或转型因果。

允许表达经历之间的业务/能力语境连接；没有事实源支持时不得写“因为 X 所以转型 Y”“为了进入 AI 行业”等动机性叙事。

## 12. Editorial Rewrite and Mutation Rule

写作顺序：

`Select → Rank → Group → Rewrite → Semantic Claim Check → Compress`

任何 Resume 文本的语义修改都会使此前针对该文本的 Semantic Claim Check 失效；修改后必须重新核验。

Recruiter Review、Single-JD Tailoring 和 ATS 如果导致语义文本变化，同样必须重新过 Claim Check。

## 13. Recruiter Quality Gate

至少独立检查：

- Role Clarity；
- Career Completeness；
- Evidence Strength；
- Information Hierarchy；
- Narrative Continuity；
- Human Writing；
- Term Discipline；
- Interview Defensibility。

Recruiter Quality PASS 不得由 Fact Safety、ATS sanity 或目录完整性替代。

## 14. Audit Content Separation

Gates、禁用主张、repo 未核验、生产边界等内部信息应放在 `*.AUDIT.md` / Claim Map / Registry 中，不直接写进招聘方面向 Resume 正文。

## 15. Single-JD Resume Gate

没有真实、完整或足够完整的目标 JD 时，只生成 Role Baseline，不宣称公司级最终定制。

真实 JD 到来后的流程：

`JD Freeze → JD × Evidence Matrix → Tailoring → Semantic Claim Check → JD/Recruiter Review → Content Freeze → ATS Audit → Semantic Re-check if modified → Final Artifact Fact Parity → Render`

JD 关键词不能产生候选人事实。

## 16. ATS and Render

ATS 与 Render 只能在内容基本冻结后进行。

最终事实门禁应理解为 `FINAL_ARTIFACT_FACT_PARITY_GATE`：确认最终将被渲染/投递的文本与最后批准的事实/Claim 状态一致。

若 ATS 建议导致任何语义文本修改，必须先重新 Semantic Claim Check，再运行 Final Artifact Fact Parity Gate。

## 17. Private Field Injection

公开仓库缺少姓名、手机号、邮箱、学校等私有字段，不等于 Resume Content Gate 自动失败。

必须区分：

- `BASELINE_CONTENT_READY`
- `PRIVATE_FIELD_INJECTION`
- `APPLICATION_PACKAGE_READY`

公开仓库允许使用 `[LOCAL_ONLY_CONTACT]`、`[LOCAL_ONLY_EDUCATION]` 等明确 marker；最终投递前必须注入真实私有字段并重新完成 Final Artifact Fact Parity / Render。

## 18. Review Conclusion Format

推荐：

```text
DELIVERABLE STATUS
R1 / R2 / R3: PARTIAL / COMPLETE / NOT_COMPLETE

SOURCE CURRENCY: PASS / BLOCKED / FAIL
CLAIM MAPPING INTEGRITY: PASS / PARTIAL / FAIL
TIMELINE GATE: PASS / FAIL
CAREER HISTORY GATE: PASS / FAIL
CAREER SUBSTANCE GATE: PASS / PARTIAL / FAIL
RECRUITER QUALITY GATE: PASS / PARTIAL / FAIL
SINGLE-JD GATE: PASS / NOT_RUN / FAIL
ATS GATE: PASS / NOT_RUN / FAIL
RENDER GATE: PASS / NOT_RUN / FAIL
APPLICATION READY: YES / NO
```

## 19. Highest-Level Principle

**事实安全只是底线；招聘方能快速理解并相信候选人的职业价值，才是简历成品。**

**完整职业史是硬约束；项目不是。**

**状态必须有唯一真相源；历史 Audit 不能覆盖当前 Registry。**

**任何文本 mutation 后，语义核验必须重新计算。**

Required invariant marker: `DIFFERENT EMPHASIS · SAME FACTS · SAME TIMELINE · FULL CAREER HISTORY`。
