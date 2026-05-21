# Action Required — Pending Reports

> Consolidated list of pending Hermes validation reports
> Updated automatically after each validation run
> Julius reviews this file to approve/reject fixes

**Last updated:** 2026-05-21 10:00:00

---

## Summary

**Pending reports:** 0

**Status:**
- ✅ All reports resolved — KB clean.

**Resolved reports:**
- [x] Output Validator — 2026-05-14 (4 issues: wikilink + warnings + info)
- [x] Format Validator — 2026-05-14 (3 issues: date_ingested removal + warnings)
- [x] Format Validator — 2026-05-17 (5 issues: extra fields, bracket syntax, broken wikilink)
- [x] Hygiene Inspector — 2026-05-14 (14 issues: folder-structure.md v1.1 + missing folders)
- [x] Hygiene Inspector — 2026-05-17 (20 issues: memory/ folder, stale files, runtime whitelist)
- [x] Hygiene Inspector — 2026-05-20 (6 issues: EOF, memory/, state/, stale backups)

---

## Critical Issues (Fix Immediately)

*No critical issues — all resolved by Julius 2026-05-21.*

Last resolved: Hygiene 2026-05-20 (EOF, memory/, state/ — moved/removed)

---

## Warnings (Can Fix Later)

*No warnings — all resolved by Julius 2026-05-21.*

Last resolved: Stale backup/tmp files in .openclaw/ — deleted

---

## Info & Suggestions

*No pending info-level issues.*

---

## Pending Reports

*No pending reports — all resolved by Julius 2026-05-21.*

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
