# Format Validation — 2026-06-19

**Status:** pending
**Issues found:** 380 (121 ERROR, 259 WARNING, 0 INFO)
**Created:** 2026-06-19 23:22:37
**Validator:** format-validator

---

## Executive Summary

| Category | Files | Findings |
|---|---|---|
| Topic files | 109 | All missing YAML frontmatter (systematic — Index Agent format) |
| Tag files | 21 | All have unquoted `parent: [[tag]]` parsed as nested YAML list |
| `wiki/tag/tag.md` | 1 | Missing `parent` + `items_managed_by` fields, missing `## Parent` section |
| Code blocks | 8 files | Missing language tags |
| Broken wikilinks | 60+ files | ~230 forward-references to uncompiled concepts (expected) |
| Field order | 2 files | Mismatch vs spec |

**Files checked:** 540 total (307 concepts + 93 sources + 31 indexes + 109 topics)

---

## ERROR Issues (121)

### Issue 1: Topic files — Missing frontmatter (systematic)

**Affected:** 109 files in `wiki/topic/`
**Severity:** ERROR
**Category:** Frontmatter
**Issue:** All 109 topic files have no YAML frontmatter (`---` delimiters). Files start directly with `# Topic: <name>` heading, followed by `Auto-generated index...` and `Last updated:` in body text.

**Current format:**
```markdown
# Topic: ai-architecture

Auto-generated index of all content with topic `ai-architecture`.

Last updated: 2026-06-19 21:02:46

---

## Concepts (1)
...
```

**Expected (per index-spec.md §5.1 + topic format):**
```yaml
---
type: index
scope: topic
topic: ai-architecture
auto_generated: true
last_updated: 2026-06-19
---
```

**Root cause:** Index Agent generates topic files without frontmatter. This is a systematic format deviation from the spec.

**Suggested fix:** Update Index Agent to write YAML frontmatter on topic files. Then regenerate all 109 topic files.

**Note:** Topic files function correctly in Obsidian (they auto-resolve via filename). The missing frontmatter primarily affects automated validation and cross-linking. This is a **systematic issue** that needs Index Agent update, not individual file fixes.

---

### Issue 2: Code blocks missing language tags (8 files)

**Severity:** ERROR
**Category:** Markdown

| # | File | Issue |
|---|---|---|
| 1 | `wiki/concepts/ai-coach-prompting.md` | Code block missing language tag |
| 2 | `wiki/concepts/content-generation-workflow.md` | Code block missing language tag |
| 3 | `wiki/concepts/dollar-as-rent-payment.md` | Code block missing language tag |
| 4 | `wiki/concepts/existential-vacuum.md` | Code block missing language tag |
| 5 | `wiki/concepts/expert-knowledge-extraction.md` | Code block missing language tag |
| 6 | `wiki/concepts/trading-addiction-cycle.md` | Code block missing language tag |
| 7 | `wiki/concepts/x-search-tool.md` | Code block missing language tag |
| 8 | `wiki/sources/src_petrodollar-system-analysis.md` | Code block missing language tag |

**Expected:** All code blocks must specify language (e.g., `` ```yaml ``, `` ```python ``). Per format-spec.md §4.2.

**Suggested fix:** Add appropriate language tags to unlabeled code blocks in each file.

---

### Issue 3: `wiki/tag/tag.md` — Missing required fields and section

**File:** `wiki/tag/tag.md`
**Severity:** ERROR
**Category:** Frontmatter + Sections

**Current state:**
- `level: 2`, `scope: tags` — level/scope now correct (fixed from previous 06-18 report) ✅
- `auto_generated: false` ✅
- Missing `parent` field ❌
- Missing `items_managed_by` field ❌
- `last_updated: 2026-06-18` ✅

**Expected (index-spec.md §4.2):**
```yaml
type: index
level: 2
scope: tags
parent: "[[wiki]]"
auto_generated: false
items_managed_by: index-agent
last_updated: YYYY-MM-DD
```

**Sections:** Missing `## Parent` section (required per §4.3). Has `## Overview`, `## Stats`, `## Items` — but missing `## Parent` and `## Notes`.

**Suggested fix:**
1. Add `parent: "[[wiki]]"` to frontmatter
2. Add `items_managed_by: index-agent` to frontmatter
3. Add `## Parent` section with `- [[wiki]]`
4. Add `## Notes` section (can be empty)

---

## WARNING Issues (259)

### Issue 4: Tag files — Unquoted `parent` wikilinks (21 files)

**Severity:** WARNING
**Category:** Frontmatter

**Affected:** All 21 `wiki/tag/<tag>.md` files

**Issue:** `parent: [[tag]]` (unquoted) is parsed by YAML as nested list `[['tag']]`, not the string `'[[tag]]'`. Obsidian handles this correctly, but it's ambiguous YAML.

**Expected:** `parent: "[[tag]]"` (quoted, per format-spec.md §9 note)

**Suggested fix:** Quote all `parent` values in tag files. Trivial batch fix.

**Cross-spec conflict:** `index-spec.md` §5.2 shows unquoted `parent: [[tag]]` but `format-spec.md` §9 requires quoted wikilinks in frontmatter. Escalate as `[SPEC CONFLICT]` — index-spec.md should be updated.

---

### Issue 5: Broken wikilinks — Forward-references (~230 instances)

**Severity:** WARNING
**Category:** Markdown

**Affected:** ~60 concepts + ~40 sources

**Issue:** Wikilinks point to concept files that don't exist yet. These are forward-references in a growing KB — concepts link to related concepts that haven't been compiled.

**Examples:**
- `[[economic-inequality]]` — not compiled
- `[[deep-work]]` — not compiled
- `[[game-theory]]` — not compiled
- `[[confirmation-bias]]` — not compiled
- `[[naval-ravikant]]` — not compiled

**Assessment:** Expected behavior for a growing KB. Not a format error. Report as WARNING per spec.

**Note:** 320 broken wikilinks were reported on 06-17. Current count is ~230 — some have been resolved by new compilations. Count will decrease naturally as more concepts are compiled.

---

### Issue 6: Field order mismatches (2 files)

**Severity:** WARNING
**Category:** Frontmatter

| File | Issue |
|---|---|
| `wiki/sources/src_dan-koe-workflow-analysis-markus.md` | Field order: has extra `original_author` field after `author` |
| `wiki/sources/src_map-is-not-territory.md` | `original` wikilink `[[2026-06-03_map-is-not-territory]]` — raw file not found |

---

## [SPEC CONFLICT] — Unquoted wikilinks in index-spec.md

**Issue:** `index-spec.md` §4.2, §5.2 show `parent: [[tag]]` (unquoted), but `format-spec.md` §9 note requires quoted wikilinks in frontmatter (`"[[...]]"`).

**Impact:** 21 tag files + 6 raw sub-indexes use unquoted format. YAML parses these as nested lists. Files work in Obsidian but are ambiguous YAML.

**Recommendation:** Update `index-spec.md` to show quoted format: `parent: "[[tag]]"`. Then Fix Agent can batch-update all affected files.

---

## [SYSTEMATIC VIOLATION] — Topic files without frontmatter

**Pattern:** 109/109 topic files have no YAML frontmatter.

**Likely cause:** Index Agent writes topic files in a format without frontmatter — the `# Topic: <name>` heading + `Last updated:` in body text. This differs from the expected `type: index, scope: topic` frontmatter format described in index-spec.md §5.1.

**Recommendation:** 
1. Update Index Agent skill to include YAML frontmatter in topic file output
2. Regenerate all 109 topic files with proper frontmatter
3. Or: update index-spec.md §5.1 to explicitly document the current format as intentional

**Severity:** These files function correctly in Obsidian (no broken behavior). The issue is purely a format compliance gap between the spec and the generator.

---

## Files with No Issues

All 307 concepts, 93 sources, 31 indexes, and 109 topics were scanned. Beyond the issues listed above:

- **Concepts:** All have correct `type: concept`, valid `main_tag`, `sub_tags` within TAGS.md, required sections present, valid `last_updated` dates. No concepts are missing sections or have invalid tags.
- **Sources:** All have correct `type: source`, valid `main_tag`, valid naming (`src_` prefix). One has a broken `original` link.
- **Indexes:** All level 1/2/3 indexes have correct fields for their level. `wiki/tag/tag.md` is the only index with issues (now down from 5 errors on 06-18 to 4 — `level` and `scope` are now correct).
- **Topics:** All function correctly in Obsidian — the missing frontmatter is a spec compliance issue, not a functional bug.

---

## Comparison with Previous Runs

| Metric | 06-17 | 06-18 | 06-19 | Trend |
|---|---|---|---|---|
| Files checked | 418 | 530 | 540 | ↗ |
| ERRORs | 16 | 11 | 121 | ↗ (109 topic frontmatter) |
| WARNINGs | 349 | 6 | 259 | ↗ (230 broken wikilinks) |
| Broken wikilinks | 320 | N/A | ~230 | ↘ |
| Code blocks no lang | 11 | resolved | 8 | ↘ |
| tag.md issues | 2 | 5 | 4 | ↘ (level/scope fixed) |
| Unquoted parent | 20+ | 6 raw indexes | 21 tags | Same pattern |

**Key improvements since 06-18:**
- `wiki/tag/tag.md` level and scope now correct (level=2, scope=tags)
- `crypto` as sub_tag issue appears resolved (was 4 files on 06-18)
- `infrastructure-capex-cycle.md` missing sections appears resolved

**New finding (06-19):**
- 109 topic files missing frontmatter — previously hidden by dispatch fix. Before 06-18, topic files were incorrectly validated as indexes (100+ false ERRORs for missing `level`). After the dispatch fix, we now see they lack frontmatter entirely.

---

**End of report.**
