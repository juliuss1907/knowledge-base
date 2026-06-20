# Hygiene Inspection — 2026-06-15

**Status:** pending
**Issues found:** 6
**Created:** 2026-06-15 23:30:00
**Validator:** hygiene-inspector

**Paths checked:** 30

---

## Issue 1: Folder not in root whitelist

**Path:** `state/`
**Severity:** ERROR
**Category:** Path
**Issue:** Folder not in root whitelist
**Current:** `state`
**Expected:** One of allowed root folders
**Suggested fix:** Remove or update folder-structure.md

---

## Issue 2: File not allowed in wiki/reviews/

**Path:** `wiki/reviews/HEARTBEAT.md`
**Severity:** ERROR
**Category:** Path
**Issue:** File not allowed in wiki/reviews/
**Current:** `HEARTBEAT.md`
**Expected:** `_action-required.md`, reports, `archive/`
**Suggested fix:** Remove (should be in `.hermes/` or root)

---

## Issue 3: Archived report naming convention violated

**Path:** `wiki/reviews/archive/2026-05/2026-05-28_validation-check.md`
**Severity:** WARNING
**Category:** Naming
**Issue:** Archived report naming convention violated
**Current:** `2026-05-28_validation-check.md`
**Expected:** `YYYY-MM-DD_<type>-report.md`
**Suggested fix:** Rename

---

## Issue 4: Draft file naming convention violated

**Path:** `wiki/drafts/RAW_BACKLOG-backup-2026-06-15.md`
**Severity:** WARNING
**Category:** Naming
**Issue:** Draft file naming convention violated
**Current:** `RAW_BACKLOG-backup-2026-06-15.md`
**Expected:** `<slug>.md` (lowercase, hyphens)
**Suggested fix:** Rename

---

## Issue 5: Draft file naming convention violated

**Path:** `wiki/drafts/MEMORY-backup-2026-06-15.md`
**Severity:** WARNING
**Category:** Naming
**Issue:** Draft file naming convention violated
**Current:** `MEMORY-backup-2026-06-15.md`
**Expected:** `<slug>.md` (lowercase, hyphens)
**Suggested fix:** Rename

---

## Issue 6: Draft file naming convention violated

**Path:** `wiki/drafts/temp_content-backup-2026-06-15.md`
**Severity:** WARNING
**Category:** Naming
**Issue:** Draft file naming convention violated
**Current:** `temp_content-backup-2026-06-15.md`
**Expected:** `<slug>.md` (lowercase, hyphens)
**Suggested fix:** Rename

---

## Summary

| Severity | Count |
|---|---|
| ERROR | 2 |
| WARNING | 4 |
| INFO | 0 |

**Top violations:**
- 2 root-level structural issues (orphan folder, misplaced file)
- 4 naming convention violations (1 archived report, 3 draft backups)

**Systemic note:** None — all issues are individual and actionable.

**Verdict:** Fix recommended. 2 ERRORs should be corrected. 4 WARNINGs are naming cleanups.


---
**Status:** applied
**Applied at:** 2026-06-16 08:21
**Applied by:** fix-agent

