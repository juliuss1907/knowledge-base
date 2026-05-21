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

### 1. Hygiene Inspection -- 2026-05-20

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

- [x] Output Validator — 2026-05-14 (wikilink fix — marked resolved 2026-05-21)
- [x] Format Validator — 2026-05-14 (date_ingested removal — marked resolved 2026-05-21)
- [x] Format Validator — 2026-05-17 (extra fields, bracket syntax, broken wikilink — marked resolved 2026-05-21)
- [x] Hygiene Inspector — 2026-05-14 (folder-structure.md v1.1 + missing folders — marked resolved 2026-05-21)
- [x] Hygiene Inspector — 2026-05-17 (memory/ folder, stale files, runtime whitelist — marked resolved 2026-05-21)

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
