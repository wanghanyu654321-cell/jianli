# V5 Baseline Manifest

Status: **NEW V5 BASELINE — UPDATED WITH REAL WECHAT DEPLOYMENT / STORE POC / ACTUAL USE — NOT YET PROMOTED TO CANONICAL INDEX**

Branch: `resume/v5-grill-complete`  
Directory: `resume-workspace/10-baseline-v5-grill-complete/`

## Purpose

This V5 baseline is a new, complete R1–R6 mother baseline created after recruiter-style 10-second screening review and Grill-style evidence review.

It does **not** overwrite or mutate the frozen V4 baseline.

The repository already contains earlier historical directories named V5/V6. To preserve audit history and avoid silent overwrite, this new V5 lineage is stored in a new directory and branch rather than replacing those historical artifacts.

## Current Verified Agent State

As of the latest user-confirmed update:

- 数字前台 Agent **已完成微信真实部署**。
- 已在**实体本地生活门店完成 POC**。
- 门店**已开始在真实接待场景中实际使用**。
- 这使项目从 Pre-ICP / Demo / POC preparation 阶段进入 **real-store actual-use stage**。
- 当前仍**不自动等同于**长期稳定运行、规模化复制、Production SLA、商业成交、持续付费、客户留存、业务 ROI 或 production-calibrated retrieval quality 已完成验证。
- 微信真实部署已确认；**Live WeCom** 不因该事实自动视为已完成，除非后续另有确认。

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
   - 数字前台 Agent 证明能力已迁移到 AI / Agent 场景，并已进入真实门店使用。
5. **同一个数字前台项目保持统一事实。** R1–R6 只改变证据权重，不改写成六个不同项目。
6. **统一技术栈索引：**
   `TypeScript / Node.js｜React｜Python / FastAPI｜PostgreSQL 16 / pgvector｜Docker Compose｜RAG / Knowledge｜Prompt / Instruction｜Tool Calling｜Agent Runtime｜Eval / Regression / Harness`
7. **产品背景统一为：**
   实体商家线下接待已存在，但微信等私域入口存在第一接待与私域流量承接空白；第一阶段先解决“有人接、常见问题能答、预约 / 线索不丢、复杂问题有人接管”，再根据真实门店使用问题扩展轻量功能。
8. **CRM 太重不是项目起点。** 它只用于解释为什么第一阶段不重建完整 CRM。
9. **事实边界继续严格保持：**
   - 已完成微信真实部署 ≠ 已完成所有渠道部署
   - 已完成门店 POC ≠ 长期客户成功 / 商业成交
   - 门店开始实际使用 ≠ 已验证留存、ROI、效率提升或规模化复制
   - 工程 Acceptance + POC 完成 ≠ Production SLA 已成立
   - Hosted Embedding / production-calibrated retrieval quality 不虚构 PASS
   - Live WeCom / 复杂企业系统集成 / 企业采购成交闭环未确认时不写成已完成
10. **Team / Business Result 与个人贡献分开表达。** 不把团队 GMV 全部归因为个人。
11. **真实使用后的新证据只按实际发生更新。** 可写真实 Query / Badcase / 门店反馈的采集入口已经出现；在样本不足时，不提前写成稳定 Dataset、production distribution 或上线后指标提升。

## Role Positioning

- **R1｜Agent Eval / LLM Quality / AI Quality**
  - 主证据：淘天 Data Agent 评测与质量治理。
  - 差异化：Badcase Root Cause、Regression、Harness、业务结果验收与 Eval Integrity。
  - 最新增强：项目已进入真实门店使用，后续 Eval 开始具备真实 Query / Badcase 输入条件，但暂不声称 production-distribution benchmark 已建立。
- **R2｜Business FDE / AI Delivery**
  - 主证据：复杂业务拆解、上下游转译、0→1、项目推进、跨角色交付。
  - Agent 直接证据：需求 → Solution → Integration → 微信真实部署 → 实体门店 POC → 实际使用。
  - POC 后的重点不再是“能否交付”，而是长期稳定性、规模化复制、复杂系统集成与商业结果。
- **R3｜AI Commerce**
  - 主证据：完整 Commerce 经营链、Search / Ads / Content / BD / Supply / GMV。
  - AI 补强：Data Agent Query / Relevance + 已进入真实本地生活门店使用的 Merchant / Service Agent。
  - 不将门店开始使用提前包装成 AI 带来的 GMV / 转化增量。
- **R4｜AI Product Ops**
  - 主证据：用户需求、产品定位、产品协作、实验、数据反馈、流程优化。
  - Agent 直接证据：产品定义、MVP、功能优先级、Badcase 驱动迭代、微信部署、门店 POC、真实使用反馈入口。
  - 当前产品阶段从 Launch Readiness 进入 real-use iteration；长期留存和 post-launch metrics 仍待积累。
- **R5｜Agent Solution / Agent Application Engineering**
  - 主证据：数字前台工程机制、Trade-off、真实微信部署与门店 POC。
  - 正式经历补强：Data Agent Root Cause / Boundary Convergence + 真实业务 Context。
  - 已从本地 / 工程验证进入真实渠道和真实 Workflow，但不声称高并发、长期 On-call / SLA 或 production-calibrated retrieval 已完成。
- **R6｜AI Solution / AI Pre-sales**
  - 主证据：商务沟通、平台 / 工厂 / 达人协作、商业 Trade-off、多方推进。
  - Agent 直接证据：客户问题 → Solution → 技术边界 → 微信真实部署 → 门店 POC → 实际使用。
  - 当前仍需进一步补长期客户价值、商业付费、采购 / 成交和规模化复制证据。

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
- `resume-workspace/CURRENT_VERSION_INDEX.md` is intentionally not changed yet.
- Promotion of this V5 to the canonical current version should happen only after final integrity review and explicit approval.
- Future JD-specific versions derive from this V5; they do not rewrite this mother baseline silently.
- Final application preparation should use: **V5 mother baseline → exact JD Must-have decomposition → evidence selection → 10-second recruiter screen → targeted compression → ATS / render check**.
