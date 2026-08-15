<div align="center">

<img width="120" src="logo.jpg" alt="Ni Haixia Skill Logo">

# Ni Haixia Skill · Classical-Formula TCM AI

**Injecting Master Ni Haixia's complete TCM (Traditional Chinese Medicine) reasoning system into an AI Agent**

`129 articles of Shang Han Lun` · `23 chapters of Jin Gui` · `71 chapters of Huang Di Nei Jing` · `345 herbs of Materia Medica` · `849 medical cases` · `2,452 pages of lecture notes` · `3.5M characters distilled`

[![GitHub Stars](https://img.shields.io/github/stars/jangviktor-web/nihaixia?style=for-the-badge&color=yellow&label=Stars)](https://github.com/jangviktor-web/nihaixia/stargazers)
[![Version](https://img.shields.io/badge/version-v2.1.0-blue?style=for-the-badge)](https://github.com/jangviktor-web/nihaixia/releases)
[![TCM Mind Distiller](https://img.shields.io/badge/TCM_Mind_Distiller-v4.4.0-red?style=for-the-badge)](https://github.com/jangviktor-web/tcm-distiller)
[![License](https://img.shields.io/badge/license-MulanPSL--2.0-green?style=for-the-badge)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Ready-orange?style=for-the-badge&logo=anthropic&logoColor=white)]()
[![Platforms](https://img.shields.io/badge/platforms-5-purple?style=for-the-badge)](#installation)

**🌐 [中文](https://github.com/jangviktor-web/nihaixia/blob/main/README.md) | [English](https://github.com/jangviktor-web/nihaixia/blob/main/README_EN.MD)**

</div>

---

> "Chinese medicine is very simple — it is nothing but yin-yang, qi, and blood. Once you understand it, one insight unlocks all." — Ni Haixia

### One-Line Introduction

Distilling Ni Haixia's (1954–2012) TCM thinking, the *Ren Ji* ("Human Meridian") teaching series, clinical insights, and the *Tian Ji* ("Heavenly Meridian") destiny studies into an activatable Agent Skill, enabling AI to perform Six-Meridian syndrome differentiation, select classical formulas, and interpret symptoms from Ni Haixia's perspective.

**Direct activation keywords**: `Ni Haixia` / `Haixia's perspective` / `Master Ni` / `classical-formula thinking` / `how would Ni Haixia see this`

---

## Quick Installation

<details open>
<summary><b> ClawHub (recommended) — updated to V2.3.0; you can copy the text below into your agent to update</b></summary>

```bash

openclaw skills install @jangviktor-web/nihaixia
npx skills add https://clawhub.ai/jangviktor-web/skills/nihaixia

```
</details>

<details>
<summary><b>SkillHub (Tencent Cloud) — updated to V2.3.0; you can copy the text below into your agent to update</b></summary>

```bash

Please install @user_ff4d9420/nihaixia-pro according to https://skillhub.cn/install/skillhub.md.

```
</details>

<details>
<summary><b>Manual Installation</b></summary>

```bash

# Manual
git clone https://github.com/jangviktor-web/nihaixia.git
cp -r nihaixia/ ~/.claude/skills/nihaixia/
Install the GitHub project "https://github.com/jangviktor-web/nihaixia" as a local skill.

```
</details>

<details>
<summary><b>Mobile (Tencent IMA App) (V2.3.0 has no skill-update channel on this platform yet; we have contacted the platform for follow-up. You can first send the Tencent SkillHub command to IMA Copilot to update — a tutorial is below)</b></summary>

### Download the older version directly from the imaSkill store

<img width="2200"  alt="03" src="https://github.com/user-attachments/assets/de39de98-60d2-40a5-ae1a-2a5ca55b693d" />

Ni Haixia skill Tencent IMA address: https://ima.qq.com/skill?shareId=70e35c8a24ed4c01a0986f9e3c83f3d1&from=share

### How to invoke:

<img width="3000"  alt="1000013924" src="https://github.com/user-attachments/assets/79ac68b1-cf18-47fe-ab32-1f876c5394f9" />
<img width="3000"  alt="1000013923" src="https://github.com/user-attachments/assets/9746a3b0-fd37-49e2-8a3a-0d72a06a765a" />

### How to update Tencent IMA to V2.3.0:

<img width="2411" height="1339" alt="01" src="https://github.com/user-attachments/assets/43e5f9b6-2eda-476b-9752-212780f271a2" />
<img width="1808" height="1339" alt="02" src="https://github.com/user-attachments/assets/74a2a813-2d68-40ba-a200-dee07d7cb661" />

</details>

<details>
<summary><b>Historical Version Downloads</b></summary>

#### v1.0.0 (Changelog: first stable release, built on a secondary open-source project, fully distilling the core content of Ni Haixia's *Ren Ji* series.)
Download: https://ghproxy.net/https://github.com/jangviktor-web/nihaixia/archive/refs/tags/v1.0.0.zip
#### v1.1.0 (Changelog: deep distillation of Shen Nong's Materia Medica property system, Shang Han Lun, and Jin Gui Yao Lue, plus full-module retrieval-link fixes)
Download: https://ghproxy.net/https://github.com/jangviktor-web/nihaixia/archive/refs/tags/v1.1.0.zip
#### v2.0.1 (Changelog: added 245 medical cases indexed by disease)
Download: https://ghproxy.net/https://github.com/jangviktor-web/nihaixia/archive/refs/tags/v2.0.1.zip
#### v2.1.0 (Changelog: upgraded from a knowledge-base query tool into a clinical diagnostic assistant with a Six-Meridian syndrome-differentiation reasoning mode)
Download: https://ghproxy.net/https://github.com/jangviktor-web/nihaixia/archive/refs/tags/v2.1.0.zip
#### v2.2.0 (Changelog: core upgrade — added a structured quick-reference layer and three important Master Ni lectures; SKILL.md entry embedded six quick-reference blocks including the opening-closing-pivoting diagram, the complete Yuan-primary-point table, and the Five-Shu-point formulas; the Sixty-Four Hexagrams were upgraded from a concise list into a complete encyclopedia of human-affairs applications)
Download: https://ghproxy.net/https://github.com/jangviktor-web/nihaixia/archive/refs/tags/V2.2.0.zip
#### V2.2.1 (Changelog: index system restructured)
Download: https://ghproxy.net/https://github.com/jangviktor-web/nihaixia/archive/refs/tags/V2.2.1.zip

</details>

---

## Feature Matrix

| Capability | Coverage | Description |
|:---|:---:|:---|
| Six-Meridian Differentiation | ✅ | Taiyang/Yangming/Shaoyang/Taiyin/Shaoyin/Jueyin, transmission rules + optimal resolution times |
| **Six-Meridian Diagnostic Formulas** | ✅ | **8 diagnostic formulas + rapid-diagnosis flowchart + pulse/tongue quick-reference + seven-step thinking model (added in v2.1.0)** |
| Classical Formula Selection | ✅ | 129 articles of Shang Han Lun + 23 chapters of Jin Gui, including composition/dosage/decoction method/contraindications |
| Herb Properties | ✅ | 345 herbs from Shen Nong's Materia Medica, three-grade classification + five flavors and meridian tropism + processing essentials |
| Clinical Cases | ✅ | 849 of Master Ni's real cases, categorized into 6 groups: cancer / cardiovascular / metabolic disease, etc. |
| Acupuncture Points | ✅ | Twelve meridians + Jing-Rong-Yu-Jing-He (Well-Spring-Transport-Channel-Sea) + key Ren and Du points + stroke first aid |
| Huang Di Nei Jing | ✅ | 71 chapters fully distilled, the core of TCM basic theory |
| Tian Ji Destiny Studies | ✅ | Zi Wei Dou Shu (Purple Star Astrology) + I Ching Sixty-Four Hexagrams + Yang House Feng Shui |
| Liang Dong Dialogue | ✅ | Full distillation of the 7 episodes from 2009, views on modern topics |
| 3rd Forum on Supporting Yang Speech | ✅ | Supporting-Yang theory / yin-deficiency → yang-deficiency → yin-excess transmission chain / major clinical cases of lupus, leukemia, brain tumors / categorized use of raw aconite and raw sulfur |
| Zhongjing's Heart Method Lecture | ✅ | Classical-formula dosology / Gui Zhi Tang as the ancestor of the cinnamon group / progression from Fang Feng Gan Fu Tang → Zhi Mu Tang → Wu Tou Tang / correspondence of digestive-system classical formulas / breast milk is menstruation · seven cancers share one origin / palm-back-and-forehead temperature difference for instant yin-yang hand diagnosis |
| Stanford University Speech + Disciples' Experience | ✅ | Treating from the common cold all the way to cancer / three steps to enter classical formulas / records of disciples Li Zong'en and Yang Zhen / summary of inspection diagnosis + ten questions for diagnosis / common tender points / special formulas for gallstones and kidney stones |
| Closed-Door Lectures | ✅ | 7 major critical-illness topics + 7 disciples' lessons, covering leukemia / breast cancer / brain tumors, etc. |
| Oral Expression | ✅ | Module for Ni Haixia's spoken style, making replies "sound like" Master Ni |

---

## Usage Examples

**Cold Damage Differentiation**
> **Q**: I've caught a cold — I'm averse to cold, have no sweat, and my neck hurts at the back.
> **A**: Taiyang cold damage, Ma Huang Tang (Ephedra Decoction) pattern. No sweat, aversion to cold, body pain — cold is binding at the exterior. Ma Huang opens the pores, Gui Zhi relieves the muscles, Xing Ren descends qi.

**Formula Query**
> **Q**: When is Xiao Chai Hu Tang (Minor Bupleurum Decoction) used?
> **A**: The master formula for Shaoyang disease. Bitter mouth, dry throat, dizzy vision, alternating chills and fever — seeing even one sign is sufficient.

**Herb Properties**
> **Q**: What is the difference between raw aconite and prepared aconite?
> **A**: Raw aconite — cold in the interior, the Si Ni (cold-extremities) pattern. Prepared aconite — unconsolidated exterior yang, sweating and aversion to wind.

**Case Reference**
> **Q**: Are there any liver-cancer cases?
> **A**: Yes, 147 cancer cases. Liver-cancer cases commonly use attacking/breaking formulas combined with soothing-liver and regulating-qi approaches.

---

## Core Knowledge System

### Six-Meridian Quick Reference

```
Taiyang (exterior) → Yangming (interior heat) → Shaoyang (half-exterior-half-interior)
         ↓ mistreatment / missed treatment
Taiyin (spleen cold) → Shaoyin (heart-kidney yang deficiency) → Jueyin (yin-yang reversal / upper heat lower cold)
```

### Ni's Six Health Standards

1. Sleep through the night until dawn, no insomnia
2. Normal appetite, feeling full and hungry at the three meals
3. Daily morning bowel movement
4. 5–7 urinations per day, pale clear yellow
5. Cool head and face, warm hands and feet (all year round)
6. Morning erection response

---

## Demonstration

<div align="center">

**Basic Application of Six-Meridian Differentiation**
<img width="729" alt="1" src="https://github.com/user-attachments/assets/5d874838-9339-40cd-ae47-70c153c9c57a" />

**Six-Meridian Transmission Rules**
<img width="729"  alt="2" src="https://github.com/user-attachments/assets/79c5c8fc-2894-4ecf-8988-42fa0dd354d6" />

**Daily Health Preservation and Dietary Contraindications**
<img width="729" alt="3" src="https://github.com/user-attachments/assets/70a37746-0d15-4839-aab4-f5fe0e37b8f6" />

</div>

---

## Related Projects

<div align="center">

### [Han Tang Chinese Medicine · Android Diagnostic App](https://github.com/jangviktor-web/nihaixia-app)

Same knowledge base, a standalone Android app. Works offline, completely free.

[![Download APK](https://img.shields.io/badge/download-APK-green?style=for-the-badge&logo=android)](https://github.com/jangviktor-web/nihaixia-app/releases/latest)
[![GitHub](https://img.shields.io/badge/GitHub-Repo-blue?style=for-the-badge)](https://github.com/jangviktor-web/nihaixia-app)

| Six-Meridian Diagnosis | 271-Formula Quick Reference | 345-Herb Quick Reference | Midnight-Noon Ebb-Flow Point Selection |
|:---:|:---:|:---:|:---:|
| Intelligent Consultation Guidance | Search + Six-Meridian Filter | Flavor/Meridian Classification | 361-Point Time Calculation |

</div>

<div align="center">

### [Li Ke Skill · Critical-Illness TCM AI](https://github.com/jangviktor-web/likeskill)

The thinking operating system of Master Li Ke (1930–2013) for acute and critical illnesses. 395 medical cases, 170+ formulas, 92 symptom-routing rules, 25 false-syndrome identifications.

Complements the Ni Haixia skill: Ni Haixia covers full-scope teaching (849 cases), while Li Ke focuses on acute/critical real-world combat (aconite up to 750g max).

[![GitHub](https://img.shields.io/badge/GitHub-Repo-blue?style=flat-square&logo=github)](https://github.com/jangviktor-web/likeskill)
[![ClawHub](https://img.shields.io/badge/ClawHub-install%20like-green?style=flat-square)](https://clawhub.ai/jangviktor-web/skills/like)

| Po Ge Jiu Xin Tang (Breaking-Formula Rescue-Heart Decoction) | 25 False-Syndrome Identifications | Circular-Motion Theory | Classical-Formula Dosology System |
|:---:|:---:|:---:|:---:|
| Aconite 30–750g | 24+ false-yang + 1 false-yin | Full distillation of Peng Ziyi | Han dynasty 1 liang = 15.625g |

</div>

<div align="center">

### [Hu Xishu Skill · Classical-Formula TCM AI](https://github.com/jangviktor-web/huxishu)

Distilling Hu Xishu's (1898–1984) clinical classical-formula thinking, the Six-Meridian-Eight-Principle differentiation system, and the formula-syndrome-correspondence method into an activatable Agent Skill, enabling AI to perform Six-Meridian differentiation, formula-syndrome discrimination, and clinical formula selection from Hu Xishu's perspective.

Hu Xishu is hailed as "the foremost transmitter of the classical formulas." His insight that "the Six Meridians arise from the Eight Principles" is the clearest interpretation of the Shang Han Lun differentiation system, directly influencing contemporary classical-formula masters such as Feng Shilun.

Complements the Ni Haixia skill: Ni Haixia covers full-scope teaching (849 cases), while Hu Xishu is the foremost transmitter of the classical formulas and offers the clearest interpretation of the Shang Han Lun differentiation system.

[![GitHub](https://img.shields.io/badge/GitHub-Repo-blue?style=flat-square&logo=github)](https://github.com/jangviktor-web/huxishu)
[![ClawHub](https://img.shields.io/badge/ClawHub-install%20huxishu-green?style=flat-square)](https://clawhub.ai/jangviktor-web/skills/huxishu)

</div>

<div align="center">

### [Wu Jutong Skill (Warm Disease School) · Warm-Disease TCM AI](https://github.com/jangviktor-web/wujutong)
**Wu Jutong** (1758–1836) — the great synthesizer of the Warm Disease School, with Triple-Energizer differentiation + Defense-Qi-Nutrient-Blood, 359 cases across 45 disease patterns, who called his work "the wings of Shang Han Lun." Centered on "the presence or absence of body fluids," he forbade sweating in warm disease, preserved fluids with sweet-cold herbs, and prioritized protecting yin.

| Dimension | Ni Haixia (Classical Formulas) | Wu Jutong (Warm Disease School) |
|------|--------------|--------------|
| **Differentiation** | Six Meridians (depth) | Triple Energizer (location) |
| **Core Treatment** | Expel the pathogen outward | Preserve body fluids |
| **Sweating Method** | Sweat when appropriate | Sweating forbidden in warm disease |
| **Formulas** | Few herbs, focused power (Ma Huang / Fu Zi / Wu Tou) | Many herbs, broad coverage (Yin Qiao / Bai Hu / Fu Mai) |
| **Cases** | 849 cases, full scope | 359 cases, warm disease + miscellaneous |

**Complementary relationship**: Ni Haixia fixes the faucet (warms yang, transforms dampness, treats the root); Wu Jutong clears the standing water (clears dampness, protects fluids, treats the branch) — one vertical, one horizontal. Use Wu in the acute phase, Ni in the remission phase; together they reveal the full picture of external-contraction disease in TCM.

[![GitHub](https://img.shields.io/badge/GitHub-Repo-blue?style=flat-square&logo=github)](https://github.com/jangviktor-web/wujutong)
[![ClawHub](https://img.shields.io/badge/ClawHub-install%20wujutong-green?style=flat-square)](https://clawhub.ai/jangviktor-web/skills/wujutong)

</div>


## Data Sources

<details>
<summary><b>Click to view the complete data-source list (10 lecture sets, 2,452 pages)</b></summary>

| Lecture Set | Pages | Extracted Characters | Status |
|---|---|---|---|
| Shang Han Lun Lecture Notes | 209 pp | 277K | Fully distilled |
| Jin Gui Yao Lue Lecture Notes | 419 pp | 626K | Fully distilled |
| Huang Di Nei Jing Lecture Notes | 461 pp | 227K | Fully distilled |
| Acupuncture Course Lecture Notes | 216 pp | 347K | Fully distilled |
| Shen Nong's Materia Medica Manuscript | 339 pp | 843K | Fully distilled |
| Tian Ji Dao (Zi Wei Dou Shu) | 75 pp | 85K | Fully distilled |
| Ren Jian Dao (I Ching) | 146 pp | 164K | Fully distilled |
| Di Mai Dao (Feng Shui) | 65 pp | 52K | Fully distilled |
| Han Tang Article Collection | 383 pp | 670K | 10 articles distilled |
| Ni Haixia Collected Works | 139 pp | 234K | 8 cases distilled |
| **Total** | **2,452 pp** | **3.5M** | |

</details>

<details>
<summary><b>Click to view the repository directory structure</b></summary>

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

## Changelog


#### v2.3.0 (2026-08-15) — Full dosology correction + expression restoration + classical-formula card system + rigor-first differentiation

Core upgrade: completed full error-correction of 258 formulas' dosages and solidified the three-system unit conversion; fixed the academic-style drift in new outputs (restoring Master Ni's flavor); launched the classical-formula article-card system and moved it to the must-read zone before answering; added the rigor-first differentiation rule plus card version labels and a Chinese-numeral anti-confusion mechanism. All changes re-reviewed with no regressions.

Changes:

#### Dosology System Full Correction (08-13)

- Cross-checked all 258 formulas ingredient-by-ingredient against source files (Ren Ji Shang Han Lun 5,174 lines / Jin Gui Yao Lue 8,920 lines), extracting ancient original formulas + Master Ni's clinical dosages in 5 batches
- Fixed 5 P0 hard errors at the module layer (Ju Pi Zhu Ru Tang / Da Huang Fu Zi Tang / Chai Hu Gui Jiang Tang / Gua Lou Xie Bai Ban Xia Tang / She Gan Ma Huang Tang), added 16 P2 dosages, added 7 P3 unlisted formulas
- Solidified the iron rule of direct conversion "1 ancient liang = 1 clinical qian"; archaeological conversion demoted to reference-only for original-formula scale
- Rewrote the six-major-cold-damage quick-reference table into 4 columns (main symptom / ancient formula / clinical), fully corrected all 6 formulas; noted Tao Hua Tang dual versions

#### Expression Fidelity Fix (08-14)

- SKILL.md 14b position-numbering-structure iron rules + expression_style three paradigms (complete answer / consultative back-and-forth / banter)
- Unbanned Master Ni-style redundancy, digression, and anti-Western-medicine intensity; deprecated the outdated 03 expression DNA
- Suan Zao Ren Tang: Chuan Xiong 2 liang → Xiong Qiong 1 liang; dosage authorization spectrum distinguishes original-text instances from clinical tiers

#### Full Clinical-Dosage Completion (08-14b)

- Classical-formula article-card spec (source + original formula + 3 clinical lines; clinical lines never omitted; per-ingredient independent judgment of oral / converted / conventional)
- Full clinical-dosage completion for 249 formulas (references/distilled/05, 06 two tables); only Xing Zi Tang lacks a source in the whole library
- Chai Hu Jia Long Gu Mu Li Tang confirmed without Huang Qin is a version difference, not a missing herb; Xiao Zhong Kui Jian Tang added

#### Formula Card Timing Advance + Session-Level Assertion Deduplication (08-15a)

- Quick-reference card ⑧ mandatory output moved to the must-read-before-answer zone; four-check mechanism; card reconciliation (body formula count = card count)
- Session-level assertion deduplication (9-phrase pool rotation, ≥3 rounds gap when pool exhausted); R1–R8 all repaired and landed
- Fixed a quote-escaping typo in the assertion pool

#### Rigor-First Differentiation + Card Version Labels + Number Anti-Confusion (08-15b)

- Rigor-first differentiation takes priority over style rules (Six-Meridian location → key follow-up questions → similar-pattern discrimination → formula-syndrome matching; wrong differentiation means rewriting the whole answer)
- "What do you readers think?" reduced to ≤1 per answer, not mandatory, only as a natural rhetorical question after a story
- Card version labels (Master Ni's lecture version / Jin Gui version / Song-edition, choose one of three); Chinese numerals never converted to Arabic (to avoid being mistaken for Song-edition Article N)
- Da Cheng Qi Tang Song-edition correspondence corrected to 208 (originally mislabeled ~220)

Verification: 30 open-consultation questions vs. 30 wins 0 losses; 5 retests 7/7 all green; 9-dimension review 90.0 vs. old 67.1 (+22.9).

| Capability Dimension | v2.2.0 | v2.3.0 |
| -------- | :----: | :--------------------: |
| Classical-formula article-card system | None | Yes (14c spec + quick-ref card ⑧ advanced) |
| Clinical dosage coverage | Not full | 258 formulas corrected + 249 formulas clinical-complete |
| Expression restoration paradigm | None | 3 paradigms (complete answer / consultative / banter) |
| Rigor-first differentiation rule | None | Yes (14b prioritized over style) |
| Assertion deduplication | None | Session-level 9-phrase pool |
| Chinese-numeral anti-confusion | None | Yes (lecture numbers preserved as-is) |
| Card version labels | None | Yes (lecture / Jin Gui / Song-edition) |

<details>
<summary><b>Click to expand the full changelog</b></summary>

#### v2.2.0 (2026-08-12) — Knowledge-base distillation quick-reference + three Master Ni lectures + full I Ching Sixty-Four Hexagram upgrade

Core upgrade: added a structured quick-reference layer and three important Master Ni lectures; SKILL.md entry embedded six quick-reference blocks including the opening-closing-pivoting diagram, the complete Yuan-primary-point table, and the Five-Shu-point formulas; the Sixty-Four Hexagrams were upgraded from a concise list into a complete encyclopedia of human-affairs applications.

New content:

#### Distillation Quick-Reference Layer (references/distilled/, 6 files, 232KB)
- Six-Meridian diagnostic formulas: 8 formulas + rapid-diagnosis flowchart + pulse/tongue quick-reference + combined/double-disease quick-reference + true-cold-false-heat discrimination + seven-step differentiation thinking model (966 lines)
- Acupuncture formula quick-reference: midnight-noon ebb-flow mnemonic + complete twelve-meridian Yuan-primary-point table + Five-Shu-point attribute rules + mother-son tonify-drain formulas (621 lines)
- Six-major-cold-damage classical-formula manual: Gui Zhi Tang / Ma Huang Tang / Ge Gen Tang / Da Qing Long Tang / Xiao Qing Long Tang / Xiao Chai Hu Tang — main symptoms + dosage + contraindications (150 lines)
- Acupuncture highlights compilation: key Ren and Du points + twelve-meridian points + selected acupuncture treatments (1,761 lines)
- Teaching/verification report: deep-distillation knowledge base 42 articles vs. existing skill four-dimension sampling comparison conclusions

#### Three Important Master Ni Lectures (modules/10-12, 28KB)
- 3rd Forum on Supporting Yang speech (2009.10): Supporting-Yang theory / yin-deficiency → yang-deficiency → yin-excess transmission chain / major clinical cases of lupus, leukemia, brain tumors / categorized use of raw aconite and raw sulfur (182 lines)
- Zhongjing's Heart Method lecture (2009.12): classical-formula dosology / Gui Zhi Tang as ancestor of the cinnamon group / Fang Feng Gan Fu Tang → Zhi Mu Tang → Wu Tou Tang progression / digestive-system classical-formula correspondence / breast milk is menstruation · seven-cancers-one-origin / palm-back-and-forehead temperature difference for instant yin-yang hand diagnosis (218 lines)
- Stanford University speech + disciples' experience (2010.09): treating from the common cold all the way to cancer / three steps to enter classical formulas / records of disciples Li Zong'en and Yang Zhen / inspection-diagnosis summary + ten diagnostic questions / common tender points / special formulas for gallstones and kidney stones (185 lines)

#### SKILL.md Entry Quick-Reference Upgrade (+130 lines)
- Opening-closing-pivoting master diagram: three yang (Taiyang opens → Shaoyang pivots → Yangming closes) + three yin (Taiyin opens → Shaoyin pivots → Jueyin closes) ASCII visualization
- Two great Shang Han Lun deficiency-tonifying formulas iron rule: Xiao Jian Zhong Tang (exterior-yang deficiency, Taiyang with Taiyin) + Zhi Gan Cao Tang (interior-yin deficiency, Shaoyin yin-yang dual deficiency)
- Complete twelve-meridian Yuan-primary-point table: 12 meridians × time-period × five-elements × Yuan point + mnemonic "Lung at Yin, Large Intestine at Mao, Stomach at Chen..."
- Five-Shu-point formulas: Jing-Rong-Yu-Jing-He × yin/yang meridian five elements + treatment-principle mnemonics
- Six-major-cold-damage quick-reference: key main symptoms + core dosage in one diagram
- Material path index: 9-file line-count / applicable-scenario quick-reference table

#### modules/09 Sixty-Four Hexagrams Full Upgrade
- Original concise list → complete structured table: 64 hexagrams × 4 columns (sequence · name · hexagram symbol · human-affairs application)
- Added dedicated Di Tian Tai hexagram chapter: hexagram-virtue explanation + 6 core human-affairs interpretations (Tai and Pi are a single thought apart / embracing openness to govern Tai / the teacher's way of Tai / Zhuge Liang's three visits / mother-in-law and daughter-in-law way / four phrases on discerning capacity) + Yang-house application (wife resides in northwest corner) + divination diagram + Master Ni's golden quotes
- Added I Ching general introduction: the I Ching is not a fortune-telling book, but a guide to the human way of avoiding the petty and following the gentleman

#### Teaching/Verification Enhancement
- Sampled comparison dimension-by-dimension against the deep-distillation knowledge base coverage (Shang Han / Jin Gui / Nei Jing / acupuncture / diagnostic formulas / clinical experience)
- Conclusion: existing skill covers 95% of facts, no major conflicts; added opening-closing-pivoting visualization / two great deficiency-tonifying-formula summary / seven-step thinking model / true-cold-false-heat discrimination
- Keyword index added 3 sections: Supporting-Yang Forum / cancer clinical, Zhongjing's Heart Method, Stanford speech

| Metric | v2.1.0 | v2.2.0 |
|------|:-----:|:-----:|
| Total files | 31 | 42 |
| Knowledge modules | 9 | 12 |
| SKILL.md lines | 11,169 | 11,277 |
| Sixty-Four Hexagrams display | Concise list | Full 64-hexagram table + hexagram symbols |
| Diagnostic formulas | Scattered in body | Standalone quick-ref file 966 lines |
| Lecture modules | 0 | 3 (Supporting-Yang + Zhongjing + Stanford) |
---
#### v2.1.0 (2026-06-08) — Six-Meridian Diagnostic Formulas

**Core upgrade**: upgraded from a knowledge-base query tool into a clinical diagnostic assistant with a Six-Meridian syndrome-differentiation reasoning mode.

**New content**:
- **8 diagnostic formulas**: Taiyang / Yangming / Shaoyang / Taiyin / Shaoyin / Jueyin / Shaoyin heat-transformation / combined-double disease, each with IF-THEN differentiation rules + typing-discrimination table + representative formula
- **Rapid-diagnosis flowchart**: complete decision tree from patient symptoms to Six-Meridian location
- **Pulse quick-reference**: 8 single pulses + 8 composite pulse images
- **Tongue quick-reference**: 5 tongue appearances + 6 composite tongues + pulse-tongue contradiction decision tree
- **True-cold-false-heat / false-cold discrimination**: eight-dimension method (facial color / mouth-nose breath / tongue shape / pulse / chest-abdomen / urine / thirst / stool) + critical-symptom warnings
- **Combined/double disease quick-reference**: 11 combinations + treatment sequence principles
- **Seven-step differentiation thinking model**: locate exterior-interior → separate yin-yang → discriminate cold-heat → judge transmission → assess constitution → select formula → refine modifications
- **Medication iron rules**: 7 contraindications + 5 emergency plans
- **Jian Zhong Tang series**: Xiao Jian Zhong / Huang Qi Jian Zhong / Dang Gui Jian Zhong / Da Jian Zhong (Taiyin disease extension)
- **Three liver-treating methods**: Wu Mei Wan / Wu Zhu Yu Tang / Xiao Jian Zhong Tang (Jin Gui core)
- **Ba Wei Shen Qi Wan detailed**: three supplements + three drains + Gui Fu Ba Wei Wan vs. Liu Wei Di Huang Wan
- **Jin Gui miscellaneous-disease Six-Meridian attribution quick-reference**: 12 miscellaneous diseases + representative formulas
- **Jin Gui-specific formula Six-Meridian attribution**: 4 cough-asthma formulas + 8 deficiency-tonifying formulas + 3 joint-pain formulas (with full composition)
- **11 cross-references**: bidirectional links from diagnostic formulas → detailed modules/articles

**Data sources**:
- Ni Haixia's *Shang Han Lun Lecture Notes* (Ren Ji series)
- Ni Haixia's *Huang Di Nei Jing Lecture Notes* (Ren Ji series)
- Ni Haixia's *Jin Gui Yao Lue Lecture Notes* (Ren Ji series)

**Quality verification**:
- Darwin skill score: 9.4/10
- 10 clinical scenario tests: 10/10 coverage
- 11 formula dosages checked formula-by-formula: 100% consistent with source files
- Six-Meridian outline articles checked: 5 of 6 fully consistent, 1 with variant-character difference

**SKILL.md changes**: +476 lines (10,697 → 11,169 lines), new lines 6097–6545

---

- **v2.0.1** (2026-05-26): added categorized case library cases/ (245 cases) + research materials references/; fixed .gitignore
- **v2.0.0** (2026-05-25): repository slimmed — removed raw reference materials (110MB), keeping only runtime-essential files (4MB)
- **v1.1.2** (2026-05-24): detail page rewritten — added installation tutorial, usage examples
- **v1.1.1** (2026-05-24): renamed to "Ni Haixia skill", slug changed to `nihaixia`
- **v1.1.0** (2026-05-23): deep distillation of Shen Nong's Materia Medica property system; keyword index fully optimized
- **v1.0.1** (2026-05-02): structural optimization; 13 OCR corrections; added 10 Han Tang article highlights
- **v1.0.0** (2026-04-14): initial release

</details>

---

## Acknowledgments

- Thanks to [huoyalong](https://github.com/huoyalong/nihaisha-skill) for providing the nihaisha-skill base framework
- Thanks to [9527qingfeng](https://github.com/9527qingfeng/hantang-nihaixia-follower) for providing medical-case data support

---

## Star History

[![RepoStars](https://repostars.dev/api/embed?repo=jangviktor-web%2Fnihaixia&theme=grape)](https://repostars.dev/?repos=jangviktor-web%2Fnihaixia&theme=grape)

---



## Disclaimer

The content of this project is for TCM learning and research only, and does not replace professional medical diagnosis. All diagnosis and treatment must be consulted with a licensed practitioner.

---


<div align="center">

**Secondary development based on [nihaisha-skill](https://github.com/huoyalong/nihaisha-skill) · Licensed under the MulanPSL-2.0 open-source license**

[![ClawHub](https://img.shields.io/badge/ClawHub-v2.1.0-orange)](https://clawhub.ai/jangviktor-web/skills/nihaixia)
[![OpenClawMP](https://img.shields.io/badge/OpenClawMP-v2.0.1-blueviolet)](https://openclawmp.cc)
[![SkillHub](https://img.shields.io/badge/SkillHub-nihaixia--pro-red)](https://skillhub.cloud.tencent.com/skills/nihaixia-pro)

</div>
