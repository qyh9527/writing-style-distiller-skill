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
