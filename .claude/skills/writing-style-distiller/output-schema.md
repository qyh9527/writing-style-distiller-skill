# Output Schema

Use this XML structure exactly. Fill every field unless evidence is explicitly unavailable.

```xml
<writing_style author="[author-or-style-name]">

  <narrative_system>
    <structure type="[use/avoid/prefer + structure type]" progression="[use/avoid/prefer + progression rule]" ending="[use/avoid/prefer + ending rule]"/>
    <perspective>
      [person / focalization type / narrative distance]
      markers: [3-6 concrete markers, comma separated]
    </perspective>
    <temporality>[order / duration / frequency rules]</temporality>
    <rhythm pattern="[use/avoid/prefer + rhythm pattern]" pacing="[use/avoid/prefer + pacing rule]">
      <example>[30-80 characters, original language]</example>
    </rhythm>
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
      place: [typical spaces]
      time: [typical times]
      symbol: [core images]
    </palette>
    <language>
      syntax: [sentence and clause patterns]
      lexicon: [word preferences and exclusions]
      rhetoric: [rhetorical devices]
    </language>
    <telos>[aesthetic goal with original-language evidence]</telos>
  </aesthetics_system>

</writing_style>
```

## Field Rules

| Field | Rule |
|---|---|
| XML attributes | Short executable instructions. Prefer verbs: use, avoid, prefer, delay, foreground, compress, withhold. |
| `perspective` | Distinguish grammatical person, focalization, and narrative distance. Do not treat focalization as a synonym for point of view. |
| `temporality` | Distinguish order, duration, and frequency. Do not treat duration as chronology. |
| `example` | Use source-language excerpts. Keep 30-80 characters when possible. Do not compress or paraphrase examples. |
| `markers` | Provide 3-6 observable words, particles, syntactic cues, or discourse markers. |
| `core` | Provide 3-5 keywords separated by slashes. |
| `categories` | Use period, genre, narrator type, theme, or aesthetic mode only when supported by evidence. |
| `telos` | State what the style tries to make the reader experience, and tie it to evidence. |

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
