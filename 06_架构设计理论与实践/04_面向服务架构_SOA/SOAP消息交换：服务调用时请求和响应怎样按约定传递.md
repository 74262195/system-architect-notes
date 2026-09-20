---
type: 考点
subject: 系统架构设计师
chapter: 面向服务架构 SOA
topic: SOAP 消息交换
status: 学习中
difficulty: 2
source:
  - 官方教材/系统架构第二版 大纲.pdf（PDF 66 页）
  - 官方教材/系统架构设计师教程第二版可搜索.pdf（PDF 540 页）
aliases: [SOAP, 简单对象访问协议]
tags: [软考/架构设计师, 软考/考点, 架构设计理论与实践, 面向服务架构]
exam_priority: P1
review_level: 理解
priority_reason: "大纲明确展开，且是传统 Web 服务消息交换的核心识别点"
priority_updated: 2026-09-20
review_status: 待复习
---

# SOAP消息交换：服务调用时请求和响应怎样按约定传递

> [!summary]- 快速复习卡片（学完再看）
> **SOAP**：用于 Web 服务消息交换的规范，强调简单性和可扩展性。
> **不要混淆**：SOAP 是消息交换规范；WSDL 是接口说明；UDDI 是服务发现目录。

## 服务两端为什么要按同一种“信封”传消息

两个系统可能用不同语言实现。若请求和响应没有共同格式，双方就很难可靠解析对方传来的内容。

**SOAP 提供的是 Web 服务消息交换的约定，而不是业务功能本身。**教材说明它的主要设计目标是简单性和可扩展性。

```mermaid
sequenceDiagram
    participant C as 调用方
    participant S as 服务提供者
    C->>S: SOAP 请求消息
    S->>C: SOAP 响应消息
```

SOAP 不负责告诉你“服务有哪些操作和地址”——那是 WSDL；也不负责替你找到服务——那是 UDDI。题干问消息封装、请求/响应交换、简单和可扩展时，才定位 SOAP。

## 自测

1. Web 服务间按统一消息规范传递请求和响应，且强调简单、可扩展，是什么？

> [!answer]- 第 1 题答案与解析
> **答案**：SOAP。
> **解析**：SOAP 是 Web 服务的消息交换规范，不是服务目录或接口说明。
