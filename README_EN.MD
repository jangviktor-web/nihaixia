<div align="center">

<img width="120" src="logo.jpg" alt="Ni Haixia skill Logo">

**🌐 [中文](https://github.com/jangviktor-web/nihaixia/README.md) | [English](https://github.com/jangviktor-web/nihaixia/README_EN.MD)**

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

Related Projects

<div align="center">

Han-Tang TCM · Android Diagnosis APP

Same knowledge base, standalone Android application. Offline capable, completely free.

https://img.shields.io/badge/Download-APK-green?style=for-the-badge&logo=android
https://img.shields.io/badge/GitHub-Repo-blue?style=for-the-badge

Six-Meridian Diagnosis 271 Formulas Quick Reference 345 Herbs Quick Reference Ziwu Liuzhu Point Selection
Smart Diagnostic Guidance Search + Six-Meridian Filter Properties & Meridian Classification 361 Points + Time Calculation

</div>

Li Ke skill · Critical Care TCM AI

Li Ke (1930-2013) critical and severe condition thinking system. 395 medical cases, 170+ formulas, 92 symptom routing, 25 false pattern identifications.

Complements Ni Haixia skill: Ni Haixia covers comprehensive teaching (849 cases), Li Ke focuses on critical care practice (Fuzi up to 750g).

https://img.shields.io/badge/GitHub-Repo-blue?style=flat-square&logo=github
https://img.shields.io/badge/ClawHub-install%20like-green?style=flat-square

Pojie Jiuxin Tang 25 False Pattern Identifications Circular Motion Theory Classical Formula Dosage System
Fuzi 30-750g 24 False Yang + 1 False Yin Complete Peng Ziyi Distillation Han Dynasty 1 Liang = 15.625g

</div>

Hu Xishu skill · Classical Formula TCM AI

Distill Hu Xishu's (1898-1984) classical formula clinical thinking, Six-Meridian Eight-Principle differentiation system, and formula-pattern correspondence into an activatable Agent Skill, enabling AI to perform Six-Meridian differentiation, formula differentiation, and clinical formula selection through Hu Xishu's lens.

Hu Xishu is hailed as "the foremost transmitter of classical formulas." His groundbreaking insight that "Six Meridians originate from the Eight Principles" provides the clearest interpretation of the differentiation system in Shanghan Lun, directly influencing contemporary classical formula masters like Feng Shilun.

Complements Ni Haixia skill: Ni Haixia covers comprehensive teaching (849 cases), while Hu Xishu offers the clearest systematic interpretation of Shanghan Lun.

https://img.shields.io/badge/GitHub-Repo-blue?style=flat-square&logo=github
https://img.shields.io/badge/ClawHub-install%20huxishu-green?style=flat-square

</div>

Wenbing School Wu Jutong skill · Wenbing TCM AI

Wu Jutong (1758-1836)—the great synthesizer of the Warm Disease school, Triple Burner differentiation + Wei-Qi-Ying-Xue system. 359 medical cases covering 45 conditions. He claimed to "supplement the wings of Shanghan Lun," with "preservation of bodily fluids" at the core. Warm diseases prohibit sweating, use sweet and cold herbs to preserve fluids, prioritizing yin protection.

Dimension Ni Haixia (Classical Formulas) Wu Jutong (Wenbing School)
Differentiation Six Meridians (depth) Triple Burner (location)
Treatment Core Expel pathogenic factors Preserve bodily fluids
Sweating Method Sweat when appropriate Sweating prohibited for warm diseases
Formulas Few herbs with focused power (Mahuang/Fuzi/Wutou) Many herbs with broad coverage (Yinqiao/Baihu/Fumai)
Cases 849 full-spectrum cases 359 warm disease + miscellaneous cases

Complementary Relationship: Ni Haixia fixes the faucet (warming yang and transforming dampness to treat the root), Wu Jutong sweeps up the water (clearing damp and protecting fluids to treat the branch)—one vertical, one horizontal. Follow Wu in acute phases, follow Ni in recovery phases; together they present the complete picture of externally-contracted diseases in TCM.

https://img.shields.io/badge/GitHub-Repo-blue?style=flat-square&logo=github
https://img.shields.io/badge/ClawHub-install%20wujutong-green?style=flat-square

</div>

Data Sources

<details>
<summary><b>Click to view complete data source list (10 lectures, 2,452 pages)</b></summary>

Lecture Pages Extracted Characters Status
Shanghan Lun Lecture 209 pages 277K Full distillation
Jingui Yaolüe Lecture 419 pages 626K Full distillation
Huangdi Neijing Lecture 461 pages 227K Full distillation
Acupuncture Lecture 216 pages 347K Full distillation
Shennong Bencao Jing 339 pages 843K Full distillation
Tianjidao (Ziwei Doushu) 75 pages 85K Full distillation
Renjiandao (I Ching) 146 pages 164K Full distillation
Dimaidao (Fengshui) 65 pages 52K Full distillation
Han-Tang Articles Collection 383 pages 670K 10 articles distilled
Ni Haixia Collected Works 139 pages 234K 8 cases distilled
Total 2,452 pages 3.5M 

</details>

<details>
<summary><b>Click to view repository directory structure</b></summary>

```
nihaixia/
├── SKILL.md                    # Main skill file (840K, read directly by Claude)
├── modules/                    # 9 knowledge modules
│   ├── 01_shanghan_sun.md      # Shanghan Lun Taiyang chapter
│   ├── 02_shanghan_other.md    # Shanghan Lun other five meridians
│   ├── 03_yian.md              # Medical case collection (849 cases)
│   ├── 04_jingui.md            # Jingui Yaolüe
│   ├── 05_huangdi_neijing.md   # Huangdi Neijing
│   ├── 06_liangdong.md         # Liang Dong dialogues
│   ├── 07_bimen_hantang.md     # Closed-door sessions + Han-Tang
│   ├── 08_huangdi_detail.md    # Huangdi Neijing detailed annotations
│   └── 09_zhenjiu_bencao.md    # Acupuncture + Shennong Bencao Jing
├── cases/                      # Categorized cases (245 cases)
│   ├── 01_cancer.md            # 147 cancer cases
│   ├── 02_cardiovascular.md    # 22 cardiovascular cases
│   ├── 03_metabolic.md         # 12 metabolic disease cases
│   ├── 04_autoimmune.md        # 2 autoimmune cases
│   ├── 05_neurological.md      # 3 neurological/psychiatric cases
│   └── 06_other.md             # 59 other cases
└── references/research/        # Research materials
```

</details>

---

Changelog

<details>
<summary><b>Click to expand full changelog</b></summary>

v2.1.0 (2026-06-08) — Six-Meridian Diagnosis Formulas

Core Upgrade: Evolved from a knowledge base query tool into a clinical diagnostic assistant equipped with Six-Meridian pattern differentiation thinking.

New Additions:

· 8 diagnostic formulas: Taiyang/Yangming/Shaoyang/Taiyin/Shaoyin/Jueyin/Shaoyin heat transformation/combined and overlapping patterns, each with IF-THEN differentiation rules + subtype differentiation tables + representative formulas
· Quick diagnosis flowchart: Complete decision tree from patient symptoms to Six-Meridian localization
· Pulse diagnosis quick reference: 8 single pulses + 8 combined pulse patterns
· Tongue diagnosis quick reference: 5 tongue patterns + 6 combined tongue patterns + pulse-tongue contradiction decision tree
· True cold false heat / false cold differentiation: 8-dimensional method (facial color/breath odor/tongue shape/pulse/chest-abdomen/urine/thirst/stool) + critical pattern warnings
· Combined/overlapping patterns quick reference: 11 combinations + treatment priority principles
· 7-step diagnostic thinking model: Determine exterior-interior → differentiate yin-yang → distinguish cold-heat → assess transmission → evaluate constitution → select formula → fine-tune modifications
· Medication iron rules: 7 contraindications + 5 emergency protocols
· Jianzhong Tang series: Xiao Jianzhong/Huangqi Jianzhong/Danggui Jianzhong/Da Jianzhong (Taiyin disease expansion)
· Three methods for treating liver: Wumei Wan/Wuzhuyu Tang/Xiao Jianzhong Tang (Jingui core)
· Bawei Shenqi Wan detailed explanation: Three tonifying + three draining + Guifu Bawei vs Liuwei Dihuang
· Jingui miscellaneous diseases Six-Meridian attribution quick reference: 12 conditions + representative formulas
· Jingui unique formulas Six-Meridian attribution: 4 cough/asthma formulas + 8 tonification formulas + 3 arthralgia formulas (with complete composition)
· 11 cross-references: Diagnostic formulas ↔ detailed provisions in modules/

Data Sources:

· Ni Haixia, Shanghan Lun Lecture (Renji Series)
· Ni Haixia, Huangdi Neijing Lecture (Renji Series)
· Ni Haixia, Jingui Yaolüe Lecture (Renji Series)

Quality Validation:

· Darwin skill score: 9.4/10
· 10 clinical scenario tests: 10/10 coverage
· 11 formula dosages verified individually: 100% consistent with source files
· Six-Meridian outline provisions verified: 5 of 6 fully consistent, 1 variant character difference

SKILL.md changes: +476 lines (10,697→11,169 lines), new lines 6097-6545

---

· v2.0.1 (2026-05-26): Added categorized case library cases/ (245 cases) + research materials references/; fixed .gitignore
· v2.0.0 (2026-05-25): Repository cleanup—removed original reference materials (110MB), kept only runtime essentials (4MB)
· v1.1.2 (2026-05-24): Details page rewrite—added installation guide, usage examples
· v1.1.1 (2026-05-24): Renamed to "Ni Haixia skill," slug changed to nihaixia
· v1.1.0 (2026-05-23): Deep distillation of Shennong Bencao Jing herbal properties; comprehensive keyword index optimization
· v1.0.1 (2026-05-02): Structural optimization; OCR correction of 13 entries; added 10 Han-Tang article essences
· v1.0.0 (2026-04-14): Initial release

</details>

---

Acknowledgements

· Thanks to huoyalong for providing the nihaisha-skill foundational framework
· Thanks to 9527qingfeng for medical case data support

---

Star History

https://repostars.dev/api/embed?repo=jangviktor-web%2Fnihaixia&theme=grape

---

Disclaimer

This project is for TCM learning and research purposes only. It is not a substitute for professional medical diagnosis. All medical consultations should be conducted with licensed practitioners.

---

<div align="center">

Forked from nihaisha-skill · Licensed under MulanPSL-2.0

https://img.shields.io/badge/ClawHub-v2.1.0-orange
https://img.shields.io/badge/OpenClawMP-v2.0.1-blueviolet
https://img.shields.io/badge/SkillHub-nihaixia--pro-red

</div>