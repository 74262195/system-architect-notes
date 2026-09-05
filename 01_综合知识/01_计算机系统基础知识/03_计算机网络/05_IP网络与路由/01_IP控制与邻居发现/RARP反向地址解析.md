---
type: 考点
subject: 系统架构设计师
chapter: 计算机网络
topic: RARP 反向地址解析
status: 学习中
difficulty: 1
source: 官方教程第2版
aliases: [RARP, 反向地址解析协议]
tags:
  - 软考/架构设计师
  - 软考/计算机网络
exam_priority: P3
review_level: 暂不复习
priority_reason: "官方教程 TCP/IP 协议集明确列出 RARP，但属于历史协议；只保留方向识别，避免形成额外学习负担"
priority_updated: 2026-09-05
quality_reviewed: 2026-09-05
---

# RARP 反向地址解析：只需要知道它和 ARP 的方向相反

> [!summary] 快速复习卡片
> **作用/定位**：官方教程 TCP/IP 协议集中保留的历史协议，用于根据物理地址取得 IP 地址。
> **核心结论**：ARP：IP → MAC；RARP：MAC → IP。
> **经典题型怎么做 / 题干怎么认**：题目直接问“反向地址解析”“MAC 地址转换为 IP” → RARP。
> **易错点 / 考试重点**：不要把 RARP 当成今天自动分配地址的主流方案；现代自动网络配置更常见的是 DHCP。

## 学到哪里就停

只记：

- ARP：IP → MAC；
- RARP：MAC → IP；
- RARP 属于历史识别项。

不学习 RARP 报文格式、服务器部署或实现流程。

## 一句话总结

**ARP 正向找 MAC，RARP 反向找 IP；RARP 只做教材历史识别。**

## 下一站

- [[ARP地址解析]]
- [[DHCP自动地址配置]]
