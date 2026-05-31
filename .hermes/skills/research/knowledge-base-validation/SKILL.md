---
name: knowledge-base-validation
description: Review wiki concept files and write review results to wiki/reviews/. Updates _pending.md and reviews_index.md.
tools:
  - read_file
---
name: knowledge-base-validation
description: Review wiki concept files and write review results to wiki/reviews/. Updates _action-required.md and writes full validator reports.
tags: [hermes, kb, validation]
---

# Knowledge Base Validation

Connor (Hermes-RK800) validates wiki files against format-spec.md v2.2. Read-only — only writes to wiki/reviews/.

## Pipeline Context

| Stage | Owner | Skill | Output |
|---|---|---|---|
| Compile | Kara (Compile Agent) | compile-agent/SKILL.md | wiki/sources/ + wiki/concepts/ |
| Validation | Connor (Hermes-VPS) | format-validator, output-validator, hygiene-inspector | wiki/reviews/*-report-YYYY-MM-DD.md |
| Fix (post-approval) | Kara (Fix Agent) | fix-agent/SKILL.md | Updates files listed in approved reports |

## Core Rule — READ ONLY

**Connor KHÔNG tự sửa file trong wiki/concepts/ hoặc wiki/sources/. Chỉ validate + report.** Kara fix sau khi Julius approve.

## Validation Types

### 1. Format Validator
Checks: frontmatter fields, field order, sub_tags count (1-3 required), wikilink format ("[[...]]" in frontmatter, bare elsewhere), naming conventions.

Known valid sub_tags (Pool B): research, opinion, tools, security, economics, politics, biology, psychology, philosophy, finance, strategy, systems, memory, agents, reasoning, planning, creativity, communication, collaboration, learning, adaptation, alignment, inference, architecture, training, evaluation

Known INVALID sub_tags ( recurring issues — do NOT flag as valid):
- `tech` → use `tools`
- `observation` → not in Pool B
- Any tag not in TAGS.md Pool B

### 2. Output Validator
Checks: summary sentences (3+), section content depth, sources section populated, status value valid.

Valid status values: `draft` | `reviewed` | `needs-revision`
**INVALID: `stub`** — 17+ files kept using `stub` after being flagged

### 3. Hygiene Inspector
Checks: folder structure, no orphan files, no .bak/.tmp files.

**Root-level items (memory/, search/, RAW_BACKLOG.md, venv/) = OUTSIDE Kara scope — belong to Julius. DO NOT flag these as hygiene issues.** Kara only cleans wiki/, sources/, concepts/.

## Output Files

After each validation run:
1. Write individual report: `wiki/reviews/{format,output,hygiene}-report-YYYY-MM-DD.md`
2. Update `wiki/reviews/_action-required.md` with pending issues and mark as ⏳ PENDING APPROVAL

## _action-required.md Update Pattern

When marking pending:
```
**Pending reports:** N

**Status:**
- ⏳ [Validator] — YYYY-MM-DD: **PENDING APPROVAL** (X issues: [brief summary])

## Critical Issues (Fix Immediately)

### ⏳ [Validator] — YYYY-MM-DD (N issues)

[Issue list grouped by type]
```

When Julius approves, mark:
```
- ✅ [Validator] — YYYY-MM-DD: **APPLIED** (N files fixed)
```

## Process

1. Run all 3 validators in parallel via delegate_task (each with `terminal` + `file` toolsets)
2. Collect findings, deduplicate, verify against spec
3. Write individual report files to wiki/reviews/
4. Update _action-required.md with all pending issues
5. Report to Julius via Telegram

### Validation Output Template

```markdown
# [Type] Validator Report — YYYY-MM-DD

**Validator:** Connor (Hermes-RK800)
**Scope:** [what was checked]
**Total files reviewed:** ~N

## Issues Found: N

### CRITICAL — [Category]

**N files affected**:
- file1.md
- file2.md

### WARNING — [Category]

**N files**:
- file3.md

### ✅ Passing

- [what passed]

---

## Verdict

**REVISE** — N issues across [categories].

Fix list ready for Kara. Approved by Julius (via _action-required.md).
```

## Criteria Quick Reference

| Check | Spec Rule |
|-------|-----------|
| sub_tags count | 1-3 per file (Pool B tags only) |
| Valid Pool B tags | research, opinion, tools, security, economics, politics, biology, psychology, philosophy, finance, strategy, systems, memory, agents, reasoning, planning, creativity, communication, collaboration, learning, adaptation, alignment, inference, architecture, training, evaluation |
| Invalid tags (recurring) | `tech` → `tools`; `observation` → not valid |
| Status valid values | `draft` \| `reviewed` \| `needs-revision` (NOT `stub`) |
| Field order (sources) | type, original, main_tag, sub_tags, topic, date_compiled, url, author |
| Wikilinks frontmatter | `"[[slug]]"` (quoted for Obsidian) |
| Wikilinks body | `[[slug]]` (bare) |
| Hygiene scope | wiki/, sources/, concepts/ only — NOT root-level folders |