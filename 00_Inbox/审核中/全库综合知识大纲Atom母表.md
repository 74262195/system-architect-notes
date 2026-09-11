---
type: 覆盖母表
subject: 系统架构设计师
status: 全局范围控制中
scope: 综合知识-官方大纲1到13
source: 官方教材/系统架构第二版 大纲.pdf
updated: 2026-09-11
baseline_commit: 9af6c32ed489ce1119ff3e4a0c94057f2dab4056
last_batch: G3-QA-CONTRACT
current_phase: G4-FINAL-RERUN-READY
tags: [软考/架构设计师, 审查/大纲覆盖, 审查/全库补全]
---

# 全库综合知识大纲 Atom 母表

> [!important] `SYL-*` 是全局范围键，不是章节稳定 Atom ID
> 本表保证官方综合知识 1～13 不从仓库范围控制中消失。01 的范围键继续保留，但用户已明确跳过顶层覆盖工程；这不等于把 01 技术性验收成 coverage_complete。

## 一、当前全局结论

- `G4-08-BUILD ~ G4-13-BUILD` 已完成首次建设，08～13 共 90 stable / 90 covered。
- `G3-DB-CLOSE` 已关闭 05 数据库阻断：34/34 coverage satisfied = 33 covered + 1 合法 link_only。
- 01 当前状态统一为 **`study_complete / user_accepted / coverage_audit_skipped`**；`G3-CS-CONTRACT` 已取消，01 不再阻断。
- `G3-QA-CONTRACT` 已建立 07 稳定契约：**29 stable = 29 covered；P0=16、P1=12、P2=1；p/u/l/b=0**。
- 当前没有已知 coverage 硬缺口，下一批是 `G4-COVERAGE-FINAL-RERUN`；在该门禁重跑前不提前宣告全库最终通过。

## 二、全局一级范围母表

| Scope Key | 官方大纲范围 | 当前仓库主承接 | 当前控制状态 | 当前动作 |
| --- | --- | --- | --- | --- |
| SYL-01 | 1 计算机系统基本知识 | `01_综合知识/01_计算机系统基础知识/` | **`study_complete / user_accepted / coverage_audit_skipped`** | 正常维护；不再进入 coverage backlog |
| SYL-02 | 2 信息系统基础知识 | `01_综合知识/02_信息系统基础知识/` | `coverage_complete / review_pending`；30/30 | REVIEW/QUALITY 队列 |
| SYL-03 | 3 信息安全技术基础知识 | `01_综合知识/03_信息安全技术/` | `coverage_complete / review_complete`；34 张原子卡三轮通过 | 正常维护 |
| SYL-04 | 4 软件工程基础知识 | `01_综合知识/04_软件工程基础知识/` | `coverage_complete / third_round_complete`；45=44 covered+1 link_only | 正常维护 |
| SYL-05 | 5 数据库设计基础知识 | `01_综合知识/05_数据库设计基础知识/` | `coverage_complete / quality_pending`；34=33 covered+1 link_only | 正常维护 |
| SYL-06 | 6 系统架构设计基础知识 | `01_综合知识/06_软件架构设计/` | `coverage_complete / third_round_complete`；34=32 covered+2 link_only | 保持唯一主源 |
| SYL-07 | 7 系统质量属性与架构评估 | `01_综合知识/07_系统质量属性与架构评估/` | **`coverage_complete / quality_pending`；29/29 covered** | `G4-COVERAGE-FINAL-RERUN` |
| SYL-08 | 8 软件可靠性技术 | `01_综合知识/08_软件可靠性技术/` | `coverage_complete / quality_pending`；15/15 | QUALITY-HARDENING |
| SYL-09 | 9 软件架构的演化和维护 | `01_综合知识/09_软件架构的演化和维护/` | `coverage_complete / quality_pending`；16/16 | QUALITY-HARDENING |
| SYL-10 | 10 未来信息综合技术 | `01_综合知识/10_未来信息综合技术/` | `coverage_complete / quality_pending`；13/13 | QUALITY-HARDENING |
| SYL-11 | 11 标准化与知识产权 | `01_综合知识/11_标准化与知识产权/` | `coverage_complete / quality_pending`；15/15 | QUALITY-HARDENING |
| SYL-12 | 12 应用数学 | `01_综合知识/12_应用数学/` | `coverage_complete / quality_pending`；16/16 | QUALITY-HARDENING |
| SYL-13 | 13 专业英语 | `01_综合知识/13_专业英语/` | `coverage_complete / quality_pending`；15/15 | QUALITY-HARDENING |

## 三、01 范围键保留但停止顶层 coverage 工程

以下 `SYL-01.*` 继续作为历史范围导航，不再触发 `G3-CS-CONTRACT`：

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

> 这里保留范围键只为导航与历史一致性；**不再拆 Atom、不再做顶层联合覆盖验收，也不把状态伪写成 coverage_complete。**

## 四、02～07 范围控制

- SYL-02：30/30 covered；剩余任务是 review/quality。
- SYL-03：34 张原子卡已完成三轮审查。
- SYL-04：45 stable，44 covered + 1 合法 link_only。
- SYL-05：34 stable，33 covered + 1 合法 link_only；p/u/b=0。
- SYL-06：34 stable，32 covered + 2 合法 link_only；p/u=0。
- SYL-07：`QA-A001 ~ QA-A029`，29 stable = 29 covered；p/u/l/b=0；官方 7.1～7.3 已建立稳定主事实源。

### 07 稳定契约汇总

| 命名空间 | 范围 | 总数 | P0 | P1 | P2 | covered | partial | unmapped | link_only | blocked |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `QA-Axxx` | A001～A029 | **29** | **16** | **12** | **1** | **29** | **0** | **0** | **0** | **0** |

具体映射见 [[系统质量属性与架构评估-G3-QA-CONTRACT收口记录]]。

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

## 六、软件三知识域稳定契约保留

| 稳定命名空间 | 范围 | 总数 | covered | partial | unmapped | link_only |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| `CS-SW-Axxx` | A001～A022 | 22 | 14 | 0 | 0 | 8 |
| `SE-Axxx` | A001～A045 | 45 | 44 | 0 | 0 | 1 |
| `ARCH-Axxx` | A001～A034 | 34 | 32 | 0 | 0 | 2 |

这些 `link_only` 为合法跨域唯一主事实源，不因后续批次复制正文。

## 七、当前停点

> **`G3-QA-CONTRACT` 已完成；`G3-CS-CONTRACT` 已由用户取消。下一批固定 `G4-COVERAGE-FINAL-RERUN`。**