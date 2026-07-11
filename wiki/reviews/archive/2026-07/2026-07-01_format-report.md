# Format Validation — 2026-07-01

**Status:** approved
**Issues found:** 312 (1 ERROR → approved, 311 WARNING, 0 INFO)
**Created:** 2026-07-01 23:15:00 +0700
**Approved:** 2026-07-02 — Slug length exception approved by Julius (53 chars acceptable)
**Validator:** format-validator
**Scope:** Full KB — 665 files (374 concepts + 120 sources + 32 indexes + 139 topics)

---

## Delta from last approved (2026-06-30 23:17)

| Metric | 2026-06-30 (APPROVED) | 2026-07-01 | Delta |
|---|---|---|---|
| Scope | 634 files | 665 files | **+31** |
| ERROR | 128 | 1 | **−127** |
| WARNING | 311 | 311 | **0** |
| INFO | 0 | 0 | 0 |

**Positive delta (issues resolved):**
- ✅ **128 topic-file frontmatter ERROR → GONE** — All 139 `wiki/topic/*.md` files now have proper YAML frontmatter. The systematic regression from 06-30 is fully resolved. Topic count also grew (+11 files, 139 vs 128).
- ✅ **Tag-file section ERRORs → still resolved** — 69 tag-file section ERRORs from 06-29 remain resolved (confirmed stable since 06-30).

**Negative delta (new/regression):**
- 🔴 **+1 new naming ERROR**: `src_youre-trained-for-world-that-no-longer-exists.md` — slug exceeds 50 chars (53 chars). This is a different file from the 06-28 slug-too-long issue (`src_give-me-14-minutes-and-ill-destroy-your-procrastination-forever.md`, 63 chars), which has since been resolved/renamed.

**WARNING delta:**
- ⚠️ **Stable at 311 WARNING**: broken wikilinks unchanged (290 individual + 21 forward-reference summary groups)
- 194 unique broken targets (same as 06-30 and 06-29)
- Top broken targets unchanged: `game-theory` (10x), `confirmation-bias` (8x), `pareto-principle` (6x)

**Files growth:** +31 files since 06-30 (374 concepts + 120 sources vs 361 concepts + 112 sources)

---

## Summary

Tình hình format compliance cải thiện đáng kể: 127 ERROR từ 06-30 đã được resolve (128 topic frontmatter ERROR → 0), chỉ còn 1 ERROR mới về slug quá dài trên 1 file source mới. WARNING count ổn định ở mức 311, toàn bộ là broken wikilinks (forward references đến các concept chưa được compile).

---

## Issue 1: Slug exceeds 50-character limit

**File:** `wiki/sources/src_youre-trained-for-world-that-no-longer-exists.md`
**Severity:** ERROR
**Category:** Naming
**Issue:** Source file slug is 53 characters, exceeding the 50-character limit defined in `format-spec.md`.
**Current:** `src_youre-trained-for-world-that-no-longer-exists` (53 chars)
**Expected:** Slug ≤ 50 characters
**Suggested fix:** Shorten slug, e.g. `src_youre-trained-for-world-that-no-longer-exists` (44 chars) or `src_trained-for-a-world-that-no-longer-exists` (42 chars). Rename both the file and update the `original` frontmatter field.

---

## Issue Group 2: Broken wikilinks — forward references (311 WARNING)

**Category:** Markdown
**Severity:** WARNING
**Count:** 311 (290 individual broken targets + 21 forward-reference summary groups)
**Unique broken targets:** 194

### Top 20 broken targets

| Target | Occurrences |
|---|---|
| `game-theory` | 10 |
| `confirmation-bias` | 8 |
| `pareto-principle` | 6 |
| `ai-coding-agents` | 5 |
| `career-design` | 5 |
| `decision-making` | 5 |
| `deep-work` | 4 |
| `ai-hype-vs-reality` | 3 |
| `economic-inequality` | 3 |
| `critical-thinking` | 3 |
| `naval-ravikant` | 3 |
| `risk-parity` | 3 |
| `second-law-of-thermodynamics` | 3 |
| `saying-no` | 3 |
| `power-imbalance` | 3 |
| `first-order-thinking` | 3 |
| `breaking-point` | 2 |
| `momentum` | 2 |
| `multi-agent-systems` | 2 |
| `dao-legal-structure` | 2 |

### Files with most broken wikilinks

| File | Broken links |
|---|---|
| `wiki/concepts/collaborative-thinking.md` | 5 |
| `wiki/concepts/probabilistic-thinking.md` | 5 |
| `wiki/concepts/feedback-loops.md` | 4 |
| `wiki/concepts/hanlons-razor.md` | 4 |
| `wiki/concepts/meaning-through-work.md` | 4 |
| `wiki/concepts/occams-broom.md` | 4 |
| `wiki/concepts/occams-razor.md` | 4 |
| `wiki/concepts/systematic-trading.md` | 4 |
| `wiki/concepts/vibe-coding.md` | 4 |
| `wiki/concepts/activation-energy.md` | 3 |

### Forward-reference summary groups (21)

These files have multiple broken wikilinks grouped into a single summary warning per file. Each represents a cluster of forward references to concepts not yet compiled:

- `wiki/concepts/third-order-thinking.md` — 6 broken wikilinks
- `wiki/concepts/thought-experiment.md` — 6 broken wikilinks
- `wiki/sources/src_11-minutes-hack-github.md` — 4 broken wikilinks
- `wiki/sources/src_6-thoi-quen-binh-thuong-dang-huy-hoai-nao-bo.md` — 4 broken wikilinks
- `wiki/sources/src_ai-future-skills.md` — 4 broken wikilinks
- `wiki/sources/src_code-as-agent-harness-arxiv-2605-18747.md` — 6 broken wikilinks
- `wiki/sources/src_critical-thinking-dennett.md` — 4 broken wikilinks
- `wiki/sources/src_farnam-street-mental-models-biology-series.md` — 6 broken wikilinks
- `wiki/sources/src_farnam-street-mental-models-systems-thinking.md` — 6 broken wikilinks
- `wiki/sources/src_feedback-loops-mental-model.md` — 4 broken wikilinks
- `wiki/sources/src_fs-blog-mental-models.md` — 7 broken wikilinks
- `wiki/sources/src_global-macro-investing.md` — 4 broken wikilinks
- `wiki/sources/src_hermes-polymarket-btc-trading-agent.md` — 4 broken wikilinks
- `wiki/sources/src_incentives-hidden-forces.md` — 6 broken wikilinks
- `wiki/sources/src_mental-models-of-art.md` — 9 broken wikilinks
- `wiki/sources/src_mental-models-of-economics.md` — 9 broken wikilinks
- `wiki/sources/src_probabilistic-thinking.md` — 6 broken wikilinks
- `wiki/sources/src_the-cost-of-discretion.md` — 4 broken wikilinks
- `wiki/sources/src_the-seed-and-the-machine.md` — 4 broken wikilinks
- `wiki/sources/src_thought-experiment.md` — 9 broken wikilinks
- `wiki/sources/src_tribute-system-new-world-order.md` — 4 broken wikilinks

---

## KB Health Assessment

| Dimension | Status | Trend |
|---|---|---|
| Frontmatter compliance (concepts + sources) | ✅ Clean | 0 errors |
| Topic file frontmatter | ✅ Clean | Resolved from 128→0 |
| Tag file structure | ✅ Clean | Stable since 06-30 |
| Section structure | ✅ Clean | 0 errors |
| Naming conventions | ⚠️ 1 file | +1 new slug violation |
| Markdown / Wikilinks | ⚠️ 311 warnings | Stable backlog |
| Code block language tags | ✅ Clean | Resolved since 06-29 |
| Overall | 🟢 Good | 99.85% clean (1/665 files with ERROR) |

---

## Actions Required

1. **Slug rename (1 file):** ~~Rename `src_youre-trained-for-world-that-no-longer-exists.md`~~ → **APPROVED by Julius. 53-char slug accepted as exception.** No action required.

2. **Broken wikilink backlog (194 targets, 311 occurrences):** No action needed — these are expected forward references in a growing KB. Will resolve naturally as concepts get compiled.

3. **No systemic violations detected.** The topic frontmatter regression from 06-30 is confirmed resolved and stable.
