---
name: writing-style-distiller
description: Use when asked for 文风蒸馏, 文风配置, 写作风格分析, AIRP writing style prompts, writing style distillation, style profiles, or <writing_style> XML from an author name, literary text file, excerpt samples, or style description
---

# Writing Style Distiller

## Overview

Generate an executable `<writing_style>` XML configuration from an author name, literary text, excerpt samples, or a style description. Treat the result as a writing-control profile: every field must guide future AI writing, not merely summarize literary criticism.

This skill optimizes for strong practical control: it separates writing style from plot tone, diagnoses the style's control axis, preserves evidence honesty, and adds prompt-engineering safeguards for AIRP / roleplay / model-specific use.

## Output Language

Use the user's conversation language for explanations and section labels. Keep XML tag names unchanged. Keep excerpts in the author's original writing language.

## Required Supporting Files

Read these files when using this skill:

- `output-schema.md` for the XML structure and field rules.
- `citation-and-examples.md` for original-language examples, citations, and selection rationale.
- `quality-checklist.md` for the final validation gate.
- `prompt-optimization.md` for style/tone separation, label-chain risk, model adaptation, example-flow rules, and drift reset rules.

## Core Boundaries

- `<writing_style>` controls how text is presented: wording, syntax, narration, paragraphing, rhythm, dialogue handling, sensory selection, and aesthetic experience.
- `<writing_style>` must not control long-term plot direction, event outcomes, relationship progress, character choices, or prescribed endings.
- If the user requests plot direction, emotional fate, healing/tragic trajectory, or ending tendency, output it as a separate optional `<tone>` block, not inside `<writing_style>`.
- Distinguish three concepts:
  - `writing style`: writing details and paragraph control.
  - `affective baseline`: reader-facing aesthetic/emotional color; allowed inside style when it only changes presentation.
  - `plot tone`: story trajectory and event handling; keep separate unless the user explicitly asks for it.
- Treat author names and works as evidence sources, not as final control instructions. Replace “imitate X” with executable parameters.

## Input Routing

| User input | Primary action |
|---|---|
| Author name | Research representative works, criticism, original excerpts, and cultural aesthetics. |
| Author name + representative work | Focus research on the named work first, then compare across the author's style if needed. |
| Local text file | Read and analyze the file before searching externally. Do not override the sample with generic author commentary. |
| Excerpt samples | Distill only from the provided samples unless the user asks for external research. |
| Style description | Convert the description into executable style parameters and mark source limitations. |
| AIRP / roleplay / preset style request | Prioritize style-only control, paragraphing, anti-cliche behavior, model adaptation, and drift reset safeguards. |
| Model target such as Gemini or Claude | Apply `prompt-optimization.md` model notes before drafting final XML. |
| Example-flow request | Separate evidence excerpts from style demonstration samples; prevent plot borrowing. |

Ask one clarifying question only when the input cannot identify an author, file, sample, style target, or requested model target.

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
- Evidence covering narrative, expression, aesthetics, and paragraphing.
- Critical vocabulary from literary criticism.
- Cultural terms in the source language, such as `物哀`, `陰翳`, `間`, or the relevant tradition's own terms.

If the user provides text, extract equivalent evidence from the text before using outside sources.

Research note format:

```text
【研究结论】
作家/对象：
文化背景：
核心特征（3项）：
主控轴：
理论框架：
原文来源（≥3条，若可得）：
资料限制（若有）：
```

### Phase 2: Diagnose the Control Axis

Before drafting, classify the target style's main control axis. Use the classification to decide which XML fields need the most density.

#### Theoretical Control Axes

| Control axis | Put most detail into |
|---|---|
| Emotion / reader experience | `<aesthetics_system>`, `<characterization>`, `<rhythm>` |
| Language / lexicon / syntax | `<language>`, `<description>`, `<dialogue>` |
| Perspective / monologue | `<perspective>`, `<temporality>`, `<characterization>` |
| Paragraph / dialogue layout | `<paragraphing>`, `<dialogue>`, `<rhythm>` |
| Genre / literary tradition | `<categories>`, `<palette>`, `<language>` |
| Anti-cliche / model correction | `<prompt_discipline>`, `<characterization>`, `<language>` |

#### AIRP Community Style Typology

In AIRP/roleplay practice, different style families have fundamentally different primary axes. Styles within the same family can share structural templates; styles across families cannot.

| Style family | Primary axis | Density focus | Examples |
|---|---|---|---|
| Emotion-expression styles | Emotion, reader experience | `<aesthetics_system>`, `<characterization>`, `<rhythm>`, `<paragraphing>` | 二次元文风, 治愈文风, 温情生活流 |
| Language-feature styles | Language, lexicon, syntax | `<language>`, `<dialogue>`, `<description>`, detailed lexicon/syntax rules | 古风/文言文风, 红楼梦风, 方言文风 |
| Narrative-structure styles | Perspective, monologue, structure | `<perspective>`, `<temporality>`, `<structure>`, `<characterization>` | 意识流, 散文小说化叙事, 自传体, 轻小说 |
| Example-driven styles | Demonstration samples | Lightweight rules + high-quality `示例流` samples | 通用散文文风 + 换示例切换风味 |

Rules:

- Identify the family before drafting. Do not force an emotion-expression style into a language-heavy template or vice versa.
- Allocate token density to the primary axis first, then fill remaining fields at lower density.
- For language-feature styles (e.g., 古风), the model's training data is often insufficient; compensate with more lexicon/syntax rules and example boundaries.
- For emotion-expression styles (e.g., 二次元), adding the genre label gives the model a strong baseline; spend tokens on emotion handling and paragraph rhythm instead of repeating what the label already conveys.
- For example-driven styles, use the example-flow strategy in `citation-and-examples.md`.

### Phase 3: Draft the XML

Fill every field in the schema from `output-schema.md`.

Rules:

- Attribute values should be short executable instructions, preferably starting with verbs such as use, avoid, prefer, compress, delay, foreground.
- `example` fields must use original-language text and remain 30-80 characters when possible.
- `markers` must contain 3-6 concrete language markers separated by commas.
- `core` must contain 3-5 aesthetic keywords separated by slashes.
- `progression` may only describe single-response internal movement, not future plot trajectory.
- `ending` may only describe local closure style, not long-term story ending, unless a separate `<tone>` was requested.
- Paragraphing must specify dialogue/description separation, paragraph length tendency, and when to use short vs long paragraphs.
- Avoid these vague Chinese words in generated analysis: `独特的`, `善于`, `富有`, `常用`, `巧妙地`.

### Phase 4: Prompt Robustness Pass

Apply `prompt-optimization.md` before final output:

- Convert high-risk abstract labels into observable behavior, syntax, paragraphing, or narrative rules.
- Prefer positive instructions; use negative instructions only as guardrails and pair them with replacements.
- Remove unnecessary extreme words such as “必须”, “绝对”, “强制”; keep them only for hard format rules or true prohibitions.
- Check that concrete objects, plot beats, relationship arcs, and scene sequences from examples did not become general rules.
- If target model is Gemini, reduce emotion/personality labels and add behaviorized alternatives and example boundaries.
- If target model is Claude, counter over-literary sameness with concrete voice, liveliness, and genre-appropriate language constraints.
- Add reset guidance when prior context, NSFW/special scenes, or example content could drift the style.

### Phase 5: Quality Gate

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

### Phase 6: Final Output

Return, in this order:

1. `<writing_style>` XML in a fenced XML code block.
2. Optional separate `<tone>` block only if the user requested plot tone / story trajectory control.
3. `【引用出处】` list.
4. `【选段理由】` list.
5. `【质检记录】` summary.

Do not say “use artifact.” In Claude Code terminal contexts, output the XML directly or ask whether the user wants it saved as a file.

## Error Handling

| Situation | Handling |
|---|---|
| Not enough original excerpts | Mark `基于有限资料`, reduce examples to 4, and explain the limitation. |
| Multiple style periods | Mark periodization in `<categories>` and avoid flattening the author into one style. |
| Search fails | Ask the user for text samples or a representative work. |
| User supplies only a style description | Generate a non-author or synthetic profile and label the evidence source. |
| User asks for AIRP practical prompt | Preserve `<writing_style>` XML, and add model notes / reset rules rather than uncontrolled prose. |
| User asks for examples to teach style | Use short evidence excerpts in XML; put any longer style demonstration outside XML with copyright and plot-borrowing limits. |
| Copyright-sensitive long text requested | Use short excerpts, summaries, and citations rather than reproducing long passages. |

## Common Mistakes

- Do not invent original excerpts.
- Do not translate examples when the rule requires author-language originals.
- Do not skip citations or selection rationale.
- Do not output literary commentary without executable writing parameters.
- Do not omit any XML system: narrative, expression, aesthetics, or prompt discipline.
- Do not let style fields command future events, relationship progress, or endings.
- Do not use author names as a substitute for concrete writing rules.
- Do not turn example scenes into reusable plot material.
- Do not rely on high-risk labels such as “羞耻”, “疯感”, “破碎”, or “压抑” without behaviorized replacements.
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
