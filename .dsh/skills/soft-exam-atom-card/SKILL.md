---
name: soft-exam-atom-card
description: 在软考系统架构师 Vault 中新建或大幅重写原子考点卡：整章补全落地单个 Atom，或单篇独立写作、补齐正文、拆卡。
whenToUse: 用户要求新增、重写、补全某个知识点 / 考点 / 原子卡，或整章建设中要落地某个 Atom。
---

# 原子考点卡：新建与重写

## 运行时必读

先确认当前工作区就是软考笔记 Vault（根目录含 `.git`、`AGENTS.md`、`prompts/`）。按顺序读取**当前 main 上的**规则文件；本技能刻意不复述任何条款，规则以这些文件为唯一真源：

1. `AGENTS.md`（全局硬门禁 + 提示词路由）
2. `prompts/00-全局写作规范.md`
3. `prompts/10-原子考点卡生成.md`（原子性、生成流程、单篇验收、批量门禁的唯一真源）

按任务追加读取：

- 涉及教材证据、解释深度、事实核验 → `prompts/65-教材证据与笔记校验.md`
- 需要覆盖矩阵 / Atom ID / 判断是否 `link_only` → `prompts/20-章节检查与重构.md`
- 正文需要图 → `prompts/40-Mermaid与Obsidian样式修复.md`
- 章节导航看板 → `prompts/30-Excalidraw章节知识看板.md`

冲突优先级、frontmatter 字段、`review_status` / `exam_priority` 的维护要求，全部以 `AGENTS.md` 与 `prompts/10` 为准。

## 执行要点

- 先读目标章节的**真实目录结构**，把笔记写进对应章节目录，不自行抽象层级、不新造目录编号。
- 先查同义/同名笔记，再决定新建、合并还是只放 wikilink 指向既有主事实源。
- 一卡一主问题；无法确定它属于哪个 Atom 时，先走 `20` 建立或读取覆盖矩阵，不凭目录印象挑题。
- 教学例子可以虚构但必须明显是解释性例子；教材原文、真题出处、分值、官方章节编号等无证据不写。
- 改完按 `prompts/10` 的单篇验收清单自检一遍。

## 交付与校验

- 写入 Vault 内真实路径，并同步需要更新的索引与 wikilink（含前后学习主线）。
- 在 Vault 根执行 `node scripts/check-vault.mjs`，处理它报告的重名、断链、冲突标记问题。
- Git 交付按 `AGENTS.md` 的规则执行；除非用户明确要求，不要自动 commit / push，提交时只 `git add` 本次改动路径。
