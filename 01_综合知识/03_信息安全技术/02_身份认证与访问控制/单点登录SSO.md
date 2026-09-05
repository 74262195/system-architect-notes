---
type: 考点
subject: 系统架构设计师
chapter: 信息安全技术
topic: 单点登录SSO
difficulty: 2
source: 教材
updated: 2026-08-28
tags:
  - 系统架构师
  - 系统架构师/信息安全
  - 系统架构师/信息安全/认证
priority: ⭐
status: 学习中
created: 2026-08-03 星期一
exam_priority: P1
review_level: 重点
priority_reason: "历年常考或核心前置"
priority_updated: 2026-09-01
quality_reviewed: 2026-09-05
quality_status: 已复核-修正OAuth与JWT定位
---
# 单点登录 SSO：为什么登录一次后多个系统可以共享认证结果

> [!summary] 快速复习卡片
> **作用/定位**：SSO 是“一个认证会话让多个受信任系统复用身份结果”的目标/能力。
> **核心结论**：SSO 不等于某一种协议；常见实现包括 Kerberos、SAML、OIDC、CAS 等。
> **题干怎么认**：一次登录、多系统免重复认证、统一身份提供方/认证中心。
> **易错点**：OAuth 2.0 本身是授权框架；OIDC 才在 OAuth 2.0 之上定义身份认证。JWT 只是令牌格式，不等于 SSO 协议。

## SSO 解决的矛盾

多个业务系统如果各自保存账号和登录状态，用户要反复登录，企业也难统一身份治理。SSO 把认证集中到可信身份系统，业务系统通过票据、断言或令牌接受认证结果。

## 常见实现怎么定位

| 机制 | 主要定位 |
| --- | --- |
| Kerberos | 基于票据和对称密钥的企业认证，可支持 SSO |
| SAML | 常用于企业 Web 联邦身份，传递认证断言 |
| OIDC | 基于 OAuth 2.0 的身份认证层，常用于现代 Web/App 登录 |
| CAS | 集中认证式 SSO 方案 |

“使用 JWT”只能说明某系统可能使用 JSON Web Token 承载声明，不能仅凭 JWT 判断整个 SSO 协议。

SSO 也不强制后台一定使用 RBAC；认证回答“你是谁”，授权仍可采用 RBAC、ABAC 或其他模型。

## 自测

1. 为什么 SSO 是目标，而 Kerberos/OIDC 是实现机制？
2. OAuth 2.0 与 OIDC 为什么不能互换名称？

## 下一站
- 上一篇：[[Kerberos认证]]
- 下一篇：[[DAC自主访问控制]]
