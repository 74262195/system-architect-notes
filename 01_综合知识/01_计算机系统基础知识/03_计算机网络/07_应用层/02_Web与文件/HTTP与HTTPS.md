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
quality_status: 已通过问题闭环与主下一站复核
---

# HTTP 与 HTTPS：找到服务器以后，浏览器怎样和它交换 Web 数据

> [!summary] 快速复习卡片
> **作用/定位**：承接 DNS 已找到服务器 IP，规定 Web 客户端与服务器怎样交换请求和响应。
> **核心结论**：HTTP/HTTPS 都属于应用层；HTTP 常见端口 80，HTTPS 常见端口 443；HTTPS 在 HTTP 业务外增加 TLS 安全保护。
> **经典题型怎么做 / 题干怎么认**：网页、浏览器请求、80 → HTTP；加密 Web、证书、443 → HTTPS。
> **易错点 / 考试重点**：DNS 负责先找到服务器 IP，HTTP/HTTPS 才负责 Web 业务；当前不展开 TLS 握手和 HTTP 版本细节。

## 先直接回答：DNS 已经找到服务器，为什么还需要 HTTP

上一站 [[DNS域名解析]] 只解决了“网站服务器在哪里”。

但浏览器找到服务器以后，还要约定：

- 怎样发起一个 Web 请求；
- 服务器怎样返回页面或其他资源；
- 双方怎样表示请求和响应。

HTTP 就是 Web 客户端与服务器之间的应用层请求/响应协议。

可以把打开网页压成：

> **DNS 找到服务器 → TCP/UDP 等下层完成传输 → HTTP/HTTPS 交换真正的 Web 业务数据。**

## HTTPS 又多解决了什么

普通 HTTP 只规定 Web 业务怎样交换，本身不等于提供完整的加密保护。

HTTPS 可以理解为：**HTTP 业务运行在 TLS 提供的安全传输保护之上**，从而为通信提供机密性、完整性和服务器身份验证等能力。

在本章只记定位：

- HTTP：Web 请求/响应，常见端口 80；
- HTTPS：受 TLS 保护的 Web 通信，常见端口 443。

TLS 的密码学细节回信息安全章节，不在这里重复。

## 为什么下一站是 FTP

HTTP/HTTPS 已经展示了一种应用层业务：浏览网页。

接下来换一个稳定考试识别项：如果题目不问网页，而明确说“专门上传/下载文件”，应该想到哪个协议？这就是 FTP。

## 一句话总结

**DNS 先找到服务器，HTTP/HTTPS 再交换 Web 数据；HTTPS 比 HTTP 多了 TLS 安全保护。**

## 下一站

**上一站：[[DNS域名解析]]**  
**主下一站：[[FTP文件传输]]**

为什么继续学它：Web 协议已经会认，下一步切换到“专门传文件”的应用层协议，建立不同业务对应不同协议的判断习惯。
