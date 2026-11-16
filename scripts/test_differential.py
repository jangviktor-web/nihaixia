#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""辨证检索回归测试：跑一批真实提问，看关键条文有没有进前 8 条。

用法：
    python scripts/test_differential.py          # 汇总
    python scripts/test_differential.py -v       # 逐条明细

评分口径：
  rank = 期望片段首次出现的名次（1-based）；0 = 前 8 条都没有
  second = 鉴别类用例的第二方/第二证是否也进了前 8
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import nishi_retrieve as n

# q=提问, want=应命中的片段(任一), second=鉴别类第二项, kind=分类
CASES = [
    # A 六经提纲：最基础的命中
    dict(kind="A 提纲", q="太阳病", want=["头项强痛"]),
    dict(kind="A 提纲", q="阳明病", want=["胃家实"]),
    dict(kind="A 提纲", q="少阳病", want=["口苦", "咽干", "目眩"]),
    dict(kind="A 提纲", q="太阴病", want=["腹满而吐", "自利益甚"]),
    dict(kind="A 提纲", q="少阴病", want=["脉微细", "但欲寐"]),
    dict(kind="A 提纲", q="厥阴病", want=["气上撞心", "消渴"]),

    # B 方证识别：给症状，看能否导出方
    dict(kind="B 方证", q="项背强几几，无汗恶风", want=["项背强"], formula="葛根汤"),
    dict(kind="B 方证", q="往来寒热，胸胁苦满，默默不欲饮食",
         want=["胸胁苦满"], formula="小柴胡汤"),
    dict(kind="B 方证", q="心下痞硬，噫气不除", want=["噫气不除"], formula="旋覆代赭汤"),
    dict(kind="B 方证", q="下利清谷，手足厥冷，脉微欲绝", want=["下利清谷"], formula="四逆汤"),
    dict(kind="B 方证", q="心中烦，不得卧", want=["不得卧", "心中烦"], formula="黄连阿胶汤"),
    dict(kind="B 方证", q="干呕发热而咳，心下有水气", want=["心下有水气"], formula="小青龙汤"),

    # C 鉴别类：两方都要拿到，否则只能答一半。
    # 判据（2026-11-16 定）：**两方均在前 3 即可，不要求 want 指定的那一方在第 1**。
    # 原因：_fill_rounds 在 priority 档内按 total 升序排，稀有方先占首槽，所以
    # 「常见方 vs 少用方」的鉴别题里常见方稳定落第 2（桂枝汤/麻黄汤即如此）。
    # 这是有意的设计（先暴露较稀有的那一方，避免常见方吃满槽位），不是回退；
    # 实测 7 组鉴别对双向、前 8 条序列逐字一致，与提问里的方名顺序无关。
    dict(kind="C 鉴别", q="桂枝汤和麻黄汤有什么区别",
         want=["桂枝汤"], second="麻黄", formula="桂枝汤"),
    dict(kind="C 鉴别", q="四逆汤和理中汤怎么分",
         want=["四逆"], second="理中", formula="四逆汤"),
    dict(kind="C 鉴别", q="真寒假热怎么辨", want=["真寒假热", "热"], second="寒"),
    dict(kind="C 鉴别", q="大青龙汤和小青龙汤区别",
         want=["大青龙"], second="小青龙", formula="大青龙汤"),

    # D 口语症状：讲稿写古名，患者说白话
    dict(kind="D 口语", q="大便不成形", want=["自利益甚", "太阴"]),
    dict(kind="D 口语", q="头晕目眩，耳鸣", want=["眩", "耳鸣"]),
    dict(kind="D 口语", q="咳嗽有白色的痰", want=["咳", "痰"]),
    dict(kind="D 口语", q="腰酸腿软", want=["腰", "酸"]),
    dict(kind="D 口语", q="半夜三四点醒来就睡不着", want=["不得眠", "失眠", "丑时", "一点", "三点"]),
    dict(kind="D 口语", q="口苦口干想喝水", want=["口苦", "咽干", "口渴"]),
    dict(kind="D 口语", q="身上一阵冷一阵热", want=["往来寒热"]),
    dict(kind="D 口语", q="吃完东西就胃胀", want=["心下痞", "腹满"]),
    dict(kind="D 口语", q="手脚发麻", want=["手足", "麻"]),

    # E 否定/排除语义：检索不理解「没有」「不」
    dict(kind="E 否定", q="没有发烧但是怕冷", want=["恶寒", "但欲寐"]),
    dict(kind="E 否定", q="不渴，小便清", want=["小便清", "不渴"]),
    dict(kind="E 否定", q="大便不通但不是热证", want=["不大便", "寒"]),

    # F 寒热错杂
    dict(kind="F 错杂", q="上热下寒", want=["上热下寒", "寒热"]),
    dict(kind="F 错杂", q="手脚冰冷但脸上长痘", want=["厥", "寒"], second="热"),
    dict(kind="F 错杂", q="口干但不想喝水", want=["口干", "不渴"]),

    # G 误治变证
    dict(kind="G 变证", q="吃错药拉肚子更厉害了", want=["利", "下"]),
    dict(kind="G 变证", q="发汗太多汗止不住", want=["汗", "漏"]),

    # H 针灸
    dict(kind="H 针灸", q="失眠扎什么穴", want=["失眠", "不寐"], acu="失眠"),
    dict(kind="H 针灸", q="腰痛扎哪个穴", want=["腰痛"], acu="腰"),
    dict(kind="H 针灸", q="胃痛针哪里", want=["胃"], acu="胃"),
    dict(kind="H 针灸", q="足三里主治什么", want=["足三里"], acu="足三里"),

    # I 列举/计数
    dict(kind="I 列举", q="太阳病有哪些方剂", want=["太阳"], formula=None),
    dict(kind="I 列举", q="伤寒论有多少条", want=[], stats=True),

    # J 边界
    dict(kind="J 边界", q="桂枝汤", want=["桂枝汤"], formula="桂枝汤"),
    dict(kind="J 边界", q="中医怎么看待疫苗", want=["疫苗", "疫"]),

    # K 多症状：口语堆叠六症。判据（2026-11-16 由产品侧裁定，方案 A）：
    # **cov 里每个症状在前 8 条各有一条代表**，不要求 top3 里出现「一条同时讲
    # 多症状」的条文。另加独立断言「首条必须命中主诉」（见 complaint_alts）。
    #
    # 语料事实（复现查询：对 load_index() 1728 条取 body=标题+正文，数每组同义词
    # 命中几个症状组）：
    #
    #   口径                    ≥2    ≥3    ≥4    ≥5   6 全中
    #   口语原文（原字面）        18     4     2     1      0
    #   古名同义（宽，含「冒」）   142    52    19     9      2
    #   古名同义（收紧，去「冒」） 109    47    17     9      2
    #
    # 收紧口径按来源拆（关键结论）：
    #   含 ≥6：2 条   {zhenjiu:1, guji:1}        ← 都是「足太阳膀胱经」章级条目
    #   含 ≥5：9 条   {neijing:1, zhenjiu:5, guji:3}
    #   含 ≥4：17 条  {neijing:2, zhenjiu:8, guji:7}   ← 伤寒 0 条 / 金匮 0 条
    #   含 ≥3：47 条  {shanghan:4, jingui:4, neijing:10, zhenjiu:13, bencao:3, guji:13}
    #
    # 为什么 ≥4 的 17 条不能当「多症状条文」用——条目粒度不同：
    #   伤寒论讲稿 394 条 / 正文中位 567 字；金匮要略讲稿 433 条 / 821 字（条级）
    #   内经讲稿    73 条 / 8373 字；针灸讲稿 72 条 / 最长 56559 字（整篇整章一条）
    # 即：整章「提到过」六个症状对辨证没有信息量。条级的伤寒/金匮里，覆盖 4 个
    # 及以上症状的条文是 0 条，覆盖 3 个的只有 8 条。
    #
    # 被否掉的方案 B1（top3 内必须出现一条覆盖 ≥3 症状的条文）：实测那 8 条候选
    # 全部进不了前 8，需要二阶段「按症状覆盖数 rerank」+ 症状归一，且实测覆盖率
    # 加权排序会让单症状场景退化（「大便不成形」滑到「第四章·任脉经穴」）。
    # ⚠️ 若将来内经/针灸改为条级切分，≥4 的候选池会变大，届时可重新评估 B1。
    dict(kind="K 多症", q="头晕乏力失眠口苦大便干小便黄",
         want=["头晕", "乏力", "口苦", "大便", "小便"],
         cov=["头晕", "乏力", "失眠", "口苦", "大便", "小便"],
         # 主诉=提问中位置最靠前的真词，本例为「头晕」；断言允许同义写法
         complaint_alts={"头晕": ["头晕", "眩", "晕"]}),
]


def complaint_of(q):
    """主诉 = 提问中位置最靠前的真词（先过 total≥3 与 free_ratio≥FREE_MIN 两道筛）。"""
    terms = []
    for w in n.keywords_for(q):
        total, _ = n.search(w, n.SNIPPET_SPAN, n.MAX_HITS)
        if total >= 3 and n.free_ratio(w) >= n.FREE_MIN:
            terms.append(w)
    return n.main_complaint(q, terms)


def run(verbose=False):
    rows = []
    for c in CASES:
        r = n.prepare(c["q"])
        titles = [(h["title"] or "") + (h["snippet"] or "") for h in r["classics"]]

        rank, seen = 0, None
        for i, t in enumerate(titles):
            if any(w in t for w in c["want"]):
                rank, seen = i + 1, next(w for w in c["want"] if w in t)
                break
        # want 为空 = 只检查块是否产出（如统计）
        ok = bool(rank) or (not c["want"])

        second_ok = None
        if c.get("second"):
            second_ok = any(c["second"] in t for t in titles)

        formula_ok = None
        if c.get("formula"):
            formula_ok = c["formula"] in r["formulas"] or any(
                c["formula"] in (b["name"] or "") for b in r["briefs"])

        acu_ok = None
        if c.get("acu"):
            acu_ok = any(c["acu"] in p["name"] or c["acu"] in (p.get("clinicalNotes") or "")
                         for p in r["acupoints"])

        stats_ok = None
        if c.get("stats"):
            stats_ok = "【本地统计" in n.build_context(r, c["q"])

        # cov：多症状用例，要求每个症状在前 8 条里各有代表
        cov_ok, cov_miss = None, []
        if c.get("cov"):
            blob = " ".join(titles)
            cov_miss = [w for w in c["cov"] if w not in blob]
            cov_ok = not cov_miss

        # 首条主诉：独立断言，防止「8 条各沾一个症状、没有一条落在主诉上」
        mc, mc_ok = None, None
        if c.get("cov"):
            mc = complaint_of(c["q"])
            alts = (c.get("complaint_alts") or {}).get(mc, [mc]) if mc else []
            head = titles[0] if titles else ""
            mc_ok = bool(alts) and any(a in head for a in alts)

        rows.append(dict(c=c, rank=rank, seen=seen, ok=ok, second=second_ok,
                         formula=formula_ok, acu=acu_ok, stats=stats_ok,
                         cov=cov_ok, cov_miss=cov_miss,
                         complaint=mc, complaint_ok=mc_ok,
                         n_hits=len(r["classics"]), top=titles[:3],
                         formulas=r["formulas"],
                         acupoints=[p["name"] for p in r["acupoints"]]))
        if verbose:
            flag = "✓" if ok else "✗"
            print(f"{flag} [{c['kind']}] {c['q'][:22]:24s} rank={rank} hit={seen}")
            if not ok:
                for t in titles[:3]:
                    print("      ", t[:58])
    return rows


def write_snapshot(rows, path):
    import json
    data = [dict(
        kind=r["c"]["kind"], q=r["c"]["q"], want=r["c"]["want"],
        rank=r["rank"], ok=r["ok"], second=r["second"],
        formula=r["formula"], acu=r["acu"], stats=r["stats"],
        top=r["top"], formulas=r["formulas"], acupoints=r["acupoints"],
    ) for r in rows]
    Path(path).write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"snapshot → {path}（{len(data)} 条）")


def diff_snapshot(base_path, rows):
    import json
    base = {d["q"]: d for d in json.loads(Path(base_path).read_text(encoding="utf-8"))}
    print(f"\n{'='*66}\n逐项 diff（基线 {base_path}）")
    moved = 0
    for r in rows:
        q = r["c"]["q"]
        b = base.get(q)
        if not b:
            print(f"[新增] {q}")
            continue
        deltas = []
        if b["rank"] != r["rank"]:
            deltas.append(f"rank {b['rank']}→{r['rank']}")
        if b["ok"] != r["ok"]:
            deltas.append(f"{'命中' if b['ok'] else '未命中'}→{'命中' if r['ok'] else '未命中'}")
        if b["second"] != r["second"]:
            deltas.append(f"second {b['second']}→{r['second']}")
        if b["formula"] != r["formula"]:
            deltas.append(f"formula {b['formula']}→{r['formula']}")
        if b["acu"] != r["acu"]:
            deltas.append(f"acu {b['acu']}→{r['acu']}")
        if b["top"][:1] != r["top"][:1]:
            moved += 1
            deltas.append(f"首条变更: {b['top'][0][:26]!r} → {r['top'][0][:26]!r}")
        if deltas:
            print(f"[{'!' if b['ok'] and not r['ok'] else ' '}] {r['c']['kind']} {q[:20]}")
            for d in deltas:
                print(f"      {d}")
    print(f"\n首条变更的用例数: {moved}/{len(rows)}")



def report(rows):
    total = len(rows)
    hit = sum(1 for r in rows if r["ok"])
    top1 = sum(1 for r in rows if r["rank"] == 1)
    top3 = sum(1 for r in rows if 0 < r["rank"] <= 3)
    print(f"\n{'='*66}")
    print(f"总计 {total} 条 | 前8命中 {hit} ({hit/total:.0%}) | 第1名 {top1} | 前3名 {top3}")

    second = [r for r in rows if r["second"] is not None]
    if second:
        s_ok = sum(1 for r in second if r["second"])
        print(f"鉴别类第二项进前8: {s_ok}/{len(second)}")
    fm = [r for r in rows if r["formula"] is not None]
    if fm:
        f_ok = sum(1 for r in fm if r["formula"])
        print(f"期望方剂命中: {f_ok}/{len(fm)}")
    ac = [r for r in rows if r["acu"] is not None]
    if ac:
        a_ok = sum(1 for r in ac if r["acu"])
        print(f"穴位块给出相关穴: {a_ok}/{len(ac)}")
    cv = [r for r in rows if r["cov"] is not None]
    for r in cv:
        n_cov = len(r["c"]["cov"]) - len(r["cov_miss"])
        flag = "✓" if r["cov"] else "✗"
        print(f"多症状覆盖 {flag} {r['c']['q']}: {n_cov}/{len(r['c']['cov'])}"
              + (f"  缺={r['cov_miss']}" if r["cov_miss"] else ""))
        print(f"首条主诉 {'✓' if r['complaint_ok'] else '✗'} 主诉={r['complaint']}"
              f" | 首条={r['top'][0][:44] if r['top'] else '（空）'}")

    print("\n--- 未命中明细 ---")
    for r in rows:
        if not r["ok"]:
            print(f"[{r['c']['kind']}] {r['c']['q']}  期望={r['c']['want']}")
            for t in r["top"]:
                print("    实际:", t[:56])

    print("\n--- 鉴别类未拿全 ---")
    for r in rows:
        if r["second"] is False:
            print(f"[{r['c']['kind']}] {r['c']['q']}  缺={r['c']['second']}")

    print("\n--- 按分类命中率 ---")
    kinds = {}
    for r in rows:
        k = r["c"]["kind"]
        a, b = kinds.get(k, (0, 0))
        kinds[k] = (a + (1 if r["ok"] else 0), b + 1)
    for k in sorted(kinds):
        a, b = kinds[k]
        print(f"  {k}: {a}/{b}")


if __name__ == "__main__":
    args = sys.argv[1:]
    rows = run("-v" in args)
    if "--snapshot" in args:
        write_snapshot(rows, args[args.index("--snapshot") + 1])
    if "--diff" in args:
        diff_snapshot(args[args.index("--diff") + 1], rows)
    report(rows)
    # 硬门禁：多症状用例的首条必须落在主诉上（回填 1 断言）
    gate = [r for r in rows if r["complaint_ok"] is False]
    if gate:
        print(f"\n❌ 首条未命中主诉：{[r['c']['q'] for r in gate]}")
        sys.exit(1)
