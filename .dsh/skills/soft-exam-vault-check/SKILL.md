---
name: soft-exam-vault-check
description: 软考系统架构师 Vault 的提交前自检：运行 check-vault 校验、核对 git 改动范围、检查 frontmatter 与复习标记是否按规则维护。
whenToUse: 用户要求校验仓库、提交、推送、开 PR，或一次批量改笔记之后需要交付前检查。
---

# 仓库校验与提交前自检

## 运行时必读

1. `AGENTS.md`（Git 交付规则、frontmatter 与复习标记硬门禁）
2. 本次改动涉及的 `prompts/*.md`（按 `AGENTS.md` §五 路由）
3. `.github/workflows/validate-notes.yml`（CI 实际执行什么）

工作目录必须是 Vault 根（脚本用 `process.cwd()` 定位仓库）。

## 执行步骤

1. `node scripts/check-vault.mjs` —— 与 CI `validate-notes` 使用的同一脚本；修复它报告的错误，人工判断它报告的警告。
2. `git status --porcelain` 与 `git diff` —— 确认改动范围正确，没有夹带无关文件、没有把教材/真题原始大文件或凭据误加入。
3. 逐项核对本次新建/修改的笔记：
   - frontmatter 必填字段是否齐全（字段清单以 `AGENTS.md` 与对应提示词为准）；
   - 知识正文改动是否按“改动即待复习”维护 `review_status`；
   - 索引、wikilink、附件与前后学习主线是否同步；
   - 可视化是否违反禁止字符拼图的硬门禁。
4. 输出一份简短自检报告：校验结果、改动文件清单、发现的问题、仍需用户确认的事项。

## 边界

- 不要为了让校验通过而删除既有笔记、占位卡或降低规则要求；有疑问先报告。
- 除非用户明确要求，不执行 `git commit` / `git push`；用户要求提交时只 `git add` 本次相关路径，绝不使用 `git add -A` 把无关改动一起提交。
