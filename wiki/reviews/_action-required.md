# Action Required — Pending Reports

> Consolidated list of pending Hermes validation reports
> Updated automatically after each validation run
> Julius reviews this file to approve/reject fixes

**Last updated:** 2026-05-22 23:33:52

---

## Summary

**Pending reports:** 3

**Status:**
- ⚠️ Output Validator — 2026-05-22: 16 issues (8 WARNING, 8 INFO) — awaiting review
- ℹ️ Format Validator — 2026-05-22: 11 issues (0 ERROR, 11 WARNING, 0 INFO) — awaiting review
- 🔴 Hygiene Inspector — 2026-05-22: 5 issues (3 ERROR, 1 WARNING, 1 INFO) — awaiting review

**Resolved reports:**
- [x] Output Validator — 2026-05-14 (4 issues: wikilink + warnings + info)
- [x] Format Validator — 2026-05-14 (3 issues: date_ingested removal + warnings)
- [x] Format Validator — 2026-05-17 (5 issues: extra fields, bracket syntax, broken wikilink)
- [x] Hygiene Inspector — 2026-05-14 (14 issues: folder-structure.md v1.1 + missing folders)
- [x] Hygiene Inspector — 2026-05-17 (20 issues: memory/ folder, stale files, runtime whitelist)
- [x] Hygiene Inspector — 2026-05-20 (6 issues: EOF, memory/, state/, stale backups)
- [x] Output Validator — 2026-05-21 (11 issues: empty sections, key ideas, typo, broken wikilinks)
- [x] Format Validator — 2026-05-21 (20 issues: section case, original wikilink, date_ingested — Compile Agent fixed)
- [x] Hygiene Inspector — 2026-05-21 (9 issues: stale backup files)

---

## Critical Issues (Fix Immediately)

- **Hygiene 2026-05-22:** 3 ERROR — `memory/` stale dir at root, `RAW_BACKLOG.md` at root (not in whitelist), `wiki/reviews/HEARTBEAT.md` in wrong location

---

## Warnings (Can Fix Later)

- Output Validator 2026-05-22: 8 WARNING issues — see report for details
- Format Validator 2026-05-22: 11 WARNING (extra sections, YAML syntax, legacy fields, field order)
- Hygiene Inspector 2026-05-22: 1 WARNING — `.gitkeep` naming in `wiki/topic/`

---

## Info & Suggestions

- Output Validator 2026-05-22: 8 INFO issues — see report for details
- Hygiene Inspector 2026-05-22: 1 INFO — `raw/raw.md` spec gap (missing from folder-structure.md Section 6)

---

## Pending Reports

- [ ] **Output Validator — 2026-05-22** (16 issues: 8 WARNING + 8 INFO)
  - WARNING: Empty Original excerpts (persistent), key points overflow × 6 files, missing trailing newlines × 3
  - INFO: 17 broken wikilinks, 49 empty Notes, format inconsistencies
  - Report: wiki/reviews/2026-05-22_output-report.md

- [ ] **Format Validator — 2026-05-22** (11 issues: 0 ERROR + 11 WARNING)
  - WARNING: Extra sections between required sections × 3, YAML list syntax × 3, legacy fields × 2, field order × 2
  - Report: wiki/reviews/2026-05-22_format-report.md

- [ ] **Hygiene Inspector — 2026-05-22** (5 issues: 3 ERROR + 1 WARNING + 1 INFO)
  - ERROR: Stale `memory/` at root, `RAW_BACKLOG.md` at root (not whitelisted), `wiki/reviews/HEARTBEAT.md` misplaced
  - WARNING: `.gitkeep` in `wiki/topic/` naming convention
  - INFO: `raw/raw.md` spec gap (missing from folder-structure.md Section 6)
  - Report: wiki/reviews/2026-05-22_hygiene-report.md

---

## Recently Applied

- [x] Output Validator — 2026-05-21 (approved 2026-05-22: empty sections, key ideas gaps, Vietnamese typo → Kara fix)
- [x] Format Validator — 2026-05-21 (approved 2026-05-22: section case / original wikilink / date_ingested — Compile Agent template fixed)
- [x] Hygiene Inspector — 2026-05-21 (approved 2026-05-22: stale backup files cleaned up)

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
