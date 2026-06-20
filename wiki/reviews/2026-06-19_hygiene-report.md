# Hygiene Inspection — 2026-06-19

**Status:** pending
**Issues found:** 4
**Created:** 2026-06-19 23:30:00
**Validator:** hygiene-inspector

**Paths checked:** 27

---

## Summary

| Severity | Count |
|---|---|
| ERROR | 0 |
| WARNING | 4 |
| INFO | 0 |
| **Total** | **4** |

All 4 issues are archived -v2 duplicate reports in `wiki/reviews/archive/2026-06/`. No ERROR-level violations. No root-level orphans. No naming convention violations in active paths.

---

## Issue 1: Archived report with -v2 suffix

**Path:** wiki/reviews/archive/2026-06/2026-06-01_output-report-v2.md
**Severity:** WARNING
**Category:** Naming
**Issue:** Archived report has -v2 suffix (duplicate)
**Current:** `2026-06-01_output-report-v2.md`
**Expected:** `2026-06-01_output-report.md` (merge into canonical)
**Suggested fix:** Merge into canonical name or remove

---

## Issue 2: Archived report with -v2 suffix

**Path:** wiki/reviews/archive/2026-06/2026-06-03_output-report-v2.md
**Severity:** WARNING
**Category:** Naming
**Issue:** Archived report has -v2 suffix (duplicate)
**Current:** `2026-06-03_output-report-v2.md`
**Expected:** `2026-06-03_output-report.md` (merge into canonical)
**Suggested fix:** Merge into canonical name or remove

---

## Issue 3: Archived report with -v2 suffix

**Path:** wiki/reviews/archive/2026-06/2026-06-01_format-report-v2.md
**Severity:** WARNING
**Category:** Naming
**Issue:** Archived report has -v2 suffix (duplicate)
**Current:** `2026-06-01_format-report-v2.md`
**Expected:** `2026-06-01_format-report.md` (merge into canonical)
**Suggested fix:** Merge into canonical name or remove

---

## Issue 4: Archived report with -v2 suffix

**Path:** wiki/reviews/archive/2026-06/2026-06-01_hygiene-report-v2.md
**Severity:** WARNING
**Category:** Naming
**Issue:** Archived report has -v2 suffix (duplicate)
**Current:** `2026-06-01_hygiene-report-v2.md`
**Expected:** `2026-06-01_hygiene-report.md` (merge into canonical)
**Suggested fix:** Merge into canonical name or remove

---

## Notes

- **No ERROR-level issues** — root structure is clean, all whitelisted paths compliant.
- **No active naming violations** — all reports in `wiki/reviews/` follow canonical `YYYY-MM-DD_<type>-report.md` format.
- **No orphan detection hits** — no files in wrong locations, no empty folders flagged, no heartbeat artifacts leaked.
- **4 archived -v2 duplicates** — same pattern as previous hygiene reports (2026-06-17, 2026-06-18). These are low-priority and can be cleaned up during the next archive maintenance pass.

---

**End of report.**
