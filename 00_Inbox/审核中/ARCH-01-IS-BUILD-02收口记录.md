---
type: 架构建设记录
subject: 系统架构设计师
status: closed
batch: ARCH-01-IS-BUILD-02
start_head: 796a8dd40ba884fe629d2bf4b5ff469b5da168f3
atoms: [ARCH-IS-A002, ARCH-IS-A003, ARCH-IS-A004]
updated: 2026-09-18
tags: [软考/架构设计师, 审查/全库补全, ARCH, 信息系统架构]
---

# ARCH-01-IS-BUILD-02 收口记录

## 本轮唯一批次

`ARCH-01-IS-BUILD-02：信息系统架构正文建设第二批`

只处理：

- `ARCH-IS-A002`：信息系统常用架构模型；
- `ARCH-IS-A003`：企业信息系统总体框架；
- `ARCH-IS-A004`：TOGAF 定位与 ADM 架构开发过程。

未触碰 A005 以后正文，未跨到层次式/云原生/SOA 等其他架构域。

## START_HEAD

`796a8dd40ba884fe629d2bf4b5ff469b5da168f3`

运行时重新读取最新 `main` 建立事实，没有沿用上一轮 SHA。

## 规则与控制面

本轮读取：

- `AGENTS.md`
- `prompts/00-全局写作规范.md`
- `prompts/10-原子考点卡生成.md`
- `prompts/60-历年真题解析与索引.md`
- `prompts/65-教材证据与笔记校验.md`
- `00_Inbox/审核中/全库补全总控计划.md`
- `00_Inbox/审核中/ARCH-架构设计理论与实践覆盖契约矩阵.md`
- `00_Inbox/审核中/QUALITY-HARDENING-全库质量债矩阵.md`
- `00_Inbox/审核中/ARCH-八域案例入口与理论Atom映射.md`
- `00_Inbox/审核中/ARCH-01-IS-代表样稿记录.md`
- 当前章节索引、A001 代表样稿和综合知识 C/S 前置正文。

范围约束继续成立：

- 01 计算机系统基础知识保持 `study_complete / user_accepted / coverage_audit_skipped`，未重开；
- 13 专业英语继续 `out_of_future_plan_by_user`，未作为缺口或 blocker；
- QUALITY 当前开放债为 0，本轮不制造新的 QUALITY 批次；
- 案例入口继续 `mapped / content_pending`，本轮不提前建设 G5。

## 证据与优先级

### 大纲

`官方教材/系统架构第二版 大纲.pdf` PDF 62–63 明确列出：

- 信息系统常用四种架构模型；
- 企业信息系统总体框架及战略/业务/应用/信息基础设施；
- TOGAF 与 ADM，包含 ADM 定义、阶段划分和详细活动。

### 主教材

- A002：`官方教材/系统架构设计师教程第二版可搜索.pdf` PDF 427–431；
- A003：同教材 PDF 431–433；
- A004：同教材 PDF 433–444。

### 真题/趋势

`第二阶段-考点映射与近年趋势` 显示：

- 企业信息化/EAI/ERP 仍有近年信号；
- SOA/REST/Web 架构仍活跃；
- 但没有足够可靠的 Atom 级直接证据把 A002/A003 提升为高优先级。

因此保持正式契约既有优先级：

- A002 = P2；
- A003 = P2；
- A004 = P1。

## 实际正文

新增：

1. `信息系统常用架构模型：从单机到企业数据交换总线.md`
   - 用“独立应用边界 + 应用怎样协作”统一四种模型；
   - 解释单机、C/S、B/S 边界、SOA、多应用公共交换总线；
   - 复用综合知识 04B 的请求/响应前置，不复制通用风格正文。

2. `企业信息系统总体框架：为什么不能只画应用系统.md`
   - 建立战略、业务、应用、信息基础设施四部分；
   - 强化“业务系统 ≠ 应用系统”；
   - 用“战略定方向、业务定活动、应用做支撑、基础设施托底座”形成考试动作。

3. `TOGAF与ADM：怎样按步骤开发企业架构.md`
   - 明确 TOGAF 与 ADM 不是同义词；
   - 建立预备阶段、A～H、需求管理主链；
   - 强化 E/F、G/H 等易混边界；
   - 说明 ADM 三层迭代概念和题干动作定位。

三篇学习笔记均设置 `review_status: 待复习`。

## coverage 变化

- A002：`partial → covered`
- A003：`unmapped → covered`
- A004：`unmapped → covered`

ARCH-IS：

- 原：`1 covered + 1 link_only + 3 partial + 5 unmapped`
- 现：`4 covered + 1 link_only + 2 partial + 3 unmapped`

ARCH 全局：

- 原：`1 covered + 9 link_only + 15 partial + 99 unmapped`
- 现：`4 covered + 9 link_only + 14 partial + 97 unmapped`

案例映射数量与状态未改变。

## 导航与控制面

已同步：

- 信息系统架构索引；
- 架构设计理论与实践总索引；
- ARCH 正式覆盖契约矩阵；
- 全库补全总控计划。

A001～A004 当前形成连续学习链：

`整体架构视角 → 常用架构模型 → 企业总体框架 → TOGAF/ADM`

## 并发复核

在控制面完成后，从 START_HEAD 比较到当时最新 HEAD：

- status = `ahead`
- behind_by = `0`
- 变化文件只包含本批次预期的 3 篇正文 + 4 个控制/索引文件；
- 未发现其他会话混入的并发文件变化。

## 检查说明

当前 GitHub 连接器环境不能执行本地仓库命令，因此：

- `node scripts/check-vault.mjs`：**未执行**
- `git diff --check`：**未执行**

不得视为脚本已通过。

已通过远端内容复核替代检查：

- 三篇文件均真实存在；
- 三篇 frontmatter 均有 `review_status: 待复习`；
- A002 → A003 → A004 导航连续；
- 覆盖矩阵和总控统计一致；
- QUALITY、案例、01 计算机系统基础、13 专业英语状态无回归。

## 下一轮候选

`ARCH-01-IS-BUILD-03：信息化总体架构方法主线建设`

优先：

- `ARCH-IS-A005` 信息化概念与建设特征；
- `ARCH-IS-A009` 数据导向与流程导向架构比较；
- `ARCH-IS-A006` 信息化建设生命周期。

## 下下轮候选

`ARCH-01-IS-BUILD-04`

候选处理：

- `ARCH-IS-A007` CSF/SST/BSP 的 link_only 复用核验；
- `ARCH-IS-A008` 信息化资源管理；
- `ARCH-IS-A010` 信息化标准、法律与规定的架构约束。

具体仍以运行时最新 `main` 和总控为准。
