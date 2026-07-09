# Format Validation — 2026-07-06

**Status:** approved
**Issues found:** 305
**Created:** 2026-07-06 23:16:24 +0700
**Validator:** format-validator

---

## Delta Summary

| Metric | 2026-07-05 (APPROVED) | 2026-07-06 | Δ |
|---|---|---|---|
| Files checked | 700 | **709** | +9 |
| — Concepts | 392 | 397 | +5 |
| — Sources | 127 | 129 | +2 |
| — Indexes | 33 | 33 | 0 |
| — Topics | 148 | 150 | +2 |
| ERROR | 2 | **1** | **−1** ✅ |
| WARNING | 304 | 304 | 0 |
| INFO | 0 | 0 | 0 |
| Broken targets | 192 | 192 | 0 |

**Positive delta:**
- ✅ −1 ERROR: `wiki/tag/tag.md` `## Items` section missing → **RESOLVED** (section added, 5-run progression: 5 → 2 → 1 → 0)
- ✅ tag/tag.md now 100% compliant after 5 consecutive runs with section errors (07-02 through 07-06)

**Stable:**
- Broken wikilink backlog: 192 unique targets (unchanged — all forward-references)
- 21 forward-reference summary groups: unchanged
- 150 topic files: all clean (stable since 07-01)
- 0 new issues introduced in this batch

**Negative delta:** None — all metrics stable or improved.

---

## Issue 1: Pre-approved slug exception

**File:** `wiki/sources/src_youre-being-trained-for-a-world-that-no-longer-exists.md`
**Severity:** ERROR
**Category:** Naming
**Issue:** Slug exceeds 50 chars (53 chars)
**Current:** `src_youre-being-trained-for-a-world-that-no-longer-exists` (53 chars)
**Expected:** Slug ≤ 50 chars per format-spec.md
**Suggested fix:** None — pre-approved by Julius (2026-07-02). Carry-over from 07-01 through 07-06.

---

## Issue 2–305: Broken wikilinks (forward-references)

**Severity:** WARNING
**Category:** Markdown
**Count:** 304 total (283 individual + 21 forward-reference summary groups)
**Issue:** 192 unique targets across concepts and sources reference concepts that have not yet been compiled

### Top 20 broken targets

| Target | Occurrences |
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
| `[[risk-parity]]` | 3 |
| `[[second-law-of-thermodynamics]]` | 3 |
| `[[saying-no]]` | 3 |
| `[[power-imbalance]]` | 3 |
| `[[first-order-thinking]]` | 3 |
| `[[breaking-point]]` | 2 |
| `[[momentum]]` | 2 |
| `[[multi-agent-systems]]` | 2 |
| `[[dao-legal-structure]]` | 2 |
| `[[ubi-universal-basic-income]]` | 2 |

### Forward-reference groups (21 files)

Files with ≥4 broken wikilinks that will auto-resolve when referenced concepts are compiled:

- `wiki/sources/src_mental-models-of-art.md`: 9 broken wikilinks
- `wiki/sources/src_mental-models-of-economics.md`: 9 broken wikilinks
- `wiki/sources/src_thought-experiment.md`: 9 broken wikilinks
- `wiki/sources/src_fs-blog-mental-models.md`: 7 broken wikilinks
- `wiki/concepts/third-order-thinking.md`: 6 broken wikilinks
- `wiki/concepts/thought-experiment.md`: 6 broken wikilinks
- `wiki/sources/src_code-as-agent-harness-arxiv-2605-18747.md`: 6 broken wikilinks
- `wiki/sources/src_farnam-street-mental-models-biology-series.md`: 6 broken wikilinks
- `wiki/sources/src_farnam-street-mental-models-systems-thinking.md`: 6 broken wikilinks
- `wiki/sources/src_incentives-hidden-forces.md`: 6 broken wikilinks
- `wiki/sources/src_probabilistic-thinking.md`: 6 broken wikilinks
- And 10 more files with 4 broken wikilinks each

**Suggested fix:** No immediate action — all broken wikilinks are forward-references to concepts not yet in the KB. They will auto-resolve when Compile Agent creates those concepts. This is a systemic backlog, not individual file errors.

---

## Health Summary

| Dimension | Status |
|---|---|
| **Frontmatter** | ✅ All files compliant |
| **Sections** | ✅ All files compliant (tag/tag.md resolved!) |
| **Naming** | ⚠️ 1 pre-approved slug exception |
| **Markdown** | ⚠️ 304 forward-reference broken wikilinks |
| **Topic files** | ✅ 150/150 clean |
| **Index files** | ✅ 33/33 clean |

**KB format health:** 99.86% (708/709 files ERROR-free)
**Tags/topics ERRORs:** 0 (fully resolved — 5 consecutive clean runs for topics, tag/tag.md now clean)
