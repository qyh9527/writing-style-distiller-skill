# Citation and Example Rules

## Original-Language Examples

Examples are evidence, not decoration.

Rules:

- Use the author's source language whenever available.
- Keep each XML `example` between 30 and 80 characters when possible.
- Do not paraphrase, translate, or compress an example while still presenting it as original text.
- If only translation is available, label it as translation and explain the limitation outside the XML.
- Use short excerpts only. Do not reproduce long copyrighted passages.
- State when evidence comes from user samples, synthetic descriptions, or limited sources.

## Two Example Types

Do not mix evidence excerpts with style demonstration samples.

| Type | Purpose | Where it belongs | Risk |
|---|---|---|---|
| Evidence excerpt | Proves a field-level style claim | XML `<example>` and citation list | Weak if uncited or paraphrased |
| Style demonstration sample | Shows scene-level flow, paragraph rhythm, and example-flow prompting | Outside XML, only when requested | Can contaminate plot, objects, relationships, and scene order |

### Evidence Excerpts

Use evidence excerpts for XML fields:

- Keep them short and source-language.
- Tie each excerpt to one field: rhythm, paragraphing, description, dialogue, characterization, sensory hierarchy, telos.
- Extract only the relevant writing method.
- Do not convert excerpt content into mandatory plot material.

### Style Demonstration Samples

Use style demonstration samples only when the user requests example-flow prompting or when the model target benefits from examples.

Rules:

- Prefer user-provided, authorized, public-domain, or newly written samples.
- Use a complete micro-scene when teaching flow; isolated decorative sentences are weaker.
- Put demonstration samples outside XML unless the user explicitly asks for a packaged prompt.
- Add a boundary statement: `文风示例仅供表达方式参考，不为正文具体内容提供情节借鉴。`
- Extract sentence movement, paragraphing, dialogue rhythm, sensory order, focalization, and narration tone.
- Do not borrow character identities, relationship arcs, event order, conflict, setting sequence, signature objects, or plot outcomes.

## Minimum Evidence Targets

When sources are available, collect at least 6 excerpt candidates covering:

| System | Evidence target |
|---|---|
| Narrative | perspective, temporal handling, rhythm, structural movement, paragraphing |
| Expression | description, dialogue, characterization, sensory hierarchy |
| Aesthetics | core concepts, symbolic palette, language texture, telos |
| Prompt discipline | risky labels, anti-cliche constraints, model-specific failure modes when relevant |

If fewer than 6 source-language excerpts are available, mark `基于有限资料` and reduce XML examples to the strongest 4.

## Citation Format

Prefer precise bibliographic citations:

```text
【引用出处】
[1] 『作品名』第X章/第X巻, 出版社, 年, p.XX / 位置No.XXX.
[2] Author, "Article Title," Journal/Publisher, Year, page or URL.
```

For web sources, include title, site, URL, and access date when available.

```text
[3] "Page Title," Site Name, URL, accessed 2026-06-01.
```

## Selection Rationale Format

Explain why each excerpt was selected:

```text
【选段理由】
rhythm.example：选自[作品/章节]，展现[节奏、句法、时距或推进特征]。
paragraphing.example：选自[作品/章节]，展现[段落单位、长短交替或对话分段规则]。
description.example：选自[作品/章节]，展现[描写原则或感官层级]。
dialogue.example：选自[作品/章节]，展现[对话模式]。
characterization.example：选自[作品/章节]，展现[人物塑造或心理策略]。
sensory.example：选自[作品/章节]，展现[感官优先级]。
telos：依据[作品/评论]，说明[美学目标]。
prompt_discipline：依据[用户要求/模型目标/样本风险]，说明[标签转写、示例边界或重置规则]。
```

## Evidence Honesty

Use these labels when needed:

- `基于有限资料` — reliable evidence is sparse.
- `译文可得，原文未核验` — translation is available but original text was not verified.
- `用户样本文本` — evidence comes from user-provided text rather than external publication.
- `综合风格描述` — profile is synthetic and not tied to a single author.
- `示例流演示` — sample is used to teach flow and must not be treated as plot evidence.
- `模型适配规则` — rule is based on target-model behavior rather than source-text evidence.

Never fabricate citations, page numbers, source-language excerpts, or permissions.

## Plot-Borrowing Guard

Before final output, check every example-derived rule:

- Keep: syntax, lexicon, rhetorical device, rhythm, paragraph shape, sensory order, dialogue mode, focalization, narrative distance.
- Remove or soften: named objects, plot sequence, scene premise, character relationship, event result, worldbuilding facts, erotic/violent framing from a special scene.
- If a concrete object is also a recurring symbol, mark it as optional motif rather than required content.

## Example-Flow Strategy

Example-flow is a style construction method that pairs a lightweight rule framework with high-quality demonstration samples. The rules provide abstract guidance; the samples teach paragraph rhythm, dialogue flow, and sensory movement. Swapping the sample changes the style flavor without rewriting the rules.

### When to Use Example-Flow

- Gemini-targeted profiles: Gemini responds strongly to concrete demonstration; abstract rules alone often trigger label-chain distortion.
- Token-constrained profiles: a compact rule framework (~300-400 tokens) plus one demonstration sample (~400 tokens) can stay under 1000 tokens total.
- Universal/swappable style frameworks: the same rule structure supports multiple flavors by exchanging the demonstration sample only.
- Zero-sample alternative: use the opening message / first response as an implicit demonstration sample instead of embedding one in the prompt.

### Sample Selection Criteria

- Use a complete micro-scene (action + dialogue + narration transition), not isolated decorative sentences.
- The sample must show paragraph rhythm, dialogue separation, and sensory order — the things rules describe abstractly.
- First-person samples should demonstrate the narrator's voice and interiority; third-person samples should demonstrate narrative distance and scene-building.
- Samples set affective baseline by implication: a sample from an erotic novel will color the entire style toward eroticism. Choose samples whose emotional register matches the intended style.

### Sample Sources

Prefer in this order:

1. User-provided text.
2. Public-domain or authorized published text.
3. Newly written demonstration text by the user or with explicit permission.
4. The opening message / first response used as an implicit sample (zero-sample approach).

### Boundary Statement

Every example-flow profile must include:

```text
文风示例仅供表达方式参考，不为正文具体内容提供情节借鉴。
```

### Rule Framework for Example-Flow

The rule framework should be abstract and genre-agnostic. Prefer analysis methods that a reader learned in school: narrative voice, paragraph structure, dialogue handling, descriptive priority, emotional register. The framework covers "how to write"; the sample shows "what it looks like."

### Comparison with Zero-Sample Profiles

| Dimension | Example-flow | Zero-sample |
|---|---|---|
| Token cost | Higher (~800-1000) | Lower, but heavier rules (~1100-1400) |
| Style stability | Sample anchors the style strongly | Rules must be more precise to compensate |
| Swappability | Change sample → change flavor | Must rewrite rules for each flavor |
| Best for | Gemini, universal frameworks, token-tight setups | Claude, detailed author-specific profiles |
