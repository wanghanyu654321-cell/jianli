# Resume Review & Acceptance Policy

本文件是本仓库所有后续 AI / Agent / 人工审查的强制验收规则。

目标：防止“目录结构正确、文件命名正确、事实治理做得好”被误判为“简历成品已经完成”。任何审查都必须先验证实际交付物，再评价内容质量。

## 1. Repository First（仓库优先）

当用户要求“看仓库里的简历怎么样”“审查当前简历进度”“判断是否可以投递”等任务时，审查者必须以指定仓库和指定 commit / branch 的实际文件为第一证据源。

禁止仅根据：

- 历史聊天上下文；
- 模型记忆；
- 之前的设计方案；
- 文件名；
- 目录名；
- Pipeline Status（流水线状态）中的自述；
- 生成过程是否规范；

直接判断交付已经完成。

历史上下文只能帮助理解验收目标，不能代替实际文件检查。

## 2. Mandatory Review Order（强制审查顺序）

任何正式评价必须按以下顺序执行：

1. 锁定用户指定的 repository（仓库）与 commit / branch。
2. 枚举本次需要评价的实际交付文件。
3. 完整读取目标文件，而不是只读取 README、索引、状态文件或摘要。
4. 找到并读取与该交付物对应的原始 acceptance criteria（验收标准）。
5. 先判断交付状态：`COMPLETE / PARTIAL / NOT_COMPLETE`。
6. 只有完成第 5 步后，才评价内容质量、岗位匹配、事实安全、ATS（招聘系统解析）等。
7. 最后才允许结合历史设计上下文解释“为什么这样写”或给下一步建议。

不得跳过第 4–5 步直接给出“很好”“已完成”“可以投递”等结论。

## 3. Process Quality ≠ Deliverable Quality（流程质量不等于成品质量）

以下内容即使做得很好，也不能单独证明 Resume（简历）成品已经完成：

- Claim Ledger（主张证据账本）完整；
- Requirement × Evidence Matrix（要求×证据矩阵）正确；
- 事实边界严格；
- 岗位族分类合理；
- 文件目录结构规范；
- Skill（技能）调用顺序正确；
- 没有事实漂移；
- Blueprint（蓝图）选材正确。

审查报告必须分别评价：

- Evidence / Fact Governance（事实与证据治理）
- Positioning / Role Selection（岗位定位与选材）
- Resume Deliverable Completeness（简历交付完整度）
- Application Readiness（真实投递准备度）

禁止把其中一个维度的高分替代其他维度。

## 4. Filename Is Not Evidence（文件名不是完成证据）

`R1-Agent-Eval.md`、`R2-Business-FDE.md`、`R3-AI-Commerce.md` 等文件即使位于 `03-baselines/`，也不能仅凭路径或文件名认定为完成的 Role Baseline Resume（岗位族基线简历）。

文件名叫 `Baseline`、`Master`、`Final`、`ATS_PASS`、`Complete` 均不构成验收证据。

必须检查文件实际内容是否满足对应 Gate（门禁）。

## 5. Role Baseline Resume Gate（岗位族基线简历门禁）

Role Baseline Resume 的目标是：作为真实 Single-JD Tailoring（单条 JD 定制）的稳定起点，而不是岗位选材摘要。

默认目标长度：约 1.5–2 页；内容不足时不强行填满 2 页，但不得只用极短摘要冒充完整基线。

一份岗位族基线至少应具备下列正式简历层内容（具体顺序可按岗位调整）：

- Header（姓名 / 联系方式 / 城市 / GitHub 等正式投递字段；若真实字段因隐私未入公开仓库，必须明确标记为外部注入字段，而不是静默缺失）；
- Target Role（目标岗位）；
- Professional Summary（职业摘要）；
- Core Competencies / Skills（核心能力 / 技能）；
- Relevant Work Experience（完整且经岗位筛选的相关工作经历）；
- Selected Project(s)（必要时加入核心项目）；
- Education（教育信息，或明确说明由私有事实源在渲染阶段注入）；
- 足够的 Bullet（要点）密度，使其能够作为真实 JD 定制的母稿。

若文件只有类似：

`Positioning → Experience selections → Skills emphasis → Gates`

这种结构，则默认判定为：

`ROLE_BLUEPRINT / PARTIAL`

而不是完成的 `ROLE_BASELINE_RESUME`。

## 6. Audit Content Must Be Separated（审计内容与投递内容分离）

以下内容属于内部审计，不应直接出现在面向招聘方的正式 Resume（简历）正文中：

- “不能写成生产部署”；
- “未确认客户交付”；
- “不宣称完整线上权限”；
- “该指标禁用”；
- “仓库尚未核验”；
- 其他 Gates（门禁）、Prohibited Claims（禁用主张）、证据状态说明。

建议拆分为：

- `*.RESUME.md`：面向招聘方的简历内容；
- `*.AUDIT.md`：证据边界、禁用表达、事实核验、ATS / Fact Gate 等内部审计信息。

如果两类内容混在同一文件中，必须明确标记为 `PARTIAL` 或 `INTERNAL_DRAFT`，不能称为最终投递版。

## 7. Single-JD Resume Gate（单条 JD 简历门禁）

Single-JD Tailored Resume（单条 JD 定制简历）必须基于一条真实、完整或足够完整的目标 JD。

没有真实 JD 时，可以生成 Role Baseline（岗位族基线），但不能宣称已经完成公司级定制。

Single-JD Resume 必须经过：

`JD Freeze → JD × Evidence Matrix → Tailoring → Content Review → ATS Audit → Final Fact Gate → Render`

其中事实只能来自已批准的事实源 / Claim Ledger / 已核验 Repo Evidence（仓库证据）。JD 中出现的关键词不能因为“岗位要求有”就直接写进简历。

## 8. Review Conclusion Format（审查结论格式）

以后评价仓库里的简历时，结论必须首先回答交付状态，而不是先给感受性评价。

推荐格式：

```text
DELIVERABLE STATUS

R1 Agent Eval: COMPLETE / PARTIAL / NOT_COMPLETE
R2 Business FDE: COMPLETE / PARTIAL / NOT_COMPLETE
R3 AI Commerce: COMPLETE / PARTIAL / NOT_COMPLETE
...

FACT GOVERNANCE: PASS / PARTIAL / FAIL
ROLE POSITIONING: PASS / PARTIAL / FAIL
ROLE BASELINE GATE: PASS / PARTIAL / FAIL
SINGLE-JD GATE: PASS / NOT_RUN / FAIL
ATS GATE: PASS / NOT_RUN / FAIL
APPLICATION READY: YES / NO
```

然后才能说明优点、缺点和下一步。

## 9. Evidence of Completion（完成证据）

任何“完成”结论必须能够回答：

- 哪个文件是交付物？
- 实际读取了什么内容？
- 对应的验收标准是什么？
- 哪些 Gate 已通过？
- 哪些 Gate 尚未运行？
- 是否可以直接用于招聘方投递？

如果无法回答其中任一关键问题，不得使用“已完成”“最终版”“可以直接投递”等措辞。

## 10. Current Repository Interpretation Rule（当前仓库解释规则）

在本规则生效后，`resume-workspace/03-baselines/` 中的 R1–R6 文件必须按实际内容重新过 `Role Baseline Resume Gate`。

在未满足第 5 节完整度要求前，应视为：

`ROLE_BLUEPRINT / PARTIAL`

即：岗位族选材蓝图 / 内容骨架，而不是完整的约 2 页岗位族基线简历。

后续如果这些文件扩展为完整基线，应通过实际内容重新验收后再升级状态；不能只改文件名或 Pipeline Status。

## 11. Highest-Level Principle（最高原则）

**先验证“交付物是不是做完了”，再评价“做得好不好”。**

**目录正确 ≠ 文件完成。**

**事实安全 ≠ 简历完整。**

**Blueprint 正确 ≠ Resume 完成。**

**历史上下文只能辅助理解，不能替代对当前仓库实际文件的完整阅读。**
