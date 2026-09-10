---
type: 联合覆盖收口记录
subject: 系统架构设计师
chapter: 数据库设计基础知识
topic: G3-DB-CLOSE
status: coverage_complete
scope: DB-A001~DB-A034
start_head: 941f9a16e3ac1b020e63c9120baf1b167095a813
created: 2026-09-10
updated: 2026-09-10
tags:
  - 软考/架构设计师
  - 审查/数据库
  - 审查/G3
  - 审查/覆盖收口
---

# 数据库设计基础知识 G3-DB-CLOSE 收口记录

## 一、本轮身份与边界

- 批次：`G3-DB-CLOSE`
- 启动远端 `START_HEAD`：`941f9a16e3ac1b020e63c9120baf1b167095a813`
- 唯一施工范围：`01_综合知识/05_数据库设计基础知识/**`
- 稳定契约：`DB-A001 ~ DB-A034`，总数保持 34；不新增、不改号。
- 共享控制面只回填数据库覆盖事实和下一接力点。
- 未修改 01、02、03、04、06～13 的知识正文；未启动 `G3-CS-CONTRACT`、`G3-QA-CONTRACT` 或 `G4-COVERAGE-FINAL-RERUN`。

本轮从远端最新文件重新识别出的 4 个 `partial` 为：`DB-A001`、`DB-A008`、`DB-A010`、`DB-A032`，不是沿用旧会话缓存。

## 二、证据锁定

| Atom | 大纲证据 | 主教材证据 | 收口前真实缺口 |
| --- | --- | --- | --- |
| DB-A001 | 5.1.1、5.1.3 | PDF 234–240 | DB/DBMS/DBS 已有，但 DBA 角色弱；缺 `DBMS ≠ Navicat/DBeaver 等客户端工具` 边界与考试动作 |
| DB-A008 | 5.2.1 | PDF 237、242 | 关系术语已有，但“关系模式=型、某时刻关系实例=值”没有明确正文落点 |
| DB-A010 | 5.2.2 | PDF 243–246 | 五种基本运算已有，但缺四类运算符全景、交/除及比较/逻辑运算符的角色 |
| DB-A032 | 5.4.4 ORM 访问接口 | **PDF 261–262** | 数据库与软件工程同时保留完整 ORM 正文，违反唯一主事实源；旧迁移页码也存在不一致 |

A032 证据纠偏：当前大纲明确是 **5.4.4**；主教材 ORM 正文在 **PDF 261–262**。PDF 252–253 属于数据库概念结构/E-R 设计区域，不再作为 ORM 主证据。

## 三、四个 partial 的定点修复

### DB-A001：DB / DBMS / DBS / DBA

主事实源：[[数据库DB-DBMS-DBS]]。

本轮只补：
- DBA 的最小职责定位；
- `DBMS` 与 Navicat/DBeaver/SQL Developer 类客户端管理工具的边界；
- “用户/客户端 → DBMS → DB”的访问方向；
- 软考角色判断和自测。

结果：`partial → covered`。

### DB-A008：关系模式与实例

主事实源：[[关系模型基本术语与完整性]]。

本轮只补：
- 关系模式是“型”；
- 某一时刻关系/关系实例是“值”；
- “加数据行”与“改属性结构”的对照；
- 快速复习与考试动作。

结果：`partial → covered`。

### DB-A010：关系代数运算符体系

主事实源：[[关系代数基础运算]]，连接细节继续由 [[连接与自然连接]] 承担。

本轮只补：
- 集合运算符、专门关系运算符、算术比较运算符、逻辑运算符四类；
- 交、除法的最小语义；
- “五种基本运算”与“四类运算符”不是同一问法；
- 比较/逻辑运算符在选择、连接条件中的位置；
- “满足全部要求”识别除法语义的考试动作。

结果：`partial → covered`。

### DB-A032：ORM 唯一主事实源收敛

数据库大纲需要 ORM 定位，但软件工程稳定契约已经明确：

> `SE-A031 | [[对象持久化与ORM]] | covered`

而本轮禁止修改 04 软件工程正文，因此不能把数据库侧再维护为第二篇完整主事实源。数据库 [[ORM访问接口]] 已收敛为定位 + 边界 + 导航，并明确唯一完整主事实源为 [[对象持久化与ORM]] / `SE-A031`。

结果：`partial → legal link_only`。

这不是缺口，也不是为了降低标准；仓库现行规则允许 `link_only` 在唯一主事实源真实存在且已 covered 时满足覆盖门禁。相反，强行把 A032 写成第二个 `covered` 全文才会违反唯一主源规则。

## 四、34/34 联合覆盖复核

本轮不批量重写原有 30 个 `covered` Atom。联合验收采用：

1. 对 30 个既有 `covered` Atom 复核稳定 ID、映射、主事实源存在性和当前状态，不发现新增 `partial/unmapped/blocked`；
2. 对 4 个原 `partial` 逐项执行大纲 → 教材 → 主事实源 → 正文落点 → 边界/考试动作或合法 link-only 深核；
3. 对 A032 额外执行跨章唯一主事实源核验，确认软件工程 `SE-A031` 已是 covered；
4. 不把旧“29/29 三轮通过”当作当前 34 Atom 完成证明。

| Atom | 当前主事实源 / 唯一事实源 | 最终状态 |
| --- | --- | --- |
| DB-A001 | [[数据库DB-DBMS-DBS]] | covered |
| DB-A002 | [[数据管理技术三个发展阶段]] | covered |
| DB-A003 | [[分布式数据库与透明性]]；[[商业智能BI]] | covered |
| DB-A004 | [[数据模型三要素与分类]] | covered |
| DB-A005 | [[DBMS核心功能]] | covered |
| DB-A006 | [[数据库三级模式与两级映像]] | covered |
| DB-A007 | [[分布式数据库与透明性]] | covered |
| DB-A008 | [[关系模型基本术语与完整性]] | covered |
| DB-A009 | [[关系模型基本术语与完整性]] | covered |
| DB-A010 | [[关系代数基础运算]]；[[连接与自然连接]] | covered |
| DB-A011 | [[关系代数基础运算]] | covered |
| DB-A012 | [[连接与自然连接]] | covered |
| DB-A013 | [[函数依赖与属性闭包]]；[[范式1NF-2NF-3NF-BCNF]] | covered |
| DB-A014 | [[函数依赖与属性闭包]] | covered |
| DB-A015 | [[函数依赖与属性闭包]]；[[候选码求解]] | covered |
| DB-A016 | [[范式1NF-2NF-3NF-BCNF]] | covered |
| DB-A017 | [[多值依赖与4NF]] | covered |
| DB-A018 | [[无损连接与保持函数依赖]] | covered |
| DB-A019 | [[数据库设计六阶段]] | covered |
| DB-A020 | [[数据需求分析]] | covered |
| DB-A021 | [[ER模型与概念结构设计]] | covered |
| DB-A022 | [[ER图合并与冲突]] | covered |
| DB-A023 | [[ER图转关系模式]] | covered |
| DB-A024 | [[逻辑设计与完整性视图]] | covered |
| DB-A025 | [[反规范化设计]] | covered |
| DB-A026 | [[物理设计与索引]] | covered |
| DB-A027 | [[数据库实施与试运行]] | covered |
| DB-A028 | [[数据库运行维护与备份恢复]] | covered |
| DB-A029 | [[嵌入式SQL与OCI]] | covered |
| DB-A030 | [[嵌入式SQL与OCI]] | covered |
| DB-A031 | [[ODBC与JDBC]] | covered |
| DB-A032 | [[对象持久化与ORM]]（`SE-A031`）；数据库 [[ORM访问接口]] 仅导航 | **link_only** |
| DB-A033 | [[NoSQL分类与特点]] | covered |
| DB-A034 | [[NoSQL体系框架与适用场景]] | covered |

最终逐行复算：

| 状态 | 数量 |
| --- | ---: |
| stable | 34 |
| covered | 33 |
| partial | 0 |
| unmapped | 0 |
| link_only | 1 |
| blocked | 0 |
| **coverage satisfied** | **34/34** |

因此：

> **数据库知识域 = `coverage_complete / quality_pending`。**

这里的“34/34”表示 34 个稳定 Atom 全部有合法覆盖闭环；不把合法 `link_only` 伪写成 `covered`。

## 五、正文复习标记

本轮实际修改的 4 个数据库知识正文均写入 `review_status: 待复习`，防止覆盖修复后被误认为无需人工回看：

- [[数据库DB-DBMS-DBS]]
- [[关系模型基本术语与完整性]]
- [[关系代数基础运算]]
- [[ORM访问接口]]

本轮只关闭 coverage 缺口，不宣告统一质量三轮完成。

## 六、共享控制面回填口径

数据库联合验收通过后，只允许把与 DB 覆盖事实直接相关的控制面改为：

- 05 数据库：`coverage_complete / quality_pending`；
- 事实：`34 = 33 covered + 1 legal link_only`；`partial/unmapped/blocked=0`；
- 当前全局 coverage **仍未通过**；
- 剩余覆盖阻断至少为：01 顶层契约、07 顶层契约；
- 下一唯一接力：`G3-CS-CONTRACT`。

不得直接进入 `G4-COVERAGE-FINAL-RERUN`。

## 七、Git 与验收说明

本记录所在提交必须满足：

- 父提交为提交前重新确认的远端最新 `main`；
- 禁止 force push；
- 只 fast-forward 更新 `main`；
- 提交后以 GitHub commit/compare 回读验证最终 SHA、parent 与实际修改文件。

当前连接器不提供仓库工作树或 shell，因此无法在提交前真实执行 `node scripts/check-vault.mjs` 与 `git diff --check`；本轮不虚报这两个检查。替代执行的是：Markdown/YAML 结构人工复核、稳定 Atom 逐项复算、Git tree/commit/compare 回读；提交后的 CI 状态若存在再另行读取。

## 八、下一轮唯一接力点

> **`G3-CS-CONTRACT：计算机系统基础知识一级范围稳定 Atom 契约建立与真实缺口审计`**

启动时仍必须从届时远端最新 `main` 重新建立事实，不能机械沿用本轮 SHA。
