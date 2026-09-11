---
type: 质量债矩阵
subject: 系统架构设计师
status: debt_matrix_locked
stage: quality_hardening_in_progress
coverage_status: syllabus_build_complete
coverage_gate: PASS
start_head: cc83f997202a64288bafc198afbc13f057fd1177
current_priority: QH-04-REL-EVO
updated: 2026-09-11
tags: [软考/架构设计师, QUALITY-HARDENING, 质量债, 审核]
---

# QUALITY-HARDENING · 全库质量债矩阵

> [!important] 阶段边界
> 本矩阵只管理 **QUALITY / REVIEW** 债务，不重新做 coverage。`G4-COVERAGE-FINAL-RERUN` 的 `PASS` 继续有效；01 保持 `study_complete / user_accepted / coverage_audit_skipped`；04/05/06 共 4 个 legal `link_only` 保持不变。

## 1. 当前结论

- coverage regression candidate：**0**
- 当前开放质量债：**P0 = 0 / P1 = 4 / P2 = 2 / 合计 = 6**
- 已收口质量债：**QH-SEC-001、QH-02-001、QH-05-001、QH-05-002、QH-07-001、QH-07-002**
- 当前质量控制状态：`quality_hardening_in_progress / debt_matrix_locked`
- 当前下一批：**`QH-04-REL-EVO`**（尚未执行）
- 02：**30/30 covered / review_closed / normal_maintenance**
- 05：**33 covered + 1 legal link_only / quality_hardened / normal_maintenance**
- 07：**29/29 covered / quality_hardened / normal_maintenance**

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
| 07 系统质量属性与架构评估 | 29/29 covered | **quality_hardened / normal_maintenance** | 0 | 0 | 0 | `QH-07-001 / QH-07-002` 已关闭；索引、路线、速记与最终 29-Atom 契约一致 | 正常维护 |
| 08 软件可靠性技术 | 15/15 covered | quality_pending | 0 | 1 | 0 | 学习路线仍写“09 尚未建设” | QH-04-REL-EVO |
| 09 软件架构的演化和维护 | 16/16 covered | quality_pending | 0 | 1 | 0 | 学习路线仍写“10 尚未建设” | QH-04-REL-EVO |
| 10 未来信息综合技术 | 13/13 covered | quality_pending | 0 | 0 | 1 | 下一站仍为条件式施工文案 | QH-05-FUT-IPR |
| 11 标准化与知识产权 | 15/15 covered | quality_pending | 0 | 1 | 0 | 学习路线仍称 12 尚未真实存在 | QH-05-FUT-IPR |
| 12 应用数学 | 16/16 covered | quality_pending | 0 | 0 | 1 | 13 下一站缺物理 Wikilink | QH-06-MATH-ENG |
| 13 专业英语 | 15/15 covered | quality_pending | 0 | 1 | 0 | 仍把已 PASS 的统一 coverage 验收写成下一动作 | QH-06-MATH-ENG |

### 开放债务汇总

| 严重度 | 数量 |
| --- | ---: |
| P0 | 0 |
| P1 | 4 |
| P2 | 2 |
| **合计** | **6** |

## 4. 文件级开放质量债

| Debt ID | 章节 | 文件 | 问题 | 证据类型 | 严重度 | 推荐动作 | 是否涉及 coverage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| QH-08-001 | 08 | `01_综合知识/08_软件可靠性技术/学习路线.md` | 仍写 09 尚未建设，但 09 已完成 coverage | 跨章导航假断点 | P1 | QH-04 改为真实 08→09 Wikilink | 否 |
| QH-09-001 | 09 | `01_综合知识/09_软件架构的演化和维护/学习路线.md` | 仍写 10 尚未建设，但 10 已完成 coverage | 跨章导航假断点 | P1 | QH-04 改为真实 09→10 Wikilink | 否 |
| QH-10-001 | 10 | `01_综合知识/10_未来信息综合技术/未来信息综合技术-学习路线.md` | 章末仍保留“下一大章若尚未建设”的施工期措辞 | 跨章导航弱化 | P2 | QH-05 直接指向 11 | 否 |
| QH-11-001 | 11 | `01_综合知识/11_标准化与知识产权/标准化与知识产权-学习路线.md` | 仍写 12_应用数学尚未真实存在 | 跨章导航假断点 | P1 | QH-05 改为真实 11→12 Wikilink | 否 |
| QH-12-001 | 12 | `01_综合知识/12_应用数学/应用数学-学习路线.md` | 下一站语义指向 13，但缺已存在 13 章物理 Wikilink | 跨章导航弱化 | P2 | QH-06 增加真实 12→13 入口 | 否 |
| QH-13-001 | 13 | `01_综合知识/13_专业英语/专业英语-学习路线.md` | 仍把后续统一 coverage 验收写成下一动作，而 FINAL-RERUN 已 PASS | 阶段导航陈旧 | P1 | QH-06 改为末章收口 + QUALITY/复习入口 | 否 |

### 已收口债务

| Debt ID | 章节 | 原问题 | 收口批次 | 结果 | coverage |
| --- | --- | --- | --- | --- | --- |
| QH-SEC-001 | 03 | 首次学习缺少统一安全教学桥 | QH-SEC-00 | 建立零基础入口与统一安全主线 | 不回退，PASS |
| QH-02-001 | 02 | 30/30 covered，但索引仍把旧 G2 三轮施工写成当前动作 | QH-01-IS-REVIEW-CLOSE | 清除旧施工状态，转正常维护 | 不回退，30/30 PASS |
| QH-05-001 | 05 | `G3-DB-CLOSE` 已完成，但数据库索引仍残留 4 partial / 待收口口径 | QH-02-DB-HARDEN | 索引同步为 34 stable = 33 covered + 1 legal link_only，旧施工状态清除 | 不回退，PASS |
| QH-05-002 | 05 | 学习路线仍把 4 partial / 尚未联合验收写成下一动作 | QH-02-DB-HARDEN | 学习路线回归正常学习主线并清除旧 G3 导航 | 不回退，PASS |
| QH-07-001 | 07 | 索引仍以旧“14 张 P0 原子卡”作为当前口径，未同步 29-Atom 最终契约 | **QH-03-QA-HARDEN** | 明确 `QA-A001~QA-A029`、29/29 covered，并说明 14 是主事实源文件数量而非 stable Atom 数 | 不回退，29/29 PASS |
| QH-07-002 | 07 | 考前速记缺功能性、可变性、互操作性、ATAM 阶段/步骤等最终契约高价值入口 | **QH-03-QA-HARDEN** | 从既有主事实源提炼题眼、第一动作、ATAM 四阶段/7 步、风险/非风险等快速复习入口 | 不回退，29/29 PASS |

## 5. coverage 回归检查

QH-03 未发现：

- stable Atom 主事实源消失；
- 已 covered Atom 只剩标题/占位；
- 新的 `partial / unmapped / blocked`；
- 失效的跨章事实源；
- 大纲有效范围被错误删除。

07 本身 `link_only = 0`；因此本轮不存在 legal link_only 失效风险。

结论：**`coverage_regression_candidate = 0`，07 仍为 29/29 covered，coverage gate 继续 PASS。**

## 6. QH-03 代表性抽查结论

- [[质量属性-开发期与运行期]]：已经完整承担功能 vs 质量、功能性、可变性、互操作性和质量冲突主线；无需修改正文。
- [[质量属性场景六要素]]：六要素的目的、关系和示例清楚；无需修改正文。
- [[性能质量属性场景]]：响应时间、吞吐量、负载、期限等第一判断入口完整；无需修改正文。
- [[可靠性与可用性]]：已明确“少故障 vs 需要服务时能用/快速恢复”；无需修改正文。
- [[安全性质量属性场景]]：保持架构质量属性语境，没有复制信息安全章节；无需修改正文。
- [[可修改性质量属性场景]]：变化范围、受影响构件、时间和成本闭环完整；无需修改正文。
- [[架构评估-问卷场景与度量]]：已经解释评估目的、三类方法和利益相关者/场景；无需修改正文。
- [[敏感点与权衡点]]：敏感点、权衡点、风险、非风险边界清楚；无需修改正文。
- [[ATAM架构权衡分析]]：目的、角色、业务驱动、四阶段、7 步和输出完整；无需修改正文。
- [[ATAM效用树]]、[[SAAM架构评估]]、[[CBAM成本效益分析]]：均具备稳定考试入口；无需修改正文。
- 真正问题只落在 07 索引、学习路线和考前速记入口；均已定点修复。

结论：**07 系统质量属性与架构评估进入 `coverage_complete / quality_hardened / normal_maintenance`。**

## 7. 后续施工路线

1. **QH-04-REL-EVO**：08 软件可靠性 + 09 软件架构演化维护（当前最高优先级，尚未执行）。
2. **QH-05-FUT-IPR**：10 未来信息综合技术 + 11 标准化与知识产权。
3. **QH-06-MATH-ENG**：12 应用数学 + 13 专业英语。
4. 后置维护：03 / 04 / 05 / 06 / 07 只有出现新证据或真实 P0 时再进入专项处理。

> [!important] 当前停点
> `QH-03-QA-HARDEN` 已关闭；当前最高优先级切换为 **`QH-04-REL-EVO`**，本轮只登记，不自动执行。
