---
type: 考点
subject: 系统架构设计师
chapter: 计算机网络
topic: ARP 地址解析
status: 学习中
difficulty: 2
source: TCP/IP基础+历年题型
aliases: [ARP, 地址解析协议, IP到MAC]
tags:
  - 软考/架构设计师
  - 软考/计算机网络
exam_priority: P2
review_level: 了解
priority_reason: "ARP 是 IP 与以太网之间的基础衔接知识；掌握作用即可，不扩展缓存攻击或报文字段"
priority_updated: 2026-09-05
quality_reviewed: 2026-09-05
---

# ARP 地址解析：知道目标 IP 后，当前这一跳的 MAC 从哪里来

> [!summary] 快速复习卡片
> **作用/定位**：在 IPv4 局域网中，根据目标 IP 找到当前链路要使用的 MAC 地址。
> **核心结论**：同网段通信时解析目标主机 MAC；跨网段通信时，主机真正需要解析的是**默认网关/下一跳的 MAC**。
> **经典题型怎么做 / 题干怎么认**：IP 已知但不知道二层地址、ARP 请求/应答、ARP 缓存 → ARP。
> **易错点 / 考试重点**：ARP 不负责域名解析；DNS 是域名 → IP，ARP 是当前链路 IP → MAC；交换机未知单播泛洪也不是“ARP 泛洪”。

## 为什么有 IP 还不够

主机发送 IP 分组时，最终还要把它封装进当前局域网的二层帧。帧需要目的 MAC，所以必须知道这一跳该把帧交给谁。

## 同网段与跨网段

### 同网段

A 要访问 B：

1. A 已知 B 的 IP；
2. ARP 查询 B 的 MAC；
3. 帧目的 MAC 写 B 的 MAC。

### 跨网段

A 要访问远程服务器 C：

1. A 发现 C 不在本地子网；
2. A 把 IP 分组交给默认网关；
3. ARP 查询的是**默认网关接口的 MAC**；
4. IP 目的地址仍然是远程服务器 C。

> **跨网段时：IP 目标不变，当前帧的 MAC 目标是下一跳。**

## 和 DNS 的区别

| 协议 | 解决的问题 |
| --- | --- |
| DNS | 域名 → IP |
| ARP | 当前 IPv4 链路 IP → MAC |

## 一句话总结

**DNS 帮你找到目标 IP，ARP 帮当前这一跳找到该写进帧里的 MAC。**

## 下一站

- [[IP编址与子网划分]]
- [[MAC地址与交换机转发表]]
- [[ICMP与Ping]]
