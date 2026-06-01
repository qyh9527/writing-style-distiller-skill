# Public Release Compliance Documentation Design

Date: 2026-06-01

## Goal

Prepare `qyh9527/writing-style-distiller-skill` for public visibility by adding clear Chinese and English documentation that credits the original author and states the known usage restrictions.

## Source Attribution

The repository must state that the work is based on content by:

- Original author: Yandhi酱
- Discord ID: `y_a_n_d_h_i`
- Original post: `https://discord.com/channels/1291925535324110879/1423575785360326716`
- Original timestamp: `2025/11/20 22:40`

## Permission Statement

Because the original license is unknown and the user reports that commercial use is prohibited, the repository must not present itself as MIT, Apache, GPL, or another standard open-source licensed project.

The documentation should state:

- The original author stated that direct use is allowed when needed and that users do not need to privately request authorization.
- Non-commercial use only unless the original author grants additional permission.
- Community redistribution is allowed.
- Community modification is allowed.
- Management/group backup is allowed.
- Attribution to the original author is required.
- If the original author publishes updated terms, those terms take precedence.

## Files to Update

- `README.md` — Chinese public-facing documentation.
- `README_EN.md` — English public-facing documentation.
- `文风蒸馏器.md` — source prompt attribution notice near the top.
- `.claude/skills/writing-style-distiller/SKILL.md` — attribution and usage restrictions in the skill package itself.

## Public Visibility Procedure

1. Add and commit documentation updates.
2. Push `master` to GitHub.
3. Change repository visibility from private to public.
4. Verify GitHub reports `isPrivate: false`.

## Non-goals

- Do not add a standard `LICENSE` file that could imply broader rights.
- Do not claim legal certainty about the original license.
- Do not remove attribution or source links from derivative skill files.