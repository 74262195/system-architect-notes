---
type: 考点
subject: 系统架构设计师
chapter: 信息安全技术
topic: XSS跨站脚本
difficulty: 2
source: 教材
updated: 2026-08-28
tags:
  - 系统架构师
  - 系统架构师/信息安全
  - 系统架构师/信息安全/应用安全
priority: ⭐⭐
status: 学习中
created: 2026-08-03 星期一
exam_priority: P2
review_level: 补充
priority_reason: "属于软件脆弱性与应用安全范围，2020 年案例资料出现 XSS；综合知识直接证据有限"
priority_updated: 2026-09-07
quality_reviewed: 2026-09-05
quality_status: 已复核-补快速复习卡并修正防御表述
---
# XSS 跨站脚本：为什么不可信内容会在用户浏览器里变成代码

> [!summary] 快速复习卡片
> **作用/定位**：不可信数据进入 HTML/JS 等执行上下文，导致浏览器执行攻击者脚本。
> **核心结论**：核心防御是按输出上下文正确编码/安全 DOM API；CSP 是重要纵深手段。
> **题干怎么认**：浏览器执行脚本、评论区/URL 回显、DOM sink、窃取会话信息。
> **易错点**：HttpOnly 只能限制脚本读取 Cookie，不能消灭 XSS；简单过滤 `<script>` 也不是可靠根治。

## 三类经典场景

- **存储型**：恶意内容先进入服务器存储，再返回给其他用户。
- **反射型**：恶意输入随请求进入，立即被页面响应反射出来。
- **DOM 型**：前端脚本把不可信数据写进危险 DOM/脚本上下文，漏洞可主要发生在客户端。

## 防御抓主线

1. 按 HTML、属性、URL、JavaScript 等不同上下文做正确输出编码；
2. 优先使用不会解释为 HTML 的安全 DOM API；
3. 必须允许富文本时使用可靠的 HTML Sanitizer；
4. 配置 CSP、HttpOnly 等做纵深防护。

## 自测

1. 为什么“统一把所有字符 HTML 转义”并不能覆盖所有 JS/URL 上下文？
2. HttpOnly 为什么只能减轻某些后果，而不是根治 XSS？

## 下一站
- 上一篇：[[SQL注入]]
- 下一篇：[[CSRF跨站请求伪造]]
