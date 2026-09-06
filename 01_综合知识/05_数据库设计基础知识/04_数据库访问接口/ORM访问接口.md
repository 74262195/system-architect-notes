---
type: 考点
subject: 系统架构设计师
chapter: 数据库设计基础知识
topic: ORM访问接口
source: 官方教材与大纲校准
textbook_pages: "261–263"
status: 学习中
created: 2026-09-06
updated: 2026-09-06
exam_priority: P2
review_level: 三轮审核通过
priority_reason: "新版大纲明确 ORM 定义、作用和典型框架；当前主要掌握对象—关系映射定位。"
priority_updated: 2026-09-06
quality_status: 三轮审核通过
---

# ORM 访问接口

> [!summary] 快速复习卡片
> **作用/定位**：ORM 解决面向对象程序中的对象模型与关系数据库表模型之间的映射问题。
> **核心结论**：通过映射元数据，把对象、属性、对象关系与表、列、外键等对应起来，实现对象持久化。
> **题干怎么认**：对象持久化、对象—关系映射、Hibernate/MyBatis/JPA → ORM 语境。
> **易错点**：ORM 不是数据库本身，也不意味着数据库不再使用 SQL/关系模型。

应用程序常按“对象”思考，例如一个 `User` 对象包含 id、name、orders；关系数据库则按表、行、列和外键组织数据。两种模型之间存在表达差异。

ORM（Object Relational Mapping，对象关系映射）通过映射信息把二者关联：

- 类/实体对象 ↔ 表；
- 对象属性 ↔ 列；
- 对象之间的关联 ↔ 外键/关联表；
- 对象的保存、查询、更新 ↔ 相应数据库操作。

它的主要价值是让业务代码更多按对象模型组织，减少大量重复的数据转换代码。

新版大纲列出的典型 ORM 框架/规范包括 Hibernate、MyBatis、JPA。复习时以“ORM 的定位和作用”优先，不必把某个框架 API 细节扩成编程教程。

## 和 ODBC 的区别

ODBC 重点是“统一地连接/访问不同数据库”；ORM 重点是“对象模型与关系模型之间怎样映射”。

## 自测

> [!question]- “将 Java 实体对象的属性自动对应到数据库表字段”主要属于哪类技术？
> ORM。
