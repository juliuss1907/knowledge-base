# Action Required — Pending Reports

> Consolidated list of pending Hermes validation reports
> Updated automatically after each validation run
> Julius reviews this file to approve/reject fixes

**Last updated:** 2026-05-21 09:30:00

---

## Summary

**Pending reports:** 1

**Status:**
- Hygiene Inspector: 1 pending report (2026-05-20: 6 issues — 3 ERROR, 3 WARNING)

**Resolved reports (pre-2026-05-20):**
- [x] Output Validator — 2026-05-14 (4 issues: wikilink + warnings + info)
- [x] Format Validator — 2026-05-14 (3 issues: date_ingested removal + warnings)
- [x] Format Validator — 2026-05-17 (5 issues: extra fields, bracket syntax, broken wikilink)
- [x] Hygiene Inspector — 2026-05-14 (14 issues: folder-structure.md v1.1 + missing folders)
- [x] Hygiene Inspector — 2026-05-17 (20 issues: memory/ folder, stale files, runtime whitelist)

---

## Critical Issues (Fix Immediately)

### Hygiene Inspector -- 2026-05-20

**1. `EOF` file at KB root** -- ERROR  
-> **REQUIRES JULIUS REVIEW**
- Zero-byte file named `EOF` at knowledge-base/ root (created 2026-05-19)
- Likely a terminal redirect artifact (`> EOF` instead of `> file`)
- Either remove or add to .gitignore

**2. `memory/` folder at KB root** -- ERROR  
-> **REQUIRES JULIUS REVIEW**
- Non-standard folder at knowledge-base/ root level
- Contains Hermes heartbeat polls and session notes (2026-05-19.md, 2026-05-20.md, .dreams/)
- Content should be merged into `.openclaw/memory/` per AGENTS.md S4.1
- Either remove or add to folder-structure.md root whitelist

**3. `state/` empty directory at KB root** -- ERROR  
-> **REQUIRES JULIUS REVIEW**
- Empty directory at knowledge-base/ root (no files)
- Purpose unclear; safe to remove

---

## Warnings (Can Fix Later)

### Hygiene Inspector -- 2026-05-20

**1-3. Stale backup/tmp files in .openclaw/** -- WARNING  
-> **SAFE FOR AUTO-CLEANUP by Fix Agent**
- `.openclaw/cron/jobs.json.bak` — backup of cron config
- `.openclaw/devices/pending.json.*.tmp` — leftover temp file
- `.openclaw/openclaw.json.bak.3` — old backup chain (keep .bak.1 only)
- **Fix:** Delete all three files

---

## Info & Suggestions

*No pending info-level issues.*

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

### 6. Hygiene Inspection -- 2026-05-20 (NEW)

**File:** [2026-05-20_hygiene-report.md](2026-05-20_hygiene-report.md)
**Status:** pending
**Created:** 2026-05-20 23:30:00
**Issues:** 6 (3 ERROR, 3 WARNING, 0 INFO)

**Key findings:**
- 3 ERROR: `EOF` file, `memory/` dir, `state/` dir at KB root — all root-level anomalies
- 3 WARNING: Stale backup/tmp files in .openclaw/ — safe for auto-cleanup

**Overall assessment:** KB structure is clean. After folder-structure.md v1.2 with catch-all clauses, noise from runtime folders eliminated. Remaining issues are genuine hygiene concerns.

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

**To apply approved fixes:**
openclaw fix apply
