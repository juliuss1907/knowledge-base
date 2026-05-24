# Action Required — Pending Reports

> Consolidated list of pending Hermes validation reports
> Updated automatically after each validation run
> Julius reviews this file to approve/reject fixes

**Last updated:** 2026-05-24 13:35 — All 2026-05-22 reports approved

---

## Summary

**Pending reports:** 0

**Status:**
- ✅ Output Validator — 2026-05-24: approved
- ✅ Format Validator — 2026-05-24: approved
- ✅ Hygiene Inspector — 2026-05-24: approved
- ✅ Output Validator — 2026-05-22: approved
- ✅ Format Validator — 2026-05-22: approved
- ✅ Hygiene Inspector — 2026-05-22: approved

**Resolved reports:**
- [x] Output Validator — 2026-05-14 (4 issues)
- [x] Format Validator — 2026-05-14 (3 issues)
- [x] Format Validator — 2026-05-17 (5 issues)
- [x] Hygiene Inspector — 2026-05-14 (14 issues)
- [x] Hygiene Inspector — 2026-05-17 (20 issues)
- [x] Hygiene Inspector — 2026-05-20 (6 issues)
- [x] Output Validator — 2026-05-21 (11 issues)
- [x] Format Validator — 2026-05-21 (20 issues)
- [x] Hygiene Inspector — 2026-05-21 (9 issues)
- [x] Hygiene Inspector — 2026-05-22 (3 ERROR + 2 issues)
- [x] Format Validator — 2026-05-22 (11 WARNING)
- [x] Output Validator — 2026-05-22 (16 issues)
- [x] Format Validator — 2026-05-24 (2 ERROR resolved + 3 WARNING)
- [x] Hygiene Inspector — 2026-05-24 (1 ERROR + 1 INFO)
- [x] Output Validator — 2026-05-24 (all 20 issues)

---

## Critical Issues (Fix Immediately)

- **Output 2026-05-24:** 1 ERROR (11 broken wikilinks) → systematic, requires Compile Agent re-run
- **Output 2026-05-24:** Systematic issues → requires Compile Agent template fix

---

## Warnings (Can Fix Later)

- Hygiene 2026-05-22: 1 WARNING — `.gitkeep` naming in `wiki/topic/`
- Hygiene 2026-05-22: 1 INFO — `raw/raw.md` spec gap

---

## Pending Reports

*None — all reports approved*

---

## Recently Applied

- [x] Hygiene Inspector — 2026-05-22: memory/ → .openclaw/memory/, RAW_BACKLOG.md deleted, wiki/reviews/HEARTBEAT.md removed
- [x] Format Validator — 2026-05-22: extra sections ×3, YAML syntax ×3, legacy fields ×2, field order ×2
- [x] Output Validator — 2026-05-22: Empty Original excerpts, Empty Notes systematic, Too many key points ×6, Broken wikilinks ×17

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