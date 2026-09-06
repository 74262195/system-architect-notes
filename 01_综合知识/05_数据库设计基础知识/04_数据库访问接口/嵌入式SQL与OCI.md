---
type: 考点
subject: 系统架构设计师
chapter: 数据库设计基础知识
topic: 嵌入式SQL与OCI
source: 官方教材与大纲校准
textbook_pages: "259–260"
status: 学习中
created: 2026-09-06
updated: 2026-09-06
exam_priority: P2
review_level: 三轮审核通过
priority_reason: "新版大纲明确 OCI 与嵌入式 SQL；以访问机制与识别差异为主，当前真题直接信号较弱。"
priority_updated: 2026-09-06
quality_status: 三轮审核通过
---

# 嵌入式 SQL 与 OCI

> [!summary] 快速复习卡片
> **作用/定位**：它们都让高级语言程序访问数据库，但一个强调“SQL 嵌进宿主语言”，另一个强调“调用厂商函数库”。
> **核心结论**：嵌入式 SQL 通常需要预编译器处理 SQL 与宿主语言；OCI 是 Oracle 提供的库函数级 API。
> **题干怎么认**：宿主语言/预编译器/游标 → 嵌入式 SQL；Oracle Call Interface/函数调用 → OCI。
> **易错点**：OCI 不是通用跨厂商接口，通常依赖特定数据库产品。

## 嵌入式 SQL

嵌入式 SQL 是把 SQL 语句直接写进 C、COBOL、Java 等**宿主语言**的源程序中。

问题在于普通宿主语言编译器并不认识 SQL，所以数据库厂商通常提供**预编译器**：先把嵌入的 SQL 转换成宿主语言可调用的函数/代码，再交给原编译器处理。

此外还要解决宿主变量、数据类型转换、查询多行结果（游标）以及事务控制等边界问题。

## OCI

OCI（Oracle Call Interface）是 Oracle 的库函数级访问接口。程序通过调用 OCI 函数完成连接数据库、执行 SQL、事务控制等操作。

这种方式通常更接近数据库产品底层接口，灵活但与具体厂商绑定更强、学习和开发复杂度也更高。

## 自测

> [!question]- “先用专用预编译器把 SQL 转换成宿主语言函数调用”描述的是哪种方式？
> 嵌入式 SQL。
