---
type: 考点
subject: 系统架构设计师
chapter: 数据库设计基础知识
topic: ORM访问接口
stable_atom_id: DB-A032
coverage_status: link_only
canonical_atom: SE-A031
canonical_source: "[[对象持久化与ORM]]"
source: 官方教材与大纲校准
outline_section: 5.4.4 ORM访问接口
textbook_pages: "261–262"
status: 学习中
review_status: 待复习
created: 2026-09-06
updated: 2026-09-10
exam_priority: P2
review_level: 待复习
priority_reason: "新版大纲明确 ORM 定义、作用和典型框架；当前跨章唯一完整主事实源固定为软件工程 SE-A031，本卡只保留数据库大纲定位与导航。"
priority_updated: 2026-09-06
quality_status: G3-DB-CLOSE唯一主源收敛-待复习
---

# ORM 访问接口

> [!summary] 快速复习入口
> **数据库大纲定位**：新版大纲 5.4.4 要求理解 ORM 的定义、作用及典型框架。
> **唯一完整主事实源**：[[对象持久化与ORM]]（软件工程稳定 Atom `SE-A031`）。
> **本卡职责**：只负责数据库章节中的定位、边界与导航，不复制第二套 ORM 完整机制。

ORM（Object Relational Mapping，对象关系映射）位于应用对象模型与关系数据库之间。考试看到“对象—关系映射、对象持久化、Hibernate/MyBatis/JPA”等关键词时，应进入 ORM 语境。

本仓库已经在软件工程主线用 [[对象持久化与ORM]] 完整讲解对象持久化、ORM 与 SQL/JDBC 的层次边界，因此这里不再重复维护同一套正文。

> [!important] 易混边界
> - ORM **不是 DBMS**；数据库的存储、事务、约束、索引等核心机制仍由数据库系统承担。
> - ORM **不等于不需要 SQL**；它可以封装或生成部分访问操作，但底层关系数据库仍执行相应数据库操作。
> - ODBC/JDBC 更偏“怎样访问数据库”；ORM 更偏“对象模型怎样映射到关系模型”。

> [!tip] 软考怎么考
> 题干强调“对象属性对应表字段、对象关系对应外键/关联关系” → 先想到 **ORM**。  
> 需要继续区分 SQL、JDBC、ORM、Hibernate、iBatis/JDO 等层次时，直接进入 [[对象持久化与ORM]]。

## 下一站

完成访问接口定位后，继续到 [[NoSQL分类与特点]]，从关系数据库访问方式转向不同数据模型与存储取向的边界。
