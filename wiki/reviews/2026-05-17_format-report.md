---
type: validation-report
validator: format-validator
date: 2026-05-17
status: pending
---

# Format Validation Report — 2026-05-17

## Summary

- **Files scanned:** 38
- **Issues found:** 5 (0 ERROR, 5 WARNING, 0 INFO)
- **Files with issues:** 2
- **Validation time:** 2026-05-17 23:15

---

## Issues by Severity

### ⚠️ WARNINGs (5)

---

#### Issue 1: Extra frontmatter fields + incorrect field order

**File:** `wiki/sources/src_how-ai-productivity-fails.md`
**Severity:** WARNING
**Category:** Frontmatter
**Issue:** Extra fields not in spec (`date_ingested`, `scope`), and field order has `author` before `url`
**Current:** `type, original, main_tag, sub_tags, topic, author, url, date_ingested, date_compiled, scope`
**Expected:** `type, original, main_tag, sub_tags, topic, date_compiled, url, author`
**Suggested fix:** Remove `date_ingested` and `scope`; move `url` before `author`

---

#### Issue 2: Extra frontmatter fields + incorrect field order

**File:** `wiki/sources/src_how-some-people-become-unrecognizable.md`
**Severity:** WARNING
**Category:** Frontmatter
**Issue:** Extra field not in spec (`date_ingested`), and field order has `author` before `url`
**Current:** `type, original, main_tag, sub_tags, topic, author, url, date_ingested, date_compiled`
**Expected:** `type, original, main_tag, sub_tags, topic, date_compiled, url, author`
**Suggested fix:** Remove `date_ingested`; move `url` before `author`

---

#### Issue 3: sub_tags uses YAML list syntax instead of brackets

**File:** `wiki/sources/src_how-ai-productivity-fails.md`
**Severity:** WARNING
**Category:** Frontmatter
**Issue:** `sub_tags` field uses YAML dash-list syntax instead of inline bracket syntax per format-spec §5.1
**Current:**
```yaml
sub_tags:
  - tools
  - automation
  - opinion
```
**Expected:**
```yaml
sub_tags: [tools, automation, opinion]
```
**Suggested fix:** Convert to `sub_tags: [tools, automation, opinion]`

---

#### Issue 4: sub_tags uses YAML list syntax instead of brackets

**File:** `wiki/sources/src_how-some-people-become-unrecognizable.md`
**Severity:** WARNING
**Category:** Frontmatter
**Issue:** `sub_tags` field uses YAML dash-list syntax instead of inline bracket syntax per format-spec §5.1
**Current:**
```yaml
sub_tags:
  - opinion
  - tools
```
**Expected:**
```yaml
sub_tags: [opinion, tools]
```
**Suggested fix:** Convert to `sub_tags: [opinion, tools]`

---

#### Issue 5: Broken wikilink

**File:** `wiki/sources/src_how-ai-productivity-fails.md`
**Severity:** WARNING
**Category:** Markdown
**Issue:** Wikilink `[[transposed-organization]]` points to a non-existent file
**Current:** Line 55 in `## Concepts referenced` section has `- [[transposed-organization]]`
**Suggested fix:** Either create `wiki/concepts/transposed-organization.md` or remove the broken link

---

## Escalations

### [SPEC CONFLICT] sources array syntax

**Issue:** format-spec.md §2.2 and §9 show `sources` field using YAML dash-list syntax:
```yaml
sources:
  - [[wiki/sources/src_<slug>]]
```
But format-spec.md §5.1 mandates: "Arrays use bracket syntax: `[item1, item2]` not YAML list syntax" with validation rule: "WARNING: Array uses YAML list syntax instead of brackets"

**Impact:** All 25 concept files in `wiki/concepts/` use YAML list syntax for the `sources` field, matching the spec's own examples. If the bracket rule applies to `sources`, all 25 files would need fixing. If the bracket rule is only for compact arrays (like `sub_tags`), the spec examples are correct.

**Recommendation:** Clarify format-spec.md — either exempt `sources` from the bracket rule, or update the examples to use bracket syntax.

---

## Statistics

- **Concept files:** 25 — all compliant (pending sources syntax clarification)
- **Source files:** 4 (2 with issues)
- **Index files (level 1):** 1 — compliant
- **Index files (level 2):** 1 — compliant
- **Index files (level 3):** 7 — all compliant

## Files verified clean

**Concepts (25):** abstraction-layer-fallacy, active-thinking, ashbys-law, casino-culture, closed-loop-system, codified-taste, complex-adaptive-systems, complicated-vs-complex, compounding-effect, cynefin-framework, discipline-system, environment-baseline, information-compression, lazy-thinking, leading-indicators, loop-ownership, negative-compounding, nice-syndrome, organizational-incrementalism, patience-vs-passivity, philosopher-syndrome, shift-left-testing, skill-atrophy, systems-thinking-limitations, taste-holders

**Sources (2 clean):** src_active-vs-lazy-thinking, src_what-comes-after-systems-thinking

**Indexes (9):** wiki/wiki.md, wiki/tag/tag.md, wiki/tag/ai.md, wiki/tag/automation.md, wiki/tag/opinion.md, wiki/tag/productivity.md, wiki/tag/research.md, wiki/tag/system.md, wiki/tag/tools.md

## Compliance rate

- **Frontmatter compliance:** 36/38 (94.7%)
- **Section structure:** 38/38 (100%)
- **Naming conventions:** 38/38 (100%)
- **Markdown syntax:** 37/38 (97.4%)

---

## Next Actions

To approve fixes: reply `approve format` in Telegram.

**Note:** The 5 WARNINGs affect only 2 files. The KB format is in very good shape. The [SPEC CONFLICT] about sources array syntax should be resolved by Julius before any fixes are applied.
