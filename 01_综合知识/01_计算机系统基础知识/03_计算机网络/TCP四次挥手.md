---
type: 考点
subject: 系统架构设计师
chapter: 计算机网络
topic: TCP 四次挥手
status: 学习中
difficulty: 3
source: 教材
aliases: [四次挥手, FIN, 连接释放]
tags:
  - 软考/架构设计师
  - 软考/考点
  - 计算机网络/TCP
exam_priority: P1
review_level: 重点
priority_reason: "历年常考或核心前置"
priority_updated: 2026-09-01
---

# TCP 四次挥手：建立连接三次，关闭为什么通常要四次

## 先定位：TCP 是全双工连接，两个方向可以分别关闭

一条 TCP 连接里：

- A 可以向 B 发数据；
- B 也可以向 A 发数据。

因此：

> **A 说“我发完了”，不代表 B 也已经发完。**

这就是连接释放通常需要分两边处理的原因。

## 经典过程

```mermaid
sequenceDiagram
    participant A as 主动关闭方
    participant B as 被动关闭方
    A->>B: FIN，我这个方向发完了
    B->>A: ACK，知道了
    B->>A: FIN，我也发完了
    A->>B: ACK，确认
```

## 为什么中间的 ACK 和 FIN 常分开

B 收到 A 的 FIN 时：

> 可以确认 A 不再发送。

但 B 自己可能还有数据要发。

所以 B 先 ACK，不一定马上 FIN。

等 B 也完成发送后，再单独发 FIN。

因此经典关闭流程通常表现为四次报文交互。

## 和三次握手不要用“3 对 4”死背

- 建立：双方 SYN 信息可以在第二次里把“确认 + 自己的 SYN”合在一起；
- 关闭：收到对方 FIN 时，自己未必同时准备关闭发送方向，因此 ACK 和 FIN 往往分开。

## 一句话记住

> **四次挥手的根本原因是全双工两个方向可以独立结束。**

## 下一站

- 上一站：[[TCP流量控制与拥塞控制]]
- 下一站：[[应用层常用协议]]
