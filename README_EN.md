# Writing Style Distiller — Claude Code Skill

[中文说明](README.md)

Converts author names, literary texts, excerpts, or style descriptions into executable `<writing_style>` XML configurations.

## Key Features

- **Adaptive pipeline** — auto-selects deep/standard/fast mode (4/3/2 phases) with review gates
- **Six style families** — emotion-expression / language-feature / narrative-structure / example-driven / scene-responsive / dialogue-driven, with per-family density allocation
- **11-dimension quality checklist** — abstraction, format, scope boundary, robustness, language cleanliness, dynamic consistency, iron-rule effectiveness, register unity, person/POV, attention allocation, scene robustness
- **Model adaptation** — Claude comfort-zone breakthrough, Gemini label-chaining suppression, cross-model universal principles
- **Research-grade sourcing** — six-tier authority priority; academic databases and original texts preferred
- **Narrative perspective system** — Genette-based person × focalization taxonomy with POV-leak and head-hopping defenses
- **Anti-formula guide** — 12 categories of AI-generated formulaic pattern detection and correction
- **Exemplary patterns** — 5 verified structural paradigms + 3-layer beginner scaffold

## Version History

| Version | Highlights |
|---|---|
| v2.0 | Adaptive pipeline, review gates, lightweight XML output, family taxonomy, separated knowledge base |
| v2.1 | Output dedup, auto-cleanup of intermediate artifacts |
| v2.2 | Anti-formula knowledge base, intent probes, example-driven family expansion, persona-voice writing |
| v2.3 | Scene-responsive & dialogue-driven families, exemplary patterns knowledge base |
| v2.4 | One-click copy output |
| v2.5 | Architecture slim-down, authority prioritization, narrative perspective KB, QA expanded to 9 dims |
| v2.6 | Model adaptation deepening, anti-formula to 12 types, pattern split, QA to 11 dims, attention optimization |

## Directory Structure

```text
.claude/skills/writing-style-distiller/
├── SKILL.md                    # Entry point: adaptive routing + workflow dispatch
├── output-format.md            # Output format definition + full example
├── quality-checklist.md        # 11-dimension quality checklist
├── error-handling.md           # Error handling & common mistakes
├── verification-notes.md       # Verification notes (dev reference)
├── phases/
│   ├── research.md             # Phase 1: Research & evidence collection
│   ├── diagnosis.md            # Phase 2: Style diagnosis & architecture
│   ├── drafting.md             # Phase 3: Style draft generation
│   └── optimization.md         # Phase 4: Optimization & quality gate
└── knowledge/
    ├── style-families.md       # Style family taxonomy & density table
    ├── label-risk-table.md     # High-risk label behaviorization table
    ├── model-adaptation.md     # Model adaptation rules
    ├── anti-bagu.md            # Anti-formula guide
    ├── exemplary-patterns.md   # Exemplary structure patterns
    └── narrative-perspective.md # Narrative person & POV knowledge base
```

## Installation

### From GitHub Releases

Download from [Releases](https://github.com/qyh9527/writing-style-distiller-skill/releases):

- `writing-style-distiller-agent.zip` — generic package for skill-folder-compatible tools
- `writing-style-distiller-claude-code-project-skill.zip` — Claude Code project-level package

### As a project-level skill

Clone into the project root; confirm `.claude/skills/writing-style-distiller/SKILL.md` exists.

### As a global skill

Copy the skill directory to `~/.claude/skills/writing-style-distiller/` (Windows: `C:\Users\<user>\.claude\skills\writing-style-distiller\`).

## Usage

```text
Use writing-style-distiller to generate a writing style config for Yasunari Kawabata.
Use writing-style-distiller to analyze this text and output <writing_style>.
```

The skill auto-detects input type and selects depth mode. Each phase pauses for confirmation; the final output is a single XML block ready for copy.

## Source

Original content by Yandhi酱 (Discord: `y_a_n_d_h_i`). Used with permission.

## Conditions

| Item | Status |
|---|---|
| Commercial use | Prohibited |
| Community redistribution / modification | Allowed |
| Attribution to original author | Required |

No standard open-source license is attached. Please retain attribution to the original author when redistributing or modifying.
