---
type: 考点
subject: 系统架构设计师
chapter: 系统质量属性与架构评估
topic: SAAM架构评估
status: 学习中
difficulty: 3
source: 教材+历年真题
aliases: [SAAM, Software Architecture Analysis Method]
tags: [软考/架构设计师, 软考/考点, 软考/综合知识, 软考/质量属性与架构评估]
exam_priority: P0
review_level: 必读
priority_reason: "历史高频且2026H1继续活跃"
priority_updated: 2026-09-01
quality_reviewed: 2026-09-05
quality_status: 已复核-按当前规则补齐
---

# SAAM：怎么用一组场景检查架构到底好不好改

> [!summary] 快速复习卡片
> **作用/定位**：用场景分析架构，经典重点是可修改性。
> **核心结论**：开发场景 → 描述架构 → 单场景评估 → 场景交互 → 总体评估。
> **题干怎么认**：场景技术、可修改性、场景交互、多个场景修改同一构件。
> **易错点**：SAAM 不是 ATAM；前者经典重点偏可修改性，后者强调多质量属性的敏感与权衡。

```mermaid
flowchart LR
    A[开发场景] --> B[描述架构]
    B --> C[单场景评估]
    C --> D[场景交互]
    D --> E[总体评估]
```

单场景评估看现有架构能否直接支持场景，还是必须修改；场景交互则关注多个场景是否反复影响同一构件，这往往意味着变化热点。

## 历年考法落点

题目出现“场景交互”或强调“可修改性场景”时，SAAM 是强识别词。若题目继续强调性能、安全、可用性之间的折中，则更可能转向 ATAM。

## 自测
1. SAAM 中为什么要专门分析场景交互？
2. SAAM 与 ATAM 的第一判断入口分别是什么？

## 下一站
- [[ATAM架构权衡分析]]
- 依据：主教材 PDF 第 295–296 页。
