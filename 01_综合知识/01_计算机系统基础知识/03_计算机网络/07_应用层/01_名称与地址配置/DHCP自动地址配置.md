---
type: 考点
subject: 系统架构设计师
chapter: 计算机网络
topic: DHCP 自动地址配置
status: 学习中
difficulty: 2
source: 教材+常见协议题
aliases: [DHCP, 自动分配IP, DORA]
tags:
  - 软考/架构设计师
  - 软考/计算机网络
exam_priority: P2
review_level: 了解
priority_reason: "应用层常用协议基础；掌握自动下发网络配置和 DORA 顺序即可"
priority_updated: 2026-09-05
quality_reviewed: 2026-09-05
---

# DHCP 自动地址配置：新主机刚接入网络时 IP 从哪里来

> [!summary] 快速复习卡片
> **作用/定位**：为主机自动提供 IP 地址、子网掩码、默认网关、DNS 等网络配置。
> **核心结论**：DHCP 属于应用层；常见客户端/服务器端口 68/67；基础流程可记 DORA：Discover → Offer → Request → ACK。
> **经典题型怎么做 / 题干怎么认**：自动获取 IP、租约、67/68、Discover/Offer → DHCP。
> **易错点 / 考试重点**：DHCP 是“发配置”，DNS 是“查域名”；不要混成同一个协议。

## 最小流程

1. Discover：客户端寻找 DHCP 服务器；
2. Offer：服务器给出配置方案；
3. Request：客户端请求采用某个方案；
4. ACK：服务器确认租约。

当前只需要掌握流程含义，不进入 DHCP Relay、Option 字段和服务器配置。

## 一句话总结

**DHCP 解决“我刚上线，网络参数从哪里拿”；DNS 解决“这个域名对应哪个 IP”。**

## 下一站

- [[DNS域名解析]]
- [[IP编址与子网划分]]
