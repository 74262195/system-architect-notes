---
type: 考点
subject: 系统架构设计师
chapter: 计算机网络
topic: DNS 域名解析
status: 学习中
difficulty: 2
source: 教材+常见协议题
aliases: [DNS, 域名解析]
tags:
  - 软考/架构设计师
  - 软考/计算机网络
exam_priority: P2
review_level: 了解
priority_reason: "应用层常用协议基础；掌握域名到IP的作用和53端口即可"
priority_updated: 2026-09-05
quality_reviewed: 2026-09-05
---

# DNS 域名解析：浏览器为什么能把域名变成服务器 IP

> [!summary] 快速复习卡片
> **作用/定位**：把便于人记忆的域名解析成网络通信需要的 IP 地址。
> **核心结论**：DNS 属于应用层，常用端口 53；它解决“域名 → IP”，不负责 IP → MAC。
> **经典题型怎么做 / 题干怎么认**：域名解析、主机名查询、53 → DNS。
> **易错点 / 考试重点**：DNS 与 ARP 不同：DNS 找 IP，ARP 找当前链路 MAC。

## 打开网站时 DNS 在哪一步

访问 `example.com` 时，应用先需要知道服务器 IP；得到 IP 后，后续才进入路由、ARP、TCP/UDP 等网络传输流程。

因此顺序可以理解为：

`域名 → DNS 得到 IP → 网络传输 → 访问应用服务`

## 一句话总结

**DNS 只回答一个核心问题：这个名字对应哪个 IP。**

## 下一站

- [[ARP地址解析]]
- [[HTTP与HTTPS]]
