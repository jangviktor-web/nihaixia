#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Holdout：验证 free_ratio 阈值（total>=3 且 free>=0.5）不是对 41 条调试集的拟合。

⛔ 冻结纪律：本文件的 want / real / junk 三项**在看到任何运行结果之前**写定。
   跑出来的任何数字都不得反过来改阈值、改过滤层、改本文件的判据。
   要改，先另开一次改动，并说明依据不是本文件。

判据（三条互相独立）：
  hit  = want 里任一期望片段出现在前 8 条的标题+片段里
  miss = real 里的真词被过滤层剔除（误杀）——注意 real 若语料根本没这个词，
         免费率 0 被剔是**正确行为**，报告里单列为「语料缺词」而非误杀
  leak = junk 里的预判拼接词通过了过滤层（漏杀），进了意图槽位

用法：python scripts/test_holdout.py [-v]

实测记录（2026-11-16，13 条合并只跑一次）：**10/13 (77%)**。
失败 3 条，归因分开记，不要混：
  · 「左边肚子疼扎右边脚」= free_ratio 边界问题。左边(.400)/肚子(.421)/右边(.452)
    三个真词都卡在 .5 下方被误杀（口语叙述段里它们几乎总黏着邻字），剩下
    「扎右边」(.714) 这个非核心短语独占槽位，把首条带到针灸章。⛔ 不许调
    FREE_MIN、不许加 holdout 专属白名单来救它；机制修复方案另案审。
  · 「咳嗽有黄痰喉咙痛」= 别名缺口。喉咙痛未映射到咽痛/喉痹（喉咙干 已映射，
    痛 没映射），所以咽痛条进不了 priority 档；另有拼接词「咙痛」漏杀。
  · 「月经来之前乳房胀痛」= 别名缺口 + 误杀。月经/乳房 两个真词被 free_ratio
    剔除，且未映射到经水/月事/乳胀。
  ⚠️ 补这两类别名前要先定「别名表边界」，别顺着 holdout 一条条补——那就是调参。
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import nishi_retrieve as n

# want=期望在前 8 条里出现的片段（任一）
# real=口语真词，应通过 free_ratio 过滤
# junk=预判的滑窗拼接词，应被 free_ratio 剔除
HOLDOUT = [
    dict(q="左边肚子疼扎右边脚",
         want=["以右治左", "以左治右", "缪刺", "巨刺", "腹痛"],
         real=["左边", "肚子", "右边", "脚"],
         junk=["边肚", "子疼", "疼扎", "扎右", "边脚"]),
    dict(q="一吹风就打喷嚏流清涕",
         want=["清涕", "嚏", "太阳", "桂枝"],
         real=["吹风", "喷嚏", "清涕"],
         junk=["风就", "就打", "吹风就", "嚏流", "喷嚏流"]),
    dict(q="晚上手心脚心发热睡不着",
         want=["手足心热", "五心", "虚烦不得眠", "阴虚", "发热"],
         real=["晚上", "手心", "脚心", "发热", "睡不着"],
         junk=["上手", "心脚", "心发", "热睡", "脚心发"]),
    dict(q="吃完东西就胀还打嗝",
         want=["心下痞", "噫气", "嗳气", "胀满", "旋覆"],
         real=["吃完", "东西", "打嗝"],
         junk=["完东", "西就", "就胀", "胀还", "还打", "就打"]),
    dict(q="早上起来嘴苦喉咙干",
         want=["口苦", "咽干"],
         real=["早上", "嘴苦", "喉咙"],
         junk=["上起", "来嘴", "嘴苦", "苦喉", "喉咙干"]),
    dict(q="腰酸腿软还怕冷",
         want=["腰痛", "四肢厥逆", "虚劳", "肾气丸"],
         real=["腰酸", "腿软", "怕冷"],
         junk=["酸腿", "软还", "腿软", "腰酸腿"]),
    dict(q="大便干小便黄口苦",
         want=["不大便", "大便", "小便", "口苦"],
         real=["大便干", "小便黄", "口苦"],
         junk=["便干", "干小", "便黄", "干小便"]),
    dict(q="咳出来的痰是黄的",
         want=["肺痿", "痰", "黄芩", "热"],
         real=["咳出", "痰"],
         junk=["出来", "来的", "的痰", "痰是", "是黄", "黄的"]),

    # ---- 第二批（2026-11-16 追加，与第一批合并后只跑这一次）----
    # 判据同样先写定再跑；want 只保留 ≥2 字的专有片段，避免「痰」「淋」这种单字
    # 随便一条就蹭中（第一批在这点上有水分，已在报告里说明）。
    dict(q="咳嗽有黄痰喉咙痛",
         want=["咽痛", "咽中痛", "肺痿", "桔梗"],
         real=["咳嗽", "黄痰", "喉咙痛"],
         junk=["嗽有", "有黄", "黄痰喉", "痰喉", "咙痛"]),
    dict(q="吃完饭胃里反酸烧心",
         want=["吞酸", "吐酸", "心中疼热", "嘈杂"],
         real=["反酸", "烧心", "吃饭"],
         junk=["完饭", "饭胃", "胃里反", "里反酸", "酸烧"]),
    dict(q="小便刺痛尿不干净",
         want=["小便不利", "石淋", "膏淋", "癃闭", "淋秘"],
         real=["小便", "刺痛", "尿"],
         junk=["便刺", "刺痛尿", "痛尿", "尿不干", "不干净"]),
    dict(q="早上起来眼皮肿脸也肿",
         want=["水肿", "水气", "风水", "目窠"],
         real=["眼皮", "脸", "早上"],
         junk=["上起", "来眼", "皮肿", "肿脸", "脸也肿"]),
    dict(q="月经来之前乳房胀痛",
         want=["经水", "经行", "月事", "乳胀"],
         real=["月经", "乳房", "胀痛"],
         junk=["经来", "来之", "之前乳", "前乳", "房胀"]),
]


def probe(q):
    """复算过滤层的实际判定，字段全部来自被测模块本身。"""
    rows = []
    for w in n.keywords_for(q):
        total, _ = n.search(w, n.SNIPPET_SPAN, n.MAX_HITS)
        if not total:
            continue
        fr = n.free_ratio(w)
        keep = total >= 3 and fr >= n.FREE_MIN
        rows.append(dict(w=w, total=total, free=fr, keep=keep))
    return rows


def main(verbose=False):
    ok = 0
    for c in HOLDOUT:
        q = c["q"]
        r = n.prepare(q)
        blob = " ".join(h["title"] + (h["snippet"] or "") for h in r["classics"])
        hit = any(w in blob for w in c["want"])
        ok += hit

        rows = probe(q)
        kept = [x["w"] for x in rows if x["keep"]]
        dropped = [x["w"] for x in rows if not x["keep"]]
        leak = [w for w in c["junk"] if w in kept]
        miss = [w for w in c["real"] if w in dropped]

        print(f"\n{'✓' if hit else '✗'} {q}")
        print(f"   前8条: {len(r['classics'])} | 匹配位={r['matched']} | "
              f"意图组={len(kept)} | 首条={r['classics'][0]['title'][:34] if r['classics'] else '（空）'}")
        print(f"   保留词: {kept}")
        print(f"   剔除词({len(dropped)}): {dropped}")
        if leak:
            print(f"   ⚠ 漏杀(拼接词通过): {leak}")
        if miss:
            print(f"   ⚠ 误杀(真词被剔): {miss}")
        if verbose or not hit:
            for i, h in enumerate(r["classics"][:3], 1):
                print(f"     {i}. [{h['label']}] {h['title'][:52]}")

    total = len(HOLDOUT)
    print(f"\n{'='*66}")
    print(f"holdout 命中 {ok}/{total} ({ok/total:.0%})")
    return ok, total


if __name__ == "__main__":
    main("-v" in sys.argv[1:])
