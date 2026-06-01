# Prompt Optimization Rules

Use these rules to turn literary analysis into strong, practical writing-control prompts. The goal is not a prettier critique; the goal is a profile that resists drift, cliche, model overreach, and plot contamination.

## 1. Separate Style, Affective Baseline, and Plot Tone

| Concept | Controls | Belongs in `<writing_style>`? |
|---|---|---|
| Writing style | wording, syntax, narration, dialogue, paragraphing, sensory selection, rhythm | Yes |
| Affective baseline | reader-facing color such as light, quiet, bitter, playful, restrained | Yes, if it changes presentation only |
| Plot tone | future event direction, healing/tragic arc, relationship outcome, fate, ending tendency | No; use separate `<tone>` only when requested |

Rules:

- Write style rules as “how to present whatever happens.”
- Do not write style rules as “what should happen next.”
- In `progression`, describe single-response movement only: contrast, zoom, pause, acceleration, turn, or local escalation.
- In `ending`, describe local closure only: image, gesture, unfinished beat, crisp punchline, withheld explanation.
- If the user asks for both style and tone, output `<writing_style>` first and a separate `<tone>` block second.

## 2. Prefer Abstract Rules That Cover a Class of Effects (Primary Principle)

This is the single most important rule for style prompt quality. Every other rule improves a prompt; this one determines whether the prompt works at all.

A strong style prompt says **how to write a class of scenes**, not which scene to write. AI-generated style prompts almost always fail here: they enumerate specific scenarios instead of abstracting the method. After writing each rule, ask: **"Does this describe a writing method, or does it list a scenario?"**

Bad — enumerates scenes:

```text
Write toothpaste squeezing, subway commuting, pillow fights, weekend bed scenes, and checking messages.
```

Bad — explains why the rule matters:

```text
The language should feel light because the reader needs to feel as if the scene is breathing and the characters are alive in a very vivid way.
```

Good — abstracts the method:

```text
Focus on ordinary domestic actions; let concrete routines reveal relationship texture without turning the routine into a required plot event.
```

Good — operational, no explanation:

```text
Use light colloquial clauses, quick turn-taking, and small interruptions to keep the scene breathing.
```

Decision flow for every rule:

1. Does the rule name a specific object, event, or scenario? → Move it to an example or remove it.
2. Does the rule explain its own importance? → Delete the explanation, keep the instruction.
3. Can the rule be expressed in one sentence starting with a verb? → Rewrite it that way.
4. Does the rule cover all instances of a class, or only the one that appeared in the sample? → Widen it to the class.

Checklist:

- Keep concrete objects and events inside examples, not hard rules.
- Extract the method behind the example: pacing, focalization, sensory hierarchy, dialogue rhythm, paragraph shape.
- If a rule names a specific object, ask whether the object is required by the style or merely appeared in a sample.
- If two rules describe the same method applied to different scenes, merge them into one class-level rule.

## 3. Positive Instructions First, Negative Guardrails Second

Use this order:

1. What to do.
2. What to avoid.
3. What to do instead when avoiding it.

Bad:

```text
Do not use grand metaphors. Do not overexplain. Do not write cliche warmth.
```

Good:

```text
Use concrete household-scale images and small bodily actions to carry warmth. Avoid grand metaphors such as stars, abyss, and destiny; replace them with objects the character can touch or notice in the current scene.
```

Rules:

- Negative instructions without replacements are weak and can become reverse prompts.
- Put the desired behavior in `positive`; put minimal prohibitions in `negative`.
- Do not stack many “avoid” lines when one positive principle can cover them.

## 4. Control Extreme Words

Extreme words include `must`, `always`, `never`, `absolutely`, `必须`, `一定`, `绝对`, `强制`.

Use them only for:

- Format rules: quote marks, XML shape, paragraph separation.
- True prohibitions: no fabricated citations, no long copyrighted excerpts, no plot borrowing from examples.
- User-stated hard requirements.

Prefer softer operational verbs for style tendencies:

- prefer, reduce, foreground, delay, compress, withhold, alternate, separate, lean toward, avoid by default.

Why: too many extreme words make the model over-attend to the prompt, stiffen the prose, or repeat the instruction language.

## 5. Convert High-Risk Labels Into Behavior

Some labels trigger model cliches or extreme continuations. Do not rely on the label alone.

| Risk label | Possible failure | Behaviorized replacements |
|---|---|---|
| 羞耻 / shame / embarrassment | blush-collapse loops, stammering, loss of agency | delayed reply, topic deflection, clipped syntax, self-protective gesture, controlled silence, boundary assertion |
| 破碎 / broken | melodramatic collapse, helplessness | fragmented paragraph rhythm, withheld explanation, practical action under strain |
| 疯感 / madness | random cruelty, incoherence | rule-breaking syntax in limited bursts, obsessive motif recurrence, unstable attention shifts |
| 压抑 / repression | abstract sadness, heavy narration | shortened sensory field, routine actions, unsaid dialogue, constrained verbs |
| 温柔 / warmth | generic healing, forced sweetness | concrete care actions, softened pacing, attentive object memory, low-pressure dialogue |
| 活人感 / liveliness | random jokes, modern slang overload | context-fitting interruption, partial answers, small contradictions, practical priorities |

Rules:

- Keep the label only as a compact heading if useful.
- The executable part must be observable in text: dialogue, action, syntax, paragraphing, sensory focus, narrative distance.
- If target model is Gemini, reduce labels further and add examples or behavior lists.

## 6. Model Adaptation

### General

- Avoid using author names as final instructions. Author names are evidence sources.
- Replace “reference X” with concrete features: sentence length, transition words, focalization, dialogue layout, sensory hierarchy.
- Keep examples from driving plot content.

### Gemini-oriented profiles

Gemini often over-expands abstract labels into extreme high-frequency patterns.

Use:

- More behaviorized rules.
- Fewer personality/emotion labels.
- Clear positive replacements after every ban.
- Short style examples or example-flow blocks when allowed.
- Explicit “do not inherit plot, objects, relationships, or scene order from examples.”

Avoid:

- Dense abstract tags like “羞耻、病态、崩溃、疯感” without behavior rules.
- Repeated extreme words that make the prose rigid.
- Letting “warmth” become forced healing or “sadness” become inevitable tragedy unless a separate tone asks for it.

### Claude-oriented profiles

Claude can overproduce polished literary sameness, especially in contemporary non-combat scenes.

Use:

- Concrete voice constraints: colloquial register, character-specific diction, practical dialogue interruptions.
- Genre-specific liveliness: jokes, argument rhythm, mundane priorities, action beats, if supported by the target style.
- Anti-overinterpretation rules: present facts and gestures; do not explain every emotional meaning.

Avoid:

- Too many solemn abstractions.
- Excessive lyrical transitions.
- Homogenized “quiet, delicate, wistful” prose when the requested style is energetic, comic, vulgar, light-novel, or genre-forward.

## 7. Example Strategy

There are two different example types:

| Type | Purpose | Placement |
|---|---|---|
| Evidence excerpt | Supports a schema field and citation | Inside XML `<example>` |
| Style demonstration sample | Teaches flow, scene-level rhythm, or example-flow prompting | Outside XML unless user asks for a prompt package |

Evidence excerpt rules:

- Keep short, source-language, cited.
- Use as proof of analysis, not as a scene template.

Style demonstration sample rules:

- Prefer user-provided, authorized, public-domain, or newly written samples.
- Use a complete micro-scene when teaching flow; isolated pretty sentences are weaker.
- State: “Examples guide expression only, not plot events.”
- Extract sentence movement, paragraphing, dialogue rhythm, sensory order, and tone of narration.
- Do not reuse character identities, setting sequence, relationship arc, conflict, signature objects, or event order.

## 8. Paragraph Control

Paragraphing is part of writing style, not decoration.

Specify:

- Paragraph unit: dialogue line, action beat, sensory beat, monologue turn, or mixed unit.
- Length tendency: short fragments, 10-50 character beats, medium blocks, long flowing paragraphs, or alternating pattern.
- Dialogue separation: independent dialogue paragraphs vs dialogue embedded with action.
- Transition logic: when emotion/action causes paragraphs to shorten or lengthen.

Examples of executable paragraphing rules:

- “Use independent dialogue paragraphs; attach action beats before or after, not inside every line.”
- “Shorten paragraphs during banter or conflict; lengthen them when attention settles on touch, weather, or interior monologue.”
- “Use sparse single-sentence paragraphs for withheld emotion; avoid explaining the silence immediately.”

## 9. Context Drift and Reset Rules

AIRP / roleplay contexts can drift because history, special scenes, NSFW modules, or examples overpower the current style.

### Drift Mechanisms

Style drift is not a single event but a progressive cycle:

1. **Module injection drift**: entering NSFW/special scenes loads additional writing directives that the model has not seen before, causing immediate style displacement.
2. **Micro-contamination loop**: after exiting a special scene, the model does not fully restore the prior style. It enters a transitional state (e.g., low-level eroticized framing) that gradually pulls the next scene back toward the special mode. Multiple cycles amplify the drift.
3. **History inertia**: the model learns from recent context and tries to maintain consistency, which locks in drifted style even after the trigger is removed.

### Reset Strategy

Use `reset_rule` to counter all three mechanisms:

- After special or NSFW scenes, restore the general style on the **next normal scene** — do not wait for style to self-correct.
- Treat previous scene-specific vocabulary as local unless the user repeats it.
- If history conflicts with the current style profile, follow the current profile for narration, paragraphing, and language.
- Use examples as expression references only; do not continue their plot state.
- For AIRP presets: consider adding a two-step restoration — an explicit exit prompt from the user, plus a style-correction instruction on the immediately following response.

Example reset rule:

```text
After any special-scene style module ends, restore this profile's narration, paragraphing, and lexicon on the next response; keep only factual continuity from history, not its temporary diction or eroticized framing.
```

## 10. Compression Pass

Before final output, compress for token efficiency. Follow this priority order — cut what matters least first:

Priority 1 — Delete explanatory sentences (“because...”, “this is to ensure...”, “the reader will feel...”). Keep the instruction, drop the justification.

Priority 2 — Merge duplicate goal statements. If three sections all say “make the reader feel warmth,” keep it in one place and remove the other two.

Priority 3 — Remove decorative modifiers that add no operational meaning (“very,” “truly,” “extremely,” “非常,” “十分”).

Priority 4 — Replace multi-sentence rules with single-sentence instructions starting with a verb.

Priority 5 — Keep the strongest example for each field. Cut weaker duplicate examples.

Priority 6 — Preserve concrete markers, paragraph rules, and dialogue rules before cutting aesthetic adjectives. Operational specifics have higher value than atmospheric descriptions.

Token efficiency principle: one well-chosen example teaches more than three sentences of vague description. When cutting for space, prefer keeping examples over keeping rule explanations.

Bad:

```text
The language should feel light because the reader needs to feel as if the scene is breathing and the characters are alive in a very vivid way.
```

Good:

```text
Use light colloquial clauses, quick turn-taking, and small interruptions to keep the scene breathing.
```
