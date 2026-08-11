<div align="center">

<img width="120" src="logo.jpg" alt="Ni Haixia skill Logo">

**🌐 [中文](https://github.com/jangviktor-web/nihaixia/blob/StableV2026.5.23/README.MD) | [English](https://github.com/jangviktor-web/nihaixia/blob/StableV2026.5.23/README_EN.MD)**

# Ni Haixia skill · Classical Formula TCM AI

**Inject Master Ni Haixia's complete TCM thinking system into AI Agent**

`129 Tiaos of Shanghan Lun` · `23 Chapters of Jingui` · `71 Chapters of Huangdi Neijing` · `345 Herbs` · `849 Medical Cases` · `2,452 Pages of Lectures` · `3.5M Words of Essence`

[![GitHub Stars](https://img.shields.io/github/stars/jangviktor-web/nihaixia?style=for-the-badge&color=yellow&label=Stars)](https://github.com/jangviktor-web/nihaixia/stargazers)
[![Version](https://img.shields.io/badge/Version-v2.1.0-blue?style=for-the-badge)](https://github.com/jangviktor-web/nihaixia/releases)
[![License](https://img.shields.io/badge/License-MulanPSL--2.0-green?style=for-the-badge)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Ready-orange?style=for-the-badge&logo=anthropic&logoColor=white)]()
[![Platforms](https://img.shields.io/badge/Platforms-5-purple?style=for-the-badge)](#installation)

[English](#english) · 中文

</div>

---

> "TCM is very simple—it's all about yin, yang, qi, and blood. Once you understand that, everything falls into place." — Ni Haixia

### One-Sentence Introduction

Distill Ni Haixia's (1954-2012) TCM thinking, Renji series teachings, clinical insights, and Tianji metaphysics into an activatable Agent Skill, enabling AI to view diagnosis through Ni Haixia's lens—performing Six-Meridian Pattern Differentiation, selecting classical formulas, and interpreting symptoms.

**Direct Activation Keywords**: `Ni Haixia` / `Haixia Perspective` / `Master Ni` / `Classical Formula Thinking` / `What would Ni Haixia say`

---

## Quick Installation

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
<summary><b>OpenClaw / OpenClawMP / Manual Installation</b></summary>

```bash
# OpenClaw
openclaw skills install @jangviktor-web/nihaixia

# Manual
git clone https://github.com/jangviktor-web/nihaixia.git
cp -r nihaixia/ ~/.claude/skills/nihaixia/
```

</details>

<details>
<summary><b>Mobile (Tencent IMA APP)</b></summary>

Download Tencent IMA APP, scan the knowledge code below, and use it directly without any configuration.

<img width="200" alt="【Ni Haixia】Knowledge Code" src="https://github.com/user-attachments/assets/fb4fb05c-fc21-41fe-941e-c820ec16b750" />

Ni Haixia skill Tencent IMA link: https://ima.qq.com/skill?shareId=70e35c8a24ed4c01a0986f9e3c83f3d1&from=share

How to invoke:
<img width="3085" alt="1000013924" src="https://github.com/user-attachments/assets/79ac68b1-cf18-47fe-ab32-1f876c5394f9" />
<img width="3085" alt="1000013923" src="https://github.com/user-attachments/assets/9746a3b0-fd37-49e2-8a3a-0d72a06a765a" />

</details>

---

Feature Matrix

Capability Coverage Description
Six-Meridian Pattern Differentiation ✅ Taiyang/Yangming/Shaoyang/Taiyin/Shaoyin/Jueyin, transmission patterns + optimal recovery times
Six-Meridian Diagnosis Formulas ✅ 8 diagnostic formulas + quick diagnosis flowchart + pulse/tongue quick reference + 7-step thinking model (new in v2.1.0)
Classical Formula Selection ✅ 129 Tiaos of Shanghan Lun + 23 chapters of Jingui, including composition/dosage/decoction methods/contraindications
Herbal Properties & Tastes ✅ 345 herbs from Shennong Bencao Jing, 3-grade classification + five tastes and meridian tropism + processing essentials
Clinical Cases ✅ 849 real Ni Haixia cases, categorized into 6 groups including cancer/cardiovascular/metabolic diseases
Acupuncture Points ✅ Twelve meridians + Jing-Rong-Shu-Jing-He points + Ren/Du vital points + stroke first aid
Huangdi Neijing ✅ Complete distillation of 71 chapters, core TCM foundational theory
Tianji Metaphysics ✅ Ziwei Doushu + 64 hexagrams of I Ching + Yangzhai Fengshui
Liang Dong Dialogues ✅ Complete distillation of 7 episodes from 2009 recordings, perspectives on modern topics
Closed-Door Sessions ✅ 7 major severe disease topics + 7 disciple classes, covering leukemia/breast cancer/brain tumors etc.
Oral Expression ✅ Ni Haixia's spoken style module, making responses sound "like" Master Ni

---

Usage Examples

Cold Pattern Differentiation

Q: I have a cold, feel chills, no sweating, and pain at the back of my neck
A: Taiyang cold damage, Mahuang Tang pattern. No sweat, chills, body pain—cold constrains the exterior. Mahuang opens the pores, Guizhi relieves the muscles, Xingren descends the qi.

Formula Inquiry

Q: When is Xiao Chaihu Tang used?
A: The primary formula for Shaoyang disease. Bitter taste in the mouth, dry throat, dizziness, alternating fever and chills—any one symptom is sufficient.

Herbal Properties

Q: What's the difference between raw Fuzi and prepared Fuzi?
A: Raw Fuzi—internal yin cold, Sini patterns. Prepared Fuzi—exterior yang insecurity, sweating and aversion to wind.

Case Reference

Q: Do you have any liver cancer cases?
A: Yes, 147 cancer cases. Liver cancer cases often use formula combinations targeting masses, combined with soothing the liver and regulating qi.

---

Core Knowledge System

Six-Meridian Pattern Differentiation Quick Reference

```
Taiyang (exterior) → Yangming (interior heat) → Shaoyang (half-exterior half-interior)
              ↓ Improper treatment
Taiyin (spleen cold) → Shaoyin (heart/kidney yang deficiency) → Jueyin (yin-yang chaos / upper heat lower cold)
```

Ni's Six Health Criteria

1. Sleep through the night without insomnia
2. Normal appetite, hunger and fullness at proper mealtimes
3. Daily morning bowel movement
4. Urination 5-7 times per day, pale clear yellow
5. Head and face cool, hands and feet warm (throughout the year)
6. Morning yang response (men) / normal menstrual cycle (women)

---

Demonstration

<div align="center">

Six-Meridian Pattern Differentiation Basic Application
<img width="729" alt="Six-Meridian Differentiation" src="https://github.com/user-attachments/assets/98af88a7-fbaa-4a50-ac63-7f10e8c61dbe" />

Six-Meridian Transmission Patterns
<img width="726" alt="Six-Meridian Transmission" src="https://github.com/user-attachments/assets/af0fb0c1-944b-4846-8dc2-4aaa2bc5b531" />

Daily Health & Dietary Contraindications
<img width="731" alt="Dietary Health" src="https://github.com/user-attachments/assets/7c252c14-9497-4a94-be31-4a9670df3afb" />

</div>

---

## Related Projects

<div align="center">

### [Han‑Tang Chinese Medicine · Android Diagnosis APP](https://github.com/jangviktor-web/nihaixia-app)

Same knowledge base, standalone Android application. Offline‑capable, completely free.

[![Download APK](https://img.shields.io/badge/Download-APK-green?style=for-the-badge&logo=android)](https://github.com/jangviktor-web/nihaixia-app/releases/latest)
[![GitHub](https://img.shields.io/badge/GitHub-Repo-blue?style=for-the-badge)](https://github.com/jangviktor-web/nihaixia-app)

| Six‑Meridian Pattern Differentiation | 271 Formula Quick Lookup | 345 Medicinal Herb Quick Lookup | Midnight‑Noon Ebb‑Flow Acupoint Selection |
|:---:|:---:|:---:|:---:|
| Guided Intelligent Inquiry | Search + Six‑Meridian Filter | Nature, Flavor & Channel Tropism Classification | Time Calculation for 361 Acupoints |

</div>

### [Li Ke Skill · Critical & Emergency TCM AI](https://github.com/jangviktor-web/likeskill)

Critical‑care clinical thinking system of senior TCM physician Li Ke (1930‑2013). 395 medical cases, 170+ formulas, 92 symptom routing rules, 25 false‑pattern identification rules.

Complementary to Ni Haixia Skill: Ni Haixia covers general clinical teaching (849 medical cases), while Li Ke focuses on critical‑emergency real‑world practice (Aconitum carmichaelii up to 750g).

[![GitHub](https://img.shields.io/badge/GitHub-Repo-blue?style=flat-square&logo=github)](https://github.com/jangviktor-web/likeskill)
[![ClawHub](https://img.shields.io/badge/ClawHub-install%20like-green?style=flat-square)](https://clawhub.ai/jangviktor-web/skills/like)

| Po‑Ge Jiu‑Xin Decoction | 25 False‑Pattern Identifications | Circular Movement Theory | Classical Prescription Dosage System |
|:---:|:---:|:---:|:---:|
| Aconitum 30‑750g | 24 False‑Yang Patterns + 1 False‑Yin Pattern | Complete distillation of Peng Ziyi’s works | 1 Han liang = 15.625g |

</div>

### [Hu Xishu Skill · Classical Prescription TCM AI](https://github.com/jangviktor-web/huxishu)

Distills Hu Xishu’s (1898‑1984) classical‑prescription clinical thinking, six‑meridian & eight‑outline pattern differentiation framework, and formula‑pattern correspondence methodology into an activatable Agent Skill. Enables AI to perform six‑meridian differentiation, formula‑pattern discrimination and clinical formula selection from Hu Xishu’s perspective.

Hu Xishu is honored as "the foremost inheritor of classical prescriptions". His insight that "Six meridians originate from eight outlines" delivers the clearest interpretation of *Shang Han Lun* pattern‑differentiation system, and has directly influenced contemporary classical‑prescription masters including Feng Shilun.

Complementary to Ni Haixia Skill: Ni Haixia provides comprehensive general‑practice teaching (849 cases), whereas Hu Xishu offers the definitive reading of *Shang Han Lun* classical‑prescription pattern differentiation.

[![GitHub](https://img.shields.io/badge/GitHub-Repo-blue?style=flat-square&logo=github)](https://github.com/jangviktor-web/huxishu)
[![ClawHub](https://img.shields.io/badge/ClawHub-install%20huxishu-green?style=flat-square)](https://clawhub.ai/jangviktor-web/skills/huxishu)

</div>

### [Wu Jutong Skill · Warm‑Disease School TCM AI](https://github.com/jangviktor-web/wujutong)
**Wu Jutong** (1758‑1836) — Grand synthesist of the Warm‑Disease School. Triple‑Jiao pattern differentiation + Wei‑Qi‑Ying‑Xue theory. 359 medical cases covering 45 disease entities. He described his work as "complementing *Shang Han Lun*", centering on "preservation or consumption of body fluids". Core principles: Warm diseases forbid diaphoresis; sweet‑cold therapy preserves fluids; yin protection takes priority.

| Dimension | Ni Haixia (Classical Prescriptions) | Wu Jutong (Warm‑Disease School) |
|------|--------------|--------------|
| **Pattern Differentiation** | Six meridians (assessing disease depth) | Triple‑Jiao (assessing disease location) |
| **Core Therapeutic Principle** | Expel pathogenic factors outward | Preserve body fluids |
| **Diaphoretic Method** | Apply sweating when indicated | Diaphoresis contraindicated for warm diseases |
| **Formulas** | Few ingredients, potent effect (Ephedra / Aconitum / Aconitum kusnezoffii) | Multi‑ingredient broad‑spectrum formulas (Yinqiao San / Baihu Tang / Fumai Decoction) |
| **Medical Cases** | 849 cases covering general medicine | 359 cases for warm diseases & miscellaneous disorders |

**Complementary Relationship**: Ni Haixia repairs the water tap (warming yang & resolving dampness to treat root causes), Wu Jutong drains accumulated floodwater (clearing dampness & protecting fluids to treat manifestations). One vertical, one horizontal. Adopt Wu Jutong for acute‑phase conditions, Ni Haixia for remission‑phase management. Combined, they yield a full picture of TCM exogenous disease theory.

[![GitHub](https://img.shields.io/badge/GitHub-Repo-blue?style=flat-square&logo=github)](https://github.com/jangviktor-web/wujutong)
[![ClawHub](https://img.shields.io/badge/ClawHub-install%20wujutong-green?style=flat-square)](https://clawhub.ai/jangviktor-web/skills/wujutong)

</div>

## Data Sources

<details>
<summary><b>Click to expand full data‑source inventory (10 lecture manuscripts, 2,452 pages)</b></summary>

| Manuscript | Pages | Extracted Characters | Status |
|---|---|---|---|
| *Shang Han Lun* Lecture Notes | 209 pages | 277K | Fully distilled |
| *Jin Gui Yao Lue* Lecture Notes | 419 pages | 626K | Fully distilled |
| *Huang Di Nei Jing* Lecture Notes | 461 pages | 227K | Fully distilled |
| Acupuncture & Moxibustion Tutorial | 216 pages | 347K | Fully distilled |
| *Shen Nong Ben Cao Jing* Manuscript | 339 pages | 843K | Fully distilled |
| *Tian Ji Dao* (Zi Wei Dou Shu Astrology) | 75 pages | 85K | Fully distilled |
| *Ren Jian Dao* (I‑Ching) | 146 pages | 164K | Fully distilled |
| *Di Mai Dao* (Feng‑Shui) | 65 pages | 52K | Fully distilled |
| Han‑Tang Collected Articles | 383 pages | 670K | 10 articles distilled |
| Ni Haixia Collected Works | 139 pages | 234K | 8 medical cases distilled |
| **Total** | **2,452 pages** | **3.5M** | |

</details>

<details>
<summary><b>Click to view repository directory structure</b></summary>

nihaixia/
├── SKILL.md                    # Main skill file (840K, directly readable by Claude)
├── modules/                    # 9 knowledge modules
│   ├── 01_shanghan_sun.md      # Shang Han Lun Taiyang chapter
│   ├── 02_shanghan_other.md    # Remaining five chapters of Shang Han Lun
│   ├── 03_yian.md              # Medical case collection (849 cases)
│   ├── 04_jingui.md            # Jin Gui Yao Lue
│   ├── 05_huangdi_neijing.md   # Huang Di Nei Jing
│   ├── 06_liangdong.md         # Liang‑Dong interview transcripts
│   ├── 07_bimen_hantang.md     # Closed‑door lectures & Han‑Tang clinic materials
│   ├── 08_huangdi_detail.md    # Annotated Huang Di Nei Jing
│   └── 09_zhenjiu_bencao.md    # Acupuncture‑Moxibustion + Shen Nong Ben Cao Jing
├── cases/                      # Categorized medical cases (245 cases)
│   ├── 01_cancer.md            # 147 cancer cases
│   ├── 02_cardiovascular.md    # 22 cardiovascular disorder cases
│   ├── 03_metabolic.md         # 12 metabolic disorder cases
│   ├── 04_autoimmune.md        # 2 autoimmune disorder cases
│   ├── 05_neurological.md      # 3 neurological & psychiatric cases
│   └── 06_other.md             # 59 miscellaneous cases
└── references/research/        # Research reference materials

</details>

---

## Changelog

<details>
<summary><b>Click to expand complete changelog</b></summary>

#### v2.1.0 (2026‑06‑08) — Six‑Meridian Pattern‑Differentiation Diagnostic Formulas

**Core Upgrade**: Upgraded from knowledge‑base query tool to clinical diagnostic assistant equipped with six‑meridian pattern‑differentiation reasoning.

**New Additions**:
- **8 diagnostic formulas**: Taiyang / Yangming / Shaoyang / Taiyin / Shaoyin / Jueyin / Shaoyin heat‑transformation / combined & concurrent disease patterns. Each includes IF‑THEN pattern‑differentiation rules, subtype discrimination tables and representative formulas.
- **Rapid‑diagnosis flowchart**: Complete decision tree mapping patient symptoms to six‑meridian localization.
- **Pulse quick reference**: 8 single pulses + 8 composite pulse conditions.
- **Tongue quick reference**: 5 tongue manifestations + 6 composite tongue presentations + decision tree for pulse‑tongue contradiction resolution.
- **True‑cold false‑heat / false‑cold discrimination**: Eight‑dimensional evaluation (complexion / nasal‑oral exhalation / tongue form / pulse / chest‑abdomen temperature / urine / thirst / stool) + critical‑condition warnings.
- **Combined / concurrent disease quick reference**: 11 pattern combinations plus therapeutic priority principles.
- **Seven‑step pattern‑differentiation workflow**: Exterior‑interior determination → yin‑yang classification → cold‑heat discrimination → transmission‑transformation assessment → constitution evaluation → formula selection → fine‑tuned modification.
- **Medication iron‑rules**: 7 contraindications + 5 first‑aid protocols.
- **Jianzhong Decoction series**: Xiao Jianzhong / Huangqi Jianzhong / Danggui Jianzhong / Da Jianzhong (Taiyin disease expansion).
- **Three liver‑treatment methods**: Wumei Wan / Wuzhuyu Tang / Xiao Jianzhong Tang (core of *Jin Gui Yao Lue*).
- **Detailed explanation of Ba Wei Shen Qi Wan**: Three‑tonify three‑drain framework + comparison between Gui‑Fu Ba Wei Wan and Liu Wei Di Huang Wan.
- **Quick mapping for miscellaneous disorders in *Jin Gui Yao Lue* to six meridians**: 12 miscellaneous disorders plus representative formulas.
- **Six‑meridian attribution for unique *Jin Gui Yao Lue* formulas**: 4 cough‑asthma formulas + 8 tonifying formulas + 3 bi‑syndrome formulas (full ingredient composition included).
- **11 cross‑references**: Bidirectional links from diagnostic formulas to detailed articles under `modules/`.

**Data Sources**:
- Ni Haixia *Shang Han Lun Lecture Notes* (Ren‑Ji Series)
- Ni Haixia *Huang Di Nei Jing Lecture Notes* (Ren‑Ji Series)
- Ni Haixia *Jin Gui Yao Lue Lecture Notes* (Ren‑Ji Series)

**Quality Validation**:
- Darwin Skill Score: 9.4/10
- 10 clinical‑scenario tests: 10/10 coverage
- Dosage cross‑check for 11 formulas: 100% consistency against source documents
- Six‑meridian outline clause verification: 5 out of 6 exact matches, 1 variant‑character discrepancy.

**SKILL.md Changes**: +476 lines (10,697 → 11,169 lines), newly added lines 6097‑6545.

---

- **v2.0.1** (2026‑05‑26): Added categorized medical‑case library `cases/` (245 cases) + research materials `references/`; fixed `.gitignore`.
- **v2.0.0** (2026‑05‑25): Repository refactoring — removed raw reference assets (110 MB), retaining only runtime‑required files (4 MB).
- **v1.1.2** (2026‑05‑24): Rewrote documentation pages; added installation guide and usage examples.
- **v1.1.1** (2026‑05‑24): Renamed to "Ni Haixia Skill", slug updated to `nihaixia`.
- **v1.1.0** (2026‑05‑23): In‑depth distillation of *Shen Nong Ben Cao Jing* medicinal property system; comprehensive keyword‑index optimization.
- **v1.0.1** (2026‑05‑02): Structural optimization; OCR correction for 13 entries; added 10 selected Han‑Tang articles.
- **v1.0.0** (2026‑04‑14): Initial release.

</details>

---

## Acknowledgements

- Thanks to [huoyalong](https://github.com/huoyalong/nihaisha-skill) for the base framework of `nihaisha‑skill`.
- Thanks to [9527qingfeng](https://github.com/9527qingfeng/hantang-nihaixia-follower) for medical‑case dataset support.

---

## Star History

[![RepoStars](https://repostars.dev/api/embed?repo=jangviktor-web%2Fnihaixia&theme=grape)](https://repostars.dev/?repos=jangviktor-web%2Fnihaixia&theme=grape)

---

## Disclaimer

This project is intended solely for traditional Chinese‑medicine study and research. It does not replace professional medical diagnosis. For all diagnosis and treatment please consult a licensed medical practitioner.

---

<div align="center">

**Secondary development based on [nihaisha‑skill](https://github.com/huoyalong/nihaisha-skill) · Licensed under MulanPSL‑2.0 open‑source license**

[![ClawHub](https://img.shields.io/badge/ClawHub-v2.1.0-orange)](https://clawhub.ai/jangviktor-web/skills/nihaixia)
[![OpenClawMP](https://img.shields.io/badge/OpenClawMP-v2.0.1-blueviolet)](https://openclawmp.cc)
[![SkillHub](https://img.shields.io/badge/SkillHub-nihaixia--pro-red)](https://skillhub.cloud.tencent.com/skills/nihaixia-pro)

</div>
