# 软考系统架构师笔记

本仓库是一个可被 Obsidian 直接打开的 Vault，GitHub `main` 是唯一真源。

## 两种工作方式

### 手动模式

在网页版 ChatGPT 中读取 `prompts/` 和相关笔记，生成完整 Markdown，保存到 `00_Inbox/AI草稿/`，人工检查后提交：

```bash
git pull --rebase
node scripts/check-vault.mjs
git add .
git commit -m "notes: <主题>"
git push
```

### 自动模式

使用网页版 Codex 从最新 `main` 创建 AI 分支，读取 `AGENTS.md`、任务提示词、索引和相邻笔记，生成后提交 PR。GitHub Actions 负责格式、链接和敏感文件检查，人工审核后合并。

## Obsidian 同步原则

本地 Obsidian 使用 `main`；Codex 只写 AI 分支。合并 PR 后再执行 `git pull --ff-only`。Canvas、Excalidraw 和二进制附件避免并行修改。

## 目录

- `01_综合知识/`：综合知识原子卡和索引
- `02_案例分析/`：案例分析卡
- `03_论文素材/`：论文素材
- `04_真题错题/`：错题卡
- `05_画图素材/`：Canvas、Excalidraw、Mermaid
- `06_模板/`：笔记模板
- `prompts/`：版本化提示词
- `scripts/`：本地和 CI 校验
