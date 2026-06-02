# Writing Style Distiller Claude Code Skill

[中文说明](README.md)

This repository contains a Claude Code project-level skill that converts an author name, literary text, excerpt samples, or a style description into an executable `<writing_style>` configuration.

## v2.0 Key Features

- **Adaptive-depth pipeline**: automatically selects deep/standard/fast mode (4/3/2 phases) based on input complexity
- **Multi-phase review gates**: each phase writes to disk; the user can intervene at every checkpoint
- **Lightweight output format**: XML shell + first-level XML section tags + plain-text content, replacing the heavy nested XML schema
- **Adaptive schema**: adjusts density by style family (emotion-expression / language-feature / narrative-structure / example-driven), targeting 600–1200 tokens
- **Separated knowledge base**: style-family taxonomy, high-risk label conversion table, and model adaptation rules managed independently

## v2.1 Updates

- **Clean output**: after the final phase of any mode, an additional clean xml code block containing only the `<writing_style>` (and optional `<tone>`) is output for easy copy-paste
- **Auto-cleanup of intermediate artifacts**: after the clean output, the intermediate artifact directory under `docs/style-output/` is automatically deleted to keep the workspace tidy

## v2.2 Updates

- **Anti-bagu knowledge base**: added `knowledge/anti-bagu.md` — systematically catalogues 6 types of formulaic patterns in AI-generated style prompts (unnecessary definitions, concrete scene enumeration, explanatory statements, formulaic rhetoric, over-expansion, incorrect example pairs), checked during Phase 3-4
- **Abstraction checks strengthened**: the abstraction-first principle now includes "one-sentence summarization test" and "unnecessary definition removal"; quality checklist section A updated accordingly
- **Intent probe**: a lightweight intent probing step is added between routing and Phase 1, using 1-2 anchoring questions (application scenario, aesthetic baseline, exclusion direction, structure vs. feel preference) to prevent distillation drift
- **Example-driven family expanded**: significantly expanded the example-driven family knowledge with example selection criteria (complete scene requirement, token reference budget, tonal influence, person-matching strategy, generic framework principle) and a reference framework
- **Persona-voice writing**: added as an optional path, documenting implementation points for writing style rules in the author's/work's voice, translator interference, character conflict, and other considerations
- **Compression priority expanded**: Phase 4 compression table expanded from 6 to 8 items, inserting summarization test and definition removal steps

## Contents

```text
.claude/skills/writing-style-distiller/
├── SKILL.md                    # Entry point: adaptive routing + workflow dispatch
├── output-format.md            # Output format definition + full example
├── quality-checklist.md        # 5-dimension quality checklist
├── verification-notes.md       # Verification notes
├── phases/
│   ├── research.md             # Phase 1: Research & evidence collection
│   ├── diagnosis.md            # Phase 2: Style diagnosis & architecture
│   ├── drafting.md             # Phase 3: Style draft generation
│   └── optimization.md         # Phase 4: Optimization & quality gate
└── knowledge/
    ├── style-families.md       # Style family taxonomy & density table
    ├── label-risk-table.md     # High-risk label behaviorization table
    ├── model-adaptation.md     # Claude/Gemini model adaptation rules
    └── anti-bagu.md            # Anti-formulaic style prompt guide
```

Other files:

- `文风蒸馏器.md`: organized source prompt (Chinese).

## Installation

### Download zip packages from GitHub Releases

The recommended installation path is to download ready-made zip packages from this repository's [GitHub Releases](https://github.com/qyh9527/writing-style-distiller-skill/releases):

- `writing-style-distiller-agent.zip`: generic Agent/Skill package for IDEs or agent tools that can import an agent/skill folder.
- `writing-style-distiller-claude-code-project-skill.zip`: Claude Code project-level skill package that can be extracted into a target project root.

The generic package extracts to:

```text
writing-style-distiller/
├── SKILL.md
├── output-format.md
├── quality-checklist.md
├── verification-notes.md
├── phases/
│   ├── research.md
│   ├── diagnosis.md
│   ├── drafting.md
│   └── optimization.md
└── knowledge/
    ├── style-families.md
    ├── label-risk-table.md
    └── model-adaptation.md
```

The Claude Code project-level package extracts to:

```text
.claude/
  skills/
    writing-style-distiller/
      SKILL.md
      output-format.md
      quality-checklist.md
      verification-notes.md
      phases/
        research.md
        diagnosis.md
        drafting.md
        optimization.md
      knowledge/
        style-families.md
        label-risk-table.md
        model-adaptation.md
```

### Use as a project-level skill

1. Clone or download this repository.
2. Open the repository root in Claude Code.
3. Confirm that this file exists:

```text
.claude/skills/writing-style-distiller/SKILL.md
```

Claude Code discovers skills from the project's `.claude/skills/` directory. After that, you can request `writing-style-distiller` directly within this project.

### Install as a global skill

If you want to use this skill from other projects, copy the skill directory into Claude Code's global skills directory:

```text
~/.claude/skills/writing-style-distiller/
```

On Windows, this usually maps to:

```text
C:\Users\<your-username>\.claude\skills\writing-style-distiller\
```

After copying, confirm that the global directory contains:

```text
~/.claude/skills/writing-style-distiller/SKILL.md
```

## Usage

In a Claude Code environment that supports project-level skills, you can ask:

```text
Use writing-style-distiller to generate a writing style config for Yasunari Kawabata.
```

Or:

```text
Use writing-style-distiller to analyze this text file's writing style and output <writing_style>.
```

The skill automatically detects input type and selects the appropriate depth mode (deep/standard/fast). Each phase writes intermediate artifacts to `docs/style-output/` and pauses at a review gate to wait for your confirmation. After the final phase, a clean `<writing_style>` code block is output for direct copying, and intermediate artifacts are automatically cleaned up.

## Source and Attribution

This project is based on original content by Yandhi酱 and adapts it into a Claude Code skill.

- Original author: Yandhi酱
- Discord ID: `y_a_n_d_h_i`
- Original post: https://discord.com/channels/1291925535324110879/1423575785360326716
- Original timestamp: 2025/11/20 22:40

The author also stated that users may directly use it when needed, without privately requesting authorization.

## Known Usage Conditions

Based on currently known information:

| Item | Status |
|---|---|
| Commercial use | Prohibited |
| Redistribution within the community | Allowed |
| Modification within the community | Allowed |
| Backup by management/group administrators | Allowed |
| Attribution to the original author | Required |
| Direct use without privately requesting authorization | Allowed |

## License and Restrictions

This repository is not released under a standard open-source license. Because the original author's complete license terms are not confirmed, this repository does not use MIT, Apache-2.0, GPL, or any other standard open-source license.

Unless the original author grants additional permission, this repository and its derivative adaptation are for non-commercial use only. When redistributing, modifying, or backing up this work, keep attribution to Yandhi酱, the Discord ID, the original post link, and the original timestamp.

If the original author later publishes clearer or updated terms, the original author's latest statement should take precedence.

## Maintainer Note

The maintainer of this repository only organized, structured, and documented the material as a Claude Code skill. The maintainer does not claim ownership of the original content.
