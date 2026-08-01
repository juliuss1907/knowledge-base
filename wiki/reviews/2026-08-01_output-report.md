# Output Validation — 2026-08-01 (22:00 Update)

**Status:** pending
**Issues found:** 3+ (1 ERROR systemic + 1 WARNING + 1 INFO + systemic patterns)
**Created:** 2026-08-01 22:00
**Validator:** output-validator
**Previous run:** Morning report 2026-08-01 (✅ APPLIED by Fix Agent) — flagged 5 double-i instances + 4 spacing merge. Now 22 double-i instances persist, suggesting either incomplete Fix Agent coverage or re-compile overwrite.

---

## Previous approved run context

Morning report at ~07:00 flagged:
- 5 new double-i instances (batch semiconductor)
- 4 new spacing merge instances
- 502/504 concepts with 1-sentence definitions
- All `✅ APPLIED by Fix Agent 2026-08-01`

Current state: 22 double-i instances still present across the same 5 files. Fix Agent either missed these files or they were re-compiled after fix application.

---

## Summary

5 new files (1 source + 4 concepts) compiled 2026-08-01. All 5 files (100%) affected by double-i typos — lần thứ 6 của Compile Agent tokenization defect. 10 forward-reference wikilinks point to not-yet-compiled concepts.

| Severity | Count | Category |
|---|---|---|
| ERROR | 1 systemic | Double-i typos (22 instances, 5/5 files) |
| WARNING | 1 | Forward-reference wikilinks (10 missing targets) |
| INFO | 1 | Empty `## Notes` section (1 file) |

---

## Issue 1: [SYSTEMATIC ISSUE] Double-i typos — lần thứ 6

**File:** All 5 new files (100% affected)
**Severity:** ERROR
**Dimension:** Vietnamese
**Issue:** Double-i typo — Compile Agent appends extra 'i' after Vietnamese grave-accented 'ờ' and other diacritic+vowel combinations. This is the 6th recurrence of the same root defect across 6 batches (06-23, 06-26, 07-01, 07-16, 07-30, 08-01).

**Evidence — 22 instances across 5 files:**

`wiki/sources/src_cuoc-ua-xem-ai-khong-i-lui-curiositypocket.md` (7 instances):
- Line 24: `ngườii` ×2 → `người`
- Line 35: `thế giớii hiện đạii` → `thế giới hiện đại`
- Line 37: `lạii`, `ngườii` → `lại`, `người`
- Line 38: `ngườii` → `người`
- Line 49: `ngườii` → `người`
- Line 51: `ngườii` → `người`

`wiki/concepts/cuoc-dua-khong-di-lui.md` (7 instances):
- Line 16: `ngườii` ×3, `giỏii`, `loạii` → `người` ×3, `giỏi`, `loại`
- Line 21: `ngườii` → `người`
- Line 22: `thờii` → `thời`

`wiki/concepts/moores-law-economics.md` (3 instances):
- Line 24: `Ngườii` ×2 → `Người` ×2
- Line 25: `hiện đạii` → `hiện đại`

`wiki/concepts/semiconductor-industry-consolidation.md` (3 instances):
- Line 23: `loạii` → `loại`
- Line 26: `lờii` → `lời`
- Line 27: `giớii` → `giới`

`wiki/concepts/technology-driven-dependence.md` (5 instances):
- Line 16: `ngườii` ×2 → `người` ×2
- Line 21: `ngườii` → `người`
- Line 23: `ngườii` → `người`
- Line 24: (embedded) `ngườii` → `người`

**Suggested fix:**
```bash
for f in wiki/sources/src_cuoc-ua-xem-ai-khong-i-lui-curiositypocket.md wiki/concepts/cuoc-dua-khong-di-lui.md wiki/concepts/moores-law-economics.md wiki/concepts/semiconductor-industry-consolidation.md wiki/concepts/technology-driven-dependence.md; do
  sed -i 's/ngườii/người/g; s/giớii/giới/g; s/lạii/lại/g; s/loạii/loại/g; s/giỏii/giỏi/g; s/thờii/thời/g; s/lờii/lời/g; s/đạii/đại/g' "$f"
done
```

**Root cause:** Compile Agent LLM prompt/tokenization mishandles the 'i' character after Vietnamese diacritic vowels. Six variants observed across 6 batches — each "fix" shifts the error rather than eliminating it. Recommend Compile Agent prompt review.

**Escalation:** 100% new files affected, 22 instances. Meets threshold for `[SYSTEMATIC ISSUE]` (>50% files + >10 instances).

---

## Issue 2: Forward-reference wikilinks — 10 missing concept targets

**File:** 4 concept files (`cuoc-dua-khong-di-lui.md`, `moores-law-economics.md`, `semiconductor-industry-consolidation.md`, `technology-driven-dependence.md`)
**Severity:** WARNING
**Dimension:** Completeness
**Issue:** All 10 wikilinks in `## Related concepts` sections point to concepts not yet compiled. These are forward-references — structural gaps that will resolve when those concepts are compiled, not errors in the current files.

**Missing targets by file:**

| File | Missing targets |
|---|---|
| `cuoc-dua-khong-di-lui.md` | `market-consolidation-dynamics`, `barriers-to-entry-innovation` |
| `moores-law-economics.md` | `economies-of-scale-semiconductor`, `process-technology-race` |
| `semiconductor-industry-consolidation.md` | `foundry-business-model`, `technological-moats`, `tsmc-dominance` |
| `technology-driven-dependence.md` | `automation-paradox`, `skill-atrophy-technology`, `human-capital-erosion` |

**Suggested fix:** No immediate fix needed. These will auto-resolve when Compile Agent processes related sources. Track as known content gaps.

---

## Issue 3: Empty `## Notes` section

**File:** `wiki/concepts/cuoc-dua-khong-di-lui.md`
**Severity:** INFO
**Dimension:** Completeness
**Issue:** `## Notes` section (line 37) is empty. Not critical — Notes is optional.
**Evidence:** Line 37: `## Notes` followed immediately by end of file (line 37, total_lines=37)
**Suggested fix:** Either remove empty section or populate with editorial notes.

---

## Systemic patterns (ongoing, not new)

| Pattern | Count | Status |
|---|---|---|
| 1-sentence definitions | 502/504 concepts | Longstanding — Compile Agent prompt needs ≥2 sentences |
| <5 key points | 86 concepts | Longstanding — Compile Agent prompt needs ≥5 items |
| Draft concepts | 335/504 (66%) | High ratio but not actionable by validator |
| ngưởi typo (original variant) | 5 files, 0 new | Carry-over from prior batches |
| ngườI capital-I typo | 6 files, 9 instances, 0 new | Carry-over from prior batches |
| người spacing merge | 12 files, 30 instances | False positives today — all 4 "new" flags are regex overlap with double-i `ngườii` (per 07-15 production lesson) |

---

## Validation checklist

| Dimension | All 5 Files | Notes |
|---|---|---|
| Factual accuracy | ✅ PASS | Claims consistent with cited source. Semiconductor timeline matches public data. |
| Completeness | ⚠️ WARNING | Forward-ref wikilinks (Issue 2). Empty Notes in 1 file (Issue 3). All required sections present otherwise — Definitions are 1-2 sentences, Key ideas 5-6 items. |
| Coherence | ✅ PASS | Logical flow. Clear arguments. No contradictions. Good inter-concept linking. |
| Vietnamese quality | ❌ ERROR | 22 double-i instances (Issue 1). Otherwise grammar and phrasing are natural. |

---

*Report generated: 2026-08-01 22:00*
*Next run: 2026-08-02 (daily at 22:00)*
