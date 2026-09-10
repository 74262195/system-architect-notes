---
type: 覆盖母表
subject: 系统架构设计师
status: 全局范围控制中
scope: 综合知识-官方大纲1到13
source: 官方教材/系统架构第二版 大纲.pdf
updated: 2026-09-10
baseline_commit: 941f9a16e3ac1b020e63c9120baf1b167095a813
last_batch: G3-DB-CLOSE
current_phase: G3-EXISTING-GAP
tags: [软考/架构设计师, 审查/大纲覆盖, 审查/全库补全]
---

# 全库综合知识大纲 Atom 母表

> [!important] `SYL-*` 是全局范围键，不是章节稳定 Atom ID
> 本表保证官方综合知识 1～13 不从施工范围中消失。具体覆盖状态必须由对应知识域稳定 Atom 契约或章节联合验收证明；不存在当前稳定分母时不猜数字。

## 一、当前全局结论

- `G4-08-BUILD ~ G4-13-BUILD` 已全部完成首次建设。
- 08～13 共 **90 个稳定 Atom，90 covered，partial/unmapped/link_only/blocked 均为 0**。
- `G3-DB-CLOSE` 已关闭 05 数据库覆盖阻断：**34/34 coverage satisfied = 33 covered + 1 合法 link_only；partial/unmapped/blocked=0**。
- 01～13 全局覆盖门禁 **仍未通过**：01、07 尚缺当前顶层稳定联合契约。
- 当前阶段继续为 `G3-EXISTING-GAP`，下一批固定 `G3-CS-CONTRACT`。

## 二、全局一级范围母表

| Scope Key | 官方大纲范围 | 当前仓库主承接 | 当前控制状态 | 当前动作 |
| --- | --- | --- | --- | --- |
| SYL-01 | 1 计算机系统基本知识 | `01_综合知识/01_计算机系统基础知识/` | `contract_pending / mixed` | **`G3-CS-CONTRACT`** |
| SYL-02 | 2 信息系统基础知识 | `01_综合知识/02_信息系统基础知识/` | `coverage_complete / review_pending`；30/30 | 继续 review，不回退 coverage |
| SYL-03 | 3 信息安全技术基础知识 | `01_综合知识/03_信息安全技术/` | `coverage_complete / review_complete`；34 张原子卡三轮通过 | 正常维护 |
| SYL-04 | 4 软件工程基础知识 | `01_综合知识/04_软件工程基础知识/` | `coverage_complete / third_round_complete`；45=44 covered+1 合法 link_only | 共享 FINAL 后置 |
| SYL-05 | 5 数据库设计基础知识 | `01_综合知识/05_数据库设计基础知识/` | **`coverage_complete / quality_pending`；34=33 covered+1 合法 link_only；p/u/b=0** | 正常维护；见 `G3-DB-CLOSE` |
| SYL-06 | 6 系统架构设计基础知识 | `01_综合知识/06_软件架构设计/` | `coverage_complete / third_round_complete`；34=32 covered+2 合法 link_only | 保持唯一主源 |
| SYL-07 | 7 系统质量属性与架构评估 | `01_综合知识/07_系统质量属性与架构评估/` | `contract_pending` | `G3-QA-CONTRACT` |
| SYL-08 | 8 软件可靠性技术 | `01_综合知识/08_软件可靠性技术/` | `coverage_complete / quality_pending`；15/15 | QUALITY-HARDENING |
| SYL-09 | 9 软件架构的演化和维护 | `01_综合知识/09_软件架构的演化和维护/` | `coverage_complete / quality_pending`；16/16 | QUALITY-HARDENING |
| SYL-10 | 10 未来信息综合技术 | `01_综合知识/10_未来信息综合技术/` | `coverage_complete / quality_pending`；13/13 | QUALITY-HARDENING |
| SYL-11 | 11 标准化与知识产权 | `01_综合知识/11_标准化与知识产权/` | `coverage_complete / quality_pending`；15/15 | QUALITY-HARDENING |
| SYL-12 | 12 应用数学 | `01_综合知识/12_应用数学/` | `coverage_complete / quality_pending`；16/16 | QUALITY-HARDENING |
| SYL-13 | 13 专业英语 | `01_综合知识/13_专业英语/` | `coverage_complete / quality_pending`；15/15 | QUALITY-HARDENING |

## 三、01 计算机系统基本知识范围键

01 顶层稳定分母尚未锁定，以下 `SYL-*` 只控制范围，不宣告 Atom 计数：

| Scope Key | 大纲子范围 | 当前主承接候选 | 当前状态/动作 |
| --- | --- | --- | --- |
| SYL-01.1 | 计算机系统概述 | 组成与体系结构等现有主源 | `G3-CS-CONTRACT` 统一核验 |
| SYL-01.2 | 计算机硬件 | `01_计算机组成与体系结构/` | 已有正文，待稳定映射 |
| SYL-01.3 | 计算机软件 | OS、软件与语言等现有主源 | 跨模块裁决唯一主源 |
| SYL-01.4 | 嵌入式系统及软件 | 当前承接待统一核验 | 建稳定映射 |
| SYL-01.5 | 计算机网络 | `03_计算机网络/` | 已有正文，待顶层契约合流 |
| SYL-01.6 | 计算机语言 | `04_计算机软件与语言/` | 22 stable；14 covered+8 合法 link_only；p/u=0 |
| SYL-01.7 | 多媒体 | `05_多媒体/` | 旧完成，顶层合流时迁移复核 |
| SYL-01.8 | 系统工程 | `06_系统工程/` | 已有迁移审计成果，顶层合流时复用 |
| SYL-01.9 | 系统性能 | 可能跨组成/OS/网络等 | 先定唯一主源再判覆盖 |

## 四、02～07 范围控制

- SYL-02：当前稳定契约 30/30 covered；所有 p/u/l=0；剩余任务是质量审查。
- SYL-03：34 张原子卡已完成范围、机制边界、可用性三轮审查。
- SYL-04：45 stable，44 covered + 1 合法 link_only；p/u=0。
- SYL-05：**34 stable，33 covered + 1 合法 link_only；partial/unmapped/blocked=0；数据库覆盖联合验收已通过。** `DB-A032` 唯一完整主事实源为软件工程 `SE-A031` → [[对象持久化与ORM]]。
- SYL-06：34 stable，32 covered + 2 合法 link_only；p/u=0。
- SYL-07：7.1 软件系统质量属性、7.2 系统架构评估、7.3 ATAM 方法架构评估实践均有正文候选，但当前顶层稳定联合契约待建立。

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

11、12、13 的稳定拆分分别由各章施工蓝图中的 `IPR-A001～A015`、`MATH-A001～A016`、`ENG-A001～A015` 承担；不再保留“顶层缺失候选”。

## 六、软件三知识域稳定契约保留

| 稳定命名空间 | 范围 | 总数 | covered | partial | unmapped | link_only |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| `CS-SW-Axxx` | A001～A022 | 22 | 14 | 0 | 0 | 8 |
| `SE-Axxx` | A001～A045 | 45 | 44 | 0 | 0 | 1 |
| `ARCH-Axxx` | A001～A034 | 34 | 32 | 0 | 0 | 2 |
| **合计** |  | **101** | **90** | **0** | **0** | **11** |

这些 `link_only` 为合法跨域唯一主事实源，不因后续批次改号或复制正文。数据库 A032 正是复用已有 `SE-A031` 主事实源，因此不新造第二篇完整 ORM 正文。

## 七、当前停点

`G3-DB-CLOSE` 已完成，05 不再阻断全局 coverage。

> **当前唯一覆盖阶段仍为 `G3-EXISTING-GAP`；下一批固定 `G3-CS-CONTRACT`，随后 `G3-QA-CONTRACT`。01、07 两个顶层稳定契约完成并清零真实缺口后，才允许重跑 `G4-COVERAGE-FINAL-RERUN`。**

G4 历史验收见 [[综合知识01-13-G4-COVERAGE-FINAL统一验收记录]]；数据库最新验收见 [[数据库设计基础知识-G3-DB-CLOSE收口记录]]。
