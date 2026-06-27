# Hygiene Inspection — 2026-05-21

**Status:** pending
**Issues found:** 9
**Created:** 2026-05-21 23:30:00
**Validator:** hygiene-inspector

**Paths checked:** 5755 (966 folders + 4789 files)

---

## Summary

| Severity | Count |
|---|---|
| ERROR | 0 |
| WARNING | 9 |
| INFO | 0 |

All issues are old backup files (`.bak`) in `.openclaw/` — agent runtime artifacts, not knowledge base content. No structural violations detected in `raw/`, `wiki/`, or `context/` layers.

---

## Issue 1: Backup file in agent home

**Path:** .openclaw/cron/jobs.json.bak.20260422
**Severity:** WARNING
**Category:** Orphan
**Issue:** Backup file in agent home
**Current:** .openclaw/cron/jobs.json.bak.20260422
**Expected:** Clean up old backups
**Suggested fix:** Delete or archive old backup

---

## Issue 2: Backup file in agent home

**Path:** .openclaw/cron/jobs.json.bak.fix2
**Severity:** WARNING
**Category:** Orphan
**Issue:** Backup file in agent home
**Current:** .openclaw/cron/jobs.json.bak.fix2
**Expected:** Clean up old backups
**Suggested fix:** Delete or archive old backup

---

## Issue 3: Backup file in agent home

**Path:** .openclaw/cron/jobs.json.bak.format
**Severity:** WARNING
**Category:** Orphan
**Issue:** Backup file in agent home
**Current:** .openclaw/cron/jobs.json.bak.format
**Expected:** Clean up old backups
**Suggested fix:** Delete or archive old backup

---

## Issue 4: Backup file in agent home

**Path:** .openclaw/cron/jobs.json.bak.market
**Severity:** WARNING
**Category:** Orphan
**Issue:** Backup file in agent home
**Current:** .openclaw/cron/jobs.json.bak.market
**Expected:** Clean up old backups
**Suggested fix:** Delete or archive old backup

---

## Issue 5: Backup file in agent home

**Path:** .openclaw/cron/jobs.json.bak.market2
**Severity:** WARNING
**Category:** Orphan
**Issue:** Backup file in agent home
**Current:** .openclaw/cron/jobs.json.bak.market2
**Expected:** Clean up old backups
**Suggested fix:** Delete or archive old backup

---

## Issue 6: Backup file in agent home

**Path:** .openclaw/openclaw.json.bak.1
**Severity:** WARNING
**Category:** Orphan
**Issue:** Backup file in agent home
**Current:** .openclaw/openclaw.json.bak.1
**Expected:** Clean up old backups
**Suggested fix:** Delete or archive old backup

---

## Issue 7: Backup file in agent home

**Path:** .openclaw/openclaw.json.bak.2
**Severity:** WARNING
**Category:** Orphan
**Issue:** Backup file in agent home
**Current:** .openclaw/openclaw.json.bak.2
**Expected:** Clean up old backups
**Suggested fix:** Delete or archive old backup

---

## Issue 8: Backup file in agent home

**Path:** .openclaw/openclaw.json.bak.4
**Severity:** WARNING
**Category:** Orphan
**Issue:** Backup file in agent home
**Current:** .openclaw/openclaw.json.bak.4
**Expected:** Clean up old backups
**Suggested fix:** Delete or archive old backup

---

## Issue 9: Backup file in agent home

**Path:** .openclaw/openclaw.json.bak_2026-04-20
**Severity:** WARNING
**Category:** Orphan
**Issue:** Backup file in agent home
**Current:** .openclaw/openclaw.json.bak_2026-04-20
**Expected:** Clean up old backups
**Suggested fix:** Delete or archive old backup

---

## Validation Notes

- **Path whitelist:** ✅ All root-level, depth-1, and depth-2+ paths comply with folder-structure.md v1.2
- **Naming conventions:** ✅ All wiki/sources/ files use `src_` prefix; all wiki/concepts/ files use lowercase-hyphen slugs; raw/ content follows `YYYY-MM-DD_<slug>.md` convention
- **No orphaned content files:** No source files in concepts/, no concept files in sources/
- **No forbidden paths:** No files at wiki/ or raw/ root outside whitelist
- **Folder structure drift:** None detected — all folders match whitelist

**Overall:** Clean bill of health. Only minor agent-runtime backup files flagged (9 WARNINGs, agent-owned `.openclaw/`). No knowledge base structural issues.
