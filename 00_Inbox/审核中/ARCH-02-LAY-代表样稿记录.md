---
type: 架构建设记录
subject: 系统架构设计师
status: awaiting_user_review
batch: ARCH-02-LAY-SAMPLE-GATE
start_head: 177ff996
atom: ARCH-LAY-A002
updated: 2026-09-20
tags: [软考/架构设计师, 审查/全库补全, ARCH, 层次式架构]
---

# ARCH-02-LAY 层次式架构代表样稿记录

## 本轮边界

- START_HEAD：`177ff996`（本地 `main` 指向该提交，工作树启动时为 detached HEAD）。
- 只处理 `ARCH-02-LAY-SAMPLE-GATE`；不批量建设其余 ARCH-LAY Atom，不跨域，不恢复 G5，不推进论文。
- 已重读最新 `AGENTS.md`、`prompts/00`、`prompts/10`、`prompts/40`、`prompts/65`、ARCH 124 Atom 正式矩阵、ARCH 总索引与全库总控。

## 真实缺口复核

本轮逐项复核 ARCH-LAY 的 18 个 stable Atom：

- `ARCH-LAY-A001`：`partial`。现有 04B 只能支持通用风格识别和基本依赖前置，不足以支持完整分层工程判断。
- `ARCH-LAY-A002～A018`：启动时共 17 个 `unmapped`，没有可验证的正文主事实源。
- OPT-03 的 04 总览 + 04A～04E 只完成软件架构风格前置，未改变 ARCH-LAY 上述状态。

## 样稿选择

选择 `ARCH-LAY-A002 表现层模式：MVC / MVP / MVVM`，而不是直接用 A001 作样稿，理由是：

1. A002 是正式矩阵中的真实 `unmapped` 缺口，不会把既有前置补强误当成新章写作基准；
2. A002 为 P1，大纲明确列出 MVC、MVP、MVVM；
3. 三个并列模式既要分别讲清交互过程，又要形成横向判断动作，能同时检验“一卡一主问题”与“同级成员不漏”；
4. 它还能检验“MVC ≠ 分层架构本身”这一已锁定边界是否落到正文。

## 证据

- 大纲：`官方教材/系统架构第二版 大纲.pdf` PDF 64，在层次式架构的表现层框架设计下明确列出 MVC、MVP 和 MVVM。
- 主教材：`官方教材/系统架构设计师教程第二版可搜索.pdf` PDF 469–471，分别给出三种模式的角色、交互、优势与边界。
- 格式证据：PDF 原件在当前 worktree 为 Git LFS 指针，本轮使用仓库已生成的对应 PDF 页分页抽取文本复核；未依赖网络扩展资料，未臆造图中信息。
- 优先级沿用正式契约 P1；本轮不从一般“设计模式”题频向下机械推导频次。

## 样稿验收

1. **Atom 与状态**：`ARCH-LAY-A002`，`unmapped → covered`。
2. **唯一主问题**：MVC、MVP 和 MVVM 如何以不同交互边界隔离界面与业务数据，做题时怎样区分？
3. **承接与前提**：承接 04B 的层次型风格前置；只需知道表现层负责用户交互。
4. **具体问题与直接答案**：正文以“订单页面刷新总价”贯穿，并直接给出三者均以中间角色隔开 View/Model，区别在交互路径。
5. **机制落点**：“MVC”、“MVP”、“MVVM”三节各自走完输入→处理→状态回到界面的闭环，不用比较表代替机制。
6. **考试动作**：“三者怎样一步区分”先判 View 能否直接接触 Model，再判 Presenter 显式协调或 ViewModel + Data Binding。
7. **边界**：“易错边界”明确 MVC 不等于整体分层架构，也不把 MVP 解释成单纯改名。
8. **可视化选择**：三种模式是简单对比，用表格比一张多分支 Mermaid 更易读；每个动态机制则用同场景有序步骤闭环，未使用 ASCII/伪图。
9. **导航**：新增层次式架构索引，上一站回链 04B，下一站仅写待批后的 Atom 组，不制造未存在 wikilink。

## 覆盖与控制面同步

- `ARCH-LAY-A002` 回填正文文件与具体标题落点，提升为 `covered`。
- ARCH-LAY 变为 `1 covered + 0 link_only + 1 partial + 16 unmapped`。
- 全库 ARCH 变为 `10 covered + 9 link_only + 12 partial + 93 unmapped`；stable Atom 仍为 124，范围与案例映射不变。
- ARCH 总索引、全库总控与新建章节索引均停在 `ARCH-02-LAY-SAMPLE-GATE / awaiting_user_review`。

## 明确确认点

**USER-GATE：待用户审核。**

只需确认这篇样稿是否可作为层次式架构后续 Atom 的写作基准。在得到“通过”或具体 minor fix 意见前，不执行其余批量生成。
