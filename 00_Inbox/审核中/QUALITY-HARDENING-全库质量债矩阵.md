---
type: 质量债矩阵
subject: 系统架构设计师
status: quality_hardening_closed
stage: quality_hardening_closed
coverage_status: syllabus_build_complete
coverage_gate: PASS
start_head: 5eef91b26c7714e43529b84535d18ecd8ac26db1
current_priority: none
updated: 2026-09-17
tags: [软考/架构设计师, QUALITY-HARDENING, 质量债, 审核]
---

# QUALITY-HARDENING · 全库质量债矩阵

> [!success] QH-SEC-04 已定点收口
> 本矩阵只管理 QUALITY / REVIEW 债务，不重新做 coverage。信息安全文件完整性与零基础机制桥接已经过 04A～04D 修复和联合验收；既有 coverage PASS 继续有效。

## 1. 当前结论

- coverage regression candidate：**0**
- 当前计划内开放质量债：**P0 = 0 / P1 = 0 / P2 = 0 / 合计 = 0**
- 已收口质量债：**QH-SEC-001、QH-SEC-04、QH-02-001、QH-05-001、QH-05-002、QH-07-001、QH-07-002、QH-08-001、QH-09-001、QH-10-001、QH-11-001、QH-12-001**
- `QH-13-001`：**`out_of_scope_by_user / no_action_required`**，不计入开放债，也不伪装成“已修复关闭”
- 当前质量控制状态：`quality_hardening_closed / normal_maintenance`
- 当前下一批：**无 QUALITY 债务**。仓库主计划恢复 `ARCH-01-IS-BUILD`。

## 2. 最终章节质量状态

| 章 | coverage 状态 | quality/review 状态 | 开放债 | 说明 |
| ---: | --- | --- | ---: | --- |
| 02 信息系统基础知识 | 30/30 covered | review_closed / normal_maintenance | 0 | `QH-02-001` 已关闭 |
| 03 信息安全技术 | coverage_complete | security_quality_closed / normal_maintenance | 0 | QH-SEC-00/01/02/03/04 已收口 |

### QH-SEC-04：网络通信及后续章节零基础质量修复

| 子任务 | 状态 | 验收重点 |
| --- | --- | --- |
| QH-SEC-04A-INTEGRITY | closed | 清除 2 个冲突文件并让检查脚本拦截冲突标记 |
| QH-SEC-04B-SAMPLE | closed | VPN 机制样稿通过并锁定批量写法 |
| QH-SEC-04C-BATCH | closed | IDS/IPS、TLS、OSI 服务、可信计算/零信任顺序及必要缩写桥接完成 |
| QH-SEC-04D-ACCEPTANCE | closed | 27 个 Markdown 联合验收、导航同步及仓库校验通过 |

本项是已完成 coverage 上的新质量证据，不推翻 QH-SEC-00/01/02/03 的历史工作。
| 04 软件工程基础知识 | 44 covered + 1 legal link_only | 已有完整审查链 | 0 | 后置维护 |
| 05 数据库设计基础知识 | 33 covered + 1 legal link_only | quality_hardened / normal_maintenance | 0 | QH-05 已关闭 |
| 06 软件架构设计 | 32 covered + 2 legal link_only | third_round_complete | 0 | 后置维护 |
| 07 系统质量属性与架构评估 | 29/29 covered | quality_hardened / normal_maintenance | 0 | QH-07 已关闭 |
| 08 软件可靠性技术 | 15/15 covered | quality_hardened / normal_maintenance | 0 | QH-08 已关闭 |
| 09 软件架构的演化和维护 | 16/16 covered | quality_hardened / normal_maintenance | 0 | QH-09 已关闭 |
| 10 未来信息综合技术 | 13/13 covered | quality_hardened / normal_maintenance | 0 | QH-10 已关闭 |
| 11 标准化与知识产权 | 15/15 covered | quality_hardened / normal_maintenance | 0 | QH-11 已关闭 |
| 12 应用数学 | 16/16 covered | **quality_hardened / normal_maintenance** | 0 | `QH-12-001` 已关闭 |
| 13 专业英语 | 历史 15/15 covered | **out_of_future_plan_by_user** | 0 | 不进入后续施工 |

## 3. QH-06-MATH 收口记录

### QH-12-001

原问题：`01_综合知识/12_应用数学/应用数学-学习路线.md` 仍把已经退出后续施工计划的 13 专业英语写成强制下一站。

本轮动作：

- 保持 12 应用数学既有 `16/16 covered`，不重开 coverage；
- 将学习路线 `quality_status` 从 `quality_pending` 改为 `quality_hardened`；
- 按“改动即待复习”补 `review_status: 待复习`；
- 删除 12→13 的强制施工导航，改成“本章收口 → 综合知识复习与错题循环”；
- 增加本章最后一次自检：先识别模型与第一动作，再进入计算；
- 未修改 13 专业英语任何正文、路线、索引或速记。

复查结论：导航与用户当前范围一致，`QH-12-001 = CLOSED`，不涉及 coverage 回退。

## 4. coverage 回归检查

历史 coverage 事实继续冻结：没有 stable Atom 主事实源消失，没有新增 `partial / unmapped / blocked`，没有 legal link_only 目标失效，也没有删除大纲有效范围正文。

13 被排除的是**后续施工范围**，不是删除历史内容，因此不会触发 coverage regression。

结论：**`coverage_regression_candidate = 0`。**

## 5. QUALITY-HARDENING 最终判定

计划内开放质量债重新统计：

| 严重度 | 数量 |
| --- | ---: |
| P0 | 0 |
| P1 | 0 |
| P2 | 0 |
| **合计** | **0** |

因此 QUALITY-HARDENING 恢复：

> **`quality_hardening_closed / normal_maintenance`**

后续原则：

1. 03～12 只在出现真实新证据、真实质量问题或用户明确学习反馈时定点维护；
2. 13 专业英语继续保持 `out_of_future_plan_by_user`，禁止自动任务重新纳入；
3. 不因为 QUALITY 已收口而自动制造 G5/G6/G7 施工；后续大阶段等待用户明确启动。
