# Action Required — Pending Reports

> Consolidated list of pending Hermes validation reports
> Updated automatically after each validation run
> Julius reviews this file to approve/reject fixes

**Last updated:** 2026-05-21 23:30:00

---

## Summary

**Pending reports:** 3

**Status:**
- ⚠️ 3 pending reports require Julius review

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

- ⚠️ 9 stale backup files (.bak) in `.openclaw/` — pending (Hygiene 2026-05-21)

Last resolved: Stale backup/tmp files in .openclaw/ — deleted

---

## Info & Suggestions

*No pending info-level issues.*

---

## Pending Reports

### 1. Output Validation — 2026-05-21

**File:** [2026-05-21_output-report.md](2026-05-21_output-report.md)
**Status:** pending
**Created:** 2026-05-21 23:05:00
**Issues:** 11 (0 ERROR, 6 WARNING, 5 INFO)
**Files affected:** 19 new files (5 sources + 14 concepts)

**Summary:**
- 0 critical quality issues (no ERRORs)
- 6 warnings: empty excerpts section, 3 files with too few key ideas, Vietnamese typo, broken wikilinks
- 5 info: excess key points, 15+ pending concept compilations, empty Notes sections

**Actions:**
- `approve output` — approve this report
- `reject output` — reject this report
- `show output` — show full report details

---

### 2. Format Validation — 2026-05-21

**File:** [2026-05-21_format-report.md](2026-05-21_format-report.md)
**Status:** pending
**Created:** 2026-05-21 23:15:00
**Issues:** 20 (3 ERROR, 17 WARNING, 0 INFO)
**Files affected:** 95 checked (78 concepts + 17 sources)

**Summary:**
- 3 ERRORs: 2 invalid sub_tag (`economic` is Pool A, not Pool B), 1 code block missing language tag
- 17 WARNINGs: 9 section case mismatches (`Key Ideas`→`Key ideas`, `Related Concepts`→`Related concepts`), 7 wikilink-wrapped `original` field, 1 deprecated `date_ingested`
- Systemic: 4 concepts share identical section case issues (same compile run); 7 sources use wikilink in `original`; 9 sources retain deprecated `date_ingested`

**Actions:**
- `approve format` — approve this report
- `reject format` — reject this report
- `show format` — show full report details

---

### 3. Hygiene Inspection — 2026-05-21

**File:** [2026-05-21_hygiene-report.md](2026-05-21_hygiene-report.md)
**Status:** pending
**Created:** 2026-05-21 23:30:00
**Issues:** 9 (0 ERROR, 9 WARNING, 0 INFO)
**Paths checked:** 5755 (966 folders + 4789 files)

**Summary:**
- 0 structural violations — all paths comply with folder-structure.md v1.2
- 9 WARNINGs: stale backup files (.bak) in `.openclaw/` agent runtime
- No issues in `raw/`, `wiki/`, or `context/` layers
- Overall: clean bill of health

**Actions:**
- `approve hygiene` — approve this report
- `reject hygiene` — reject this report
- `show hygiene` — show full report details

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
