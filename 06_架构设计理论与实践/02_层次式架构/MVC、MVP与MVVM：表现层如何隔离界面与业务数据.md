---
type: 考点
subject: 系统架构设计师
chapter: 层次式架构
topic: 表现层模式 MVC MVP MVVM
status: 学习中
difficulty: 3
source:
  - 官方教材/系统架构第二版 大纲.pdf（PDF 64 页）
  - 官方教材/系统架构设计师教程第二版可搜索.pdf（PDF 469–471 页）
aliases: [MVC, MVP, MVVM, 表现层设计模式]
tags: [软考/架构设计师, 软考/考点, 架构设计理论与实践, 层次式架构]
exam_priority: P1
review_level: 重点
priority_reason: "大纲明确展开 MVC、MVP 和 MVVM，且三者的交互边界是表现层的核心判断入口"
priority_updated: 2026-09-20
review_status: 待复习
---

# MVC、MVP 与 MVVM：表现层如何隔离界面与业务数据

> [!summary]- 快速复习卡片（学完再看）
> **共同目标**：把界面显示与业务数据/逻辑分离，减少界面变化对核心功能的影响。
> **MVC**：Controller 解释输入并调用 Model，View 可从 Model 取得状态。
> **MVP**：View 不直接访问 Model，交互都通过 Presenter。
> **MVVM**：View 通过数据绑定与 ViewModel 同步，ViewModel 转换和暴露界面需要的状态。
> **第一反应**：先看 View 能否直接接触 Model，再看是 Presenter 显式协调，还是 ViewModel + Data Binding 自动同步。

在[[01_综合知识/06_软件架构设计/04B_调用返回风格：控制为什么沿明确调用关系传递|调用-返回风格]]里，我们已经知道分层会把表示、业务和数据访问职责分开。这一站只进入表现层内部：用户点击按钮、页面要显示数据时，界面怎样才不会和业务数据紧紧绑在一起？

**MVC、MVP 和 MVVM 都用中间角色隔开 View 与 Model；三者的核心区别，是界面与数据究竟通过谁、以什么方式交互。**

## 先用同一个订单页面看清三个角色

假设用户在订单页面点击“刷新总价”：

- **View（视图）**：显示订单明细和总价，接收点击等界面操作；
- **Model（模型）**：保存订单状态，并执行计算总价等业务处理；
- **Controller / Presenter / ViewModel**：位于界面与模型之间，但三种模式赋予它们的交互责任不同。

关键不是背三组英文，而是追问：**用户动作如何到达模型，模型的新状态又如何回到界面？**

## MVC：Controller 处理输入，View 可以查询 Model

**MVC（Model-View-Controller）把输入、处理和输出分给 Controller、Model 和 View，使业务处理与显示分离。**

沿用订单页面，一次交互可以这样走：

1. View 把“刷新总价”的用户请求交给 Controller；
2. Controller 解释请求，调用 Model 的总价计算方法；
3. Model 完成业务处理并产生新状态；
4. Controller 选择合适的 View，View 获取需要的模型状态并显示结果。

按主教材的考试口径，MVC 中 View 可以向 Model 查询状态；Controller 负责解释输入和调度处理。不同实现框架可能调整细节，做题时不要用某个框架的特例覆盖教材的角色关系。

MVC 的优势是同一 Model 可支持多种 View，界面变化不必重写核心业务处理。它的边界也很明确：**它是表现层的组织模式，不等于整个系统已经完成分层架构设计。**

## MVP：View 不再直接找 Model

**MVP（Model-View-Presenter）把 View 与 Model 的所有交互集中到 Presenter，以进一步降低两者的耦合。**

同一次“刷新总价”会变成：

1. View 把用户动作通知 Presenter；
2. Presenter 调用 Model 完成总价计算；
3. Presenter 取得新状态，通过 View 提供的接口要求界面更新；
4. View 只负责把结果显示给用户，不直接读取 Model。

Presenter 通常依赖抽象的 View 接口，因此可以用一个模拟 View 单独测试交互逻辑。代价是 Presenter 需要显式协调很多界面操作；界面类型和状态越多，View 接口与交互代码也可能膨胀。

## MVVM：ViewModel 用数据绑定与 View 同步

**MVVM（Model-View-ViewModel）用 ViewModel 暴露界面需要的状态和操作，再用数据绑定把 View 与这些状态同步起来。**

订单页面的交互变为：

1. View 把按钮命令映射给 ViewModel；
2. ViewModel 调用 Model 执行总价计算，并把模型结果转换成界面可直接使用的状态；
3. ViewModel 中的绑定状态发生变化，View 自动更新；
4. 如果使用双向绑定，View 中的变化也可通过 ViewModel 反向同步到数据状态。

这种方式适合界面状态频繁变化的数据驱动场景。但自动绑定也会让更新来源更难追踪；出现问题时，需要分清是 Model 数据、ViewModel 转换逻辑，还是 View 绑定导致。

## 三者怎样一步区分

| 模式 | View 与 Model 的关系 | 中间角色的核心动作 | 题干第一个信号 |
| --- | --- | --- | --- |
| MVC | 按教材经典关系，View 可查询 Model 状态 | Controller 解释输入、调用 Model、选择 View | 输入/处理/输出分离，Controller 接收请求 |
| MVP | View 不直接访问 Model | Presenter 集中交互，并通过 View 接口更新界面 | 所有交互经 Presenter、便于脱离 UI 测试 |
| MVVM | View 不直接访问 Model | ViewModel 暴露/转换状态，由 Data Binding 同步 | ViewModel、数据绑定、响应式更新 |

遇到选择题时，不要先看哪个名字更新，而是用两步判断：

1. **View 能否直接获取 Model 状态？** 能，且输入由 Controller 处理，先想 MVC；不能，继续判断。
2. **更新是 Presenter 显式命令 View，还是通过 ViewModel 的数据绑定同步？** 前者是 MVP，后者是 MVVM。

## 易错边界

- **MVC 不是整个分层架构的同义词**：它本篇只解决表现层内部的交互组织；系统还需要业务层、数据访问层等责任设计。
- **MVP 不只是把 Controller 改名为 Presenter**：考试关键是 View 不直接使用 Model，交互经 Presenter 集中处理。
- **MVVM 不只是多一个 ViewModel 类**：题眼是 ViewModel 提供界面状态，并由数据绑定促成同步。

## 自测

1. 某界面把用户动作交给中间对象，中间对象调用 Model，再通过 `IView` 要求界面显示结果。更符合哪种模式？

> [!answer]- 第 1 题答案与解析
> **答案**：MVP。
> **解析**：View 不直接访问 Model，交互由 Presenter 集中处理，且 Presenter 依赖抽象 View 接口。

2. 题干说“界面状态与 ViewModel 属性绑定，属性改变后界面自动刷新”，第一步应判断什么？

> [!answer]- 第 2 题答案与解析
> **答案**：MVVM。
> **解析**：ViewModel + 数据绑定 + 界面自动同步是直接题眼。

3. 为什么看到 MVC 不能立即断定“整个系统采用了分层架构”？

> [!answer]- 第 3 题答案与解析
> **答案**：MVC 在本章是表现层的设计模式，它不能单独证明系统的业务层、数据访问层和层间依赖也已正确设计。
> **解析**：表现层内部模式与整体分层架构不在同一层级。

## 上一站 / 下一站

- 上一站：[[01_综合知识/06_软件架构设计/04B_调用返回风格：控制为什么沿明确调用关系传递|调用-返回风格]] —— 先建立层次型中“上层使用下层服务”的基本识别。
- 下一站：待 `ARCH-LAY-A003/A009/A010` 获批建设后，继续学习 XML 表现层统一、UIP 与动态生成设计。
- 章节入口：[[层次式架构索引]]。
