# Core 100 Interview Questions

更新时间：2026-09-24

## 使用说明

这 100 题是从用户提供的真实面试题，以及对阿里系/阿里云 FDE、字节、腾讯、百度、美团、携程、PDD、小红书、快手、有赞、得物、去哪儿等真实面经的重复主题中抽取出的核心题。**单题的“来源”采用公司/岗位簇归纳，不伪造成某一家公司的逐字原题。**

状态口径：`P0`=当前经历/项目应直接防守；`P1`=JD 高频缺口，只能讲设计/取舍，未实现不得说“做过”。“已学/可答”不等于已通过压力面，最终以 `看懂 → 讲出 → 定位 → 小改 → 压力追问` 为完成标准。

## 事实边界

- 当前 `-agent` 有：Pi Runtime、Enterprise Authority、Durable Business、Governed RAG、FastAPI/pgvector、Harness/Eval、Durable Acceptance、AgentProfile、Public HTTPS、Live WeCom、bounded DeepSeek real-provider eval。
- 当前 **没有**：BM25+Vector Hybrid、RRF、Cross-Encoder reranker、真正 Multi-Agent、MCP、完整 Long-term Memory、完整 Context Compression、K8s、Production Data Flywheel、自主 Skill 在线进化。
- 任何网上示例百分比、固定评测集规模或“跑 5 次”等经验值都不能直接变成个人项目事实。

## 一、项目总览与业务价值（1–12）

来源标签：阿里/字节/PDD/小红书/有赞/美团等 Agent、AI 应用、AI 产品真实面经归纳

| # | 核心题 | 模块 | 当前状态 | 当前项目证据 / 边界 |
|---:|---|---|---|---|
| 1 | 用 2–3 分钟完整介绍 Customer Support Agent：业务问题、用户、架构、本人负责、当前做到什么程度？ | M1/M7 | P0·待压测 | `-agent: README.md, docs/job-ready/CURRENT_STATE.md` |
| 2 | 为什么这个场景需要 Agent，而不是普通 Workflow、规则系统或 Chatbot？ | M1/M8 | P0·可答 | 项目演进主线；当前仍是单 Agent |
| 3 | 这个 Agent 实际解决的业务问题是什么？原流程痛点在哪里？ | M1 | P0·待打磨 | Customer Support Agent 业务边界 |
| 4 | 从用户请求进入系统到最终回答/业务动作完成，完整链路是什么？ | M1/M2/M3 | P0·学习中 | `src/enterprise/http-api.ts → application.ts → src/index.ts` |
| 5 | 项目最困难的三个问题是什么？分别怎么解决？ | M1/M7 | P0·待压测 | Runtime/RAG/Durable business/Delivery 真实证据 |
| 6 | 这个项目与普通 Agent Demo 的本质区别是什么？ | M1 | P0·可答 | Enterprise boundary + Durable + Eval + Delivery |
| 7 | 项目中哪些部分是你真正能够独立解释、修改和排障的？ | M7 | P0·未完成 | Code Ownership Gate 尚未完成 |
| 8 | 哪个设计是你最满意的？为什么？ | M1/M7 | P0·待打磨 | 建议从 Authority / Harness / Durable Acceptance 中选真实可守项 |
| 9 | 如果重新做一次，你会删掉什么、重做什么？ | M7/M8 | P1·待准备 | 只能基于当前真实边界复盘 |
| 10 | 当前项目为什么采用单 Agent，而不是 Multi-Agent？ | M1/M8 | P1·可解释 | 当前项目没有真正 Multi-Agent |
| 11 | 怎样证明一个新增架构不是为了技术而技术的过度设计？ | M1/M5 | P0·待压测 | 以风险/失败模式/验收证据论证 |
| 12 | 当前 POC 离 Production Ready 还缺什么？ | M1/M6/M8 | P0·可答 | `docs/job-ready/CURRENT_STATE.md` 的明确 deferred/claim boundary |

## 二、Eval / Benchmark / Badcase（13–29）

来源标签：腾讯/字节/百度/携程/阿里系大模型与 Agent 评测面经 + 用户真实 Data Agent Eval 经历

| # | 核心题 | 模块 | 当前状态 | 当前项目证据 / 边界 |
|---:|---|---|---|---|
| 13 | 过去的 Data Agent 主要针对什么场景评测？评测目标是什么？ | M5 | P0·强项 | 真实工作：Data Agent Eval / 搜索链路 / 业务质量 |
| 14 | SOP 和评测标准怎样从业务目标拆出来？ | M5 | P0·强项 | 真实工作：SOP、评测标准、L1/L2/L3、Badcase |
| 15 | 黄金评测集怎么构建？ | M5 | P0·强项 | 真实工作 + 当前 Harness/Eval |
| 16 | 一个 Case 应包含哪些字段：Input、GT、Evidence、Expected Action、Rubric 分别是什么？ | M5 | P0·待工程化表达 | `harness/contracts.ts`, eval suites |
| 17 | 如何保证评测集覆盖主流程、边界场景和异常场景？ | M5 | P0·强项 | 业务分层 + holdout/robustness/safety |
| 18 | 为什么随机抽线上 Log 不能直接形成高质量评测集？ | M5 | P0·可答 | 分布偏斜、长尾/关键风险覆盖不足 |
| 19 | 海量线上 Log 如何转成有限但有代表性的离线评测集？ | M5 | P0·待压测 | 分层抽样 + 风险桶 + Badcase 回流 |
| 20 | 如果没有 GT，线上 Case 能不能直接评估？怎么做？ | M5 | P1·待准备 | LLM-as-Judge/规则/人工抽检；当前项目未完整做线上无 GT 评估 |
| 21 | AI 自动生成测试 Case 时，怎样保证引用的知识和事实正确？ | M5 | P0·待准备 | 文档约束 + source/evidence 校验 + 人工抽检 |
| 22 | 如何利用真实文档和历史案例生成测试 Case？ | M5 | P0·待准备 | 文档/案例分源组织，生成后做证据核验 |
| 23 | 什么情况适合规则自动判分，什么适合 LLM-as-a-Judge，什么必须人工审核？ | M5 | P0·强项 | 规则唯一真值 / 开放式 rubric / 边界裁决 |
| 24 | 黄金集里的 Badcase 为什么仍然可能需要人工裁决？ | M5 | P0·强项 | 业务歧义、标注冲突、边界规则、不可自动判定 |
| 25 | 人工 Badcase 归因如何制定一致的标签体系和 SOP？ | M5 | P0·强项 | 真实工作证据 |
| 26 | 如何判断问题来自模型、RAG、Tool、Prompt、业务规则还是数据本身？ | M5/M6 | P0·待压测 | Harness + request debugging + durable outcome |
| 27 | Badcase 怎么回流成 Regression Set？ | M5 | P0·强项 | 当前 repo 有 regression/eval 治理 |
| 28 | 修改模型、Prompt、Skill 或检索后，如何证明整体真的变好而不是只修好几题？ | M5 | P0·强项 | 固定集 + holdout + repeated run + regression |
| 29 | 如果下一步做 Eval-driven Human-in-the-loop Self-improvement，完整闭环怎么设计？ | M5/M8 | P1·规划中 | 当前仅有 Harness/Eval/AgentProfile；Data Flywheel/自动晋级未实现 |

## 三、指标与实验设计（30–38）

来源标签：字节/腾讯/百度/淘天/美团/携程等 AI 产品、Agent、评测岗位真实面经归纳

| # | 核心题 | 模块 | 当前状态 | 当前项目证据 / 边界 |
|---:|---|---|---|---|
| 30 | Agent 最核心的业务指标和技术指标分别是什么？ | M5 | P0·待压测 | 业务成功率/转化等 vs task completion/safety/latency/cost |
| 31 | 为什么 Agent 不能只看最终答案正确率？ | M5 | P0·可答 | Tool/过程/副作用/持久化结果都可能失败 |
| 32 | 如何评价 Tool Selection、Tool Parameter、Task Completion 和 Durable Outcome？ | M5 | P0·学习中 | `harness/*`, durable acceptance |
| 33 | 怎样衡量同一个 Case 多次运行的稳定性？ | M5 | P0·待准备 | 重复运行/通过率/方差；具体次数需真实实验决定 |
| 34 | 如何统计 Hallucination、Unsafe Action、Fallback 和 Escalation？ | M5 | P0·待准备 | Safety/eval/audit 真实字段 |
| 35 | RAG 应看 Retrieval 指标还是最终 Answer 指标？两者如何关联？ | M4/M5 | P0·未系统学习 | M4/M5 后完成 |
| 36 | 如何设计 Baseline 和 Ablation 实验？ | M5 | P0·待准备 | 固定 Case/Config，单变量对照 |
| 37 | 如何同时比较质量、延迟、Token、成本和稳定性？ | M5/M6 | P0·待准备 | Harness measurement + runtimeDuration；成本观测待补 |
| 38 | 如果准确率提高，但延迟和成本翻倍，如何决定是否上线？ | M5/M6 | P0·待打磨 | 按业务价值、SLA、风险、ROI 决策 |

## 四、Agent Runtime / Loop / Harness（39–51）

来源标签：字节 Agent/Agent Infra、阿里 Agent、百度 Agent 等真实面经归纳

| # | 核心题 | 模块 | 当前状态 | 当前项目证据 / 边界 |
|---:|---|---|---|---|
| 39 | 什么是 Agent Loop？ | M2 | P0·已学 | Pi 通用 loop + 产品治理边界 |
| 40 | SupportAgentRuntime 一次请求的完整控制流是什么？ | M2 | P0·学习中 | `src/index.ts::SupportAgentRuntime.run` |
| 41 | Pi Agent Runtime 和自己的 Runtime 分别负责什么？ | M2 | P0·已学 | Pi: generic loop；repo: authority/tools/policy/evidence/business |
| 42 | Planning 到底是框架负责还是模型负责？ | M2 | P0·待压测 | Pi 提供 loop；模型决定具体推理/调用 |
| 43 | ReAct 与 Plan-and-Execute 有什么区别？什么时候分别用？ | M8 | P1·未学 | 当前项目不以该对照实现 |
| 44 | Agent 为什么会空转、路径震荡或死循环？ | M2 | P0·待准备 | 不良 tool descriptions/context/模型行为；budget 防失控 |
| 45 | 怎么限制 Agent Turn 和 Tool Call？ | M2 | P0·已学 | 4 turns / 6 tool calls |
| 46 | Overall Timeout 与 Per-tool Timeout 分别解决什么问题？ | M2 | P0·已学 | 10s overall / 2s tool |
| 47 | Abort 为什么不等于 Rollback？ | M2/M3 | P0·已学 | 取消计算不回滚已发生副作用 |
| 48 | Harness 和 Runtime 有什么区别？ | M5 | P0·已学 | Harness 是实验执行/完整性控制，不是第二 Agent Loop |
| 49 | 为什么 Harness 必须调用真实 Runtime，而不是另写测试 Agent？ | M5 | P0·已学 | 避免评测与生产执行链漂移 |
| 50 | Harness 的 Case / Suite / Config / Measurement / Receipt 分别解决什么问题？ | M5 | P0·未系统复习 | `harness/contracts.ts`, `runner.ts`, `evaluate.ts`, `suites.ts` |
| 51 | Durable Acceptance 为什么比只检查模型文本更适合企业 Agent？ | M5 | P0·学习中 | `tests/harness/acceptance.test.ts` 等 |

## 五、Tool / Skill / MCP / AgentProfile（52–62）

来源标签：百度/字节/小红书/有赞等 Agent、产品工程面经归纳

| # | 核心题 | 模块 | 当前状态 | 当前项目证据 / 边界 |
|---:|---|---|---|---|
| 52 | Tool Calling 的完整过程是什么？ | M2 | P0·学习中 | `src/index.ts` createTools/beforeToolCall/events |
| 53 | 模型凭什么知道该调用哪个 Tool？ | M2 | P0·待准备 | tool schema/description + prompt/context |
| 54 | Tool Schema 设计不好会导致什么问题？ | M2 | P0·待准备 | 误选、参数错、歧义、不可验证 |
| 55 | 如何保证 Tool 参数可靠？ | M2/M3 | P0·待准备 | TypeBox schema + beforeToolCall + authority checks |
| 56 | Tool 调用超时、脏数据、重复执行分别怎么处理？ | M2/M3 | P0·部分已学 | timeout / validation / idempotency |
| 57 | Skill 和 Tool 有什么区别？ | M2 | P0·已学 | Skill=知识/工作方法上下文；Tool=可执行能力 |
| 58 | Skill 是怎么加载进 Runtime 的？ | M2 | P0·学习中 | `loadSkillsFromDir`, `AgentProfile.allowedSkills` |
| 59 | AgentProfile 的 identityPrompt、workPolicy、allowedSkills、allowedTools 各解决什么？ | M2 | P0·已学 | `src/enterprise/agent-profile.ts` |
| 60 | AgentProfile 限制 Tool 与 beforeToolCall 限制执行有什么区别？ | M2 | P0·已学 | 能力暴露 vs 单次动作授权 |
| 61 | MCP 和 Function Calling / 普通 API 有什么区别？ | M8 | P1·未学 | 当前 MCP 未实现 |
| 62 | 什么时候 MCP 是合理基础设施，什么时候属于过度设计？ | M8 | P1·未学 | 需在 M8 做架构取舍 |

## 六、RAG / Knowledge / Evidence（63–76）

来源标签：PDD/快手/字节/腾讯/阿里云/携程等 RAG、Agent、FDE 面经归纳

| # | 核心题 | 模块 | 当前状态 | 当前项目证据 / 边界 |
|---:|---|---|---|---|
| 63 | 从知识文档进入系统到 Agent 最终回答，完整 RAG 链是什么？ | M4 | P0·已有概念/未系统学习 | Node → FastAPI/pgvector → candidates → Node reconciliation → Evidence |
| 64 | Markdown、TXT、PDF 应分别怎样切块？ | M4 | P1·未系统学习 | 当前 repo 不支持用该问题反推已实现所有格式策略 |
| 65 | Chunk Size 和 Overlap 怎么确定，而不是拍脑袋？ | M4/M5 | P1·未系统学习 | 需通过 retrieval/e2e eval 验证 |
| 66 | 用什么实验判断切块策略更好？ | M4/M5 | P1·未系统学习 | 固定评测集比较 recall/answer/latency |
| 67 | Query 口语化、错别字或表达不清楚时怎么办？ | M4 | P0·有工作证据 | 过往搜索 Query 理解/Rewrite；当前项目未做完整 query rewrite pipeline |
| 68 | Query Rewrite 什么时候有帮助，什么时候可能改错用户意图？ | M4 | P0·有工作证据/待工程化 | 搜索评测经验可讲 |
| 69 | Vector Retrieval 擅长什么、短板是什么？ | M4 | P0·未系统学习 | 当前有 vector path |
| 70 | BM25 擅长什么、为什么很多系统要做 Hybrid Retrieval？ | M8 | P1·Gap | 当前项目 **未实现 BM25 Hybrid** |
| 71 | BM25 分数和 Vector Score 不在一个尺度上，怎么融合？ | M8 | P1·Gap | 当前项目未实现 hybrid score fusion |
| 72 | RRF 解决什么问题？ | M8 | P1·Gap | 当前项目 docs 中为 deferred/not implemented |
| 73 | 为什么还需要 Reranker / Cross-Encoder？ | M8 | P1·Gap | 当前项目未实现 reranker |
| 74 | 如果业务没有做 BM25/RRF/Reranker，怎样诚实解释当前方案和未来验证方式？ | M4/M8 | P0·必须会 | 现有 lexical default + vector opt-in；不得冒充 hybrid |
| 75 | Retrieval Candidate 为什么不能直接成为 Agent 可回答的 Evidence？ | M4 | P0·已学 | Evidence governance/admission |
| 76 | Node canonical reconciliation 具体解决什么风险？ | M4 | P0·已有概念/未系统学习 | scope/version/source/hash/status/profile 等校验 |

## 七、Context / Memory / Session（77–84）

来源标签：字节/快手/携程/小红书等 Agent、AI 应用面经归纳

| # | 核心题 | 模块 | 当前状态 | 当前项目证据 / 边界 |
|---:|---|---|---|---|
| 77 | System Prompt、Session History、Skill、RAG Evidence、Tool Result 分别属于什么上下文？ | M2 | P0·已学 | 当前 context engineering 边界 |
| 78 | Short-term Memory 和 Long-term Memory 有什么区别？ | M2/M8 | P0·可答 | 当前 short-term=Pi Session；未做完整 long-term memory |
| 79 | 当前项目为什么主要有 Session，而不是完整长期 Memory？ | M2 | P0·可答 | 真实 claim boundary |
| 80 | 上下文超过限制时有哪些压缩策略？ | M8 | P1·Gap | 当前未实现完整 context compression |
| 81 | 为什么不能无脑把所有历史对话都塞回 Context？ | M2 | P0·可答 | token/噪声/旧事实/权限风险 |
| 82 | Tool Result 应不应该进入会话历史？ | M2 | P0·待压测 | 需按 Pi Session/event 实际语义回答 |
| 83 | 新会话为什么不能直接复用旧 Session？ | M2 | P0·待压测 | 身份/上下文污染/权限与状态边界 |
| 84 | Session 恢复时如果 AgentProfile 或模型配置已经变化，应该怎么办？ | M2 | P0·学习中 | Profile id/version/hash binding；模型变化策略需守事实边界 |

## 八、企业权限、安全、Durable State（85–91）

来源标签：PDD/腾讯/携程/阿里/蚂蚁等企业 Agent、FDE、应用工程面经归纳

| # | 核心题 | 模块 | 当前状态 | 当前项目证据 / 边界 |
|---:|---|---|---|---|
| 85 | 为什么 LLM 不能成为最终权限判断者？ | M3 | P0·已学 | Node-owned authority |
| 86 | Identity、Tenant、Store Scope、Capability 应在哪里确定？ | M3 | P0·已学 | Enterprise layer/server-derived authority |
| 87 | Prompt Injection 如何防？ | M2/M3 | P0·已学 | authority not from user text + RAG as data + tool/output guards |
| 88 | 对有副作用的 Tool，如何处理授权、确认和审计？ | M3 | P0·未系统学习 | beforeToolCall + durable business + audit |
| 89 | 幂等键怎样防止 Ticket/Handoff 被重复创建？ | M3 | P0·已有概念/未系统学习 | `src/index.ts`, business store / PG path |
| 90 | Pi Session 为什么不能当作 Business Truth？ | M3 | P0·已学 | Session ≠ durable business records |
| 91 | 请求已经 Timeout，但数据库操作结果未知，为什么不能直接重试？ | M3 | P0·已学 | 先按 idempotency/durable state reconcile |

## 九、FDE / 交付 / 排障（92–97）

来源标签：阿里云 FDE 职责 + 多家公司 FDE/AI 解决方案/Agent 应用真实面经归纳

| # | 核心题 | 模块 | 当前状态 | 当前项目证据 / 边界 |
|---:|---|---|---|---|
| 92 | 客户只说“想上一个 Agent 提效”，怎么把模糊需求拆成可以实施和验收的项目？ | M6/M8 | P0·业务强项/待结构化 | 业务目标→流程→边界→数据→方案→验收 |
| 93 | 怎么判断客户流程适合 Agent、Workflow、普通软件还是根本不应使用 AI？ | M6/M8 | P0·待打磨 | 不为 Agent 而 Agent；按不确定性/工具/规则/风险取舍 |
| 94 | POC 的成功标准应该什么时候定义？技术指标和业务指标如何约定？ | M5/M6 | P0·强相关 | Eval 工作经验 + POC 验收 |
| 95 | 客户现场 Agent 突然效果下降，怎么判断是模型、Prompt、RAG、Tool、网络还是业务数据问题？ | M6 | P0·未系统学习 | request correlation + logs + eval split |
| 96 | 服务本地正常、部署到客户环境失败，Linux / Docker / HTTP / DNS / TLS / DB 怎么依次排查？ | M6 | P0·未系统学习 | Docker/Public HTTPS/Nginx/TLS/PG 真实项目链 |
| 97 | 客户要求一周上线，但当前 Eval 不达标，怎么沟通范围、风险、Fallback 和人工兜底？ | M5/M6 | P0·业务强项/待结构化 | FDE 沟通 + claim boundary + fail-closed |

## 十、AI 产品 / 电商业务（98–100）

来源标签：淘天/1688/PDD/美团/字节等 AI 产品、电商产品真实面经归纳

| # | 核心题 | 模块 | 当前状态 | 当前项目证据 / 边界 |
|---:|---|---|---|---|
| 98 | 如果给 1688 / PDD / 淘宝商家做选品 Agent，如何定义用户、目标、数据、Workflow 和验收指标？ | M8 | P0·业务强项/待打磨 | 真实电商运营经验 + AI 产品拆解 |
| 99 | 如何把用户评价、客服反馈、搜索 Query、转化数据变成下一步经营建议？ | M8 | P0·业务强项 | 电商运营 + 搜索评测 + Agent 产品 |
| 100 | AI 功能上线后 DAU、CTR 或转化没有变化，如何判断是产品价值、模型效果、用户采用还是实验设计问题？ | M5/M8 | P0·强项/待打磨 | 过往 A/B/DAU/CTR/转化观察经验 |

## 训练规则

每学完一个模块，只更新对应题的状态，不重排 M1–M8。每题最终至少保留：60–90 秒主回答、2–3 个压力追问、1 个真实代码/业务证据、1 个明确 Claim Boundary。真实面试出现的新题先归类到现有 100 题；只有出现新的能力维度时才新增题，不因同义问法无限扩容。
