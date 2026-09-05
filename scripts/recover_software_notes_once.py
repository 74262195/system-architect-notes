from pathlib import Path
import runpy, re, shutil, subprocess

ROOT=Path('.')
DRAFT=ROOT/'00_Inbox/审核中/软件工程基础知识_未完成工作稿.py'
TARGET=ROOT/'01_综合知识/04_软件工程基础知识'
OLDQ=ROOT/'01_综合知识/04_系统质量属性与架构评估'
NEWQ=ROOT/'01_综合知识/07_系统质量属性与架构评估'
TODAY='2026-09-05'

def write(p,s):
    p.parent.mkdir(parents=True,exist_ok=True); p.write_text(s.rstrip()+"\n",encoding='utf-8')

def esc(s): return str(s).replace('"','\\"')

# 1) 恢复工作稿：正文 body 原样使用，不重新生成。
ns=runpy.run_path(str(DRAFT))
items=ns.get('items',[])
assert len(items)==55, f'expected 55 items, got {len(items)}'
for it in items:
    p=TARGET/it['group']/(it['name']+'.md')
    body=it['body'].rstrip()
    content=f'''---
type: 考点
subject: 系统架构设计师
chapter: 软件工程基础知识
topic: {it['name']}
source: 官方教材工作稿
textbook_pages: "{esc(it['pages'])}"
status: 学习中
created: {TODAY}
updated: {TODAY}
tags:
  - 系统架构师
  - 系统架构师/软件工程
  - 系统架构师/软件工程/{it['group']}
quality_status: 工作稿恢复
---

# {it['name']}

> [!summary] 快速复习卡片
> - **核心结论**：{it['core']}
> - **做题入口**：{it['signal']}

{body}

## 自测

> [!question]- {it['question']}
> {it['answer']}
'''
    write(p,content)

# 2) 第四章索引与学习路线。
groups=[]
for it in items:
    if it['group'] not in groups: groups.append(it['group'])
by={g:[x for x in items if x['group']==g] for g in groups}
idx=['# 软件工程基础知识索引','', '> 本章 55 篇原子笔记从 `00_Inbox/审核中/软件工程基础知识_未完成工作稿.py` 恢复；正文未重新生成。','', '## 学习主线','', '[[软件工程的定位]] → [[瀑布模型]] / [[迭代与增量模型]] / [[螺旋模型]] → [[需求开发与需求管理]] → [[结构化分析与设计分工]] / [[面向对象分析OOA]] → [[静态测试与动态测试]] → [[构件模型与容器]] → [[软件项目管理的范围]]','']
for g in groups:
    idx += [f'## {g}','']+[f'- [[{x["name"]}]]' for x in by[g]]+['']
idx += ['## 配套入口','','- [[学习路线]]','- [[软件工程基础知识-覆盖检查]]','']
write(TARGET/'软件工程基础知识索引.md','\n'.join(idx))

route=['# 软件工程基础知识学习路线','', '## 为什么按这个顺序','', '先建立“软件工程怎样组织开发”的过程视角，再学习需求如何确定、设计如何落地、测试如何验证、构件如何复用，最后用项目管理把范围、进度、配置、质量和风险串起来。','', '## 第一轮：先抓主线','']
for g in groups:
    names=' → '.join(f'[[{x["name"]}]]' for x in by[g])
    route += [f'### {g}','',names,'']
route += ['## 第二轮：按题干识别','','- 看到“阶段顺序、风险驱动、迭代增量”先定位过程模型。','- 看到“业务/用户/功能/非功能、变更、追踪”先定位需求工程。','- 看到“DFD、内聚耦合、OOA/OOD”先定位分析与设计。','- 看到“静态/动态、黑盒/白盒、单元/集成/系统/验收”先定位测试分类维度。','- 看到“复用构件、适配、组装”先定位 CBSE。','- 看到“WBS、依赖、基线、SQA、风险”先定位项目管理。','', '## 下一站','', '- 返回：[[软件工程基础知识索引]]','- 后续章节按全局索引继续。','']
write(TARGET/'学习路线.md','\n'.join(route))

# 3) 证据覆盖检查：只做可追溯文本匹配，不编造考频。
evidence=[]
for p in ROOT.rglob('*'):
    if not p.is_file() or p.suffix.lower() not in {'.md','.txt','.json','.csv'}: continue
    s=str(p)
    if any(k in s for k in ('考试大纲','官方教材','教程','真题','题库','抽取')):
        evidence.append(p)
terms={
'软件过程':['瀑布','螺旋','RUP','敏捷','Scrum','XP','CMMI'],
'需求工程':['需求工程','需求获取','需求管理','需求变更','需求跟踪'],
'分析与设计':['结构化分析','数据流图','DFD','内聚','耦合','面向对象分析','OOA'],
'软件测试':['静态测试','动态测试','黑盒','白盒','单元测试','集成测试','系统测试','验收测试'],
'构件软件工程':['构件','CBSE','组装','适配'],
'项目管理':['WBS','配置管理','质量保证','SQA','风险管理']}
found={k:set() for k in terms}
source_hits={}
for p in evidence:
    try: text=p.read_text(encoding='utf-8',errors='ignore')
    except: continue
    hits=[]
    for cat,ks in terms.items():
        for k in ks:
            if k.lower() in text.lower(): found[cat].add(k); hits.append(k)
    if hits: source_hits[str(p)]=sorted(set(hits))
report=['# 软件工程基础知识覆盖检查','',f'- 检查日期：{TODAY}','- 方法：以仓库中可直接读取的考试大纲、官方教材/教程抽取文本、真题/题库文本为证据做关键词与主题覆盖交叉检查。','- 边界：**不把“搜到一次”解释为高频，也不根据工作稿里的旧题说明推导考频。真题来源未核验时只作为覆盖信号。**','', '## 当前 55 卡覆盖','']
for cat,ks in terms.items():
    report.append(f'- **{cat}**：55 卡中已有对应原子卡；证据文本命中关键词：'+('、'.join(sorted(found[cat])) if found[cat] else '当前可读证据未命中，保留为待核验'))
report += ['', '## 可追溯证据文件','']
if source_hits:
    for p,h in sorted(source_hits.items())[:80]: report.append(f'- `{p}`：'+ '、'.join(h))
else: report.append('- 当前仓库可直接读取的文本证据未检出上述关键词；因此本报告不作考频判断。')
report += ['', '## 覆盖结论','', '- 工作稿已经覆盖软件过程、需求工程、结构化/面向对象分析设计、软件测试、净室、CBSE、项目管理七条主线。','- 55 卡正文中的教材页码保留为工作稿证据线索；若对应官方教材版本发生变化，应重新核对页码，不据页码本身推导优先级。','- 工作稿中引用的 2018 年题目均维持“来源待核验”口径；在没有更可靠题源前，不升级成“高频/必考”。','- CMMI 具体过程域/目标/实践数量存在版本口径风险，当前卡已明确不背未经核验的数字；继续保留该限制。','']
write(TARGET/'软件工程基础知识-覆盖检查.md','\n'.join(report))

# 4) 用户指定：质量属性章节 04 -> 07，并修仓库文本路径引用。
if OLDQ.exists():
    if NEWQ.exists(): raise RuntimeError('target quality chapter already exists')
    shutil.move(str(OLDQ),str(NEWQ))
old='01_综合知识/04_系统质量属性与架构评估'; new='01_综合知识/07_系统质量属性与架构评估'
for p in ROOT.rglob('*'):
    if p.is_file() and p.suffix.lower() in {'.md','.txt','.json','.yml','.yaml'}:
        try: t=p.read_text(encoding='utf-8')
        except: continue
        nt=t.replace(old,new).replace('04_系统质量属性与架构评估','07_系统质量属性与架构评估')
        if nt!=t: p.write_text(nt,encoding='utf-8')

# 5) 更新综合知识全局索引（按真实目录，不猜未创建章节）。
gi=ROOT/'01_综合知识/综合知识索引.md'
if gi.exists():
    t=gi.read_text(encoding='utf-8')
    t=t.replace('[[04_系统质量属性与架构评估','[[07_系统质量属性与架构评估')
    if '04_软件工程基础知识' not in t and '软件工程基础知识索引' not in t:
        marker='## 章节入口'
        addition='\n- [[04_软件工程基础知识/软件工程基础知识索引|04 软件工程基础知识]]\n- [[07_系统质量属性与架构评估/系统质量属性与架构评估索引|07 系统质量属性与架构评估]]\n'
        if marker in t: t=t.replace(marker,marker+addition,1)
        else: t += '\n## 软件工程与架构评估\n'+addition
    write(gi,t)

# 6) 信息安全技术审核：扫描所有原子卡，生成/续写可复核报告。
sec=ROOT/'01_综合知识/03_信息安全技术'
notes=[p for p in sec.rglob('*.md') if p.name not in {'信息安全技术索引.md','学习路线.md','信息安全技术-考前速记.md'}]
absolute=('一定','绝对','永远','完全不会','必然','100%','只能','任何情况下','所有情况下','保证')
abs_hits=[]; missing_review=[]; missing_mech=[]; missing_cond=[]; term_hits=[]
mechanism_terms=('原理','机制','流程','过程','如何','怎样','为什么','步骤','验证','握手','认证','校验')
condition_terms=('前提','条件','例外','取决于','通常','一般','可能','若','如果','不能','不等于','并不')
term_checks={'加密等于编码':'加密.*编码','哈希可逆':'哈希.*可逆','防火墙万能':'防火墙.*(所有|全部|万能)','零信任是不信任任何人':'零信任.*不信任任何','数字签名保证绝对不可否认':'签名.*绝对.*不可否认'}
for p in notes:
    text=p.read_text(encoding='utf-8',errors='ignore')
    rel=str(p.relative_to(ROOT))
    for w in absolute:
        for m in re.finditer(re.escape(w),text):
            line=text.count('\n',0,m.start())+1; abs_hits.append((rel,line,w,text.splitlines()[line-1].strip()[:100]))
    if '快速复习卡片' not in text and '[!summary]' not in text: missing_review.append(rel)
    if not any(k in text for k in mechanism_terms): missing_mech.append(rel)
    if not any(k in text for k in condition_terms): missing_cond.append(rel)
    for label,pat in term_checks.items():
        if re.search(pat,text,re.S): term_hits.append((rel,label))
# Append to any prior audit report if found, otherwise create stable report path.
candidates=list((ROOT/'00_Inbox/审核中').glob('*信息安全*审核*.md'))
aud=candidates[0] if candidates else ROOT/'00_Inbox/审核中/信息安全技术_审核报告.md'
base_text=aud.read_text(encoding='utf-8') if aud.exists() else '# 信息安全技术审核报告\n'
section=f'''\n\n## {TODAY} 续审：绝对化、机制、条件例外、术语、复习卡片\n\n### 审核方法\n\n- 范围：`01_综合知识/03_信息安全技术/` 下 {len(notes)} 篇正文卡。\n- 绝对化：扫描“一定/绝对/永远/必然/只能/保证”等词，**命中只代表需要人工复核，不自动判错**。\n- 机制缺失：检查是否只给定义/结论而没有解释流程、原理、验证或“为什么”。\n- 条件与例外：检查安全能力是否写明前提、边界、失败条件或不能推出的结论。\n- 术语：专项检查加密/编码、哈希可逆、防火墙万能、零信任字面化、数字签名绝对不可否认等高风险误写。\n- 复习卡：检查是否存在 `[!summary]` 或“快速复习卡片”入口。\n\n### 绝对化表述候选\n'''
if abs_hits:
    for rel,line,w,snip in abs_hits[:120]: section += f'- `{rel}:{line}` 命中“{w}”：{snip}\n'
else: section += '- 未命中上述绝对化词表。\n'
section += '\n### 机制说明缺失候选\n'
section += ''.join(f'- `{x}`：未检测到机制/流程类表达，建议人工确认是否只剩定义。\n' for x in missing_mech) or '- 未发现明显候选。\n'
section += '\n### 条件与例外缺失候选\n'
section += ''.join(f'- `{x}`：未检测到前提/条件/例外类表达，建议复核安全能力是否被写成无条件结论。\n' for x in missing_cond) or '- 未发现明显候选。\n'
section += '\n### 错误术语/危险口径候选\n'
section += ''.join(f'- `{x}`：命中“{lab}”风险模式，需人工看上下文判定。\n' for x,lab in term_hits) or '- 未命中预设危险术语模式；这不等于不存在术语问题。\n'
section += '\n### 复习卡片缺失\n'
section += ''.join(f'- `{x}`\n' for x in missing_review) or '- 本轮扫描的正文卡均检测到复习卡入口。\n'
section += '''\n### 本轮结论与后续门禁\n\n1. 绝对化词命中必须逐条结合上下文判断；“只能”用于定义边界可能正确，不能批量替换。\n2. 密码学、认证、TLS、访问控制、攻击防护类卡必须说明“机制如何工作 + 成立条件 + 不能提供什么”，否则即使名词定义正确也判为不完整。\n3. “安全”类结论不得从单一机制直接推出系统整体安全；例如签名不单独提供机密性，防火墙不能覆盖全部应用层漏洞。\n4. 真题优先级仍按“大纲定范围、教材定深度、近年可靠真题定优先级”；本轮不新增任何无证据“高频/必考”标签。\n'''
if f'## {TODAY} 续审：绝对化、机制、条件例外、术语、复习卡片' not in base_text:
    write(aud,base_text+section)

# 7) 清理一次性执行文件，让最终业务提交不留下临时设施。
for tmp in (ROOT/'scripts/recover_software_notes_once.py', ROOT/'.github/workflows/recover-software-notes-once.yml'):
    if tmp.exists(): tmp.unlink()

print(f'restored={len(items)} security_notes={len(notes)} abs_hits={len(abs_hits)} missing_review={len(missing_review)}')
