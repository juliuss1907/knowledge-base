# Format Validation — 2026-07-05

**Status:** pending
**Issues found:** 306
**Created:** 2026-07-05 23:16:05 +0700
**Validator:** format-validator

---

## Delta Summary

**Baseline:** 2026-07-04 (approved)

| Metric | 07-04 | 07-05 | Δ |
|---|---|---|---|
| Files in scope | 694 | 700 | +6 |
| Concepts | 388 | 392 | +4 |
| Sources | 126 | 127 | +1 |
| Indexes | 33 | 33 | 0 |
| Topics | 147 | 148 | +1 |
| **ERROR** | 3 | **2** | −1 ✅ |
| **WARNING** | 328 | **304** | −24 ✅ |
| **INFO** | 0 | 0 | 0 |
| Total issues | 331 | 306 | −25 ✅ |

**Positive delta (issues resolved):**
- ✅ 24 unquoted wikilink WARNINGs → resolved (Index Agent template fix working since 07-03 confirmed stable, no regression this run)
- ✅ 1 `tag/tag.md` section ERROR resolved (`## Overview` + `## Parent` now present)
- ✅ Error count down: 2 vs 3 (tag/tag.md now only missing `## Items`)

**Negative delta (new issues):**
- None. All metrics improved or stable.

**Stable (unchanged):**
- 🔒 Broken wikilink backlog: 283 individual + 21 forward-reference groups — unchanged from 07-04
- 🔒 Unique broken targets: 192 — unchanged
- 🔒 Topic files: all 148 pass cleanly
- 🔒 Slug exception: `src_youre-being-trained-for-a-world-that-no-longer-exists.md` (53 chars) — pre-approved, still present

---

## Issue 1: Slug exceeds 50-char limit (pre-approved exception)

**File:** wiki/sources/src_youre-being-trained-for-a-world-that-no-longer-exists.md
**Severity:** ERROR
**Category:** Naming
**Issue:** Slug `youre-being-trained-for-a-world-that-no-longer-exists` is 53 characters, exceeding the 50-char limit
**Current:** `src_youre-being-trained-for-a-world-that-no-longer-exists.md`
**Expected:** Slug ≤ 50 chars per format-spec.md naming rules
**Status:** Pre-approved exception by Julius (07-01). Keep as-is. Listed for tracking only.

---

## Issue 2: Missing required section `## Items`

**File:** wiki/tag/tag.md
**Severity:** ERROR
**Category:** Sections
**Issue:** `## Items` section is required for Tầng 2 index files per index-spec.md §4.2 but is missing
**Current:** File has `## Overview`, `## Parent`, `## Notes` but lacks `## Items`
**Expected:** All four required sections present: `## Overview`, `## Parent`, `## Items`, `## Notes`
**Progress:** This is the last remaining tag/tag.md ERROR (down from 5 on 07-03 → 2 on 07-04 → 1 today). Sections `## Overview` and `## Parent` were added since 07-04.
**Suggested fix:** Add `## Items` section listing all child tag files in `wiki/tag/`

---

## WARNINGs Summary

### Broken wikilinks (283 individual + 21 forward-reference groups)

All 304 WARNINGs are broken wikilinks. These are forward-references to concepts that have not yet been compiled or are planned but not yet created. This is a known and accepted backlog — no action required unless Julius wants to prioritize compiling specific missing concepts.

**Top 10 broken targets (by frequency):**

| Target | Count |
|---|---|
| `[[game-theory]]` | 10 |
| `[[confirmation-bias]]` | 8 |
| `[[ai-coding-agents]]` | 5 |
| `[[career-design]]` | 5 |
| `[[decision-making]]` | 5 |
| `[[deep-work]]` | 4 |
| `[[ai-hype-vs-reality]]` | 3 |
| `[[economic-inequality]]` | 3 |
| `[[critical-thinking]]` | 3 |
| `[[naval-ravikant]]` | 3 |

**Top 10 files by broken link count:**

| File | Broken links |
|---|---|
| `collaborative-thinking.md` | 5 |
| `probabilistic-thinking.md` | 5 |
| `feedback-loops.md` | 4 |
| `hanlons-razor.md` | 4 |
| `meaning-through-work.md` | 4 |
| `occams-broom.md` | 4 |
| `occams-razor.md` | 4 |
| `systematic-trading.md` | 4 |
| `vibe-coding.md` | 4 |
| `third-order-thinking.md` | 6 (group) |

### Forward-reference groups (21 files)

21 source and concept files use summary-format for broken wikilinks (e.g., "6 broken wikilinks (forward-references to uncompiled concepts)"). This is the correct format-spec.md convention for files with many broken links — no action required.

---

## Clean zones

- ✅ **148 topic files** — all pass validation (stable since 07-01)
- ✅ **33 index files** (excluding tag/tag.md) — all pass
- ✅ **YAML frontmatter** — all 700 files have valid YAML, no parse errors
- ✅ **Code blocks** — all have language tags (regression fix from 06-25 confirmed stable)
- ✅ **Section structure** — all concept/source files have required sections in correct order
- ✅ **Naming conventions** — all files comply (except pre-approved slug exception)
- ✅ **Unquoted wikilinks** — no regression (Index Agent template fix confirmed stable since 07-03)

---

## [ESCALATION] tag/tag.md section regression pattern

`wiki/tag/tag.md` has now been flagged across 4 consecutive runs (07-02 through 07-05). The ERROR count decreased from 5 → 2 → 1 as sections were progressively added, but the file is still incomplete.

**Pattern:** Index Agent regenerates `wiki/tag/tag.md` without all required sections per index-spec.md.

**Recommendation:** Update `index-agent/SKILL.md` to include the full `## Items` section template for tag/tag.md regeneration. Without a template fix, this ERROR will persist or resurface on every Index Agent run.

---

## Key metrics

| Metric | Value |
|---|---|
| Format health | 99.71% (698/700 files with 0 ERROR) |
| Broken wikilink backlog | 192 unique targets (stable) |
| Files in scope | 700 (+6 since 07-04) |
| KB growth | +5 content files, +1 topic index |
| Clean topic files | 148/148 (100%) |
| Clean index files | 32/33 (97%) |
