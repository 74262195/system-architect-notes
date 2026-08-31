# Excalidraw 章节知识看板

用于创建或维护系统架构设计师知识库的 Excalidraw 可视化导航。

## 核心原则

1. **先看真实目录，再画看板。**
2. Markdown 章节知识库是事实源，Excalidraw 只做视觉导航。
3. 若章节目录下有多个直接子目录，先建立目录总览，再按子目录一对一建立详细看板。
4. 不把整章所有原子知识点塞进一张超宽画布。
5. 每个点击目标只保留一个真实 Excalidraw link。

## 执行前必须读取

- `AGENTS.md`
- 对应章节知识库 Markdown
- 当前章节根目录和直接子目录
- 每个子目录中的实际文件列表
- 已存在的相关 Excalidraw 看板

## 目录映射

总览层必须镜像**真实直接子目录**。详细看板内部才按知识块分组。

## 紧凑卡片

- 总览建议 2~3 列。
- 默认单卡宽度约 380~460；无必要不要使用 700~1000 宽卡。
- 一个知识块通常放 2~7 个知识点。
- 内容多时向下增加行，不无限拉宽画布。
- 留白用于分组，不制造大片无效空白。

## 链接实现：强制要求

- 每个知识点/目录入口必须有独立标题 text 元素。
- **标题 text 元素的 `link`** 使用 `[[真实笔记或看板路径]]`。
- 背景 shape 的 `link` 必须为空。
- 同一目标只设置一个 link。
- 不额外显示“↗”假装可点击。
- 生成后解析 JSON，确认 `element.link` 非空。
- 看板保存 `appState.viewModeEnabled: true`。
- 移动 Markdown 后同步更新完整路径 link。

## 连线与预览

- 默认 0 条 line/arrow；只有明确流程、依赖、因果关系才添加少量有语义的线。
- 默认不用 file preview。
- 看板是导航，不复制原子笔记正文。

## JSON 验收

至少统计 `linkedElements`、`uniqueTargets`、`textLinks`、`rectLinks`、`line/arrow`、`viewModeEnabled`。

合格标准：导航链接全部在 text；`rectLinks = 0`；目标无重复 link；默认 `line/arrow = 0`；`viewModeEnabled = true`；每个 target 对应真实文件；总览目录与真实目录一一对应。

## Git 交付

批量创建多张看板时尽量一个批量提交；完成 JSON/链接等必要校验后直接提交到 `main`。
