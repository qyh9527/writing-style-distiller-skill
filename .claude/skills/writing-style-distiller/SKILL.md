---
name: writing-style-distiller
description: Use when asked for 文风蒸馏, 文风配置, 写作风格分析, writing style distillation, style profiles, or <writing_style> XML from an author name, literary text file, excerpt samples, or style description
---

# Writing Style Distiller

## Overview

Generate an executable `<writing_style>` XML configuration from an author name, literary text, excerpt samples, or a style description. Treat the result as a writing-control profile: every field must guide future AI writing, not merely summarize literary criticism.

## Output Language

Use the user's conversation language for explanations and section labels. Keep XML tag names unchanged. Keep excerpts in the author's original writing language.

## Required Supporting Files

Read these files when using this skill:

- `output-schema.md` for the XML structure and field rules.
- `citation-and-examples.md` for original-language examples, citations, and selection rationale.
- `quality-checklist.md` for the final validation gate.

## Input Routing

| User input | Primary action |
|---|---|
| Author name | Research representative works, criticism, original excerpts, and cultural aesthetics. |
| Author name + representative work | Focus research on the named work first, then compare across the author's style if needed. |
| Local text file | Read and analyze the file before searching externally. Do not override the sample with generic author commentary. |
| Excerpt samples | Distill only from the provided samples unless the user asks for external research. |
| Style description | Convert the description into executable style parameters and mark source limitations. |

Ask one clarifying question only when the input cannot identify an author, file, sample, or style target.

## Workflow

### Phase 1: Research or Source Extraction

If the user provides an author name, perform focused research using searches like:

1. `[author] representative works literary style`
2. `[author] narrative criticism`
3. `[representative work] original excerpt`
4. `[author] cultural aesthetic terms`
5. If the author writes in a non-English language, repeat key searches in that language.

Extract:

- At least 6 original-language excerpt candidates when available.
- Evidence covering narrative, expression, and aesthetics.
- Critical vocabulary from literary criticism.
- Cultural terms in the source language, such as `物哀`, `陰翳`, `間`, or the relevant tradition's own terms.

If the user provides text, extract equivalent evidence from the text before using outside sources.

Research note format:

```text
【研究结论】
作家/对象：
文化背景：
核心特征（3项）：
理论框架：
原文来源（≥3条，若可得）：
资料限制（若有）：
```

### Phase 2: Draft the XML

Fill every field in the schema from `output-schema.md`.

Rules:

- Attribute values should be short executable instructions, preferably starting with verbs such as use, avoid, prefer, compress, delay, foreground.
- `example` fields must use original-language text and remain 30-80 characters when possible.
- `markers` must contain 3-6 concrete language markers separated by commas.
- `core` must contain 3-5 aesthetic keywords separated by slashes.
- Avoid these vague Chinese words in generated analysis: `独特的`, `善于`, `富有`, `常用`, `巧妙地`.

### Phase 3: Quality Gate

Apply `quality-checklist.md` before final output. Fix issues before presenting the final answer.

Important: token length is an estimate unless a real token-counting tool is available. Do not claim strict tool verification if no tool was run.

Quality note format:

```text
【质检记录】
初稿长度估计：
问题（若有）：
修正操作：
终稿长度估计：
```

### Phase 4: Final Output

Return, in this order:

1. `<writing_style>` XML in a fenced XML code block.
2. `【引用出处】` list.
3. `【选段理由】` list.
4. `【质检记录】` summary.

Do not say “use artifact.” In Claude Code terminal contexts, output the XML directly or ask whether the user wants it saved as a file.

## Error Handling

| Situation | Handling |
|---|---|
| Not enough original excerpts | Mark `基于有限资料`, reduce examples to 4, and explain the limitation. |
| Multiple style periods | Mark periodization in `<categories>` and avoid flattening the author into one style. |
| Search fails | Ask the user for text samples or a representative work. |
| User supplies only a style description | Generate a non-author or synthetic profile and label the evidence source. |
| Copyright-sensitive long text requested | Use short excerpts, summaries, and citations rather than reproducing long passages. |

## Common Mistakes

- Do not invent original excerpts.
- Do not translate examples when the rule requires author-language originals.
- Do not skip citations or selection rationale.
- Do not output literary commentary without executable writing parameters.
- Do not omit any XML system: narrative, expression, or aesthetics.
- Do not claim exact token verification unless a token-counting tool actually ran.

## Attribution and Use Restrictions

This skill adapts original content by Yandhi酱.

- Original author: Yandhi酱
- Discord ID: `y_a_n_d_h_i`
- Original post: https://discord.com/channels/1291925535324110879/1423575785360326716
- Original timestamp: 2025/11/20 22:40
- Author note: users may directly use it when needed, without privately requesting authorization.
- Known restrictions: commercial use is prohibited; redistribution within the community, modification within the community, and management/group backup are allowed; attribution to the original author is required.

This is not a standard open-source license grant. If the original author publishes updated terms, follow the original author's latest statement.