---
type: 考点
subject: 系统架构设计师
chapter: 计算机网络
topic: TCP 四次挥手
status: 学习中
difficulty: 3
source: 教材+经典TCP模型
aliases: [四次挥手, FIN, 连接释放]
tags:
  - 软考/架构设计师
  - 软考/考点
  - 计算机网络/TCP
exam_priority: P1
review_level: 重点
priority_reason: "历年常考或核心前置"
priority_updated: 2026-09-01
quality_reviewed: 2026-09-02
quality_status: 已复核
---

# TCP 四次挥手：全双工连接为什么通常要分四步关闭

## 先定位：关闭的是两个独立发送方向

TCP 是全双工连接：

- A 可以向 B 发送；
- B 也可以向 A 发送。

A 发出 FIN 只表示“A 已没有数据要发”，并不表示 B 也发送完毕。因此两个方向通常分别关闭。

## 经典过程

~~~mermaid
sequenceDiagram
    participant A as 主动关闭方
    participant B as 被动关闭方
    A->>B: FIN
    B-->>A: ACK
    Note over B: 仍可继续发送剩余数据
    B->>A: FIN
    A-->>B: ACK
    Note over A: 进入 TIME_WAIT
~~~

1. A 发 FIN，关闭 A→B 的发送方向；
2. B 确认 FIN，但 B→A 仍可继续传数据；
3. B 发送完毕后再发 FIN；
4. A 确认 B 的 FIN，两个方向都完成关闭。

中间 ACK 和 FIN 有时能合并，但经典考试模型通常画成四次。

## TIME_WAIT 为什么不能省

主动关闭方发出最后一个 ACK 后，通常还要在 TIME_WAIT 状态等待 2MSL。这里 MSL 是报文段在网络中的最大生存时间。

等待主要解决两件事：

1. **保证最后 ACK 有机会重传**：若最后 ACK 丢失，被动关闭方会再次发送 FIN，主动关闭方仍能回应；
2. **让旧连接的延迟报文消失**：避免旧报文混入稍后使用相同连接标识的新连接。

TIME_WAIT 不是“连接还在正常传业务”，而是关闭后的保护期。

## 为什么建立常见三次，关闭常见四次

建立连接时，服务器可以把“确认客户端 SYN”和“发送自己的 SYN”合在同一个报文里。

关闭时，收到对方 FIN 的一方可能还有数据未发完，只能先 ACK，稍后再发自己的 FIN，所以通常无法立即合并。

## 易错点

- FIN 表示本方向不再发送，不是双方立刻全部关闭；
- 收到 FIN 后仍可把本方向剩余数据发完；
- TIME_WAIT 通常出现在主动关闭方；
- 四次是经典常见过程，同时关闭等特殊情形的报文序列可能不同，以题设为准。

## 一句话记住

> **全双工要分方向关闭；最后 ACK 后等待 TIME_WAIT，既能补确认，也让旧报文退出网络。**

## 下一站

- 上一站：[[TCP流量控制与拥塞控制]]
- 下一站：[[应用层常用协议]]
