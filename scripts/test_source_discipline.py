#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""考据陷阱：只判「回答有没有把后世概念归给《伤寒论》」，与检索解耦。

⛔ 这不是模型正确率评测。回答样本是人工构造的正反例，验证 check() 这个判据
   能否区分合规/违规；真实模型输出另开评测脚本，直接复用 check() 即可。

题 4 的原始输入输出不在仓库，此处按用户诊断描述重建：模型把《温病条辨》
的「白虎四大症」当成《伤寒论》白虎汤证背书。判据须把这句判为违规。

用法：python scripts/test_source_discipline.py [-v]
"""

import re
import sys

# 后世/归纳概念：讲稿原文不这么归纳，归给《伤寒论》即出处错配
LATER_CONCEPTS = (
    "四大症", "四大证", "酸甘化阴", "卫气营血", "三焦辨证", "气血辨证",
)
# 归属表述：把概念挂到伤寒论或倪师原话上
ATTRIBUTION = ("伤寒论", "伤寒", "倪师讲", "倪师说", "原文说", "讲稿里")
# 显式标后世来源，或明确否认归属 → 合规
EXEMPT = ("温病条辨", "后世", "吴鞠通", "叶天士", "不是伤寒", "非伤寒", "不同于伤寒")

_SENT = re.compile(r"[。！？\n；;]")


def check(answer):
    """返回违规句列表；空列表＝合规。按句判，不做跨句推断。"""
    bad = []
    for sent in _SENT.split(answer or ""):
        s = sent.strip()
        if not s:
            continue
        if (any(c in s for c in LATER_CONCEPTS)
                and any(a in s for a in ATTRIBUTION)
                and not any(e in s for e in EXEMPT)):
            bad.append(s)
    return bad


# expect_bad=True 表示这段回答应被判违规
CASES = [
    dict(name="题4·白虎四大症归伤寒", expect_bad=True,
         answer=" 《伤寒论》白虎汤证的四大症是大热、大汗、大渴、脉洪大。"),
    dict(name="白虎·显式分源", expect_bad=False,
         answer=" 《伤寒论》白虎汤证见大汗出、大烦渴、脉洪大。《温病条辨》另立四大症，两者不同。"),
    dict(name="桂枝汤解肌·有原文", expect_bad=False,
         answer=" 《伤寒论》原文说桂枝汤本为解肌，脉浮紧汗不出者不可与。"),
    dict(name="桂枝汤·混入四大症", expect_bad=True,
         answer=" 桂枝汤解肌之外，《伤寒论》讲四大症是其辨证要点。"),
    dict(name="小柴胡七或然证·原文有", expect_bad=False,
         answer=" 《伤寒论》小柴胡汤条文列七个或然证，见往来寒热胸胁苦满。"),
    dict(name="酸甘化阴·归伤寒", expect_bad=True,
         answer=" 《伤寒论》芍药甘草汤酸甘化阴、缓急止痛，服后脚伸可弃杖。"),
    dict(name="酸甘化阴·标后世", expect_bad=False,
         answer=" 芍药甘草汤服后其脚即伸，这是《伤寒论》原文。酸甘化阴是后世医家的概括，不是倪师原话。"),
    dict(name="卫气营血·归伤寒", expect_bad=True,
         answer=" 《伤寒论》温病用卫气营血辨证，与六经并行。"),
    dict(name="卫气营血·标温病条辨", expect_bad=False,
         answer=" 《温病条辨》讲卫气营血辨证，《伤寒论》讲六经，这是两套体系。"),
    dict(name="混合·双重错配", expect_bad=True,
         answer=" 倪师讲白虎四大症，又讲卫气营血辨证，都是《伤寒论》的精髓。"),
]


def main(verbose=False):
    ok = 0
    for c in CASES:
        bad = check(c["answer"])
        got_bad = bool(bad)
        passed = got_bad == c["expect_bad"]
        ok += passed
        mark = "✓" if passed else "✗"
        want = "应判违规" if c["expect_bad"] else "应判合规"
        print(f"{mark} {c['name']}（{want}，实得{'违规' if got_bad else '合规'}）")
        if bad and (verbose or not passed):
            for s in bad:
                print(f"   ⚠ {s[:60]}")
    total = len(CASES)
    print(f"\n{'='*60}")
    print(f"考据陷阱判据 {ok}/{total} ({ok/total:.0%})")
    return ok, total


if __name__ == "__main__":
    main("-v" in sys.argv[1:])
