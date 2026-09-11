---
type: 覆盖母表
subject: 系统架构设计师
status: syllabus_build_complete
scope: 综合知识-官方大纲1到13
source: 官方教材/系统架构第二版 大纲.pdf
updated: 2026-09-11
baseline_commit: ff6c26677b6bda34006e807f46b0ae1eabf2390d
last_batch: G4-COVERAGE-FINAL-RERUN
current_phase: QUALITY-HARDENING-READY
tags: [软考/架构设计师, 审查/大纲覆盖, 审查/全库补全]
---

# 全库综合知识大纲 Atom 母表

> [!success] 大纲建设阶段已完成
> `SYL-*` 继续作为 01～13 的全局范围键，不替代各知识域自己的稳定 Atom ID。当前 FINAL RERUN 已通过：**01 用户接受并跳过顶层技术覆盖审计；02～13 technical coverage 全部满足。**

## 一、当前全局结论

- 01：`study_complete / user_accepted / coverage_audit_skipped`，不计 technical coverage_complete，也不再阻塞；
- 02：30/30 covered；剩余 review debt 进入 QUALITY/REVIEW；
- 03：34 张原子卡联合审查通过；
- 04：45 = 44 covered + 1 legal link_only；
- 05：34 = 33 covered + 1 legal link_only；
- 06：34 = 32 covered + 2 legal link_only；
- 07：29/29 covered；
- 08～13：90/90 covered；
- 02～13 合计：296 coverage satisfied = 292 covered + 4 legal link_only，`partial/unmapped/blocked=0`；
- 当前阶段：**`syllabus_build_complete / quality_hardening_next`**。

## 二、全局一级范围母表

| Scope Key | 官方大纲范围 | 当前仓库主承接 | 当前控制状态 | 下一阶段 |
| --- | --- | --- | --- | --- |
| SYL-01 | 1 计算机系统基本知识 | `01_综合知识/01_计算机系统基础知识/` | **`study_complete / user_accepted / coverage_audit_skipped`** | 正常维护 |
| SYL-02 | 2 信息系统基础知识 | `01_综合知识/02_信息系统基础知识/` | `coverage_complete / review_pending`；30/30 | QUALITY/REVIEW |
| SYL-03 | 3 信息安全技术基础知识 | `01_综合知识/03_信息安全技术/` | `coverage_complete / review_complete` | QUALITY-HARDENING 按需 |
| SYL-04 | 4 软件工程基础知识 | `01_综合知识/04_软件工程基础知识/` | `coverage_complete / third_round_complete`；45=44+1 link_only | QUALITY-HARDENING 按需 |
| SYL-05 | 5 数据库设计基础知识 | `01_综合知识/05_数据库设计基础知识/` | `coverage_complete / quality_pending`；34=33+1 link_only | QUALITY-HARDENING |
| SYL-06 | 6 系统架构设计基础知识 | `01_综合知识/06_软件架构设计/` | `coverage_complete / third_round_complete`；34=32+2 link_only | QUALITY-HARDENING 按需 |
| SYL-07 | 7 系统质量属性与架构评估 | `01_综合知识/07_系统质量属性与架构评估/` | `coverage_complete / quality_pending`；29/29 | QUALITY-HARDENING |
| SYL-08 | 8 软件可靠性技术 | `01_综合知识/08_软件可靠性技术/` | `coverage_complete / quality_pending`；15/15 | QUALITY-HARDENING |
| SYL-09 | 9 软件架构的演化和维护 | `01_综合知识/09_软件架构的演化和维护/` | `coverage_complete / quality_pending`；16/16 | QUALITY-HARDENING |
| SYL-10 | 10 未来信息综合技术 | `01_综合知识/10_未来信息综合技术/` | `coverage_complete / quality_pending`；13/13 | QUALITY-HARDENING |
| SYL-11 | 11 标准化与知识产权 | `01_综合知识/11_标准化与知识产权/` | `coverage_complete / quality_pending`；15/15 | QUALITY-HARDENING |
| SYL-12 | 12 应用数学 | `01_综合知识/12_应用数学/` | `coverage_complete / quality_pending`；16/16 | QUALITY-HARDENING |
| SYL-13 | 13 专业英语 | `01_综合知识/13_专业英语/` | `coverage_complete / quality_pending`；15/15 | QUALITY-HARDENING |

## 三、01 范围键保留但 coverage 工程永久停止

| Scope Key | 大纲子范围 | 当前处理口径 |
| --- | --- | --- |
| SYL-01.1 | 计算机系统概述 | 用户已完成学习；正常维护 |
| SYL-01.2 | 计算机硬件 | 用户已完成学习；正常维护 |
| SYL-01.3 | 计算机软件 | 用户已完成学习；正常维护 |
| SYL-01.4 | 嵌入式系统及软件 | 用户已完成学习；正常维护 |
| SYL-01.5 | 计算机网络 | 用户已完成学习；正常维护 |
| SYL-01.6 | 计算机语言 | 用户已完成学习；正常维护 |
| SYL-01.7 | 多媒体 | 用户已完成学习；正常维护 |
| SYL-01.8 | 系统工程 | 用户已完成学习；正常维护 |
| SYL-01.9 | 系统性能 | 用户已完成学习；正常维护 |

> 保留这些范围键仅用于导航、历史和学习结构。`G3-CS-CONTRACT` 已取消，不得因后续质量任务重新触发。

## 四、02～07 稳定事实

| 范围 | stable / 等价分母 | covered | link_only | partial | unmapped | blocked |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| SYL-02 | 30 | 30 | 0 | 0 | 0 | 0 |
| SYL-03 | 34 | 34 | 0 | 0 | 0 | 0 |
| SYL-04 | 45 | 44 | 1 | 0 | 0 | 0 |
| SYL-05 | 34 | 33 | 1 | 0 | 0 | 0 |
| SYL-06 | 34 | 32 | 2 | 0 | 0 | 0 |
| SYL-07 | 29 | 29 | 0 | 0 | 0 | 0 |

07 命名空间保持 `QA-A001 ~ QA-A029`；数据库保持 `DB-A001 ~ DB-A034`；软件工程和软件架构保持既有稳定 ID，不因 FINAL RERUN 改号。

## 五、08～13 稳定 Atom 合流

| 命名空间 | 范围 | 总数 | P0 | P1 | P2 | covered | partial | unmapped | link_only | blocked |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `REL-Axxx` | A001～A015 | 15 | 4 | 9 | 2 | 15 | 0 | 0 | 0 | 0 |
| `EVO-Axxx` | A001～A016 | 16 | 5 | 10 | 1 | 16 | 0 | 0 | 0 | 0 |
| `FUT-Axxx` | A001～A013 | 13 | 5 | 7 | 1 | 13 | 0 | 0 | 0 | 0 |
| `IPR-Axxx` | A001～A015 | 15 | 6 | 7 | 2 | 15 | 0 | 0 | 0 | 0 |
| `MATH-Axxx` | A001～A016 | 16 | 9 | 7 | 0 | 16 | 0 | 0 | 0 | 0 |
| `ENG-Axxx` | A001～A015 | 15 | 9 | 4 | 2 | 15 | 0 | 0 | 0 | 0 |
| **合计** |  | **90** | **38** | **44** | **8** | **90** | **0** | **0** | **0** | **0** |

## 六、合法跨域主事实源

04、05、06 中的 4 个 legal link_only 保持合法，不为追求“全 covered”复制第二套正文。01 内既有子域的历史 link_only 继续服务正常学习维护，但不参与已跳过的 01 顶层 coverage audit。

## 七、最终门禁与下一站

`G4-COVERAGE-FINAL-RERUN`：**PASS**。

完整证据见 [[综合知识01-13-G4-COVERAGE-FINAL-RERUN统一验收记录]]。

> **下一阶段：`QUALITY-HARDENING`。**

本轮不自行启动下一阶段。
