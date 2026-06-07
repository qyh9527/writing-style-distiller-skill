# 文风蒸馏器 Claude Code Skill

[English README](README_EN.md)

这是一个 Claude Code 项目级 skill，用于将作家名称、文学文本、摘录样本或风格描述转换为可执行的 `<writing_style>` 文风配置。

## v2.0 核心特性

- **自适应深度管道**：根据输入复杂度自动选择深度/标准/快速三种模式（4/3/2 阶段）
- **多阶段审查门**：每阶段文件落盘，用户可在关键节点介入修改
- **轻量输出格式**：XML 壳 + 一级 XML 分区 + 纯文本内容，替换过重的嵌套 XML schema
- **自适应 Schema**：按风格家族（情感表达/语言特征/叙事结构/示例驱动）自动调整密度，token 目标 600-1200
- **知识库分离**：风格家族分类、高风险标签转换表、模型适配规则独立管理

## v2.1 更新

- **纯净输出**：所有模式的最终阶段完成后，额外输出一个仅含 `<writing_style>`（及可选 `<tone>`）的干净 xml 代码块，方便直接复制使用
- **中间产物自动清理**：纯净输出完成后，自动删除 `docs/style-output/` 下的中间产物目录，保持工作区整洁

## v2.2 更新

- **反八股知识库**：新增 `knowledge/anti-bagu.md`，系统梳理 6 类 AI 生成文风提示词的八股模式（不必要定义、场景枚举、解释性语句、模式化修辞、过度展开、错误正反例对），Phase 3-4 阶段逐项排查
- **抽象度检验强化**：抽象优先原则新增「一句话概括测试」和「不必要定义删除」两步，质检清单 A 项同步更新
- **意图探针**：路由完成后、Phase 1 之前新增轻量意图探针环节，通过 1-2 个锚定问题（应用场景、审美基线、排除方向、结构vs感受侧重）避免蒸馏方向偏离
- **示例驱动类扩充**：大幅扩展示例驱动类知识，补充示例选择标准（完整场景要求、token 参考量、基调影响、人称匹配策略、框架大众化原则）和通用框架参考
- **人格化写法**：新增可选路径文档，说明用作者/作品口吻撰写文风规则的实施要点、译者干扰、角色冲突等注意事项
- **压缩优先级扩展**：Phase 4 压缩表从 6 项扩展到 8 项，插入概括测试和定义删除步骤

## v2.3 更新

- **场景响应/对话驱动家族**：新增两个风格家族分类（场景响应型、对话驱动型），扩展密度分配表与触发条件
- **反八股增强**：反八股知识库新增第 7-10 类八股模式识别（空洞对比、修饰词堆砌、万能模板、伪个性化标签）
- **优秀范式知识库**：新增 `knowledge/exemplary-patterns.md`，提供经过验证的文风配置结构范式参考

## v2.4 更新

- **输出去重**：移除"纯净输出"概念，所有模式只输出一份 `<writing_style>` 配置。附属信息（引用出处、质检记录）前置，XML 代码块放最后，用户可直接一键复制

## v2.5 更新

- **架构瘦身**：SKILL.md 从 178 行精简到 ~85 行，异常处理/常见错误拆分到独立文件 `error-handling.md`，符合 Anthropic 官方 Skill 最佳实践
- **description 规范化**：修改为官方推荐格式（第一句能力描述 + 第二句触发词），提升 skill 发现准确率
- **Quick Start + 流程看板**：SKILL.md 新增极速上手示例和 Checklist 进度看板
- **权威渠道优选**：Phase 1 研究阶段新增六级权威渠道优先级体系（★★★学术/原作 → ☆☆☆自媒体），每次研究至少使用 2 个 ★★★ 级渠道，低级渠道必须交叉验证
- **叙事人称与视角知识库**：新增 `knowledge/narrative-perspective.md`，基于热奈特聚焦理论系统化整理人称×聚焦分类、各视角对文风的具体影响、AI 常见人称失败模式及防御规则、AIRP 双视角特殊配置
- **人称视角深度集成**：Phase 2 诊断新增人称与视角诊断步骤，Phase 3 起草新增人称锚定句和级联约束检查，质检清单新增第 I 维「人称与视角一致性」（视角泄漏、跳脑、人称滑动等 6 项检查）
- **100+ 行文件目录**：anti-bagu、style-families、exemplary-patterns、output-format 四个长文件顶部添加目录索引
- **质检维度扩展**：质检清单从 5 维扩展到 9 维（A-I），覆盖规则抽象度、格式、边界、鲁棒性、干净度、动态一致、铁律、语域、人称
- **打包脚本改进**：`_create_release_zips.py` 现在自动从源目录同步到 release-staging（清空再复制），排除开发专用文件

## v2.6 更新

- **模型适配深化**：Claude 新增"舒适区突破策略"（识别文青底层倾向、非舒适区文风多层约束叠加），Gemini 新增"标签连锁机制"（极端化拆解问题及行为序列翻译法）和"高频区规避"策略，新增跨模型通用原则（U形注意力分配、正面表述原则、高频区通用防御）
- **反八股扩展**：新增第 11-12 类八股模式（物理词汇滥用、极端词汇堆砌），第5项过度展开增加温情生活流错误/正确对比案例
- **优秀范式拆分与新增**：第5条拆分为 5a 场景节奏循环范式（男性视觉小说）和 5b 关键词串+感官氛围范式（古风晋江文学），新增第6条"三层框架公式"作为新手入门脚手架
- **标签风险表扩充**：新增 Gemini 标签连锁退化警告、3个 NSFW 标签（发情/高潮/精液）、羞耻条目 Gemini 特有失败、骚话人格滑坡防御
- **输出格式增强**：新增 U 形注意力分区位置优化原则、control_scope 标准声明模板、3个精简基调示例（治愈/伤感/消极梯度）、格式扩展说明（场景节奏循环/底色声明/变量封装）
- **质检维度扩展**：从 9 维扩展到 11 维（A-K），新增 J Token效率与注意力分配、K NSFW场景鲁棒性
- **NSFW 鲁棒性强化**：起草阶段新增 NSFW 后风格漂移重置规则、Token效率原则；异常处理新增 NSFW偏移/预设冲突/人格化冲突三种情况；常见错误新增物理词汇/精液温度/触碰即发情/机制术语禁入正文
- **研究阶段增强**：探针问题池新增三层框架引导问题和八股预判探针，渠道增加青空文库和知乎长评
- **压缩优化增强**：新增 P0 物理词汇检查（最高优先级），Gemini 复读词汇检查，2个新证据诚实标签
- **密度表校准**：style-families.md 新增总纲声明、示例基调影响警告、密度范围实测注释；diagnosis.md 修正步骤编号重复，新增跨家族文风处理规则
- **模型执行门槛**：SKILL.md 标注建议使用 Sonnet 或 Opus 及以上模型执行

## 项目内容

```text
.claude/skills/writing-style-distiller/
├── SKILL.md                    # 主入口：自适应路由 + 工作流调度
├── output-format.md            # 输出格式定义 + 完整示例
├── quality-checklist.md        # 9 维质检清单
├── error-handling.md           # 异常处理与常见错误
├── verification-notes.md       # 验证记录（开发参考）
├── phases/
│   ├── research.md             # Phase 1: 研究与证据收集（含权威渠道优选）
│   ├── diagnosis.md            # Phase 2: 风格诊断与架构（含人称视角诊断）
│   ├── drafting.md             # Phase 3: 文风初稿生成（含人称锚定）
│   └── optimization.md         # Phase 4: 优化与质检
└── knowledge/
    ├── style-families.md       # 风格家族分类与密度表
    ├── label-risk-table.md     # 高风险标签行为化转换表
    ├── model-adaptation.md     # Claude/Gemini 模型适配规则
    ├── anti-bagu.md            # 文风提示词反八股指南
    ├── exemplary-patterns.md   # 优秀范式知识库
    └── narrative-perspective.md # 叙事人称与视角知识库
```

其他文件：

- `文风蒸馏器.md`：原始提示词整理稿。

## 安装方式

### 从 GitHub Releases 下载 zip

推荐从本仓库的 [GitHub Releases](https://github.com/qyh9527/writing-style-distiller-skill/releases) 下载现成 zip：

- `writing-style-distiller-agent.zip`：通用 Agent/Skill 包，适合导入支持 agent 或 skill 文件夹的 IDE/Agent 工具。
- `writing-style-distiller-claude-code-project-skill.zip`：Claude Code 项目级 skill 包，适合解压到目标项目根目录。

通用包解压后结构为：

```text
writing-style-distiller/
├── SKILL.md
├── output-format.md
├── quality-checklist.md
├── error-handling.md
├── phases/
│   ├── research.md
│   ├── diagnosis.md
│   ├── drafting.md
│   └── optimization.md
└── knowledge/
    ├── style-families.md
    ├── label-risk-table.md
    ├── model-adaptation.md
    ├── anti-bagu.md
    ├── exemplary-patterns.md
    └── narrative-perspective.md
```

Claude Code 项目级包解压后结构为：

```text
.claude/
  skills/
    writing-style-distiller/
      SKILL.md
      output-format.md
      quality-checklist.md
      error-handling.md
      phases/
        research.md
        diagnosis.md
        drafting.md
        optimization.md
      knowledge/
        style-families.md
        label-risk-table.md
        model-adaptation.md
        anti-bagu.md
        exemplary-patterns.md
        narrative-perspective.md
```

### 作为项目级 skill 使用

1. 克隆或下载本仓库。
2. 在 Claude Code 中打开仓库根目录。
3. 确认以下文件存在：

```text
.claude/skills/writing-style-distiller/SKILL.md
```

Claude Code 会从项目内的 `.claude/skills/` 目录发现该 skill。之后即可在当前项目中直接请求使用 `writing-style-distiller`。

### 安装到全局 skills 目录

如果希望在其他项目中也能使用，可以把 skill 目录复制到 Claude Code 的全局 skills 目录：

```text
~/.claude/skills/writing-style-distiller/
```

在 Windows 上通常对应：

```text
C:\Users\<你的用户名>\.claude\skills\writing-style-distiller\
```

复制后，确认全局目录下存在：

```text
~/.claude/skills/writing-style-distiller/SKILL.md
```

## 使用方式

在支持项目级 skills 的 Claude Code 环境中，可以这样请求：

```text
使用 writing-style-distiller，帮我生成川端康成的文风配置
```

或：

```text
用 writing-style-distiller 分析这个文本文件的文风，并输出 <writing_style>
```

Skill 会自动判断输入类型并选择对应的深度模式（深度/标准/快速），每个阶段会将中间产物写入 `docs/style-output/` 目录，并在审查门处暂停等待你的确认。最终阶段输出附属信息后，以一个 `<writing_style>` XML 代码块收尾供直接复制，随后自动清理中间产物。

## 来源与署名

本项目基于 Yandhi酱 的原始内容整理并转换为 Claude Code skill。

- 原作者：Yandhi酱
- Discord ID：`y_a_n_d_h_i`
- 原帖链接：https://discord.com/channels/1291925535324110879/1423575785360326716
- 原发布时间：2025/11/20 22:40

作者补充说明：需要的话可以直接使用，不用私信要授权。

## 已知使用条件

根据目前已知信息：

| 项目 | 状态 |
|---|---|
| 商业化使用 | 禁止 |
| 社区内二次传播 | 允许 |
| 社区内二次修改 | 允许 |
| 管理组备份 | 允许 |
| 署名原作者 | 必须 |
| 直接使用，无需私信授权 | 允许 |

## 授权与限制说明

本项目不是标准开源协议项目。由于原作者的完整协议尚未确认，本仓库不使用 MIT、Apache-2.0、GPL 等标准开源许可证。

除非原作者另行明确授权，本项目及其衍生整理内容仅允许非商业用途。传播、修改或备份时，请保留对原作者 Yandhi酱 的署名、Discord ID、原帖链接和原发布时间。

如果原作者后续发布更明确或更新的授权条款，应以原作者最新声明为准。

## 维护说明

本仓库维护者只对 Claude Code skill 的整理、结构化和文档化负责，不声明拥有原始内容版权。
