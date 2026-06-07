---
name: writing-style-distiller
description: >-
  Distills executable <writing_style> XML configuration from author names, 
  literary texts, excerpt samples, or style descriptions. Use when asked for 
  文风蒸馏, 文风配置, 写作风格分析, AIRP writing style prompts, writing style 
  distillation, style profiles, or <writing_style> XML.
---

# Writing Style Distiller v2

从作者名、文学文本、摘录样本或风格描述中，蒸馏出可执行的 `<writing_style>` 配置。采用自适应多阶段工作流，每阶段文件落盘并设审查门。

## ⚠️ 模型执行门槛

本 skill 的自适应路由和多阶段审查门需要极强的指令遵循与逻辑分析能力。**强烈建议**在 Claude 3.5/4.5 Sonnet 或 Opus 及以上执行模型下运行。

## 🚀 极速上手 (Quick Start)

当用户输入：
> "帮我蒸馏‘老舍’写市井市民文风的气息"

1. **自动诊断并输出**：进入 **[深度]模式**，预计 4 个阶段，每阶段有审查门。
2. **轻量提问锚定**（意图探针）。
3. **分步执行**：按阶段进行并落盘。向用户确认后，点击下一阶段，最终输出一份高精准的 `<writing_style>`。

## 📦 支持文件

在执行各阶段时，按需读取以下文件：

| 文件 | 用途 | 读取时机 |
|---|---|---|
| `output-format.md` | 输出格式定义与完整示例 | Phase 3-4 |
| `quality-checklist.md` | 质检清单（9 维精悍版） | Phase 4 |
| `phases/research.md` | 研究与证据收集指令（**优选权威学术渠道**） | Phase 1 |
| `phases/diagnosis.md` | 风格诊断与架构指令 | Phase 2 |
| `phases/drafting.md` | 文风初稿生成指令 | Phase 3 |
| `phases/optimization.md` | 优化与质检指令 | Phase 4 |
| `knowledge/style-families.md` | 风格家族分类与密度表 | Phase 2 |
| `knowledge/label-risk-table.md` | 高风险标签行为化转换 | Phase 3-4 |
| `knowledge/model-adaptation.md` | 模型适配规则（Claude / Gemini） | Phase 4 |
| `knowledge/anti-bagu.md` | 文风提示词反八股指南 | Phase 3-4 |
| `knowledge/exemplary-patterns.md` | 优秀文风结构范式参考 | Phase 2-3 |
| `knowledge/narrative-perspective.md` | 叙事人称与视角知识库 | Phase 2-3 |
| `error-handling.md` | 常见错误防御与边缘异常处理 | Phase 3-4 |

## 🔀 自适应路由

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

路由完成后向用户输出诊断信息并立即触发 **1-2个意图探针问题**（详见 `phases/research.md`），提问与诊断一起展示，不单设审查门。

## 🎯 核心编排流程

### 流程进度看板 (Checklist)
进行过程中，用此看板指示当前阶段：
- [ ] 路由决策与意图探针 (`phases/research.md`)
- [ ] Phase 1: 研究与证据收集 (`phases/research.md`)
- [ ] Phase 2: 风格诊断与架构 (`phases/diagnosis.md`)
- [ ] Phase 3: 文风初稿 (`phases/drafting.md`)
- [ ] Phase 4: 最终优化与质检 (`phases/optimization.md`)
- [ ] 清理与最终输出 (`phases/optimization.md` + `error-handling.md`)

## 🚪 审查门交互规则

每个 Phase 完成后，必须：
1. **文件落盘**：将当前阶段产物写入 `docs/style-output/{timestamp}-{style-name}/`。
2. **交互审查**：在终端展示摘要，并向用户发送审查提问（如：方向是否正确？是否进下一阶段？）。**禁止一次性吐出所有最终配置，必须分步确认再读取下一份 md 执行**。

各模式下的详细工作流执行细节，请参考各阶段指令说明文件。关于常见异常与规避原则，请参见 [error-handling.md](error-handling.md)。

---
本技能改编自 Yandhi酱 的原创内容（Discord ID: `y_a_n_d_h_i`，禁止商用，开源需署名，遵循原作者最新声明）。
