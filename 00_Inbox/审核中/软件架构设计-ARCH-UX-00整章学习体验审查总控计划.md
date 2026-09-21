---
type: 总控计划
subject: 系统架构设计师
chapter: 软件架构设计
topic: 整章学习体验审查与必要优化
task_id: ARCH-UX
status: active
current_batch: ARCH-UX-05-ACCEPT
last_completed: ARCH-UX-04-NAV
baseline_commit: 5630e6b455c7e91de7b29b795fcdceb7db5243a0
last_batch_start: 43199e99e59d60e36ff3bce67f12328ddf630f10
last_batch_commit: dfa7a4603625103f089d3f464d714177d187a969
historical_coverage: "34 = 32 covered + 2 legal link_only（ARCH-A005 / ARCH-A008）"
created: 2026-09-21
updated: 2026-09-21
tags:
  - 软考/架构设计师
  - 计划/软件架构设计
  - 质量/学习体验
---

# 软件架构设计 ARCH-UX 整章学习体验审查总控计划

> [!important] 任务范围
> 只处理 `01_综合知识/06_软件架构设计/`，不是根级 `06_架构设计理论与实践/`。历史 coverage 默认冻结：`ARCH-A001～ARCH-A034 = 32 covered + 2 legal link_only`。

## 审查目标

本轮标准不是“内容越完整越好”，而是**完成考试闭环后尽量短**。一篇只解决一个核心问题；优先删除重复定义、重复总结、多组同作用例和对第一次学习帮助很小的扩展。阅读时间继续执行 `prompts/00`：P0 通常 5～8 分钟，P1 3～5 分钟。

同时保持：总问题先于术语、前后站自然、概念层级清楚、唯一主事实源、不保留已失效的“未来建设 / 当前 partial / 尚未完成”描述。

## 当前事实

核心主线：

`软件架构是什么 → 生命周期 → 架构描述 → 4+1 多视图 → ABSD → 架构风格 → 架构复用 → DSSA → 质量属性与架构评估`

04 架构风格内部五类是**并列分类**，不是因果阶段：

`数据流 / 调用-返回 / 数据中心 / 虚拟机 / 独立构件`

coverage：`34 stable = 32 covered + 2 legal link_only + 0 partial + 0 unmapped`。

合法 link_only：`ARCH-A005 → UML用例图`；`ARCH-A008 → UML总览等 UML 主事实源`。

## 已确认问题

- 02 原先页尾上一站错误跳回 01，漏掉 01B；正文也明显超过完成 4+1 考试闭环所需长度。
- 03 原先写“前两张卡”，跳过 01A / 01B；同时六子过程逐阶段重复展开，P1 篇幅过重。
- 04A～04E 的顺序链接容易让零基础读者误解成五类风格有因果递进。
- 04B 仍写“未来 ARCH-LAY-A001 / ARCH-IS-A002”，但对应根级正文已经存在。
- 04E 仍写“未来 ARCH-CN-A010 / 当前 partial”，但根级事件驱动架构正文已经存在，旧状态失效。
- 索引仍残留 `SW-09C-FINAL 尚未开始` 历史施工状态。
- 07 / 08 是扩展骨架，不属于 ARCH-A001～A034；不擅自扩写，不让其干扰核心学习主线。

## 执行批次

| 批次 | 范围 | 状态 / 目标 |
| --- | --- | --- |
| ARCH-UX-00-AUDIT | 整章扫描 | 已完成 |
| ARCH-UX-01-FOUNDATION | 01 / 01A / 01B / 02 / 03 | **已完成**：01～01B 无真实问题不机械改；02、03完成主线修复和减负 |
| **ARCH-UX-02-STYLE** | 04 + 04A～04E | **当前**：明确五类并列关系；继续按“考试闭环后尽量短”审查；修复 04B / 04E 过时跨章状态 |
| ARCH-UX-03-REUSE-DSSA | 05 / 06 | 复核“风格 → 复用 → DSSA → 质量属性评估”，并检查是否存在胖卡；无问题不改 |
| ARCH-UX-04-NAV | 软件架构设计索引 | **已完成**：学习入口减负、清理历史施工状态、统一核心主线与扩展骨架边界 |
| **ARCH-UX-05-ACCEPT** | 全章 | **当前批次**：一次联合验收 |

## ARCH-UX-01 执行记录

START_HEAD：`43199e99e59d60e36ff3bce67f12328ddf630f10`。

- 01 / 01A / 01B：抽查后保持原文，避免为了统一格式机械重写。
- 02：压缩重复的逐视图解释、贯穿例子、重复总结与 5 道自测；保留 4+1 定位、四视图职责、+1 机制、关键边界、真题动作和 Mermaid；修正直接上一站为 01B；设置 `review_status: 待复习`。提交 `114072317e984a70bf1c72fe00aac9375b0f0f17`。
- 03：把原先逐阶段长篇展开压成“一张六子过程表 + 一个贯穿例子 + 反馈机制 + 两个易混边界”；恢复 01 → 01A → 01B → 02 的真实承接；保留三个基础、六子过程、考试动作与证据；设置 `review_status: 待复习`。提交 `f3bcfe88a6899cd2a4b9cf8a60e6b5788d4c57a0`。
- Atom / coverage：无变化，仍为 `34 = 32 covered + 2 legal link_only`。
- 导航：02 → 03、03 → 04 已同步；未新增主事实源。
- 并发：START_HEAD 后未发现外部并发提交；本批次 HEAD 变化来自本批次自身写入。
- `node scripts/check-vault.mjs`、`git diff --check`：当前连接器环境无法执行，明确记为**未执行**。


## ARCH-UX-04 执行记录

START_HEAD：`b3344d42fe8083598bfaa7f936c022d79cbe1d0d`。

- [[软件架构设计索引]] 从约 5913 字符 / 145 行缩减为约 2674 字符 / 105 行，删除历史 SW-09C 施工状态、逐卡旧审查记录和重复控制面信息。
- 索引现在只承担学习入口职责：第一次学习主线、每站主问题、04A～04E 并列关系、三组易混边界、扩展骨架边界、考试第一动作与证据入口。
- 核心下一站明确为 [[01_综合知识/07_系统质量属性与架构评估/系统质量属性与架构评估索引|系统质量属性与架构评估]]；07/08 明确为可跳过的扩展骨架。
- UML / Use Case 与根级架构理论继续保持唯一主事实源，不复制第二套正文。
- Atom / coverage：无变化，仍为 `34 = 32 covered + 2 legal link_only + 0 partial + 0 unmapped`。
- 修改索引保持 `review_status: 待复习`。
- 检查：当前 GitHub 连接器无本地工作树，`node scripts/check-vault.mjs` 与 `git diff --check` 未执行；已做远端回读，不把回读冒充本地检查通过。
- 本批正文提交：`dfa7a4603625103f089d3f464d714177d187a969`。

## 执行规则

每轮从远端最新 `main` 记录 START_HEAD，重读 `AGENTS.md`、任务路由 prompts、本计划、目标正文及直接前后站。写入前再次核对 HEAD；外部并发时基于新正文重建。修改学习正文必须 `review_status: 待复习`。跨章已有完整主事实源时只定位 + wikilink，不复制第二套正文。需要图时只用 Mermaid/Excalidraw，禁止 ASCII/TXT 伪图。

## 退出条件

核心学习链无断站；五类风格不会被误读成因果阶段；不再有失效建设状态；唯一主事实源边界不变；改动正文均待复习；完成一次联合验收；若无事实缺口，coverage 保持 `34 = 32 covered + 2 legal link_only`。完成后恢复运行时最新 [[全库补全总控计划]] 的 `current_priority`。
