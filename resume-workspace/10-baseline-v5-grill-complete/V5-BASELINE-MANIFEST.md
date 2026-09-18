# V5 Baseline Manifest

Status: **NEW V5 BASELINE — CREATED / REVIEWED CONTENT / NOT YET PROMOTED TO CANONICAL INDEX**

Branch: `resume/v5-grill-complete`  
Directory: `resume-workspace/10-baseline-v5-grill-complete/`

## Purpose

This V5 baseline is a new, complete R1–R6 mother baseline created after recruiter-style 10-second screening review and Grill-style evidence review.

It does **not** overwrite or mutate the frozen V4 baseline.

The repository already contains earlier historical directories named V5/V6. To preserve audit history and avoid silent overwrite, this new V5 lineage is stored in a new directory and branch rather than replacing those historical artifacts.

## V5 Writing Rules

1. **母版不压缩。** 完整 reasoning chain 保留在母版中；压缩只发生在后续具体 JD 投递版。
2. **粗体标题优先使用中文 / 常见 JD 招聘关键词。** 技术内部术语作为正文证据，不抢第一视觉层。
3. **每条高价值 bullet 尽量保留完整链路：**
   - 业务场景 / 问题
   - 观察信号
   - 判断
   - 动作
   - 方案取舍
   - 结果 / 验证
4. **正式经历与 Agent 项目保持平衡。**
   - 正式经历证明过去真实做过什么。
   - 可迁移能力解释为什么能够进入目标岗位。
   - 数字前台 Agent 证明能力已迁移到 AI / Agent 场景。
5. **同一个数字前台项目保持统一事实。** R1–R6 只改变证据权重，不改写成六个不同项目。
6. **统一技术栈索引：**
   `TypeScript / Node.js｜React｜Python / FastAPI｜PostgreSQL 16 / pgvector｜Docker Compose｜RAG / Knowledge｜Prompt / Instruction｜Tool Calling｜Agent Runtime｜Eval / Regression / Harness`
7. **产品背景统一为：**
   实体商家线下接待已存在，但微信等私域入口存在第一接待与私域流量承接空白；第一阶段先解决“有人接、常见问题能答、预约 / 线索不丢、复杂问题有人接管”，再根据真实门店使用问题扩展轻量功能。
8. **CRM 太重不是项目起点。** 它只用于解释为什么第一阶段不重建完整 CRM。
9. **事实边界继续严格保持：**
   - Pre-ICP Engineering Baseline ≠ Production Ready
   - 工程验收 ≠ 真实客户 POC 验收
   - Demo / POC 准备 ≠ 已完成真实客户部署
   - Hosted Embedding / production-calibrated retrieval quality 不虚构 PASS
   - Live WeCom / Production SLA / 企业采购成交闭环未完成时不写成已完成
10. **Team / Business Result 与个人贡献分开表达。** 不把团队 GMV 全部归因为个人。

## Role Positioning

- **R1｜Agent Eval / LLM Quality / AI Quality**
  - 主证据：淘天 Data Agent 评测与质量治理。
  - 差异化：Badcase Root Cause、Regression、Harness、业务结果验收与 Eval Integrity。
- **R2｜Business FDE / AI Delivery**
  - 主证据：复杂业务拆解、上下游转译、0→1、项目推进、跨角色交付。
  - Agent 补强：需求 → Solution → Integration → POC 准备。
- **R3｜AI Commerce**
  - 主证据：完整 Commerce 经营链、Search / Ads / Content / BD / Supply / GMV。
  - AI 补强：Data Agent Query / Relevance + Merchant / Service Agent。
- **R4｜AI Product Ops**
  - 主证据：用户需求、产品定位、产品协作、实验、数据反馈、流程优化。
  - Agent 补强：产品定义、MVP、功能优先级、Badcase 驱动迭代、产品边界。
- **R5｜Agent Solution / Agent Application Engineering**
  - 主证据：数字前台工程机制与 Trade-off。
  - 正式经历补强：Data Agent Root Cause / Boundary Convergence + 真实业务 Context。
- **R6｜AI Solution / AI Pre-sales**
  - 主证据：商务沟通、平台 / 工厂 / 达人协作、商业 Trade-off、多方推进。
  - Agent 补强：客户问题 → Solution → 技术边界 → POC 验收准备。

## Files

- `R1-Agent-Eval/R1-Agent-Eval.RESUME.md`
- `R2-Business-FDE/R2-Business-FDE.RESUME.md`
- `R3-AI-Commerce/R3-AI-Commerce.RESUME.md`
- `R4-AI-Product-Ops/R4-AI-Product-Ops.RESUME.md`
- `R5-Agent-Solution/R5-Agent-Solution.RESUME.md`
- `R6-AI-Solution/R6-AI-Solution.RESUME.md`

## Governance

- V4 remains untouched as a restoration point.
- Existing historical V5/V6 directories remain untouched.
- `resume-workspace/CURRENT_VERSION_INDEX.md` is intentionally not changed in this creation step.
- Promotion of this V5 to the canonical current version should happen only after integrity verification and explicit approval.
- Future JD-specific versions derive from this V5; they do not rewrite this mother baseline silently.
