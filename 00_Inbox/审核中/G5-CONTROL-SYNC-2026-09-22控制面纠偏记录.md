---
type: 控制面纠偏记录
subject: 系统架构设计师
batch: G5-CONTROL-SYNC
status: CLOSED
start_head: 27a09d9e9d46d4f0578308702a078d7777118fbe
corrected_stop: G5-11-CASE-2012-STYLE-MIX-CLOSED
current_priority: G5-12-CANDIDATE-AUDIT
updated: 2026-09-22
tags: [软考/架构设计师, G5, 案例分析, 控制面, 纠偏]
---

# G5-CONTROL-SYNC 控制面纠偏记录

## 本轮结论

运行时最新 `main` 的真实提交历史已经完成并收口 G5-10、G5-11；而 `全库补全总控计划.md` 与 `G5-案例能力建设总控计划.md` 的 frontmatter 仍停在 `G5-09 / G5-10-CASE-NEXT`。该停点属于**滞后控制面**，不得再作为重复执行 G5-10/G5-11 的依据。

本记录作为本轮边界清晰的控制面纠偏事实，锁定真实停点：

> `G5-10-CASE-2022-DISTRIBUTED-FAULT = CLOSED`
>
> `G5-11-CASE-2012-STYLE-MIX = CLOSED`

恢复主线时，以真实提交历史、案例索引以及两份 CLOSED 收口记录优先解释旧 frontmatter；旧 `current_priority: G5-10-CASE-NEXT` 视为历史滞后值。

## 已核验事实

- `01_综合知识/06_软件架构设计/` ARCH-UX：保持 CLOSED，不重新开启。
- 01 计算机系统基础：保持用户已学完状态，不重开 coverage/contract。
- 13 专业英语：保持 `out_of_future_plan_by_user`，不作为 blocker。
- ARCH 理论 coverage：继续保持 `124 stable = 121 covered + 3 legal link_only + 0 partial + 0 unmapped`。
- G5-10：第十类动作“状态难集中掌握 → 心跳/超时发现可疑故障 → 按对象边界分层监控 → 汇总监测数据 → 选择诊断方法”已 CLOSED。
- G5-11：第十一类动作“需求拆分 → 风格匹配 → 机制解释 → 多风格组合”已 CLOSED。
- 两批均保留来源待核验边界，没有升级为官方原卷/官方答案。

## 下一真实优先级

下一批不是直接假定“必须建设 G5-12”，而是：

> **`G5-12-CANDIDATE-AUDIT`：只审计是否仍存在证据可靠、且能新增可复用答题动作的案例缺口。**

执行门槛：

1. 优先检查仍未形成完整案例动作的 CASE-COM-01 故障检测/切换、CASE-COM-02 IPv4/IPv6 融合；
2. 若可靠文本仍不足，允许检查其他尚未形成代表动作的案例入口；
3. 若候选只会重复现有十一类动作、依赖缺图缺表才能作答、或来源无法可靠核验，则判定“不建设”；
4. 如果审计后没有真实可执行缺口，停止扩充 G5，不为数量制造 G5-12 正文。

## 本轮边界

本轮只纠正控制面解释，不修改学习正文、不改 Atom、不改 coverage、不重写案例页。由于当前 GitHub 连接器的文件更新接口要求整文件替换，而两份历史总控均为长文件，本轮不以不完整内容覆盖它们；本记录用于安全锁定真实停点，后续任何执行必须先读取本记录与最新提交历史，不能机械服从旧 frontmatter。

## 验收

- START_HEAD：`27a09d9e9d46d4f0578308702a078d7777118fbe`。
- G5-10 CLOSED 记录存在：PASS。
- G5-11 CLOSED 记录存在：PASS。
- 旧控制面滞后已显式识别：PASS。
- 重复执行 G5-10/G5-11 已禁止：PASS。
- Atom / coverage：零变化。
- 学习正文：零修改，因此无 `review_status` 变化。
- `node scripts/check-vault.mjs`：当前连接器环境未执行。
- `git diff --check`：当前连接器环境未执行。

## 下一轮与下下轮

下一轮：`G5-12-CANDIDATE-AUDIT`，只做候选证据审计；有真实新增动作才进入正文建设。

下下轮：若候选审计 PASS，建设一个边界清晰的 G5-12 案例；若候选审计无真实缺口，则报告 G5 当前已收口并恢复全库总控中下一条真实未完成主线，不制造案例。
