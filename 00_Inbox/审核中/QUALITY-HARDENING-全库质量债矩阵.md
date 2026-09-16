---
type: 质量债矩阵
subject: 系统架构设计师
status: debt_matrix_locked
stage: quality_hardening_in_progress
coverage_status: syllabus_build_complete
coverage_gate: PASS
start_head: cc83f997202a64288bafc198afbc13f057fd1177
current_priority: QH-06-MATH-ENG
updated: 2026-09-16
tags: [软考/架构设计师, QUALITY-HARDENING, 质量债, 审核]
---

# QUALITY-HARDENING · 全库质量债矩阵

> [!important] 阶段边界
> 本矩阵只管理 **QUALITY / REVIEW** 债务，不重新做 coverage。`G4-COVERAGE-FINAL-RERUN` 的 `PASS` 继续有效；01 保持 `study_complete / user_accepted / coverage_audit_skipped`；04/05/06 共 4 个 legal `link_only` 保持不变。

## 1. 当前结论

- coverage regression candidate：**0**
- 当前开放质量债：**P0 = 0 / P1 = 1 / P2 = 1 / 合计 = 2**
- 已收口质量债：**QH-SEC-001、QH-02-001、QH-05-001、QH-05-002、QH-07-001、QH-07-002、QH-08-001、QH-09-001、QH-10-001、QH-11-001**
- 当前质量控制状态：`quality_hardening_in_progress / debt_matrix_locked`
- 当前下一批：**`QH-06-MATH-ENG`**（尚未执行）
- 02：**30/30 covered / review_closed / normal_maintenance**
- 05：**33 covered + 1 legal link_only / quality_hardened / normal_maintenance**
- 07：**29/29 covered / quality_hardened / normal_maintenance**
- 08：**15/15 covered / quality_hardened / normal_maintenance**
- 09：**16/16 covered / quality_hardened / normal_maintenance**
- 10：**13/13 covered / quality_hardened / normal_maintenance**
- 11：**15/15 covered / quality_hardened / normal_maintenance**

## 2. 等级口径

- **P0**：事实/教材错误、stable 主事实源失效、真正导航断裂、关键机制缺失到可能直接导致考试选错。
- **P1**：明显影响学习效率或考试判断，例如关键入口不同步、学习链有假断点、零基础入口缺少必要前因后果。
- **P2**：不阻塞学习的导航、措辞、排版和一致性优化。

## 3. 02～13 质量画像

| 章 | 当前 coverage 状态 | 当前 quality/review 状态 | P0 | P1 | P2 | 主要质量债 | 推荐批次 |
| ---: | --- | --- | ---: | ---: | ---: | --- | --- |
| 02 信息系统基础知识 | 30/30 covered | review_closed / normal_maintenance | 0 | 0 | 0 | `QH-02-001` 已关闭 | 正常维护 |
| 03 信息安全技术 | coverage_complete | security_quality_insert_closed / normal_maintenance | 0 | 0 | 0 | QH-SEC-00/01/02/03 已收口 | 正常维护 |
| 04 软件工程基础知识 | 44 covered + 1 legal link_only | 已有完整审查链 | 0 | 0 | 0 | 无当前开放债 | 后置维护 |
| 05 数据库设计基础知识 | 33 covered + 1 legal link_only | quality_hardened / normal_maintenance | 0 | 0 | 0 | `QH-05-001 / QH-05-002` 已关闭 | 正常维护 |
| 06 软件架构设计 | 32 covered + 2 legal link_only | third_round_complete | 0 | 0 | 0 | 无当前开放债 | 后置维护 |
| 07 系统质量属性与架构评估 | 29/29 covered | quality_hardened / normal_maintenance | 0 | 0 | 0 | `QH-07-001 / QH-07-002` 已关闭 | 正常维护 |
| 08 软件可靠性技术 | 15/15 covered | quality_hardened / normal_maintenance | 0 | 0 | 0 | `QH-08-001` 已关闭；章级速记入口已建立 | 正常维护 |
| 09 软件架构的演化和维护 | 16/16 covered | quality_hardened / normal_maintenance | 0 | 0 | 0 | `QH-09-001` 已关闭；章级速记入口已建立 | 正常维护 |
| 10 未来信息综合技术 | 13/13 covered | **quality_hardened / normal_maintenance** | 0 | 0 | 0 | `QH-10-001` 已关闭；章级速记入口已建立 | 正常维护 |
| 11 标准化与知识产权 | 15/15 covered | **quality_hardened / normal_maintenance** | 0 | 0 | 0 | `QH-11-001` 已关闭；章级速记入口已建立 | 正常维护 |
| 12 应用数学 | 16/16 covered | quality_pending | 0 | 0 | 1 | 13 下一站缺物理 Wikilink | QH-06-MATH-ENG |
| 13 专业英语 | 15/15 covered | quality_pending | 0 | 1 | 0 | 仍把已 PASS 的统一 coverage 验收写成下一动作 | QH-06-MATH-ENG |

### 开放债务汇总

| 严重度 | 数量 |
| --- | ---: |
| P0 | 0 |
| P1 | 1 |
| P2 | 1 |
| **合计** | **2** |

## 4. 文件级开放质量债

| Debt ID | 章节 | 文件 | 问题 | 证据类型 | 严重度 | 推荐动作 | 是否涉及 coverage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| QH-12-001 | 12 | `01_综合知识/12_应用数学/应用数学-学习路线.md` | 下一站语义指向 13，但缺已存在 13 章物理 Wikilink | 跨章导航弱化 | P2 | QH-06 增加真实 12→13 入口 | 否 |
| QH-13-001 | 13 | `01_综合知识/13_专业英语/专业英语-学习路线.md` | 仍把后续统一 coverage 验收写成下一动作，而 FINAL-RERUN 已 PASS | 阶段导航陈旧 | P1 | QH-06 改为末章收口 + QUALITY/复习入口 | 否 |

### 已收口债务

| Debt ID | 章节 | 原问题 | 收口批次 | 结果 | coverage |
| --- | --- | --- | --- | --- | --- |
| QH-SEC-001 | 03 | 首次学习缺少统一安全教学桥 | QH-SEC-00 | 建立零基础入口与统一安全主线 | 不回退，PASS |
| QH-02-001 | 02 | 30/30 covered，但索引仍把旧 G2 三轮施工写成当前动作 | QH-01-IS-REVIEW-CLOSE | 清除旧施工状态，转正常维护 | 不回退，30/30 PASS |
| QH-05-001 | 05 | 数据库索引仍残留 4 partial / 待收口口径 | QH-02-DB-HARDEN | 同步最终契约并清除旧施工状态 | 不回退，PASS |
| QH-05-002 | 05 | 学习路线仍把 4 partial / 尚未联合验收写成下一动作 | QH-02-DB-HARDEN | 学习路线回归正常学习主线 | 不回退，PASS |
| QH-07-001 | 07 | 索引未同步 29-Atom 最终契约 | QH-03-QA-HARDEN | 同步 `QA-A001~QA-A029`、29/29 covered | 不回退，29/29 PASS |
| QH-07-002 | 07 | 考前速记缺最终契约高价值入口 | QH-03-QA-HARDEN | 补齐快速复习入口 | 不回退，29/29 PASS |
| QH-08-001 | 08 | 学习路线仍写 09 尚未建设 | QH-04-REL-EVO | 建立真实 08→09 Wikilink，并清理 `REL-A015` 同源旧施工文案 | 不回退，15/15 PASS |
| QH-09-001 | 09 | 学习路线仍写 10 尚未建设 | QH-04-REL-EVO | 建立真实 09→10 Wikilink，并清理 `EVO-A016` 同源旧施工文案 | 不回退，16/16 PASS |
| QH-10-001 | 10 | 学习路线仍保留“下一大章若尚未建设”的施工期措辞 | **QH-05-FUT-IPR** | 建立真实 10→11 Wikilink；同步修复 `FUT-A013` 旧下一章文案；新增章级速记 | 不回退，13/13 PASS |
| QH-11-001 | 11 | 学习路线仍写 12 应用数学尚未真实存在 | **QH-05-FUT-IPR** | 建立真实 11→12 Wikilink；同步修复 `IPR-A015` 旧施工文案；新增章级速记 | 不回退，15/15 PASS |

## 5. coverage 回归检查

QH-05 未发现：stable Atom 主事实源消失、正文只剩标题/占位、新的 `partial / unmapped / blocked`、legal link_only 目标失效或大纲有效范围被错误删除。

- 10：13 covered，link_only = 0，partial = 0，unmapped = 0，blocked = 0。
- 11：15 covered，link_only = 0，partial = 0，unmapped = 0，blocked = 0。
- 全库既有 4 个 legal link_only 仍属于 04/05/06，本轮未触碰。

结论：**`coverage_regression_candidate = 0`，10/11 coverage gate 继续 PASS。**

## 6. QH-05 代表性抽查结论

- 10：抽查 `FUT-A001 / A008 / A010 / A013`，CPS、边缘计算、数字孪生、云与大数据主线均已有明确题干信号、边界和考试第一动作，无需批量重写。
- 10 真实修复集中在：索引质量状态、章级速记入口、10→11 学习路线，以及 `FUT-A013` 末尾错误下一章文案。
- 11：抽查 `IPR-A001 / A006 / A008 / A015`，标准化与知识产权分流、“先认对象再认权利”、软件著作权表达边界均清楚，无需批量重写。
- 11 真实修复集中在：索引质量状态、章级速记入口、11→12 学习路线，以及 `IPR-A015` 末尾旧施工文案。
- 本轮没有新增 Atom，没有改变 P0/P1/P2 构成，也没有凭模型记忆新增法律数字；版本敏感内容继续以本章审核记录为准。

结论：**10 未来信息综合技术与 11 标准化与知识产权均进入 `coverage_complete / quality_hardened / normal_maintenance`。**

## 7. 后续施工路线

1. **QH-06-MATH-ENG**：12 应用数学 + 13 专业英语（当前最高优先级，尚未执行）。
2. 后置维护：03～11 只有出现新证据或真实 P0 时再进入专项处理。
3. QH-06 收口后重新统计全库 QUALITY 债；若确认为 0，再由总控决定 QUALITY-HARDENING 是否正式结束，不自动制造新批次。

> [!important] 当前停点
> `QH-05-FUT-IPR` 已关闭；当前最高优先级切换为 **`QH-06-MATH-ENG`**，本轮只登记，不自动执行。
