# Writing Style Distiller Skill Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create a maintainable Claude Code project skill that converts the existing `文风蒸馏器.md` prompt into a reusable writing-style distillation workflow.

**Architecture:** Use a B-lite modular skill: `SKILL.md` contains discovery triggers and workflow rules; three supporting files isolate XML schema, quality checks, and citation/example rules. Verification uses skill-documentation TDD: record baseline failure modes, write the skill, then check the skill covers those failures.

**Tech Stack:** Markdown, Claude Code skill specification, local git worktree.

---

## File Structure

- Create: `.claude/skills/writing-style-distiller/SKILL.md` — main skill entry point and invocation guidance.
- Create: `.claude/skills/writing-style-distiller/output-schema.md` — canonical `<writing_style>` XML schema and field rules.
- Create: `.claude/skills/writing-style-distiller/quality-checklist.md` — theory, culture, executability, and length checks.
- Create: `.claude/skills/writing-style-distiller/citation-and-examples.md` — citation, original-language excerpt, and selection-rationale rules.
- Create: `.claude/skills/writing-style-distiller/verification-notes.md` — RED/GREEN/REFACTOR notes for this skill.

### Task 1: RED Verification Notes

**Files:**
- Create: `.claude/skills/writing-style-distiller/verification-notes.md`

- [ ] **Step 1: Create baseline failure notes**

Write a concise baseline note listing expected failures without this skill:

```markdown
# Verification Notes

## RED: Baseline Failure Modes Without Skill

A general prompt-to-skill conversion tends to fail in these ways:

1. Writes frontmatter description as a workflow summary instead of trigger conditions.
2. Copies the original prompt verbatim instead of turning it into operational skill guidance.
3. Omits local-text and excerpt-input modes, treating every request as an author-name search.
4. Keeps “artifact” output wording, which is not reliable in Claude Code terminal use.
5. Claims strict token verification without an actual token-counting tool.
6. Weakens citation discipline and permits translated or invented examples.
7. Forgets a final quality gate for theory accuracy, cultural fit, and executability.

## GREEN Criteria

The completed skill must explicitly prevent each failure above.
```

- [ ] **Step 2: Commit baseline notes**

Run:

```bash
git add .claude/skills/writing-style-distiller/verification-notes.md
git commit -m "test: record writing style skill baseline failures"
```

Expected: commit succeeds.

### Task 2: Main Skill Entry Point

**Files:**
- Create: `.claude/skills/writing-style-distiller/SKILL.md`

- [ ] **Step 1: Create `SKILL.md`**

Use frontmatter with trigger-only description:

```markdown
---
name: writing-style-distiller
description: Use when generating, distilling, or analyzing writing style configurations from an author name, literary text file, excerpt samples, or style description
---

# Writing Style Distiller

## Overview

Generate an executable `<writing_style>` XML configuration from an author name, literary text, excerpt samples, or a style description. Treat the result as a writing-control profile: every field must guide future AI writing, not merely summarize literary criticism.

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
```

- [ ] **Step 2: Commit main skill file**

Run:

```bash
git add .claude/skills/writing-style-distiller/SKILL.md
git commit -m "feat: add writing style distiller skill entry"
```

Expected: commit succeeds.

### Task 3: Supporting Reference Files

**Files:**
- Create: `.claude/skills/writing-style-distiller/output-schema.md`
- Create: `.claude/skills/writing-style-distiller/quality-checklist.md`
- Create: `.claude/skills/writing-style-distiller/citation-and-examples.md`

- [ ] **Step 1: Create schema reference**

Create `output-schema.md` with canonical XML and field rules.

- [ ] **Step 2: Create quality checklist**

Create `quality-checklist.md` with theory, culture, executability, and length checks.

- [ ] **Step 3: Create citation and examples guide**

Create `citation-and-examples.md` with original-language excerpt constraints and citation format.

- [ ] **Step 4: Commit supporting files**

Run:

```bash
git add .claude/skills/writing-style-distiller/output-schema.md .claude/skills/writing-style-distiller/quality-checklist.md .claude/skills/writing-style-distiller/citation-and-examples.md
git commit -m "feat: add writing style distiller references"
```

Expected: commit succeeds.

### Task 4: GREEN/REFACTOR Verification

**Files:**
- Modify: `.claude/skills/writing-style-distiller/verification-notes.md`
- Modify if needed: `.claude/skills/writing-style-distiller/SKILL.md`
- Modify if needed: supporting files

- [ ] **Step 1: Check GREEN criteria**

Verify each RED failure mode is addressed:

1. Description is trigger-only.
2. Skill converts prompt into operational workflow.
3. Input routing includes author, file, excerpts, and style description.
4. Final output avoids artifact dependency.
5. Token verification is honest.
6. Citations and original examples are mandatory.
7. Quality gate is explicit.

- [ ] **Step 2: Append verification result**

Append:

```markdown
## GREEN: Skill Coverage Check

- Trigger-only description: covered in `SKILL.md` frontmatter.
- Operational workflow: covered by phases 1-4.
- Input routing: covers author, representative work, local file, excerpts, and style description.
- Terminal-compatible output: final XML is emitted directly; artifacts are not required.
- Honest length validation: token count is marked as estimate unless a tool is run.
- Citation discipline: covered in `citation-and-examples.md`.
- Final quality gate: covered in `quality-checklist.md`.

## REFACTOR Notes

The skill uses four files to keep maintenance simple: workflow, schema, quality, and citation rules. No additional scripts are needed for the first version.
```

- [ ] **Step 3: Commit verification result**

Run:

```bash
git add .claude/skills/writing-style-distiller
git commit -m "test: verify writing style distiller skill coverage"
```

Expected: commit succeeds.

## Self-Review

- Spec coverage: plan creates the exact B-lite structure from the design and adds verification notes.
- Placeholder scan: no TBD/TODO placeholders remain.
- Scope check: no GitHub push or global skill installation included.
