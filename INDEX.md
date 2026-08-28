# 软考系统架构师知识库

这是仓库根目录的 Obsidian Vault，也是 GitHub `main` 的本地工作副本。

## 工作流入口

- 网页 ChatGPT 下载的草稿：[[Inbox索引]]
- 综合知识：[[综合知识索引]]
- 案例分析：[[案例分析索引]]
- 论文素材：[[论文素材索引]]
- 真题错题：[[真题错题索引]]
- 统一规范：[[AGENTS]]、[[STYLE]]、[[prompts/README]]

## 本地自动化

Codex App 负责处理 `00_Inbox/AI草稿/` 中的新 Markdown：识别章节、去重、补 frontmatter、更新 MOC 和前后链接，运行 `node scripts/check-vault.mjs`，再提交并推送。

同一台 Mac 上 Obsidian 与 Codex App 使用同一目录，因此文件修改会立即反映在 Obsidian；GitHub 用于备份、版本历史和多设备同步。

## 人工兜底

```bash
git pull --rebase
node scripts/check-vault.mjs
git add .
git commit -m "notes: <主题>"
git push
```
