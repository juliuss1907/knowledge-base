# Format Validation — 2026-07-09

**Status:** approved
**Approved by:** Julius
**Issues found:** 307
**Created:** 2026-07-09 23:16
**Validator:** format-validator

> **Context:** Evening run after Output Validator (22:00). Previous approved baseline: 2026-06-23 (APPLIED with 463 issues: 134 ERROR, 319 WARNING).
> **Delta:** -156 total (-132 ERROR, -14 WARNING), +75 files checked. All previous ERROR categories resolved. Remaining issues are 2 actionable ERRORs + 305 forward-reference wikilink WARNINGs (same systemic pattern as prior runs).

---

## Delta Summary

| Metric | 2026-06-23 (baseline) | 2026-07-09 (today) | Delta |
|---|---|---|---|
| Files checked | 634 | 709 | +75 |
| Total issues | 463 | 307 | -156 |
| ERROR | 134 | 2 | -132 ✅ |
| WARNING | 319 | 305 | -14 |
| INFO | 0 | 0 | 0 |

**Key changes:**
- ✅ **main_tag errors resolved** — the 134 ERRORs from 06-23 (misclassified main_tag values) are gone
- ✅ **Missing section errors resolved** — tag files previously missing sections are fixed (except `tag.md` — see Issue 2)
- ⏳ **Forward-reference wikilinks persist** — 305 WARNINGs remain as expected (concepts not yet compiled)

---

## ERRORs (2)

### Issue 1: Slug exceeds 50-character limit

**File:** `wiki/sources/src_youre-being-trained-for-a-world-that-no-longer-exists.md`
**Severity:** ERROR
**Category:** Naming
**Issue:** Slug is 53 characters, exceeding the 50-character maximum
**Current:** `src_youre-being-trained-for-a-world-that-no-longer-exists` (53 chars)
**Expected:** Slug ≤ 50 characters
**Suggested fix:** Shorten slug, e.g. `src_youre-trained-for-world-no-longer-exists` (45 chars). Update all backlinks after rename.

---

### Issue 2: Missing required section in tag index

**File:** `wiki/tag/tag.md`
**Severity:** ERROR
**Category:** Sections
**Issue:** Missing required section `## Notes`
**Current:** File has ## Summary, ## Items, ## Stats but no ## Notes section
**Expected:** Tầng 2 index per index-spec.md §4 requires `## Notes` section
**Suggested fix:** Add `## Notes` section. If empty, write `_No notes at this time._`

---

## WARNINGs (305) — Forward-reference wikilinks

All 305 WARNINGs are broken wikilinks pointing to concepts/sources that do not yet exist in the KB. This is a systemic pattern — the KB references concepts ahead of compilation.

### Top 20 most-referenced missing targets

| Target | File count |
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

**193 unique broken targets across 284 individual references**, plus **21 forward-reference groups** (files where all wikilinks are forward-references batched as one warning each).

### Forward-reference groups (21)

Files where all broken wikilinks were batched:
- `wiki/concepts/third-order-thinking.md` — 6 links
- `wiki/concepts/thought-experiment.md` — 6 links
- `wiki/sources/src_code-as-agent-harness-arxiv-2605-18747.md` — 6 links
- `wiki/sources/src_farnam-street-mental-models-biology-series.md` — 6 links
- `wiki/sources/src_farnam-street-mental-models-systems-thinking.md` — 6 links
- `wiki/sources/src_incentives-hidden-forces.md` — 6 links
- `wiki/sources/src_probabilistic-thinking.md` — 6 links
- `wiki/sources/src_mental-models-of-art.md` — 9 links
- `wiki/sources/src_mental-models-of-economics.md` — 9 links
- `wiki/sources/src_thought-experiment.md` — 9 links
- `wiki/sources/src_fs-blog-mental-models.md` — 7 links
- Plus 10 more files with 4 links each (see raw output for full list)

### Files with most individual broken links (top 5)

| File | Broken count |
|---|---|
| `wiki/concepts/collaborative-thinking.md` | 5 |
| `wiki/concepts/probabilistic-thinking.md` | 5 |
| `wiki/concepts/feedback-loops.md` | 4 |
| `wiki/concepts/hanlons-razor.md` | 4 |
| `wiki/concepts/meaning-through-work.md` | 4 |

### Resolution path for forward-reference warnings

These WARNINGs will auto-resolve as referenced concepts are compiled. **No action needed** — this is expected behavior for a growing KB. Priority candidates for compilation (most-referenced):
1. `game-theory` (10 refs) — foundational concept, high value
2. `confirmation-bias` (8 refs) — cognitive bias, widely referenced
3. `ai-coding-agents`, `career-design`, `decision-making` (5 refs each)

---

## Summary

| Severity | Count | Actionable |
|---|---|---|
| ERROR | 2 | ✅ Yes — both need fixing |
| WARNING | 305 | ⏳ No — forward-refs auto-resolve |
| INFO | 0 | — |

**Recommendation:** Fix the 2 ERRORs (slug length + missing section). WARNINGs are forward-refs — approve as-is (no action). Same pattern as 07-06 and 07-07 reports.
