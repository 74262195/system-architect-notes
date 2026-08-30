#!/usr/bin/env python3
from __future__ import annotations

import re
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BANK = ROOT / "历年真题" / "AI题库"
STANDARD_ROOT = BANK / "标准化题库"
RAW_ROOT = BANK / "原始文本"
OUT_ROOT = BANK / "知识点索引"

YEARS = range(2009, 2019)

RECENT_SOURCES = [
    (2019, "历年真题/AI题库/原始文本/2019年下半年/2019年11月系统架构设计师真题及解析.md", "解析资料"),
    (2020, "历年真题/AI题库/原始文本/2020年下半年/2020年系统架构设计师真题及解析.md", "解析资料"),
    (2021, "历年真题/AI题库/原始文本/2021年下半年/2021.11系统架构设计师真题及解析.md", "解析资料"),
    (2022, "历年真题/AI题库/原始文本/2022年下半年/2022年系统架构师考试科目一：综合知识真题及解析.md", "综合知识解析资料"),
    (2023, "历年真题/AI题库/原始文本/2023年下半年（回忆版）/2023年下半年系统架构设计师wen老师整理.md", "回忆/考点总结"),
    (2024, "历年真题/AI题库/原始文本/2024年上半年/24年5月系统架构设计师真题(回忆）+答案.md", "回忆版"),
    (2025, "历年真题/AI题库/原始文本/2025年上半年（回忆版）/202505系统架构设计师真题回忆.md", "低质量回忆抽取"),
]

@dataclass(frozen=True)
class Rule:
    topic: str
    domain: str
    terms: tuple[str, ...]
    note: str = ""
    coverage: str = "待建"

RULES = [
    Rule("计算机系统组成","计算机组成与体系结构",("冯诺依曼","计算机系统","硬件层"),"[[计算机系统组成]]","已有笔记"),
    Rule("数据表示与编码","计算机组成与体系结构",("补码","原码","反码","浮点","定点","进制","字符编码","数值表示"),"[[数据表示与编码-原反补移码]]","已有笔记"),
    Rule("CPU组成与寄存器","计算机组成与体系结构",("运算器","控制器","寄存器","程序计数器","指令寄存器","状态寄存器"),"[[CPU内部组成-运算器与控制器]]","已有笔记"),
    Rule("CISC与RISC","计算机组成与体系结构",("cisc","risc","精简指令","复杂指令"),"[[CPU指令集 CISC与RISC]]","已有笔记"),
    Rule("指令寻址","计算机组成与体系结构",("寻址方式","立即寻址","直接寻址","间接寻址","变址寻址","相对寻址"),"[[指令寻址方式]]","已有笔记"),
    Rule("指令流水线","计算机组成与体系结构",("流水线","吞吐率","加速比","流水周期"),"[[指令流水线]]","已有笔记"),
    Rule("并行体系与Flynn","计算机组成与体系结构",("flynn","simd","mimd","并行计算","多处理机"),"[[Flynn分类法]]","已有笔记"),
    Rule("存储层次与主存","计算机组成与体系结构",("存储体系","主存","dram","sram","存储器层次","分级存储"),"[[存储层次与主存]]","已有笔记"),
    Rule("Cache","计算机组成与体系结构",("cache","高速缓存","命中率","组相联","全相联","直接映射","写回","写直达"),"[[Cache]]","已有笔记"),
    Rule("外存与RAID","计算机组成与体系结构",("raid","磁盘阵列","存储冗余","校验盘"),"[[外存与RAID]]","已有笔记"),
    Rule("总线与I/O","计算机组成与体系结构",("总线","串行总线","并行总线","io接口","i/o接口","dma","程序查询","通道"),"[[总线]]","已有笔记"),
    Rule("中断技术","计算机组成与体系结构",("中断","断点","中断向量","中断响应"),"[[中断技术]]","已有笔记"),
    Rule("校验码","计算机组成与体系结构",("海明码","hamming","crc","循环冗余","奇偶校验","校验码"),"[[校验码]]","已有笔记"),
    Rule("性能与Amdahl","计算机组成与体系结构",("amdahl","阿姆达尔","mips","性能指标","基准测试","主频","倍频","外频"),"[[计算机性能指标与Amdahl定律]]","已有笔记"),

    Rule("进程与线程","操作系统",("进程","线程","pcb","进程状态","三态模型","多线程","共享内存"),"[[进程与线程]]","已有笔记"),
    Rule("进程调度","操作系统",("进程调度","作业调度","先来先服务","短作业","时间片","fcfs","sjf","优先级调度"),"[[进程调度]]","已有笔记"),
    Rule("信号量与PV操作","操作系统",("信号量","pv操作","p操作","v操作","互斥","同步"),"[[信号量与PV操作]]","已有笔记"),
    Rule("死锁与银行家算法","操作系统",("死锁","银行家","安全序列","资源分配图"),"[[死锁与银行家算法]]","已有笔记"),
    Rule("存储管理","操作系统",("分页","分段","页表","段表","逻辑地址","物理地址","页号","页框"),"[[存储管理]]","已有笔记"),
    Rule("虚拟存储与页面置换","操作系统",("虚拟存储","页面置换","缺页","lru","fifo","clock","belady"),"[[虚拟存储与页面置换]]","已有笔记"),
    Rule("文件管理","操作系统",("文件系统","索引节点","inode","一级间接","二级间接","索引块","位示图","文件分配"),"[[文件管理]]","已有笔记"),
    Rule("设备管理与磁盘调度","操作系统",("磁盘调度","移臂","sstf","scan","spooling","设备管理"),"[[设备管理与磁盘调度]]","已有笔记"),
    Rule("嵌入式系统","操作系统",("嵌入式","实时操作系统","rtos","低功耗","实时系统"),"[[嵌入式系统]]","已有笔记"),

    Rule("数据通信与交换","计算机网络",("香农","信道","调制","编码","波特率","电路交换","分组交换","报文交换","时分复用","频分复用"),"[[数据通信与交换技术]]","已有笔记"),
    Rule("网络类型与广域网","计算机网络",("局域网","广域网","wan","lan","帧中继","atm","sonet","ddn","网络拓扑"),"[[网络类型与广域网技术]]","已有笔记"),
    Rule("以太网与WLAN","计算机网络",("以太网","csma/cd","csma/ca","802.11","无线局域网","wlan"),"[[以太网技术]]","已有笔记"),
    Rule("OSI与TCP/IP分层","计算机网络",("osi","tcp/ip","七层","协议栈","网络层","传输层","会话层","表示层"),"[[网络协议与OSI七层]]","已有笔记"),
    Rule("交换机/VLAN/STP","计算机网络",("交换机","vlan","stp","生成树","mac地址","广播域","冲突域","链路聚合"),"[[交换机]]","已有笔记"),
    Rule("IP编址与IPv4/IPv6","计算机网络",("子网","cidr","vlsm","ipv4","ipv6","ip地址","子网掩码","广播地址","分片","mtu"),"[[IP编址与子网划分]]","已有笔记"),
    Rule("路由与路由协议","计算机网络",("路由协议","路由选择","rip","ospf","bgp","路由表","最长前缀"),"[[路由协议与路由选择]]","已有笔记"),
    Rule("TCP与UDP","计算机网络",("tcp","udp","三次握手","四次挥手","拥塞控制","流量控制"),"[[TCP与UDP协议]]","已有笔记"),
    Rule("应用层协议","计算机网络",("dns","dhcp","http","https","ftp","smtp","pop3","imap","snmp","ptr记录"),"[[应用层常用协议]]","已有笔记"),
    Rule("网络工程","计算机网络",("网络工程","物理网络设计","逻辑网络设计","核心层","汇聚层","接入层","网络规划"),"[[网络拓扑、组网与网络工程]]","已有笔记"),

    Rule("软件分类/中间件/构件基础","计算机软件与语言",("中间件","系统软件","应用软件","构件是","构件接口","component"),"[[计算机软件基础-分类、中间件与构件]]","已有笔记"),
    Rule("编译与解释","计算机软件与语言",("编译器","编译程序","解释程序","词法分析","语法分析","目标代码"),"[[计算机语言-编译与解释]]","已有笔记"),
    Rule("多媒体技术","多媒体",("多媒体","采样频率","量化","jpeg","mpeg","音频","图像压缩","视频压缩"),"[[多媒体基础与压缩技术]]","已有笔记"),
    Rule("企业信息化/EAI/ERP","信息系统基础",("企业信息化","eai","企业应用集成","erp","crm","scm","mrp"),"[[企业应用集成EAI]]","已有笔记"),
    Rule("商业智能/数据仓库","信息系统基础",("商业智能","bi","数据仓库","数据挖掘","olap","知识发现"),"[[商业智能BI]]","已有笔记"),
    Rule("电子商务/EDI","信息系统基础",("电子商务","edi","b2b","b2c","c2c"),"[[电子商务]]","已有笔记"),
    Rule("信息系统开发方法","信息系统基础",("信息系统开发","结构化方法","原型法","面向对象方法","面向服务方法"),"[[结构化方法]]","已有笔记"),
    Rule("系统工程方法","系统工程",("霍尔","切克兰德","系统工程","综合集成法","并行工程"),"[[系统工程与信息系统基础索引]]","已有章节"),

    Rule("对称/非对称加密","信息安全",("rsa","des","aes","非对称加密","对称加密","公钥加密","私钥加密"),"[[非对称加密]]","已有笔记"),
    Rule("哈希/数字签名/PKI","信息安全",("数字签名","消息摘要","hash","哈希","数字证书","pki","ca证书"),"[[数字签名]]","已有笔记"),
    Rule("身份认证","信息安全",("kerberos","身份认证","单点登录","sso","口令认证"),"[[身份认证]]","已有笔记"),
    Rule("访问控制","信息安全",("rbac","dac","mac强制","访问控制","权限控制"),"[[RBAC基于角色访问控制]]","已有笔记"),
    Rule("网络与通信安全","信息安全",("防火墙","ids","ips","vpn","ipsec","tls","ssl"),"[[防火墙]]","已有笔记"),
    Rule("攻击与应用安全","信息安全",("sql注入","xss","csrf","ddos","中间人攻击","重放攻击","木马","病毒"),"[[常见网络攻击]]","已有笔记"),
    Rule("安全治理/等保","信息安全",("等级保护","安全保护等级","iso27001","安全架构","纵深防御","可信计算","零信任"),"[[等级保护2.0]]","已有笔记"),

    Rule("数据库需求与设计","数据库",("数据库设计","需求分析阶段","数据字典","数据流图","e-r","er图","概念设计","逻辑设计","物理设计"),"","当前未建"),
    Rule("关系代数与SQL","数据库",("关系代数","sql","select","自然连接","投影","选择运算","group by","having","笛卡尔积"),"","当前未建"),
    Rule("函数依赖与范式","数据库",("函数依赖","候选关键字","候选码","无损连接","范式","1nf","2nf","3nf","bcnf","4nf","armstrong","多值依赖"),"","当前未建"),
    Rule("事务/并发/完整性","数据库",("事务","原子性","一致性","隔离性","持久性","触发器","参照完整性","并发控制"),"","当前未建"),
    Rule("分布式/NoSQL/数据库架构","数据库",("分布式数据库","数据库读写分离","redis","mongodb","hbase","nosql","数据分布","数据复制"),"","当前未建"),

    Rule("需求工程","软件工程",("需求管理","需求变更","需求获取","需求分析","需求规格说明","需求评审","需求跟踪"),"","当前未建"),
    Rule("软件过程与开发模型","软件工程",("瀑布模型","螺旋模型","喷泉模型","v模型","敏捷","rup","快速应用开发","原型模型","迭代增量"),"[[敏捷开发模型]]","部分已有"),
    Rule("软件设计","软件工程",("概要设计","详细设计","模块结构图","hipo","软件设计","人机界面设计","数据设计"),"","当前未建"),
    Rule("软件测试","软件工程",("软件测试","黑盒","白盒","灰盒","单元测试","集成测试","系统测试","确认测试","回归测试","边界值","逻辑覆盖","mccabe","净室"),"","当前未建"),
    Rule("配置/项目/进度管理","软件工程",("配置项","配置管理","项目管理","关键路径","进度管理","成本估算","变更控制"),"","当前未建"),
    Rule("维护/逆向/再工程","软件工程",("逆向工程","再工程","重构","设计恢复","软件维护","系统移植"),"","当前未建"),
    Rule("软件复用","软件工程",("软件复用","重用","可复用资产","机会复用","系统复用"),"","当前未建"),
    Rule("面向对象与UML/SysML","软件工程",("uml","sysml","用例图","类图","序列图","活动图","状态图","包含关系","扩展关系"),"","当前未建"),

    Rule("软件架构基础/视图","软件架构",("软件架构","体系结构文档","4+1","视角","视图","架构描述","词汇表和一组约束"),"","当前未建"),
    Rule("架构风格","软件架构",("架构风格","体系结构风格","管道-过滤器","黑板","解释器","c2体系","仓库风格","事件驱动","分层系统"),"","当前未建"),
    Rule("设计模式","软件架构",("设计模式","abstractfactory","抽象工厂","bridge","command","adapter","proxy","visitor","singleton","facade","memento"),"","当前未建"),
    Rule("质量属性","软件架构",("质量属性","可用性","可修改性","性能属性","互操作性","质量属性场景","刺激源","响应度量","效用树"),"","当前未建"),
    Rule("ATAM/SAAM架构评估","软件架构",("atam","saam","架构评估","体系结构评估","权衡分析"),"","当前未建"),
    Rule("ABSD/DSSA领域架构","软件架构",("absd","dssa","领域分析","领域设计","领域实现","特定领域软件架构"),"","当前未建"),
    Rule("SOA/REST/Web架构","软件架构",("soa","rest","restful","wsdl","uddi","web服务","微服务","三层架构","c/s","b/s"),"","当前未建"),
    Rule("可靠性","软件质量",("软件可靠性","mttf","mttr","mtbf","容错","可靠性建模","可靠性评价"),"","当前未建"),

    Rule("知识产权/标准法规","其他",("知识产权","著作权","专利","商标","许可","标准化法"),"","当前未建"),
    Rule("云计算/新技术","新技术",("云计算","iaas","paas","saas","区块链","数字孪生","边云协同","lambda架构","kappa架构","机器学习"),"","当前未建"),
]
GENERIC = Rule("其他/待人工分类","其他",tuple(),"","待人工分类")

def normalize(s):
    return re.sub(r"\s+","",s).lower()

def score_rule(text, rule):
    t = normalize(text)
    score = 0
    for term in rule.terms:
        nt = normalize(term)
        if nt and nt in t:
            score += 2 + min(t.count(nt),3)
    return score

def classify(text):
    best = (0, None)
    for i, rule in enumerate(RULES):
        score = score_rule(text, rule)
        if score > best[0]:
            best = (score, rule)
    return (best[1] or GENERIC), best[0]

def parse_standardized(path):
    text = path.read_text(encoding="utf-8")
    groups = list(re.finditer(r"^### 第 .+?题(?:（共用题干）)?\s*$",text,re.M))
    for i, gm in enumerate(groups):
        start = gm.start()
        end = groups[i+1].start() if i+1 < len(groups) else text.find("\n## 来源",start)
        if end < 0: end = len(text)
        block = text[start:end]
        qnums = [int(x) for x in re.findall(r"^#### 第 (\d{1,2}) 题$",block,re.M)]
        if not qnums: continue
        qm = re.search(r"\*\*题干与选项（原题抽取）：\*\*\s*(.*?)(?=^#### 第 )",block,re.S|re.M)
        am = re.search(r"\*\*题组解析（来源原文）：\*\*\s*(.*)$",block,re.S|re.M)
        qtext = qm.group(1).strip() if qm else ""
        analysis = am.group(1).strip() if am else ""
        rule, score = classify(qtext + "\n" + analysis)
        yield qnums, qtext, rule, score

def raw_body(text):
    if "## 抽取文本" in text:
        text = text.split("## 抽取文本",1)[1]
    lines=[]
    for line in text.splitlines():
        t=line.strip()
        if "PDF_PAGE_BREAK" in t or "软考达人" in t or "手机端题库" in t:
            continue
        lines.append(line)
    return "\n".join(lines)

def comprehensive_slice(year, body):
    if year == 2023:
        a=body.find("第一，针对综合知识部分"); b=body.find("第二，针对案例")
        if a>=0: body=body[a:b if b>a else None]
    elif year == 2024:
        a=body.find("一、综合知识"); b=body.find("案例分析部分")
        if a>=0: body=body[a:b if b>a else None]
    elif year in {2019,2020,2021}:
        candidates=[x for x in (body.find("案例分析"),body.find("下午试卷"),body.find("论文")) if x>3000]
        if candidates: body=body[:min(candidates)]
    return body

def recent_signals():
    hits=defaultdict(set)
    quality=[]
    for year, rel, kind in RECENT_SOURCES:
        path=ROOT/rel
        if not path.exists():
            quality.append((year,kind,"缺文件",0)); continue
        body=comprehensive_slice(year,raw_body(path.read_text(encoding="utf-8",errors="ignore")))
        compact=normalize(body)
        status="可用" if len(compact)>=1200 else ("弱信号" if len(compact)>=120 else "不可用")
        quality.append((year,kind,status,len(compact)))
        if status=="不可用": continue
        for rule in RULES:
            if score_rule(body,rule)>0:
                hits[rule.topic].add(year)
    return hits, quality

def priority(hist_count,recent_count,coverage):
    gap=coverage in {"当前未建","待人工分类"}
    score=hist_count+recent_count*4+(6 if gap and (hist_count>=3 or recent_count>=1) else 0)
    if (recent_count>=3 and gap) or score>=28: return "P0",score
    if recent_count>=2 or hist_count>=10 or score>=18: return "P1",score
    if recent_count>=1 or hist_count>=5: return "P2",score
    return "P3",score

def main():
    OUT_ROOT.mkdir(parents=True,exist_ok=True)
    records=[]
    topic_counts=Counter()
    topic_years=defaultdict(set)
    topic_rule={}
    domain_counts=Counter()

    for year in YEARS:
        path=STANDARD_ROOT/f"{year}-下半年"/"综合知识.md"
        if not path.exists():
            raise SystemExit(f"缺少标准化题库: {path.relative_to(ROOT)}")
        seen=set()
        for qnums,qtext,rule,score in parse_standardized(path):
            topic_rule[rule.topic]=rule
            for q in qnums:
                qid=f"{year}-H2-综合知识-{q:02d}"
                if qid in seen: raise SystemExit(f"重复题号: {qid}")
                seen.add(qid)
                records.append((year,q,qid,rule,score,qtext))
                topic_counts[rule.topic]+=1
                topic_years[rule.topic].add(year)
                domain_counts[rule.domain]+=1
        if len(seen)!=75:
            raise SystemExit(f"{year} 只解析到 {len(seen)} 个题号")
    if len(records)!=750:
        raise SystemExit(f"总题号应为750，实际{len(records)}")

    recent_hits,recent_quality=recent_signals()

    map_lines=[
        "---","type: exam-question-topic-map","subject: 系统架构设计师","status: generated",
        "scope: 2009-2018-综合知识","source: scripts/build-exam-topic-radar.py",
        "tags: [软考, 系统架构设计师, 历年真题, 知识点映射]","---","",
        "# 2009–2018 综合知识题目 → 知识点映射","",
        "> [!info] 自动分类第一版",
        "> 这是导航映射，不改写原题事实。分类依据题干 + 来源解析关键词；低置信度项进入人工复核队列。","",
        "| 题目标识 | 知识点 | 模块 | 当前笔记 | 覆盖状态 | 分类分 |",
        "| --- | --- | --- | --- | --- | ---: |",
    ]
    for year,q,qid,rule,score,_ in records:
        map_lines.append(f"| {qid} | {rule.topic} | {rule.domain} | {rule.note or '—'} | {rule.coverage} | {score} |")
    (OUT_ROOT/"2009-2018题目映射.md").write_text("\n".join(map_lines)+"\n",encoding="utf-8")

    rows=[]
    for topic in set(topic_counts)|set(recent_hits):
        rule=topic_rule.get(topic) or next((r for r in RULES if r.topic==topic),GENERIC)
        hc=topic_counts.get(topic,0); hy=len(topic_years.get(topic,set()))
        ryset=sorted(recent_hits.get(topic,set()))
        band,pscore=priority(hc,len(ryset),rule.coverage)
        rows.append((band,pscore,len(ryset),hc,hy,topic,rule,ryset))
    order={"P0":0,"P1":1,"P2":2,"P3":3}
    rows.sort(key=lambda x:(order[x[0]],-x[1],-x[3],x[5]))

    report=[
        "---","type: exam-topic-radar","subject: 系统架构设计师","status: generated",
        "scope: 2009-2018-history-plus-2019-2025-signals","source: scripts/build-exam-topic-radar.py",
        "tags: [软考, 系统架构设计师, 历年真题, 考频, 笔记缺口]","---","",
        "# 第二阶段：考点映射与近年趋势雷达","",
        "## 怎么读这张雷达","",
        "- 历史题数：2009–2018 标准化综合知识中映射到该主题的题号数。",
        "- 历史年份：2009–2018 中出现过该主题的年份数。",
        "- 近年年份：2019–2025 原始资料中检测到该主题的年份；这是趋势信号，不等于严格题频。",
        "- 当前笔记：只链接仓库现在确实已有的笔记；没有就明确标成当前未建。",
        "- 优先级：启发式排序。P0/P1 代表历史多且近年仍活跃，或近年活跃但当前缺笔记，不是官方权重。","",
        "> [!warning] 近年数据边界",
        "> 2019–2025 尚未正式标准化；部分资料为回忆版，部分 PDF 文字层质量较差。因此这里只用来判断“是否仍活跃”，不声称精确考了几题。","",
        "## 优先级总表","",
        "| 优先级 | 知识点 | 模块 | 历史题数 | 历史年份 | 近年出现年份 | 当前笔记 | 覆盖状态 |",
        "| --- | --- | --- | ---: | ---: | --- | --- | --- |",
    ]
    for band,pscore,ry,hc,hy,topic,rule,ryset in rows:
        if hc==0 and not ryset: continue
        report.append(f"| {band} | {topic} | {rule.domain} | {hc} | {hy} | {'、'.join(map(str,ryset)) if ryset else '—'} | {rule.note or '—'} | {rule.coverage} |")

    report += ["","## 当前笔记缺口：优先补什么","",
        "| 优先级 | 缺失主题 | 历史题数 | 近年出现年份 | 为什么要补 |",
        "| --- | --- | ---: | --- | --- |"]
    gaps=[r for r in rows if r[6].coverage in {"当前未建","待人工分类"} and (r[3]>0 or r[2]>0)]
    for band,pscore,ry,hc,hy,topic,rule,ryset in gaps[:30]:
        why="近年仍活跃且当前无原子笔记" if ryset else "历史反复出现但当前无原子笔记"
        report.append(f"| {band} | {topic} | {hc} | {'、'.join(map(str,ryset)) if ryset else '—'} | {why} |")

    report += ["","## 已有笔记中：哪些仍值得优先复习","",
        "| 优先级 | 知识点 | 历史题数 | 近年出现年份 | 笔记 |",
        "| --- | --- | ---: | --- | --- |"]
    existing=[r for r in rows if r[6].note and (r[3]>0 or r[2]>0)]
    for band,pscore,ry,hc,hy,topic,rule,ryset in existing[:30]:
        report.append(f"| {band} | {topic} | {hc} | {'、'.join(map(str,ryset)) if ryset else '—'} | {rule.note} |")

    report += ["","## 近年来源可用性","",
        "| 年份 | 来源类型 | 状态 | 可用字符量 |","| --- | --- | --- | ---: |"]
    for year,kind,status,chars in recent_quality:
        report.append(f"| {year} | {kind} | {status} | {chars} |")

    report += ["","## 模块历史分布","",
        "| 模块 | 2009–2018 题号数 |","| --- | ---: |"]
    for domain,count in domain_counts.most_common():
        report.append(f"| {domain} | {count} |")

    report += ["","## 后续动作","",
        "1. P0/P1 且当前未建的主题，优先交给教材线补原子笔记。",
        "2. P0/P1 且已有笔记的主题，下一步做“真题考法 → 当前笔记覆盖度”检查。",
        "3. 对其他/待人工分类和分类分较低的题目做人工复核，逐步修正规则。",
        "4. 等 2019+ 正式标准化后，把近年趋势信号升级成精确题频。","",
        "完整逐题映射见 [[2009-2018题目映射]]。"]
    (OUT_ROOT/"第二阶段-考点映射与近年趋势.md").write_text("\n".join(report)+"\n",encoding="utf-8")

    review=[
        "---","type: exam-topic-review-queue","subject: 系统架构设计师","status: generated",
        "source: scripts/build-exam-topic-radar.py","tags: [软考, 历年真题, 人工复核]","---","",
        "# 考点分类人工复核队列","",
        "优先复核其他/待人工分类或分类分较低（≤3）的题。","",
        "| 题目标识 | 当前分类 | 分类分 | 题干摘录 |",
        "| --- | --- | ---: | --- |",
    ]
    for year,q,qid,rule,score,qtext in records:
        if rule.topic==GENERIC.topic or score<=3:
            excerpt=re.sub(r"\s+"," ",qtext).replace("|","\\|")[:100]
            review.append(f"| {qid} | {rule.topic} | {score} | {excerpt} |")
    (OUT_ROOT/"考点分类人工复核队列.md").write_text("\n".join(review)+"\n",encoding="utf-8")
    print(f"OK: 750题完成主题映射，输出到 {OUT_ROOT.relative_to(ROOT)}")

if __name__=="__main__":
    main()
