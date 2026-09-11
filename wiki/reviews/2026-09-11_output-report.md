# Output Validation — 2026-09-11

**Status:** pending
**Issues found:** 4
**Created:** 2026-09-11 23:00:50
**Validator:** output-validator

---

## Summary

**Files checked:** 774 (197 sources + 573 concepts)
**New files:** 8 (1 source + 7 concepts — compiled 2026-09-11)
**Issues found:** 4 (0 ERROR, 1 WARNING, 3 INFO)
**Result:** Pipeline active after 9-day idle. 8 new files from `src_0xhvdes-seven-ways-to-get-ahead` batch. Quality is high — definitions solid, key ideas comprehensive, sources fully backlinked. Dropped-i variant-5 grep: 0 matches (streak: **13 consecutive** clean runs 08-23→09-11).

---

## Issue 1: Forward-refs without raw source (3 targets)

**File:** wiki/concepts/increasing-surface-area-luck.md, wiki/concepts/proximity-to-opportunity.md
**Severity:** WARNING
**Dimension:** Completeness
**Issue:** 3 wikilinks point to concepts with no concept file, no source file, and no raw material in `raw/`. No natural resolution path exists.
**Evidence:**
- `[[serendipity-engineering]]` in increasing-surface-area-luck.md line 30
- `[[career-pivots]]` in increasing-surface-area-luck.md line 31
- `[[network-effects]]` in proximity-to-opportunity.md line 33
**Suggested fix:** Two options: (a) compile these concepts when suitable raw sources arrive, or (b) Fix Agent drops the links. Format Validator will track targets in broken-targets backlog.

---

## Issue 2: Personal reference in talent-stack.md

**File:** wiki/concepts/talent-stack.md
**Severity:** INFO
**Dimension:** Coherence
**Issue:** Key idea bullet 4 contains a direct personal reference to Julius.
**Evidence:** Line 25: "Julius với combo viết + crypto + AI là ví dụ điển hình"
**Suggested fix:** Either keep intentional (owner's KB, personal example) or replace with generic example. Minor — no action blocking.

---

## Issue 3: Multi-source backlink gap check — clean

**File:** (aggregate check across all multi-source concepts)
**Severity:** INFO (pass)
**Dimension:** Completeness
**Issue:** All 3 multi-source concepts (asymmetric-positions: 3 sources, compounding-effect: 4 sources, talent-stack: 3 sources) have matching frontmatter vs body `## Sources` counts. No backlink gap detected. Defect A from 08-31 not recurring.

---

## Issue 4: Source section-name check — clean

**File:** wiki/sources/src_0xhvdes-seven-ways-to-get-ahead.md
**Severity:** INFO (pass)
**Dimension:** Completeness
**Issue:** New source file correctly uses `## Key points` (not `## Key ideas`). Defect C from 08-31 not recurring.

---

## Carry-over (unchanged)

- 112 concepts with 1-sentence definitions (depth-debt baseline, legacy)
- 84 concepts with <5 key ideas (depth-debt baseline, legacy)
- `[[prompt-injection]]` no-source forward-ref still open (2 refs, unchanged since 09-02)
- Dropped-i variant-5 streak: 13 consecutive (08-23 → 09-11). Demotion to weekly recommended 5th time (08-30/08-31/09-01/09-08/09-11), not confirmed.
