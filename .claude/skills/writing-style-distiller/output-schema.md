# Output Schema

Use this XML structure exactly. Fill every field unless evidence is explicitly unavailable.

```xml
<writing_style author="[author-or-style-name]" source="[author/text/samples/synthetic]" mode="[style-only/style-with-affective-baseline]">

  <control_scope>
    style: [what this profile controls: wording, narration, paragraphing, rhythm, dialogue, sensory selection]
    tone: [state whether plot tone is excluded or supplied separately]
    examples: [state examples guide expression only, not plot events]
  </control_scope>

  <narrative_system>
    <structure type="[use/avoid/prefer + structure type]" progression="[single-response movement rule, not future plot trajectory]" ending="[local closure style, not prescribed story ending]"/>
    <perspective>
      [person / focalization type / narrative distance]
      markers: [3-6 concrete markers, comma separated]
    </perspective>
    <temporality>[order / duration / frequency rules]</temporality>
    <rhythm pattern="[use/avoid/prefer + rhythm pattern]" pacing="[use/avoid/prefer + pacing rule]">
      <example>[30-80 characters, original language]</example>
    </rhythm>
    <paragraphing unit="[preferred paragraph unit]" length="[short/medium/long pattern]" dialogue="[dialogue and narration separation rule]" transition="[how paragraph length changes with emotion/action]">
      <example>[30-80 characters, original language]</example>
    </paragraphing>
  </narrative_system>

  <expression_system>
    <description style="[use/avoid/prefer + descriptive style]" principle="[use/avoid/prefer + selection principle]">
      <example>[30-80 characters, original language]</example>
    </description>
    <dialogue mode="[use/avoid/prefer + dialogue mode]">
      <example>[30-80 characters, original-language dialogue]</example>
    </dialogue>
    <characterization method="[use/avoid/prefer + characterization method]" psychology="[use/avoid/prefer + psychological strategy]">
      <example>[30-80 characters, original language]</example>
    </characterization>
    <sensory hierarchy="[ordered sensory priorities]">
      <example>[30-80 characters, original language]</example>
    </sensory>
  </expression_system>

  <aesthetics_system>
    <core>[3-5 core aesthetic concepts separated by slashes]</core>
    <categories types="[classification dimensions]">[features of each category, including periodization if needed]</categories>
    <palette>
      place: [typical spaces as aesthetic evidence, not mandatory scene requirements]
      time: [typical times as atmosphere evidence, not mandatory chronology]
      symbol: [core images as optional motifs, not required plot objects]
    </palette>
    <language>
      syntax: [sentence and clause patterns]
      lexicon: [word preferences and exclusions]
      rhetoric: [rhetorical devices]
    </language>
    <telos>[aesthetic goal with original-language evidence]</telos>
  </aesthetics_system>

  <prompt_discipline>
    <positive>[primary positive writing instructions]</positive>
    <negative>[minimal negative guardrails with positive replacements]</negative>
    <label_risk>[high-risk labels and their behaviorized replacements]</label_risk>
    <model_notes target="[general/gemini/claude/other]">[model-specific adaptation rules]</model_notes>
    <reset_rule>[how to restore style after context drift, special scenes, or example contamination]</reset_rule>
  </prompt_discipline>

</writing_style>
```

If the user explicitly requests plot tone / story trajectory control, output a separate companion block after `<writing_style>`:

```xml
<tone name="[tone-name]">
  baseline: [short affective or plot baseline]
  event_handling: [how positive and negative events should be emotionally processed]
  emotional_logic: [trajectory tendency]
  limitation: [state this controls plot tone, not wording]
</tone>
```

## Three-Layer Architecture Mapping

This schema maps to the community-standard three-layer model: 基调 (aesthetic foundation) + 文体特征 (stylistic features / reader experience) + 叙述规则 (narrative rules / writing technique).

| Community layer | Schema mapping | Purpose |
|---|---|---|
| 基调 | `<core>`, `<telos>`, `<control_scope>`, `mode` attribute | The highest-level aesthetic pursuit and creative foundation. What the style is fundamentally trying to achieve. |
| 文体特征 | `<aesthetics_system>`, `<sensory>`, `<characterization>`, `<palette>` | The reader experience the style produces: atmosphere, emotional texture, descriptive stance, sensory priorities. |
| 叙述规则 | `<narrative_system>`, `<expression_system>`, `<language>`, `<paragraphing>` | Concrete writing techniques: sentence structure, dialogue handling, paragraph layout, perspective, temporal logic. |

The `<prompt_discipline>` section serves all three layers by enforcing operational constraints and model-specific adaptations.

## Field Rules

| Field | Rule |
|---|---|
| XML attributes | Short executable instructions. Prefer verbs: use, avoid, prefer, delay, foreground, compress, withhold. |
| `source` | Use `author`, `text`, `samples`, or `synthetic`; mark limitations outside XML. |
| `mode` | Use `style-only` unless the user asks for reader-facing affective baseline inside the style. Do not use it for plot trajectory. |
| `control_scope` | State the profile's jurisdiction. It must explicitly prevent examples and style rules from steering future plot. In AIRP contexts: style controls only "how to present"; character behavior logic belongs to char/user persona modules; anti-cliche correction belongs to the preset's base module; plot direction belongs to a separate `<tone>` block or user control. |
| `structure.progression` | Describe movement inside a single generated response: escalation, pause, contrast, zoom, or transition. Do not prescribe long-term story development. |
| `structure.ending` | Describe local closure style: open pause, crisp turn, lingering image, withheld explanation. Do not prescribe final story outcomes. |
| `perspective` | Distinguish grammatical person, focalization, and narrative distance. Do not treat focalization as a synonym for point of view. |
| `temporality` | Distinguish order, duration, and frequency. Do not treat duration as chronology. |
| `paragraphing` | Specify paragraph unit, length pattern, dialogue separation, and transition logic. This is required for AIRP / roleplay / dialogue-heavy styles. |
| `example` | Use source-language excerpts. Keep 30-80 characters when possible. Do not compress or paraphrase examples. |
| `markers` | Provide 3-6 observable words, particles, syntactic cues, punctuation cues, or discourse markers. |
| `core` | Provide 3-5 keywords separated by slashes. These may include aesthetic baseline, not plot tone. |
| `categories` | Use period, genre, narrator type, theme, or aesthetic mode only when supported by evidence. |
| `palette` | Treat place/time/symbol as optional aesthetic tendencies, not required scene content. |
| `language` | Separate syntax, lexicon, and rhetoric. Prefer concrete constraints over author-name shorthand. |
| `telos` | State what the style tries to make the reader experience, and tie it to evidence. |
| `prompt_discipline.positive` | Tell the model what to do first. Positive rules should carry the main behavior. |
| `prompt_discipline.negative` | Use as guardrails only. Pair each prohibition with a replacement behavior. |
| `prompt_discipline.label_risk` | Convert risky emotion/personality labels into observable behavior, dialogue, paragraphing, or narration rules. |
| `prompt_discipline.model_notes` | Include only when model target matters. Gemini usually needs label-risk reduction and examples; Claude may need anti-homogenization and livelier concrete voice. |
| `prompt_discipline.reset_rule` | Add when prior context, NSFW/special scenes, or examples could pull the generated text away from the requested style. |

## Executability Test

A field passes only if another AI could use it to write in the target style. Replace vague labels with operational constraints.

Bad:

```xml
<description style="unique and rich">
```

Good:

```xml
<description style="foreground tactile detail before visual summary" principle="avoid abstract evaluation until after concrete objects">
```

Bad:

```xml
<structure progression="make the relationship become sweeter over time" ending="end in healing">
```

Good:

```xml
<structure progression="alternate quick dialogue beats with short sensory pauses inside each response" ending="close on a concrete gesture without deciding the future">
```

Bad:

```xml
<label_risk>羞耻但不要八股</label_risk>
```

Good:

```xml
<label_risk>replace 羞耻 with delayed replies, topic deflection, hand-covering action, clipped syntax; avoid blush-collapse loops</label_risk>
```
