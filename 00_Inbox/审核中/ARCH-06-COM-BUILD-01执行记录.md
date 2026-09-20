---
type: 执行记录
subject: 系统架构设计师
chapter: 通信系统架构
batch: ARCH-06-COM-BUILD-01
status: completed
date: 2026-09-20
source: 大纲 PDF 68 + 主教材 PDF 616-618、630-631、643-645
tags: [软考/架构设计师, 架构设计理论与实践, 通信系统架构, 执行记录]
---

# ARCH-06-COM-BUILD-01 执行记录

## 范围与结果

| Atom | 原状态 | 正文 | 结果 |
| --- | --- | --- | --- |
| ARCH-COM-A001 | unmapped | [[局域网架构模式：小网络怎样在简单、可靠和可扩展之间取舍]] | covered |
| ARCH-COM-A002 | partial | [[网关冗余协议：默认网关故障后怎样让终端仍能出网]] | covered |
| ARCH-COM-A011 | unmapped | [[STP 与 LACP：二层冗余链路怎样既不成环又能增加容量]] | covered |
| ARCH-COM-A012 | unmapped | [[OSPF、RIP 与 BGP：三层路由协议怎样按管理范围分工]] | covered |
| ARCH-COM-A013 | unmapped | [[网络协议组合与选型：不同层的协议怎样一起解决一张网的问题]] | covered |

五篇分别承担局域网模式、虚拟网关、二层多链路、三层动态路由、组合选型五个独立主问题；既有计算机网络章节只作为协议机制前置，不重复复制完整正文。

## 证据与边界

- 大纲 PDF 68 将通信系统架构列为范围；主教材 PDF 616-618 给出四种局域网架构及 VRRP/HSRP/GLBP、STP/LACP、OSPF/RIP/BGP 的分层应用。
- 主教材 PDF 630-631 将 OSPF/BGP 等纳入高可用网络的路由和检测协作；PDF 643-645 以园区网说明 STP、VRRP 和 OSPF 在不同层的组合，不把任一协议写成万能可靠性方案。
- 原全局汇总的 `unmapped_count: 30` 与域行之和不一致；本次按 124 个 stable Atom 重算并修正为构建前 32、本批后 28，未改变任何 Atom 范围。

## 下一批

通信系统架构现在为 `5 covered + 1 partial + 13 unmapped`。下一批处理 ARCH-COM-A003/A004/A005/A006：广域网架构、移动通信与 5G 边缘、存储网络和 SDN。
