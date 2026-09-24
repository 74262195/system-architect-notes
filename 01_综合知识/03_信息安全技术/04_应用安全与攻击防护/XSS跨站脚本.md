---
type: 考点
subject: 系统架构设计师
chapter: 信息安全技术
topic: XSS跨站脚本
difficulty: 2
source: 教材 + OWASP Cross Site Scripting Prevention Cheat Sheet
updated: 2026-08-28
review_status: 待复习
tags:
  - 系统架构师
  - 系统架构师/信息安全
  - 系统架构师/信息安全/应用安全
priority: ⭐⭐
status: 学习中
created: 2026-08-03 星期一
exam_priority: P2
review_level: 补充
priority_reason: "属于软件脆弱性与应用安全范围，2020 年案例资料出现 XSS；综合知识直接证据有限"
priority_updated: 2026-09-07
quality_reviewed: 2026-09-17
quality_status: QH-SEC-05已将抽象定位表改为评论展示场景与直接答案
---
# XSS 跨站脚本：为什么不可信内容会在用户浏览器里变成代码

> [!summary]- 快速复习卡片（学完再看）
> **作用/定位**：不可信数据进入 HTML/JS 等执行上下文，导致浏览器执行攻击者脚本。
> **核心结论**：核心防御是按输出上下文正确编码/安全 DOM API；CSP 是重要纵深手段。
> **题干怎么认**：浏览器执行脚本、评论区/URL 回显、DOM sink、窃取会话信息。
> **易错点**：HttpOnly 只能限制脚本读取 Cookie，不能消灭 XSS；简单过滤 `<script>` 也不是可靠根治。

## 评论里的文字，为什么会在别人浏览器里运行

评论区本来只应展示用户输入的文字。如果网站把攻击者提交的内容直接当成 HTML 或 JavaScript 交给浏览器解释，其他用户打开页面时，里面的恶意脚本就会运行。**XSS（跨站脚本攻击）就是不可信内容越过了“普通数据”的边界，被浏览器当成代码执行。**

防御的核心是根据内容将要进入的位置正确编码，并使用不会把文字当成 HTML 的安全接口。CSP（内容安全策略）和 HttpOnly Cookie 可以减轻风险，但不能代替根因修复。下一篇会讲另一种浏览器风险：攻击者不运行脚本，也可能借用户已经登录的身份发请求。

### 一条评论怎样从文字变成浏览器行为

假设评论内容只是要原样展示。下面字符串带有一个无害的 `console.log` 演示处理器，不读取或发送数据，也不修改页面：

```js
const comment = `<img src="invalid-demo" onerror="console.log('XSS demo')">`;
```

若页面把评论交给危险的 HTML 插入接口：

```js
commentElement.innerHTML = comment;
```

浏览器会把字符串解析成一个 `img` 元素，而不是显示尖括号文字；图片地址加载失败后，事件处理器会在控制台输出 `XSS demo`。真实攻击可能把事件处理器换成其他脚本，因此代码示例只保留无害行为。

同一段评论若用纯文本接口显示：

```js
commentElement.textContent = comment;
```

浏览器会把整段内容显示为字面文本，不创建 `img` 元素，也不会触发事件。这正是“原始输入→进入危险输出位置→浏览器解析并执行”的边界变化。

这个结论限定在**纯文本插入 HTML 元素内容**的场景。若数据进入属性、URL、JavaScript 或 CSS，上下文解析规则不同，应选对应编码并避免危险上下文；若产品确实需要富文本，应使用可靠净化器，不能把 `textContent` 当作所有输出位置的通用替代。参考 [OWASP Cross Site Scripting Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)。

## 三类经典场景

- **存储型**：恶意内容先进入服务器存储，再返回给其他用户。
- **反射型**：恶意输入随请求进入，立即被页面响应反射出来。
- **DOM 型**：DOM 是浏览器在内存中表示网页结构的对象模型；前端脚本把不可信数据写进危险 DOM/脚本上下文时，漏洞可主要发生在客户端。

## 防御抓主线

1. 按 HTML、属性、URL、JavaScript 等不同上下文做正确输出编码；
2. 优先使用不会解释为 HTML 的安全 DOM API（浏览器提供的网页结构操作接口）；
3. 必须允许富文本时使用可靠的 HTML Sanitizer（按规则清除危险标签和属性的净化器）；
4. 配置 CSP（内容安全策略，用白名单限制页面可加载或执行的内容）、HttpOnly（禁止前端脚本直接读取特定 Cookie）等做纵深防护。

## 自测

1. 为什么“统一把所有字符 HTML 转义”并不能覆盖所有 JS/URL 上下文？

> [!answer]- 第 1 题答案与解析
> **答案**：不同输出上下文有不同的解析规则和安全编码要求，HTML 编码不能自动适用于 JavaScript、URL 或属性上下文。
> **解析**：先识别数据最终进入什么上下文，再选对应的安全处理方式。

2. HttpOnly 为什么只能减轻某些后果，而不是根治 XSS？

> [!answer]- 第 2 题答案与解析
> **答案**：它可限制脚本直接读取某些 Cookie，但恶意脚本仍可能篡改页面、诱导操作或利用已有会话发请求。
> **解析**：根因仍是不可信内容进入可执行上下文。

3. 评论字符串交给 `innerHTML` 后为什么会运行事件处理器，交给 `textContent` 后为什么只显示文字？

> [!answer]- 第 3 题答案与解析
> **答案**：`innerHTML` 将字符串交给 HTML 解析器，浏览器据此创建元素并处理事件属性；`textContent` 把它作为文本节点内容，不解析成 HTML。
> **解析**：漏洞由数据进入了会解释为标记/代码的输出位置引起。

4. `textContent` 能否安全处理所有属性、URL 和脚本上下文？

> [!answer]- 第 4 题答案与解析
> **答案**：不能。
> **解析**：它适用于把纯文本放入元素内容；属性、URL、JavaScript、CSS 各有不同解析规则，应使用对应编码并避开危险上下文。

## 下一站
- 上一篇：[[SQL注入]]
- 下一篇：[[CSRF跨站请求伪造]]
