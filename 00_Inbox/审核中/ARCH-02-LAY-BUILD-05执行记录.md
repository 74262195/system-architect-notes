---
type: 执行记录
subject: 系统架构设计师
chapter: 层次式架构
batch: ARCH-02-LAY-BUILD-05
status: completed
updated: 2026-09-20
tags: [软考/架构设计师, 审查/执行记录, ARCH, 层次式架构]
---

# ARCH-02-LAY-BUILD-05 执行记录

## 范围

本批严格处理数据访问层的三个 Atom：

- `ARCH-LAY-A006`：XML Schema 在数据访问层的运用；
- `ARCH-LAY-A016`：事务处理设计；
- `ARCH-LAY-A017`：连接对象管理设计。

未提前进入数据库与类/XML 的设计融合，也未进入物联网三层架构。

## 教材证据与落点

教材 PDF 486–488 分别给出 XML Schema 的合法结构、内容、限制、类型和验证作用；事务的整体提交/失败回滚、ACID 与 JDBC 自动提交语境；以及资源池用于数据库连接初始化、分配、归还和复用的说明。

对应正文：

- [[XML Schema：怎样先写清数据长什么样再让系统接收它]]；
- [[事务处理：多步修改失败时怎样回到原状]]；
- [[数据库连接池：连接用完为什么通常要归还而不是关闭]]。

## 覆盖变化

| 口径 | 本批前 | 本批后 |
| --- | ---: | ---: |
| ARCH-LAY covered | 12 | 15 |
| ARCH-LAY unmapped | 6 | 3 |
| 全局 covered | 21 | 24 |
| 全局 unmapped | 83 | 80 |

## 下一批

`ARCH-02-LAY-BUILD-06` 只处理 `ARCH-LAY-A007/A018`：数据库设计与类设计融合、数据库设计与 XML 设计融合。
