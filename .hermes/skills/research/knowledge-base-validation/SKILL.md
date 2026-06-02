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

**Pool B tags are defined in TAGS.md — ALWAYS read TAGS.md as ground truth, do NOT hardcode.**  
Current Pool B (16 tags as of 2026-06-01): hack, tools, automation, vibecode, research, tutorial, opinion, news, defi, perpdex, layer1, layer2, law, coding, psychology, health.

**RECURRING SYSTEMIC ISSUE — Main-tags used as sub_tags:**  
Compile Agent frequently puts main_tags (economic, productivity, systems, ai, politic, tech, crypto) into sub_tags. These are Pool A tags, NOT Pool B. Pattern: `sub_tags: [opinion, productivity, systems]` — `productivity` and `systems` are main_tags masquerading as sub_tags. Fix: strip main-tag duplicates, keep only valid Pool B tags.

Known INVALID sub_tags (recurring — do NOT flag as valid):
- `economic` → already main_tag (Pool A), remove from sub_tags
- `productivity` → already main_tag, remove from sub_tags  
- `systems` → already main_tag, remove from sub_tags
- `ai` → already main_tag, remove from sub_tags
- `politic` → already main_tag, remove from sub_tags
- `tech` → already main_tag, remove from sub_tags
- `crypto` → already main_tag, remove from sub_tags
- `economics` → typo, use `economic` as main_tag only
- `psychology`, `health`, `behavior`, `blindspots`, `frontend`, `analysis` → not in Pool B, need Julius approval to add
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

1. **Verify working directory**: `cd ~/knowledge-base` — NOT the hermes-agent repo. Check `ls wiki/concepts/ | head -3` to confirm.
2. **Read TAGS.md** to get current Pool B (not hardcoded from skill memory).
3. **Run all 3 validators using `execute_code` with shell scripts** — do NOT use `delegate_task` for validation runs. Subagent overhead is too high (684s for partial run vs 15s direct). Each validator runs as a shell pipeline via `terminal()` inside `execute_code`.
4. Collect findings, deduplicate, verify against TAGS.md
5. Write individual report files to `wiki/reviews/`
6. Update `_action-required.md` with all pending issues, prepending new entries above old ones
7. Report summary to Julius via Telegram

### Re-validation Cycle (Post-Fix)

After Julius approves reports and Fix Agent applies fixes, re-run all 3 validators to verify what was actually fixed:

1. **Append `-v2`** to report filenames: `wiki/reviews/2026-06-01_format-report-v2.md`
2. **Compare before/after** counts — show improvement explicitly (e.g., "86→57, 36% fixed")
3. **Categorize remaining issues**:
   - **Fixable by Fix Agent** — individual file errors (invalid sub_tags, empty sub_tags, wrong status)
   - **Systemic — needs re-compile** — content quality issues (Summary 1-dòng, Key Points <3, Definition too short). Fix Agent cannot expand content.
4. **Update `_action-required.md`** with v2 reports, prepending above v1 entries

### Compile Agent Patching Pattern

When systemic issues trace to Compile Agent config, patch these files (NOT individual wiki files):

| File | What to patch |
|---|---|
| `SKILL.md` | Language policy, section specs (Summary 3-5 câu, Key ideas ≥3, Sources not empty), Status lifecycle |
| `workflow.md` | Prompt templates — add hard constraints, switch to Vietnamese, add ⚠️ warnings for recurring mistakes |
| `TAGS.md` | Only Julius can modify — propose new tags, don't auto-add |

**Proven patches (2026-06-01):**
- Language: "keep original" → "compile bằng tiếng Việt" + "KHÔNG dịch technical terms"
- Summary: "3-5 câu tiếng Việt (KHÔNG ĐƯỢC viết 1 câu)" — both in SKILL.md spec AND workflow.md prompt template
- Sub-tags: Add ⚠️ block: "KHÔNG dùng main_tags (ai, crypto, tech, productivity, system, economic, politic) làm sub_tags" — must appear in BOTH the decision logic section AND the prompt template
- Constraints must appear in prompt templates, not just in spec docs. LLM agents skip spec docs but follow prompt templates.

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

## Root Cause Tracing — Compile Agent Config

When systemic issues are found across many files, the root cause is almost always in Compile Agent's config. Config files live at:

```
.openclaw/skills/compile-agent/
├── SKILL.md          — Main agent instructions, language policy, section specs
├── workflow.md       — Step-by-step compile workflow with prompt templates
├── tagging_rules.md  — Tag selection decision trees
└── examples.md       — Input→output transformation examples
```

**Pattern:** Validation finds systemic errors → trace to which compile-agent file/prompt caused it → patch that file. Do NOT fix individual wiki files — fix the agent config, then re-compile.

Recent fixes applied (2026-06-01):
- Language policy: "keep original" → "compile bằng tiếng Việt" (SKILL.md L45-49)
- Summary: added constraint "KHÔNG ĐƯỢC viết 1 câu" (SKILL.md, workflow.md)
- Sub-tags: added ⚠️ warning block against main_tags leaking into sub_tags (workflow.md Step 5.3)

## Criteria Quick Reference

| Check | Spec Rule |
|-------|-----------|
| sub_tags count | 1-3 per file (Pool B tags only) |
| Valid Pool B tags | **ALWAYS read TAGS.md.** Current (2026-06-01): hack, tools, automation, vibecode, research, tutorial, opinion, news, defi, perpdex, layer1, layer2, law, coding, psychology, health |
| Invalid tags (recurring) | main_tags used as sub_tags: `economic`, `productivity`, `systems`, `ai`, `politic`, `tech`, `crypto` → remove, these are Pool A only |
| Status valid values | `draft` \| `reviewed` \| `needs-revision` (NOT `stub`) |
| Summary min length | 3-5 sentences required. 1-sentence summary = systemic compile-agent prompt failure |
| Field order (sources) | type, original, main_tag, sub_tags, topic, date_compiled, url, author |
| Wikilinks frontmatter | `"[[slug]]"` (quoted for Obsidian) |
| Wikilinks body | `[[slug]]` (bare) |
| Hygiene scope | wiki/, sources/, concepts/ only — NOT root-level folders |