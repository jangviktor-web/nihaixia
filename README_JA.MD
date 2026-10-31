<div align="center">

<img width="120" src="logo.jpg" alt="倪海厦Skill ロゴ">

# 倪海厦Skill · 経方中医AI

**経方の大家・倪海厦の完全な中医（伝統中国医学）思考体系を AI Agent に注入する**

`『傷寒論』129条` · `『金匱』23篇` · `『黄帝内経』71篇` · `本草345種` · `医案849例` · `講義2,452ページ` · `3.5M字を精錬`

[![GitHub Stars](https://img.shields.io/github/stars/jangviktor-web/nihaixia?style=for-the-badge&color=yellow&label=Stars)](https://github.com/jangviktor-web/nihaixia/stargazers)
[![Version](https://img.shields.io/badge/version-v2.1.0-blue?style=for-the-badge)](https://github.com/jangviktor-web/nihaixia/releases)
[![TCM Mind Distiller](https://img.shields.io/badge/TCM_Mind_Distiller-v4.4.0-red?style=for-the-badge)](https://github.com/jangviktor-web/tcm-distiller)
[![License](https://img.shields.io/badge/license-MulanPSL--2.0-green?style=for-the-badge)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Ready-orange?style=for-the-badge&logo=anthropic&logoColor=white)]()
[![Platforms](https://img.shields.io/badge/platforms-5-purple?style=for-the-badge)](#クイックインストール)

**🌐 [中文](https://github.com/jangviktor-web/nihaixia/blob/main/README.md) | [English](https://github.com/jangviktor-web/nihaixia/blob/main/README_EN.MD) | [日本語](https://github.com/jangviktor-web/nihaixia/blob/main/README_JA.MD)**

</div>

---

> 「中医はとてもシンプルです。陰陽と気血、それだけです。これがわかれば、一つに通じてすべてに通じます。」—— 倪海厦

### 一言で紹介

倪海厦（1954–2012）の中医思考、「人紀」シリーズの教え、臨床心法、「天紀」命理学を、起動可能な Agent Skill へと蒸留しました。これにより AI は倪海厦の視点から六経弁証を行い、経方を選び、症状を読み解くことができます。

**直接起動キーワード**：`Ni Haixia` / `Haixia's perspective` / `Master Ni` / `classical-formula thinking` / `how would Ni Haixia see this`

---

## クイックインストール

<details open>
<summary><b> ClawHub（推奨）— V2.3.0 に更新済み。下記のテキストをエージェントにコピーして更新できます</b></summary>

```bash

openclaw skills install @jangviktor-web/nihaixia
npx skills add https://clawhub.ai/jangviktor-web/skills/nihaixia

```
</details>

<details>
<summary><b>SkillHub（Tencent Cloud）— V2.3.0 に更新済み。下記のテキストをエージェントにコピーして更新できます</b></summary>

```bash

Please install @user_ff4d9420/nihaixia-pro according to https://skillhub.cn/install/skillhub.md.

```
</details>

<details>
<summary><b>手動インストール</b></summary>

```bash

# Manual
git clone https://github.com/jangviktor-web/nihaixia.git
cp -r nihaixia/ ~/.claude/skills/nihaixia/
Install the GitHub project "https://github.com/jangviktor-web/nihaixia" as a local skill.

```
</details>

<details>
<summary><b>モバイル（Tencent IMA アプリ）（V2.3.0 はこのプラットフォームではまだスキル更新チャネルがありません。プラットフォームに連絡して対応中です。まず Tencent SkillHub のコマンドを IMA Copilot に送って更新できます — 手順は下記）</b></summary>

### imaSkill ストアから旧バージョンを直接ダウンロード

<img width="2200"  alt="03" src="https://github.com/user-attachments/assets/de39de98-60d2-40a5-ae1a-2a5ca55b693d" />

倪海厦Skill の Tencent IMA アドレス：https://ima.qq.com/skill?shareId=70e35c8a24ed4c01a0986f9e3c83f3d1&from=share

### 呼び出し方法：

<img width="3000"  alt="1000013924" src="https://github.com/user-attachments/assets/79ac68b1-cf18-47fe-ab32-1f876c5394f9" />
<img width="3000"  alt="1000013923" src="https://github.com/user-attachments/assets/9746a3b0-fd37-49e2-8a3a-0d72a06a765a" />

### Tencent IMA を V2.3.0 に更新する方法：

<img width="2411" height="1339" alt="01" src="https://github.com/user-attachments/assets/43e5f9b6-2eda-476b-9752-212780f271a2" />
<img width="1808" height="1339" alt="02" src="https://github.com/user-attachments/assets/74a2a813-2d68-40ba-a200-dee07d7cb661" />

</details>

<details>
<summary><b>過去バージョンのダウンロード</b></summary>

#### v1.0.0（更新履歴：最初の正式安定版。オープンソースプロジェクトを基に二次開発し、倪海厦「人紀」シリーズの中核内容を完全に蒸留。）
ダウンロード：https://ghproxy.net/https://github.com/jangviktor-web/nihaixia/archive/refs/tags/v1.0.0.zip
#### v1.1.0（更新履歴：『神農本草経』の薬性体系、『傷寒論』、『金匱要略』を深く蒸留 + 全モジュールの検索リンクを修正）
ダウンロード：https://ghproxy.net/https://github.com/jangviktor-web/nihaixia/archive/refs/tags/v1.1.0.zip
#### v2.0.1（更新履歴：疾患別に索引付けした医案245例を追加）
ダウンロード：https://ghproxy.net/https://github.com/jangviktor-web/nihaixia/archive/refs/tags/v2.0.1.zip
#### v2.1.0（更新履歴：ナレッジベース検索ツールから、六経弁証の推論モードを備えた臨床診断アシスタントへアップグレード）
ダウンロード：https://ghproxy.net/https://github.com/jangviktor-web/nihaixia/archive/refs/tags/v2.1.0.zip
#### v2.2.0（更新履歴：中核アップグレード — 構造化クイックリファレンス層と倪師の重要講演3本を追加。SKILL.md の入口に開闔枢図、原穴全表、五兪穴の公式など6つのクイックリファレンスブロックを組み込み。六十四卦を簡潔なリストから人事応用の完全な百科へアップグレード）
ダウンロード：https://ghproxy.net/https://github.com/jangviktor-web/nihaixia/archive/refs/tags/V2.2.0.zip
#### V2.2.1（更新履歴：索引体系を再構築）
ダウンロード：https://ghproxy.net/https://github.com/jangviktor-web/nihaixia/archive/refs/tags/V2.2.1.zip

</details>

---

## 機能マトリクス

| 機能 | 対応 | 説明 |
|:---|:---:|:---|
| 六経弁証 | ✅ | 太陽/陽明/少陽/太陰/少陰/厥陰、伝変の法則 + 欲解時 |
| **六経弁証の診断公式** | ✅ | **診断公式8種 + 迅速診断フローチャート + 脈・舌クイックリファレンス + 七段階思考モデル（v2.1.0 で追加）** |
| 経方の選方 | ✅ | 『傷寒論』129条 + 『金匱』23篇。組成/用量/煎じ方/禁忌を含む |
| 薬物の性味 | ✅ | 『神農本草経』345種。三品分類 + 五味帰経 + 炮製の要点 |
| 臨床医案 | ✅ | 倪師の実際の医案849例。がん/心血管/代謝疾患など6分類 |
| 鍼灸の経穴 | ✅ | 十二経絡 + 井滎兪経合 + 任脈・督脈の要穴 + 中風の救急 |
| 『黄帝内経』 | ✅ | 71篇を完全蒸留。中医基礎理論の中核 |
| 「天紀」命理学 | ✅ | 紫微斗数 + 『易経』六十四卦 + 陽宅風水 |
| 梁冬との対談 | ✅ | 2009年の全7回を完全蒸留。現代的な話題への見解 |
| 第3回扶陽フォーラム講演 | ✅ | 扶陽理論/陰虚→陽虚→陰実の伝変連鎖/紅斑性狼瘡・白血病・脳腫瘍の臨床重症例/生附子と生硫黄の分類別の応用 |
| 仲景心法講義 | ✅ | 経方の用量（剤量）学/桂枝湯は桂枝類方の祖/風湿甘附湯→知母湯→烏頭湯の段階的展開/消化器系に対応する経方/母乳はすなわち月経・七つのがんは同源/掌背と額の温度差で陰陽を即断する手診法 |
| スタンフォード大学講演 + 弟子の経験 | ✅ | 感冒からがんまで一貫して治療/経方入門の三ステップ/弟子・李宗恩と楊貞の記録/望診のまとめ + 診病十問/よく使う圧痛点/胆石・腎結石の専用方 |
| 非公開講座 | ✅ | 重病の大テーマ7つ + 弟子向け講義7回。白血病/乳がん/脳腫瘍などを網羅 |
| 口述表現 | ✅ | 倪海厦の話し言葉スタイルのモジュール。回答を倪師「らしく」します |

---

## 使用例

**傷寒の弁証**
> **Q**：風邪をひきました。寒気がして、汗が出ず、首の後ろが痛みます。
> **A**：太陽傷寒、麻黄湯証です。無汗・悪寒・身体痛 — 寒が表を束縛しています。麻黄は毛孔を開き、桂枝は解肌し、杏仁は気を降ろします。

**方剤の照会**
> **Q**：小柴胡湯はどんなときに使いますか？
> **A**：少陽病の主方です。口苦・咽乾・目眩・往来寒熱 — 一証でも見られれば十分です。

**薬物の性味**
> **Q**：生附子と炮附子の違いは何ですか？
> **A**：生附子 — 陰寒が裏にある、四逆証。炮附子 — 表陽が固まらず、汗が出て風を嫌う。

**医案の参照**
> **Q**：肝臓がんの医案はありますか？
> **A**：はい、がんの医案が147例あります。肝臓がんの症例では、攻堅の処方に疏肝理気を組み合わせることがよくあります。

---

## 中核知識体系

### 六経クイックリファレンス

```
Taiyang (exterior) → Yangming (interior heat) → Shaoyang (half-exterior-half-interior)
         ↓ mistreatment / missed treatment
Taiyin (spleen cold) → Shaoyin (heart-kidney yang deficiency) → Jueyin (yin-yang reversal / upper heat lower cold)
```

### 倪氏の六つの健康基準

1. 朝まで一度も目覚めずに眠れる、不眠がない
2. 食欲が正常で、三食ともに満腹感と空腹感がある
3. 毎朝起床後に排便がある
4. 排尿は1日5～7回、淡く澄んだ黄色
5. 頭と顔は涼しく、手足は温かい（一年中）
6. 朝の勃起反応がある

---

## デモンストレーション

<div align="center">

**六経弁証の基本的な応用**

<img width="729" alt="1" src="https://github.com/user-attachments/assets/5d874838-9339-40cd-ae47-70c153c9c57a" />

**六経の伝変の法則**

<img width="729"  alt="2" src="https://github.com/user-attachments/assets/79c5c8fc-2894-4ecf-8988-42fa0dd354d6" />

**日常の養生と飲食の禁忌**

<img width="729" alt="3" src="https://github.com/user-attachments/assets/70a37746-0d15-4839-aab4-f5fe0e37b8f6" />

</div>

---

## 関連プロジェクト

<div align="center">

### [漢唐中医 · Android 診断アプリ](https://github.com/jangviktor-web/nihaixia-app)

同じナレッジベースを使った独立型の Android アプリです。オフラインで動作し、完全無料です。

[![Download APK](https://img.shields.io/badge/download-APK-green?style=for-the-badge&logo=android)](https://github.com/jangviktor-web/nihaixia-app/releases/latest)
[![GitHub](https://img.shields.io/badge/GitHub-Repo-blue?style=for-the-badge)](https://github.com/jangviktor-web/nihaixia-app)

| 六経診断 | 271方クイックリファレンス | 345薬クイックリファレンス | 子午流注による取穴 |
|:---:|:---:|:---:|:---:|
| インテリジェント問診ガイド | 検索 + 六経フィルター | 性味/帰経による分類 | 361穴の時刻計算 |

</div>

<div align="center">

### [李可Skill · 急危重症の中医AI](https://github.com/jangviktor-web/likeskill)

李可老中医（1930–2013）による急性・危重症のための思考オペレーティングシステムです。医案395例、方剤170以上、症状ルーティングルール92件、仮証の鑑別25種。

倪海厦Skill と相互補完します：倪海厦は全領域にわたる教え（医案849例）をカバーし、李可は急性・危重症の実戦（附子は最大750g）に特化しています。

[![GitHub](https://img.shields.io/badge/GitHub-Repo-blue?style=flat-square&logo=github)](https://github.com/jangviktor-web/likeskill)
[![ClawHub](https://img.shields.io/badge/ClawHub-install%20like-green?style=flat-square)](https://clawhub.ai/jangviktor-web/skills/like)

| 破格救心湯 | 仮証の鑑別25種 | 円運動理論 | 経方の用量（剤量）体系 |
|:---:|:---:|:---:|:---:|
| 附子 30–750g | 仮陽24種以上 + 仮陰1種 | 彭子益を完全蒸留 | 漢代の1両 = 15.625g |

</div>

<div align="center">

### [胡希恕Skill · 経方中医AI](https://github.com/jangviktor-web/huxishu)

胡希恕（1898–1984）の臨床における経方思考、六経八綱弁証体系、方証相応の方法を起動可能な Agent Skill へと蒸留しました。これにより AI は胡希恕の視点から六経弁証、方証の鑑別、臨床での選方を行うことができます。

胡希恕は「経方の第一の伝承者」と称えられています。「六経は八綱に由来する」という彼の洞察は『傷寒論』の弁証体系に対する最も明快な解釈であり、馮世綸ら現代の経方大家に直接影響を与えました。

倪海厦Skill と相互補完します：倪海厦は全領域にわたる教え（医案849例）をカバーし、胡希恕は経方の第一の伝承者として『傷寒論』の弁証体系に対する最も明快な解釈を提供します。

[![GitHub](https://img.shields.io/badge/GitHub-Repo-blue?style=flat-square&logo=github)](https://github.com/jangviktor-web/huxishu)
[![ClawHub](https://img.shields.io/badge/ClawHub-install%20huxishu-green?style=flat-square)](https://clawhub.ai/jangviktor-web/skills/huxishu)

</div>

<div align="center">

### [呉鞠通Skill（温病学派） · 温病の中医AI](https://github.com/jangviktor-web/wujutong)
**呉鞠通**（1758–1836）— 温病学派の集大成者。三焦弁証 + 衛気営血を用い、45病証にわたる医案359例を残し、自らの著作を「『傷寒論』の羽翼」と称しました。「津液の存亡」を中心に据え、温病での発汗を禁じ、甘寒の薬で津液を保ち、陰を守ることを優先しました。

| 観点 | 倪海厦（経方） | 呉鞠通（温病学派） |
|------|--------------|--------------|
| **弁証** | 六経（深さ） | 三焦（部位） |
| **治療の核心** | 邪を外へ駆逐する | 津液を保つ |
| **汗法** | 汗すべきときは汗させる | 温病では発汗を禁ずる |
| **方剤** | 薬味が少なく力が集中（麻黄 / 附子 / 烏頭） | 薬味が多く広くカバー（銀翹 / 白虎 / 復脈） |
| **医案** | 849例、全領域 | 359例、温病 + 雑病 |

**相互補完の関係**：倪海厦は蛇口を修理し（温陽化湿、本を治す）、呉鞠通はたまった水を払います（清湿護津、標を治す）— 一つは縦、一つは横です。急性期には呉を、寛解期には倪を用いれば、両者を合わせて中医における外感病の全体像が見えてきます。

[![GitHub](https://img.shields.io/badge/GitHub-Repo-blue?style=flat-square&logo=github)](https://github.com/jangviktor-web/wujutong)
[![ClawHub](https://img.shields.io/badge/ClawHub-install%20wujutong-green?style=flat-square)](https://clawhub.ai/jangviktor-web/skills/wujutong)

</div>


## データソース

<details>
<summary><b>クリックしてデータソースの完全な一覧を表示（講義録10セット、計2,452ページ）</b></summary>

| 講義録 | ページ数 | 抽出文字数 | 状態 |
|---|---|---|---|
| 『傷寒論』講義録 | 209ページ | 277K | 全量蒸留済み |
| 『金匱要略』講義録 | 419ページ | 626K | 全量蒸留済み |
| 『黄帝内経』講義録 | 461ページ | 227K | 全量蒸留済み |
| 鍼灸教程講義録 | 216ページ | 347K | 全量蒸留済み |
| 『神農本草経』原稿 | 339ページ | 843K | 全量蒸留済み |
| 天機道（紫微斗数） | 75ページ | 85K | 全量蒸留済み |
| 人間道（『易経』） | 146ページ | 164K | 全量蒸留済み |
| 地脈道（風水） | 65ページ | 52K | 全量蒸留済み |
| 漢唐文章集 | 383ページ | 670K | 10篇を蒸留 |
| 倪海厦文集 | 139ページ | 234K | 医案8例を蒸留 |
| **合計** | **2,452ページ** | **3.5M** | |

</details>

<details>
<summary><b>クリックしてリポジトリのディレクトリ構成を表示</b></summary>

```
nihaixia/
├── SKILL.md                    # Main skill file (107KB / 1,548 lines, with six quick-reference blocks incl. opening-closing-pivoting diagram / complete Yuan-primary-point table + role rules + dosology system)
├── expression_style.md         # Ni Haixia's spoken-expression DNA (exclamation usage / rhetorical-interactive style / assertive closings)
├── distilled_cases.md          # Merged edition of 243 categorized narrative cases
├── index.html                  # Detail page
├── logo.jpg                    # Project Logo
├── modules/                    # 14 knowledge modules
│   ├── 01_shanghan_sun.md      # Shang Han Lun Taiyang disease chapter (articles 1–129, line-by-line commentary)
│   ├── 02_shanghan_other.md    # Shang Han Lun Yangming / Shaoyang / Taiyin / Shaoyin / Jueyin
│   ├── 03_yian.md              # Case collection (849 cases)
│   ├── 04_jingui.md            # Jin Gui Yao Lue, 23 chapters fully commented
│   ├── 05_huangdi_neijing.md   # Huang Di Nei Jing 72 chapters + Shang Gu Tian Zhen Lun
│   ├── 06_liangdong.md         # Full Liang Dong dialogue
│   ├── 07_bimen_hantang.md     # Closed-door lectures + Han Tang articles
│   ├── 08_huangdi_detail.md    # Detailed Huang Di Nei Jing lecture contents (461 pp)
│   ├── 09_zhenjiu_bencao.md    # Acupuncture course + Shen Nong's Materia Medica 374 herbs + Tian Ji + full Sixty-Four Hexagram table
│   ├── 10_fuyang_luntan.md     # 3rd Forum on Supporting Yang speech (classical-formula yin-yang + major cancer cases)
│   ├── 11_zhongjing_xinfa.md   # Zhongjing's Heart Method (dosology + hand diagnosis + seven-cancers-one-origin)
│   ├── 12_stanford_jingfang.md # Stanford speech + classical-formula marvels + disciples' experience
│   ├── 13_shanghan_quebing.md  # Supplemented Shang Han Lun articles (Taiyang lower + Yangming chapters)
│   └── 14_yijinjing_bidu.md    # Yi Jin Jing (Tendon-Change Classic) + five-organ toxin-expelling method
├── cases/                      # Case library (1,500+ entries)
│   ├── 00_merged_table.md      # 1,257 fully structured cases table (12 columns: diagnosis / pathogenesis / formula / acupuncture / course / viewpoint)
│   ├── 01_cancer.md            # 147 cancer cases
│   ├── 02_cardiovascular.md    # 22 cardiovascular cases
│   ├── 03_metabolic.md         # 12 metabolic-disease cases
│   ├── 04_autoimmune.md        # 2 autoimmune cases
│   ├── 05_neurological.md      # 3 neuro-psychiatric cases
│   └── 06_other.md             # 59 other cases
├── references/
│   ├── distilled/              # Distillation quick-reference layer (6 files)
│   │   ├── 01-six-meridian-formulas.md # Six-Meridian diagnostic formulas (966 lines)
│   │   ├── 02-acupuncture-quick-ref.md # Acupuncture formula quick-reference (621 lines)
│   │   ├── 03-clinical-experience.md   # Six major cold-damage classical formulas + nineteen pathogenic-mechanism clauses (150 lines)
│   │   ├── 04-acupuncture-highlights.md # Acupuncture highlights compilation (1,761 lines)
│   │   ├── README.md                   # Distillation directory notes
│   │   └── audit-notes.md              # Teaching/verification report
│   ├── research/               # Research materials (10 files: works / dialogues / expression DNA / external evaluations / decisions / timeline / pedagogy / clinical cases / synthesis / distillation log)
│   ├── audit/                  # Formula and acupuncture audit checklists (fangji_112.txt / zhenjiu_164.txt)
│   └── CHANGELOG.md            # Change log
```
</details>

---

## 更新履歴


#### v2.3.0 (2026-08-15) — 用量（剤量）の全面訂正 + 表現の復元 + 経方条文カード体系 + 弁証の厳密さ優先

主なアップグレード：258方の用量の全面訂正を完了し、3体系の単位換算を確定しました。新しい出力が学術的な文体に流れてしまう問題を修正しました（倪師らしさの復元）。経方条文カード体系を導入し、回答前の必読エリアに前倒ししました。弁証の厳密さを優先する鉄則に加え、カードの版表示と漢数字の混同防止の仕組みを追加しました。すべての変更は再レビューを経ており、デグレードはありません。

変更内容：

#### 用量体系の全面訂正（08-13）

- 全258方について、出典ファイル（「人紀」『傷寒論』5,174行 / 『金匱要略』8,920行）と一味ずつ照合し、古代の原方 + 倪師の臨床用量を5回に分けて抽出しました
- モジュール層のP0の明白な誤り5件を修正しました（橘皮竹茹湯 / 大黄附子湯 / 柴胡桂姜湯 / 栝楼薤白半夏湯 / 射干麻黄湯）。P2の用量16件を補い、P3の未収載方7方を追加しました
- 「古方の1両 = 臨床の1銭」という直接換算の鉄則を確定し、考古学的な換算は原方の規模を知るための参考に格下げしました
- 感冒六大経方の早見表を4列（主症 / 古方 / 臨床）に書き直し、6方すべてを訂正しました。桃花湯の2つの版について注記しました

#### 表現の忠実度の修正（08-14）

- SKILL.md 14bの位置・番号付け構造に関する鉄則 + expression_styleの3つの範式（完全な回答 / 問診のやり取り / 冗談まじりの掛け合い）
- 倪師流の冗長さ、脱線、西洋医学批判の強さの禁止を解除し、古くなった03の表現DNAを廃止しました
- 酸棗仁湯：川芎2両 → 芎藭1両。用量の許容範囲で、原文の実例と臨床の段階を区別しました

#### 臨床用量の全面補完（08-14b）

- 経方条文カードの仕様（出典 + 原方 + 臨床の3行。臨床行は決して省略せず、一味ごとに口述 / 換算 / 慣例を個別に判定）
- 249方の臨床用量を全面補完しました（references/distilled/05、06の2つの表）。ライブラリ全体で出典が欠けているのは杏子湯のみです
- 柴胡加竜骨牡蛎湯に黄芩が含まれないのは版の違いであり、薬味の欠落ではないことを確認しました。消腫潰堅湯を追加しました

#### 方剤カードのタイミング前倒し + セッション単位の断定表現の重複排除（08-15a）

- 早見カード⑧の必須出力を回答前の必読エリアに移動しました。4項目チェックの仕組み、カードの照合（本文の方剤数 = カード数）
- セッション単位の断定表現の重複排除（9フレーズのプールをローテーションし、プールを使い切った場合は3ラウンド以上の間隔を空ける）。R1–R8の修正をすべて反映しました
- 断定表現プールの引用符エスケープの誤記を修正しました

#### 弁証の厳密さ優先 + カードの版表示 + 番号の混同防止（08-15b）

- 弁証の厳密さを文体ルールより優先します（六経の定位 → 重要な追加質問 → 類証の鑑別 → 方証の対応。弁証を誤った場合は回答全体を書き直す）
- 「読者の皆さんはどう思いますか？」は1回答につき1回以下に減らし、必須とせず、エピソードを語り終えた後の自然な問いかけとしてのみ使います
- カードの版表示（倪師の講義版 / 金匱版 / 宋本の3つから1つを選択）。漢数字はアラビア数字に変換しません（宋本の第N条と誤認されるのを防ぐため）
- 大承気湯の宋本での対応条文を208に訂正しました（当初は約220と誤記）

検証：オープンな問診30問の比較で30勝0敗。5問の再テストで7/7すべて合格。9次元レビューで90.0（旧版67.1、+22.9）。

| 能力の次元 | v2.2.0 | v2.3.0 |
| -------- | :----: | :--------------------: |
| 経方条文カード体系 | なし | あり（14c仕様 + 早見カード⑧を前倒し） |
| 臨床用量のカバー範囲 | 全量ではない | 258方を訂正 + 249方の臨床用量を完備 |
| 表現復元の範式 | なし | 3範式（完全な回答 / 問診 / 冗談まじりの掛け合い） |
| 弁証の厳密さ優先ルール | なし | あり（14bを文体より優先） |
| 断定表現の重複排除 | なし | セッション単位の9フレーズプール |
| 漢数字の混同防止 | なし | あり（講義の番号をそのまま保持） |
| カードの版表示 | なし | あり（講義版 / 金匱版 / 宋本） |

<details>
<summary><b>クリックして更新履歴の全文を展開</b></summary>

#### v2.2.0 (2026-08-12) — ナレッジベース蒸留早見表 + 倪師の講演3本 + 『易経』六十四卦の全面アップグレード

主なアップグレード：構造化された早見層と倪師の重要な講演3本を追加しました。SKILL.mdの入口に、開闔枢図、原穴の完全な一覧表、五兪穴の公式などを含む6つの早見ブロックを組み込みました。六十四卦は簡潔な一覧から、人事への応用を網羅した完全な事典へとアップグレードしました。

新規内容：

#### 蒸留早見層（references/distilled/、6ファイル、232KB）
- 六経弁証の診断公式：8つの公式 + 迅速診断フローチャート + 脈・舌の早見表 + 合病・併病の早見表 + 真寒仮熱の鑑別 + 7ステップの弁証思考モデル（966行）
- 鍼灸公式早見表：子午流注の口訣 + 十二経の原穴の完全な一覧表 + 五兪穴の属性の法則 + 子母補瀉の公式（621行）
- 感冒六大経方マニュアル：桂枝湯 / 麻黄湯 / 葛根湯 / 大青竜湯 / 小青竜湯 / 小柴胡湯 — 主症 + 用量 + 禁忌（150行）
- 鍼灸の要点集：任脈・督脈の要穴 + 十二経絡の経穴 + 鍼灸治療の精選（1,761行）
- 教学検証レポート：深層蒸留ナレッジベース42篇と既存Skillとの4次元サンプリング比較の結論

#### 倪師の重要な講演3本（modules/10-12、28KB）
- 第3回扶陽論壇での講演（2009.10）：扶陽理論 / 陰虚 → 陽虚 → 陰実の伝変の連鎖 / 紅斑性狼瘡・白血病・脳腫瘍の重症臨床例 / 生附子と生硫黄の分類別の使い方（182行）
- 仲景心法の講義（2009.12）：経方の用量（剤量）学 / 桂枝湯は桂枝類方の祖 / 風湿甘附湯 → 知母湯 → 烏頭湯の段階的な展開 / 消化器系と経方の対応 / 母乳は月経である・七癌同源 / 手の甲と額の温度差で陰陽を即座に見分ける手診法（218行）
- スタンフォード大学での講演 + 弟子たちの経験（2010.09）：感冒から癌まで一貫して治療する / 経方に入門する3つのステップ / 弟子の李宗恩・楊貞の実録 / 望診のまとめ + 診病十問 / よく使う圧痛点 / 胆石・腎結石の専用方（185行）

#### SKILL.md入口の早見表アップグレード（+130行）
- 開闔枢の総合図：三陽（太陽は開 → 少陽は枢 → 陽明は闔）+ 三陰（太陰は開 → 少陰は枢 → 厥陰は闔）のASCII図
- 『傷寒論』の二大補虚方の鉄則：小建中湯（表の陽虚、太陽に太陰を兼ねる）+ 炙甘草湯（裏の陰虚、少陰の陰陽両虚）
- 十二経の原穴の完全な一覧表：12経 × 時辰 × 五行 × 原穴 + 口訣「肺寅大卯胃辰宮……」
- 五兪穴の公式：井滎兪経合 × 陰経・陽経の五行 + 主治法則の口訣
- 感冒六大経方の早見表：主症の要点 + 中核となる用量を1枚の図に
- 資料パス索引：9ファイルの行数 / 適用場面の早見表

#### modules/09 六十四卦の全面アップグレード
- 元の簡潔な一覧 → 完全な構造化表：64卦 × 4列（順序・卦名・卦象記号・人事への応用）
- 地天泰卦の専用章を追加：卦徳の解説 + 人事に関する6つの中核的解釈（泰と否は一念の差 / 包荒をもって泰を治める / 師道の泰 / 諸葛亮の三顧の礼 / 嫁姑の道 / 器量を見極める4つの言葉）+ 陽宅への応用（妻は北西の隅に住む）+ 占いの図解 + 倪師の名言
- 『易経』総論を追加：『易経』は占いの本ではなく、小人を避けて君子に従う人の道の手引きである

#### 教学検証の強化
- 深層蒸留ナレッジベースのカバー範囲と次元ごとにサンプリング比較しました（傷寒 / 金匱 / 内経 / 鍼灸 / 診断公式 / 臨床経験）
- 結論：既存のSkillは事実の95%をカバーしており、大きな矛盾はありません。開闔枢の図解 / 二大補虚方のまとめ / 7ステップ思考モデル / 真寒仮熱の鑑別を補いました
- キーワード索引に3つのセクションを追加：扶陽論壇 / 癌の臨床、仲景心法、スタンフォード講演

| 指標 | v2.1.0 | v2.2.0 |
|------|:-----:|:-----:|
| 総ファイル数 | 31 | 42 |
| ナレッジモジュール | 9 | 12 |
| SKILL.mdの行数 | 11,169 | 11,277 |
| 六十四卦の表示 | 簡潔な一覧 | 64卦の完全な表 + 卦象記号 |
| 診断公式 | 本文中に散在 | 独立した早見ファイル966行 |
| 講演モジュール | 0 | 3（扶陽 + 仲景 + スタンフォード） |
---
#### v2.1.0 (2026-06-08) — 六経弁証の診断公式

**主なアップグレード**：ナレッジベース検索ツールから、六経弁証の思考モードを備えた臨床診断アシスタントへとアップグレードしました。

**新規内容**：
- **8つの診断公式**：太陽 / 陽明 / 少陽 / 太陰 / 少陰 / 厥陰 / 少陰熱化 / 合病・併病。それぞれにIF-THEN形式の弁証ルール + 病型鑑別表 + 代表方剤を収録
- **迅速診断フローチャート**：患者の症状から六経の定位までの完全な決定木
- **脈診早見表**：単一の脈8種 + 複合脈象8種
- **舌診早見表**：舌象5種 + 複合舌象6種 + 脈と舌が矛盾する場合の決定木
- **真寒仮熱 / 仮寒の鑑別**：8次元法（顔色 / 口鼻の息 / 舌の形 / 脈 / 胸腹 / 小便 / 口渇 / 大便）+ 危重証候の警告
- **合病・併病の早見表**：11の組み合わせ + 治療の先後の原則
- **7ステップの弁証思考モデル**：表裏を定める → 陰陽を分ける → 寒熱を弁じる → 伝変を判断する → 体質を見極める → 方剤を選ぶ → 加減を精緻にする
- **用薬の鉄則**：禁忌7条 + 救急プラン5条
- **建中湯シリーズ**：小建中 / 黄耆建中 / 当帰建中 / 大建中（太陰病の拡張）
- **治肝三法**：烏梅丸 / 呉茱萸湯 / 小建中湯（金匱の中核）
- **八味腎気丸の詳解**：三補三瀉 + 桂附八味丸と六味地黄丸の比較
- **金匱雑病の六経帰属早見表**：雑病12種 + 代表方剤
- **金匱固有の方剤の六経帰属**：咳喘類4方 + 補虚類8方 + 歴節類3方（完全な組成付き）
- **11か所の相互参照**：診断公式 → モジュール / 詳細な条文への双方向リンク

**データソース**：
- 倪海厦『傷寒論講義』（「人紀」シリーズ）
- 倪海厦『黄帝内経講義』（「人紀」シリーズ）
- 倪海厦『金匱要略講義』（「人紀」シリーズ）

**品質検証**：
- Darwin skillスコア：9.4/10
- 臨床シナリオテスト10件：10/10をカバー
- 11方の用量を一方ずつ照合：出典ファイルと100%一致
- 六経の提綱条文の照合：6条中5条が完全一致、1条は異体字の違いのみ

**SKILL.mdの変更**：+476行（10,697 → 11,169行）、新規追加は第6097–6545行

---

- **v2.0.1** (2026-05-26)：分類別医案ライブラリ cases/（245例）+ 研究資料 references/ を追加。.gitignore を修正
- **v2.0.0** (2026-05-25)：リポジトリを軽量化 — 生の参考資料（110MB）を削除し、実行に必要なファイル（4MB）のみを残しました
- **v1.1.2** (2026-05-24)：詳細ページを書き直し — インストール手順と使用例を追加
- **v1.1.1** (2026-05-24)：「倪海厦Skill」に改名し、slugを `nihaixia` に変更
- **v1.1.0** (2026-05-23)：『神農本草経』の薬性体系を深層蒸留。キーワード索引を全面的に最適化
- **v1.0.1** (2026-05-02)：構造を最適化。OCRの誤りを13か所訂正。漢唐文章の精華10篇を追加
- **v1.0.0** (2026-04-14)：初版リリース

</details>

---

## 謝辞

- nihaisha-skillのベースフレームワークを提供してくださった[huoyalong](https://github.com/huoyalong/nihaisha-skill)に感謝します
- 医案データの面で支援してくださった[9527qingfeng](https://github.com/9527qingfeng/hantang-nihaixia-follower)に感謝します

---

## Star History

[![RepoStars](https://repostars.dev/api/embed?repo=jangviktor-web%2Fnihaixia&theme=grape)](https://repostars.dev/?repos=jangviktor-web%2Fnihaixia&theme=grape)

---



## 免責事項

本プロジェクトの内容は中医学の学習と研究のみを目的としており、専門的な医学的診断に代わるものではありません。診断と治療については、必ず資格を持つ医療従事者にご相談ください。

---


<div align="center">

**[nihaisha-skill](https://github.com/huoyalong/nihaisha-skill)をベースにした二次開発 · MulanPSL-2.0 オープンソースライセンスの下で公開**

[![ClawHub](https://img.shields.io/badge/ClawHub-v2.1.0-orange)](https://clawhub.ai/jangviktor-web/skills/nihaixia)
[![OpenClawMP](https://img.shields.io/badge/OpenClawMP-v2.0.1-blueviolet)](https://openclawmp.cc)
[![SkillHub](https://img.shields.io/badge/SkillHub-nihaixia--pro-red)](https://skillhub.cloud.tencent.com/skills/nihaixia-pro)

</div>
