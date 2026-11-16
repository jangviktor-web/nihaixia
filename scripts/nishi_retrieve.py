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


def load_acupoints():
    if "acu" not in _CACHE:
        items = _json("acupoints.json")["acupoints"]
        # 正名带「穴」（足三里穴），提问与医案多写短名（足三里）→ 两形态都要进候选。
        # ponytail: 未复刻 App 的 kShortNameLinkForm 避撞表；撞普通词最多多给一条穴位资料。
        by_name, names = {}, set()
        for p in items:
            full = p["name"]
            by_name[full] = p
            names.add(full)
            short = full.replace("穴", "")
            if len(short) >= 2:
                by_name.setdefault(short, p)
                names.add(short)
        _CACHE["acu"] = (items, by_name, sorted(names, key=len, reverse=True))
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
    """2–4 字连续片段，功能字过滤，长词优先，上限 32（llm_service.dart:199-209）。"""
    clean = re.sub(r"[^\u4e00-\u9fffA-Za-z0-9]", "", q)
    words, seen = [], set()
    for ln in range(4, 1, -1):
        for i in range(len(clean) - ln + 1):
            w = clean[i:i + ln]
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
    for name in sorted(set(candidates), key=len, reverse=True):
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


def retrieve_result(q, priority=(), extra=(), seed=(), cap=MAX_HITS):
    """三阶检索（llm_service.dart:222-296）。"""
    total, direct = search(q, SNIPPET_SPAN, cap)
    if direct and not priority and not extra and not seed:
        return {"total": total, "hits": direct}

    pool = {}
    for h in list(seed) + list(direct):
        if len(pool) >= cap:
            break
        pool.setdefault(_key(h), h)
    best_total = total

    def sweep(w, cap_, per_word=0):
        nonlocal best_total
        r_total, hits = search(w, SNIPPET_SPAN, per_word if per_word > 0 else cap_)
        if r_total == 0:
            return
        if r_total > best_total:
            best_total = r_total
        take = 0
        for h in hits:
            if len(pool) >= cap:
                break
            if per_word > 0 and take >= per_word:
                break
            before = len(pool)
            pool.setdefault(_key(h), h)
            if len(pool) > before:
                take += 1

    # ① 已知术语（古病名 / 方名）优先，留 2 条给用户原话
    if priority:
        pcap = max(1, min(cap - 2, cap))
        for w in priority:
            if len(pool) >= pcap:
                break
            sweep(w, pcap)
    # ② 首个命中的词才允许填满，其后每词最多 2 条
    first_hit = True
    for w in keywords_for(q):
        if len(pool) >= cap:
            break
        before = len(pool)
        sweep(w, cap, 0 if first_hit else 2)
        if len(pool) > before:
            first_hit = False
    # ③ 病名对照的补充叫法，一律每词 2 条
    for w in extra:
        if len(pool) >= cap:
            break
        sweep(w, cap, 2)
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
    priority = [e["a"] for e in aliases if e.get("k") == "gujin"] + extract_formula_names(q)

    case_formulas = []
    for c in cases:
        for f in extract_formula_names(c["formula"]):
            if len(case_formulas) >= MAX_CASE_FORMULAS:
                break
            if f not in case_formulas:
                case_formulas.append(f)

    # 二跳必须预留槽位，否则第一轮填满 8 条，二跳永远轮不上
    reserve = MAX_CASE_FORMULAS if case_formulas else 0
    res = retrieve_result(q, priority=priority, extra=expand_terms(aliases),
                          seed=acu_hits, cap=MAX_HITS - reserve)
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

    return {
        "classics": res["hits"],
        "matched": res["total"],
        "formulas": formulas,
        "briefs": briefs,
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

    print("selftest OK：切词/检索/医案/穴位/二跳 全部通过")


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
