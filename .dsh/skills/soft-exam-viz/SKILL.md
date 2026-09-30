---
name: soft-exam-viz
description: 软考系统架构师 Vault 的可视化：正文 Mermaid 教学图、Excalidraw 教学插图与章节导航看板的新建和样式修复。
whenToUse: 用户要求画图、修图、图看不清、Mermaid 渲染报错、Excalidraw 看板维护，或正文需要教学流程图/拓扑图/对比图。
---

# Mermaid 与 Excalidraw 可视化

## 运行时必读

按顺序读取当前 main 上的规则文件（本技能不复述条款）：

1. `AGENTS.md`（可视化硬门禁与画图路由）
2. `prompts/00-全局写作规范.md`
3. `prompts/40-Mermaid与Obsidian样式修复.md`（正文可视化选择、Mermaid/教学图验收的唯一真源）

章节导航看板追加 `prompts/30-Excalidraw章节知识看板.md`。

## 执行要点

- 先看真实目录再画；一图尽量只回答一个主要问题，不靠极小字号或横向滚动才能读。
- 严禁用 `text` / `plaintext` / 普通代码块或 ASCII、Unicode 字符拼教学流程图、树、框图、拓扑图、映射图。
- 修改既有 `.excalidraw` 文件时保留其既有 JSON 结构与元素 id 习惯，只做必要增删，不要手写结构不明的文件；新建看板严格按 `prompts/30` 的目录总览与一对一规则。
- Markdown 章节知识库是事实源，看板只做视觉导航，不承载知识结论。
- 图的每个点击目标只保留一个真实 Excalidraw link，并确认目标文件确实存在。

## 交付与校验

- 在 Vault 根执行 `node scripts/check-vault.mjs`，确认链接与附件路径有效。
- 提醒用户在 Obsidian 中实际打开确认渲染效果（Mermaid/Excalidraw 的最终渲染只有 Obsidian 能验证）。
- Git 交付按 `AGENTS.md`；除非用户明确要求，不自动 commit / push。
