---
copilot-command-context-menu-enabled: true
copilot-command-slash-enabled: true
copilot-command-context-menu-order: 2030
copilot-command-model-key: ""
copilot-command-last-used: 0
---
请基于选中的软考知识点，先选择最合适的绘图工具，再生成一张适合 Obsidian 的图。

要求：
1. 用简体中文解释图中节点。
2. 工具选择：简单流程、时序、类图、ER 图用 Mermaid；多节点关系、环形依赖、资源分配、网络拓扑和复杂架构用 Graphviz DOT；自由排版的论文展示图用 Excalidraw；知识地图和章节总览用 Canvas。
3. Mermaid 节点 ID 不要使用小数点。
4. 节点文本简短，需要换行时用 <br/>。
5. 一张图只选择一种主工具；复杂关系优先 Graphviz DOT，使用 `dot` 代码块。环形布局可注明 `layout=circo`，若插件不能切换引擎则说明用 `circo` 命令导出。
6. 始终以方便阅读为第一优先：小图保持紧凑，不要无意义地铺满页面；Graphviz 小图必须设置明确的 `size="宽,高!"` 画布上限，并检查生成 SVG 的实际宽高；控制节点不超过 12 个，检查无重叠、箭头方向正确、文字可读、颜色有语义且不过度装饰。
7. 图中存在形状、颜色或箭头语义时，优先在图内加入紧凑图例；图例必须使用与正文一致的真实形状和箭头示例，不能只在正文单独解释。
8. 最后说明工具选择理由、考题关键词和论文可用场景。

待处理内容：{}
