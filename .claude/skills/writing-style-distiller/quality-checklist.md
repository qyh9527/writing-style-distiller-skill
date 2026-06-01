# Quality Checklist

Run this checklist before final output. Fix failures before responding.

## A. Theoretical Accuracy

- [ ] Narrative person, focalization, and narrative distance are separated.
- [ ] Temporality distinguishes order, duration, and frequency.
- [ ] The narrative, expression, and aesthetics systems do not contradict one another.
- [ ] Each parameter is supported by at least one example, citation, or stated evidence limitation.
- [ ] Critical terms are used precisely rather than as decorative labels.

## B. Cultural Fit

- [ ] Aesthetic terms come from the relevant literary or cultural tradition when possible.
- [ ] Source-language terms are preserved when translation would flatten the concept.
- [ ] Western theory is not imposed when indigenous or genre-specific concepts explain the evidence better.
- [ ] Every `example` remains in the author's writing language unless the source is unavailable and the limitation is stated.

## C. Executability

- [ ] Each XML attribute can directly guide generation behavior.
- [ ] Positive instructions and negative constraints both appear where useful.
- [ ] Vague praise words are removed: `独特的`, `善于`, `富有`, `常用`, `巧妙地`.
- [ ] The output is not just literary criticism; it is a usable writing-control profile.
- [ ] No required XML section is missing.

## D. Length and Density

- [ ] Target final XML length is approximately 950-1050 tokens when feasible.
- [ ] If overlong, compress attributes, categories, and explanatory wording first.
- [ ] Do not compress, paraphrase, or truncate `example` excerpts merely to save space.
- [ ] If too short, add concrete markers, categories, or language constraints rather than filler.
- [ ] Report length as an estimate unless an actual token-counting tool was run.

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

- No reliable source-language excerpts are available.
- The author or target style cannot be identified.
- The user requests exact imitation of a living author's style without enough permitted source material; offer a high-level, non-infringing style profile instead.
