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

## GREEN: Skill Coverage Check

- Trigger-only description: covered in `SKILL.md` frontmatter; it lists use conditions and search keywords without summarizing the workflow.
- Operational workflow: covered by phases 1-4 in `SKILL.md`.
- Input routing: covers author, representative work, local file, excerpts, and style description.
- Terminal-compatible output: final XML is emitted directly; artifacts are not required.
- Honest length validation: token count is marked as estimate unless a tool is run.
- Citation discipline: covered in `citation-and-examples.md`.
- Final quality gate: covered in `quality-checklist.md`.

## REFACTOR Notes

The skill uses four operating files to keep maintenance simple: workflow, schema, quality, and citation rules. `verification-notes.md` remains as the TDD record. No additional scripts are needed for the first version.

Additional refactor adjustments made after GREEN review:

- Added Chinese trigger keywords to improve discovery for `文风蒸馏`, `文风配置`, and `写作风格分析` requests.
- Added an output-language rule so explanations follow the user's language while examples stay in the author's original language.
- Added a search instruction to repeat key searches in the author's writing language when relevant.
