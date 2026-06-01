# 文风蒸馏器 Skill 设计

日期：2026-06-01

## 目标

把 `文风蒸馏器.md` 转换为 Claude Code 项目级 skill，用于从作家名、文学文本、摘录样本或风格描述生成可执行的 `<writing_style>` XML 文风配置。

## 方案

采用 B-lite 模块化结构：

```text
.claude/skills/writing-style-distiller/
  SKILL.md
  output-schema.md
  quality-checklist.md
  citation-and-examples.md
```

## 设计原则

- `SKILL.md` 只承载触发条件、核心流程、强制规则和常见错误，便于 Claude 搜索与快速加载。
- XML 输出结构放入 `output-schema.md`，后续调整字段时不需要改主流程。
- 质检规则放入 `quality-checklist.md`，便于扩展理论准确性、文化适配性和可执行性检查。
- 引用与例句规则放入 `citation-and-examples.md`，集中约束“原文、出处、选段理由”，降低编造风险。

## 范围

本次只创建项目级 skill，不推送 GitHub，不复制到全局技能目录。后续确认效果稳定后，可以复制到 `C:\Users\50893\.claude\skills\writing-style-distiller\` 作为全局个人 skill。

## 验证

按 skill TDD 的轻量流程验证：

1. RED：记录无 skill 时容易出现的失败模式。
2. GREEN：创建 skill 后，用应用场景检查是否覆盖失败模式。
3. REFACTOR：修补规则漏洞，确保后续维护清晰。

## 非目标

- 不实现真实 token 计数脚本。
- 不自动联网抓取版权文本全文。
- 不创建 GitHub 远程仓库或推送。
