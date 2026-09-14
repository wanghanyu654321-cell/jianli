# Role Baseline Writing Module

状态：ACTIVE。适用于 R1、R2、R3 及后续岗位族基线简历。

## 1. Core invariants

`ROLE FOCUS ≠ EXPERIENCE DELETION`。

`FULL CAREER HISTORY = HARD INVARIANT`。

`PROJECT_SELECTION = ROLE_DEPENDENT`。

岗位方向可以改变 Summary、Bullet 强调、每段经历的篇幅、项目选择与顺序、Skills 强调；岗位方向不得改变公司名称、岗位路径、起止月份、标准倒序或事实边界。

所有正式 Role Baseline 必须保留 Work Experience 的三段正式经历：人瑞 → 今宜 → 朗臻。Project 不属于职业时间轴不变量，不得用 Project 替代 Work Experience。

默认结构：Header → Target Role → Professional Summary → Core Competencies → Work Experience（人瑞 → 今宜 → 朗臻）→ Selected Project（可选）→ Education → optional Tools / Additional Skills。

## 2. Career History Gate

必须同时满足：

- 三家公司全部存在；
- 公司名称、岗位路径和日期与 `CANONICAL_TIMELINE.md` 一致；
- 标准倒序为人瑞 → 今宜 → 朗臻；
- 时间空档不被填补、隐藏或重新解释；
- 工作早于毕业的事实关系原样保留，不推断工作性质。

任何违反均使 `CAREER_HISTORY_GATE = FAIL`，并触发 `TIMELINE_GATE = FAIL`（若涉及时间轴字段）。

## 3. Career Substance Gate

完整职业史不等于完整职业内容。

每段正式 Work Experience 必须：

- `ROLE_SCOPE_VISIBLE = YES`：招聘方能看懂这一阶段实际负责什么；
- 至少有一个 `SCALE / RESULT / OWNERSHIP` 强证据，而不是只剩背景性职责；
- `TITLE_SUBSTANCE_CONSISTENCY = PASS`：正文能够解释岗位路径，不得出现 Title 写着项目管理但正文完全没有项目管理内容等失配。

整份 Resume 还必须满足：

- `CAREER_PROGRESSION_VISIBLE = YES`：招聘方能理解责任、问题复杂度或业务/质量能力如何随职业经历演进。

Career Substance Gate 不设置固定 Bullet 配额。条数只是编辑结果，不能反向驱动内容凑数。

## 4. Evidence Selection and Priority

Claim Ledger 只回答“能不能写”；Role Baseline 还必须回答“值不值得写”。

证据优先级使用离散等级，避免伪精确打分：

- `A_CORE_RESULT`：核心结果 / 强量化 / 强区分度证据；
- `B_STRONG_SCOPE`：强职责、规模、Ownership 或复杂协作证据；
- `C_SUPPORTING`：支撑目标岗位理解的能力或场景证据；
- `D_BACKGROUND`：事实成立，但当前岗位价值低；
- `X_EXCLUDE`：禁止或当前不使用。

另行判断目标岗位相关性：`HIGH / MEDIUM / LOW`。相关性会随 Role Family / Single-JD 改变，事实等级本身不得被 JD 反向修改。

## 5. Career Story Map Boundary

Career Story Map 用于解释不同经历之间的能力连续性，不用于创造职业选择因果。

允许：

- “早期搜索与商品运营经验为后续理解 Query、商品相关性提供业务语境。”

禁止在没有事实支持时写成：

- “因为做过搜索，所以转型进入 Agent Eval。”
- “为了进入 AI 行业主动转岗”等未经事实源确认的人生动机。

## 6. R1 Agent Eval focus

职业主线建议：

`E-commerce Search / Business Context → Data Review / SOP / Collaboration → Data Agent Eval / Query / Recall / Relevance → QA / Badcase / Quality Governance → Agent Eval Practice`

- 人瑞为主经历：突出 Data Agent、Query、Recall、Relevance、QA、Badcase、争议、SOP、任务规模、一致性和指标观察；
- 今宜必须保留真实项目 Scope，并优先选择能证明业务结果、数据复盘、SOP 和跨角色协作的强证据；不得压缩成纯背景脚注；
- 朗臻必须同时让“京东电商运营 → 宠物项目管理”的岗位路径在正文中可见；搜索/商品证据与跨店经营/项目责任可按篇幅排序；
- Agent 项目通常高相关，但仍属于 `ROLE_DEPENDENT` 选择，不得因为 Policy 强制占据固定篇幅。

## 7. R2 Business FDE focus

目标不是堆叠 `Solution Boundary / Acceptance Criteria / Runtime / Authority` 等内部 taxonomy，而是让招聘方看到：

`Business Problem → Requirement Breakdown → Coordination → Solution / Responsibility Boundary → Validation / Acceptance → Badcase / Feedback`

技术术语只有在能解释真实工作、项目边界或验收行为时才保留。

## 8. R3 AI Commerce focus

优先展示电商经营、搜索、GMV / 利润率 / DSR、CTR / CVR / ROI、渠道、内容、达人和 Data Agent 电商质量证据。

Agent Project 是否保留、压缩或省略取决于岗位族和真实 JD 的信息价值，不得为了模板统一强制保留。

## 9. Role-family emphasis guidance

以下比例仅用于方向判断，不是机械配额：

| role family | Renrui | Jinyi | Langzhen | Project |
|---|---:|---:|---:|---:|
| R1 Agent Eval | high | medium | medium | medium-high, role-dependent |
| R2 Business FDE | medium | medium-high | medium-high | high, role-dependent |
| R3 AI Commerce | medium | high | high | low-medium, role-dependent |

禁止根据比例推导“某段只能写两条”等固定规则。

## 10. Editorial rewrite order

固定顺序：

`Select → Rank → Group → Rewrite → Semantic Claim Check → Compress`

不要把“扩写”作为默认目标。先让每段工作成立，再做全局篇幅优化。

任何语义文本修改后，之前针对该文本的 Semantic Claim Check 自动失效，必须重新核验。

## 11. Prohibited changes

禁止：

- 删除任意一段正式工作经历；
- 把旧经历压成“其他经历”；
- 用项目替代正式工作经历；
- 为匹配岗位修改公司、岗位路径、日期、时间顺序、责任边界或数字口径；
- 把 JD 关键词、Skill 模板或 Career Story 推断写成候选人事实；
- 为满足篇幅/权重规则机械补 Bullet；
- 为显得专业而堆叠 taxonomy、技术词或未经证据支持的 AI 表达。

允许：

- Project 根据 Role / Single-JD 价值保留、前置、后置、压缩、替换为其他已批准项目或省略。

## 12. Acceptance criteria

岗位族简历必须同时满足：

- 目标岗位在 15–20 秒内可识别；
- `CAREER_HISTORY_GATE = PASS`；
- `CAREER_SUBSTANCE_GATE = PASS`；
- 最强证据优先，而不是所有事实平铺；
- 职业连续性可理解但不制造因果；
- Project 选择服务于岗位价值；
- 候选人实际做过的事情不被改写。

原则：`DIFFERENT EMPHASIS · SAME FACTS · SAME TIMELINE · FULL CAREER HISTORY`。
