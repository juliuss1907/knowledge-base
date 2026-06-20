# Output Validation — 2026-06-17

**Status:** approved
**Approved by:** Julius
**Issues found:** 6
**Created:** 2026-06-17 23:07:09
**Validator:** output-validator

**Files checked:** 100 (9 sources + 14 concepts new, 77 existing)
**New files (compiled today):** 23

---

## Issue 1: SYSTEMIC — Vietnamese spelling error "ngưởi" → "người"

**File:** Multiple (9 source files, all from today's batch)
**Severity:** WARNING
**Dimension:** Vietnamese
**Issue:** Consistent misspelling of "người" (person/people) as "ngưởi" across multiple source files. The correct Vietnamese diacritic is circumflex + hook (ườ), not circumflex + hook reversed (ưở). This appears in nearly every Vietnamese-language source compiled today.

**Evidence:**
- `wiki/sources/src_tai-chinh-ca-nhan-9-ban-co-ang-thuc.md` line 34: *"Ngưởi dùng tiền để mua 'cái nhìn của những ngưởi xung quanh'"*
- `wiki/sources/src_after-the-heater-rule-keeps-you-alive.md` line 34: *"Trader sống sót không phải ngưởi biết khi nào đánh mạnh"*
- `wiki/sources/src_how-average-people-will-get-rich-with-ai.md` line 23: *"cách ngưởi bình thường có thể làm giàu"*

**Suggested fix:** Replace all occurrences of "ngưởi" with "người" across affected files. Likely source: Compile Agent prompt or LLM diacritic rendering artifact.

---

## Issue 2: SYSTEMIC — All 14 new concepts have status: draft

**File:** All 14 new concept files (wiki/concepts/*.md compiled 2026-06-17)
**Severity:** WARNING
**Dimension:** Completeness
**Issue:** Every concept file compiled today carries `status: draft` in frontmatter. This is consistent with the broader systemic issue (~160+ draft concepts across the wiki) previously flagged in the 2026-06-14 Output Validation report.

**Evidence:**
- `seed-vs-machine-architecture.md` — `status: draft`
- `ai-coach-prompting.md` — `status: draft`
- `systematic-trading.md` — `status: draft`
- ... (11 more, identical pattern)

**Suggested fix:** Either set `status: done` for concepts that are complete, or keep `draft` intentionally. This was flagged previously (2026-06-14) and marked as "Not Approved In This Pass" by Julius.

---

## Issue 3: SYSTEMIC — Broken wikilinks: 25+ references target non-existent concepts

**File:** 9 source files + 14 concept files (today's batch)
**Severity:** WARNING
**Dimension:** Coherence
**Issue:** Today's new files reference 25+ concepts that do not exist yet. These are forward-references expected to be filled by future compilation passes. This is consistent with the broader 289 broken wikilinks pattern flagged in Format Validator 2026-06-14.

**Non-existent targets referenced (top 15 by frequency):**
- `trading-psychology` (referenced from src_after-the-heater + heater-rule concept)
- `post-win-discipline`, `dry-powder-strategy` (from src_after-the-heater + heater-rule)
- `saving-rate-vs-return`, `psychology-of-money`, `wealth-gap-analysis` (from src_tai-chinh + lifestyle-inflation)
- `discretionary-vs-systematic-trading`, `trading-cognitive-biases`, `walk-forward-analysis` (from src_the-cost + systematic-trading)
- `swap-test`, `semantic-layer-moat`, `ora-system`, `three-layer-shift` (from src_the-seed + seed-vs-machine)
- `monte-carlo-simulation` (from systematic-trading concept)
- `attention-economy`, `prospective-memory`, `deep-work` (from brain-rot + cognitive-load concepts)

**Suggested fix:** These are expected forward-references. The Compile Agent should prioritize creating these concepts in the next compilation pass, or sources should only reference already-existing concepts.

---

## Issue 4: Key points exceed maximum (11 items, limit is 10)

**File:** wiki/sources/src_the-cost-of-discretion.md
**Severity:** INFO
**Dimension:** Completeness
**Issue:** Key points section has 11 bullet items. The recommended range is 5-10.

**Evidence:** Lines 27-38 contain 11 distinct key points, all substantive.

**Suggested fix:** Consolidate or merge 2 adjacent points to stay within the 5-10 range. E.g., points about "4 cognitive holes" and "cannot discipline out of biases" could be merged.

---

## Issue 5: Key points exceed maximum (11 items, limit is 10)

**File:** wiki/sources/src_cach-nhanh-nhat-nop-ho-so-bao-hiem-that-nghiep.md
**Severity:** INFO
**Dimension:** Completeness
**Issue:** Key points section has 11 bullet items. The recommended range is 5-10.

**Evidence:** Lines 27-37 contain 11 distinct key points covering BHTN calculation, process, and psychological barriers.

**Suggested fix:** Merge 2 adjacent points. E.g., the 3 separate points about thời gian (wait time) could be consolidated into one.

---

## Issue 6: Missing "Published" date in metadata

**File:** wiki/sources/src_how-average-people-will-get-rich-with-ai.md, wiki/sources/src_dan-koe-workflow-analysis-markus.md
**Severity:** INFO
**Dimension:** Completeness
**Issue:** Both source files about Dan Koe's article are missing the `- **Published:**` field in their Metadata section. Other source files in the same batch include this field (e.g., src_the-cost-of-discretion has `- **Published:** June 16, 2026`).

**Evidence:**
- `src_how-average-people-will-get-rich-with-ai.md`: Metadata has Author, Source, URL, Original file — but no Published date.
- `src_dan-koe-workflow-analysis-markus.md`: Same — Author, Original author, Source, URL, Original file — no Published date.

**Suggested fix:** Add `- **Published:** June 17, 2026` (for Dan Koe article) and `- **Published:** June 17, 2026` (for Markus analysis) to respective Metadata sections.

---

## Summary

| Severity | Count |
|---|---|
| ERROR | 0 |
| WARNING | 3 (all systemic) |
| INFO | 3 |

**Systemic issues detected:**
1. Vietnamese "ngưởi" typo — 9 files (Compile Agent rendering artifact)
2. All new concepts carry `status: draft` — 14 files (already known, not approved in prior pass)
3. Broken wikilinks — 25+ targets (consistent with 289-link pattern, expected forward-refs)

**Individual issues:**
4-5. Two source files with 11 key points (1 over limit)
6. Two source files missing Published date in Metadata

**Overall assessment:** Today's batch is well-compiled. Content faithfully represents source material. No factual errors or contradictions detected. Vietnamese language quality is good aside from the single systematic "ngưởi" typo. Completeness is high — all required sections present in all files. The main quality gap is broken wikilinks, which is an expected artifact of incremental compilation rather than a content quality issue.

**No ERRORs — no files need to be blocked from referencing.**
