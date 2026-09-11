---
type: 质量债矩阵
subject: 系统架构设计师
status: debt_matrix_locked
stage: quality_hardening_in_progress
coverage_status: syllabus_build_complete
coverage_gate: PASS
start_head: cc83f997202a64288bafc198afbc13f057fd1177
current_priority: QH-02-DB-HARDEN
updated: 2026-09-11
tags: [软考/架构设计师, QUALITY-HARDENING, 质量债, 审核]
---

# QUALITY-HARDENING · 全库质量债矩阵

> [!important] 阶段边界
> 本矩阵只管理 **QUALITY / REVIEW** 债务，不重新做 coverage。`G4-COVERAGE-FINAL-RERUN` 的 `PASS` 继续有效；01 继续保持 `study_complete / user_accepted / coverage_audit_skipped`；04/05/06 共 4 个 legal `link_only` 保持不变。

## 1. 当前结论

- coverage regression candidate：**0**
- 当前开放质量债：**P0 = 0 / P1 = 8 / P2 = 2**
- 已收口质量债：**QH-SEC-001（P1）、QH-02-001（P1）**
- 当前质量控制状态：`quality_hardening_in_progress / debt_matrix_locked`
- 当前下一批：**`QH-02-DB-HARDEN`**（尚未执行）
- 02 信息系统基础知识：**30/30 covered / review_closed / normal_maintenance**。
- `QH-SEC-00 / 01 / 02 / 03` 已完成信息安全专项教学连续性增强；信息安全专项 QUALITY 插队结束，不得因为“还能润色”自动制造 `QH-SEC-04`。

## 2. 等级口径

- **P0**：事实/教材错误、stable 主事实源失效、真正导航断裂、关键机制缺失到可能直接导致考试选错。
- **P1**：明显影响学习效率或考试判断，例如机制偏薄、关键易混边界不足、复习入口不同步、学习链有假断点、零基础入口缺少必要前因后果。
- **P2**：不阻塞学习的导航、措辞、排版和一致性优化。

> [!important] 用户优先级覆盖规则
> 严重度与施工优先级分离。用户正在实际学习的章节若出现明确学习阻塞，可获得 **USER-PRIORITY OVERRIDE**。任何插队都只处理具体、可复现的真实学习问题；不得借 quality 债重新打开已经 PASS 的 coverage。

## 3. 02～13 质量画像

| 章 | 当前 coverage 状态 | 当前 quality/review 状态 | P0 | P1 | P2 | 主要质量债 | 推荐批次 |
| ---: | --- | --- | ---: | ---: | ---: | --- | --- |
| 02 信息系统基础知识 | 30/30 covered | **review_closed / normal_maintenance** | 0 | 0 | 0 | `QH-02-001` 已关闭；索引与学习路线已对齐最终稳定事实 | 正常维护 |
| 03 信息安全技术 | coverage_complete | review_complete / teaching_entry_closed / crypto_chain_closed / network_chain_closed / app_governance_chain_closed / security_quality_insert_closed | 0 | 0 | 0 | QH-SEC-00/01/02/03 已收口入口、密码学、身份权限、网络通信、应用安全到安全架构治理主线；coverage 与既有事实主源保持不变 | 后置维护 |
| 04 软件工程基础知识 | 44 covered + 1 legal link_only | 已有完整审查链 | 0 | 0 | 0 | 未发现需插队的真实 P0；历史旧缺口不得复活 | 后置维护 |
| 05 数据库设计基础知识 | 33 covered + 1 legal link_only | quality_pending | 0 | 2 | 0 | 索引、学习路线仍残留“4 partial/尚未联合验收”的旧阶段描述 | QH-02-DB-HARDEN |
| 06 软件架构设计 | 32 covered + 2 legal link_only | third_round_complete | 0 | 0 | 0 | 最新第三轮/DSSA 专项收口未发现需重新打开的真实 P0 | 后置维护 |
| 07 系统质量属性与架构评估 | 29/29 covered | quality_pending | 0 | 2 | 0 | 索引仍停留在旧 14 张 P0 补齐口径；考前速记未同步 29-Atom 最终稳定契约中的若干新增高价值判断入口 | QH-03-QA-HARDEN |
| 08 软件可靠性技术 | 15/15 covered | quality_pending | 0 | 1 | 0 | 学习路线仍写“09 尚未建设”，形成施工期遗留假断点 | QH-04-REL-EVO |
| 09 软件架构的演化和维护 | 16/16 covered | quality_pending | 0 | 1 | 0 | 学习路线仍写“10 尚未建设”，形成施工期遗留假断点 | QH-04-REL-EVO |
| 10 未来信息综合技术 | 13/13 covered | quality_pending | 0 | 0 | 1 | 章末仍保留“下一大章若尚未建设”的条件式施工文案，未收口为已存在的 11 章物理导航 | QH-05-FUT-IPR |
| 11 标准化与知识产权 | 15/15 covered | quality_pending | 0 | 1 | 0 | 学习路线明确写“12_应用数学尚未真实存在”，与 12 已完成 16/16 coverage 的事实冲突 | QH-05-FUT-IPR |
| 12 应用数学 | 16/16 covered | quality_pending | 0 | 0 | 1 | 下一站语义正确指向 13，但仍缺已存在 13 章的物理 Wikilink，属于弱导航 | QH-06-MATH-ENG |
| 13 专业英语 | 15/15 covered | quality_pending | 0 | 1 | 0 | 章末仍把“后续 01～13 coverage 统一验收”写成下一动作，而 FINAL-RERUN 已 PASS | QH-06-MATH-ENG |

### 开放债务汇总

| 严重度 | 数量 |
| --- | ---: |
| P0 | 0 |
| P1 | 8 |
| P2 | 2 |
| **合计** | **10** |

## 4. 文件级开放质量债

| Debt ID | 章节 | 文件 | 问题 | 证据类型 | 严重度 | 推荐动作 | 是否涉及 coverage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| QH-05-001 | 05 | `01_综合知识/05_数据库设计基础知识/数据库设计基础知识索引.md` | `G3-DB-CLOSE` 已确认 34/34 coverage satisfied，但索引仍残留 4 partial/待收口口径 | 状态/导航陈旧 | P1 | QH-02 同步索引到最终 coverage 事实并转入 quality_pending | 否 |
| QH-05-002 | 05 | `01_综合知识/05_数据库设计基础知识/学习路线.md` | 学习路线仍保留 4 partial/尚未联合验收的施工期描述，可能误导学习和自动接力 | 学习链/阶段陈旧 | P1 | QH-02 仅同步学习路线和复习链，不重做 stable Atom | 否 |
| QH-07-001 | 07 | `01_综合知识/07_系统质量属性与架构评估/系统质量属性与架构评估索引.md` | 索引仍以“14 张 P0 原子卡补齐”为当前成功口径，未同步 `QA-A001~QA-A029` 的 29-Atom 最终稳定契约 | 契约入口不同步 | P1 | QH-03 将索引切到 29-Atom 最终事实，并保持唯一主事实源 | 否 |
| QH-07-002 | 07 | `01_综合知识/07_系统质量属性与架构评估/系统质量属性与架构评估-考前速记.md` | 当前速记仍以旧闭卷清单为核心，对最终契约新增/加强的功能性、可变性、互操作性以及 ATAM 阶段/步骤等高价值判断没有同等强度的 30～90 秒入口 | 快速复习/考试动作 | P1 | QH-03 精炼增补题眼与第一动作，不复制正文 | 否 |
| QH-08-001 | 08 | `01_综合知识/08_软件可靠性技术/学习路线.md` | 章末仍写“09 章当前尚未建设”，但 09 已完成 16/16 coverage | 跨章导航假断点 | P1 | QH-04 改为真实 08→09 Wikilink 与承接语义 | 否 |
| QH-09-001 | 09 | `01_综合知识/09_软件架构的演化和维护/学习路线.md` | 章末仍写“10 章尚未建设”，但 10 已完成 13/13 coverage | 跨章导航假断点 | P1 | QH-04 改为真实 09→10 Wikilink 与承接语义 | 否 |
| QH-10-001 | 10 | `01_综合知识/10_未来信息综合技术/未来信息综合技术-学习路线.md` | 章末仍保留“下一大章若尚未建设”的通用施工期措辞，11 已存在但没有形成明确物理下一站 | 跨章导航弱化 | P2 | QH-05 直接指向 11，并保留现有边界说明 | 否 |
| QH-11-001 | 11 | `01_综合知识/11_标准化与知识产权/标准化与知识产权-学习路线.md` | 明确写“12_应用数学尚未真实存在”，与 12 已完成 16/16 coverage 的事实冲突 | 跨章导航假断点 | P1 | QH-05 改为真实 11→12 Wikilink | 否 |
| QH-12-001 | 12 | `01_综合知识/12_应用数学/应用数学-学习路线.md` | 下一站语义正确指向 13，但未把已存在的 13 章做成物理 Wikilink | 跨章导航弱化 | P2 | QH-06 增加真实 12→13 入口 | 否 |
| QH-13-001 | 13 | `01_综合知识/13_专业英语/专业英语-学习路线.md` | 章末仍把“后续统一 coverage 验收”写成下一动作；该验收已经 FINAL-RERUN PASS | 阶段导航陈旧 | P1 | QH-06 改为综合知识末章收口 + QUALITY/复习入口，不复活 G4 | 否 |

### 已收口债务

| Debt ID | 章节 | 原问题 | 收口批次 | 结果 | coverage |
| --- | --- | --- | --- | --- | --- |
| QH-SEC-001 | 03 | 首次学习缺少从“系统已建成”到“为什么需要安全”的教学桥，以及资产/威胁/脆弱性/攻击/风险/目标/机制的统一主线 | `QH-SEC-00` | 新增开篇；重构索引与学习路线入口；后移治理；定点增强《信息安全基本目标》承接；建立统一网上办事系统场景 | 不回退，继续 PASS |
| QH-02-001 | 02 | 已是 30/30 covered，但索引仍把 G2-IS03 / G2-IS04-* / 三轮审查写成当前或固定下一动作 | `QH-01-IS-REVIEW-CLOSE` | 索引切换到最终稳定事实；旧 G2 降级为历史证据；学习路线与代表正文抽查通过；02 转为 `review_closed / normal_maintenance` | 不回退，继续 30/30 PASS |

## 5. coverage 回归检查

本轮未发现以下任一情况：

- stable Atom 主事实源消失；
- legal `link_only` 目标失效；
- 已标 covered 的正文完全缺少必要机制；
- 新的 `partial / unmapped / blocked`；
- 大纲有效范围被错误删除。

因此：**`coverage_regression_candidate = 0`，coverage gate 继续保持 PASS。**

QH-01 修改的是章节索引、review 状态和 QUALITY 控制面，不是 coverage 缺口；不得因此重新跑 02 coverage。

## 6. 代表性正文抽查与 QH-01 结论

- 02：[[MIS 管理信息系统]] 已具备功能—层次矩阵、机制、与 DSS 的边界和考试动作；无需修改。
- 02：[[DSS 支持决策系统]] 已明确半结构化/非结构化决策、两库结构、基于知识 DSS，以及与 MIS 的边界；无需修改。
- 02：[[企业信息化的概念]] 已明确企业信息化是过程/战略，信息系统是具体支撑系统；无需修改。
- 02：[[信息系统基础知识复习主线]] 已能承担正常学习导航，不存在旧 G2 固定施工路由；无需修改。
- 02：真实问题只落在 [[信息系统基础知识索引]] 的施工期阶段状态，因此本轮定点修复索引并关闭 `QH-02-001`。
- 03：QH-SEC-00/01/02/03 已收口，恢复正常维护。
- 05：DB/DBMS/DBS、关系代数代表正文未发现 P0；当前开放债务仍集中在 G3-DB-CLOSE 后入口状态未同步。
- 07：质量属性分类、ATAM 代表正文未发现 P0；当前开放债务仍集中在索引/速记与 29-Atom 契约不同步。
- 08～13：继续保持既有定点质量债，不因 QH-01 扩大范围。
- 04/06：只有出现新证据或真实 P0 才允许插队。

结论：

> **02 信息系统基础知识 review 正式收口，进入 `coverage_complete / review_closed / normal_maintenance`；不再制造 QH-01 连续批次。**

## 7. 后续施工路线

排序原则继续为：**用户当前学习阻塞 / 明确最新决策 → P0 → P1 考试影响 → review 状态 → 学习主线影响 → 批次可控性**。

1. **QH-02-DB-HARDEN**：05 数据库设计基础知识质量强化（下一批，尚未执行）。
2. **QH-03-QA-HARDEN**：07 系统质量属性与架构评估质量强化。
3. **QH-04-REL-EVO**：08 软件可靠性 + 09 软件架构演化维护。
4. **QH-05-FUT-IPR**：10 未来信息综合技术 + 11 标准化与知识产权。
5. **QH-06-MATH-ENG**：12 应用数学 + 13 专业英语。
6. **后置复核**：03 信息安全正常维护；04 / 06 仅在出现新证据或真实 P0 时插队。

> [!important] 当前停点
> `QH-01-IS-REVIEW-CLOSE` 已关闭；当前最高优先级切换为 `QH-02-DB-HARDEN`，但本轮禁止自动执行下一批。
