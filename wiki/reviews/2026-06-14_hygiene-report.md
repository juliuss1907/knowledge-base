# Hygiene Inspection — 2026-06-14

**Status:** pending
**Issues found:** 16
**Created:** 2026-06-14 23:30:00
**Validator:** hygiene-inspector

**Paths checked:** 26

---

## Issue 1: File not in root whitelist

**Path:** `MEMORY.md`
**Severity:** ERROR
**Category:** Path
**Issue:** File not in root whitelist
**Current:** `MEMORY.md` exists at root level
**Expected:** Root whitelist allows only: AGENTS.md, TAGS.md, README.md, knowledge-base.md, HEARTBEAT.md, IDENTITY.md, SOUL.md, TOOLS.md, USER.md, .gitignore
**Suggested fix:** Remove or move to `.hermes/` or `.openclaw/`

---

## Issue 2: Folder not in root whitelist

**Path:** `temp_content/`
**Severity:** ERROR
**Category:** Path
**Issue:** Folder not in root whitelist
**Current:** `temp_content/` exists at root level
**Expected:** Allowed root folders: .git, .obsidian, .openclaw, .hermes, context, raw, wiki, scripts
**Suggested fix:** Remove or update folder-structure.md

---

## Issue 3: File not in root whitelist

**Path:** `RAW_BACKLOG.md`
**Severity:** ERROR
**Category:** Path
**Issue:** File not in root whitelist
**Current:** `RAW_BACKLOG.md` exists at root level
**Expected:** Root whitelist allows only 4 required files + 5 allowed symlinks + .gitignore
**Suggested fix:** Move to `wiki/drafts/` or `raw/` and remove from root

---

## Issue 4: Folder not in root whitelist

**Path:** `search/`
**Severity:** ERROR
**Category:** Path
**Issue:** Folder not in root whitelist
**Current:** `search/` exists at root level
**Expected:** Allowed root folders: .git, .obsidian, .openclaw, .hermes, context, raw, wiki, scripts
**Suggested fix:** Remove or update folder-structure.md

---

## Issue 5: Folder not in root whitelist

**Path:** `memory/`
**Severity:** ERROR
**Category:** Path
**Issue:** Folder not in root whitelist
**Current:** `memory/` exists at root level
**Expected:** Allowed root folders: .git, .obsidian, .openclaw, .hermes, context, raw, wiki, scripts
**Suggested fix:** Remove (migrated to `.openclaw/memory/` per folder-structure.md v1.2)

---

## Issue 6: Folder not in root whitelist

**Path:** `state/`
**Severity:** ERROR
**Category:** Path
**Issue:** Folder not in root whitelist
**Current:** `state/` exists at root level
**Expected:** Allowed root folders: .git, .obsidian, .openclaw, .hermes, context, raw, wiki, scripts
**Suggested fix:** Remove or update folder-structure.md

---

## Issue 7: Hidden file not allowed at raw/ root

**Path:** `raw/.last_heartbeat`
**Severity:** ERROR
**Category:** Path
**Issue:** Hidden file not allowed at raw/ root
**Current:** `raw/.last_heartbeat` exists
**Expected:** Only `raw.md` allowed at `raw/` root level
**Suggested fix:** Remove

---

## Issue 8: File not allowed in wiki/reviews/

**Path:** `wiki/reviews/HEARTBEAT.md`
**Severity:** ERROR
**Category:** Path
**Issue:** File not allowed in wiki/reviews/
**Current:** `HEARTBEAT.md` exists in `wiki/reviews/`
**Expected:** `wiki/reviews/` allows only `_action-required.md`, `YYYY-MM-DD_<type>-report.md`, and `archive/`
**Suggested fix:** Remove (should be in `.hermes/` or root)

---

## Issue 9: Review file naming convention violated

**Path:** `wiki/reviews/hygiene-report-2026-05-30.md`
**Severity:** WARNING
**Category:** Naming
**Issue:** Review file naming convention violated
**Current:** `hygiene-report-2026-05-30.md`
**Expected:** `YYYY-MM-DD_<type>-report.md`
**Suggested fix:** Rename to `2026-05-30_hygiene-report.md` or archive

---

## Issue 10: Review file naming convention violated

**Path:** `wiki/reviews/hygiene-report-2026-06-14.md`
**Severity:** WARNING
**Category:** Naming
**Issue:** Review file naming convention violated
**Current:** `hygiene-report-2026-06-14.md`
**Expected:** `YYYY-MM-DD_<type>-report.md`
**Suggested fix:** Rename to `2026-06-14_hygiene-report.md` or archive

---

## Issue 11: Review file naming convention violated

**Path:** `wiki/reviews/output-report-2026-06-14.md`
**Severity:** WARNING
**Category:** Naming
**Issue:** Review file naming convention violated
**Current:** `output-report-2026-06-14.md`
**Expected:** `YYYY-MM-DD_<type>-report.md`
**Suggested fix:** Rename to `2026-06-14_output-report.md` or archive

---

## Issue 12: Review file naming convention violated

**Path:** `wiki/reviews/2026-05-28_validation-check.md`
**Severity:** WARNING
**Category:** Naming
**Issue:** Review file naming convention violated
**Current:** `2026-05-28_validation-check.md`
**Expected:** `YYYY-MM-DD_<type>-report.md`
**Suggested fix:** Rename to `2026-05-28_output-report.md` or archive

---

## Issue 13: Review file naming convention violated

**Path:** `wiki/reviews/format-report-2026-05-30.md`
**Severity:** WARNING
**Category:** Naming
**Issue:** Review file naming convention violated
**Current:** `format-report-2026-05-30.md`
**Expected:** `YYYY-MM-DD_<type>-report.md`
**Suggested fix:** Rename to `2026-05-30_format-report.md` or archive

---

## Issue 14: Review file naming convention violated

**Path:** `wiki/reviews/output-report-2026-05-30.md`
**Severity:** WARNING
**Category:** Naming
**Issue:** Review file naming convention violated
**Current:** `output-report-2026-05-30.md`
**Expected:** `YYYY-MM-DD_<type>-report.md`
**Suggested fix:** Rename to `2026-05-30_output-report.md` or archive

---

## Issue 15: Review file naming convention violated

**Path:** `wiki/reviews/format-report-2026-06-14.md`
**Severity:** WARNING
**Category:** Naming
**Issue:** Review file naming convention violated
**Current:** `format-report-2026-06-14.md`
**Expected:** `YYYY-MM-DD_<type>-report.md`
**Suggested fix:** Rename to `2026-06-14_format-report.md` or archive

---

## Issue 16: Draft file naming convention violated

**Path:** `wiki/drafts/analysis_2026-advice.md`
**Severity:** WARNING
**Category:** Naming
**Issue:** Draft file naming convention violated
**Current:** `analysis_2026-advice.md` (contains underscore)
**Expected:** `<slug>.md` — lowercase, hyphens only
**Suggested fix:** Rename to `analysis-2026-advice.md`

---

## Issue 17: File directly in archive/

**Path:** `wiki/reviews/archive/.gitkeep`
**Severity:** INFO
**Category:** Orphan
**Issue:** File directly in archive/ root
**Current:** `.gitkeep` exists in `wiki/reviews/archive/`
**Expected:** `archive/` should contain only `YYYY-MM/` subfolders
**Suggested fix:** Remove `.gitkeep` (archive folder is non-empty due to subfolders)

---

## Summary

| Severity | Count |
|---|---|
| ERROR | 8 |
| WARNING | 8 |
| INFO | 1 |

**Top violations:**
- Root whitelist violations: 6 (folders/files not allowed at root)
- Review naming convention: 7 files with wrong naming pattern
- Draft naming convention: 1 file with underscore

**Systemic note:**
`wiki/reviews/` contains multiple historical reports with non-standard naming (`<type>-report-YYYY-MM-DD.md` and `YYYY-MM-DD_validation-check.md`). Recommend standardizing all review filenames to `YYYY-MM-DD_<type>-report.md`.

---

*Report generated by Hygiene Inspector — Knowledge Base V2*
