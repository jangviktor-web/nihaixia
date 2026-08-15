<div align="center">

<img width="120" src="logo.jpg" alt="Ni Haixia Skill Logo">

# Ni Haixia Skill · Classical Formula (Jingfang) TCM AI

**Inject the complete TCM thinking system of master classic-formula physician Ni Haixia into an AI Agent**

`129 Treatises of Shanghan Lun` · `23 Chapters of Jingui` · `71 Chapters of Huangdi Neijing` · `345 Herbs` · `849 Case Records` · `2,452 Pages of Lectures` · `3.5M Characters of Essence`

[![GitHub Stars](https://img.shields.io/github/stars/jangviktor-web/nihaixia?style=for-the-badge&color=yellow&label=Stars)](https://github.com/jangviktor-web/nihaixia/stargazers)
[![Version](https://img.shields.io/badge/version-v2.1.0-blue?style=for-the-badge)](https://github.com/jangviktor-web/nihaixia/releases)
[![License](https://img.shields.io/badge/license-MulanPSL--2.0-green?style=for-the-badge)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Ready-orange?style=for-the-badge&logo=anthropic&logoColor=white)]()
[![Platform](https://img.shields.io/badge/platform-5-purple?style=for-the-badge)](#quick-install)

**🌐 [中文 (Chinese)](https://github.com/jangviktor-web/nihaixia/blob/main/README.md) | [English](https://github.com/jangviktor-web/nihaixia/blob/main/README_EN.MD)**

</div>

---

> "TCM is very simple — it is just yin-yang, qi, and blood. Once you understand it, everything clicks into place." — Ni Haixia

### One-line Introduction

Distill Ni Haixia's (1954–2012) TCM thinking, the Renji teaching series, clinical insights, and the Tianji destiny system into an activatable Agent Skill, enabling AI to perform Six-Meridian (Liu Jing) syndrome differentiation, select classic formulas, and interpret symptoms from Ni Haixia's perspective.

**Direct activation keywords**: `Ni Haixia` / `Haixia's perspective` / `Master Ni` / `classic-formula thinking` / `how would Ni Haixia see this`

---

## Quick Install

<details open>
<summary><b> ClawHub (Recommended)</b></summary>

```bash
openclaw skills install @jangviktor-web/nihaixia
```
</details>

<details>
<summary><b>SkillHub (Tencent Cloud)</b></summary>

```bash
curl -fsSL https://skillhub.cn/install/install.sh | bash -s -- --no-skills
skillhub install nihaixia-pro
```
</details>

<details>
<summary><b>OpenClaw / OpenClawMP / Manual Install</b></summary>

```bash
# OpenClaw
openclaw skills install @jangviktor-web/nihaixia


# Manual
git clone https://github.com/jangviktor-web/nihaixia.git
cp -r nihaixia/ ~/.claude/skills/nihaixia/
```
</details>

<details>
<summary><b>Mobile (Tencent IMA App)</b></summary>

Download the Tencent IMA App, scan the knowledge QR code below, and use it directly with no configuration required.

<img width="200"  alt="Ni Haixia Knowledge QR Code" src="https://github.com/user-attachments/assets/fb4fb05c-fc21-41fe-941e-c820ec16b750" />

Ni Haixia Skill on Tencent IMA: https://ima.qq.com/skill?shareId=70e35c8a24ed4c01a0986f9e3c83f3d1&from=share

How to invoke:
<img width="3085"  alt="1000013924" src="https://github.com/user-attachments/assets/79ac68b1-cf18-47fe-ab32-1f876c5394f9" />
<img width="3085"  alt="1000013923" src="https://github.com/user-attachments/assets/9746a3b0-fd37-49e2-8a3a-0d72a06a765a" />
</details>


---

## Feature Matrix

| Capability | Coverage | Description |
|:---|:---:|:---|
| Six-Meridian Differentiation | ✅ | Taiyang / Yangming / Shaoyang / Taiyin / Shaoyin / Jueyin, transmission rules + optimal resolution times |
| **Six-Meridian Diagnostic Formulas** | ✅ | **8 diagnostic formulas + rapid diagnostic flowchart + pulse/tongue quick reference + seven-step thinking model (new in v2.1.0)** |
| Classic Formula Selection | ✅ | 129 Treatises of Shanghan Lun + 23 Chapters of Jingui, including composition / dosage / decoction method / contraindications |
| Herb Properties | ✅ | 345 herbs from Shennong Bencao Jing, three-tier classification + five flavors & meridian tropism + processing essentials |
| Clinical Case Records | ✅ | 849 authentic case records of Master Ni, categorized into 6 groups (cancer / cardiovascular / metabolic, etc.) |
| Acupuncture Points | ✅ | Twelve meridians + Five Shu points + Ren/Du key points + stroke first aid |
| Huangdi Neijing | ✅ | 71 chapters fully distilled, core of TCM foundational theory |
| Tianji Destiny System | ✅ | Ziwei Doushu (Purple Star Astrology) + I Ching 64 hexagrams + Yangzhai Feng Shui |
| Liang Dong Dialogue | ✅ | 7 complete recorded dialogues from 2009, views on modern topics |
| 3rd Fuyang Forum Lecture | ✅ | Fuyang theory / yin-deficiency → yang-deficiency → yin-excess transmission chain / severe lupus / leukemia / brain tumor cases / raw aconite & raw sulfur classification |
| Zhang Zhongjing's Heart Method Lecture | ✅ | Classic-formula dosology / Guizhi Tang as ancestor of all formulas / rheumatic-Gancao-Fuzi → Zhimu → Wutou progression / digestive-system formula mapping / breast milk = menstruation · seven cancers share one origin / hand & back & forehead temperature differential for instant yin-yang diagnosis |
| Stanford University Lecture + Disciple Experience | ✅ | From common cold all the way to cancer / three-step classic-formula入门 / Li Zong'en & Yang Zhen disciple records / inspection summary + ten diagnostic questions / common tender points / specialized formulas for gall/kidney stones |
| Closed-door Lectures | ✅ | 7 major critical-illness topics + 7 disciple sessions, leukemia / breast cancer / brain tumor, etc. |
| Spoken Expression | ✅ | Ni Haixia spoken-style module, responses "sound like" Master Ni |

---

## Usage Examples

**Cold/Flu Differentiation**
> **Q**: I caught a cold, I'm afraid of cold, no sweating, and the back of my neck hurts
> **A**: Taiyang cold damage, Mahuang Tang (Ephedra Decoction) syndrome. No sweat, aversion to cold, body aches — cold is bound at the exterior. Ephedra opens the pores, cinnamon twig relieves the muscles, apricot kernel descends qi.

**Formula Lookup**
> **Q**: When do you use Xiao Chaihu Tang (Minor Bupleurum Decoction)?
> **A**: The sovereign formula for Shaoyang disease. Bitter mouth, dry throat, dizzy vision, alternating chills and fever — the presence of even one sign is sufficient.

**Herb Properties**
> **Q**: Difference between raw aconite and processed aconite?
> **A**: Raw aconite — yin-cold deep inside, the Four-Reversal (Sini) syndrome. Processed aconite — exterior yang not secure, sweating with aversion to wind.

**Case Reference**
> **Q**: Any liver cancer case records?
> **A**: Yes, 147 cancer case records. Liver cancer cases commonly use hardness-breaking formulas combined with liver-soothing and qi-regulating.

---

## Core Knowledge System

### Six-Meridian Quick Reference

```
Taiyang (exterior) → Yangming (interior heat) → Shaoyang (half-exterior half-interior)
         ↓ mistreatment / missed treatment
Taiyin (spleen cold) → Shaoyin (heart-kidney yang deficiency) → Jueyin (yin-yang reversal / upper heat lower cold)
```

### Ni's Six Health Standards

1. Sleep through the night until dawn, no insomnia
2. Normal appetite, hunger/satiety sensation at three meals
3. Daily morning bowel movement
4. 5–7 urinations per day, pale clear yellow
5. Head and face cool, hands and feet warm (all year round)
6. Morning arousal response (spontaneous erection)

---

## Demonstration

<div align="center">

**Basic Six-Meridian Differentiation Application**
<img width="729" alt="1" src="https://github.com/user-attachments/assets/5d874838-9339-40cd-ae47-70c153c9c57a" />

**Six-Meridian Transmission Rules**
<img width="729"  alt="2" src="https://github.com/user-attachments/assets/79c5c8fc-2894-4ecf-8988-42fa0dd354d6" />

**Daily Health Preservation & Dietary Contraindications**
<img width="729" alt="3" src="https://github.com/user-attachments/assets/70a37746-0d15-4839-aab4-f5fe0e37b8f6" />

</div>

---

## Related Projects

<div align="center">

### [Han Tang TCM · Android Diagnostic App](https://github.com/jangviktor-web/nihaixia-app)

The same knowledge base, as a standalone Android app. Works offline, completely free.

[![Download APK](https://img.shields.io/badge/download-APK-green?style=for-the-badge&logo=android)](https://github.com/jangviktor-web/nihaixia-app/releases/latest)
[![GitHub](https://img.shields.io/badge/GitHub-Repo-blue?style=for-the-badge)](https://github.com/jangviktor-web/nihaixia-app)

| Six-Meridian Diagnosis | 271 Formula Quick Search | 345 Herb Quick Search | Midnight-Noon Flow Point Selection |
|:---:|:---:|:---:|:---:|
| Smart Consultation Guide | Search + Six-Meridian Filter | Flavor & Meridian Classification | 361-Point Time Calculation |

</div>

<div align="center">

### [Li Ke Skill · Critical Care TCM AI](https://github.com/jangviktor-web/likeskill)

The critical-care thinking operating system of veteran physician Li Ke (1930–2013). 395 case records, 170+ formulas, 92 symptom routing paths, 25 false-syndrome identifications.

Complements Ni Haixia Skill: Ni covers full-spectrum teaching (849 cases), Li focuses on critical-care practice (aconite up to 750g).

[![GitHub](https://img.shields.io/badge/GitHub-Repo-blue?style=flat-square&logo=github)](https://github.com/jangviktor-web/likeskill)
[![ClawHub](https://img.shields.io/badge/ClawHub-install%20like-green?style=flat-square)](https://clawhub.ai/jangviktor-web/skills/like)

| Po Ge Jiu Xin Tang | 25 False-Syndrome IDs | Round-Motion Theory | Classic-Formula Dosology |
|:---:|:---:|:---:|:---:|
| Aconite 30–750g | 24+ false-yang + 1 false-yin | Peng Ziyi fully distilled | Han dynasty 1 liang = 15.625g |

</div>

<div align="center">

### [Hu Xishu Skill · Classic Formula TCM AI](https://github.com/jangviktor-web/huxishu)

Distill Hu Xishu's (1898–1984) classic-formula clinical thinking, the Six-Meridian Eight-Principle differentiation system, and the formula-syndrome correspondence method into an activatable Agent Skill, enabling AI to perform Six-Meridian differentiation, formula-syndrome discrimination, and clinical formula selection from Hu Xishu's perspective.

Hu Xishu is celebrated as the "foremost transmitter of classic formulas." His insight that "the Six Meridians derive from the Eight Principles" is the clearest interpretation of the Shanghan Lun differentiation system, directly influencing contemporary classic-formula masters such as Feng Shilun.

Complements Ni Haixia Skill: Ni covers full-spectrum teaching (849 cases), Hu is the foremost transmitter of classic formulas and offers the clearest interpretation of the Shanghan Lun differentiation system.

[![GitHub](https://img.shields.io/badge/GitHub-Repo-blue?style=flat-square&logo=github)](https://github.com/jangviktor-web/huxishu)
[![ClawHub](https://img.shields.io/badge/ClawHub-install%20huxishu-green?style=flat-square)](https://clawhub.ai/jangviktor-web/skills/huxishu)

</div>

<div align="center">

### [Wenbing School (Wu Jutong) Skill · Warm-Disease TCM AI](https://github.com/jangviktor-web/wujutong)
**Wu Jutong** (1758–1836) — the synthesizer of the Warm-Disease (Wenbing) school, Sanjiao (Triple Burner) differentiation + Defense-Qi-Nutrient-Blood, 359 cases across 45 disease patterns, self-described as the "wings of Shanghan Lun," centered on the "presence or loss of body fluids," forbidding sweating in warm disease, preserving yin with sweet-cool herbs as the first priority.

| Dimension | Ni Haixia (Classic Formula) | Wu Jutong (Wenbing School) |
|------|--------------|--------------|
| **Differentiation** | Six Meridians (depth) | Sanjiao (location) |
| **Core Treatment** | Expel pathogen outward | Preserve body fluids |
| **Sweating** | Sweat when indicated | Forbidden in warm disease |
| **Formulas** | Few herbs, concentrated power (ephedra / aconite / wutou) | Many herbs, broad coverage (YinQiao / Baihu / Fumai) |
| **Cases** | 849 cases, full spectrum | 359 cases, warm disease + miscellaneous |

**Complementary relationship**: Ni Haixia fixes the faucet (warming yang, transforming dampness, treating the root); Wu Jutong clears the standing water (clearing dampness, protecting fluids, treating the branch) — one vertical, one horizontal. Use Wu in the acute phase, Ni in the remission phase; together they reveal the full picture of external contraction disease in TCM.

[![GitHub](https://img.shields.io/badge/GitHub-Repo-blue?style=flat-square&logo=github)](https://github.com/jangviktor-web/wujutong)
[![ClawHub](https://img.shields.io/badge/ClawHub-install%20wujutong-green?style=flat-square)](https://clawhub.ai/jangviktor-web/skills/wujutong)

</div>


## Data Sources

<details>
<summary><b>Click to view the full data source list (10 lecture sets, 2,452 pages)</b></summary>

| Lecture Set | Pages | Characters | Status |
|---|---|---|---|
| Shanghan Lun Lecture | 209 pages | 277K | Fully distilled |
| Jingui Yaolue Lecture | 419 pages | 626K | Fully distilled |
| Huangdi Neijing Lecture | 461 pages | 227K | Fully distilled |
| Acupuncture Course Lecture | 216 pages | 347K | Fully distilled |
| Shennong Bencao Jing Manuscript | 339 pages | 843K | Fully distilled |
| Tianji Dao (Ziwei Doushu) | 75 pages | 85K | Fully distilled |
| Renjian Dao (I Ching) | 146 pages | 164K | Fully distilled |
| Dima Dao (Feng Shui) | 65 pages | 52K | Fully distilled |
| Han Tang Article Collection | 383 pages | 670K | 10 articles distilled |
| Ni Haixia Collected Works | 139 pages | 234K | 8 cases distilled |
| **Total** | **2,452 pages** | **3.5M** | |

</details>

<details>
<summary><b>Click to view the repository structure</b></summary>

```
nihaixia/
├── SKILL.md                    # Main skill file (107KB / 1,548 lines, with 6 quick-reference blocks: opening-closing-pivot diagram / source-point table / five-shu formula, plus role rules + dosage system)
├── expression_style.md         # Ni Haixia spoken-expression DNA (usage of "hao" / rhetorical Q&A interaction / assertive closing)
├── distilled_cases.md          # Merged version of 243 categorized narrative cases
├── index.html                  # Detail page
├── logo.jpg                    # Project logo
├── modules/                    # 14 knowledge modules
│   ├── 01_shanghan_sun.md      # Shanghan Lun Taiyang disease chapter (treatises 1-129, line-by-line)
│   ├── 02_shanghan_other.md    # Shanghan Lun Yangming / Shaoyang / Taiyin / Shaoyin / Jueyin
│   ├── 03_yian.md              # Case collection (849 cases)
│   ├── 04_jingui.md            # Jingui Yaolue, 23 chapters fully interpreted
│   ├── 05_huangdi_neijing.md   # Huangdi Neijing 72 chapters + Shanggu Tianzhen Lun
│   ├── 06_liangdong.md        # Full Liang Dong dialogue
│   ├── 07_bimen_hantang.md     # Closed-door lectures + Han Tang articles
│   ├── 08_huangdi_detail.md    # Huangdi Neijing detailed lecture index (461 pages)
│   ├── 09_zhenjiu_bencao.md    # Acupuncture course + Shennong Bencao Jing 374 herbs + Tianji + 64-hexagram full table
│   ├── 10_fuyang_luntan.md     # 3rd Fuyang Forum lecture (classic-formula yin-yang + severe cancer cases)
│   ├── 11_zhongjing_xinfa.md   # Zhang Zhongjing's Heart Method (dosology + hand diagnosis + seven cancers one origin)
│   ├── 12_stanford_jingfang.md # Stanford lecture + classic-formula ingenuity + disciple experience
│   ├── 13_shanghan_quebing.md  # Shanghan Lun treatise completion (lower Taiyang + Yangming chapters)
│   └── 14_yijinjing_bidu.md    # Tendon-Classic (Yijinjing) + Five-Organ Toxic-Expulsion Method
├── cases/                      # Case library (1,500+ entries)
│   ├── 00_merged_table.md      # 1,257 cases full structured table (12 columns: diagnosis / mechanism / formula / acupuncture / course / viewpoint)
│   ├── 01_cancer.md            # 147 cancer cases
│   ├── 02_cardiovascular.md    # 22 cardiovascular cases
│   ├── 03_metabolic.md         # 12 metabolic disease cases
│   ├── 04_autoimmune.md        # 2 autoimmune cases
│   ├── 05_neurological.md      # 3 neuro-psychiatric cases
│   └── 06_other.md             # 59 other cases
├── references/
│   ├── distilled/              # Distilled quick-reference layer (6 files)
│   │   ├── 01-six-meridian-formulas.md # Six-Meridian diagnostic formulas (966 lines)
│   │   ├── 02-acupuncture-quick-ref.md # Acupuncture formula quick reference (621 lines)
│   │   ├── 03-clinical-experience.md   # Six major cold formulas + 19 pathogen mechanisms (150 lines)
│   │   ├── 04-acupuncture-highlights.md # Acupuncture key-content compilation (1,761 lines)
│   │   ├── README.md                   # Distilled directory notes
│   │   └── audit-notes.md              # Teaching-validation report
│   ├── research/               # Research materials (10 files: works / dialogues / expression DNA / external reviews / decisions / timeline / pedagogy / clinical cases / synthesis / distillation log)
│   ├── audit/                  # Formula & acupuncture audit checklists (fangji_112.txt / zhenjiu_164.txt)
│   └── CHANGELOG.md            # Change log
```
</details>

---

## Changelog


#### v2.3.0 (2026-08-15) — Full Dosage Audit + Expression Restoration + Classic-Formula Card System + Differentiation Rigor Priority

Core upgrade: Completed full dosage audit of 258 formulas with the three-system conversion solidified; fixed the over-academic tone of new outputs (restoring Master Ni's voice); launched the classic-formula treatise card system and moved it to the pre-response must-read zone; added the differentiation-rigor-priority rule plus card version labeling and Chinese-numeral anti-confusion mechanism. All changes registered and re-verified with no rollback.

Changes:

#### Full Dosage Audit (08-13)

- Audited all 258 formulas ingredient-by-ingredient against source files (Renji Shanghan Lun 5,174 lines / Jingui Yaolue 8,920 lines), extracting ancient original dosages + Master Ni's clinical dosages in 5 batches
- Fixed 5 P0 hard errors at the module layer (Jupi Zhuru Tang / Dahuang Fuzi Tang / Chaihu Guijiang Tang / Gualou Xiebai Banxia Tang / Shegan Mahuang Tang), added 16 P2 dosages, added 7 P3 unlisted formulas
- Solidified the iron rule of "ancient 1 liang = clinical 1 qian" direct conversion; archaeological conversion demoted to reference for original formula scale only
- Rewrote the six-major-cold-formula quick-reference table into 4 columns (main symptom / ancient formula / clinical), all 6 formulas fixed; dual-version note for Taohua Tang

#### Expression Restoration Fix (08-14)

- SKILL.md 14b iron rule against localization / numbered-structure + expression_style three paradigms (complete answer / consultative back-and-forth / banter)
- Unbanned Master Ni-style redundancy, digression, and anti-Western-medicine intensity; deprecated the outdated 03 expression DNA
- Chuanzi Teng Tang: 芎䓖二两 → 芎藭一两; dosage authorization spectrum now distinguishes original-text instances from clinical tiers

#### Full Clinical Dosage Completion (08-14b)

- Classic-formula treatise card spec (source + original formula + clinical, three lines, clinical line never omitted, per-ingredient independent judgment: oral / converted / conventional)
- 249 formulas' clinical dosages fully completed (references/distilled/05, 06 tables); only Xingzi Tang lacks a source formula in the whole library
- Chaihu Jia Longgu Muli Tang confirmed to omit huangqin as a version difference, not a missing herb; Xiaozhong Kuijian Tang supplemented

#### Formula-Card Timing Advance + Session-Level Assertion Deduplication (08-15a)

- Quick-reference card ⑧ (mandatory card output) moved to the pre-response must-read zone; four-check mechanism; card reconciliation (body formula count = card count)
- Session-level assertion deduplication (9-phrase pool rotation, ≥3 rounds interval when pool exhausted); R1–R8 fixes all landed
- Fixed assertion-pool quote-escaping typo

#### Differentiation Rigor Priority + Card Version Label + Numeral Anti-Confusion (08-15b)

- Differentiation rigor prioritized over style rules (Six-Meridian location → key follow-up questions → similar-syndrome discrimination → formula-syndrome matching; wrong differentiation = full rewrite)
- "What do readers think?" frequency reduced to ≤1 per answer, non-mandatory, only as a natural反问 after finishing a story
- Cards labeled with version (Master Ni lecture version / Jingui version / Song edition, one of three); Chinese numerals forbidden from converting to Arabic (prevents mislabeling as Song treatise N)
- Dachengqi Tang Song-edition mapping corrected to 208 (originally mislabeled ~220)

Validation: 30 open consultation A/B tests, 30 wins 0 losses; 5-question retest 7/7 all green; 9-dimension review 90.0 vs old 67.1 (+22.9).

| Capability Dimension | v2.2.0 | v2.3.0 |
| -------- | :----: | :--------------------: |
| Classic-formula treatise card system | None | Yes (14c spec + quick-card ⑧ advance) |
| Clinical dosage coverage | Not full | 258-formula audit + 249-formula full clinical |
| Expression restoration paradigm | None | 3 paradigms (complete answer / consultative back-and-forth / banter) |
| Differentiation rigor rule | None | Yes (14b prioritized over style) |
| Assertion deduplication | None | Session-level 9-phrase pool |
| Chinese numeral anti-confusion | None | Yes (lecture numerals preserved as-is) |
| Card version labeling | None | Yes (lecture / Jingui / Song edition) |

<details>
<summary><b>Click to expand the full changelog</b></summary>

#### v2.2.0 (2026-08-12) — Knowledge Base Distillation Quick-Reference + Three Master Ni Lectures + I Ching 64-Hexagram Full Upgrade

Core upgrade: Added a structured quick-reference layer and three important Master Ni lectures; planted six major quick-reference blocks into the SKILL.md entry (opening-closing-pivot diagram / source-point full table / five-shu formula, etc.); upgraded the 64 hexagrams from a concise list to a complete human-affairs application encyclopedia.

New content:

#### Distillation Quick-Reference Layer (references/distilled/, 6 files, 232KB)
- Six-Meridian diagnostic formulas: 8 formulas + rapid diagnostic flowchart + pulse/tongue quick reference + concurrent/combined disease quick reference + true-cold-false-heat discrimination + seven-step thinking model (966 lines)
- Acupuncture formula quick reference: midnight-noon flow mnemonic + twelve-meridian source-point full table + five-shu attribute rules + mother-son tonify-drain formula (621 lines)
- Six-major-cold-formula handbook: Guizhi Tang / Mahuang Tang / Gegen Tang / Daqinglong Tang / Xiaoqinglong Tang / Xiao Chaihu Tang, main symptoms + dosage + contraindications (150 lines)
- Acupuncture key-content compilation: Ren/Du key points + twelve-meridian points + selected acupuncture treatments (1,761 lines)
- Teaching-validation report: deep-distillation knowledge base 42 articles vs existing skill, four-dimensional sampling comparison conclusions

#### Three Important Master Ni Lectures (modules/10-12, 28KB)
- 3rd Fuyang Forum lecture (2009.10): Fuyang theory / yin-deficiency → yang-deficiency → yin-excess transmission chain / severe lupus leukemia brain-tumor cases / raw aconite & raw sulfur classification (182 lines)
- Zhang Zhongjing's Heart Method lecture (2009.12): classic-formula dosology / Guizhi Tang as ancestor of all formulas / rheumatic-Gancao-Fuzi → Zhimu → Wutou progression / digestive-system formula mapping / breast milk = menstruation · seven cancers one origin / hand-back-forehead temperature differential for instant yin-yang hand diagnosis (218 lines)
- Stanford University lecture + disciple experience (2010.09): from common cold all the way to cancer / three-step classic-formula entry / Li Zong'en & Yang Zhen disciple records / inspection summary + ten diagnostic questions / common tender points / specialized formulas for gall/kidney stones (185 lines)

#### SKILL.md Entry Quick-Reference Upgrade (+130 lines)
- Opening-closing-pivot master diagram: three yang (Taiyang opening → Shaoyang pivot → Yangming closing) + three yin (Taiyin opening → Shaoyin pivot → Jueyin closing) ASCII visualization
- Two major Shanghan Lun deficiency-tonifying formulas iron rule: Xiao Jianzhong Tang (exterior yang deficiency, Taiyang with Taiyin) + Zhigancao Tang (interior yin deficiency, Shaoyin yin-yang dual deficiency)
- Twelve-meridian source-point full table: 12 meridians × time-period × five elements × source point + "Lung at Yin, Large Intestine at Mao, Stomach at Chen" mnemonic
- Five-shu formula: Jing-Ying-Shu-Jing-He × yin/yang meridian five elements + treatment-rule mnemonic
- Six-major-cold-formula quick reference: key main symptoms + core dosage in one diagram
- Material path index: 9 files with line counts / applicable scenarios quick table

#### modules/09 64-Hexagram Full Upgrade
- Original concise list → complete structured table: 64 hexagrams × 4 columns (number · name · hexagram symbol · human-affairs application)
- New Tai hexagram (Earth over Heaven) dedicated chapter: hexagram virtue explanation + 6 core human-affairs interpretations (Tai/Pi a thought apart / embracing openness to govern Tai / the Tao of teaching in Tai / Zhuge Liang's three visits / mother-in-law & daughter-in-law way / four phrases for judging capacity) + Yangzhai application (wife resides in northwest corner) + divination diagram + Master Ni's golden quotes
- New I Ching general theory: the I Ching is not a fortune-telling book, but a guide to the human way for the gentleman to avoid the petty man

#### Teaching-Validation Enhancement
- Four-dimensional sampling comparison with the deep-distillation knowledge base coverage (Shanghan / Jingui / Neijing / acupuncture / diagnostic formulas / clinical experience)
- Conclusion: existing skill covers 95% of facts, no major conflicts; supplemented opening-closing-pivot visualization / two major deficiency-tonifying formula summary / seven-step thinking model / true-cold-false-heat discrimination
- Keyword index added 3 sections: Fuyang Forum / cancer clinical, Zhang Zhongjing's Heart Method, Stanford lecture

| Metric | v2.1.0 | v2.2.0 |
|------|:-----:|:-----:|
| Total files | 31 | 42 |
| Knowledge modules | 9 | 12 |
| SKILL.md lines | 11,169 | 11,277 |
| 64-hexagram display | Concise list | 64-hexagram full table + symbols |
| Diagnostic formulas | Scattered in body | Standalone quick-ref file, 966 lines |
| Lecture modules | 0 | 3 (Fuyang + Zhongjing + Stanford) |
---
#### v2.1.0 (2026-06-08) — Six-Meridian Diagnostic Formulas

**Core upgrade**: Upgraded from a knowledge-base query tool into a clinical diagnostic assistant with a Six-Meridian differentiation thinking model.

**New content**:
- **8 diagnostic formulas**: Taiyang / Yangming / Shaoyang / Taiyin / Shaoyin / Jueyin / Shaoyin heat-transformation / concurrent-combined disease, each with IF-THEN differentiation rules + subtype discrimination table + representative formulas
- **Rapid diagnostic flowchart**: complete decision tree from patient symptoms to Six-Meridian location
- **Pulse quick reference**: 8 single pulses + 8 combined pulse images
- **Tongue quick reference**: 5 tongue appearances + 6 combined tongue appearances + pulse-tongue contradiction decision tree
- **True-cold-false-heat / false-cold discrimination**: eight-dimension method (facial color / mouth-nose breath / tongue shape / pulse / chest-abdomen / urine / thirst / stool) + critical-syndrome warnings
- **Concurrent/combined disease quick reference**: 11 combinations + treatment sequencing principles
- **Seven-step differentiation thinking model**: determine exterior-interior → separate yin-yang → distinguish cold-heat → judge transmission → assess constitution → select formula → fine-add-subtract
- **Medication iron rules**: 7 contraindications + 5 emergency plans
- **Jianzhong Tang series**: Xiao Jianzhong / Huangqi Jianzhong / Danggui Jianzhong / Da Jianzhong (Taiyin disease extension)
- **Three liver-methods**: Wumei Wan / Wuzhuyu Tang / Xiao Jianzhong Tang (Jingui core)
- **Bawei Shenqi Wan detailed**: three tonify three drain + Guifu Bawei Wan vs Liuwei Dihuang Wan
- **Jingui miscellaneous disease Six-Meridian attribution quick reference**: 12 miscellaneous diseases + representative formulas
- **Jingui-specific formula Six-Meridian attribution**: cough-asthma 4 formulas + deficiency-tonifying 8 formulas + joint pain 3 formulas (with full composition)
- **11 cross-references**: diagnostic formulas ↔ modules/ detailed treatise bidirectional links

**Data sources**:
- Ni Haixia's "Shanghan Lun Lecture" (Renji series)
- Ni Haixia's "Huangdi Neijing Lecture" (Renji series)
- Ni Haixia's "Jingui Yaolue Lecture" (Renji series)

**Quality validation**:
- Darwin skill score: 9.4/10
- 10 clinical scenario tests: 10/10 coverage
- 11 formula dosages checked formula-by-formula: 100% consistent with source files
- Six-Meridian outline treatise check: 5 of 6 fully consistent, 1 variant-character difference

**SKILL.md change**: +476 lines (10,697 → 11,169 lines), new lines 6097–6545

---

- **v2.0.1** (2026-05-26): Added categorized case library cases/ (245 cases) + research materials references/; fixed .gitignore
- **v2.0.0** (2026-05-25): Repository slimming — removed raw reference materials (110MB), kept only runtime-essential files (4MB)
- **v1.1.2** (2026-05-24): Detail page rewrite — added install tutorial, usage examples
- **v1.1.1** (2026-05-24): Renamed to "Ni Haixia Skill", slug changed to `nihaixia`
- **v1.1.0** (2026-05-23): Shennong Bencao Jing property system deeply distilled; keyword index fully optimized
- **v1.0.1** (2026-05-02): Structure optimized; OCR correction 13 places; added 10 Han Tang article highlights
- **v1.0.0** (2026-04-14): Initial release

</details>

---

## Acknowledgements

- Thanks to [huoyalong](https://github.com/huoyalong/nihaisha-skill) for providing the nihaisha-skill base framework
- Thanks to [9527qingfeng](https://github.com/9527qingfeng/hantang-nihaixia-follower) for providing case data support

---

## Star History

[![RepoStars](https://repostars.dev/api/embed?repo=jangviktor-web%2Fnihaixia&theme=grape)](https://repostars.dev/?repos=jangviktor-web%2Fnihaixia&theme=grape)

---


## Disclaimer

The content of this project is for TCM learning and research only, and does not replace professional medical diagnosis. Please always consult a licensed practitioner for any diagnosis or treatment.

---

<div align="center">

**Secondary development based on [nihaisha-skill](https://github.com/huoyalong/nihaisha-skill) · Licensed under MulanPSL-2.0 open-source license**

[![ClawHub](https://img.shields.io/badge/ClawHub-v2.1.0-orange)](https://clawhub.ai/jangviktor-web/skills/nihaixia)
[![OpenClawMP](https://img.shields.io/badge/OpenClawMP-v2.0.1-blueviolet)](https://openclawmp.cc)
[![SkillHub](https://img.shields.io/badge/SkillHub-nihaixia--pro-red)](https://skillhub.cloud.tencent.com/skills/nihaixia-pro)

</div>
