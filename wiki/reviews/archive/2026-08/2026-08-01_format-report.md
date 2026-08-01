# Format Validator Report — 2026-08-01

**Status:** applied
**Applied by:** Fix Agent
**Applied at:** 2026-08-01
**Approved by:** Julius
**Approved date:** 2026-08-01
**Issues found:** 438
**Created:** 2026-08-01
**Validator:** format-validator
**Files checked:** 882 (504 concepts + 161 sources + 34 indexes + 183 topics)
**Delta from 07-30:** +15 files (+9 concepts, +2 sources, +4 topics), +27 issues (411→438)

---

## Issues Found: 438

| Severity | Count | Category |
|---|---|---|
| ERROR | **5** | Pool A tags in sub_tags (4) + source sub_tags (1) |
| WARNING | **433** | Broken wikilinks (forward-refs) + field order (3) |
| INFO | 0 | — |

**⚠️ 0-ERROR streak BROKEN.** 9 consecutive clean days (07-22 through 07-30) ended.

---

## CRITICAL — Pool A tags used as sub_tags

Compile Agent regression: `tech` and `economic` (Pool A main-tags) are being used as sub_tags again. This was supposed to be fixed in workflow.md.

### Affected files (5):

| # | File | Invalid sub_tags |
|---|---|---|
| 1 | `wiki/concepts/moores-law-economics.md` | `tech` (Pool A) |
| 2 | `wiki/concepts/optionality-principle.md` | `economic` (Pool A) |
| 3 | `wiki/concepts/semiconductor-industry-consolidation.md` | `tech` (Pool A) |
| 4 | `wiki/concepts/technology-driven-dependence.md` | `tech` (Pool A) |
| 5 | `wiki/sources/src_cuoc-ua-xem-ai-khong-i-lui-curiositypocket.md` | `tech` (Pool A) |

**Fix:** Replace `tech` → appropriate Pool B tag (e.g. `tools`, `automation`, `vibecode`, `research`). Replace `economic` → appropriate Pool B tag.

---

## WARNING — Extra frontmatter fields

3 files have non-standard frontmatter fields causing field order warnings:

| # | File | Extra field |
|---|---|---|
| 1 | `wiki/concepts/moores-law-economics.md` | `field` |
| 2 | `wiki/concepts/semiconductor-industry-consolidation.md` | `core_industry` |
| 3 | `wiki/concepts/technology-driven-dependence.md` | `field` |

These are harmless but non-standard. Compile Agent template may be injecting them.

---

## WARNING — Broken wikilinks

433 forward-reference broken wikilinks — same pattern as before. +22 WARNINGs vs 07-30.

### New batch: semiconductor-themed concepts

New concepts from `src_cuoc-ua-xem-ai-khong-i-lui-curiositypocket` (source):
- `cuoc-dua-khong-di-lui.md` — link đến `barriers-to-entry-innovation`, `market-consolidation-dynamics`
- `moores-law-economics.md` — link đến `economies-of-scale-semiconductor`, `process-technology-race`
- `semiconductor-industry-consolidation.md` — link đến `foundry-business-model`, `technological-moats`, `tsmc-dominance`
- `technology-driven-dependence.md` — link đến `automation-paradox`, `human-capital-erosion`, `skill-atrophy-technology`

---

## ✅ Passing

- ✅ All YAML sections parse correctly
- ✅ sub_tags count within range (1-3) — but contents wrong
- ✅ All tags exist in TAGS.md — but wrong pool
- ✅ Section order valid
- ✅ No duplicate YAML keys
- ✅ File naming conventions followed
- ✅ Wikilink format correct

---

## New Files Since 07-30

**Concepts (9 new):**
- `colin-powell-40-70-rule.md`
- `cuoc-dua-khong-di-lui.md`
- `decision-cost-analysis.md`
- `moores-law-economics.md`
- `optionality-principle.md` *(re-compiled?)*
- `semiconductor-industry-consolidation.md`
- `small-bets-strategy.md`
- `technology-driven-dependence.md`

**Sources (2 new):**
- `src_cuoc-ua-xem-ai-khong-i-lui-curiositypocket.md`

---

## Verdict

**REVISE** — 5 ERRORs (Pool A tags in sub_tags) + 3 WARNINGs (extra fields). Fix Agent can handle all.

### Action items:
1. **Fix Agent:** Replace `tech` in sub_tags → valid Pool B tag (4 files concept + 1 source)
2. **Fix Agent:** Replace `economic` → valid Pool B tag (1 file)
3. **Fix Agent:** Remove extra `field`/`core_industry` frontmatter fields (3 files)
4. **Compile Agent:** Re-check workflow.md — Pool A leakage into sub_tags đã tái diễn
