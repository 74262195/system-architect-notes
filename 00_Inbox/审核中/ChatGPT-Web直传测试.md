---
title: ChatGPT Web 直传测试
tags:
  - workflow-test
  - chatgpt
status: draft
source: ChatGPT Web
created: 2026-08-28
---

# ChatGPT Web 直传 GitHub 测试

这是一次实际链路测试。

## 测试目的

验证普通网页版 ChatGPT 是否能够通过已连接的 GitHub，直接将 Markdown 文件写入私有仓库，而无需手动下载文件到 Mac。

## 目标链路

```text
网页版 ChatGPT
→ GitHub 私有仓库
→ 00_Inbox/AI草稿/
→ 本地 git pull
→ Codex App 自动整理
→ Obsidian
```

## 预期结果

如果你在 GitHub 中看到本文件，说明“网页版 ChatGPT → GitHub”这一步已经打通。

接下来只需要解决 GitHub → Mac 本地仓库的自动同步，即可实现无需手工下载 Markdown 的工作流。

> [!IMPORTANT]
> 本文件仅用于验证自动化流程，可以在测试完成后删除。

测试