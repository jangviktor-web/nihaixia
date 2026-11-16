# 设计文档：为 nihaixia skill 增装确定性检索器

- 版本：v0.1（2026-11-16）
- 状态：**设计定稿待实施**，未改动任何现有 skill 文件
- 来源模块：`D:\AndroidProjects\nihaisha_app` 的「问倪师 AI」
- 选定路线：**B — 增强现有 nihaixia skill**，不新建独立 skill

---

## 1. 目标与非目标

### 目标

让 nihaixia skill 具备与 App 内「问倪师 AI」**同构**的检索能力：提问 → 确定性切词 → 六源检索 → 预算内拼装 → 交给宿主模型在人格约束下作答。

核心收益：把「让模型自己翻阅 4.5 MB `modules/` markdown」换成「脚本先检索出 ≤ 6 KB 的相关原文，再让模型基于它作答」。带来三点改善：

| 维度 | 现状（纯 LLM 翻文件） | 改造后 |
|---|---|---|
| 可复现性 | 同一问题两次回答引用的条文可能不同 | 检索结果确定性可复现 |
| 引文可审计 | 模型可能凭记忆虚构条文号 | 条文号只来自索引命中 |
| Token 成本 | 读模块需数千至数万 token | 上下文硬预算 6000 字（约 3–4 K token） |

### 非目标

- ⛔ **不改 App 代码**。App 侧继续以 `assets/llm/persona.md` + `llm_service.dart` 独立运行。
- ⛔ **不做 HTTP 调用**。App 自己 POST 到 OpenAI 兼容端点（`llm_service.dart:887 ask()`）；skill 版由宿主模型作答，检索器只产出上下文文本。这是两者最大的架构差异。
- ⛔ **不重建索引**。直接复用 App 已有的 `classic_index.json.gz`，避免两套索引漂移。

---

## 2. 现状与差距

`nihaixia/SKILL.md` 现 1614 行，前 24 行的表达速查卡与 App 的 `persona.md:1-24` 大段重合（同源），`决策启发式 / 诚实边界` 亦已覆盖。**因此人格层不需要搬，需要新增的只有检索层。**

差距清单：

| App 模块能力 | nihaixia 现状 | 判定 |
|---|---|---|
| 表达规范、八查、条文卡片 | ✅ SKILL.md 已有且更详细 | 不搬 |
| 环境约束（`persona.md:109-133`） | ❌ 不存在 | 🔴 改写为新协议 |
| 讲义索引 1728 条 | ❌ 靠模型翻 4.5 MB modules | 🔴 补检索器 |
| 方剂库 314 方（含禁忌） | ⚠️ 存在但无结构化查询 | 🟠 接进检索器 |
| 穴位库 401 条 | ⚠️ 散见 `modules/09` | 🟠 接进检索器 |
| 病名对照 48 条 | ❌ 不存在 | 🟠 搬入 |
| 医案 1089 例（12 列表格） | ✅ `cases/` 已有叙事版 | ⚠️ 需确认是否重复 |
| 语义切分 / 预算拼装 / 二跳 | ❌ 不存在 | 🔴 从 Dart 重写 |

---

## 3. 目录结构

新增文件全部落在 `nihaixia/` 下，现有文件只改 `SKILL.md` 一处。

```
~/.workbuddy/skills/nihaixia/
├── SKILL.md                          # 仅新增一节「检索协议」（约 60 行）
├── scripts/
│   ├── nishi_retrieve.py             # 检索器主体（CLI + 可导入）
│   ├── build_data.py                 # 从 App 仓库同步并转换数据资产
│   └── verify_citations.py           # 回答自检：文中方剂是否都在上下文内
├── data/
│   ├── classic_index.json.gz         # 1728 条，直接复制
│   ├── formulas.json                 # 314 方，直接复制
│   ├── acupoints.json                # 401 穴，直接复制
│   ├── disease_alias_index.json      # 48 条，直接复制
│   └── cases.json                    # 1089 例，由 md 表格转出
└── references/
    └── retriever-spec.md             # 检索算法细节（切词规则、坑位说明）
```

`data/` 总体积约 4.5 MB（其中 `classic_index.json.gz` 3.1 MB 占主要部分），符合 skill 包可接受的体积。

---

## 4. 检索器接口

### CLI

```bash
python scripts/nishi_retrieve.py "糖尿病有哪些方剂"
python scripts/nishi_retrieve.py --json "足三里主治什么"     # 同时输出结构化结果
python scripts/nishi_retrieve.py --explain "咳嗽"            # 打印切词与命中决策
```

### 输出

默认输出 **Markdown 文本**，与 App 的 `buildContext()`（`llm_service.dart:692-786`）同构，可被 SKILL.md 直接引用为「下方的【讲义片段】…」：

```
【讲义片段】
【金匮·肺痿肺痈咳嗽上气病脉证治】
...（每条 ≤ 520 字，总长 ≤ 3600 字）

【古今·中西医病名对照】
消渴（糖尿病）：倪师原话「以上就是消渴，糖尿病了。」

【命中片段中出现的方剂】（从上述原文确定性抽取，可全部列出）
白虎加人参汤、肾气丸、…

【方剂库摘要】（本地结构化整理，非讲稿原文；用来讲「什么情况不能用」）
· 白虎加人参汤：禁忌 …｜要点 …

【倪师医案】（本地医案库，引用时写「医案 #序号」）
#232｜诊断：糖尿病｜病机：…｜方剂：…｜结果：…

【本地统计（口径＝本 skill 收录量）】
· 《伤寒论》讲稿 394 条，出现方剂 … 首
```

`--json` 额外产出 `{hits, formulas, briefs, cases, acupoints, diseases, stats, emergency, keywords}`，供 `verify_citations.py` 与回归测试消费。

🔴 **`emergency` 字段必须输出**：`persona.md:147-155` 的急症词表在 App 里用于渲染加强版免责框。skill 环境没有 UI，改为在文本首行插入 `⚠️ 急症提示`，由宿主模型原样带到回答开头。

### Python API

```python
from nishi_retrieve import prepare, build_context, keywords_for

r = prepare("糖尿病有哪些方剂")     # -> Retrieval
print(build_context(r, "糖尿病有哪些方剂"))
```

---

## 5. 函数级迁移映射

源文件 `lib/services/llm_service.dart`（1039 行）。逐项对照，实施时按行号读取原逻辑。

### 5.1 常量

| Dart 位置 | 名称 | 值 | Python 目标 |
|---|---|---|---|
| `:106` | `maxHits` | 8 | `CFG.MAX_HITS` |
| `:109` | `contextSnippetSpan` | 200 | `CFG.SNIPPET_SPAN` |
| `:110` | `maxSnippetChars` | 520 | `CFG.MAX_SNIPPET_CHARS` |
| `:111` | `maxContextChars` | 3600 | `CFG.MAX_CONTEXT_CHARS` |
| `:114` | `maxExtraChars` | 2400 | `CFG.MAX_EXTRA_CHARS` |
| `:115` | `maxFormulaList` | 12 | `CFG.MAX_FORMULA_LIST` |
| `:116` | `maxCases` | 3 | `CFG.MAX_CASES` |
| `:119` | `maxCaseCandidates` | 5 | `CFG.MAX_CASE_CANDIDATES` |
| `:122` | `maxCaseFormulas` | 3 | `CFG.MAX_CASE_FORMULAS` |
| `:125` | `maxAcupoints` | 3 | `CFG.MAX_ACUPOINTS` |
| `:129` | `maxAcuHits` | 3 | `CFG.MAX_ACU_HITS` |

### 5.2 词表与判定

| Dart 位置 | 职责 | Python 目标 | 备注 |
|---|---|---|---|
| `:131-134` | `_acuKeywords` 20 词 | `ACU_KEYWORDS` | 针灸意图词 |
| `:149-155` | `emergencyKeywords` | `EMERGENCY_KEYWORDS` | 13 词 |
| `:160-172` | `_stopWords` | `STOP_WORDS` | 🔴 含领域泛词与求诊话术泛词两层，**逐字照搬** |
| `:179-184` | `_functionChars` | `FUNCTION_CHARS` | 🔴 ⛔ 不得添加「上下中里」 |
| `:186-197` | `_isContentWord` | `is_content_word()` | 子串判定，非整词判定 |
| `:199-209` | `keywordsFor` | `keywords_for()` | 4→2 字降序切片，上限 32 |

### 5.3 检索主链

| Dart 位置 | 职责 | Python 目标 |
|---|---|---|
| `:222-296` | `_retrieveResult` 三阶检索 | `retrieve_result()` |
| `:417-445` | `_extendByFormulas` 二跳 | `extend_by_formulas()` |
| `:449-502` | `retrieveCases` | `retrieve_cases()` |
| `:503-511` | `isAcupunctureQuery` | `is_acupuncture_query()` |
| `:512-549` | `retrieveAcupoints` | `retrieve_acupoints()` |
| `:550-596` | `_retrieveAcuHits` 限源检索 | `retrieve_acu_hits()` |
| `:597-638` | `_jumpByAcupoints` 第三跳 | `jump_by_acupoints()` |
| `:639-669` | `_statsIfCounting` | `stats_if_counting()` |
| `:303-414` | `prepare` 总编排 | `prepare()` |
| `:692-786` | `buildContext` 六块拼装 | `build_context()` |
| `:872-886` | `unverifiedFormulas` | `unverified_formulas()`（供自检脚本） |

### 5.4 不迁移

| Dart 位置 | 原因 |
|---|---|
| `:139-145` `normalizeBase` | 端点配置，skill 无 HTTP |
| `:671-686` `loadPersona` / `buildSystem` | 宿主已加载 SKILL.md 作人格 |
| `:795-814` `buildMessages` | 会话组装由宿主负责 |
| `:816-1039` 网络层 | skill 无网络调用 |

---

## 6. 六处必须照搬的算法细节

这些是 App 反复实测后才定下来的规则，注释里写明了失败现况。照搬，不要「优化」。

### 🔴 6.1 贪心填满 + 首词特权

`_retrieveResult:280-289`：原关键词按 `keywordsFor` 顺序扫描，**只有首个命中的词允许填满剩余槽位，其后每词最多 2 条**。否则「大肠癌」只命中 1–2 条时，会由「大肠」把剩余槽位全吃掉，塞进大肠经条文（实测 8 条里 5 条无关）。

### 🔴 6.2 二跳必须预留槽位

`prepare:368`：`reserve = caseFormulas.isEmpty ? 0 : maxCaseFormulas`，第一次检索 `cap = maxHits - reserve`。不预留则第一轮填满 8 条，二跳永远轮不上（注释：「实测白改」）。

### 🔴 6.3 二跳取片要轮流

`_extendByFormulas:426-443`：外层 round 循环、内层逐方各取 1 条。若让首方吃满预留槽位，排在后面、往往才是答案的方永远进不来（实测「射干麻黄汤」被「麻黄附子细辛汤」挤掉）。

### 🔴 6.4 针灸源必须单独限定

`_retrieveAcuHits:550` + `seed` 机制（`:242-247`）：`zhenjiu` 源仅 72 条，全源检索永远排不进前 8。做法是限定 source 单独检索，并以 `seed` 先落位再填别的。

### 🔴 6.5 第三跳在医案反查之前

`prepare:315-332`：症状→穴位（第三跳）先用，医案「针灸方案」反查后补。顺序反了会被「随便哪条医案的配穴」占满 3 个名额（实测问带状疱疹给出下关/合谷/胆石点）。

### 🔴 6.6 优先级三档不可合并

`priority`（病名索引古名 + 提问中的方名）→ 原关键词 → `extra`（病名对照的其他叫法）。合并会让扩展词把原词结果挤掉。

---

## 7. 数据资产规格

| 文件 | 来源 | 处理 | 体积 |
|---|---|---|---|
| `classic_index.json.gz` | `assets/guji/` | 直接复制 | 3.1 MB |
| `formulas.json` | `assets/data/` | 直接复制（314 方） | 419 KB |
| `acupoints.json` | `assets/data/` | 直接复制（401 穴） | 622 KB |
| `disease_alias_index.json` | `assets/data/` | 直接复制（48 条） | 12 KB |
| `cases.json` | `assets/medical_cases/cases_table.md` | **格式转换** | 约 400 KB |

### `classic_index.json.gz` 结构

```json
{"v":1,"entries":[{"s":"jingui","t":"标题","a":"assets/jingui/clause_111.md","x":"正文…"}]}
```

- 条目 1728 条，源分布：`jingui` 433 / `guji` 421 / `shanghan` 394 / `bencao` 335 / `neijing` 73 / `zhenjiu` 72
- 检索直接对 `x` 做子串匹配，**不需要另建倒排索引**：1728 条线性扫描在 Python 中约数十毫秒，最多 32 个关键词仍在秒级以内。保持与 App 同源，避免两套索引漂移。

### `cases.json` 转换规则

`cases_table.md` 为 12 列 markdown 表格（序号 / 日期 / 患者 / 主要诊断 / 病因分析 / 西医背景 / 方剂剂量 / 针灸方案 / 治疗原则 / 疗程结果 / 生活医嘱 / 核心观点）。App 侧解析在 `lib/data/medical_case_data.dart:454-461`，转换时对齐其字段语义：

| 输出字段 | 源列 |
|---|---|
| `seq` | 序号 |
| `diagnosis` | 主要诊断 |
| `mechanism` | 中医病因分析 |
| `formula` | 具体方剂剂量/治疗组成 |
| `acupuncture` | 针灸方案 |
| `result` | 疗程/结果 |
| `comment` | 核心观点 |

⚠️ 两个易错点：
1. 表格单元格内含 `|` 与换行，**不能简单按 `|` 切分**，需处理转义与续行；
2. 「未公开」「未提及」的条目 App 会剔除（1256 行 → 1089 例可用），转换时保持同一剔除规则，否则统计口径会不一致。

---

## 8. SKILL.md 改动方案

**只加一节，约 60 行，插在「知识库蒸馏精华速查」之前**（即紧跟现有表达速查卡）。不放全文算法，细节进 `references/retriever-spec.md`。

新增节骨架：

```markdown
## 检索协议（回答中医内容前必做）

🔴 回答任何中医辨证 / 方剂 / 穴位 / 条文问题前，先执行：

python scripts/nishi_retrieve.py "用户原问题"

把输出原样当作你的【讲义片段】【病名对照】【方剂清单】
【方剂库摘要】【倪师医案】【本地统计】六块材料，然后：

1. 只依据这六块作答。都未涉及就说「讲义里没有涉及这个话题」。
2. 条文出处只写输出里出现的标题，不得凭记忆补条文号。
3. 【方剂库摘要】是二手整理数据，不是倪师原话，引用时不得称「倪师说」。
4. 输出含 ⚠️ 急症提示 时，把它放在回答开头，再继续讲辨证。
5. 回复末尾附固定免责框（本 skill 场景下由你输出，非 App 渲染）。

⛔ 禁止跳过检索直接凭记忆作答。
⛔ 禁止用 modules/ 下的文件替代检索结果——那是全文语料，不是本次命中。
```

同时处理 `persona.md:109-133` 那 25 行 App 环境约束的对应关系：这些内容**不进 SKILL.md**，因为其中「你没有文件读取工具、没有联网工具」在 skill 环境恰好相反，照搬会让模型拒绝调用检索器。其中仍有价值的 5 条（五步辨证流程、禁止罗列方名、针灸四步、穴位只用给出的、禁教人下针、禁复述医案剂量）已分别落在 SKILL.md 现有正文与第 8 节新增协议中，实施时逐条核对，不遗漏。

⚠️ 工程提醒：SKILL.md 已 1614 行，接近单文件可维护上限。新增节控制在 60 行内，若后续再扩，应合并现有重复段落（前 24 行速查卡与 `expression_style.md` 已有明显重复）。

---

## 9. 双源同步策略

`persona.md` 与 SKILL.md 的表达规则目前同源但无同步机制，存在漂移风险。建议：

| 项 | 唯一真源 | 同步方向 |
|---|---|---|
| 表达规范 / 八查 / 卡片 | nihaixia SKILL.md | App 构建时从 skill 抽取（`llm_service.dart:673` 注释已声明此机制） |
| 讲义索引 / 方剂 / 穴位 / 医案 | nihaisha_app 仓库 | `build_data.py` 从 App 仓库单向拉取 |

即：**表达规则从 skill → App，数据资产从 App → skill**，两条单向流，不双向合并。`build_data.py` 每次运行时打印源文件 sha256，便于判断是否需要重跑。

---

## 10. 验收方案

### 10.1 检索一致性（主要闸）

用 `test/llm_case_accuracy_test.dart` 的用例集作为基准。对每条用例，分别取：

- App 侧：`LlmService.prepare(q)` 的 `LlmRetrieval`
- skill 侧：`prepare(q)` 的 `Retrieval`

比对三项，全部一致才算通过：

1. `hits` 的 `source|title` 集合（允许顺序不同）
2. `formulas` 清单
3. `cases` 的 `seq` 集合

注：App 侧需临时加一个导出脚本，把 `prepare()` 结果落 JSON。这属于**只读探测，不改业务逻辑**，实施前需你确认是否允许临时改动 App（否则改为手工抽 10 条样本对账）。

### 10.2 回答质量（人工闸）

抽 12 条覆盖六类：伤寒条文、金匮病名、方剂禁忌、针灸取穴、医案回链、计数类提问。同一问题分别走 skill 链路与 App 链路，人工比对「首推方剂 / 引用条文 / 是否编造」。验收线：编造条文数 = 0。

### 10.3 性能与体积

- 单次检索耗时 ≤ 1.5 s（含 gzip 解压）
- `data/` 总体积 ≤ 5 MB
- `python scripts/nishi_retrieve.py --explain "咳嗽"` 能打印切词与命中决策，便于排障

---

## 11. 实施步骤与工时

| 步 | 内容 | 产出 | 工时 |
|---|---|---|---|
| 1 | 数据搬运与 `cases.json` 转换 | `build_data.py` + `data/` | 0.5 天 |
| 2 | 检索器主体（6 处算法细节） | `nishi_retrieve.py` | 1–1.5 天 |
| 3 | SKILL.md 新增检索协议 | 60 行新节 + `references/retriever-spec.md` | 0.5 天 |
| 4 | 一致性对账与调参 | 对账报告 | 0.5–1 天 |
| | **合计** | | **2.5–3.5 天** |

建议按步交付：步 1–2 完成后先跑「检索器原型 + 5 个真实问题」验证命中质量，命中质量不过关就不进步 3，避免白写协议。

---

## 12. 风险与回滚

| 风险 | 等级 | 应对 |
|---|---|---|
| App 侧 `prepare()` 需临时改动才能对账 | 🟠 P1 | 改为手工抽 10 条样本，或仅在 App 加独立 `tool/` 脚本不碰 `lib/` |
| SKILL.md 过长影响加载 | 🟠 P1 | 新增节压到 60 行；同步清理与 `expression_style.md` 的重复段 |
| 医案 md 解析踩到 `|` 转义 | 🟠 P1 | 先写单测：解析出的例数须 == 1089，不等就停 |
| 切词规则「优化」后检索退化 | 🔴 P0 | `--explain` 固化 6 条坑位的期望输出作快照测试，改动即报警 |
| 数据与 App 脱节 | 🟡 P2 | `build_data.py` 记录源 sha256，发版时提醒重跑 |

**回滚**：所有新增均在 `scripts/`、`data/`、`docs/` 三个新目录，SKILL.md 仅追加一节。回滚方式为删除新增目录 + `git checkout SKILL.md`。建议实施前先 `cp SKILL.md SKILL.md.bak.<日期>`（该 skill 目录已有多个 `.bak` 先例）。

---

## 13. 待你确认的三件事

1. **App 侧是否允许临时加只读导出脚本**（用于 10.1 的一致性对账）？
2. `cases/` 目录里的叙事医案与 `cases.json`（1089 例表格）用途是否重叠？如果 `cases/` 已够用，可考虑检索器只回链 seq、不引入 `cases.json`，省 400 KB 和一步转换。
3. `zhenjiu` 源 72 条 + `modules/09_zhenjiu_bencao.md` 有重复，检索协议里要不要明确「针灸一律以检索结果为准，modules/09 只看本草」？
