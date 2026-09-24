# Interview Status

更新时间：2026-09-24

## 当前状态

### 已建立第一层理解 / 可以继续加深
- Agent Runtime / Pi 与产品边界
- Budget / Timeout / Abort
- Session vs Business Truth
- Context / Skill / Tool / Evidence
- Node Authority / beforeToolCall
- Governed RAG 的基本职责边界
- Harness 与 Eval 的区别
- 项目从 Runtime V0 → Enterprise POC 的演进主线

### 当前正在学习
- **M2 Agent Runtime & Context**
- 当前断点：已补 AgentProfile、allowedSkills/allowedTools、Profile version/hash、Session profile binding、Real Policy、Audit 的新增演进。
- 下一步：Pi real-provider、Session、Context、fallback、finish/result governance 串成完整链后结束 M2。

### 第一阶段未完成
- M3 Enterprise & Business
- M4 Knowledge & Retrieval
- M5 Harness & Eval
- M6 Delivery & Debugging
- M7 Code Ownership

### 第二阶段 JD Gap
- MCP
- Multi-Agent
- LangGraph
- K8s
- Long-term Memory / Context Compression
- Production Observability
- HITL / Data Flywheel / Eval-driven controlled self-improvement

## 面试题暴露出的高优先级风险

1. **评测是优势但需要工程化表达**  
   不能只讲 SOP/人工评测；必须把过往业务评测经验和当前 Harness / Eval / Durable Acceptance 串起来。

2. **RAG 面试极易被带到未实现技术**  
   当前项目没有 BM25/RRF/Cross-Encoder。必须会守边界，不能顺着面试官问题把它讲成已实现。

3. **项目复杂度高于当前个人源码掌控度**  
   现阶段继续加功能的收益低于 Code Ownership。

4. **FDE 面试不仅问 Agent，还会问排障、客户沟通、验收与部署**  
   M6 和真实需求拆解要提高权重，但不改变课程顺序。

5. **分布式系统基础可能成为意外深挖点**  
   Lease/Fencing/Redis/MySQL consistency 等纳入 P2 专项，不现在打断 POC 主线。

## 核心 100 题训练集

- 主文件：`CORE_100_INTERVIEW_QUESTIONS.md`
- 已按 P0/P1、M1–M8、当前掌握状态、项目证据/事实边界建立追踪。
- 后续每完成一个模块或真实面试复盘，只更新对应题状态；不因面经新增而打乱冻结学习顺序。
- BM25/RRF/Cross-Encoder/MCP/Multi-Agent/Long-term Memory 等仍按 Gap 管理，未实现不得包装为项目事实。

## 后续每场面试的记录格式

- 岗位 / 公司 / 轮次 / 日期
- 面试官原题
- 现场回答
- 追问
- 当场卡点
- 归类：P0 / P1 / P2 / P3
- 映射模块：M1–M8
- 是否属于当前项目真实实现
- 修正答案
- 是否需补源码/知识
- 压力复测：未测 / 未通过 / 通过

## 当前时间预算

- 现有 POC 第一轮全景：约 7–8 小时
- Code Ownership + 排障：约 10–14 小时
- JD Gap：约 5–7 小时

当前不改变总节奏：**先 POC 全景 → Code Ownership → JD Gap；投递可在第一轮完成后并行开始。**
