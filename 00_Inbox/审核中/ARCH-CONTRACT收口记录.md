---
type: 收口记录
subject: 系统架构设计师
batch: ARCH-CONTRACT
status: closed
start_head: 51156f22c40208a8e6c3d67b09add8cbd8ec5663
end_head: 本批提交SHA见Git历史与会话交付
next_batch: ARCH-01-IS-BUILD
updated: 2026-09-16
tags: [软考/架构设计师, 收口, ARCH, coverage]
---

# ARCH-CONTRACT 收口记录

> [!note] 历史记录
> 本文件保留当时事实；最终契约已由 [[OPT-01-CONTRACT收口记录]] 与 [[ARCH-架构设计理论与实践覆盖契约矩阵]] 取代。

## 一、本轮目标

本轮只完成：

**八大架构域大纲原子化 → stable Atom 契约 → 现有正文复用映射 → 正式 coverage 统计 → 物理目录方案锁定。**

没有批量生成八大域正文。

## 二、证据基线

运行时 `START_HEAD`：

`51156f22c40208a8e6c3d67b09add8cbd8ec5663`

已重新读取：

- `AGENTS.md`
- `prompts/00-全局写作规范.md`
- `prompts/20-章节检查与重构.md`
- `prompts/65-教材证据与笔记校验.md`
- `prompts/66-章节三轮审查.md`
- `官方教材/AI教材库/README.md`
- `教材索引.md`
- `抽取报告.md`
- 考试大纲 PDF 62～71 页对应 AI 文本
- 主教材第 12～19 章相关文本
- 现有信息系统、软件架构、安全、网络、云计算与大数据正文候选

范围证据确认：八大域不是互联网扩展，而是考试大纲“系统架构设计案例分析”明确范围；主教材也将其完整展开为第 12～19 章。

## 三、stable Atom 契约

最终锁定：

- 信息系统架构：8
- 层次式架构：8
- 云原生架构：10
- SOA：9
- 嵌入式系统架构：9
- 通信系统架构：10
- 安全架构：10
- 大数据架构：4

总计：**68 stable Atom**。

正式 coverage：

- covered = **0**
- legal link_only = **10**
- partial = **15**
- unmapped = **43**
- blocked = **0**

完整逐 Atom 事实源：[[ARCH-架构设计理论与实践覆盖契约矩阵]]。

## 四、为什么没有把已有知识直接算 covered

现有正文大量属于基础技术主事实源：

- 架构风格有分层、C/S、事件系统；
- 信息系统有 CSF/SST/BSP、EAI、面向服务方法；
- 信息安全已有安全模型、WPDRRC、OSI、数据库安全和脆弱性基础；
- 未来信息技术已有云计算和大数据基础。

但本轮检查的是“架构设计理论与实践”的最小考试闭环。只有基础定义或技术原理，没有架构层的**组织关系、设计动作、边界和取舍**时，只能记 `partial`；完全没有架构落点则 `unmapped`。

因此没有制造虚假 covered 数字。

## 五、10 个合法 link_only

正式保留：

- ARCH-IS-A007 → CSF / SST / BSP 既有主事实源
- ARCH-EMB-A007 → ABSD 既有主事实源
- ARCH-SEC-A002 → 安全模型
- ARCH-SEC-A003 → 安全三体系
- ARCH-SEC-A004 → WPDRRC
- ARCH-SEC-A006 → OSI 安全体系
- ARCH-SEC-A007 → 数据库安全与完整性
- ARCH-SEC-A008 → 软件脆弱性定义/生命周期
- ARCH-SEC-A009 → 软件脆弱性分析方法
- ARCH-BIG-A001 → 大数据问题/特征/处理链

其中安全域复用最多，因此后续 `ARCH-07-SECURITY-BUILD` 只补 3 个 partial，不重复造第二套信息安全笔记。

## 六、微服务与跨域主事实源

锁定：

- `ARCH-CN-A003` = **微服务唯一完整主事实源**；
- `ARCH-SOA-A007` = 只讲 `SOA → 微服务` 演化与边界，后续链接到 CN-A003；
- 微服务与容器、Service Mesh、分布式事务、可观测性分别建立独立关系；
- 云计算 ≠ 云原生；
- 大数据基础 ≠ Lambda/Kappa 架构。

详细见 [[ARCH-架构关系矩阵]]。

## 七、物理目录决策

真实仓库已经稳定占用：

`01_综合知识 / 02_案例分析 / 03_论文素材 / 04_真题错题 / 05_画图素材`

若强行把架构主干改成物理 `02_`，会触发大量 wikilink、Excalidraw、Dataview、脚本和案例回链迁移。

因此锁定：

> **物理根目录：`06_架构设计理论与实践/`**

逻辑课程顺序仍是：

`综合知识 → 架构设计理论与实践 → 案例分析 → 论文`

本轮只创建架构主干索引，不创建八个空目录。

## 八、仓库校验脚本同步

`check-vault.mjs` 的一级学习目录检查范围同步加入：

`06_架构设计理论与实践`

并允许执行前置文件路径校验识别：

`06_架构设计理论与实践/*.md`

这样后续新架构正文进入主学习区后，会受到与现有主干一致的 frontmatter 与路径检查。

## 九、本轮边界

本轮没有：

- 重跑 01～13 综合知识 coverage；
- 改动任何综合知识学习正文；
- 批量生成架构正文；
- 移动案例、论文、真题或画图目录；
- 恢复 G5；
- 修改 13 专业英语。

G5 继续 `preserved_paused_by_arch_realign`。

## 十、校验说明

本环境通过 GitHub 连接器直接构建远端 Git tree，没有本地完整 working tree，因此：

- `node scripts/check-vault.mjs`：**未执行**；
- `git diff --check`：**未执行**。

提交前已做远端 HEAD 并发检查；提交后还需通过 commit compare 确认只包含本批控制面、索引与检查脚本修改。

## 十一、下一唯一批次

> **`ARCH-01-IS-BUILD：信息系统架构 8 个 stable Atom 定点建设与验收`**

下一批必须从运行时最新 `main` 重新记录 START_HEAD，并追加读取 `prompts/10-原子考点卡生成.md`。只处理 ARCH-IS 的真实缺口，不提前进入层次式架构。
