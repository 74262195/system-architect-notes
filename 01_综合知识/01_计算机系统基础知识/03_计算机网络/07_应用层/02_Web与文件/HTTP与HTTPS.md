---
type: 考点
subject: 系统架构设计师
chapter: 计算机网络
topic: HTTP 与 HTTPS
status: 学习中
difficulty: 2
source: 教材+常见协议题
aliases: [HTTP, HTTPS, Web]
tags:
  - 软考/架构设计师
  - 软考/计算机网络
exam_priority: P2
review_level: 了解
priority_reason: "Web 协议基础；当前只掌握用途、应用层定位和常见端口，不进入报文头或 TLS 握手细节"
priority_updated: 2026-09-05
quality_reviewed: 2026-09-05
---

# HTTP 与 HTTPS：找到服务器以后，浏览器怎样和它交换 Web 数据

> [!summary] 快速复习卡片
> **作用/定位**：规定 Web 客户端与服务器怎样交换请求和响应。
> **核心结论**：HTTP/HTTPS 都属于应用层；HTTP 常见端口 80，HTTPS 常见端口 443；HTTPS 在 HTTP 通信外增加 TLS 安全保护。
> **经典题型怎么做 / 题干怎么认**：网页、浏览器请求、80 → HTTP；加密 Web、证书、443 → HTTPS。
> **易错点 / 考试重点**：DNS 负责先找到服务器 IP，HTTP/HTTPS 才负责后续 Web 业务；当前不展开 TLS 握手和 HTTP 版本细节。

## 打开网页时它和 DNS 的关系

1. DNS 把域名解析为 IP；
2. 建立网络/传输层通信；
3. HTTP/HTTPS 交换真正的 Web 请求与响应。

所以：

> **DNS 是“找到谁”，HTTP 是“找到以后谈什么业务”。**

## HTTP 与 HTTPS 只记这层区别

- HTTP：Web 请求/响应协议；
- HTTPS：在安全传输保护下使用 HTTP；
- 常见端口：80 / 443。

不进入：HTTP 方法全集、状态码全集、TLS 密码套件和握手字段。

## 一句话总结

**DNS 先找到服务器，HTTP/HTTPS 再和服务器交换 Web 数据；HTTPS 多了安全保护。**

## 下一站

- [[DNS域名解析]]
- [[应用层协议功能与端口识别]]
