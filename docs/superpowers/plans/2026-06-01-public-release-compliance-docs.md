# Public Release Compliance Docs Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add bilingual compliance documentation and make the GitHub repository public only after attribution and non-commercial restrictions are documented.

**Architecture:** Use root-level `README.md` and `README_EN.md` for public-facing Chinese and English explanations. Add compact attribution notices to the original prompt and packaged skill so source and restrictions remain visible even when files are copied independently.

**Tech Stack:** Markdown, git, GitHub CLI.

---

## File Structure

- Create: `README.md` — Chinese overview, usage, attribution, and restrictions.
- Create: `README_EN.md` — English overview, usage, attribution, and restrictions.
- Modify: `文风蒸馏器.md` — add source attribution notice near the top.
- Modify: `.claude/skills/writing-style-distiller/SKILL.md` — add attribution and usage restriction section.

### Task 1: Add Bilingual README Files

**Files:**
- Create: `README.md`
- Create: `README_EN.md`

- [ ] **Step 1: Create Chinese README**

Write `README.md` with project purpose, skill location, attribution, direct-use permission note, known permissions, restrictions, and disclaimer that this is not a standard open-source license.

- [ ] **Step 2: Create English README**

Write `README_EN.md` with equivalent English content, including the direct-use permission note.

- [ ] **Step 3: Verify required attribution terms appear**

Run:

```powershell
Select-String -Path "README.md","README_EN.md" -Pattern "Yandhi酱|y_a_n_d_h_i|discord.com/channels/1291925535324110879/1423575785360326716|non-commercial|非商业|直接使用|without privately requesting authorization|2025/11/20 22:40"
```

Expected: matches appear in both README files.

### Task 2: Add Embedded Attribution Notices

**Files:**
- Modify: `文风蒸馏器.md`
- Modify: `.claude/skills/writing-style-distiller/SKILL.md`

- [ ] **Step 1: Add source notice to original prompt**

Insert a short attribution block at the top of `文风蒸馏器.md`, before the existing XML-like prompt.

- [ ] **Step 2: Add source notice to skill package**

Append an `Attribution and Use Restrictions` section to `.claude/skills/writing-style-distiller/SKILL.md`.

- [ ] **Step 3: Verify embedded notices**

Run:

```powershell
Select-String -Path "文风蒸馏器.md",".claude/skills/writing-style-distiller/SKILL.md" -Pattern "Yandhi酱|y_a_n_d_h_i|禁止商业|non-commercial|discord.com/channels/1291925535324110879/1423575785360326716"
```

Expected: matches appear in both files.

### Task 3: Commit and Push Documentation

**Files:**
- All modified documentation files.

- [ ] **Step 1: Check status**

Run:

```powershell
git status --short
```

Expected: README files and two attribution edits are visible.

- [ ] **Step 2: Commit docs**

Run:

```powershell
git add README.md README_EN.md "文风蒸馏器.md" ".claude/skills/writing-style-distiller/SKILL.md" docs/superpowers/plans/2026-06-01-public-release-compliance-docs.md
git commit -m "docs: add public release attribution and restrictions"
```

Expected: commit succeeds.

- [ ] **Step 3: Push docs**

Run:

```powershell
git push
```

Expected: push succeeds to `origin/master`.

### Task 4: Make GitHub Repository Public

**Files:**
- Remote repository setting only.

- [ ] **Step 1: Make repository public**

Run:

```powershell
gh repo edit qyh9527/writing-style-distiller-skill --visibility public --accept-visibility-change-consequences
```

Expected: command exits successfully.

- [ ] **Step 2: Verify visibility**

Run:

```powershell
gh repo view qyh9527/writing-style-distiller-skill --json nameWithOwner,isPrivate,url
```

Expected: `isPrivate` is `false`.

## Self-Review

- Spec coverage: plan covers bilingual README files, embedded notices, push, and public visibility change.
- Placeholder scan: no TBD/TODO placeholders remain.
- Scope check: no standard `LICENSE` file is added, matching the unknown-license/non-commercial requirement.