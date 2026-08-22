# Output Validation — 2026-08-13

**Status:** applied
**Approved by:** Julius
**Approved date:** 2026-08-14
**Issues found:** 3
**Created:** 2026-08-13 22:00:00
**Applied:** 2026-08-22 14:40 by fix-agent (OpenClaw)
**Validator:** output-validator

---

## Issue 1: Missing concept backlinks

**File:** wiki/concepts/repeated-games.md
**Severity:** WARNING
**Dimension:** Completeness
**Issue:** Two wikilinks reference concepts that do not exist yet: `[[game-theory]]` and `[[reputation-economics]]`. These are forward references to un-compiled concepts.
**Evidence:**
- Line 33: `[[game-theory]]` — no matching file in `wiki/concepts/` or `wiki/sources/`
- Line 34: `[[reputation-economics]]` — no matching file in `wiki/concepts/` or `wiki/sources/`
**Suggested fix:** Either compile the missing concepts, or remove the dead links from Related concepts.

---

## Issue 2: Near-duplicate concept names — costly-signaling vs costly-signal

**File:** wiki/concepts/costly-signaling.md + wiki/concepts/costly-signal.md
**Severity:** INFO
**Dimension:** Coherence
**Issue:** Two concepts with near-identical names and overlapping content. `costly-signaling.md` focuses on the theoretical mechanism (time as costly signal, Spence 1973 application to comebacks), while `costly-signal.md` focuses on practical application (making invisible competence visible to the market). Both reference each other in Related concepts. Naming is confusing — readers may not know which one to look up.
**Evidence:** Both define costly signaling/signal theory. `costly-signaling.md` sources only `src_how-to-come-back-from-anything-game-theory`, while `costly-signal.md` sources three including the same comeback source. They cross-reference each other.
**Suggested fix:** Consider merging into one concept, or rename to clearly distinguish (e.g., `costly-signaling-theory` vs `costly-signal-career`). Current naming is too similar.

---

## Issue 3: Overlapping concepts — identity-detachment vs identity-transformation

**File:** wiki/concepts/identity-detachment.md + wiki/concepts/identity-transformation.md
**Severity:** INFO
**Dimension:** Coherence
**Issue:** Two concepts sourced from the same material (`src_just-let-go-cipheron`) covering highly overlapping territory. `identity-detachment` focuses on the act of letting go of the old self, while `identity-transformation` focuses on stepping into the new self. Both reference each other in Related concepts. The boundary between "detachment" and "transformation" is thin — readers may find the distinction unclear.
**Evidence:** Both define "buông bỏ phiên bản hiện tại của bản thân" as core mechanism. Both source `src_just-let-go-cipheron`. Both cross-reference each other.
**Suggested fix:** Consider merging (detachment is a prerequisite step of transformation), or clarify the boundary in each Definition. If kept separate, add a note in each explaining how they differ.

---

## Summary

- **Files checked:** 665 (168 sources + 524 concepts) — full scan
- **New files since last validation (2026-08-01):** 32 (7 sources + 25 concepts)
- **Issues:** 0 ERROR, 1 WARNING, 2 INFO
- **Overall quality:** Good. All 32 new files are well-structured with complete sections. Vietnamese quality is natural, no typos or dropped-i variants detected. No truncated files. No systematic issues.
- **Carry-over from prior batches:** quick-scan reports existing typos in older files (5 ngưởi, 8 double-i, 9 spacing-merge, 6 capital-I) — these are all in files from prior batches, not new. 85 concepts have <5 key ideas, 522 have 1-sentence definitions — these are pre-existing systemic issues not addressed yet.