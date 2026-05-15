# Format Validation — 2026-05-14

**Status:** pending
**Issues found:** 3
**Created:** 2026-05-14 23:18:48
**Validator:** format-validator

**Files checked:** 14 (2 sources + 12 concepts)

---

## Issue 1: Extra field `date_ingested` in source frontmatter

**File:** 
- `wiki/sources/src_what-comes-after-systems-thinking.md`
- `wiki/sources/src_active-vs-lazy-thinking.md`

**Severity:** WARNING
**Category:** Frontmatter
**Issue:** Both source files include a `date_ingested` field that is not defined in format-spec §3.2. The format-spec defines only 8 fields for source frontmatter: `type`, `original`, `main_tag`, `sub_tags`, `topic`, `date_compiled`, `url` (optional), `author` (optional). The `date_ingested` field appears to be a legacy field from format-spec v1.0 that was renamed to `date_compiled` in v2.0 (2026-05-09).

**Current:**
```yaml
date_ingested: 2026-04-02
date_compiled: 2026-05-14
```

**Expected:** Only `date_compiled` (no `date_ingested`).

**Suggested fix:** Remove the `date_ingested` line from both source files. `date_compiled` already captures the compilation date.

---

## Issue 2: Field order disrupted by `date_ingested`

**File:**
- `wiki/sources/src_what-comes-after-systems-thinking.md`
- `wiki/sources/src_active-vs-lazy-thinking.md`

**Severity:** WARNING
**Category:** Frontmatter
**Issue:** The `date_ingested` field appears between `topic` and `date_compiled`, disrupting the required field order per format-spec §3.2:
```
topic → date_compiled → url → author
```
Current order in both files:
```
topic → date_ingested → date_compiled → url → author
```

**Current:**
```yaml
topic: post-systems-thinking
date_ingested: 2026-04-02
date_compiled: 2026-05-14
url: ...
author: ...
```

**Expected:**
```yaml
topic: post-systems-thinking
date_compiled: 2026-05-14
url: ...
author: ...
```

**Suggested fix:** Remove `date_ingested` entirely (see Issue 1). This automatically restores correct field order.

---

## Issue 3: Bare slug wikilinks in concept `sources` field (vs format-spec convention)

**File:**
- `wiki/concepts/systems-thinking-limitations.md`
- `wiki/concepts/complex-adaptive-systems.md`
- `wiki/concepts/cynefin-framework.md`
- `wiki/concepts/complicated-vs-complex.md`
- `wiki/concepts/ashbys-law.md`

**Severity:** INFO
**Category:** Markdown / Wikilinks
**Issue:** These 5 concept files use bare-slug wikilinks in the frontmatter `sources` field (`[[src_what-comes-after-systems-thinking]]`). The format-spec §2.2 schema and §9 examples consistently use the full path form `[[wiki/sources/src_what-comes-after-systems-thinking]]` for concepts referencing sources. Both forms resolve correctly in Obsidian, but the full-path form is the documented convention.

This is the inverse of the Output Validator's Issue 1 — which flagged 7 productivity-topic concepts for using the full-path form. The format-spec documents full paths as the schema, while noting bare slugs as a simplification (line 140: "INFO: Could use wikilink instead of full path for internal links").

**Current:**
```yaml
sources:
  - [[src_what-comes-after-systems-thinking]]
```

**Expected per format-spec example:**
```yaml
sources:
  - [[wiki/sources/src_what-comes-after-systems-thinking]]
```

**Suggested fix:** Standardize to one convention across all concept files. Recommend aligning with format-spec examples (`[[wiki/sources/src_<slug>]]`) for consistency. Julius may want to clarify which convention is canonical.

---

## Validation Summary

| Category | ERROR | WARNING | INFO | Total |
|---|---|---|---|---|
| Frontmatter | 0 | 2 | 0 | 2 |
| Sections | 0 | 0 | 0 | 0 |
| Naming | 0 | 0 | 0 | 0 |
| Markdown / Wikilinks | 0 | 0 | 1 | 1 |
| **Total** | **0** | **2** | **1** | **3** |

---

## Clean Checks (no issues found)

- ✅ **Naming:** All 14 files follow lowercase-hyphen slugs, within 50-char limit, correct prefix (`src_`) for sources
- ✅ **Section structure:** All required sections present in correct order; H2 used for all section headers; no Setext headers; no skipped heading levels
- ✅ **YAML syntax:** All frontmatter blocks have valid YAML, correct delimiters, bracket syntax for arrays
- ✅ **Tag validity:** All `main_tag` values exist in TAGS.md Pool A; all `sub_tags` values exist in Pool B; no `#` prefix on tags
- ✅ **Date format:** All dates use valid ISO 8601 YYYY-MM-DD format
- ✅ **Code blocks:** No code blocks present in any file (no language tag issues)
- ✅ **Lists:** Consistent use of `-` for unordered lists across all files
- ✅ **Emphasis:** Consistent use of `**bold**` (no `__bold__` found)
- ✅ **Wikilink syntax:** No spaces around brackets, no external URLs in wikilinks, no broken targets
- ✅ **Optional sections:** `## Original excerpts` in sources and `## Notes` in concepts are recognized optional sections per format-spec

---

## Systemic Observation

**Pattern:** The `date_ingested` field appears in both source files and may be a systematic issue in Compile Agent. Format-spec v2.0 renamed `date_ingested` → `date_compiled` (2026-05-09 change log), but Compile Agent may still be emitting the legacy field alongside the new one.

**Recommendation:** Review Compile Agent's frontmatter generation to ensure it only emits `date_compiled`, not both fields. Check `.openclaw/skills/compile-agent/SKILL.md`.

---

## Ambiguity Flag

```
[FORMAT UNCERTAINTY]
File: All 12 concept files
Issue: Two conflicting conventions exist for sources wikilinks:
  - Format-spec §2.2 + §9 examples: [[wiki/sources/src_<slug>]]
  - Output Validator recommendation: [[src_<slug>]] (bare slug)
  - Format-spec line 140: "INFO: Could use wikilink instead of full path"
Question: Which is the canonical convention? Bare slug is simpler; full path is verbatim from spec examples.
Recommendation: Julius to clarify in format-spec.md or resolve the contradiction.
```
