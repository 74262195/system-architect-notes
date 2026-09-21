---
type: 总控计划
subject: 系统架构设计师
chapter: 软件工程基础知识
topic: 整章学习体验重构
task_id: SE-UX
status: active
current_batch: SE-UX-09-NAV
last_completed: SE-UX-08-PM
last_batch_commit: cf9ad2121b25764903df091261d79398e697e366
baseline_commit: 5e45340707ea3a97d4e79f5ff874a458f95e79bc
sample_note: "[[软件工程的定位]]"
historical_coverage: "45 = 44 covered + 1 legal link_only（SE-A009）"
created: 2026-09-21
updated: 2026-09-21
tags:
  - 软考/架构设计师
  - 计划/软件工程
  - 质量/学习体验
---

# 软件工程 SE-UX 整章学习体验重构总控计划

> [!important] 本任务性质
> 以 [[软件工程的定位]] 为零基础学习样例，把“04_软件工程基础知识”从一组正确考点卡提升为一条能顺着学下去的知识链。
>
> **这不是重新做 coverage，也不是重新生成 45 个 Atom。** 历史事实继续保留：`SE-A001–SE-A045 = 44 covered + 1 legal link_only（SE-A009）`。只有按“大纲 → 可靠真题 → 主教材 → 当前正文”核验确认原正文达不到最小考试闭环时，才允许真实退回 `partial`。

## 一、样例门槛

每篇按内容自然组织，但至少检查：承接定位、具体问题、大白话直接答案、机制与概念层级、易混边界、考试第一动作、高价值自测、自然下一站。

固定门禁：

- 快速复习卡默认 `[!summary]-`，只负责学完后的召回；
- 修改学习正文后 `review_status: 待复习`；
- 需要流程/层次图时使用 Mermaid，禁止 TXT/ASCII 伪图；
- 同一事实只保留一个完整主事实源；跨章内容使用合法 `link_only`；
- RUP 4+1 在软件工程章继续 legal link_only，完整主事实源在软件架构章；
- 不为格式统一机械重写已经达到样例标准且没有真实问题的正文。

## 二、固定学习主链

### A. 软件过程

`软件工程定位 → 瀑布 → 迭代/增量 → 螺旋 → 原型 → 构件组装 → RUP → 敏捷方法 → CMMI`

### B. 需求工程

`需求层次 → 需求开发/管理总览 → 获取 → 规格与确认验证 → 变更控制 → 双向追踪`

核心是两条线：先把需求弄清楚，再把已经形成的需求长期管住。

### C. 分析与设计

`结构化方法总览 → DFD/数据字典 → 模块设计（信息隐藏/内聚/耦合）→ 详细设计工具 → 面向对象总览 → OOA → OOD → UML → 实体/边界/控制 → OOP → 持久化 → 逆向工程/形式化方法`

重点分清：分析/设计活动、UML 表达语言、OOP 编码实现不在同一层。

### D. 软件测试

`是否运行：静态/动态 → 是否利用内部结构：黑/白/灰 → 黑盒用例/白盒覆盖 → V&V → 测试层次 → 性能/回归/Alpha Beta/A-B/自动化`

后续卡必须说明自己属于分类维度、测试技术、测试层次、测试目的、测试场景中的哪一层。

### E. 净室 / CBSE / 项目管理

- 净室：`净室整体思想 → 盒子结构`
- CBSE：`构件模型与容器 → CBSE过程 → 组装方式 → 接口适配`
- 项目管理：`管理范围 → WBS → 活动依赖/进度 → 配置管理 → 版本/基线 → SQA → 风险管理`

## 三、执行批次

| 批次 | 范围 | 状态 / 核心目标 |
| --- | --- | --- |
| SE-UX-01A-WATERFALL | [[瀑布模型]] | 已完成：建立过程模型坐标、晚改返工链、生命周期边界 |
| SE-UX-01B-ITER-SPIRAL | [[迭代与增量模型]]、[[螺旋模型]] | 已完成：分清反复细化 / 增加能力 / 风险驱动 |
| SE-UX-01C-PROT-COMP | [[原型的去留与目标系统]]、[[构件组装模型]] | 已完成：需求澄清 vs 构件复用；清理 `[[原型法]]` 幽灵链接 |
| SE-UX-02A-RUP | [[RUP]]、[[RUP九类工作流]]、[[RUP四加一视图]] | 已完成：阶段 / 工作流 / 架构视图三维分层，4+1 保持 link_only |
| SE-UX-02B-AGILE-CMMI | XP、Scrum、水晶、FDD、CMMI | 已完成：敏捷方法家族 vs 组织过程成熟度 |
| SE-UX-03-REQ | 02_需求工程 6 张卡 | 已完成：开发需求 → 管理需求连续主线 |
| SE-UX-04-STRUCT | 结构化分析设计组 | 已完成：结构化分析、模块设计、详细设计连续主线 |
| **SE-UX-05-OO-UML** | OO / UML / 持久化 / 逆向 / 形式化 | **已完成**：方法阶段 vs 表达语言 vs 编码实现；补齐前后链 |
| **SE-UX-06-TEST** | 04_软件测试 13 张卡 | **已完成**：建立测试分类坐标，避免不同分类轴串层 |
| **SE-UX-07-CLEAN-CBSE** | 净室 2 张 + CBSE 4 张 | **已完成**：保留净室机制正文，补齐净室 → 盒子结构 → CBSE 构件/过程/组装/适配连续链 |
| **SE-UX-08-PM** | 项目管理 7 张卡 | **已完成**：建立“管理范围 → WBS → 进度 → SCM/版本/基线 → SQA → 风险”连续链 |
| SE-UX-09-NAV | 索引、学习路线、优先级、链接、frontmatter | 同步真实学习顺序；清理死链、旧 quality/source 和元数据 |
| SE-UX-10-ACCEPT | 全章一次联合验收 | 核验学习链、样例门槛、主事实源、链接和历史 coverage |

## 四、每轮固定执行规则

1. 从远端最新 `main` 获取真实 `START_HEAD`；
2. 重新读取 `AGENTS.md`、任务路由 prompts、本计划、目标正文、直接上一站/下一站、章节索引/学习路线及相关教材证据；
3. 每轮只执行 `current_batch`；不重复 `last_completed`；
4. 写入前再次读取远端 HEAD；若变化，基于新 HEAD 重读目标并安全重建修改；
5. 直接安全提交 `main`，不创建 PR、不 force push、不改写历史；
6. 能运行时执行 `node scripts/check-vault.mjs` 与 `git diff --check`；当前连接器环境不能运行时必须明确记录“未执行”；
7. 完成后更新 `last_completed`、`current_batch`、`last_batch_commit` 与执行进度；
8. 每轮报告 START_HEAD / END_HEAD、修改文件、真实问题与修复、Atom/coverage、导航/链接、检查、并发、下一轮和下下轮。

## 五、执行进度

### SE-UX-01A-WATERFALL（已完成）

- START_HEAD：`aee7401448bc3d68edfa47ff44c2a487141d4422`
- 正文提交：`b98360619d663ab1070fdeb07a45d069e829e80f`
- 结果：补齐过程模型坐标、阶段依赖、晚期返工原因、生命周期边界与迭代/增量下一站。
- coverage：历史 coverage 不变。

### SE-UX-01B-ITER-SPIRAL（已完成）

- START_HEAD：`e5499829bebab19101f80bd4fcce8b344b7f2975`
- 正文提交：`583b321d983467b75559df288ae5a18796b0c88d`、`5ecc96d0a7a181a8d32237fe098d7dfb1d0a2473`
- 结果：迭代 = 反复细化；增量 = 增加能力；螺旋 = 每轮风险驱动。补齐前后链。
- coverage：历史 coverage 不变。

### SE-UX-01C-PROT-COMP（已完成）

- 结果：分清原型的需求澄清目标与构件复用过程；确认并移除无主事实源的 `[[原型法]]` 幽灵链接。
- coverage：历史 coverage 不变。

### SE-UX-02A-RUP（已完成）

- START_HEAD：`6ae5e29c783d142f671fe1c57e418807f5737778`
- 正文提交：`b3b9d65691cadaa30d4655d24968499dd814c0c9`、`bb2e14118b9fe3864d69650f3197e71f63a6637b`、`76754d4c3fd389bdadee892f703f4ab745e11cef`
- 结果：四阶段 = 时间推进；九类工作流 = 工作种类；4+1 = 架构观察视角。4+1 继续 legal link_only。
- coverage：`44 covered + 1 legal link_only` 不变。

### SE-UX-02B-AGILE-CMMI（已完成）

- START_HEAD：`4d77bc78e2ac91f54d3244ff7772a13acb6c746b`
- 正文提交：`1d7ae026bebfed048476c8ffd435fbb8bf187f1a`、`1020c78cb1d7b9c11859e50a7864c1d6b285db95`、`97966d7002805627a472135dd5e573883cd1fc1b`、`2b12ad7267965d8c6915368a3e156c68b660ec8c`、`93dbc6ebec5e4b00fcd5a3207c63d96592ccfd8c`
- 结果：建立敏捷家族共同坐标；CMMI 切回组织过程成熟度层级。
- coverage：历史 coverage 不变。

### SE-UX-03-REQ（已完成）

- 结果：把需求层次、开发/管理、获取、规格/确认、变更控制、双向追踪串成“先弄清 → 再管住”的连续主线。
- coverage：历史 coverage 不变。

### SE-UX-04-STRUCT（已完成）

- last batch commit：`c97593286fe5709775717ce2ae9f73d6a1c06dd4`
- 结果：以 [[结构化分析与设计分工]] 为样例，收敛结构化分析、DFD/数据字典、模块设计与详细设计的层级和学习桥梁。
- coverage：历史 coverage 不变。

### SE-UX-05-OO-UML（已完成）

- 日期：2026-09-21
- START_HEAD：`c3523a0cc759f75446e62dbea494fb86ef45da70` 之前本批已有并发正文提交；本轮运行时首次读取的 HEAD 为 `c3523a0cc759f75446e62dbea494fb86ef45da70`，随后安全观察到本批后续提交推进至 `0b4d179702ebd15243abc6a683fc5194143c7a09`。
- 代表正文提交：
  - `c3523a0cc759f75446e62dbea494fb86ef45da70`：[[面向对象程序设计OOP]]
  - `7ce85218002aef0f26ee26f6eb6462915217d506`：[[对象持久化与ORM]]
  - `adf1712bc6dd3fe2045405be78c5f831bb4990e9`：[[逆向工程]]
  - `0b4d179702ebd15243abc6a683fc5194143c7a09`：[[形式化方法]]
- 已核验正文还包括：[[面向对象方法]]、[[面向对象分析OOA]]、[[面向对象设计OOD]]、[[UML总览]]、UML 核心图组、[[实体类边界类与控制类]]。
- 真实问题与修复：
  - 建立 `OOA = 问题域理解 / OOD = 职责接口协作设计 / UML = 模型表达语言 / OOP = 编码实现` 的层级坐标；
  - UML 总览明确“三大组成 → 基本构造块（事物/关系）→ 图”与“五视图”不是同一分类层；
  - 实体/边界/控制类回到 OOD 职责分配语境；
  - OOP 明确实现边界，持久化承接运行对象状态长期保存；
  - 逆向工程切换到已有实现恢复知识的维护视角；形式化方法明确规格/验证作用并自然衔接测试模块。
- 教材证据：主教材 PDF 217–221（OOA/OOD/OOP/持久化）及 PDF 97–100（UML 组成、关系、图与视图），AI 文本均标记 `extract_status: 可解析`。
- Atom / coverage：未发现需要把历史 covered 退回 partial 的事实缺口；全章仍为 `44 covered + 1 legal link_only（SE-A009）`。
- 导航 / 链接：正文学习链已按 `面向对象方法 → OOA → OOD → UML → 实体/边界/控制 → OOP → 持久化 → 逆向 → 形式化 → 静态/动态测试` 连续衔接；本批不新增第二套导航。
- 并发：运行期间观察到同一批次的连续安全提交；未覆盖这些提交。本轮只在正文稳定后推进控制面。
- 检查：远端回读完成；当前 GitHub 连接器环境无本地工作树，`node scripts/check-vault.mjs` 与 `git diff --check` **未执行**。
- 下一轮：`SE-UX-06-TEST`。
- 下下轮：`SE-UX-07-CLEAN-CBSE`。

## 六、最终退出条件

SE-UX 仅在以下条件同时满足时收口：学习链无明显断链；重点概念达到样例最低教学闭环；测试、OO/UML、过程模型等多维概念有明确层级坐标；失效/幽灵 wikilink 清零；修改过的学习笔记均为 `review_status: 待复习`；SE-UX-10 一次联合验收完成；若无事实回退，历史 coverage 仍保持 `44 covered + 1 legal link_only`。

SE-UX-10 收口后，恢复执行运行时最新 [[全库补全总控计划]] 的 `current_priority`。
