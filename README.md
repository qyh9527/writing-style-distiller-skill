# 文风蒸馏器 Claude Code Skill

[English README](README_EN.md)

这是一个 Claude Code 项目级 skill，用于将作家名称、文学文本、摘录样本或风格描述转换为可执行的 `<writing_style>` XML 文风配置。

## 项目内容

主要文件：

- `.claude/skills/writing-style-distiller/SKILL.md`：Claude Code skill 主入口。
- `.claude/skills/writing-style-distiller/output-schema.md`：`<writing_style>` XML 输出结构。
- `.claude/skills/writing-style-distiller/quality-checklist.md`：理论准确性、文化适配性、可执行性检查清单。
- `.claude/skills/writing-style-distiller/citation-and-examples.md`：原文例句、引用出处、选段理由规则。
- `文风蒸馏器.md`：原始提示词整理稿。

## 使用方式

在支持项目级 skills 的 Claude Code 环境中，可以这样请求：

```text
使用 writing-style-distiller，帮我生成川端康成的 writing_style XML
```

或：

```text
用 writing-style-distiller 分析这个文本文件的文风，并输出 <writing_style>
```

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