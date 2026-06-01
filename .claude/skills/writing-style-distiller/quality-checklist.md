# Quality Checklist

Run this checklist before final output. Fix failures before responding.

## A. Theoretical Accuracy

- [ ] Narrative person, focalization, and narrative distance are separated.
- [ ] Temporality distinguishes order, duration, and frequency.
- [ ] The narrative, expression, aesthetics, and prompt discipline systems do not contradict one another.
- [ ] Each parameter is supported by at least one example, citation, user-stated requirement, model-adaptation reason, or stated evidence limitation.
- [ ] Critical terms are used precisely rather than as decorative labels.
- [ ] Author names are treated as research/evidence sources, not as final executable instructions.

## B. Cultural Fit

- [ ] Aesthetic terms come from the relevant literary or cultural tradition when possible.
- [ ] Source-language terms are preserved when translation would flatten the concept.
- [ ] Western theory is not imposed when indigenous, genre-specific, or community-specific concepts explain the evidence better.
- [ ] Every XML `example` remains in the author's writing language unless the source is unavailable and the limitation is stated.
- [ ] Genre/community terms such as AIRP, light novel, 古白话, 二次元, or 示例流 are translated into executable writing behavior.

## C. Executability

- [ ] Each XML attribute can directly guide generation behavior.
- [ ] Positive instructions and negative constraints both appear where useful.
- [ ] Vague praise words are removed: `独特的`, `善于`, `富有`, `常用`, `巧妙地`.
- [ ] The output is not just literary criticism; it is a usable writing-control profile.
- [ ] No required XML section is missing: `control_scope`, `narrative_system`, `expression_system`, `aesthetics_system`, `prompt_discipline`.
- [ ] `markers` contains 3-6 observable markers, not abstract adjectives.
- [ ] `paragraphing` is explicit enough to guide dialogue, narration, and paragraph length.
- [ ] `label_risk` converts risky labels into observable behaviors, syntax, dialogue, paragraphing, or narration rules.

## D. Length and Density

- [ ] Target final XML length is approximately 1100-1400 tokens when the expanded schema is useful; shorter is acceptable for simple style-only requests.
- [ ] If overlong, compress attributes, categories, and explanatory wording first.
- [ ] Do not compress, paraphrase, or truncate `example` excerpts merely to save space.
- [ ] If too short, add concrete markers, paragraphing, label-risk replacements, or language constraints rather than filler.
- [ ] Report length as an estimate unless an actual token-counting tool was run.

## E. AIRP / Prompt Robustness

- [ ] `<writing_style>` controls presentation, not future plot trajectory.
- [ ] Affective baseline is not confused with plot tone.
- [ ] If plot tone is requested, it is separated into an optional `<tone>` block.
- [ ] `progression` describes movement inside one response, not long-term story development.
- [ ] `ending` describes local closure style, not final story outcome.
- [ ] Paragraph control explains dialogue/description separation, paragraph length, and transition logic.
- [ ] Abstract labels are replaced or backed by observable writing behaviors.
- [ ] Negative instructions have positive replacement behaviors.
- [ ] Extreme words such as `必须`, `绝对`, `强制`, `always`, and `never` are kept only for hard format rules or true prohibitions.
- [ ] Examples guide expression only; they do not lend plot, characters, relationship arcs, scene order, or signature objects.
- [ ] Concrete objects from samples are optional motifs unless evidence proves they are central symbols.
- [ ] If target model is Gemini, emotion/personality tags are reduced and behaviorized alternatives are added.
- [ ] If target model is Claude, anti-homogenization rules preserve liveliness, concrete voice, or genre-specific diction when needed.
- [ ] If prior context, NSFW/special scenes, or examples may drift the output, `reset_rule` restores the style profile.
- [ ] The profile favors reusable class-level rules over one-off event lists.

## F. Anti-AI-Generation Bias

AI-generated style prompts tend toward specific enumeration, over-explanation, and decorative rhetoric. Check for these patterns and fix them.

- [ ] No rule explains its own importance with "because the reader needs to feel..." or "this is to ensure..." — remove the explanation, keep the instruction.
- [ ] No rule enumerates specific scenes or objects when an abstract class-level principle would cover them. Ask: "does this rule describe a method, or does it list a scenario?"
- [ ] No section repeats the same goal statement that already appears in another section.
- [ ] No decorative AI rhetoric remains: phrases like "let the text breathe," "weave emotion," "paint with words," or "编织情感", "让文字呼吸", "赋予温度" are replaced with operational verbs.
- [ ] Each rule is one concise sentence. If a rule takes two or more sentences, the extra sentences are either redundant or belong in a separate rule.
- [ ] Example slots contain source-language excerpts, not AI-written illustrative prose.

## G. Citation and Example Integrity

- [ ] At least 6 excerpt candidates were considered when reliable sources are available.
- [ ] Fewer excerpts are explicitly labeled `基于有限资料`.
- [ ] Evidence excerpts and style demonstration samples are not mixed.
- [ ] Any longer demonstration sample is authorized, public-domain, user-provided, or newly written.
- [ ] Copyright-sensitive text is summarized or quoted only in short excerpts.
- [ ] Citations do not invent page numbers, URLs, permissions, or original-language text.
- [ ] Style demonstration samples (if used) show a complete micro-scene, not isolated decorative sentences.

## Quality Note Template

```text
【质检记录】
初稿长度估计：
问题（若有）：
修正操作：
终稿长度估计：
```

## Stop Conditions

Stop and ask the user for more material when:

- No reliable source-language excerpts are available and the user specifically requires author-grounded analysis.
- The author or target style cannot be identified.
- The user requests exact imitation of a living author's style without enough permitted source material; offer a high-level, non-infringing style profile instead.
- The user requests example-flow output but provides no usable samples and does not allow synthetic or public-domain demonstrations.
- The user asks for plot tone and style control together, but refuses to separate `<writing_style>` from `<tone>`.
