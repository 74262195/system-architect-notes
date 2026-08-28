---
type: 索引
subject: 系统架构设计师
chapter: 工作流
topic: Inbox 草稿
status: 使用中
tags:
  - 软考/工作流
  - 软考/索引
---

# Inbox 索引

## 用途

网页 ChatGPT 生成的完整 `.md` 文件先保存到 `00_Inbox/AI草稿/`。这里是输入区，不是正式知识库；Codex App 处理完成后应将文件移动到正式章节目录。

## Codex 处理顺序

1. 读取草稿和元数据，判断目标章节。
2. 搜索同名、别名和相邻知识点，避免重复建卡。
3. 按 [[STYLE]] 补齐结构、frontmatter、LaTeX、Mermaid 和考试关系。
4. 更新对应 MOC、上一篇和下一篇的链接。
5. 运行 `node scripts/check-vault.mjs`。
6. 将通过审核的草稿移出 Inbox，提交并推送。

## 待处理草稿

```dataview
TABLE file.mtime AS 修改时间, file.size AS 字节数
FROM "00_Inbox/AI草稿"
SORT file.mtime DESC
```

## 状态约定

- `00_Inbox/AI草稿/`：待 Codex 处理。
- `00_Inbox/审核中/`：需要人工确认，Codex 不自动归档。
- 正式章节目录：已整理并可被索引引用。

## 下一站

> 顺着自动整理流程看 [[prompts/00-Inbox自动整理]]。
> 想回总入口，回 [[INDEX]]。
