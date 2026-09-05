---
type: 考点
subject: 系统架构设计师
chapter: 计算机网络
topic: 自治系统与 IGP-BGP
status: 学习中
difficulty: 2
source: 教材+组网基础
aliases: [AS, IGP, BGP, EGP, 域内路由, 域间路由]
tags:
  - 软考/架构设计师
  - 软考/计算机网络
exam_priority: P2
review_level: 了解
priority_reason: "只需掌握 AS 内/AS 间的协议定位，不进入具体动态路由算法"
priority_updated: 2026-09-05
quality_reviewed: 2026-09-05
---

# 自治系统与 IGP-BGP：为什么互联网的路由协议要分“内部”和“外部”

> [!summary] 快速复习卡片
> **作用/定位**：解释动态路由协议为什么按自治系统边界分类。
> **核心结论**：一个自治系统 AS 是由同一管理策略控制的一组网络；AS 内使用 IGP 类协议，AS 之间的核心域间路由协议是 BGP。
> **经典题型怎么做 / 题干怎么认**：自治系统内部、域内 → IGP；运营商/Internet 域间/边界网关 → BGP。
> **易错点 / 考试重点**：IGP 是协议类别，不是单个协议名；当前不背 OSPF 状态机、BGP 属性或复杂选路规则。

## 为什么要有 AS

互联网不是由一个组织统一管理。不同运营商、企业或大型机构各自管理一部分网络，并对内部路由采用自己的策略。

这种管理边界就是自治系统 AS 的核心概念。

## 只记这层关系

- **AS 内**：IGP 类；
- **AS 间**：BGP。

RIP、OSPF 等名称只作为 IGP 的典型例子识别即可。

## 不进入的内容

- OSPF LSA；
- 邻居状态机；
- BGP LOCAL_PREF、MED、AS_PATH 等属性比较；
- 厂商路由配置命令。

## 一句话总结

**一个组织内部用 IGP 思路学路，不同自治系统之间主要靠 BGP 交换路由。**

## 下一站

- [[路由表与最长前缀匹配]]
