---
type: 执行记录
subject: 系统架构设计师
chapter: 层次式架构
status: closed
batch: ARCH-02-LAY-BUILD-04
scope: ARCH-LAY-A005/A014/A015
updated: 2026-09-20
tags: [软考/架构设计师, 架构设计理论与实践, 层次式架构, 执行记录]
---

# ARCH-02-LAY-BUILD-04 执行记录

## 一、范围与教材依据

本批只处理数据访问层基础：大纲 PDF 64 页；主教材 PDF 480–486 页。

| Atom | 教材最小闭环 | 正文落点 |
| --- | --- | --- |
| A005 | 五种模式逐项定位并区分在线、DAO、DTO、离线与 O/R 映射 | [[06_架构设计理论与实践/02_层次式架构/五种数据访问模式：数据怎样在业务层和数据源之间来回|五种数据访问模式]] |
| A014 | 统一接口、具体实现、工厂按数据库类型创建对象，以及专有功能边界 | [[06_架构设计理论与实践/02_层次式架构/数据访问层工厂模式：换数据库时为什么调用方不用改一片|数据访问层工厂模式]] |
| A015 | ORM 对象↔关系记录映射、Hibernate 示例与 CMP 2.0 的证据边界 | [[06_架构设计理论与实践/02_层次式架构/ORM与Hibernate：怎样让程序主要操作对象而不是表记录|ORM 与 Hibernate]] |

## 二、证据边界

主教材的 `13.4.3` 标题并列“ORM、Hibernate 与 CMP 2.0”，但当前可解析正文只详细解释 ORM 和 Hibernate；CMP 2.0 没有可核验的机制段落。本批不以通用记忆补造 CMP 2.0 的流程或接口，只保留它是本节持久化语境下的旧技术定位。

## 三、状态变化

- ARCH-LAY：`9 covered + 0 partial + 9 unmapped` → `12 covered + 0 partial + 6 unmapped`；
- ARCH 全局：`18 covered + 9 link_only + 11 partial + 86 unmapped` → `21 covered + 9 link_only + 11 partial + 83 unmapped`。

## 四、下一批

`ARCH-02-LAY-BUILD-05` 只处理 `ARCH-LAY-A006/A016/A017`：XML Schema、事务处理和连接对象管理。
