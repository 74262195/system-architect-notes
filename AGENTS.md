# 软考系统架构师笔记仓库规范

本仓库根目录同时是 Obsidian Vault。默认使用简体中文，面向软考系统架构设计师零基础学习者。

## 笔记质量

- 原子卡按“痛点 → 定义 → 逐个认识 → 核心机制 → 考试关系 → 口诀 → 下一站”组织。
- 计算、推导、公式统一使用 LaTeX；流程和结构优先 Mermaid。
- 保留并补齐 frontmatter：`type`、`subject`、`chapter`、`topic`、`status`、`difficulty`、`source`、`tags`。
- 使用 Obsidian wikilink；新建或移动笔记必须检查链接、附件和前后“下一站”。
- 不杜撰真题出处、分值、项目数据或教材原文；缺失信息标记“待补充”。

## Inbox 自动整理与 Git 交付

- `00_Inbox/AI草稿/` 是网页 ChatGPT 的唯一落点。Codex App 读取 [[prompts/00-Inbox自动整理]] 后整理到正式目录。
- `main` 保持可用；自动整理前必须先检查是否有未提交改动。若本地已有未提交改动，暂停并报告，不覆盖用户编辑。
- 同一台 Mac 上 Obsidian 与 Codex App 使用同一目录，Codex 写入后 Obsidian 会立即看到；GitHub 只负责备份、历史和多设备同步。
- 自动整理完成后运行校验、`git diff --check`，再提交并推送；不使用强制 push。
- 若使用网页 Codex 的分支/PR 模式，AI 修改必须创建 `ai/<topic>-YYYYMMDD` 分支并提交 PR。
- 一个 PR 只处理一个知识点或一个明确章节。
- 修改前读取对应 MOC、模板、上一篇和下一篇；修改后运行 `node scripts/check-vault.mjs`。
- 不提交认证、Token、私钥、插件数据、工作资料或整本教材扫描件。

## 提示词

具体任务读取 `prompts/` 下对应文件；手动模式输出完整 Markdown 和建议保存路径，PR 模式负责落盘并更新索引。
