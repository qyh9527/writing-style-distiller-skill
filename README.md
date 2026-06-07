# 文风蒸馏器 Claude Code Skill

[English README](README_EN.md)

将作者名称、文学文本、摘录样本或风格描述转换为可执行的 `<writing_style>` XML 文风配置。

## 核心特性

- **自适应深度管道**：根据输入复杂度自动选择深度/标准/快速三种模式（4/3/2 阶段），含审查门
- **六大家族分类**：情感表达 / 语言特征 / 叙事结构 / 示例驱动 / 场景响应 / 对话驱动，按家族自适应密度
- **11 维质检**：覆盖规则抽象度、格式规范、剧情边界、鲁棒性、语言干净度、动态一致性、铁律有效性、语域统一、人称视角、注意力分配、场景鲁棒性
- **模型适配**：Claude 舒适区突破与反文青策略、Gemini 标签连锁抑制与高频区规避、跨模型通用原则
- **研究级搜索**：六级权威渠道优先级，优先学术数据库与原作，避免民科来源
- **叙事视角体系**：基于热奈特聚焦理论的人称×聚焦分类，防视角泄漏/跳脑/人称滑动
- **反八股指南**：12 类 AI 生成文风的八股模式识别与修正
- **优秀范式库**：5 种经实测验证的文风结构范式 + 新手三层框架入门脚手架

## 版本历史

| 版本 | 主要变更 |
|---|---|
| v2.0 | 自适应管道、审查门、轻量 XML 输出、家族分类、知识库分离 |
| v2.1 | 输出去重、中间产物自动清理 |
| v2.2 | 反八股知识库、意图探针、示例驱动类扩充、人格化写法 |
| v2.3 | 场景响应/对话驱动家族、优秀范式知识库 |
| v2.4 | 输出简化为一键复制 |
| v2.5 | 架构瘦身、权威渠道优选、叙事视角知识库、质检扩至 9 维 |
| v2.6 | 模型适配深化、反八股扩至 12 类、范式拆分、质检扩至 11 维、注意力分配优化 |

## 目录结构

```text
.claude/skills/writing-style-distiller/
├── SKILL.md                    # 主入口：自适应路由 + 工作流调度
├── output-format.md            # 输出格式定义 + 完整示例
├── quality-checklist.md        # 11 维质检清单
├── error-handling.md           # 异常处理与常见错误
├── verification-notes.md       # 验证记录（开发参考）
├── phases/
│   ├── research.md             # Phase 1: 研究与证据收集
│   ├── diagnosis.md            # Phase 2: 风格诊断与架构
│   ├── drafting.md             # Phase 3: 文风初稿生成
│   └── optimization.md         # Phase 4: 优化与质检
└── knowledge/
    ├── style-families.md       # 风格家族分类与密度表
    ├── label-risk-table.md     # 高风险标签行为化转换表
    ├── model-adaptation.md     # 模型适配规则
    ├── anti-bagu.md            # 反八股指南
    ├── exemplary-patterns.md   # 优秀范式知识库
    └── narrative-perspective.md # 叙事人称与视角知识库
```

## 安装

### 从 GitHub Releases 下载

推荐从 [Releases](https://github.com/qyh9527/writing-style-distiller-skill/releases) 下载：

- `writing-style-distiller-agent.zip` — 通用包，适合导入支持 skill 文件夹的工具
- `writing-style-distiller-claude-code-project-skill.zip` — Claude Code 项目级包

### 作为项目级 skill

将仓库克隆到项目根目录，确认 `.claude/skills/writing-style-distiller/SKILL.md` 存在即可。

### 安装到全局

复制整个 skill 目录到 `~/.claude/skills/writing-style-distiller/`（Windows 下为 `C:\Users\<用户名>\.claude\skills\writing-style-distiller\`）。

## 使用

```text
使用 writing-style-distiller，帮我生成川端康成的文风配置
用 writing-style-distiller 分析这段文本的文风，输出 <writing_style>
```

Skill 会自动判断输入类型并选择深度模式，每阶段暂停等待确认，最终输出一步到位的 XML 代码块。

## 来源

原内容作者：Yandhi酱（Discord: `y_a_n_d_h_i`），已获直接使用授权。

## 使用条件

| 项目 | 状态 |
|---|---|
| 商业化使用 | 禁止 |
| 社区内传播/修改 | 允许 |
| 署名原作者 | 必须 |

本项目不附加标准开源许可证。传播、修改或备份时请保留原作者署名。
