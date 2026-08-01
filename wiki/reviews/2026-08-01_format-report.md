# Format Validation — 2026-08-01

**Status:** pending
**Issues found:** 433
**Created:** 2026-08-01 23:15
**Validator:** format-validator
**Files checked:** 886 (504 concepts + 161 sources + 34 indexes + 187 topics)

**Δ from 2026-07-30 (last approved):** +19 files (+9 concepts, +2 sources, +0 indexes, +8 topics), +22 issues (411→433). **0-ERROR streak BROKEN** (was 9 days: 07-22 through 07-30) — 3 ERRORs surfaced.

---

## Issues Found: 433

| Files checked | Concepts | Sources | Indexes | Topics |
|---|---|---|---|---|
| 886 | 504 | 161 | 34 | 187 |

| Severity | Count | Category |
|---|---|---|
| **ERRORs**: 3 | 1 | Invalid sub_tag not in TAGS.md |
| | 2 | Missing required section in tag indexes |
| **WARNINGS**: 430 | 410 | Individual broken wikilinks (forward-references) |
| | 20 | Forward-reference summary groups |
| **INFOS:** 0 | — | — |

**0-ERROR streak:** 9 days (07-22 → 07-30) BROKEN today. 3 ERRORs detected.

---

## ERROR 1: Invalid sub_tag — not in TAGS.md

**File:** `wiki/concepts/optionality-principle.md`
**Severity:** ERROR
**Category:** Frontmatter
**Issue:** `sub_tags` contains `"career"` — not in TAGS.md Pool A or Pool B
**Current:** `sub_tags: [psychology, career]`
**Expected:** All sub_tags must be in TAGS.md Pool B (or Pool A tags that are also in Pool B)
**Suggested fix:** Replace `career` with a valid Pool B tag, or propose adding `career` to TAGS.md Pool B. Pool A tag candidates: `productivity` (current main_tag). Valid Pool B sub-tags for this concept: `psychology`, `opinion`, `research`, `tutorial`

---

## ERROR 2: Missing required section — ## Co-occurring tags

**File:** `wiki/tag/opinion.md`
**Severity:** ERROR
**Category:** Sections
**Issue:** Missing required section `## Co-occurring tags` (required by index-spec.md §5.3 for Tầng 3 tag files)
**Current:** Section absent from file
**Expected:** `## Co-occurring tags` section with top 5 co-occurring tags ranked by frequency
**Suggested fix:** Index Agent should regenerate `wiki/tag/opinion.md` with all required sections including `## Co-occurring tags`

---

## ERROR 3: Missing required section — ## Co-occurring tags

**File:** `wiki/tag/research.md`
**Severity:** ERROR
**Category:** Sections
**Issue:** Missing required section `## Co-occurring tags` (required by index-spec.md §5.3 for Tầng 3 tag files)
**Current:** Section absent from file
**Expected:** `## Co-occurring tags` section with top 5 co-occurring tags ranked by frequency
**Suggested fix:** Index Agent should regenerate `wiki/tag/research.md` with all required sections including `## Co-occurring tags`

---

## WARNINGs: Broken Wikilinks (Forward-References) — 430 total

All 430 WARNINGs are **broken wikilinks** — concepts and sources linking to target concepts that have not yet been compiled. This is a forward-reference pattern, not a structural format error.

### Breakdown

| Category | Count |
|---|---|
| Individual broken wikilinks (≤5 per file) | 410 |
| Forward-reference summary groups (>5 per file) | 20 |
| **Unique broken targets** | **278** |

### Top 20 Broken Link Targets

| Target | Occurrences | Category |
|---|---|---|
| `[[game-theory]]` | 10x | Social science / economics |
| `[[src_agent-memory-7-types-substack.md]]` | 8x | Source wikilink (has `.md` suffix) |
| `[[confirmation-bias]]` | 8x | Psychology / cognitive science |
| `[[src_you-just-hired-a-million-bad-employees-a16z.md]]` | 5x | Source wikilink (has `.md` suffix) |
| `[[src_the-let-them-theory-gabriel-reality.md]]` | 5x | Source wikilink (has `.md` suffix) |
| `[[ai-coding-agents]]` | 5x | AI / tech |
| `[[src_how-to-remember-everything-you-read-dan-koe.md]]` | 5x | Source wikilink (has `.md` suffix) |
| `[[career-design]]` | 5x | Career / productivity |
| `[[decision-making]]` | 5x | Psychology |
| `[[deep-work]]` | 4x | Productivity |
| `[[src_cuoc-ua-xem-ai-khong-i-lui-curiositypocket.md]]` | 4x | Source wikilink (has `.md` suffix) |
| `[[src_introducing-backsearch-gr-inc.md]]` | 3x | Source wikilink (has `.md` suffix) |
| `[[src_monid-ai-agent-tool-platform.md]]` | 3x | Source wikilink (has `.md` suffix) |
| `[[attention-economy]]` | 3x | Economics / media |
| `[[ai-hype-vs-reality]]` | 3x | AI / tech |
| `[[economic-inequality]]` | 3x | Economics |
| `[[critical-thinking]]` | 3x | Psychology / education |
| `[[naval-ravikant]]` | 3x | Person / philosophy |
| `[[risk-parity]]` | 3x | Finance / investment |
| `[[second-law-of-thermodynamics]]` | 3x | Physics |

### Top 10 Files by Warning Count

| File | WARNINGS |
|---|---|
| `wiki/concepts/collaborative-thinking.md` | 5 |
| `wiki/concepts/probabilistic-thinking.md` | 5 |
| `wiki/concepts/feedback-loops.md` | 4 |
| `wiki/concepts/hanlons-razor.md` | 4 |
| `wiki/concepts/meaning-through-work.md` | 4 |
| `wiki/concepts/occams-broom.md` | 4 |
| `wiki/concepts/occams-razor.md` | 4 |
| `wiki/concepts/parametric-memory.md` | 4 |
| `wiki/concepts/pay-per-call-pricing.md` | 4 |
| `wiki/concepts/prospective-memory.md` | 4 |

### Source Wikilinks with `.md` Suffix (~11 instances)

Source wikilinks in concept bodies use `.md` suffix (e.g., `[[src_agent-memory-7-types-substack.md]]`) instead of bare slugs (`[[src_agent-memory-7-types-substack]]`). This is a pattern introduced by the new memory theory batch. While Obsidian resolves both forms, it deviates from format-spec.md convention (bare slugs preferred).

**Pattern note:** First observed 07-30 (~11 instances). These targets are flagged as broken because the validator strip-and-glob logic may not handle the `.md` suffix correctly in all cases. Some of these source files do exist under `wiki/sources/` — the broken-wikilink flag is likely a false positive from the `.md` suffix pattern.

---

## [SYSTEMATIC VIOLATION]

**Pattern:** `## Co-occurring tags` section missing from 2 tag index files (`opinion.md`, `research.md`)  
**Likely cause:** Index Agent not regenerating these files with full required sections after tag reclassification or tag addition  
**Recommendation:** Review Index Agent SKILL.md — ensure Tầng 3 tag file regeneration always includes `## Co-occurring tags` section

---

## [FORMAT UNCERTAINTY]

**Issue:** `sub_tags` contains `"career"` — not in TAGS.md  
**File:** `wiki/concepts/optionality-principle.md`  
**Question:** Should `career` be added to TAGS.md Pool B, or should this concept use an existing Pool B tag?  
**Context:** `career` was previously flagged in the 08-01 morning run as a Pool A tag that is not also in Pool B. This may indicate compile-agent using a tag that doesn't exist in either pool.

---

## Verification

- [x] All 886 files scanned (504 concepts + 161 sources + 34 indexes + 187 topics)
- [x] Validation script output parsed: 3 ERROR + 430 WARNING + 0 INFO
- [x] Code fence regression check: no false-positive language-tag errors (line-by-line validation)
- [x] Raw-subdir wikilink resolution: `original` field validation uses 7 raw subdirectories
- [x] Source-body wikilinks: validated against raw/ subdirectories (not just wiki/concepts + wiki/sources)
- [x] Topic files (187): dispatched to light topic validation (no false `level` field ERRORs)
- [x] `context/USER.md`: skipped (read-only, no frontmatter expected)
- [x] Index files with path-level override: `wiki/tag/tag.md` correctly routed as Tầng 2
- [x] Unquoted wikilinks in YAML: handled as WARNING (not false ERROR)
- [x] YAML date parsing: `datetime.date` objects accepted alongside string dates

Files checked: 886
Total issues: 433

---

**Total issues**: 433

## Escalations

1. **[SYSTEMATIC VIOLATION]** — 2 tag files (`opinion.md`, `research.md`) missing `## Co-occurring tags`. Likely Index Agent defect. Recommend reviewing index-agent SKILL.md.

2. **[FORMAT UNCERTAINTY]** — `career` tag used in `optionality-principle.md` sub_tags but not in TAGS.md. Julius decides: add to Pool B or replace with existing tag.

---

*End of report.*
