<div align="center">

<img width="120" src="logo.jpg" alt="倪海厦skill Logo">

# 倪海厦Skill · 经方中医AI

**将经方大师倪海厦的完整中医思维体系注入 AI Agent**

`129条伤寒论` · `23篇金匮` · `72篇黄帝内经` · `神农本草经374种本草（上137/中110/下127）` · `1257 例结构化医案 + 243 例叙事医案` · `2,452页讲义` · `3.5M字精萃`

[![GitHub Stars](https://img.shields.io/github/stars/jangviktor-web/nihaixia?style=for-the-badge&color=yellow&label=Stars)](https://github.com/jangviktor-web/nihaixia/stargazers)
[![版本](https://img.shields.io/badge/版本-v2.3.1-blue?style=for-the-badge)](https://github.com/jangviktor-web/nihaixia/releases)
[![中医思维蒸馏器](https://img.shields.io/badge/中医思维蒸馏器-v4.4.0-red?style=for-the-badge)](https://github.com/jangviktor-web/tcm-distiller)
[![License](https://img.shields.io/badge/协议-MulanPSL--2.0-green?style=for-the-badge)](LICENSE)
[![Agent Skills Standard](https://img.shields.io/badge/Agent%20Skills%20Standard-Ready-orange?style=for-the-badge&logo=openai&logoColor=white)]()
[![Multi-Runtime](https://img.shields.io/badge/Multi--Runtime-5个-purple?style=for-the-badge)](#安装)

**🌐 [中文](https://github.com/jangviktor-web/nihaixia/blob/main/README.md) | [English](https://github.com/jangviktor-web/nihaixia/blob/main/README_EN.MD)**

</div>

---

> 「中医很简单，就是阴阳气血。你搞懂了，一通百通。」—— 倪海厦

### 一句话介绍

将倪海厦（1954-2012）的中医思维、人纪系列教学、临床心法、天纪命理蒸馏为可激活的 Agent Skill，使 AI 能以倪海厦的视角进行六经辨证、经方选药、解读症状。

**直接激活词**：`倪海厦` / `海厦视角` / `倪师` / `经方思维` / `倪海厦会怎么看`

---

## 快速安装

<details open>
<summary><b> ClawHub（推荐）已更新至V2.2.0版本可复制下面文字到agent更新，V2.3.1 系统审核中 </b></summary>

```bash

openclaw skills install @jangviktor-web/nihaixia
npx skills add https://clawhub.ai/jangviktor-web/skills/nihaixia

```
</details>

<details>
<summary><b>SkillHub（腾讯云·推荐）已更新至V2.3.1版本可复制下面文字到agent更新</b></summary>

```bash

请根据 https://skillhub.cn/install/skillhub.md，安装 @user_ff4d9420/nihaixia-pro。

```
</details>

<details>
<summary><b>手动安装</b></summary>

```bash

# 手动
git clone https://github.com/jangviktor-web/nihaixia.git
cp -r nihaixia/ ~/.claude/skills/nihaixia/
把github“https://github.com/jangviktor-web/nihaixia”项目安装到本地skill

```
</details>

<details>
<summary><b>手机端（腾讯 IMA APP）（平台商场已更新至V2.3.1，直接到IMA SKILL 商场更新即可)</b></summary>

### 第一步 直接在imaSkill商店下载旧版

<img width="2200"  alt="03" src="https://github.com/user-attachments/assets/de39de98-60d2-40a5-ae1a-2a5ca55b693d" />

倪海厦skill腾讯ima地址： https://ima.qq.com/skill?shareId=70e35c8a24ed4c01a0986f9e3c83f3d1&from=share

### 第二步 调用方法：

<img width="3000"  alt="1000013924" src="https://github.com/user-attachments/assets/79ac68b1-cf18-47fe-ab32-1f876c5394f9" />
<img width="3000"  alt="1000013923" src="https://github.com/user-attachments/assets/9746a3b0-fd37-49e2-8a3a-0d72a06a765a" />

### 第三步 腾讯ima更新到V2.3.0方法（先复制腾讯SkillHub命令发给IMA Copilot更新）：
```bash
复制下面文字
请根据 https://skillhub.cn/install/skillhub.md，安装 @user_ff4d9420/nihaixia-pro。

```
<img width="2411" height="1339" alt="01" src="https://github.com/user-attachments/assets/43e5f9b6-2eda-476b-9752-212780f271a2" />
<img width="1808" height="1339" alt="02" src="https://github.com/user-attachments/assets/74a2a813-2d68-40ba-a200-dee07d7cb661" />

</details>

<details>
<summary><b>历史版本下载</b></summary>

#### v1.0.0  （更新日志：首个正式稳定版，基于开源项目二次开发，完整蒸馏倪海厦人纪系列核心内容。）
下载地址：https://ghproxy.net/https://github.com/jangviktor-web/nihaixia/archive/refs/tags/v1.0.0.zip
#### v1.1.0 （更新日志：神农本草经药性体系、伤寒论、金匮要略深度蒸馏 + 全模块检索链路修复）
下载地址：https://ghproxy.net/https://github.com/jangviktor-web/nihaixia/archive/refs/tags/v1.1.0.zip   
#### v2.0.1版本 （更新日志：更新245 例医案按疾病索引）
下载地址：https://ghproxy.net/https://github.com/jangviktor-web/nihaixia/archive/refs/tags/v2.0.1.zip   
#### v2.1.0版本 （更新日志：从知识库查询工具升级为具备六经辨证思维模式的临床诊断助手。）
下载地址：https://ghproxy.net/https://github.com/jangviktor-web/nihaixia/archive/refs/tags/v2.1.0.zip
#### v2.2.0版本  （更新日志：核心升级：新增结构化速查层与三场倪师重要演讲，SKILL.md 入口植入开阖枢图/原穴全表/五输穴公式等六大速查块，六十四卦从简洁列表升级为完整人事应用百科。）
下载地址：https://ghproxy.net/https://github.com/jangviktor-web/nihaixia/archive/refs/tags/V2.2.0.zip
#### V2.2.1版本  （更新日志：索引体系重构）
下载地址：https://ghproxy.net/https://github.com/jangviktor-web/nihaixia/archive/refs/tags/V2.2.1.zip
#### V2.2.2版本  （更新日志：完成伤寒金匮 258 方逐条剂量提取与两轮复核，修正通行本与倪师授课原版剂量偏差、模块硬错误、速查表错乱、源文件行号标注错误，整改勘误表自身误判漏判，提升方剂剂量原始数据准确率。）
下载地址：https://ghproxy.net/https://github.com/jangviktor-web/nihaixia/releases/download/V2.2.1/nihaixia_skill_20260813.V2.2.2tar.gz
#### V2.2.3版本  （更新日志：方剂数据补全、遗方增补与版本口径统一：批量补齐多方剂缺失的古代原方剂量、倪师临床剂量与规范方行，增补差后劳复、金匮附方共计7类未收录方剂并标注史料来源边界，统一处理全书多处方剂古今版本分歧，固化桃花汤等方剂的倪师标准解读口径，规范版本差异备注规则，仅保留5处源文件无记载遗留项。）
下载地址：https://ghproxy.net/https://github.com/jangviktor-web/nihaixia/releases/download/V2.2.1/nihaixia_skill_20260813_v2.2.3.tar.gz
#### V2.2.4版本  （更新日志：批量补齐缺失古方、临床剂量与方行文本，增补差后劳复、金匮附方遗方，统一多方剂版本分歧与解读口径；重构三套度量衡换算体系，固化倪师临床直换开方铁律，重写感冒经方速查表，厘清各换算体系使用边界，规避判定误判。）
下载地址：https://ghproxy.net/https://github.com/jangviktor-web/nihaixia/releases/download/V2.2.1/nihaixia_skill_20260813_v2.2.4.tar.gz
#### V2.2.8d版本 （更新日志：完成 7 处核心改动与 R1‑R8 补修，将经方条文卡片触发规则前移置顶，新增方剂出卡对账校验实现首次出现即出卡，落实会话级断言短语去重与断言池轮换，同步修正范例矛盾、触发口径、失效编号引用等细节，解决漏卡与模板复用缺陷。）
下载地址：https://ghproxy.net/https://github.com/jangviktor-web/nihaixia/releases/download/V2.3.0/nihaixia_skill_20260815_v2.2.8d.tar.gz
#### V2.3.0版本 （更新日志：完成 258 方剂量全量勘误与三体系换算固化；修复新版输出学术化问题（倪师味还原）；上线经方条文卡片体系并前移到回答前必读区；新增辨证严谨优先铁律与卡片版本标注、中文编号防混机制。）
下载地址：https://ghproxy.net/https://github.com/jangviktor-web/nihaixia/releases/download/V2.3.0/nihaixia_skill_20260815_v2.3.0.tar.gz
#### 🆕V2.3.1版本🆕 （更新日志：重构输出格式为 "优化版"—— 口语叙述为主体 + 表格 / 加粗标注重点，每答必达；置顶速查卡四查升级为八查并新增 ✅/❌ 双错误示范；固化表格完整性铁律（主证表症状逐条独立成行、涉方必出剂量对照、鉴别回归完整格式）
下载地址：https://ghproxy.net/https://github.com/jangviktor-web/nihaixia/releases/download/v2.3.1/nihaixia-2.3.1.zip

</details>


---

## 功能矩阵

| 能力 | 覆盖范围 | 说明 |
|:---|:---:|:---|
| 六经辨证 | ✅ | 太阳/阳明/少阳/太阴/少阴/厥阴，传变规律+欲解时 |
| **六经辨证诊断公式** | ✅ | **8个诊断公式+快速诊断流程图+脉舌速查+七步走思维模式（v2.1.0新增）** |
| 经方选药 | ✅ | 伤寒论129条+金匮23篇，含组成/剂量/煎服法/禁忌 |
| 药物性味 | ✅ | 神农本草经345种，三品分类+五味归经+炮制要点 |
| 临床医案 | ✅ | 849例倪师真实医案，按癌症/心血管/代谢病等6类分类 |
| 针灸穴位 | ✅ | 十二经络+井荣俞经合+任督要穴+中风急救 |
| 黄帝内经 | ✅ | 71篇完整蒸馏，中医基础理论核心 |
| 天纪命理 | ✅ | 紫微斗数+易经六十四卦+阳宅风水 |
| 梁冬对话 | ✅ | 2009年7期完整录音蒸馏，现代话题观点 |
|第三届扶阳论坛演讲|✅|扶阳理论/阴虚→阳虚→阴实传变链/红斑狼疮血癌脑瘤临床重案/生附子生硫黄分类应用|
|仲景心法讲授讲|✅|经方剂量学/桂枝汤群方之祖/风湿甘附汤→知母汤→乌头汤递进/消化系统经方对应/奶水即月经·七癌同源/掌背额温差秒断阴阳手诊法|
|斯坦福大学演讲 + 弟子经验|✅|从感冒一路治到癌症/经方入门三步走/李宗恩杨贞弟子实录/望诊总结+诊病十问/常用压痛点/胆肾结石专方|
| 闭门课 | ✅ | 7大重病专题+7堂弟子课，血癌/乳癌/脑瘤等 |
| 口述表达 | ✅ | 倪海厦口语风格模块，回复"像"倪师 |

---

## 使用示例

**感冒辨证**
> **Q**：我感冒了，怕冷，没有汗，脖子后面疼
> **A**：太阳伤寒，麻黄汤证。无汗恶寒、体痛——寒束于表。麻黄开毛孔，桂枝解肌，杏仁降气。

**方剂查询**
> **Q**：小柴胡汤什么时候用？
> **A**：少阳病主方。口苦、咽干、目眩、往来寒热——但见一证便是。

**药物性味**
> **Q**：生附子和炮附子区别？
> **A**：生附子——阴寒在里，四逆证。炮附子——表阳不固，汗出恶风。

**医案参考**
> **Q**：有没有肝癌的医案？
> **A**：有，147个癌症医案。肝癌案例常用攻坚处方配合疏肝理气。

---

## 核心知识体系

### 六经辨证速查

```
太阳（表）→ 阳明（里热）→ 少阳（半表半里）
         ↓ 失治误治
太阴（脾寒）→ 少阴（心肾阳虚）→ 厥阴（阴阳逆乱 / 上热下寒）
```

### 倪氏六健康标准

1. 一觉到天亮，无失眠
2. 胃口正常，三餐有饱饿感
3. 每天晨起大便
4. 一天小便 5-7 次，淡清黄色
5. 头面冷、手足温热（四季皆然）
6. 晨起阳反应

---

## 效果演示

<div align="center">

# 六经辨证基础应用
<img width="992" height="808" alt="图1_compressed" src="https://github.com/user-attachments/assets/791a3053-fc0e-4ea6-a4d5-a3d8a9f80b6e" />



# 六经传变规律
<img width="992" height="808" alt="图2_compressed" src="https://github.com/user-attachments/assets/314dabce-0554-4765-bf53-203e276d2813" />


# 日常养生与饮食禁忌
<img width="992" height="836" alt="图3_compressed" src="https://github.com/user-attachments/assets/e44968de-983e-458d-929f-6e90f63c6490" />

</div>

---

## 相关项目

<div align="center">

### [汉唐中医 · 安卓中医诊断命理玄学 APP](https://github.com/jangviktor-web/nihaixia-app)

同一个知识库，独立的安卓应用。离线可用，完全免费。

[![Download APK](https://img.shields.io/badge/下载-APK-green?style=for-the-badge&logo=android)](https://github.com/jangviktor-web/nihaixia-app/releases/latest)
[![GitHub](https://img.shields.io/badge/GitHub-Repo-blue?style=for-the-badge)](https://github.com/jangviktor-web/nihaixia-app)

| 六经辨证诊断 | 322 首方剂速查 | 448 味药物速查 | 408 穴针灸速查 |
|:---:|:---:|:---:|:---:|
| 智能问诊引导 | 搜索 + 六经筛选 | 性味归经分类 | 穴位 ↔ 处方互链 |

| 紫微斗数排盘 | 易经六十四卦 | 四柱命卦 | 穴位处方 · 透针 |
|:---:|:---:|:---:|:---:|
| 十二宫 / 四化 / 大限 | 起卦 + 64 卦讲义 | 先天 / 后天卦推算 | 257 方 + 31 透针 |

</div>

---

<div align="center">

### [中医思维蒸馏器 · TCM-Distiller](https://github.com/jangviktor-web/tcm-distiller)

中医思维蒸馏器TCM-Distiller是开源中医AI蒸馏流水线，不堆砌中医典籍素材，而是搭建标准化体系，把胡希恕、黄元御、吴鞠通等医家的著作、讲稿、医案，提炼成可被AI调用、还原真人辨证思路的专属思维技能。

[![Download APK](https://img.shields.io/badge/中医思维蒸馏器-v4.4.0-red?style=for-the-badge&logo=Skill)](https://github.com/jangviktor-web/tcm-distiller)
[![GitHub](https://img.shields.io/badge/GitHub-Repo-blue?style=for-the-badge)](https://github.com/jangviktor-web/tcm-distiller)

| 人物 | 流派 | 成果 |
|---|---|---|
| 胡希恕 | 经方派 | 38 万字讲稿 → 完整技能（首发验证案例） |
| 黄元御 | 气机升降派 | 3.5MB/38,266 行医书十一种 → V3 深度优化 |
| 吴鞠通 | 温病派 | 4 著作 → V3.5 端到端 + 359 医案 + GitHub 发布 |
| 倪海厦 | 经方派 | 258 方剂量全量勘误 + 表达还原度反超旧版 + 输出格式折中优化（V4.5 七项经验反哺） |

</div>

---

<div align="center">
         
### [李可skill · 急危重症中医AI](https://github.com/jangviktor-web/likeskill)

李可老中医（1930-2013）急危重症思维操作系统。395个医案、170+首方剂、92种症状路由、25种假证识别。

与倪海厦skill互补：倪海厦覆盖全科教学（849医案），李可专注急危重症实战（附子最大750g）。

[![GitHub](https://img.shields.io/badge/GitHub-Repo-blue?style=flat-square&logo=github)](https://github.com/jangviktor-web/likeskill)
[![ClawHub](https://img.shields.io/badge/ClawHub-install%20like-green?style=flat-square)](https://clawhub.ai/jangviktor-web/skills/like)

| 破格救心汤 | 假证识别25种 | 圆运动理论 | 经方剂量体系 |
|:---:|:---:|:---:|:---:|
| 附子30-750g | 假阳证24+假阴证1 | 彭子益完整蒸馏 | 汉代一两=15.625g |

</div>

---

<div align="center">

### [胡希恕skill · 经方中医AI](https://github.com/jangviktor-web/huxishu)

将胡希恕（1898-1984）的经方临床思维、六经八纲辨证体系、方证对应心法蒸馏为可激活的 Agent Skill，使 AI 能以胡希恕的视角进行六经辨证、方证鉴别、临床选方。

胡希恕被誉为"经方传道第一人"，其"六经来自八纲"的创见是对《伤寒论》辨证体系最清晰的解读，直接影响了冯世纶等当代经方名家。

与倪海厦skill互补：倪海厦覆盖全科教学（849医案），胡希恕是经方传道第一人，是对《伤寒论》辨证体系最清晰的解读。

[![GitHub](https://img.shields.io/badge/GitHub-Repo-blue?style=flat-square&logo=github)](https://github.com/jangviktor-web/huxishu)
[![ClawHub](https://img.shields.io/badge/ClawHub-install%20huxishu-green?style=flat-square)](https://clawhub.ai/jangviktor-web/skills/huxishu)

</div>

---

<div align="center">

### [温病派吴鞠通skill · 温病派中医AI](https://github.com/jangviktor-web/wujutong)
**吴鞠通**（1758-1836）——温病学派集大成者，三焦辨证 + 卫气营血，359 医案 45 病证，自称"羽翼伤寒"，以"津液的存亡"为核心，温病禁汗、甘寒存津，护阴第一。

| 维度 | 倪海厦（经方） | 吴鞠通（温病派） |
|------|--------------|--------------|
| **辨证** | 六经（看深浅） | 三焦（看部位） |
| **治法核心** | 驱邪外出 | 存津液 |
| **汗法** | 该汗则汗 | 温病禁汗 |
| **方剂** | 药少力专（麻黄/附子/乌头） | 药多面广（银翘/白虎/复脉） |
| **医案** | 849 案全科 | 359 案温病+杂病 |

**互补关系**：倪海厦修水龙头（温阳化湿治本），吴鞠通扫积水（清湿护津治标）——一纵一横，急性期从吴、缓解期从倪，合观乃得中医外感病全貌。

[![GitHub](https://img.shields.io/badge/GitHub-Repo-blue?style=flat-square&logo=github)](https://github.com/jangviktor-web/wujutong)
[![ClawHub](https://img.shields.io/badge/ClawHub-install%20wujutong-green?style=flat-square)](https://clawhub.ai/jangviktor-web/skills/wujutong)

</div>


## 数据来源

<details>
<summary><b>点击查看完整数据来源清单（10份讲义，2,452页）</b></summary>

| 讲义 | 页数 | 提取字符 | 状态 |
|---|---|---|---|
| 伤寒论讲义 | 209 页 | 277K | 全量蒸馏 |
| 金匮要略讲义 | 419 页 | 626K | 全量蒸馏 |
| 黄帝内经讲义 | 461 页 | 227K | 全量蒸馏 |
| 针灸教程讲义 | 216 页 | 347K | 全量蒸馏 |
| 神农本草经文稿 | 339 页 | 843K | 全量蒸馏 |
| 天机道（紫微斗数） | 75 页 | 85K | 全量蒸馏 |
| 人间道（易经） | 146 页 | 164K | 全量蒸馏 |
| 地脉道（风水） | 65 页 | 52K | 全量蒸馏 |
| 汉唐文章集锦 | 383 页 | 670K | 10 篇蒸馏 |
| 倪海厦文集 | 139 页 | 234K | 8 则医案蒸馏 |
| **合计** | **2,452 页** | **3.5M** | |



</details>

<details>
<summary><b>点击查看仓库目录结构</b></summary>

```
nihaixia/
├── SKILL.md                    # 主技能文件（107KB/1,548行，含开阖枢图/原穴全表等六大速查块+角色规则+剂量体系）
├── expression_style.md         # 倪海厦口语表达 DNA（嚎用法/反问互动/断言收束）
├── distilled_cases.md          # 243 例分类叙事医案合并版
├── index.html                  # 详情页
├── logo.jpg                    # 项目 Logo
├── modules/                    # 14 个知识模块
│   ├── 01_shanghan_sun.md      # 伤寒论太阳病篇（条文1-129 逐条解读）
│   ├── 02_shanghan_other.md    # 伤寒论阳明/少阳/太阴/少阴/厥阴
│   ├── 03_yian.md              # 医案集（849 例）
│   ├── 04_jingui.md            # 金匮要略 23 篇完整解读
│   ├── 05_huangdi_neijing.md   # 黄帝内经 72 篇 + 上古天真论
│   ├── 06_liangdong.md         # 梁冬对话全文
│   ├── 07_bimen_hantang.md     # 闭门课 + 汉唐文章
│   ├── 08_huangdi_detail.md    # 黄帝内经讲义详细篇目（461 页）
│   ├── 09_zhenjiu_bencao.md    # 针灸教程 + 神农本草经 374 种 + 天纪 + 六十四卦全表
│   ├── 10_fuyang_luntan.md     # 第三届扶阳论坛演讲（经方阴阳+癌症重案）
│   ├── 11_zhongjing_xinfa.md   # 仲景心法（剂量学+手诊+七癌同源）
│   ├── 12_stanford_jingfang.md # 斯坦福演讲+经方妙用+弟子经验
│   ├── 13_shanghan_quebing.md  # 伤寒论条文补齐（太阳下篇+阳明篇）
│   └── 14_yijinjing_bidu.md    # 易筋经 + 五脏逼毒法
├── cases/                      # 医案库（1,500+ 条）
│   ├── 00_merged_table.md      # 1,257 例全量结构化医案表（12列：诊断/病机/方剂/针灸/疗程/观点）
│   ├── 01_cancer.md            # 147 个癌症医案
│   ├── 02_cardiovascular.md    # 22 个心血管医案
│   ├── 03_metabolic.md         # 12 个代谢病医案
│   ├── 04_autoimmune.md        # 2 个自身免疫医案
│   ├── 05_neurological.md      # 3 个神经精神医案
│   └── 06_other.md             # 59 个其他医案
├── references/
│   ├── distilled/              # 蒸馏速查层（6 文件）
│   │   ├── 01-six-meridian-formulas.md # 六经辨证诊断公式（966 行）
│   │   ├── 02-acupuncture-quick-ref.md # 针灸公式速查（621 行）
│   │   ├── 03-clinical-experience.md   # 感冒六大经方 + 病机十九条（150 行）
│   │   ├── 04-acupuncture-highlights.md # 针灸重点内容汇编（1,761 行）
│   │   ├── README.md                   # 蒸馏目录说明
│   │   └── audit-notes.md              # 教验报告
│   ├── research/               # 研究资料（10 文件：著作/对话/表达DNA/外部评价/决策/时间线/教学法/临床案例/综合/蒸馏日志）
│   ├── audit/                  # 方剂与针灸审计清单（fangji_112.txt / zhenjiu_164.txt）
│   └── CHANGELOG.md            # 变更记录
```
</details>

---

## 更新日志


#### v2.3.1 (2026-08-19) — 输出格式优化版：重点好找 + 倪师口吻兼得

核心升级：根据用户反馈（"输出整段文字重点难找，希望像 v2.1.0 那样有格式区分"），重构输出格式规则为"折中版"——**口语叙述为主体 + 表格/加粗标注重点**，既保留倪师口吻温度，又让辨证结论、鉴别、剂量、禁忌一眼可找。所有改动经 3 独立评审盲测验证，零败绩。

改动内容：

#### 输出格式折中版（08-19a）
- 14b 由"禁止表格/编号"改为"折中版"：正文口语叙述是主体，**每答必达至少 1 个表格或加粗要点块**标注重点（主证表/剂量对照/⚠️注意），无则违规重写
- 置顶速查卡四查升级为**八查**：新增"表格必达""表格行全""辨证行模板""防重复"四项自检
- 新增✅/❌双错误示范："只有口语无表格/卡片=错误示范二"，正反双向锚定边界

#### 表格完整性铁律（08-19b）
- 吸收 v2.1.0"表格行全"优点并固化为显式规则：**主证表症状逐条独立成行**（禁止挤行合并，如"口渴引饮、脉洪大"必须拆两行，与知识库条目逐条对齐）
- 涉方必出剂量对照（药名+剂量逐味）；⚠️注意/禁忌加粗必达
- 鉴别改用 **v2.1.0 原生格式**：粗体"XX vs YY 的鉴别"标题 + 项目符号列表，不用表格（用户定稿）

#### 辨证行模板 + 防重复条款（08-19c）
- 辨证行统一模板：`**辨证：{证型}（{病机}·{方名}证）**`（如"**辨证：脏躁证（心神失养、脏阴不足·甘麦大枣汤证）**"）
- 防重复条款：同一要点只写一次，"**注意**：X"整句复制两遍=违规；倪师原话用括注并入一行
- README 运行时中立化：移除单一 runtime badge，改为 Agent Skills Standard + Multi-Runtime

验证：40+ 道经方辨证题（本地 10 + 联网 30+）双版本盲测，折中版 **100+ 比 0 全胜**；judge 一致评"口语开场+鉴别清单+断言收束+条文卡片"为必胜模板。

<details>
<summary><b>点击展开完整更新日志</b></summary>

#### v2.3.0 (2026-08-15) — 剂量全量勘误 + 表达还原 + 经方卡片体系 + 辨证严谨优先

核心升级：完成 258 方剂量全量勘误与三体系换算固化；修复新版输出学术化问题（倪师味还原）；上线经方条文卡片体系并前移到回答前必读区；新增辨证严谨优先铁律与卡片版本标注、中文编号防混机制。所有改动复查无负优化。

改动内容：

#### 剂量体系全量勘误（08-13）

- 258 方逐味对照源文件（人纪伤寒论 5174 行 / 金匮要略 8920 行），分 5 批提取古代原方 + 倪师临床剂量
- 修 P0 模块层硬错 5 处（橘皮竹茹汤 / 大黄附子汤 / 柴胡桂姜汤 / 栝蒌薤白半夏汤 / 射干麻黄汤）、补 P2 剂量 16 处、补 P3 未列方 7 方
- 固化「古方一两 = 临床一钱」直换铁律，考古换算降级为仅参考原方规模
- 感冒六大经方速查表重写为 4 列（主症 / 古方 / 临床），6 方全修；桃花汤双版本注

#### 表达还原度修复（08-14）

- SKILL.md 14b 禁定位 / 编号结构铁律 + expression_style 三范式（完整回答 / 问诊往返 / 调侃）
- 解禁倪师式冗余、跑题、骂西医强度；废弃过时 03 表达 DNA
- 酸枣仁汤芎䓖二两 → 芎藭一两；剂量授权谱区分原文实例与临床档位

#### 临床剂量全量补齐（08-14b）

- 经方条文卡片规范（出处 + 原方 + 临床三行，临床行永不省，逐味独立判定口述 / 换算 / 常例）
- 249 方临床剂量全量补齐（references/distilled/05、06 两表），全库仅杏子汤源阙
- 柴胡加龙骨牡蛎汤确认无黄芩为版本差异非缺药；消肿溃坚汤补录

#### 方剂卡时机前移 + 断言会话级去重（08-15a）

- 速查卡⑧卡片必出前移到回答前必读区；四查机制；出卡对账（正文方数 = 卡片数）
- 断言会话级去重（9 短语池轮换，池尽间隔 ≥3 轮）；R1–R8 补修全落地
- 修复断言池引号转义笔误

#### 辨证严谨优先 + 卡片版本标注 + 编号防混（08-15b）

- 辨证严谨优先于风格铁律（六经定位 → 关键追问 → 类证鉴别 → 方证对症，辨证错整答重写）
- 「读者认为呢」降频至每答 ≤1 处、非必达、仅故事讲完后自然反问
- 卡片标版本（倪师讲课版 / 金匮版 / 宋本三选一）；中文编号禁转阿拉伯（防误成宋本 N 条）
- 大承气宋本对应修正为 208（原标约 220 错误）

验证：30 题开放问诊对照 30 胜 0 输；5 题复测 7/7 全绿；9 维评审 90.0 vs 旧版 67.1（+22.9）。

| 能力维度     | v2.2.0 |         v2.3.0         |
| -------- | :----: | :--------------------: |
| 经方条文卡片体系 |    无   |   有（14c 规范 + 速查卡⑧前移）   |
| 临床剂量覆盖   |   未全量  |   258 方勘误 + 249 方临床全量  |
| 表达还原范式   |    无   | 3 范式（完整回答 / 问诊往返 / 调侃） |
| 辨证严谨铁律   |    无   |      有（14b 优先于风格）      |
| 断言去重     |    无   |        会话级 9 短语池       |
| 中文编号防混   |    无   |       有（讲课编号原样保留）      |
| 卡片版本标注   |    无   |    有（讲课版 / 金匮版 / 宋本）   |



#### v2.2.0 (2026-08-12) — 知识库蒸馏速查 + 倪师演讲三讲 + 易经六十四卦全量升级

核心升级：新增结构化速查层与三场倪师重要演讲，SKILL.md 入口植入开阖枢图/原穴全表/五输穴公式等六大速查块，六十四卦从简洁列表升级为完整人事应用百科。

新增内容：

#### 蒸馏速查层（references/distilled/，6 文件，232KB）
- 六经辨证诊断公式：8 公式 + 快速诊断流程图 + 脉舌速查 + 合病并病速查 + 真寒假热鉴别 + 七步走辨证思维模式（966 行）
- 针灸公式速查本：子午流注口诀 + 十二经原穴全表 + 五输穴属性规律 + 子母补泻公式（621 行）
- 感冒六大经方手册：桂枝汤/麻黄汤/葛根汤/大青龙汤/小青龙汤/小柴胡汤 主症+剂量+禁忌（150 行）
- 针灸重点内容汇编：任督二脉要穴 + 十二经络穴位 + 针灸治症精选（1,761 行）
- 教验报告：深度蒸馏知识库 42 篇 vs 现有 skill 四维度抽样对比结论

#### 三场倪师重要演讲（modules/10-12，28KB）
- 第三届扶阳论坛演讲（2009.10）：扶阳理论/阴虚→阳虚→阴实传变链/红斑狼疮血癌脑瘤临床重案/生附子生硫黄分类应用（182 行）
- 仲景心法讲授（2009.12）：经方剂量学/桂枝汤群方之祖/风湿甘附汤→知母汤→乌头汤递进/消化系统经方对应/奶水即月经·七癌同源/掌背额温差秒断阴阳手诊法（218 行）
- 斯坦福大学演讲 + 弟子经验（2010.09）：从感冒一路治到癌症/经方入门三步走/李宗恩杨贞弟子实录/望诊总结+诊病十问/常用压痛点/胆肾结石专方（185 行）

#### SKILL.md 入口速查升级（+130 行）
- 开阖枢总图：三阳（太阳开→少阳枢→阳明阖）+ 三阴（太阴开→少阴枢→厥阴阖）ASCII 可视化图
- 伤寒论两大补虚方铁律：小建中汤（表阳虚，太阳兼太阴）+ 炙甘草汤（里阴虚，少阴阴阳两虚）
- 十二经原穴全表：12 经 × 时辰 × 五行 × 原穴 +「肺寅大卯胃辰宫」口诀
- 五输穴公式：井荥俞经合 × 阴阳经五行 + 主治法则口诀
- 感冒六大经方速查：主症关键 + 剂量核心一图呈现
- 素材路径索引：9 文件行数/适用场景速查表

#### modules/09 六十四卦全量升级
- 原版简洁列表→完整结构化表格：64 卦 × 4 列（序号·卦名·卦象符号·人事应用）
- 新增地天泰卦专章：卦德解释 + 6 条核心人事解读（泰否一念间/包荒治泰/师道之泰/诸葛亮三顾茅庐/婆媳之道/鉴定器量四句话）+ 阳宅应用（妻居西北角）+ 占卜图示 + 倪师金句
- 新增易经总论：易经非算命书，乃君子避小人之人间道指南

#### 教验增强
- 与深度蒸馏知识库覆盖四维度逐维度抽样对比（伤寒/金匮/内经/针灸/诊断公式/临床经验）
- 结论：现有 skill 覆盖 95% 事实，无重大冲突，补充开阖枢可视化图/两大补虚方汇总/七步思维模式/真寒假热鉴别
- 关键词索引新增 3 板块：扶阳论坛/癌症临床、仲景心法、斯坦福演讲

| 指标 | v2.1.0 | v2.2.0 |
|------|:-----:|:-----:|
| 总文件数 | 31 | 42 |
| 知识模块 | 9 | 12 |
| SKILL.md 行数 | 11,169 | 11,277 |
| 六十四卦展示 | 简列表 | 64 卦全表 + 卦象符号 |
| 诊断公式 | 零散于正文 | 独立速查文件 966 行 |
| 演讲模块 | 0 | 3（扶阳+仲景+斯坦福） |
---
#### v2.1.0 (2026-06-08) — 六经辨证诊断公式

**核心升级**：从知识库查询工具升级为具备六经辨证思维模式的临床诊断助手。

**新增内容**：
- **8个诊断公式**：太阳/阳明/少阳/太阴/少阴/厥阴/少阴热化/合病并病，每个含IF-THEN辨证规则+分型鉴别表+代表方剂
- **快速诊断流程图**：从患者症状到六经定位的完整决策树
- **脉诊速查**：8种单脉+8种复合脉象
- **舌诊速查**：5种舌象+6种复合舌象+脉舌矛盾决策树
- **真寒假热/假寒鉴别**：八维法（面色/口鼻气/舌形/脉象/胸腹/小便/口渴/大便）+危重证候警示
- **合病/并病速查**：11种组合+治疗先后原则
- **七步走辨证思维模式**：定表里→分阴阳→辨寒热→判传变→审体质→选方剂→精细加减
- **用药铁律**：7条禁忌+5条急救方案
- **建中汤系列**：小建中/黄芪建中/当归建中/大建中（太阴病扩展）
- **治肝三法**：乌梅丸/吴茱萸汤/小建中汤（金匮核心）
- **八味肾气丸详解**：三补三泻+桂附八味丸vs六味地黄丸
- **金匮杂病六经归属速查**：12种杂病+代表方剂
- **金匮特有方剂六经归属**：咳喘类4方+补虚类8方+历节类3方（含完整组成）
- **11处交叉引用**：诊断公式→modules/详细条文的双向链接

**数据来源**：
- 倪海厦《伤寒论讲义》（人纪系列）
- 倪海厦《黄帝内经讲义》（人纪系列）
- 倪海厦《金匮要略讲义》（人纪系列）

**质量验证**：
- 独立评估评分：9.4/10
- 10个临床场景测试：10/10覆盖
- 11个方剂剂量逐方核对：100%与源文件一致
- 六经提纲条文核对：6条中5条完全一致，1条异体字差异

**SKILL.md变化**：+476行（10,697→11,169行），新增第6097-6545行

---

- **v2.0.1** (2026-05-26)：新增分类医案库 cases/（245 例）+ 研究资料 references/；修复 .gitignore
- **v2.0.0** (2026-05-25)：仓库精简——移除原始参考资料(110MB)，仅保留运行必需文件(4MB)
- **v1.1.2** (2026-05-24)：详情页重写——新增安装教程、使用示例
- **v1.1.1** (2026-05-24)：更名为「倪海厦skill」，slug 改为 `nihaixia`
- **v1.1.0** (2026-05-23)：神农本草经药性体系深度蒸馏；关键词索引全面优化
- **v1.0.1** (2026-05-02)：结构优化；OCR 校正 13 处；新增汉唐文章精华 10 篇
- **v1.0.0** (2026-04-14)：初版发布

</details>

---

## 致谢

- 感谢 [huoyalong](https://github.com/huoyalong/nihaisha-skill) 提供 nihaisha-skill 基础框架
- 感谢 [9527qingfeng](https://github.com/9527qingfeng/hantang-nihaixia-follower) 提供医案数据支持

---

## Star History

[![RepoStars](https://repostars.dev/api/embed?repo=jangviktor-web%2Fnihaixia&theme=grape)](https://repostars.dev/?repos=jangviktor-web%2Fnihaixia&theme=grape)

---



## 免责声明

本项目内容仅供中医学习与研究，不替代专业医疗诊断。所有诊疗请务必咨询执业医师。

---

<div align="center">

**基于 [nihaisha-skill](https://github.com/huoyalong/nihaisha-skill) 二次开发 · 遵循 MulanPSL-2.0 开源协议**

[![ClawHub](https://img.shields.io/badge/ClawHub-v2.1.0-orange)](https://clawhub.ai/jangviktor-web/skills/nihaixia)
[![OpenClawMP](https://img.shields.io/badge/OpenClawMP-v2.0.1-blueviolet)](https://openclawmp.cc)
[![SkillHub](https://img.shields.io/badge/SkillHub-nihaixia--pro-red)](https://skillhub.cloud.tencent.com/skills/nihaixia-pro)

</div>
