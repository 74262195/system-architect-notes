---
type: textbook-ai-guide
subject: 系统架构设计师
status: maintained
source: repository
tags: [软考, 系统架构设计师, 教材, AI教材库]
---

# AI 教材库说明

这个目录是教材的 **AI 可读层**，不是 PDF 原件目录。

原始 6 份 PDF 暂时继续保留在 `官方教材/` 根目录，并由 Git LFS 管理；AI教材库保存脚本抽取出的 Markdown、教材索引和抽取报告。只有在 OCR、图片、表格、公式和页码证据都已形成可独立核验的替代层后，才考虑删除 PDF 原件。

## 为什么要做这一层

GitHub 连接器直接读取 Git LFS 文件时只能看到 LFS pointer，无法读取几百 MB PDF 正文。

因此采用：

1. Git LFS 保存 PDF 原件；
2. GitHub Actions 拉取教材 LFS；
3. scripts/extract-textbook-text.py 优先抽取 PDF 文字层；文字层不足时可对扫描页做简体中文+英文 OCR；
4. 按 12 个 PDF 页切成一个 Markdown 块；
5. 普通 Git 保存这些 Markdown；
6. ChatGPT / Codex 后续直接读取 Markdown，并通过 source_file + PDF 页码回溯原件。

这样既不需要把整本 PDF 每次塞给 AI，也不会因为单个 Markdown 太大而难以检索。

## 目录职责

- README.md：人工维护，说明规则。
- 教材索引.md：脚本生成，记录 6 份资料角色、优先级和 AI 文本位置。
- 抽取报告.md：脚本生成，记录是否可解析、是否需要 OCR、页数和分块数。
- 原始文本/：脚本生成，每本 PDF 一个子目录，每 12 页一个 Markdown 块。

原始文本目录是自动生成层，不建议手工修改。

## 6 份资料的使用优先级

### 1. 考试范围

系统架构第二版 大纲.pdf

作用：判断考试范围、能力要求和知识边界。

### 2. 主教材

系统架构设计师教程第二版可搜索.pdf

作用：概念、机制、公式、章节内容和知识覆盖的主干依据。

### 3. 教材交叉核验

【带搜索】系统架构设计师第二版.pdf

作用：主教材文字层、页码或内容疑点的交叉核验。

### 4. 应试辅导

- 2_系统架构师32小时.pdf
- 彩色 考试32小时通关-第2版（2023）.pdf

作用：重点归纳、应试表达、例题和记忆辅助。

### 5. 扩展参考

软件体系结构原理、方法与实践_第2版.pdf

作用：软件体系结构相关知识的深入理解。

> [!warning] 这里的“资料角色”是仓库内部的 AI 使用策略，不等同于对出版社、作者或官方身份的认证。仅凭文件名不能自动证明资料来源身份。

## 冲突处理原则

遇到不同资料说法不一致时：

1. “考不考、要求到什么层级”优先核验大纲。
2. “是什么、为什么、怎么工作”优先核验主教材。
3. 主教材抽取异常时，用另一份可搜索教材交叉核验。
4. 辅导资料用于帮助理解和应试，不静默覆盖大纲和主教材。
5. 扩展参考用于补充理论深度，不把超出考试要求的内容包装成必考点。
6. 如果仍然冲突，保留差异并标记待核验，不自行拼成所谓“官方口径”。

## PDF 页码是稳定引用锚点

每个自动生成 Markdown 都带有：

- source_file
- pdf_page_start
- pdf_page_end
- source_kind
- source_priority
- extract_status

后续做笔记校验时，优先记录“原始 PDF + PDF 页码”，不要把自动生成 Markdown 的行号当成教材页码。

例如 AI 需要说明某个概念来自教材第 120—123 页，应保存对应 source_file 和 PDF 页码范围，而不是只写某个 Markdown 文件的行号。

## 图片、表格和公式限制

pdftotext 只能稳定抽取文字层。

以下内容可能丢失或错位：

- 架构图；
- 流程图；
- 表格布局；
- 数学公式排版；
- 扫描页；
- 图片里的文字。

因此出现以下情况时必须回看原 PDF：

- 文字明显断裂；
- 公式无法理解；
- 原文提到“如下图”但 Markdown 没有图；
- 表格列发生错位；
- 页面几乎没有文字。

脚本会把疑似扫描版标记为 需OCR，把大量弱文字页面的文件标记为 部分可解析。

## 本地运行

macOS 首次建议安装 Poppler 和 Tesseract：

brew install poppler tesseract tesseract-lang

拉取教材 LFS：

git lfs pull --include="官方教材/*.pdf"

执行：

python3 scripts/extract-textbook-text.py

需要同时处理扫描版 PDF 时使用：

python3 scripts/extract-textbook-text.py --ocr-fallback --ocr-workers 2 --ocr-dpi 180

默认每 12 页生成一个 Markdown；需要调整时可以使用：

python3 scripts/extract-textbook-text.py --chunk-pages 20

## 自动运行

工作流文件：

.github/workflows/extract-textbook-text.yml

它会在以下情况运行：

- 教材 PDF 新增或更新；
- 教材抽取脚本更新；
- 工作流自身更新；
- 手动触发。

工作流只拉取教材目录的 LFS PDF，不主动下载历年真题 LFS，避免两套任务互相影响。工作流默认启用 OCR 回退，并安装简体中文与英文 Tesseract 语言包；已有可靠文字层的教材不会重复 OCR。

## 与真题解析的关系

教材库和真题库是两个独立证据层：

- 教材库回答：应该学什么、概念如何解释、知识体系是否完整。
- 真题库回答：实际怎么考、哪些知识高频、题干怎样设陷阱。

后续检查一篇笔记时，推荐同时结合：

1. 大纲范围；
2. 主教材；
3. 去重后的历年真题；
4. 当前笔记。

这样可以区分“教材要求但暂未高频出现”和“真题高频但笔记解释不完整”。

需要使用教材补全或校验笔记时，显式读取 prompts/65-教材证据与笔记校验.md。
