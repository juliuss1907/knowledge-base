# Format Validation — 2026-07-23

**Status:** pending
**Issues found:** 337
**ERRORs**: 1
**WARNINGS**: 336
**INFOS:** 0
**Created:** 2026-07-23 23:15
**Validator:** format-validator
**Files checked:** 828
**Total issues**: 337
Files checked: 828
Total issues: 337

> **Δ from 07-22 (previous, pending):** +13 files (815→828), +19 issues (318→337). +9 concepts, +2 sources, +2 topics. +1 ERROR (new — `wiki/tag/psychology.md` missing `## Co-occurring tags`), +18 WARNING (new forward-reference wikilinks from fresh compilation batch).
>
> **Δ from 07-20 (last approved):** +32 files (796→828), +19 issues (318→337). +1 ERROR (first since 07-14 clean streak baseline broken). +18 WARNING. +27 concepts, +5 sources, +0 indexes, +5 topics since 07-20.

---

## Issue 1: Missing required section in tag index

**File:** wiki/tag/psychology.md
**Severity:** ERROR
**Category:** Sections
**Issue:** Missing required section `## Co-occurring tags` — tag index files (level 3) must have this section per index-spec.md §5.
**Current:** File has sections: Parent, Stats, Files with this tag — but no Co-occurring tags
**Expected:** Add `## Co-occurring tags` section after `## Files with this tag`

---

## Summary

| Metric | Value | Δ from 07-22 | Δ from 07-20 |
|---|---|---|---|
| Files checked | 828 | +13 | +32 |
| Concepts | 466 | +9 | +27 |
| Sources | 153 | +2 | +5 |
| Indexes | 33 | 0 | 0 |
| Topics | 176 | +2 | +5 |
| **Total issues** | **337** | **+19** | **+19** |
| ERRORs | 1 | +1 | +1 |
| WARNINGs | 336 | +18 | +18 |
| Unique broken targets | 211 | +13 | — |

### Issue breakdown

| Category | Count | Details |
|---|---|---|
| **Sections (ERROR)** | 1 | `wiki/tag/psychology.md` missing `## Co-occurring tags` |
| **Broken wikilinks (WARNING)** | 334 | Forward references to uncompiled concepts/sources + 2 raw file `original` false positives |
| ├─ Individual links | 313 | Each listed with file + target |
| ├─ Forward-ref groups | 21 | Batched with `N broken wikilinks (forward-references)` summary |
| └─ Raw file `original` | 2 | `original` field points to raw file that exists but validator resolution failed (false positive) |
| **Frontmatter** | 0 | All required fields present and valid |
| **Naming** | 0 | All filenames and slugs valid |
| **Markdown syntax** | 0 | All code blocks, lists, emphasis valid |

---

## Top 20 Broken Wikilink Targets

| # | Target | Count |
|---|---|---|
| 1 | `[[game-theory]]` | 10 |
| 2 | `[[confirmation-bias]]` | 8 |
| 3 | `[[src_you-just-hired-a-million-bad-employees-a16z.md]]` | 5 |
| 4 | `[[ai-coding-agents]]` | 5 |
| 5 | `[[career-design]]` | 5 |
| 6 | `[[decision-making]]` | 5 |
| 7 | `[[deep-work]]` | 4 |
| 8 | `[[attention-economy]]` | 3 |
| 9 | `[[ai-hype-vs-reality]]` | 3 |
| 10 | `[[economic-inequality]]` | 3 |
| 11 | `[[critical-thinking]]` | 3 |
| 12 | `[[naval-ravikant]]` | 3 |
| 13 | `[[risk-parity]]` | 3 |
| 14 | `[[second-law-of-thermodynamics]]` | 3 |
| 15 | `[[saying-no]]` | 3 |
| 16 | `[[power-imbalance]]` | 3 |
| 17 | `[[src_why-the-math-mafia-is-doing-well-jesse-zhang.md]]` | 3 |
| 18 | `[[first-order-thinking]]` | 3 |
| 19 | `[[momentum]]` | 2 |
| 20 | `[[multi-agent-systems]]` | 2 |

---

## Top 10 Files by Warning Count

| # | File | Count |
|---|---|---|
| 1 | `wiki/concepts/collaborative-thinking.md` | 5 |
| 2 | `wiki/concepts/probabilistic-thinking.md` | 5 |
| 3 | `wiki/concepts/feedback-loops.md` | 4 |
| 4 | `wiki/concepts/hanlons-razor.md` | 4 |
| 5 | `wiki/concepts/meaning-through-work.md` | 4 |
| 6 | `wiki/concepts/occams-broom.md` | 4 |
| 7 | `wiki/concepts/occams-razor.md` | 4 |
| 8 | `wiki/concepts/systematic-trading.md` | 4 |
| 9 | `wiki/concepts/vibe-coding.md` | 4 |
| 10 | `wiki/concepts/activation-energy.md` | 3 |

---

## Forward-Reference Groups (21)

These files have 4–9 broken wikilinks each, batched into summary groups:

| # | File | Count |
|---|---|---|
| 1 | `wiki/sources/src_mental-models-of-art.md` | 9 |
| 2 | `wiki/sources/src_mental-models-of-economics.md` | 9 |
| 3 | `wiki/sources/src_thought-experiment.md` | 9 |
| 4 | `wiki/sources/src_fs-blog-mental-models.md` | 7 |
| 5 | `wiki/concepts/third-order-thinking.md` | 6 |
| 6 | `wiki/concepts/thought-experiment.md` | 6 |
| 7 | `wiki/sources/src_code-as-agent-harness-arxiv-2605-18747.md` | 6 |
| 8 | `wiki/sources/src_farnam-street-mental-models-biology-series.md` | 6 |
| 9 | `wiki/sources/src_farnam-street-mental-models-systems-thinking.md` | 6 |
| 10 | `wiki/sources/src_incentives-hidden-forces.md` | 6 |

*11 more groups with 4 broken links each (see raw output for full list).*

---

## Issue: Raw file `original` wikilink resolution false positives

**Severity:** WARNING
**Category:** Frontmatter

Two source files have `original` frontmatter fields the validator flags as "raw file not found", but the raw files actually exist (verified):

| Source file | `original` value | Raw file path | Status |
|---|---|---|---|
| `src_you-just-hired-a-million-bad-employees-a16z.md` | `[[2026-07-15_you-just-hired-a-million-bad-employees-a16z.md]]` | `raw/articles/2026-07-15_you-just-hired-a-million-bad-employees-a16z.md` | ✅ Exists |
| `src_why-the-math-mafia-is-doing-well-jesse-zhang.md` | `[[2026-07-14_why-the-math-mafia-is-doing-well-jesse-zhang.md]]` | `raw/articles/2026-07-14_why-the-math-mafia-is-doing-well-jesse-zhang.md` | ✅ Exists |

These are **false positives** — the validator's `original` field resolution doesn't search raw subdirectories. Same root cause as the documented pitfall but applies to the `original` frontmatter field.

**Suggested fix:** Update `validate.py` `check_original_wikilink()` to search raw subdirectories.

---

## Verification

- [x] Validation script ran cleanly (0 errors reading files)
- [x] All 828 files parsed successfully
- [x] 1 ERROR: `wiki/tag/psychology.md` missing `## Co-occurring tags` — first structural ERROR since 07-14 clean streak
- [x] 334 WARNINGs are broken wikilinks — expected forward references to uncompiled concepts/sources
- [x] 2 raw file `original` references verified — files exist, false positive
- [x] Clean streak broken at day 9 — first ERROR since 07-14 baseline (index-spec.md §5 compliance gap)
- [x] +18 new WARNINGs from compilation activity on 07-23 (+13 files)

---

## Escalations

### [SYSTEMATIC VIOLATION]
**Pattern:** `wiki/tag/psychology.md` is the only tag index missing `## Co-occurring tags` — all 32 other level-3 tag indexes have this section.
**Likely cause:** Index Agent failed to add the section when `psychology` tag was created or when the tag's last concept was updated.
**Recommendation:** Fix Agent should add `## Co-occurring tags` section to `wiki/tag/psychology.md`. Review Index Agent to ensure all tag indexes receive this section on creation/update.
