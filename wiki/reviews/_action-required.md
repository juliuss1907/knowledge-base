# Action Required — Pending Reviews

> Consolidated list of pending Hermes validation reports
> Updated automatically after each validation run
> Julius reviews this file to approve/reject fixes

**Last updated:** 2026-05-17 23:35:00

---

## Summary

**Pending reports:** 5

**Status:**
- Output Validator: 1 pending report (4 issues -- **1 ERROR ready for Fix Agent**)
- Format Validator: 2 pending reports (2026-05-14: 3 issues -> 1 Fix Agent / 2026-05-17: 5 issues -- **5 WARNING ready for Fix Agent**)
- Hygiene Inspector: 1 pending report (20 issues -- 2 ERROR, 18 WARNING -> **most are spec gaps in runtime folder whitelists**)

**Fixed by Julius (2026-05-15):**
- [x] folder-structure.md -> v1.1: runtime artifacts whitelisted (S3.1 & S3.2), symlinks allowed (S2), skills expanded (S4)
- [x] format-spec.md -> wikilink canonical: bare slug `[[src_slug]]`, full path deprecated (S6.1 & S6.2)
- [x] Created missing folders: `wiki/drafts/`, `wiki/reviews/archive/`, `wiki/tag/`, `wiki/topic/`

---

## Critical Issues (Fix Immediately)

### Output Validator -- 2026-05-14

**1. Incorrect wikilink format in frontmatter `sources` field** -- ERROR  
-> **APPROVED for Fix Agent**
- 7 concept files use `[[wiki/sources/src_active-vs-lazy-thinking]]` instead of `[[src_active-vs-lazy-thinking]]`
- Affected files:
  - `wiki/concepts/philosopher-syndrome.md`
  - `wiki/concepts/information-compression.md`
  - `wiki/concepts/abstraction-layer-fallacy.md`
  - `wiki/concepts/organizational-incrementalism.md`
  - `wiki/concepts/nice-syndrome.md`
  - `wiki/concepts/lazy-thinking.md`
  - `wiki/concepts/active-thinking.md`
- **Fix:** Replace `[[wiki/sources/src_active-vs-lazy-thinking]]` -> `[[src_active-vs-lazy-thinking]]` in each file's frontmatter `sources` field

### Format Validator -- 2026-05-14

**1. Legacy `date_ingested` field in source files** -- WARNING  
-> **APPROVED for Fix Agent**
- 2 source files have `date_ingested` field (removed in format-spec v2.0)
- Affected files:
  - `wiki/sources/src_what-comes-after-systems-thinking.md`
  - `wiki/sources/src_active-vs-lazy-thinking.md`
- **Fix:** Remove the `date_ingested` line from both files (keep `date_compiled`)

### Hygiene Inspector -- 2026-05-17

**1. `memory/` folder at KB root** -- ERROR
-> **REQUIRES JULIUS REVIEW**
- Non-standard folder at knowledge-base/ root level
- Contains Hermes heartbeat polls and session notes (2026-05-15-heartbeat-poll.md, 2026-05-17.md)
- Either remove or add to folder-structure.md root whitelist

**2. `wiki/meta/index-spec.md` not in meta/ whitelist** -- ERROR
-> **REQUIRES JULIUS REVIEW**
- AGENTS.md lists index-spec.md as ground-truth reference alongside format-spec and folder-structure.md
- But folder-structure.md S7 says meta/ contains exactly 2 files
- Either add to S7 whitelist or reconcile the spec conflict

### Hygiene Inspector -- 2026-05-14

[RESOLVED by Julius] -- folder-structure.md updated to v1.1, all folders created

---

## Warnings (Can Fix Later)

### Output Validator -- 2026-05-14

**1. Empty `## Notes` sections in all 12 concept files** -- WARNING
- All concept files have empty Notes section headers
- Either remove or add annotations
- Not urgent -- can wait for Julius review

### Format Validator -- 2026-05-14

**1. Field order disrupted by `date_ingested`** -- WARNING  
-> **FIXED by removing `date_ingested` (see Critical Issues above)**

### Hygiene Inspector -- 2026-05-17

**1-6. Stale .bak/.tmp files in .openclaw/** -- WARNING
-> **SAFE FOR AUTO-CLEANUP by Fix Agent**
- `.openclaw/cron/jobs.json.bak`
- `.openclaw/devices/paired.json.*.tmp`
- `.openclaw/devices/paired.json.bak`
- `.openclaw/devices/pending.json.bak`
- `.openclaw/devices/pending.json.*.tmp`
- `.openclaw/openclaw.json.bak`

**7-18. Legitimate runtime folders not whitelisted** -- WARNING
-> **REQUIRES JULIUS REVIEW (spec update)**
- .openclaw/: canvas, completions, devices, flows -- all legitimate OpenClaw runtime folders
- .openclaw/: TOOLS.md, USER.md -- additional identity files
- .hermes/: bin, cache, logs, memories -- legitimate Hermes runtime folders
- **Recommendation:** Expand S3.1 and S3.2 to allow broader runtime folder categories

### Hygiene Inspector -- 2026-05-14

**1. Non-standard file in skill folder** -- WARNING
- [RESOLVED] -- `validation-criteria.md` now allowed in folder-structure.md S4

---

## Info & Suggestions

### Output Validator -- 2026-05-14

**1. Source summaries at minimum boundary (3 sentences)** -- INFO
- Both source files (`src_what-comes-after-systems-thinking`, `src_active-vs-lazy-thinking`) at exactly 3 sentences

**2. Key points above recommended range** -- INFO
- 3 files (2 sources + 1 concept) have 10-11 items vs 5-10 target

### Hygiene Inspector -- 2026-05-14

**1-4. Expected subfolders not yet created** -- INFO
- `wiki/tag/`, `wiki/topic/`, `wiki/drafts/`, `wiki/reviews/archive/` -- now created as of v1.1

---

## Pending Reports

### 1. Output Validation -- 2026-05-14

**File:** [2026-05-14_output-report.md](2026-05-14_output-report.md)
**Status:** partially approved
**Created:** 2026-05-14 23:00:00
**Issues:** 4 (1 ERROR -> Fix Agent, 1 WARNING, 2 INFO)

**Actions for Fix Agent:**
- Fix wikilink format in 7 concept files (see Critical Issues above)

---

### 2. Format Validation -- 2026-05-14

**File:** [2026-05-14_format-report.md](2026-05-14_format-report.md)
**Status:** partially approved
**Created:** 2026-05-14 23:18:48
**Issues:** 3 (0 ERROR, 2 WARNING -> 1 Fix Agent, 1 INFO)

**Actions for Fix Agent:**
- Remove `date_ingested` field from 2 source files (see Critical Issues above)

---

### 3. Format Validation -- 2026-05-17

**File:** [2026-05-17_format-report.md](2026-05-17_format-report.md)
**Status:** pending
**Created:** 2026-05-17 23:15:00
**Issues:** 5 (0 ERROR, 5 WARNING, 0 INFO)

**Actions for Fix Agent:**
- Fix extra fields and field order in `wiki/sources/src_how-ai-productivity-fails.md`
- Fix extra fields and field order in `wiki/sources/src_how-some-people-become-unrecognizable.md`
- Convert `sub_tags` to bracket syntax in both files
- Fix broken wikilink `[[transposed-organization]]` in `src_how-ai-productivity-fails.md`

[SPEC CONFLICT] pending: `sources` array syntax in concept files -- bracket vs YAML list (see report escalation)

---

### 4. Hygiene Inspection -- 2026-05-14 [RESOLVED]

**File:** [2026-05-14_hygiene-report.md](2026-05-14_hygiene-report.md)
**Status:** resolved
**Created:** 2026-05-14 23:34:24
**Resolution:** folder-structure.md v1.1 + missing folders created
- 14 issues all addressed via spec update

---

### 5. Hygiene Inspection -- 2026-05-17

**File:** [2026-05-17_hygiene-report.md](2026-05-17_hygiene-report.md)
**Status:** pending
**Created:** 2026-05-17 23:35:00
**Issues:** 20 (2 ERROR, 18 WARNING, 0 INFO)

**Key findings:**
- 2 ERROR: `memory/` folder at KB root (non-standard) + `wiki/meta/index-spec.md` not in meta/ whitelist
- 5 WARNING: Stale .bak/.tmp files in .openclaw/ -- safe for auto-cleanup
- 13 WARNING: Legitimate runtime folders/identity files in .openclaw/ and .hermes/ not yet whitelisted in folder-structure.md

[ESCALATION] 10+ WARNINGs are legitimate runtime folders. Recommend expanding agent home whitelists (S3.1 & S3.2) to use broader runtime-folder categories or catch-all clauses.

---

## Recently Applied

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
