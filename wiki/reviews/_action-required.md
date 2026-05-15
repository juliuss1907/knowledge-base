# Action Required — Pending Reviews

> Consolidated list of pending Hermes validation reports
> Updated automatically after each validation run
> Julius reviews this file to approve/reject fixes

**Last updated:** 2026-05-15 08:00:00

---

## Summary

**Pending reports:** 3

**Status:**
- Output Validator: 1 pending report (4 issues — **1 ERROR ready for Fix Agent**)
- Format Validator: 1 pending report (3 issues — **2 WARNING ready for Fix Agent**)
- Hygiene Inspector: **RESOLVED** — folder-structure.md updated to v1.1, all folders created, spec ambiguities resolved

**Fixed by Julius (2026-05-15):**
- ✅ folder-structure.md → v1.1: runtime artifacts whitelisted (§3.1 & §3.2), symlinks allowed (§2), skills expanded (§4)
- ✅ format-spec.md → wikilink canonical: bare slug `[[src_slug]]`, full path deprecated (§6.1 & §6.2)
- ✅ Created missing folders: `wiki/drafts/`, `wiki/reviews/archive/`, `wiki/tag/`, `wiki/topic/`

---

## 🔴 Critical Issues (Fix Immediately)

### Output Validator — 2026-05-14

**1. Incorrect wikilink format in frontmatter `sources` field** — ERROR  
→ **APPROVED for Fix Agent**
- 7 concept files use `[[wiki/sources/src_active-vs-lazy-thinking]]` instead of `[[src_active-vs-lazy-thinking]]`
- Affected files:
  - `wiki/concepts/philosopher-syndrome.md`
  - `wiki/concepts/information-compression.md`
  - `wiki/concepts/abstraction-layer-fallacy.md`
  - `wiki/concepts/organizational-incrementalism.md`
  - `wiki/concepts/nice-syndrome.md`
  - `wiki/concepts/lazy-thinking.md`
  - `wiki/concepts/active-thinking.md`
- **Fix:** Replace `[[wiki/sources/src_active-vs-lazy-thinking]]` → `[[src_active-vs-lazy-thinking]]` in each file's frontmatter `sources` field

### Format Validator — 2026-05-14

**1. Legacy `date_ingested` field in source files** — WARNING  
→ **APPROVED for Fix Agent**
- 2 source files have `date_ingested` field (removed in format-spec v2.0)
- Affected files:
  - `wiki/sources/src_what-comes-after-systems-thinking.md`
  - `wiki/sources/src_active-vs-lazy-thinking.md`
- **Fix:** Remove the `date_ingested` line from both files (keep `date_compiled`)

### Hygiene Inspector — 2026-05-14

✅ **RESOLVED by Julius** — folder-structure.md updated to v1.1, all folders created

---

## 🟡 Warnings (Can Fix Later)

### Output Validator — 2026-05-14

**1. Empty `## Notes` sections in all 12 concept files** — WARNING
- All concept files have empty Notes section headers
- Either remove or add annotations
- ⏳ Not urgent — can wait for Julius review

### Format Validator — 2026-05-14

**1. Field order disrupted by `date_ingested`** — WARNING  
→ **FIXED by removing `date_ingested` (see Critical Issues above)**

### Hygiene Inspector — 2026-05-14

**1. Non-standard file in skill folder** — WARNING
- ✅ **RESOLVED** — `validation-criteria.md` now allowed in folder-structure.md §4

---

## 🟢 Info & Suggestions

### Output Validator — 2026-05-14

**1. Source summaries at minimum boundary (3 sentences)** — INFO
- Both source files (`src_what-comes-after-systems-thinking`, `src_active-vs-lazy-thinking`) at exactly 3 sentences

**2. Key points above recommended range** — INFO
- 3 files (2 sources + 1 concept) have 10-11 items vs 5-10 target

### Hygiene Inspector — 2026-05-14

**1-4. Expected subfolders not yet created** — INFO
- `wiki/tag/`, `wiki/topic/`, `wiki/drafts/`, `wiki/reviews/archive/` — create as needed

---

## Pending Reports

### 1. Output Validation — 2026-05-14

**File:** [2026-05-14_output-report.md](2026-05-14_output-report.md)
**Status:** partially approved
**Created:** 2026-05-14 23:00:00
**Issues:** 4 (1 ERROR → Fix Agent, 1 WARNING, 2 INFO)

**Actions for Fix Agent:**
- Fix wikilink format in 7 concept files (see Critical Issues above)

---

### 2. Format Validation — 2026-05-14

**File:** [2026-05-14_format-report.md](2026-05-14_format-report.md)
**Status:** partially approved
**Created:** 2026-05-14 23:18:48
**Issues:** 3 (0 ERROR, 2 WARNING → 1 Fix Agent, 1 INFO)

**Actions for Fix Agent:**
- Remove `date_ingested` field from 2 source files (see Critical Issues above)

---

### 3. Hygiene Inspection — 2026-05-14 ✅ RESOLVED

**File:** [2026-05-14_hygiene-report.md](2026-05-14_hygiene-report.md)
**Status:** resolved
**Created:** 2026-05-14 23:34:24
**Resolution:** folder-structure.md v1.1 + missing folders created
- 14 issues all addressed via spec update

---

## Recently Applied

<!-- Reports applied in last 7 days appear here -->
<!-- Auto-cleaned after 7 days -->

*No recently applied reports.*

---

## Commands

**To approve a report:**
approve output
approve format
approve hygiene

**To view full report:**
show output
show format
show hygiene

**To reject a report:**
reject output
reject format
reject hygiene

**To apply approved fixes:**
openclaw fix apply
