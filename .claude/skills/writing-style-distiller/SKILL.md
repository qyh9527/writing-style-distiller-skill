---
name: writing-style-distiller
description: Use when asked for 文风蒸馏, 文风配置, 写作风格分析, AIRP writing style prompts, writing style distillation, style profiles, or <writing_style> XML from an author name, literary text file, excerpt samples, or style description
---

# Writing Style Distiller v2

从作者名、文学文本、摘录样本或风格描述中，蒸馏出可执行的 `<writing_style>` 配置。采用自适应多阶段工作流，每阶段文件落盘并设审查门。

## 输出语言

使用用户的对话语言书写说明和标签。XML 标签名不变。示例保持作者原文语言。

## 核心边界

- `<writing_style>` 控制**如何书写**：措辞、句法、叙事、段落、节奏、对话处理、感官选择。
- `<writing_style>` **不控制**：长期剧情走向、事件结果、关系发展、角色选择、结局。
- 若用户请求剧情方向/情感命运/基调，输出为独立的 `<tone>` 块，不混入 `<writing_style>`。
- 区分三个概念：
  - **文风**：写作细节与段落控制。
  - **情感底色**：读者体验的审美/情绪色彩；仅改变呈现方式时可置于文风内。
  - **剧情基调**：故事轨迹与事件处理；必须独立。
- 作者名和作品名是证据来源，不是最终控制指令。用可执行参数替换"模仿X"。

## 支持文件

在执行各阶段时，按需读取以下文件：

| 文件 | 用途 | 读取时机 |
|---|---|---|
| `output-format.md` | 输出格式定义与完整示例 | Phase 3-4 |
| `quality-checklist.md` | 质检清单 | Phase 4 |
| `phases/research.md` | 研究与证据收集指令 | Phase 1 |
| `phases/diagnosis.md` | 风格诊断与架构指令 | Phase 2 |
| `phases/drafting.md` | 文风初稿生成指令 | Phase 3 |
| `phases/optimization.md` | 优化与质检指令 | Phase 4 |
| `knowledge/style-families.md` | 风格家族分类与密度表 | Phase 2 |
| `knowledge/label-risk-table.md` | 高风险标签行为化转换 | Phase 3-4 |
| `knowledge/model-adaptation.md` | 模型适配规则 | Phase 4 |

## 自适应路由

每次接收请求时，判断输入类型并选择对应深度模式：

| 输入类型 | 深度模式 | 阶段路线 |
|---|---|---|
| 作者名（无文本） | **深度** | P1 研究 → P2 诊断 → P3 初稿 → P4 优化 |
| 作者名 + 代表作 | **深度** | P1 研究 → P2 诊断 → P3 初稿 → P4 优化 |
| AIRP 预设定制（复杂） | **深度** | P1 研究 → P2 诊断 → P3 初稿 → P4 优化 |
| 本地文件 / 大量摘录 | **标准** | P1 分析 → P2 初稿+质检 → P3 输出 |
| 少量摘录（<500字） | **标准** | P1 分析 → P2 初稿+质检 → P3 输出 |
| 风格描述（>100字或多维度） | **标准** | P1 分析 → P2 初稿+质检 → P3 输出 |
| 风格描述（≤100字且单一方向） | **快速** | P1 草稿 → P2 输出 |
| 已有文风 + 修改请求 | **快速** | P1 草稿 → P2 输出 |

路由时向用户输出诊断信息：
> "检测到输入类型：[类型] → 进入**[深度/标准/快速]模式**。预计 [N] 个阶段，每阶段有审查门。"

仅当输入无法识别作者、文件、样本、风格目标或模型目标时，才提出一个澄清问题。

## 工作流阶段

### 深度模式（4 阶段）

**Phase 1: 研究与证据收集**
- 读取 `phases/research.md` 执行。
- 产出：`docs/style-output/{timestamp}-{style-name}/research-notes.md`
- 🚪 审查门：展示研究笔记摘要，确认方向。

**Phase 2: 风格诊断与架构**
- 读取 `phases/diagnosis.md` + `knowledge/style-families.md` 执行。
- 产出：`docs/style-output/{timestamp}-{style-name}/style-diagnosis.md`
- 🚪 审查门：展示密度分配方案，确认架构。

**Phase 3: 文风初稿**
- 读取 `phases/drafting.md` + `output-format.md` + `knowledge/label-risk-table.md` 执行。
- 产出：`docs/style-output/{timestamp}-{style-name}/style-draft.md`
- 🚪 审查门：展示完整初稿，接受修改意见。

**Phase 4: 优化 + 质检**
- 读取 `phases/optimization.md` + `quality-checklist.md` + `knowledge/model-adaptation.md` 执行。
- 产出：终端输出最终 `<writing_style>` + 可选 `final-style.md` 落盘。

### 标准模式（3 阶段）

Phase 1: 源文本分析 → `analysis-notes.md` → 🚪 审查门
Phase 2: 文风草稿 + 质检 → `style-draft.md` → 🚪 审查门
Phase 3: 最终输出

### 快速模式（2 阶段）

Phase 1: 直接生成草稿 → `style-draft.md` → 🚪 审查门
Phase 2: 最终输出

## 审查门规则

每个 Phase 完成后，必须执行以下两步：
1. **文件落盘**：将当前阶段产物写入 `docs/style-output/{timestamp}-{style-name}/` 对应文件。
2. **交互审查**：在终端展示摘要，停止执行，向用户发送审查门提问。
   - 只有在用户确认（如"没问题"、"继续"、"同意"）后，才读取下一阶段指令文件继续执行。
   - **禁止一次性输出所有中间产物和终稿。必须分阶段、分回合让用户逐步确认。**

## 异常处理

| 情况 | 处理 |
|---|---|
| 原文摘录不足 | 标注 `基于有限资料`，减少示例到 4 段，说明限制。 |
| 多时期风格 | 在诊断书中标注分期，禁止将冲突风格揉在同一规则。 |
| 搜索失败 | 请求用户提供文本样本或代表作。 |
| 仅有风格描述 | 生成合成配置，标注 `综合风格描述`。 |
| 用户请求 AIRP 实用提示词 | 保持 `<writing_style>` 格式，增加模型适配和重置规则。 |
| 用户请求示例教学 | 在 XML 内用短摘录，长示例置于 XML 外并标注版权和剧情借用限制。 |

## 常见错误

- 不要伪造原文摘录。
- 不要翻译需要保持原语种的示例。
- 不要跳过引用和选段理由。
- 不要输出纯文学评论而无可执行写作参数。
- 不要让文风字段指挥未来事件、关系发展或结局。
- 不要用作者名替代具体写作规则。
- 不要将示例中的场景变为可复用的剧情素材。
- 不要依赖高风险标签（羞耻、疯感、破碎）而不附加行为化替换。
- 不要在规则中枚举具体场景替代抽象类规则。
- 不要未经质检就声称通过验证。

## 署名与使用限制

本技能改编自 Yandhi酱 的原创内容。

- 原创者：Yandhi酱
- Discord ID：`y_a_n_d_h_i`
- 原始帖子：https://discord.com/channels/1291925535324110879/1423575785360326716
- 原始时间：2025/11/20 22:40
- 作者声明：用户可直接使用，无需私下授权。
- 已知限制：禁止商用；社区内共享、修改、管理备份均允许；需署名原作者。

如原作者发布更新条款，以原作者最新声明为准。
