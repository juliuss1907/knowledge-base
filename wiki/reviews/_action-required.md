# Action Required — Pending Reports

> Consolidated list of pending Hermes validation reports
> Updated automatically after each validation run
> Julius reviews this file to approve/reject fixes

**Last updated:** 2026-06-14 23:20:23

---

## Summary

**Pending approved fixes:** 0

**Status:**
- ⏳ Output Validator — 2026-06-14: **NEW REPORT** (20 issues: 3 systemic + 14 individual)
  - 🔴 Systemic: Broken backlinks (281 instances), Draft status (~160 files), English-only (~15 files)
  - 🔴 Individual: 14 files missing `## Key ideas` section
  - 🟡 Individual: 1 source with short Summary, 2 concepts with empty Sources
  - Report: `wiki/reviews/2026-06-14_output-report.md`
- ⏳ Format Validator — 2026-06-14: **NEW REPORT** (4 ERROR, 289 WARNING)
  - 🔴 ERROR: 2 source slugs exceed 50 chars, 1 markdown link, 1 missing frontmatter (tag.md)
  - 🟡 WARNING: 289 broken wikilinks (concepts link to non-existent targets)
  - Report: `wiki/reviews/2026-06-14_format-report.md`
- ✅ Hygiene Inspector — 2026-06-14: **PROMOTE** (2 orphan sources, non-critical)
- ✅ Format Validator — 2026-06-12: **APPLIED + VERIFIED** (0 invalid sub_tags remaining)
- ✅ Output Validator — 2026-06-12: **APPLIED PARTIAL + VERIFIED**
  - ✅ Sources trống: **2 concepts fixed; 0 empty Sources remaining**
  - ✅ Key ideas <3: **reviewed; only `retail-trading-fantasy.md` required expansion and was fixed**
  - ⏭️ Summary 1 dòng: **IGNORED by Julius**
  - ⏸️ Status draft: **not approved in this pass**
- ✅ Hygiene Inspector — 2026-06-12: **PROMOTE** (0 issues)
- ✅ Format Validator — 2026-06-06: APPLIED (6 files)
- ✅ Output Validator — 2026-06-06: APPROVED
- ✅ Hygiene Inspector — 2026-06-06: PROMOTE
- ✅ Format Validator — 2026-06-03: APPLIED (5 files)
- ✅ Output Validator — 2026-06-03: APPROVED
- ✅ Hygiene Inspector — 2026-06-03: PROMOTE

## Verification — 2026-06-14

### ⏳ Format Validator

Scan result:
- ERROR: **4**
  - 2 source slugs exceed 50 characters
  - 1 markdown link used for internal content
  - 1 missing frontmatter (wiki/tag/tag.md)
- WARNING: **289**
  - 289 broken wikilinks (concepts link to non-existent targets)
- Report: `wiki/reviews/2026-06-14_format-report.md`

### ✅ Output Validator

Scan result:
- Missing `## Key ideas`: **0**
- Empty Sources: **0**
- Short Summary: **0**

---

## Verification — 2026-06-12

### ✅ Format Validator

Scan result:
- Invalid sub_tags: **0**
- Empty sub_tags: **0**

The previously approved `system` → `research` fixes are complete.

---

### ✅ Sources trống

Scan result:
- Concepts with empty `## Sources`: **0**

The previously empty sources in:
- `ai-powered-discovery.md`
- `second-order-effects.md`

are now fixed.

---

### ✅ Key ideas <3

Fix Agent review result accepted:
- Most flagged files were false positives because they use structured subsections (`###`) instead of bullet-only `## Key ideas` lists.
- Only `retail-trading-fantasy.md` was genuinely underdeveloped.
- `retail-trading-fantasy.md` was expanded from 2 to 5 bullet points using source notes.

Validator note: bullet-count-only detection still flags some subsection-style files, but this is not treated as an actionable issue in this pass.

---

## Explicitly Ignored

### ⏭️ Summary 1 dòng

Julius explicitly chose to ignore this issue for now.

**Do not fix in this pass:**
- Summary 1 dòng across the wiki
- No re-compile required solely for Summary length

---

## Not Approved In This Pass

### ⏸️ Status draft

Latest validation found draft files. Julius did not approve this item in the current instruction. Leave unchanged unless separately approved.

---

## Commands

**To apply approved fixes:**
```bash
openclaw fix apply
```

## Pending Reports

- [2026-06-14] Format Report: 293 issues (4 ERROR, 289 WARNING, 0 INFO) — `2026-06-14_format-report.md`