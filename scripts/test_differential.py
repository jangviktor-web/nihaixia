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

    # C 鉴别类：两方都要拿到，否则只能答一半
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
]


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

        rows.append(dict(c=c, rank=rank, seen=seen, ok=ok, second=second_ok,
                         formula=formula_ok, acu=acu_ok, stats=stats_ok,
                         n_hits=len(r["classics"]), top=titles[:3]))
        if verbose:
            flag = "✓" if ok else "✗"
            print(f"{flag} [{c['kind']}] {c['q'][:22]:24s} rank={rank} hit={seen}")
            if not ok:
                for t in titles[:3]:
                    print("      ", t[:58])
    return rows


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
    report(run("-v" in sys.argv))
