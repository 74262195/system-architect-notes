---
type: 考点
subject: 系统架构设计师
chapter: 数据库设计基础知识
topic: ODBC与JDBC
source: 官方教材与大纲校准
textbook_pages: "260–262"
status: 学习中
created: 2026-09-06
updated: 2026-09-22
exam_priority: P2
review_level: 三轮审核通过
priority_reason: "大纲明确 ODBC；主教材补充 JDBC。当前以识别统一访问接口及二者定位为主。"
priority_updated: 2026-09-06
review_status: 待复习
quality_status: QH2-05-DB-04-待复习
---

# ODBC 与 JDBC

> [!summary] 快速复习卡片
> **作用/定位**：两者都在降低应用直接适配具体数据库产品的成本，但所处生态与接口形式不同。
> **核心结论**：ODBC 强调通过统一接口和数据库驱动访问异构数据源；JDBC 是 Java 访问关系数据库的标准 API。
> **题干怎么认**：开放数据库连接、数据源/驱动、异构 DB → ODBC；Java 类和接口、Java 程序直接执行 SQL → JDBC。
> **易错点**：新版大纲明确点名 ODBC；JDBC 是主教材补充，不应因为熟悉 Java 就把它提升为同等大纲权重。

## ODBC 是什么

ODBC（Open Database Connectivity，开放数据库连接）要解决的是：应用不应该为每一种 DBMS 都重写一套访问代码。

应用面对统一的 ODBC API，真正与具体 DBMS 交互的差异由相应的 **ODBC 驱动程序**处理。数据源配置帮助 ODBC 找到数据库位置、类型和对应驱动。

因此题干如果强调“统一方式访问不同关系数据库”“驱动程序”“数据源”，优先想到 ODBC。

## JDBC 是什么

JDBC 是 Java 语言访问数据库的一组标准类和接口。Java 程序可通过 JDBC 建立连接、执行 SQL、处理返回结果。

二者可以类比理解为“都提供标准化程序接口”，但不要把实现生态混为一谈：ODBC 是通用数据库连接标准语境，JDBC 面向 Java。

## 自测

> [!question]- 第 1 题：某题问“由 Java 编写的一组类和接口，用于数据库访问”，更接近 ODBC 还是 JDBC？
>
> > [!answer]- 答案与解析
> > **答案**：JDBC。
> > **解析**：Java 的类和接口是 JDBC 的直接识别信号；ODBC 的核心线索是统一 API、数据源和驱动处理异构 DBMS 差异。

下一站：[[ORM访问接口]]，理解对象与关系记录怎样建立映射。
