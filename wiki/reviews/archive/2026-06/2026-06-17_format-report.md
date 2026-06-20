# Format Validation — 2026-06-17

**Status:** approved
**Approved by:** Julius
**Issues found:** 365 (16 ERROR, 349 WARNING, 0 INFO)
**Files checked:** 418 (296 concepts + 91 sources + 21 tag indexes + 10 root/raw indexes)
**Broken wikilinks:** 320 (forward-references and non-existent targets)
**Created:** 2026-06-17 23:19:46
**Validator:** format-validator

---

## Summary

| Category | ERROR | WARNING | INFO | Total |
|---|---|---|---|---|
| Frontmatter | 2 | 26 | 0 | 28 |
| Sections | 3 | 0 | 0 | 3 |
| Naming | 0 | 0 | 0 | 0 |
| Markdown | 11 | 3 | 0 | 14 |
| **Total (excl. wikilinks)** | **16** | **29** | **0** | **45** |

---

## Top Issues (up to 20, excluding broken wikilinks)

### Issue 1: Markdown — ERROR

**File:** wiki/concepts/ai-coach-prompting.md
**Severity:** ERROR
**Category:** Markdown
**Issue:** Code block missing language tag
**Suggested fix:** Add language e.g. ```python

### Issue 2: Markdown — ERROR

**File:** wiki/concepts/ai-coach-prompting.md
**Severity:** ERROR
**Category:** Markdown
**Issue:** Code block missing language tag
**Suggested fix:** Add language e.g. ```python

### Issue 3: Markdown — ERROR

**File:** wiki/concepts/content-generation-workflow.md
**Severity:** ERROR
**Category:** Markdown
**Issue:** Code block missing language tag
**Suggested fix:** Add language e.g. ```python

### Issue 4: Markdown — ERROR

**File:** wiki/concepts/content-generation-workflow.md
**Severity:** ERROR
**Category:** Markdown
**Issue:** Code block missing language tag
**Suggested fix:** Add language e.g. ```python

### Issue 5: Markdown — ERROR

**File:** wiki/concepts/dollar-as-rent-payment.md
**Severity:** ERROR
**Category:** Markdown
**Issue:** Code block missing language tag
**Suggested fix:** Add language e.g. ```python

### Issue 6: Markdown — ERROR

**File:** wiki/concepts/existential-vacuum.md
**Severity:** ERROR
**Category:** Markdown
**Issue:** Code block missing language tag
**Suggested fix:** Add language e.g. ```python

### Issue 7: Markdown — ERROR

**File:** wiki/concepts/expert-knowledge-extraction.md
**Severity:** ERROR
**Category:** Markdown
**Issue:** Code block missing language tag
**Suggested fix:** Add language e.g. ```python

### Issue 8: Markdown — ERROR

**File:** wiki/concepts/expert-knowledge-extraction.md
**Severity:** ERROR
**Category:** Markdown
**Issue:** Code block missing language tag
**Suggested fix:** Add language e.g. ```python

### Issue 9: Markdown — ERROR

**File:** wiki/concepts/trading-addiction-cycle.md
**Severity:** ERROR
**Category:** Markdown
**Issue:** Code block missing language tag
**Suggested fix:** Add language e.g. ```python

### Issue 10: Markdown — ERROR

**File:** wiki/concepts/x-search-tool.md
**Severity:** ERROR
**Category:** Markdown
**Issue:** Code block missing language tag
**Suggested fix:** Add language e.g. ```python

### Issue 11: Markdown — ERROR

**File:** wiki/sources/src_petrodollar-system-analysis.md
**Severity:** ERROR
**Category:** Markdown
**Issue:** Code block missing language tag
**Suggested fix:** Add language

### Issue 12: Frontmatter — ERROR

**File:** wiki/tag/tag.md
**Severity:** ERROR
**Category:** Frontmatter
**Issue:** level=1 but scope="tag" (expected raw/wiki/context)
**Suggested fix:** Fix scope or level

### Issue 13: Frontmatter — ERROR

**File:** wiki/tag/tag.md
**Severity:** ERROR
**Category:** Frontmatter
**Issue:** level=1 requires auto_generated: false
**Suggested fix:** Set auto_generated: false

### Issue 14: Sections — ERROR

**File:** wiki/tag/tag.md
**Severity:** ERROR
**Category:** Sections
**Issue:** Missing ## Overview
**Suggested fix:** Add ## Overview section

### Issue 15: Sections — ERROR

**File:** wiki/tag/tag.md
**Severity:** ERROR
**Category:** Sections
**Issue:** Missing ## Sub-indexes
**Suggested fix:** Add ## Sub-indexes section

### Issue 16: Sections — ERROR

**File:** wiki/tag/tag.md
**Severity:** ERROR
**Category:** Sections
**Issue:** Missing ## Notes
**Suggested fix:** Add ## Notes section

### Issue 17: Markdown — WARNING

**File:** wiki/concepts/incentives-mental-model.md
**Severity:** WARNING
**Category:** Markdown
**Issue:** sources item: broken wikilink [[src_the-power-of-incentives-hidden-forces-shape-behavior]]
**Suggested fix:** Target not found

### Issue 18: Markdown — WARNING

**File:** wiki/concepts/operant-conditioning.md
**Severity:** WARNING
**Category:** Markdown
**Issue:** sources item: broken wikilink [[src_the-power-of-incentives-hidden-forces-shape-behavior]]
**Suggested fix:** Target not found

### Issue 19: Markdown — WARNING

**File:** wiki/sources/src_map-is-not-territory.md
**Severity:** WARNING
**Category:** Markdown
**Issue:** original: broken wikilink [[2026-06-03_map-is-not-territory]]
**Suggested fix:** Target not found

### Issue 20: Frontmatter — WARNING

**File:** wiki/tag/ai.md
**Severity:** WARNING
**Category:** Frontmatter
**Issue:** parent: unquoted [[tag]] parsed as YAML list — use "[[tag]]"
**Suggested fix:** Quote: parent: "[[tag]]"

---

## Broken Wikilinks (320 total)

**Severity:** WARNING
**Note:** Broken wikilinks in a growing KB are expected forward-references. Reported as WARNING per format-spec.md §6.2.

**Sample (5 of 320):**

- **wiki/concepts/activation-energy.md** — Broken wikilink: [[momentum]]

- **wiki/concepts/activation-energy.md** — Broken wikilink: [[inertia]]

- **wiki/concepts/activation-energy.md** — Broken wikilink: [[breaking-point]]

- **wiki/concepts/agent-harness.md** — Broken wikilink: [[agent-initiated-code-artifacts]]

- **wiki/concepts/agent-harness.md** — Broken wikilink: [[multi-agent-systems]]


---

## Files with Most Issues (top 10)

- **wiki/sources/src_mental-models-of-art.md** — 9 issues
- **wiki/sources/src_mental-models-of-economics.md** — 9 issues
- **wiki/sources/src_thought-experiment.md** — 9 issues
- **wiki/sources/src_fs-blog-mental-models.md** — 7 issues
- **wiki/concepts/third-order-thinking.md** — 6 issues
- **wiki/concepts/thought-experiment.md** — 6 issues
- **wiki/sources/src_code-as-agent-harness-arxiv-2605-18747.md** — 6 issues
- **wiki/sources/src_farnam-street-mental-models-biology-series.md** — 6 issues
- **wiki/sources/src_farnam-street-mental-models-systems-thinking.md** — 6 issues
- **wiki/sources/src_incentives-hidden-forces.md** — 6 issues


---

## Notes

- **Topic files** (`wiki/topic/*.md`, 105 files): Auto-generated by Index Agent, not validated (per index-spec.md §5.1).
- **Draft files** (`wiki/drafts/`): Skipped (4 files).
- **Broken wikilinks**: 320 instances — forward-references to concepts not yet compiled.
- **Format ground truth**: `wiki/meta/format-spec.md` v2.0 + `wiki/meta/index-spec.md` v1.0.

---

## Escalations

### [SPEC CONFLICT] Unquoted wikilinks in index frontmatter vs format-spec.md

**Issue:** `index-spec.md` §4.2 and §5.2 show `parent: [[tag]]` (unquoted), but `format-spec.md` §9 note states: "Wikilinks in frontmatter fields use quoted format `"...[[...]]..."` for Obsidian compatibility."

**Impact:** 20 `wiki/tag/*.md` files use unquoted `parent: [[tag]]`. YAML parses this as a nested list `[['tag']]` instead of the string `'[[tag]]'`. While Obsidian handles it correctly, the YAML is ambiguous.

**Recommendation:** 
1. Update `index-spec.md` to show quoted format: `parent: "[[tag]]"`
2. Update Index Agent to write quoted format
3. Fix Agent can apply `parent: "[[tag]]"` to all 20 tag files

### [FORMAT UNCERTAINTY] wiki/tag/tag.md — level mismatch

**Issue:** `wiki/tag/tag.md` has `level: 1` but `index-spec.md` §4.1 lists it as Tầng 2 (level 2) with scope `tags` and parent `[[wiki]]`.

**Question:** Should `tag.md` be level 1 (root of tag subsystem) or level 2 (sub-index of wiki.md)? The spec seems to have it as level 2.

**Recommendation:** Set `level: 2`, `scope: tags`, `parent: "[[wiki]]"`, `items_managed_by: index-agent`.
