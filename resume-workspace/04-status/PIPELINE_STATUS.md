> STATUS: SUPERSEDED — historical snapshot retained for audit only. Use `resume-workspace/00-source/CANONICAL_TIMELINE.md` and `resume-workspace/05-baseline-v2/` for current facts.

# Resume Pipeline Status

## Completed

- Source Discovery 已完成：找到唯一事实母版和唯一 JD MASTER。
- Source resolution 已通过：两份文档均为 V3，文件和正文没有冲突。
- DOCX 已在本地抽取段落/表格并保存到 `work/source-extracted/`，可用行号复核。
- Claim Ledger、Requirement × Evidence Matrix 和六个岗位族基线已建立。
- R7 Stretch 已单独记录缺口，不生成基线。

## Deliberately not run

- `repo-to-resume`：当前工作区没有事实源引用项目的本地 checkout；同目录现有仓库是 Seedance 项目，不能替代。
- `resume-tailoring`：没有单条真实公司/岗位 JD。
- `$build-tailored-resume` 和 Param/ASu ATS 审查：必须在单条 JD 的内容冻结后执行。
- `$make-resume`：没有姓名/联系方式/教育等完整投递字段，且当前只处于岗位族基线阶段。

## Verification boundary

- `python-docx` 本地段落/表格抽取成功：事实源 643 段落、0 表格；JD 源 581 段落、4 表格。
- 文档渲染检查已尝试，但运行时未找到 bundled LibreOffice `soffice.exe`，因此没有 PNG 级视觉结论；这不影响文本/结构抽取结论。
- 不能据此宣称任何招聘平台 ATS 通过、生产上线、真实客户结果或仓库实现已核验。
