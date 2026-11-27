#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""倪师检索器：把本地讲义索引 / 方剂库 / 穴位库 / 病名对照 / 医案库
检索成一段有限长度的上下文，供宿主模型在倪师人格约束下作答。

与 nihaisha_app/lib/services/llm_service.dart 同构；六处算法细节（贪心填满、
二跳预留、二跳轮流、针灸限源、第三跳次序、优先级三档）是 App 实测定下的，
改动前先看 references/retriever-spec.md。

用法：
    python nishi_retrieve.py "糖尿病有哪些方剂"
    python nishi_retrieve.py --json "足三里主治什么"    # 附结构化结果
    python nishi_retrieve.py --selftest                # 自检

ponytail: 1728 条线性扫描（~50ms），不建倒排索引；索引与 App 同源，避免两套漂移。
"""

import gzip
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"

# ---- 预算常量（llm_service.dart:106-135）----
MAX_HITS = 8
# 关键词「自由率」下限：低于此值判为滑窗拼接的假词，不进意图槽位。
# 实测分界很宽（真词 .64–.95，拼接词 .00–.22），.5 落在空档中间。
# ⚠️ holdout（test_holdout.py，8 条独立症状句）实测 6/8=75%，未达 80%：
#    露出的不是阈值高低，而是 free_ratio 对「口语方位/身体词」的系统性偏杀
#    （左边/右边/肚子/手心/脚心/腿软/早上/晚上 在讲稿口语段里常黏在邻字上），
#    以及 3-gram 拼接漏杀（扎右边、便黄）。调阈值前先看那份报告，别单点调。
FREE_MIN = 0.5
# P1-2/P1-3 (2026-11-27)：否定词与方位/身体/时段词口语里常黏邻字，free_ratio 系统性误杀。
# 这些词进 priority 档（tier=0）天然豁免过滤；只取提问里实际出现的，不按词表硬塞。
EXEMPT_TERMS = (
    "不渴", "无汗", "不恶寒", "不汗出", "不下利", "不呕", "不烦",
    "左边", "右边", "肚子", "手心", "脚心", "腿软", "早上", "晚上",
)
# TODO(性能)：prepare() 158ms/问，free_ratio 约占 60ms，因为每个候选词都要扫一遍
#   索引。词表有限（keywords_for 上限 32 个），可按词做进程内缓存
#   （_CACHE["free"]），跨进程持久化没必要。本轮不做。
# P1-2/P1-3 (2026-11-27 完成)：否定词与方位/身体词见 EXEMPT_TERMS，进 priority 档豁免过滤。
SNIPPET_SPAN = 200
MAX_SNIPPET_CHARS = 520
MAX_CONTEXT_CHARS = 3600
MAX_EXTRA_CHARS = 2400
MAX_FORMULA_LIST = 12
MAX_CASES = 3
MAX_CASE_CANDIDATES = 5
MAX_CASE_FORMULAS = 3
MAX_ACUPOINTS = 3
MAX_ACU_HITS = 3

# 方剂→经典反查只做旁路上下文，不改 classics 排名；3 方 × 每方 5 条足够。
MAX_FORMULA_HITS = 3
MAX_CLASSIC_PER_FORMULA = 5
MAX_FORMULA_HIT_BLOCK = 600

# 标题锚点：只匹配 skill 自带 classic_index 中的金匮条目，不依赖 App 文件路径。
SONGBEN_CROSSBOOK = {
    391: "吐利发汗，脉平，小烦者",
    392: "阴阳易之为病",
    393: "大病差后，劳复者",
    394: "伤寒差以后，更发热",
    395: "从腰以下有水气者",
    396: "喜唾久不了了",
    397: "伤寒解后，虚羸少气",
    398: "病人脉已解，而日暮微烦",
}
SONGBEN_CN = {391: "三九一", 392: "三九二", 393: "三九三", 394: "三九四",
              395: "三九五", 396: "三九六", 397: "三九七", 398: "三九八"}

ACU_KEYWORDS = {
    "针灸", "针", "灸", "扎针", "下针", "取穴", "穴位", "艾灸", "艾条",
    "刺血", "放血", "耳针", "耳穴", "拔罐", "火罐", "经络", "埋线", "电针",
}

EMERGENCY_KEYWORDS = {
    "胸口剧痛", "胸痛", "大汗淋漓", "心梗", "中风", "昏迷", "大出血",
    "呼吸困难", "窒息", "抽搐", "高热不退", "剧烈腹痛", "休克",
}

COUNT_WORDS = {
    "多少", "几个", "几首", "几种", "几条", "几例", "几篇", "几味",
    "一共", "总共", "总数", "数量", "统计",
}

# llm_service.dart:160-172 —— 子串判定，逐字照搬。含领域泛词与求诊话术泛词两层。
STOP_WORDS = {
    "什么", "怎么", "如何", "为何", "为什", "是否", "可以", "应该", "请问",
    "一下", "这个", "那个", "有没有", "能不能", "关系", "要点", "区别",
    "哪些", "多少", "哪里", "帮我", "告诉", "说说", "介绍", "是不是",
    "方剂", "方子", "处方", "方名", "经方", "中药", "中医", "药材", "药物",
    "医师", "医生", "病人", "症状", "治疗", "治法", "办法", "方法", "情况",
    "问题", "内容", "意思", "作用", "功效", "效果", "用法", "用量", "剂量",
    "时候", "怎么用", "用什么", "有哪些",
    "西医", "诊断", "医院", "检查", "患者",
}

# llm_service.dart:179-184 —— ⛔ 只放功能字，不要加「上下中里」（会切碎中焦/心下/上气）。
FUNCTION_CHARS = (
    "的了吗呢吧啊么什怎哪那些这有多几是个用能可会要该应为请帮我你他她它们"
    "和与及或而也都还又但如若者之"
)

SOURCE_LABELS = {
    "shanghan": "伤寒论讲稿",
    "jingui": "金匮要略讲稿",
    "neijing": "内经讲稿",
    "zhenjiu": "针灸讲稿",
    "bencao": "本草讲稿",
}
GUJI_BOOKS = {"lingshu": "黄帝内经·灵枢", "zhenjiudacheng": "针灸大成"}

# 经名 → 提纲条标题片段。用户问「太阳病」，而讲义标题写的是
# 「一、「太阳」之为病，脉浮，头项强痛而恶寒。」—— 「太阳病」不是它的子串
# （多了书名号和一个「之」），所以 77 条命中里一条提纲都没有（实测）。
# 命中经名时强制注入对应提纲。dict 保序，遍历稳定，不依赖 set。
SUTRA_OUTLINE = {
    "太阳病": "「太阳」之为病",
    "阳明病": "「阳明」之为病",
    "少阳病": "「少阳」之为病",
    "太阴病": "「太阴」之为病",
    "少阴病": "「少阴」之为病",
    "厥阴病": "「厥阴」之为病",
}

# 口语症状 → 古病名（讲稿原词）。这是 **skill 侧** 的补充层，不改 App 的
# disease_alias_index.json —— App 那套有 build + verify 门禁、绑发版流程，
# 不该为了 skill 多命中一条条文去回灌。词表进 priority 槽位，与「已知术语」同义。
# ⚠️ 扩展词必须**专有**：用「自利」这种短词会命中「小便自利」「不大便」，
# 语义正好相反（实测加入后比不加更差）。宁用长短语，不用宽泛词。
# ✅ TODO(别名 key 过 free_ratio) —— 2026-11-16 **方案否，已关闭**，勿再提。
#   实测（90 个 key 逐项算 free_ratio + 命中条目数）：
#     · 阈值 .5 会挡掉 48 个（53%）、.6 挡 56 个。但「短口语自由率天然低」的假设**是反的**：
#       2 字 key 30 个里 20 个达标（67%）、中位 .561；3 字中位 .250；4 字中位 **.000**。
#       越长越低 —— 被误杀的主体是**长口语**（「大便不成形」「醒了就睡不着」语料里根本没有原句）。
#     · free_ratio = 0 的 39 个里 **35 个是「语料 0 条」**（`total=0`，词根本不存在），
#       只有 4 个是真黏连（乳房胀 / 声音哑 / 腿软 / 拉稀）→ 门禁分不清「不存在」与「拼接垃圾」。
#   更根本的是**判据维度错**：free_ratio 判「该词在语料里是否黏着邻字」，用途是识别**滑窗产物**；
#   而 key 是**用户原话的子串**，不是 n-gram —— 语料里有没有这个词，跟它能否当别名无关。
# TODO(别名展开目标的排序权重，待评)：`腰酸腿软` 首槽问题的真因不是「腿软是假词」，
#   而是 priority 档**免 free_ratio** + 排序键 `(tier, total)` 让别名目标整档压在同题真词之前。
#   待评：别名展开出的目标，是否该以**低于同题真词**的权重参与排序？（只报方案，未动代码）
#
# 补词规则（2026-11-16 第二批起生效，补词前先读这两条）：
# ① 同一口语词只映射到**一个古名家族**。一对多会把 priority 槽位稀释（早期
#    「打嗝→噫气+呃逆」就是一键两槽）。要区分症状就拆 key，不是给一个 key 挂多个目标
#    （喉咙痛→咽痛、喉咙肿→咽肿 是两个 key；不是一个 key 挂 咽痛+咽肿）。
# ② 不因单条 holdout 追加，按**症状类整组补**（咽喉类 / 妇科类 / 乳房类 …）。
#    单条失败先归因，分三类：别名缺口 / free_ratio 边界 / 语料真的没有对应条文。
#    只有确认是整类的别名缺口才补，且补完必须跑同一批 holdout（不增不减、判据不改）。
SYMPTOM_ALIAS = {
    "大便不成形": ["自利益甚", "下利清谷"],
    "大便不成型": ["自利益甚", "下利清谷"],
    "大便稀": ["自利益甚", "下利清谷"],
    "拉稀": ["下利清谷", "自利益甚"],
    "腹泻": ["下利清谷", "自利益甚"],
    "手脚出汗": ["手足濈然汗出", "手足汗出"],
    "手脚出冷汗": ["手足濈然汗出", "四肢厥逆"],
    "手心出汗": ["手足濈然汗出"],
    "手脚冰凉": ["四肢厥逆"],
    "手脚冰冷": ["四肢厥逆"],
    "畏寒": ["四肢厥逆"],
    "疲劳": ["但欲寐"],
    "提不起劲": ["但欲寐"],
    "想睡觉": ["但欲寐"],
    "胸闷": ["胸胁苦满"],
    # 原为 "怕冷": ["手足濈然汗出", "四肢厥逆"]，语义错 —— 怕冷是恶寒，不是手足汗出。
    # 实测该目标全库仅 2 条（伤寒 2），却把「没有发烧但是怕冷」「腰酸腿软还怕冷」
    # 两条的首条都带到一九一条（阳明中寒·手足濈然汗出）。改 恶寒 后：
    # 「没有发烧但是怕冷」首条 = 一条「太阳之为病，脉浮，头项强痛而恶寒」；
    # 「腰酸腿软还怕冷」首条 = 二九条（微恶寒·脚挛急）。两条均变好，命中不变。
    # 目标词按质量二选一：恶寒 total=150 / 条文类 140；畏寒 total=4 / 条文类 3。
    "怕冷": ["恶寒"],
    # ⛔ 原「胃胀 → 心下痞」已移除（2026-11-16 实测）：target 心下痞 的首条落在一五条
    #  （太阳病下之后其气上冲，与胃胀无关）。移除后首条变金匮胸痹「心中痞气，气结在胸，
    #  胸满，胁下逆抢心，枳实薤白桂枝汤主之」，42+13 逐条无命中丢失（仅该用例首条变化）。
    # 「遂漏不止」是二〇条桂枝加附子汤的标准证；不映射则被「发汗太多」带到
    # 一七五条（风湿相搏），首条从正解退化（实测）。
    "汗止不住": ["遂漏不止"],
    "出汗不止": ["遂漏不止"],
    "汗流不止": ["遂漏不止"],
    # 丑时（1–3 点）醒 → 虚劳虚烦不得眠，酸枣仁汤；不映射则「四点」这种
    # 数字巧合词抢走首条（实测落到「第四章·任脉经穴」）。
    "半夜醒来": ["虚烦不得眠"],
    "半夜醒": ["虚烦不得眠"],
    "凌晨醒来": ["虚烦不得眠"],
    "凌晨醒": ["虚烦不得眠"],
    "三四点醒": ["虚烦不得眠"],
    "早醒": ["虚烦不得眠"],
    "醒了就睡不着": ["虚烦不得眠"],
    "醒来就睡不着": ["虚烦不得眠"],
    # 口语「一阵冷一阵热」= 往来寒热；不映射则滑窗切出的「冷一阵热」把
    # 一〇四条挡在 8 条之外（实测）。
    "一阵冷一阵热": ["往来寒热"],
    "忽冷忽热": ["往来寒热"],
    "时冷时热": ["往来寒热"],

    # ---- 通用口语→古名（批次补充，2026-11-16）----
    # 每条目标词过四道门禁：
    #   ① 库中 total ≥ 1；② 长度 ≥ 2（单字太泛）；③ total ≤ 300（泛化词白占 priority 槽）；
    #   ④ 至少 1 条命中来自条文类来源（伤寒/金匮/内经/针灸），只有本草命中不算 ——
    #      本草是「一味药一条」，拿它当症状锚点会把辨证提问的首条带到本草条目。
    # ④ 是被实测打出来的：撤掉「长痘→面皰」的那次见 §面皰 处的注释。
    # 上焦/头面
    "嘴苦": ["口苦"], "嘴里苦": ["口苦"], "口里苦": ["口苦"],
    "喉咙干": ["咽干"], "嗓子干": ["咽干"], "喉干": ["咽干"],
    "眼花": ["目眩"], "头晕眼花": ["目眩"],
    "耳鸣": ["耳鸣"], "耳朵响": ["耳鸣"],
    # 长痘/痤疮：库里只有「面皰」3 条且全在本草里（唯一一个零条文类命中的目标词），
    # 映射过去会把辨证提问的首条带到本草条目（实测「手脚冰冷但脸上长痘」首条变
    # 「上经·榆皮」）。按门禁第 4 条撤掉，登记为「无好目标词」。
    # 胸腹
    "心慌": ["心悸", "心下悸"],
    "胸口痛": ["胸痛"], "胸口疼": ["胸痛"],
    # 打嗝：原挂 ["噫气","呃逆"] 双目标（违反规则①），且 呃逆(total=6) 把首条带到
    # 内经「第七十五篇 着至教论篇」（章级条目）。实测三种写法：
    #   移除 → 首条变四〇条小青龙，但「吃完东西就胀还打嗝」命中丢失（不许）；
    #   →["呃逆"] → 首条不变（第七十五篇 来自呃逆），无效；
    #   →["噫气"] → 首条 = 一六一条「心下痞硬，噫气不除者，旋覆代赭汤主之」，命中不变。
    # 取第三种：既是正解，又消掉一个双目标。
    "打嗝": ["噫气"], "打呃": ["噫气", "呃逆"], "呃逆": ["噫气", "呃逆"],
    "反酸": ["吞酸", "吐酸"], "烧心": ["吞酸", "心中疼热"],
    "没胃口": ["不能食"], "吃不下": ["不能食"], "不想吃饭": ["不欲食"],
    # 二便
    "便秘": ["不大便", "大便难"], "便秘不通": ["不大便"], "便秘干结": ["大便硬"],
    "尿频": ["小便数"], "小便次数多": ["小便数"], "尿不出来": ["小便不利"],
    "浮肿": ["水肿"],
    # 四肢/肌肤
    "腿软": ["脚弱", "胫酸"], "腿没劲": ["脚弱"], "脚软": ["脚弱"],
    "抽筋": ["脚挛急"],
    "手脚发麻": ["麻木", "不仁"], "手麻": ["麻木", "不仁"], "脚麻": ["麻木", "不仁"],
    "皮肤痒": ["身痒", "瘙痒"], "身上痒": ["身痒", "瘙痒"],
    # 汗出
    "怕风": ["恶风"], "出虚汗": ["自汗"],
    "睡着了出汗": ["盗汗"], "夜里出汗": ["盗汗"],
    "打喷嚏": ["清涕"], "流清涕": ["清涕"],

    # ---- 第二批：按症状类整组补（2026-11-16），遵守文件头两条规则 ----
    # 每词都过四道门禁（total≥1 / 长度≥2 / total≤300 / 至少 1 条条文类命中）。
    # 咽喉类
    "喉咙痛": ["咽痛"], "嗓子疼": ["咽痛"], "咽喉痛": ["咽痛"],
    "喉咙肿": ["咽肿"],
    "嗓子哑": ["声哑"], "声音哑": ["声哑"],
    "喉咙堵": ["梅核气"],
    # 妇科类
    "月经": ["经水"], "月经不调": ["经水不利"], "闭经": ["经闭"],
    "月经淋漓": ["漏下"], "崩漏": ["崩中"], "白带多": ["带下"],
    # 乳房类
    # ✅ 已移除 乳房胀痛 / 乳房胀（2026-11-16），证据见下：
    #    · 目标「乳胀」全库仅 **1 条**命中，且那条是针灸讲稿「第四章·任脉经穴」
    #      —— 针灸 72 条 / 整章一条，属**章级条目**，等于章级假阳性
    #      （「月经来之前乳房胀痛」首条就是它）。
    #    · 该用例命中并不依赖 乳胀，而是靠 月经 → 经水 命中一四三 / 一四四 / 一四五
    #      （妇人中风·经水适来，真条文）。实测移除两个 key 后首条变一四三条、
    #      **命中不变**（holdout 仍 12/13）→ 纯改善，故直接移除，不留「待处理」。
    #    「乳房痛 → 乳痛」保留：乳痛 3 条全属条文类（guji 2 / zhenjiu 1），非章级独占。
    "乳房痛": ["乳痛"],
    # ⚠️ 本批未收，原因是「库里没有能用的目标词」而非漏补：
    #   痛经（经行腹痛 0 条）、月经后期（0 条）、乳房肿块（乳岩仅 2 条且属重证，语义过强）、
    #   咽乾（29 条全在古籍/本草，零条文类命中，被门禁 ④ 挡）。
}
# ⚠️ 仍缺的口语（本轮补完后 holdout 复盘得到，不是漏补，是"没有好目标词"）：
#   「打嗝」这一类里「哕」只有 4 条，太窄没收；「痤疮」库里 0 条，改映射到「面皰」(3)。
#   补新词前先跑门禁：库里 total ≥1、长度 ≥2、total ≤300，否则会白占 priority 槽位。
# TODO(数据 alias，不塞进检索逻辑)：「心下痞硬，噫气不除」期望旋覆代赭汤，但讲稿写作
#   「旋复花代赭石汤」（复/覆 异体，同 蛰/蟅/䗪 那一类）。FormulaRepository.search 只做
#   name/alias.contains，所以正解是数据侧在 formulas.json 的 alias 显式登记，
#   ⛔ 不要在检索层加字形映射。

_CACHE = {}


# ---------------------------------------------------------------- 数据加载

def _json(name):
    if name not in _CACHE:
        with open(DATA / name, encoding="utf-8") as f:
            _CACHE[name] = json.load(f)
    return _CACHE[name]


def load_index():
    """索引条目；预存小写文本，避免每次检索重复 lower（30MB 文本）。"""
    if "index" not in _CACHE:
        with gzip.open(DATA / "classic_index.json.gz", "rt", encoding="utf-8") as f:
            raw = json.load(f)["entries"]
        _CACHE["index"] = [
            {
                "s": e.get("s") or "",
                "t": e.get("t") or "",
                "a": e.get("a"),
                "b": e.get("b"),
                "x": e.get("x") or "",
                "tl": (e.get("t") or "").lower(),
                "xl": (e.get("x") or "").lower(),
            }
            for e in raw
        ]
    return _CACHE["index"]


def load_formulas():
    """返回 (全部方剂, 正名→方剂, 候选名列表)。"""
    if "formulas" not in _CACHE:
        items = _json("formulas.json")["formulas"]
        by_name = {f["name"]: f for f in items}
        candidates = []
        for f in items:
            candidates.append(f["name"])
            for al in (f.get("alias") or "").split(","):
                al = al.strip()
                if al:
                    candidates.append(al)
        _CACHE["formulas"] = (items, by_name, candidates)
    return _CACHE["formulas"]


def load_formula_index():
    """方剂→经典/讲稿提及；跳过 App 的 `_v` 版本键。"""
    if "formula_index" not in _CACHE:
        _CACHE["formula_index"] = {
            k: v for k, v in _json("formula_index.json").items()
            if isinstance(v, dict)
        }
    return _CACHE["formula_index"]


def _classic_titles():
    """按 asset 反查标题；j 按 skill 索引中 jingui 顺序对齐 App seq。"""
    if "classic_titles" not in _CACHE:
        sh, jg = {}, []
        for e in load_index():
            a = e.get("a") or ""
            if e["s"] == "shanghan":
                m = re.search(r"clause_(\d+)\.md$", a)
                if m:
                    sh[int(m.group(1)) - 1] = e["t"]
            elif e["s"] == "jingui":
                jg.append(e["t"])
        _CACHE["classic_titles"] = (sh, jg)
    return _CACHE["classic_titles"]


def formula_classic_hits(name):
    """方剂见于哪些伤寒/金匮条目；讲稿提及只给计数，不冒充条文。"""
    v = load_formula_index().get(name)
    if not v:
        return None
    sh_titles, jg_titles = _classic_titles()
    out = {"name": name, "shanghan": [], "jingui": [], "lectureCounts": {}}
    for seq in (v.get("s") or [])[:MAX_CLASSIC_PER_FORMULA]:
        out["shanghan"].append({
            "songben": seq + 1,
            "title": sh_titles.get(seq, ""),
        })
    for seq in (v.get("j") or [])[:MAX_CLASSIC_PER_FORMULA]:
        out["jingui"].append({"title": jg_titles[seq] if seq < len(jg_titles) else ""})
    for key, label in (("b", "bencao"), ("z", "zhenjiu")):
        out["lectureCounts"][label] = sum(
            int(x.get("n") or 0) for x in (v.get(key) or []) if isinstance(x, dict)
        )
    return out


def crossbook_hits(q):
    """宋本391-398在金匮；按标题锚点重定向，不依赖 App 资产路径。"""
    text = normalize(q)
    nums = []
    for n in SONGBEN_CROSSBOOK:
        if re.search(r"(?<!\d){}(?!\d)".format(n), text) or SONGBEN_CN[n] in text:
            nums.append(n)
    if not nums:
        return []
    out = []
    for n in nums:
        anchor = SONGBEN_CROSSBOOK[n]
        e = next((x for x in load_index()
                  if x["s"] == "jingui" and anchor in x["t"]), None)
        if not e:
            continue
        out.append({
            "source": e["s"],
            "label": label_of(e["s"], e.get("b")),
            "title": e["t"],
            "asset": e["a"],
            "snippet": _snippet(e["x"], -1, len(q), SNIPPET_SPAN),
            "songben": n,
        })
    return out


def load_acupoints():
    if "acu" not in _CACHE:
        items = _json("acupoints.json")["acupoints"]
        # 正名带「穴」（足三里穴），提问与医案多写短名（足三里）→ 两形态都要进候选。
        # ponytail: 未复刻 App 的 kShortNameLinkForm 避撞表；撞普通词最多多给一条穴位资料。
        by_name, names = {}, []
        for p in items:
            full = p["name"]
            by_name[full] = p
            names.append(full)
            short = full.replace("穴", "")
            if len(short) >= 2:
                by_name.setdefault(short, p)
                names.append(short)
        _CACHE["acu"] = (items, by_name, ordered_by_len(names))
    return _CACHE["acu"]


def load_aliases():
    if "alias" not in _CACHE:
        _CACHE["alias"] = _json("disease_alias_index.json")["entries"]
    return _CACHE["alias"]


def load_cases():
    """解析 cases/00_merged_table.md（12 列规整表格，无内嵌管道符）。

    与 medical_case_data.dart:400-444 同规则：无方剂 / 未公开 / 未提及 的剔除。
    """
    if "cases" in _CACHE:
        return _CACHE["cases"]
    path = ROOT / "cases" / "00_merged_table.md"
    out = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line.startswith("|"):
                continue
            cells = [c.strip() for c in line.split("|")]
            if cells and not cells[0]:
                cells.pop(0)
            if cells and not cells[-1]:
                cells.pop()
            if not cells or not re.fullmatch(r"\d+", cells[0] or ""):
                continue
            cells += [""] * (12 - len(cells))
            cells = ["" if c == "---" else c for c in cells]
            formula = cells[6]
            if not formula.strip() or "未公开" in formula or formula.strip() == "未提及":
                continue
            out.append({
                "seq": int(cells[0]),
                "date": cells[1], "patient": cells[2], "diagnosis": cells[3],
                "mechanism": cells[4], "western": cells[5], "formula": formula,
                "acupuncture": cells[7], "method": cells[8], "result": cells[9],
                "advice": cells[10], "view": cells[11],
                # medical_case_data.dart:307-309
                "search": normalize("{} \n{} \n{} \n{} \n{} \n{}".format(
                    cells[3], formula, cells[9], cells[11], cells[4], cells[2])).lower(),
                "diagNorm": normalize(cells[3]).lower(),
            })
    _CACHE["cases"] = out
    return out


def load_t2s():
    if "t2s" not in _CACHE:
        _CACHE["t2s"] = _json("t2s.json")
    return _CACHE["t2s"]


def ordered_by_len(items):
    """保序去重后按长度降序。

    ⛔ 不能用 sorted(set(...))：set 的迭代顺序受 str hash 随机化影响，**等长元素
    跨进程顺序会变**。实测「四逆汤和理中汤」两个 3 字方名一次排出 四逆→理中、
    下一次排 理中→四逆，前 8 条命中结果完全不同 —— 确定性检索的前提就没
    了。dict.fromkeys 保序 + sorted 稳定排序，等长时保留原始顺序。
    """
    return sorted(dict.fromkeys(items), key=lambda s: -len(s))


def normalize(text):
    """繁体 → 简体。索引正文构建期已统一简体，只归一问句。"""
    if not text:
        return ""
    t = load_t2s()
    return "".join(t.get(ch, ch) for ch in text)


# ---------------------------------------------------------------- 切词

def is_content_word(w):
    for s in STOP_WORDS:
        if s in w:
            return False
    for ch in w:
        if ch in FUNCTION_CHARS:
            return False
    return True


def keywords_for(q):
    """2–4 字连续片段，功能字过滤，长词优先，上限 32（llm_service.dart:199-209）。

    ⛔ 滑窗不得跨标点：删标点后拼成连续串再滑窗，会把相邻两个症状缝成假词
    （「头晕乏力失眠口苦」产出「晕乏力失」「眠口苦大」），实测 32 个槽位里 23 个
    是这种垃圾，真词被挤到 24 位之后。先按非汉字边界分段，段内再滑窗。
    """
    segments = [s for s in re.split(r"[^\u4e00-\u9fffA-Za-z0-9]+", q) if s]
    words, seen = [], set()
    for ln in range(4, 1, -1):
        for seg in segments:
            for i in range(len(seg) - ln + 1):
                w = seg[i:i + ln]
                if w not in seen and is_content_word(w):
                    seen.add(w)
                    words.append(w)
    return words[:32]


def extract_names(text, candidates):
    """已知名称抽取：长度降序非重叠扫描（短名不得截胡长名）。"""
    if not text:
        return []
    norm = normalize(text).lower()
    used = [False] * len(norm)
    out = []
    for name in ordered_by_len(candidates):
        if len(name) < 2:
            continue
        n = normalize(name).lower()
        start = 0
        while True:
            at = norm.find(n, start)
            if at < 0:
                break
            end = at + len(n)
            if not any(used[at:end]):
                out.append(name)
                for i in range(at, end):
                    used[i] = True
            start = end
    return out


def extract_formula_names(text):
    return extract_names(text, load_formulas()[2])


def unverified_formulas(answer, r):
    """回答里出现、但本次检索块未支撑的方名（llm_service.dart:951-963 直译）。
    只挑出不改写、不拦截回答；天花板＝只认方剂库里有的方名，漏报但不误报。
    支撑面 = 命中方剂清单 ∪ 医案用方 ∪ 讲义片段正文里的方名。
    """
    cited = extract_formula_names(answer)
    if not cited:
        return []
    supported = set(r["formulas"])
    for c in r["cases"]:
        supported.update(extract_formula_names(c["formula"]))
    for h in r["classics"]:
        supported.update(extract_formula_names(h["snippet"]))
    return [f for f in cited if f not in supported]


def extract_disease_names(text):
    cands = []
    for e in load_aliases():
        cands.append(e["a"])
        cands.extend(e.get("m") or [])
        cands.extend(e.get("al") or [])
    return extract_names(text, cands)


# ---------------------------------------------------------------- 讲义检索

def label_of(source, book_id):
    if source == "guji":
        return GUJI_BOOKS.get(book_id, "古籍原文")
    return SOURCE_LABELS.get(source, source)


def _snippet(text, idx, qlen, span):
    """clasic_search_service.dart:213-223 —— idx<0 表示仅标题命中，取正文开头。"""
    if not text:
        return ""
    n = len(text)
    if idx < 0:
        start, end = 0, min(span * 2, n)
    else:
        start, end = max(0, idx - span), min(idx + qlen + span, n)
    raw = text[start:end].replace("\n", " ").strip()
    return ("…" if start > 0 else "") + raw + ("…" if end < n else "")


def search(query, snippet_span=32, max_results=40, only_sources=None):
    """标题命中优先，其次正文命中（classic_search_service.dart:144-189）。"""
    q = (query or "").strip()
    if not q:
        return 0, []
    needle = normalize(q).lower()
    title_hits, body_hits = [], []
    total = 0
    for e in load_index():
        if only_sources and e["s"] not in only_sources:
            continue
        in_title = needle in e["tl"]
        idx = e["xl"].find(needle)
        if not in_title and idx < 0:
            continue
        total += 1
        if len(title_hits) + len(body_hits) >= max_results:
            continue
        hit = {
            "source": e["s"],
            "label": label_of(e["s"], e["b"]),
            "title": e["t"],
            "asset": e["a"],
            "snippet": _snippet(e["x"], -1 if in_title else idx, len(q), snippet_span),
        }
        (title_hits if in_title else body_hits).append(hit)
    return total, title_hits + body_hits


def _key(h):
    return "{}|{}".format(h["source"], h["title"])


_PUNCT = set("，。；、：！？「」『』（）《》【】…—·,.!?;:\"'()[]{}<>\n\r\t ")


def free_ratio(needle, sample=30):
    """词在语料里「自由」出现的比例（两侧是标点或条目边界即算自由）。

    用来分开真词与滑窗切出来的拼接 n-gram —— 后者在语料里永远黏在前后字上
    （「左边腹痛扎右脚」的「痛扎」、「寒热往来就…」的「来就」），自由率≈0；
    真词（「身疼，腰痛，骨节」）两侧多是标点。实测：腰痛 .71 / 痛扎 .00，
    睡不着 .64 / 来就 .01，失眠 .67 / 三四 .15，但欲寐 .95。

    只采样前 sample 次出现，够判阈值即可；全量扫会拖到 30ms/词。
    """
    n = normalize(needle).lower()
    if not n:
        return 0.0
    free = total = 0
    ln = len(n)
    for e in load_index():
        x = e["xl"]
        i = x.find(n)
        while i >= 0:
            total += 1
            if ((i == 0 or x[i - 1] in _PUNCT)
                    or (i + ln >= len(x) or x[i + ln] in _PUNCT)):
                free += 1
            i = x.find(n, i + 1)
        if total >= sample:
            break
    return (free / total) if total else 0.0


def outline_hits(q):
    """命中经名时取出对应提纲条（P1-1）。按 dict 插入顺序返回，稳定。"""
    text = normalize(q)
    out = []
    for name, frag in SUTRA_OUTLINE.items():
        if name not in text:
            continue
        for e in load_index():
            if e["s"] == "shanghan" and frag in e["t"]:
                out.append({
                    "source": e["s"],
                    "label": label_of(e["s"], e["b"]),
                    "title": e["t"],
                    "asset": e["a"],
                    "snippet": _snippet(e["x"], -1, len(q), SNIPPET_SPAN),
                })
                break
    return out


def _fill_rounds(pool, priority_terms, keyword_terms, cap, span):
    """多意图分配：priority 词无条件优先，普通关键词按稀有度进 round 轮流。

    为什么不用纯贪心：priority 里有两个方名时（「四逆汤和理中汤怎么分」），
    第一方会吃满全部槽位、第二方 0 条，问鉴别只答一半；多症状同理，首个
    碰巧命中的症状词独吞 8 条（「头晕乏力失眠口苦…」只答了头晕）。

    为什么不用纯 round：切词认不出无标点句里的症状边界（「头晕乏力失眠」
    切出「晕乏力失」）。这类假词必须先筛掉，否则无论正序还是稀有度序都会
    排错：按稀有度，total=3 的「痛扎」抢第 1 名（「腰痛扎哪个穴」→ 麻黄升麻
    汤条）；按词序，total=320 的「来就」抢前面。筛据是 free_ratio —— 拼接词
    在语料里永远黏在邻字上，自由率≈0。三条门槛：total ≥ 3、free_ratio ≥ .5、
    priority 词（已知方名 / 古病名 / 症状古名）不受限，它们本身即精准术语。

    同档内按 total 升序（越专有越先占第 1 轮），list.sort 稳定，跨进程一致；
    单词场景退化为「取该词前 cap 条」，与原贪心一致不退化。

    设计决策：priority 档内「稀有方先占首槽」，即鉴别题优先暴露少用的那一方。
    代价：常见方在鉴别题里稳定落第 2（桂枝汤/麻黄汤恒为麻黄汤在前），已由
    test_differential.py 的 C 类注释记录。不改 tie-break —— 改它要动本函数的
    排序主干，风险大于收益。

    ⛔ 2026-11-16 回滚记录：曾加过「keyword 档主诉词固定占第 1 轮首槽」
    （main_complaint），因把「下利清谷，手足厥冷，脉微欲绝」的逐字正解
    三一七条换成九一条而被回滚。若再提同类方案，必须先证明它不替换正解首条。

    ⛔ P3「2 字词免 free_ratio、只允许进 rnd≥1」——**设计不可行，判死，不再评估**
    （2026-11-16 定论，不是暂缓）。理由：**约束维度选错**。它限的是**轮次**，不是
    **条位**；而 round-robin 第 1 轮只落「通过 free_ratio 的真词组数」条 —— 真词组
    数 < 3 时（实测 `腰痛扎哪个穴` 只剩「腰痛」、`咳出来的痰是黄的` 只剩「咳出来」、
    `咳嗽有白色的痰` 只剩「咳嗽」、`左边肚子疼扎右边脚` 只剩「扎右边」total=5），
    第 2 轮立刻把免检词插到**第 2 位**，结构上守不住前 3。实测落位：
    腰痛(rnd0) → 痛扎(rnd1) → 腰痛(rnd1) → 痛扎(rnd2) → 腰痛(rnd2) → 痛扎(rnd3)…
    免检词稳定占 2/4/6/8 位。
    代价已量化（42 回归 + 13 holdout 共 55 条）：恢复条 35 / 挤掉条 35（对称换血），
    其中 **23 条是「本来含 want 的正解被另一条也含 want 的条替换」**，与上面
    main_complaint 同型失败；holdout 12/13→13/13 的收益不足以抵。⛔ 不要再试
    「只进第 N 轮」这类约束 —— 除非改成按**条位**约束。
    """
    groups, best = [], 0

    def collect(terms, tier, min_total):
        nonlocal best
        for w in terms:
            if not (w or "").strip():
                continue
            total, hits = search(w, span, cap)
            if total > best:
                best = total
            if not hits or total < min_total:
                continue
            # priority 档是真术语，不做自由率筛查（「遂漏不止」这类短语够长够专）
            if tier and free_ratio(w) < FREE_MIN:
                continue
            groups.append((tier, total, hits))

    collect(priority_terms, 0, 1)
    collect(keyword_terms, 1, 3)
    groups.sort(key=lambda g: (g[0], g[1]))

    rnd = 0
    while len(pool) < cap:
        added = False
        for _, _, hits in groups:
            if len(pool) >= cap:
                break
            if rnd >= len(hits):
                continue
            h = hits[rnd]
            k = _key(h)
            if k in pool:
                continue
            pool[k] = h
            added = True
        if not added:
            break
        rnd += 1
    return best


def retrieve_result(q, priority=(), extra=(), seed=(), cap=MAX_HITS):
    """seed 强制落位 → priority+原关键词 round 轮流 → extra 回填。"""
    total, direct = search(q, SNIPPET_SPAN, cap)
    if direct and not priority and not extra and not seed:
        return {"total": total, "hits": direct}

    pool = {}
    for h in list(seed) + list(direct):
        if len(pool) >= cap:
            break
        pool.setdefault(_key(h), h)
    best_total = total

    # ① priority（古病名 / 方名 / 症状古名）与 ② 原关键词**合并**分配。
    #    分档而非两次独立填池：两档共用 8 个槽位，先跑的那档必然吃满。
    best_total = max(best_total, _fill_rounds(
        pool, list(priority), keywords_for(q), cap, SNIPPET_SPAN))
    # ③ 病名对照的补充叫法：优先级最低，只在剩余槽位回填
    for w in extra:
        if len(pool) >= cap:
            break
        r_total, hits = search(w, SNIPPET_SPAN, cap)
        best_total = max(best_total, r_total)
        for h in hits:
            if len(pool) >= cap:
                break
            pool.setdefault(_key(h), h)
    return {"total": best_total, "hits": list(pool.values())}


def extend_by_formulas(base, formulas):
    """二跳：医案反推的方剂回讲稿找原文（llm_service.dart:417-445）。"""
    pool = {_key(h): h for h in base["hits"]}
    for rnd in range(MAX_HITS):
        added = False
        for f in formulas:
            if len(pool) >= MAX_HITS:
                break
            _, hits = search(f, SNIPPET_SPAN, rnd + 1)
            if len(hits) <= rnd:
                continue
            h = hits[rnd]
            if _key(h) in pool:
                continue
            pool[_key(h)] = h
            added = True
        if not added:
            break
    return {"total": base["total"], "hits": list(pool.values())}


# ---------------------------------------------------------------- 医案 / 穴位

def retrieve_cases(q, maximum=MAX_CASES):
    """llm_service.dart:449-497 —— 按命中词长度加权，诊断命中再加一倍。"""
    all_cases = load_cases()
    needles = set(extract_disease_names(q)) | set(extract_formula_names(q))
    if not needles:
        kws = sorted([w for w in keywords_for(q) if len(w) >= 2], key=len)[:10]
        needles.update(kws)
    if not needles:
        return []
    norm = [n for n in {normalize(x).lower() for x in needles} if n]

    scored = []
    for c in all_cases:
        score = 0
        for n in norm:
            if n in c["search"]:
                score += len(n)
            if n in c["diagNorm"]:
                score += len(n) * 2
        if score > 0:
            scored.append((c, score))
    if not scored:
        return []
    scored.sort(key=lambda e: (-e[1], len(e[0]["diagnosis"]), e[0]["seq"]))
    return [c for c, _ in scored[:maximum]]


def retrieve_acupoints(q, maximum=MAX_ACUPOINTS):
    """提问里点名的穴位，最长优先非重叠（llm_service.dart:512-547）。"""
    text = normalize(q)
    if not text:
        return []
    items, by_name, names = load_acupoints()
    out, used = [], [False] * len(text)
    for name in names:
        if len(out) >= maximum:
            break
        if len(name) < 2:
            continue
        start = 0
        while True:
            at = text.find(name, start)
            if at < 0:
                break
            end = at + len(name)
            if not any(used[at:end]) and name in by_name:
                out.append(by_name[name])
                for i in range(at, end):
                    used[i] = True
            start = end
    return out


def is_acupuncture_query(q):
    text = normalize(q)
    if any(k in text for k in ACU_KEYWORDS):
        return True
    return bool(retrieve_acupoints(q))


def retrieve_acu_hits(q):
    """限源 zhenjiu（仅 72 条，全源检索永远排不上）。llm_service.dart:550-588。"""
    words = [p["name"] for p in retrieve_acupoints(q)]
    words += [w for w in keywords_for(q) if not any(a in w for a in ACU_KEYWORDS)]
    words.append(q)
    out = {}
    for w in words:
        if not (w or "").strip() or len(out) >= MAX_ACU_HITS:
            continue
        _, hits = search(w, SNIPPET_SPAN, MAX_ACU_HITS, only_sources={"zhenjiu"})
        for h in hits:
            if len(out) >= MAX_ACU_HITS:
                break
            out.setdefault(_key(h), h)
    if not out:
        # 兜底：至少给「什么时候不能下针」那一篇
        _, hits = search("不下针", SNIPPET_SPAN, 1, only_sources={"zhenjiu"})
        for h in hits:
            out.setdefault(_key(h), h)
    return list(out.values())


def jump_by_acupoints(q):
    """第三跳：症状 → 穴位（按主治命中次数）→ 医案配穴（llm_service.dart:597-635）。"""
    symptoms = [w for w in keywords_for(q)
                if len(w) >= 2 and not any(a in w for a in ACU_KEYWORDS)][:4]
    if not symptoms:
        return [], []
    items, _, _ = load_acupoints()
    scored = []
    for p in items:
        notes = p.get("clinicalNotes") or ""
        if not notes:
            continue
        s = sum(notes.count(w) for w in symptoms)
        if s > 0:
            scored.append((p, s))
    scored.sort(key=lambda e: -e[1])
    points = [p for p, _ in scored[:MAX_ACUPOINTS]]
    if not points:
        return [], []
    scored_cases = []
    for c in load_cases():
        acu = c.get("acupuncture") or ""
        if not acu:
            continue
        # 每穴最多计 1 次（正名/短名同时出现不重复加权）
        n = sum(1 for p in points
                if p["name"] in acu or p["name"].replace("穴", "") in acu)
        if n > 0:
            scored_cases.append((c, n))
    scored_cases.sort(key=lambda e: -e[1])
    return points, [c for c, _ in scored_cases[:MAX_CASES]]


# ---------------------------------------------------------------- 病名对照

def match_aliases(q):
    text = normalize(q)
    out = []
    for e in load_aliases():
        keys = [e["a"]] + (e.get("m") or []) + (e.get("al") or [])
        if any(k and k in text for k in keys):
            out.append(e)
    return out


def expand_terms(aliases):
    seen, out = set(), []
    for e in aliases:
        for t in [e["a"]] + (e.get("m") or []) + (e.get("al") or []):
            if t and t not in seen:
                seen.add(t)
                out.append(t)
    return out


def symptom_terms(q):
    """口语症状 → 古病名。进 priority 槽位：原词（大便）命中的多是便秘条文，
    真答案在「自利益甚」那条里，不让它优先就只能拿一堆无关条辨。"""
    text = normalize(q)
    out = []
    for k, vs in SYMPTOM_ALIAS.items():
        if k in text:
            for v in vs:
                if v not in out:
                    out.append(v)
    return out


def disease_brief(aliases):
    if not aliases:
        return ""
    lines = ["【古今·中西医病名对照】"]
    for e in aliases:
        ancient, modern, other = e["a"], "、".join(e.get("m") or []), "、".join(e.get("al") or [])
        bits = [ancient]
        if modern:
            bits.append("今名/西医名：" + modern)
        if other:
            bits.append("又称：" + other)
        note = (e.get("note") or "").strip()
        lines.append("· " + "｜".join(bits) + ("　原话：" + note if note else ""))
    return "\n".join(lines)


# ---------------------------------------------------------------- 编排

def is_emergency(q):
    text = normalize(q)
    return any(k in text for k in EMERGENCY_KEYWORDS)


def stats_if_counting(q, matched, n_cases):
    if not any(w in q for w in COUNT_WORDS):
        return ""
    entries = load_index()
    counts = {}
    for e in entries:
        counts[e["s"]] = counts.get(e["s"], 0) + 1
    return "\n".join([
        "【本地统计（口径＝本 skill 收录量）】",
        "· 《伤寒论》讲稿 {} 条".format(counts.get("shanghan", 0)),
        "· 《金匮要略》讲稿 {} 条".format(counts.get("jingui", 0)),
        "· 方剂库（含组成与主治）{} 首".format(len(load_formulas()[0])),
        "· 医案库 {} 例".format(len(load_cases())),
        "· 本次提问检索命中 {} 条，医案相关 {} 例".format(matched, n_cases),
    ])


def prepare(q):
    """一次提问的全部本地素材（llm_service.dart:303-414）。"""
    acupoints = list(retrieve_acupoints(q))
    is_acu = is_acupuncture_query(q)
    acu_hits = retrieve_acu_hits(q) if is_acu else []

    cases = retrieve_cases(q, MAX_CASE_CANDIDATES)
    if is_acu:
        jump_pts, jump_cases = jump_by_acupoints(q)
        for p in jump_pts:
            if len(acupoints) >= MAX_ACUPOINTS:
                break
            if not any(e["name"] == p["name"] for e in acupoints):
                acupoints.append(p)
        if jump_cases:
            merged = list(jump_cases)
            for c in cases:
                if len(merged) >= MAX_CASE_CANDIDATES:
                    break
                if not any(e["seq"] == c["seq"] for e in merged):
                    merged.append(c)
            cases = merged
    # 医案「针灸方案」反查穴位库（后补，顺序不可提前）
    for c in cases:
        if len(acupoints) >= MAX_ACUPOINTS:
            break
        acu = c.get("acupuncture") or ""
        if not acu:
            continue
        for p in retrieve_acupoints(acu, MAX_ACUPOINTS - len(acupoints)):
            if not any(e["name"] == p["name"] for e in acupoints):
                acupoints.append(p)

    aliases = match_aliases(q)
    priority = ([e["a"] for e in aliases if e.get("k") == "gujin"]
                + extract_formula_names(q)
                + symptom_terms(q)
                + [w for w in EXEMPT_TERMS if w in q])

    case_formulas = []
    for c in cases:
        for f in extract_formula_names(c["formula"]):
            if len(case_formulas) >= MAX_CASE_FORMULAS:
                break
            if f not in case_formulas:
                case_formulas.append(f)

    crossbook = crossbook_hits(q)

    # 二跳必须预留槽位，否则第一轮填满 8 条，二跳永远轮不上。
    # 按「每个方剂 1 条」预留，不是固定 3 条：只有 1 个方剂时固定留 3 会
    # 白白砍掉两个意图槽位（实测六症状查询的第 6 个症状被挤掉）。
    reserve = min(len(case_formulas), MAX_CASE_FORMULAS)
    res = retrieve_result(q, priority=priority, extra=expand_terms(aliases),
                          seed=outline_hits(q) + crossbook + list(acu_hits),
                          cap=MAX_HITS - reserve)
    if case_formulas:
        res = extend_by_formulas(res, case_formulas)

    formulas = []
    for h in res["hits"]:
        for f in extract_formula_names(h["snippet"]):
            if len(formulas) >= MAX_FORMULA_LIST:
                break
            if f not in formulas:
                formulas.append(f)

    by_name = load_formulas()[1]
    briefs = []
    for name in formulas:
        d = by_name.get(name)
        if not d:
            continue
        briefs.append({
            "name": d["name"],
            "caution": (d.get("contraindication") or "").strip(),
            "gist": (d.get("explanation") or "").strip(),
        })

    formula_hits = []
    for name in formulas[:MAX_FORMULA_HITS]:
        fh = formula_classic_hits(name)
        if fh:
            formula_hits.append(fh)

    return {
        "classics": res["hits"],
        "matched": res["total"],
        "formulas": formulas,
        "briefs": briefs,
        "formulaHits": formula_hits,
        "crossbook": crossbook,
        "cases": cases,
        "caseFormulas": case_formulas,
        "acupoints": acupoints,
        "diseases": aliases,
        "stats": stats_if_counting(q, res["total"], len(cases)),
        "emergency": is_emergency(q),
        "keywords": keywords_for(q),
    }


def _clip(s, n):
    t = (s or "").strip().replace("\n", " ")
    return t[:n] + ("…" if len(t) > n else "")


def build_context(r, question):
    """六块拼装（llm_service.dart:692-786），预算与截断规则同构。"""
    buf = []
    used = 0
    for h in r["classics"][:MAX_HITS]:
        body = (h["snippet"] or "")[:MAX_SNIPPET_CHARS]
        line = "【{}·{}】\n{}\n".format(h["label"], h["title"], body)
        if used + len(line) > MAX_CONTEXT_CHARS:
            break
        buf.append(line)
        used += len(line)
    excerpts = "\n".join(buf).strip()

    extra = []
    if r["acupoints"]:
        extra.append("【相关穴位（本地穴位库：定位 / 手法 / 禁忌）】")
        for p in r["acupoints"]:
            bits = []
            if p.get("location"):
                bits.append("定位：" + _clip(p["location"], 46))
            if p.get("needling"):
                bits.append("针刺：" + _clip(p["needling"], 40))
            if p.get("moxibustion"):
                bits.append("灸法：" + _clip(p["moxibustion"], 36))
            if p.get("clinicalNotes"):
                bits.append("主治：" + _clip(p["clinicalNotes"], 46))
            if p.get("contraindication"):
                bits.append("禁忌：" + _clip(p["contraindication"], 32))
            extra.append("· {}（{}）｜{}".format(
                p["name"], p.get("meridian", ""), "｜".join(bits)))
        extra.append("")
    if r["diseases"]:
        extra.append(disease_brief(r["diseases"]))
        extra.append("")
    if r["formulas"]:
        extra.append("【命中片段中出现的方剂】（从上述原文确定性抽取，可全部列出）")
        extra.append("、".join(r["formulas"][:MAX_FORMULA_LIST]))
        extra.append("")
    if r["briefs"]:
        # 标题必须保留「非讲稿原文」：二手整理数据，不标注会被当成倪师原话
        extra.append("【方剂库摘要】（本地结构化整理，非讲稿原文；用来讲「什么情况不能用」）")
        for b in r["briefs"]:
            parts = []
            if b["caution"]:
                parts.append("禁忌 " + _clip(b["caution"], 46))
            if b["gist"]:
                parts.append("要点 " + _clip(b["gist"], 40))
            if parts:
                extra.append("· {}：{}".format(b["name"], "｜".join(parts)))
        extra.append("")
    if r.get("formulaHits"):
        lines = ["【方剂见于经典（本地预索引；提及≠该方出处）】"]
        for h in r["formulaHits"][:MAX_FORMULA_HITS]:
            bits = []
            if h["shanghan"]:
                bits.append("伤寒·" + "、".join(
                    "宋本{}条".format(x["songben"]) for x in h["shanghan"]))
            if h["jingui"]:
                bits.append("金匮·" + "、".join(
                    _clip(x["title"], 18) for x in h["jingui"]))
            counts = h.get("lectureCounts") or {}
            if counts.get("bencao"):
                bits.append("本草讲稿{}处".format(counts["bencao"]))
            if counts.get("zhenjiu"):
                bits.append("针灸讲稿{}处".format(counts["zhenjiu"]))
            lines.append("· {}：{}".format(h["name"], "；".join(bits)))
        extra.append("\n".join(lines)[:MAX_FORMULA_HIT_BLOCK])
        extra.append("")
    if r.get("crossbook"):
        lines = ["【宋本跨书归属】宋本391-398正文收在金匮，不是伤寒未覆盖"]
        lines.extend("· 宋本{}条 → 金匮·{}".format(h["songben"], _clip(h["title"], 46))
                     for h in r["crossbook"])
        extra.append("\n".join(lines)[:MAX_FORMULA_HIT_BLOCK])
        extra.append("")
    if r["cases"]:
        extra.append("【倪师医案】（本地医案库，引用时写「医案 #序号」）")
        for c in r["cases"][:MAX_CASES]:
            bits = ["#{}".format(c["seq"]), "诊断：" + _clip(c["diagnosis"], 40)]
            if c["mechanism"]:
                bits.append("病机：" + _clip(c["mechanism"], 40))
            if c["formula"]:
                bits.append("方剂：" + _clip(c["formula"], 60))
            if c["acupuncture"]:
                bits.append("针灸：" + _clip(c["acupuncture"], 60))
            if c["result"]:
                bits.append("结果：" + _clip(c["result"], 40))
            extra.append("｜".join(bits))
        extra.append("")
    if r["stats"]:
        extra.append(r["stats"])
        extra.append("")

    parts = ["【讲义片段】\n" + (excerpts or "（本次检索没有命中讲义内容）")]
    extra_text = "\n".join(extra).strip()
    if extra_text:
        parts.append(extra_text[:MAX_EXTRA_CHARS])
    parts.append("【提问】\n" + question)
    body = "\n\n".join(parts)
    if r["emergency"]:
        # App 里由 UI 渲染加强版免责框；skill 环境改为文首提示，由模型带到回答开头
        body = "⚠️ 急症提示：以下内容仅供学术参考，请立即就医或拨打 120。\n\n" + body
    return body


# ---------------------------------------------------------------- CLI

def _selftest():
    """非平凡逻辑的最小可运行检查。"""
    # 确定性：等长元素必须保持输入顺序（否则 set 顺序漂移会让同一问题两次结果不同）
    assert ordered_by_len(["ab", "cd", "e"]) == ["ab", "cd", "e"], "等长元素须保持原序"
    assert ordered_by_len(["e", "ab", "cd", "ab"]) == ["ab", "cd", "e"], "须保序去重"

    assert keywords_for("桂枝汤证的辨证要点是什么")[0].startswith("桂枝"), "长词必须优先"
    assert "方剂" not in keywords_for("有哪些方剂"), "领域泛词必须被过滤"
    assert "中焦" in keywords_for("中焦虚寒"), "功能字不得切碎中焦/心下/上气"

    total, hits = search("桂枝汤", SNIPPET_SPAN, 3)
    assert total > 100 and len(hits) == 3, "桂枝汤应大量命中"
    assert search("桂枝汤证的辨证要点是什么？", SNIPPET_SPAN, 5)[0] == 0, \
        "整句必须 0 命中，这是切词存在的原因"

    cases = load_cases()
    assert 1000 < len(cases) < 1300, "医案解析例数异常：{}".format(len(cases))
    assert all(c["formula"] for c in cases), "医案必须有方剂列"

    r = prepare("糖尿病有哪些方剂")
    assert r["classics"], "糖尿病应命中文"
    assert r["diseases"], "病名对照应命中"
    assert r["caseFormulas"] or r["cases"], "医案或二跳方剂至少有一项"
    ctx = build_context(r, "糖尿病有哪些方剂")
    assert "【讲义片段】" in ctx and "【提问】" in ctx

    r2 = prepare("足三里主治什么")
    assert r2["acupoints"] and r2["acupoints"][0]["name"].startswith("足三里"), "穴位点名必须命中"
    assert is_acupuncture_query("足三里主治什么"), "无针/灸字也须判为针灸提问"

    # 口语症状 → 古病名：「大便不成形」在讲义里写作「自利益甚」，不对照则只能命中便秘条文
    r3 = prepare("大便不成形")
    assert "太阴" in r3["classics"][0]["title"], \
        "大便不成形应命中太阴提纲，实际：{}".format(r3["classics"][0]["title"][:30])

    # 自由率：真词两侧多是标点，滑窗拼接词永远黏在邻字上
    assert free_ratio("腰痛") > 0.6, "腰痛应判为自由词"
    assert free_ratio("痛扎") < 0.1, "痛扎是「腹痛扎右脚」的拼接，必须判假"
    assert free_ratio("来就") < 0.1, "来就是最常见拼接 bigram，必须判假"

    # 拼接词不得进意图槽位：「腰痛扎哪个穴」首条必须是含腰痛的条辨，
    # 不能是「痛扎」撞上的麻黄升麻汤条（总=12，稀有度序会把它排第一）。
    r4 = prepare("腰痛扎哪个穴")
    assert "腰痛" in r4["classics"][0]["title"], \
        "首条须含腰痛，实际：{}".format(r4["classics"][0]["title"][:30])

    # 多意图：六症状各留一个代表，不能被稀有度最高的那一个吃满槽位
    r5 = prepare("头晕乏力失眠口苦大便干小便黄")
    blob = " ".join(h["title"] + h["snippet"] for h in r5["classics"])
    for w in ["头晕", "乏力", "失眠", "口苦", "大便", "小便"]:
        assert w in blob, "多症状查询缺代表：{}".format(w)

    # 出处审计：检索块内的方名不报，块外的方名要挑出
    ra = prepare("白虎汤证")
    assert "白虎汤" in ra["formulas"], "审计样本须含白虎汤"
    assert "白虎汤" not in unverified_formulas("用白虎汤即可", ra), "有据方名不得误报"
    assert "一物瓜蒂汤" in unverified_formulas("再用一物瓜蒂汤", ra), "无据方名须挑出"

    # P0：方剂→经典反查（旁路，不改 classics 排名）
    fi = load_formula_index()
    assert len(fi) == 278 and "_v" not in fi, "方剂索引须跳过版本键"
    fh = formula_classic_hits("桂枝汤")
    assert fh and fh["shanghan"] and fh["jingui"], "桂枝汤应有伤寒/金匮命中"
    assert all(x["songben"] > 0 for x in fh["shanghan"]), "伤寒须输出宋本条号"
    rc = prepare("桂枝汤")
    ctx = build_context(rc, "桂枝汤")
    assert "【方剂见于经典" in ctx and "assets/" not in ctx, "反查块不得输出 asset"

    # P1：宋本391-398跨书重定向（标题锚点须唯一）
    for n, anchor in SONGBEN_CROSSBOOK.items():
        hits = [e for e in load_index()
                if e["s"] == "jingui" and anchor in e["t"]]
        assert len(hits) == 1, "宋本{}锚点不唯一".format(n)
    cb = prepare("宋本398条")
    assert any(h.get("songben") == 398 for h in cb["crossbook"]), "398须重定向金匮"
    cb_ctx = build_context(cb, "宋本398条")
    assert "【宋本跨书归属】" in cb_ctx and "assets/" not in cb_ctx

    print("selftest OK：切词/检索/医案/穴位/二跳/自由率/多意图/审计/方剂反查/跨书 全部通过")


def main(argv):
    args = [a for a in argv[1:] if not a.startswith("--")]
    flags = {a for a in argv[1:] if a.startswith("--")}
    if "--selftest" in flags:
        _selftest()
        return 0
    if not args:
        print(__doc__.strip())
        return 2
    q = " ".join(args)
    r = prepare(q)
    print(build_context(r, q))
    if "--json" in flags:
        slim = dict(r)
        slim.pop("classics", None)
        slim["classics"] = [{"source": h["source"], "title": h["title"]} for h in r["classics"]]
        slim["cases"] = [{"seq": c["seq"], "diagnosis": c["diagnosis"]} for c in r["cases"]]
        slim["acupoints"] = [p["name"] for p in r["acupoints"]]
        slim["diseases"] = [e["a"] for e in r["diseases"]]
        print("\n---JSON---")
        print(json.dumps(slim, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
