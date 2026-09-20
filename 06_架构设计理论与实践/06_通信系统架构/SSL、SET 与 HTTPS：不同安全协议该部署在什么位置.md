---
type: 考点
subject: 系统架构设计师
chapter: 通信系统架构
topic: SSL SET HTTPS 部署边界
status: 学习中
difficulty: 2
source: 系统架构设计师教程第二版 PDF 637-648
exam_priority: P2
review_level: 了解
priority_reason: 大纲和主教材明确安全协议部署边界，当前缺少足够近年直接题频证据。
priority_updated: 2026-09-20
review_status: 待复习
tags: [软考/架构设计师, 通信系统架构, SSL, HTTPS, SET]
---

# SSL、SET 与 HTTPS：不同安全协议该部署在什么位置

> [!summary]- 快速复习卡片（学完再看）
> **核心结论**：HTTPS 是 HTTP 运行在 TLS/SSL 保护之上的 Web 访问方式；SET 是面向银行卡支付交易的历史协议语境，不能和 HTTPS 混成同一用途。
> **题干信号 → 第一反应**：浏览器到网站的安全 Web 访问 → HTTPS；支付参与方和银行卡交易流程 → SET 语境。

安全协议要跟业务接口一起部署。**HTTPS 用 TLS/SSL 给 Web 访问提供传输保护；SET 面向支付交易的参与方和流程，二者都不能代替网络隔离、权限控制或服务端业务校验。**

题目问“网站登录、浏览器、HTTP 加密”先锁定 HTTPS；问“银行卡支付专用协议语境”再识别 SET。不要把“使用 HTTPS”写成整个系统已经安全。

## 自测

1. 浏览器访问网站且题干强调 HTTP 加密，优先判断什么？

> [!answer]- 第 1 题答案与解析
> **答案**：HTTPS。
> **解析**：HTTPS 是 HTTP 在 TLS/SSL 保护下的 Web 访问方式。
