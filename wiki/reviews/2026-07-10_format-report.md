# Format Validation — 2026-07-10

**Status:** pending
**Issues found:** 308
**Created:** 2026-07-10 23:15
**Validator:** format-validator

> **Context:** Evening run after Output Validator (22:00). Previous report: 2026-07-09 (PENDING — 307 issues: 2 ERROR + 305 WARNING).
> **Delta vs 07-09:** +10 files, +1 WARNING, same 2 ERRORs remain unfixed.

---

## Delta Summary

| Metric | 2026-07-09 (previous) | 2026-07-10 (today) | Delta |
|---|---|---|---|
| Files checked | 709 | 719 | +10 |
| Concepts | 409 | 415 | +6 |
| Sources | 135 | 137 | +2 |
| Indexes | 10 | 10 | 0 |
| Topics | 155 | 157 | +2 |
| Total issues | 307 | 308 | +1 |
| ERROR | 2 | 2 | 0 |
| WARNING | 305 | 306 | +1 |
| INFO | 0 | 0 | 0 |

**Key changes:**
- ⚠️ **Same 2 ERRORs persist** — slug length (src_youre-being-trained-for-a-world-that-no-longer-exists) and missing `## Notes` in `tag.md` still unfixed
- 📈 **+10 files since yesterday** — 6 new concepts, 2 new sources, 2 new topics
- ⚠️ **+1 WARNING** — one new broken wikilink (marginal, expected growth)

---

## ERRORs (2)

### Issue 1: Slug exceeds 50-character limit

**File:** `wiki/sources/src_youre-being-trained-for-a-world-that-no-longer-exists.md`
**Severity:** ERROR
**Category:** Naming
**Issue:** Slug body is 53 characters, exceeding the 50-character maximum
**Current:** `src_youre-being-trained-for-a-world-that-no-longer-exists` (53 chars after `src_` prefix)
**Expected:** Slug body ≤ 50 characters per format-spec.md §3
**Suggested fix:** Shorten slug, e.g. `src_youre-trained-for-world-no-longer-exists` (45 chars). Update all backlinks after rename.
**Carry-over from:** 2026-07-09, 2026-07-07, 2026-07-06, 2026-07-05, 2026-07-04, 2026-07-03, 2026-07-02 ⚠️

---

### Issue 2: Missing required section in tag index

**File:** `wiki/tag/tag.md`
**Severity:** ERROR
**Category:** Sections
**Issue:** Missing required section `## Notes`
**Current:** File has ## Overview, ## Parent, ## Stats, ## Items but no ## Notes section
**Expected:** Tầng 2 index per index-spec.md §4 requires `## Notes` section
**Suggested fix:** Add `## Notes` section. If empty, write `_No notes at this time._`
**Carry-over from:** 2026-07-09, 2026-07-07, 2026-07-06, 2026-07-05, 2026-07-04, 2026-07-03, 2026-07-02 ⚠️

---

## WARNINGs (306) — Forward-reference wikilinks

All 306 WARNINGs are broken wikilinks pointing to concepts/sources that do not yet exist in the KB. This is a systemic pattern — the KB references concepts ahead of compilation.

### Top 20 most-referenced missing targets

| Target | File count |
|---|---|
| `[[game-theory]]` | 10 |
| `[[confirmation-bias]]` | 9 |
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

**193 unique broken targets across 285 individual references**, plus **21 forward-reference groups** (files where all wikilinks are forward-references batched as one warning each).

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
2. `confirmation-bias` (9 refs) — cognitive bias, widely referenced
3. `ai-coding-agents`, `career-design`, `decision-making` (5 refs each)

---

## Spec Compliance Summary

| Category | Files | ERROR | WARNING | Notes |
|---|---|---|---|---|
| **Concepts** (415) | `wiki/concepts/` | 0 | 285+21 groups | All clean — only forward-ref wikilinks |
| **Sources** (137) | `wiki/sources/` | 1 | 0 | Slug length ERROR (carry-over) |
| **Indexes** (10) | `wiki/tag/` | 1 | 0 | Missing Notes section (carry-over) |
| **Topics** (157) | `wiki/topic/` | 0 | 0 | 100% clean |
| **Raw indexes** | `raw/*/` | 0 | 0 | 100% clean |
| **Root indexes** | `wiki/wiki.md`, etc. | 0 | 0 | 100% clean |

---

## Systemic Observation

The same 2 ERRORs have now been flagged across **7 consecutive format reports** (07-02 through 07-10). Both are low-complexity fixes:

1. **Slug rename** — `src_youre-being-trained-for-a-world-that-no-longer-exists.md` → shorter name, update backlinks
2. **Add section** — `## Notes` to `wiki/tag/tag.md`

Neither has been addressed in any Fix Agent run. Recommend Julius explicitly include these in the next approval batch.

---

## Summary

| Severity | Count | Actionable |
|---|---|---|
| ERROR | 2 | ✅ Yes — both need fixing (7-day carry-over) |
| WARNING | 306 | ⏳ No — forward-refs auto-resolve |
| INFO | 0 | — |

**Recommendation:** Fix the 2 ERRORs (slug length + missing section). WARNINGs are forward-refs — approve as-is (no action). These 2 ERRORs have been stale for 7 days — strongly recommend addressing in the next Fix Agent batch.
