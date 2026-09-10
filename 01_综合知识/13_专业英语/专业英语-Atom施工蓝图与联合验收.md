---
type: plan
subject: 系统架构设计师
chapter: 专业英语
topic: Atom施工蓝图与联合验收
status: coverage_complete
quality_status: quality_pending
source:
  - 系统架构设计师考试大纲（第二版）PDF 62
  - 2009—2018 综合知识 A 级标准化题库 Q71—Q75
  - 系统架构设计师教程第二版可搜索 PDF 721—724
  - 2_系统架构师32小时 PDF 301—304
tags: [专业英语, Atom, 覆盖验收, 英文阅读, 术语映射]
---

# 专业英语-Atom施工蓝图与联合验收

> [!success] 本轮结论
> `G4-13-BUILD` 按“英文题给什么 → 先抓什么信号 → 去掉什么修饰 → 映射哪个中文知识 → 怎样排除答案”完成首次建设。形成 `ENG-A001 ~ ENG-A015` 共 15 个稳定 Atom；每个 Atom 均有唯一正文、快速复习卡和上一站/下一站，目标状态为 `coverage_complete / quality_pending`。

## 1. 大纲真实范围

考试大纲（第二版）PDF 62 对第 13 章只给出两项要求：

1. 具有高级工程师所要求的英文阅读水平；
2. 掌握本领域的英语术语。

因此本章不是语法教材，也不是英语词典。它只解决一个考试问题：**已经学会的中文知识换成英文题干以后，怎样仍然认得出来并完成选择。**

## 2. 真题考法锁定

当前仓库 2009—2018 综合知识属于 A 级标准化批次。Q71—Q75 连续呈现了稳定形态：一段专业英文共用题干，连续 5 个空格依靠上下文、定义、关系和专业术语完成判断。

| 年份 | Q71—Q75 主题 | 能证明的考试动作 |
|---|---|---|
| 2009 | 架构风格、component、connector、constraint、semantic model、pipe-and-filter | 定义链 + 术语搭配 + 上下文完形 |
| 2010 | architectural pattern/model、business/application/reference architecture | 定义识别 + 相近术语排除 |
| 2011 | 信息系统设计任务、数据库规格、internal controls、programmer、feasibility | 顺序词 + purpose + 流程上下文 |
| 2013 | system architecture、module/C&C/allocation structures | 长句主干 + 分类关系 |
| 2014 | architecture reconstruction、information extraction、view fusion | 流程词 + 前后照应 |
| 2015—2016 | architecture design、data storage/access/application logic、client/server/network | 定义 + 并列结构 + 专业搭配 |
| 2017 | functional/nonfunctional requirements、client-server、performance/security | 需求分类 + 术语边界 |
| 2018 | data storage、file types、legacy database、referential integrity | 数据库术语 + 定义语义 |

这组证据说明：**完整段落理解比孤立单词翻译更重要，专业知识映射比完整语法体系更重要。**

> [!warning] 证据与 OCR 边界
> 大纲 AI 文本使用 OCR 回退；两条专业英语要求当前清晰可读，但本轮未回看 LFS 原 PDF 图像。`2_系统架构师32小时` 也是 OCR 层，只作辅导证据。A 级标准化题库个别英文存在抽取/排版噪声（如漏字、拼写错位），本章不把这些噪声当成应背表达。未对每个 Atom 做独立精确题频统计，所以所有正文 `exam_priority` 保持 `待评估`。

## 3. 稳定 Atom 契约

| Atom | P级 | 主问题 | 英文考试动作 | 对应中文知识域 | 唯一主事实源 | 状态 |
|---|---:|---|---|---|---|---|
| ENG-A001 | P0 | 共用英文段落有空格时先看哪里？ | 先判空格角色，再读左右文 | 跨域 | [[01_上下文完形与空格定位]] | covered |
| ENG-A002 | P0 | 长句怎样先抓主干？ | 主语→谓语→宾语，再还原修饰 | 跨域 | [[02_长句主干与修饰剥离]] | covered |
| ENG-A003 | P0 | 怎样识别英文定义题？ | 锁定 defined as / refers to / is the…that | 跨域 | [[03_定义题与定义信号]] | covered |
| ENG-A004 | P0 | not/except/incorrect 怎样避免反选？ | 先把题目改写成“找错误项” | 跨域 | [[04_否定例外与错误项识别]] | covered |
| ENG-A005 | P0 | 怎样识别因果和目的？ | 圈 because / result in / so that / in order to | 跨域 | [[05_因果与目的关系识别]] | covered |
| ENG-A006 | P0 | 条件边界怎样读？ | 圈 if / when / unless / only if / until | 跨域 | [[06_条件与范围边界识别]] | covered |
| ENG-A007 | P0 | 比较和转折怎样帮助排项？ | 圈 unlike / whereas / however / rather than | 跨域 | [[07_比较转折与对照关系]] | covered |
| ENG-A008 | P0 | 流程型段落怎样保持衔接？ | first→next→once→finally 串步骤 | 跨域 | [[08_流程顺序与篇章衔接]] | covered |
| ENG-A009 | P0 | 缩写看懂后怎样映射知识？ | 还原全称→拆关键词→定位中文域 | 跨域 | [[09_缩写与英文全称还原]] | covered |
| ENG-A010 | P1 | 架构术语怎样成组识别？ | component/connector/style/pattern/view 成组判断 | 软件架构 | [[10_软件架构术语映射]] | covered |
| ENG-A011 | P1 | 信息系统和软件工程术语怎样路由？ | requirements/process/use case/DFD/cohesion 先定位域 | 信息系统/软件工程 | [[11_信息系统与软件工程术语映射]] | covered |
| ENG-A012 | P1 | 数据库题眼怎样识别？ | key/transaction/normalization/replication/integrity | 数据库 | [[12_数据库与数据存储术语映射]] | covered |
| ENG-A013 | P1 | 质量、安全、可靠性怎样避免串义？ | performance/availability/reliability/CIA/auth 区分 | 架构质量/安全/可靠性 | [[13_质量属性安全与可靠性术语映射]] | covered |
| ENG-A014 | P2 | 网络和操作系统术语怎样快速定位？ | protocol/routing/subnet/process/thread/deadlock 路由 | 网络/操作系统 | [[14_网络操作系统与系统术语映射]] | covered |
| ENG-A015 | P2 | 数学、项目和新技术术语怎样最低成本识别？ | critical path/probability/simulation/edge/digital twin 路由 | 应用数学/项目/未来技术 | [[15_应用数学项目与新技术术语映射]] | covered |

### 数量

- stable Atom：15
- P0：9
- P1：4
- P2：2
- 英文阅读动作型：9
- 专业术语映射型：6

## 4. 教材与辅导资料如何使用

主教材没有把第 13 章展开成一套独立英语语法课程。PDF 721—724 等内容反而提供了大量“中文概念 + 英文专业名词”的事实锚，例如 Software System Modeling、架构风格、构件/连接件等。本章只借这些已有中文事实确认术语所指，不复制原章节正文。

`2_系统架构师32小时` PDF 301—304 同样出现开放架构、设计模式 Adapter/Builder/Command/Strategy 等中英术语，适合作为“英文词形如何映射已学概念”的辅证，不作为范围扩张依据。

## 5. 统一做题流水线

```mermaid
flowchart LR
    A["先看题问什么"] --> B["圈否定/条件/比较/顺序信号"]
    B --> C["找句子主干"]
    C --> D["找专业关键词或缩写"]
    D --> E["映射中文知识域"]
    E --> F["用上下文排除选项"]
```

## 6. 边界裁决

1. 不建立几百张孤立单词卡；术语只按“考试动作或知识域路由”成组出现。
2. 不系统讲时态、虚拟语气、非谓语等完整语法，只解释会改变题意的结构。
3. `critical path` 在本章只负责认出“关键路径”；计算仍回到第 12 章。
4. `normalization`、`deadlock`、`cohesion/coupling`、CIA 等同理，本章不复制中文正文。
5. P0 是本轮**建设级别**，表示对英语做题链的重要性；不等于已经得到逐 Atom 真题频次统计。

## 7. 联合覆盖验收

- [x] stable Atom 全部唯一：15 / 15
- [x] covered + link_only + blocked = 15：15 + 0 + 0 = 15
- [x] partial = 0
- [x] unmapped = 0
- [x] P0/P1/P2 保留 Atom 均有正文
- [x] 9 个 P0 均有完整英文教学例句与逐步判断
- [x] 快速复习卡 = 15 / 15
- [x] 上一站/下一站 = 15 / 15
- [x] Atom → 正文正向映射无缺口
- [x] 正文 → Atom 反向映射无孤岛
- [x] fake covered = 0
- [x] 章内 Wikilink 只指向本轮实际创建文件
- [x] 不复制前 12 章大量正文
- [x] 第 12 → 第 13 章语义承接成立
- [x] 第 13 章末不创建不存在的第 14 章链接

## 8. Coverage 快照

| 指标 | 当前值 |
|---|---:|
| stable Atom | 15 |
| covered | 15 |
| partial | 0 |
| unmapped | 0 |
| link_only | 0 |
| blocked | 0 |
| 快速复习卡 | 15 |
| 上一站/下一站 | 15 |
| 阅读动作型 | 9 |
| 术语映射型 | 6 |
| exam_priority | 全部待评估 |
| 当前状态 | coverage_complete / quality_pending |

本轮到此只完成首次覆盖，不追求 `quality_complete`，也不修改共享控制面。