# Inbox 自动整理任务

当 `00_Inbox/AI草稿/` 出现新的 Markdown 时，Codex App 按以下顺序处理；没有新文件则不产生提交。

1. 只读取新草稿、`AGENTS.md`、`STYLE.md`、[[Inbox索引]]、相关 MOC、上一篇和下一篇。
2. 根据标题和内容判断唯一正式章节；先搜索同名、aliases 和相似主题，已有笔记则合并或更新，不重复创建。
3. 补齐 frontmatter；保留原始事实和公式，纠正明显错误但不要杜撰来源。
4. 按零基础原子卡结构重写；计算使用 LaTeX，流程使用 Mermaid。
5. 将成品移动到正式目录，更新 MOC、索引、前后“下一站”和必要的 Canvas/Dataview 路径。
6. 将需要人工判断的内容移到 `00_Inbox/审核中/`，不要自动合并。
7. 运行 `node scripts/check-vault.mjs`；检查通过后执行 `git diff --check`。
8. 创建提交并推送到 `main`，提交信息使用 `notes: inbox整理 <主题>`。

安全边界：不得提交认证文件、Token、私钥、未脱敏工作资料、教材扫描件；不得使用强制 push；不得删除原始草稿，除非已移动到正式目录且 Git 中可追溯。
