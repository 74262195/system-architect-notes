---
type: 考点
subject: 系统架构设计师
chapter: 信息安全技术
topic: VPN
difficulty: 2
source: 教材
updated: 2026-08-28
tags:
  - 系统架构师
  - 系统架构师/信息安全
  - 系统架构师/信息安全/网络安全
priority: ⭐⭐
status: 学习中
created: 2026-08-03 星期一
exam_priority: P1
review_level: 重点
priority_reason: "历年常考或核心前置"
priority_updated: 2026-09-01
quality_reviewed: 2026-09-05
quality_status: 已复核-修正IPSec与SSL VPN绝对化
---
# VPN：怎样在不可信公网之上建立受保护的逻辑连接

> [!summary] 快速复习卡片
> **作用/定位**：利用隧道、认证、加密等机制，把远程用户或网络连接成受保护的逻辑专用网络。
> **核心结论**：IPsec 属于 IP 层安全机制；AH 不提供机密性，ESP 可提供机密性并可配合完整性/认证保护。
> **题干怎么认**：IPsec、AH/ESP、传输/隧道模式、站点互联、远程接入。
> **易错点**：“SSL VPN = 浏览器免客户端”“ESP 永远同时提供全部安全服务”都过于绝对。

## IPsec 的两个常见协议

- **AH**：提供数据源认证和完整性等保护，不提供加密机密性。
- **ESP**：核心能力包括机密性；根据所选算法/配置，还可以提供完整性和认证等保护。

## 两种模式

- **传输模式**：主要保护原 IP 报文的上层载荷，原 IP 头仍用于路由。
- **隧道模式**：把整个原 IP 包封装到新的 IP 包中，常用于网关到网关/站点到站点。

## SSL/TLS VPN 怎么理解

教材/经典题常把 IPsec VPN 与 SSL VPN 按层次和使用场景对比：IPsec 更接近网络层透明保护，SSL/TLS VPN 更接近基于 TLS 的远程应用/接入。

工程实现中 SSL/TLS VPN 既可能是浏览器门户，也可能需要客户端建立全隧道，因此不要把“SSL VPN 一定免客户端”当定义。

## 自测

1. AH 与 ESP 最稳定的区分点是什么？
2. 为什么站点到站点常使用隧道模式？
3. “SSL VPN 一定工作在应用层且无需客户端”为什么只能作为经典简化口径？

## 下一站
- 上一篇：[[IDS与IPS]]
- 下一篇：[[TLS与HTTPS]]
