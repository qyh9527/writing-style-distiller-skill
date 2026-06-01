# Writing Style Distiller Claude Code Skill

[中文说明](README.md)

This repository contains a Claude Code project-level skill that converts an author name, literary text, excerpt samples, or a style description into an executable `<writing_style>` XML writing-style configuration.

## Contents

Main files:

- `.claude/skills/writing-style-distiller/SKILL.md`: main Claude Code skill entry point.
- `.claude/skills/writing-style-distiller/output-schema.md`: canonical `<writing_style>` XML output structure.
- `.claude/skills/writing-style-distiller/quality-checklist.md`: checklist for theoretical accuracy, cultural fit, and executability.
- `.claude/skills/writing-style-distiller/citation-and-examples.md`: rules for original-language examples, citations, and selection rationale.
- `文风蒸馏器.md`: organized source prompt.

## Installation

### Download zip packages from GitHub Releases

The recommended installation path is to download ready-made zip packages from this repository's GitHub Releases:

- `writing-style-distiller-agent.zip`: generic Agent/Skill package for IDEs or agent tools that can import an agent/skill folder.
- `writing-style-distiller-claude-code-project-skill.zip`: Claude Code project-level skill package that can be extracted into a target project root.

The generic package extracts to:

```text
writing-style-distiller/
  SKILL.md
  output-schema.md
  quality-checklist.md
  citation-and-examples.md
  verification-notes.md
```

The Claude Code project-level package extracts to:

```text
.claude/
  skills/
    writing-style-distiller/
      SKILL.md
      output-schema.md
      quality-checklist.md
      citation-and-examples.md
      verification-notes.md
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
Use writing-style-distiller to generate a writing_style XML for Yasunari Kawabata.
```

Or:

```text
Use writing-style-distiller to analyze this text file's writing style and output <writing_style>.
```

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