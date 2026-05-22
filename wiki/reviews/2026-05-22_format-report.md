# Format Validation — 2026-05-22

**Status:** pending
**Issues found:** 11 (0 ERROR, 11 WARNING, 0 INFO)
**Files checked:** 67 (50 concepts + 17 sources)
**Created:** 2026-05-22 23:15:00
**Validator:** format-validator (Hermes)

---

## Summary

All 67 wiki content files pass ERROR-level format validation. 11 WARNING-level issues found across 6 files — all are convention violations (section order, legacy fields, YAML syntax preference). No ERRORs requiring immediate fix.

**Top violation patterns:**
- Extra sections between required sections (3 files): `## Setup`, `## Cost Comparison`, `## Comparison với x_search`
- YAML list syntax for sub_tags (3 files): prefer `[tag1, tag2]` over `\n  - tag1\n  - tag2`
- Legacy fields `date_ingested` and `scope` (2 files): removed in format-spec v2.0
- Field order mismatch (2 files): `date_compiled` placed after `url`/`author`

---

## Issue 1: Extra section breaks required section order

**File:** wiki/concepts/cookie-fun-mcp.md
**Severity:** WARNING
**Category:** Sections
**Issue:** Extra section `## Comparison với x_search` inserted between `## Key ideas` and `## Related concepts`, breaking the required section order
**Current:** `## Comparison với x_search` between Key ideas and Related concepts
**Expected:** Move extra sections after `## Sources` (format-spec.md §2.3 allows optional `## Notes` after Sources)
**Suggested fix:** Move `## Comparison với x_search` to after `## Sources`

---

## Issue 2: Extra section breaks required section order

**File:** wiki/concepts/grok-hermes-integration.md
**Severity:** WARNING
**Category:** Sections
**Issue:** Extra section `## Cost Comparison` inserted between `## Key ideas` and `## Related concepts`
**Current:** `## Cost Comparison` between Key ideas and Related concepts
**Expected:** Move after required sections (`## Sources` or as subsection)
**Suggested fix:** Move `## Cost Comparison` to after `## Sources` or make it a subsection under `## Key ideas`

---

## Issue 3: Extra section breaks required section order

**File:** wiki/concepts/x-search-tool.md
**Severity:** WARNING
**Category:** Sections
**Issue:** Extra section `## Setup` inserted between `## Key ideas` and `## Related concepts`
**Current:** `## Setup` between Key ideas and Related concepts
**Expected:** Move after required sections
**Suggested fix:** Move `## Setup` to after `## Sources`

---

## Issue 4: YAML list syntax for sub_tags

**File:** wiki/sources/src_1-month-with-hermes-ive-been-using-wrong.md
**Severity:** WARNING
**Category:** Frontmatter
**Issue:** `sub_tags` uses YAML list syntax (`\n  - tag1\n  - tag2`) instead of bracket syntax (`[tag1, tag2]`)
**Current:** YAML list-style sub_tags
**Expected:** `sub_tags: [tag1, tag2]` (format-spec.md §5.1: "Arrays use bracket syntax: [item1, item2] not YAML list syntax")
**Suggested fix:** Convert to bracket syntax: `sub_tags: [automation, tools, opinion]`

---

## Issue 5: YAML list syntax for sub_tags

**File:** wiki/sources/src_how-ai-productivity-fails.md
**Severity:** WARNING
**Category:** Frontmatter
**Issue:** `sub_tags` uses YAML list syntax instead of bracket syntax
**Current:** YAML list-style sub_tags
**Expected:** `sub_tags: [tools, automation, opinion]`

---

## Issue 6: Legacy field — date_ingested

**File:** wiki/sources/src_how-ai-productivity-fails.md
**Severity:** WARNING
**Category:** Frontmatter
**Issue:** Legacy field `date_ingested` present — replaced by `date_compiled` in format-spec v2.0 (May 2025)
**Current:** `date_ingested: 2026-05-14`
**Expected:** Remove `date_ingested` (keep only `date_compiled`)
**Suggested fix:** Delete the `date_ingested` line from frontmatter

---

## Issue 7: Legacy field — scope

**File:** wiki/sources/src_how-ai-productivity-fails.md
**Severity:** WARNING
**Category:** Frontmatter
**Issue:** Legacy field `scope` present with no value — not in source file frontmatter schema (format-spec.md §3.2)
**Current:** `scope:` (empty)
**Expected:** Remove `scope` field entirely
**Suggested fix:** Delete the `scope:` line from frontmatter

---

## Issue 8: Field order mismatch

**File:** wiki/sources/src_how-ai-productivity-fails.md
**Severity:** WARNING
**Category:** Frontmatter
**Issue:** Frontmatter fields in wrong order — `date_compiled` comes after `url` instead of before per format-spec.md §3.2
**Current:** `type, original, main_tag, sub_tags, topic, author, url, date_compiled`
**Expected:** `type, original, main_tag, sub_tags, topic, date_compiled, url, author`
**Suggested fix:** Reorder: move `date_compiled` before `url`, then place `url` before `author`

---

## Issue 9: YAML list syntax for sub_tags

**File:** wiki/sources/src_how-some-people-become-unrecognizable.md
**Severity:** WARNING
**Category:** Frontmatter
**Issue:** `sub_tags` uses YAML list syntax instead of bracket syntax
**Current:** YAML list-style sub_tags
**Expected:** `sub_tags: [opinion, tools]`

---

## Issue 10: Legacy field — date_ingested

**File:** wiki/sources/src_how-some-people-become-unrecognizable.md
**Severity:** WARNING
**Category:** Frontmatter
**Issue:** Legacy field `date_ingested` present — replaced by `date_compiled` in format-spec v2.0
**Current:** `date_ingested: 2026-05-14`
**Expected:** Remove `date_ingested`
**Suggested fix:** Delete the `date_ingested` line from frontmatter

---

## Issue 11: Field order mismatch

**File:** wiki/sources/src_how-some-people-become-unrecognizable.md
**Severity:** WARNING
**Category:** Frontmatter
**Issue:** Frontmatter field order mismatch — `date_compiled` should precede `url`
**Current:** `type, original, main_tag, sub_tags, topic, author, url, date_compiled`
**Expected:** `type, original, main_tag, sub_tags, topic, date_compiled, url, author`
**Suggested fix:** Reorder: `date_compiled` before `url`, `url` before `author`

---

## Statistics

| Metric | Count |
|---|---|
| Concept files checked | 50 |
| Source files checked | 17 |
| Total files | 67 |
| ERROR issues | 0 |
| WARNING issues | 11 |
| INFO issues | 0 |
| Files with issues | 6 (9.0%) |
| Clean files | 61 (91.0%) |

## Top violation categories

| Category | Count |
|---|---|
| Frontmatter — Field order | 2 |
| Frontmatter — Legacy fields | 2 |
| Frontmatter — YAML syntax | 3 |
| Sections — Extra section order | 3 |
| Sections — Other | 0 |

This is a very clean run — no ERRORs, all issues are WARNING-level convention violations.
