# Hygiene Inspection — 2026-06-17

**Status:** approved
**Approved by:** Julius
**Issues found:** 7 (2 ERROR, 5 WARNING, 0 INFO)
**Created:** 2026-06-17 23:30:00
**Validator:** hygiene-inspector (Hermes)

**Paths checked:** 27

---

## Summary

| Severity | Count | Category |
|---|---|---|
| ERROR | 2 | Root whitelist violation ×1, Heartbeat artifact ×1 |
| WARNING | 5 | Naming convention ×5 (4 v2 duplicates + 1 non-standard archive) |
| INFO | 0 | — |

**Trend:** 7 issues this run (+1 from 2026-06-15). Two are recurring: `RAW_BACKLOG.md` (regression from 06-14 fix) and `wiki/reviews/HEARTBEAT.md` (regression from 06-15 fix). Four are `-v2` duplicate reports that should be merged into canonical names or archived.

---

## Issue 1: Root-level orphan — RAW_BACKLOG.md

**Path:** `RAW_BACKLOG.md`
**Severity:** ERROR
**Category:** Path
**Issue:** File not in root whitelist
**Current:** `RAW_BACKLOG.md` exists at knowledge base root
**Expected:** Root whitelist allows only: `AGENTS.md`, `TAGS.md`, `README.md`, `knowledge-base.md`, `HEARTBEAT.md` (symlink), `IDENTITY.md` (symlink), `SOUL.md` (symlink), `TOOLS.md` (symlink), `USER.md` (symlink), `.gitignore`
**Suggested fix:** Move content to `wiki/drafts/` or `raw/articles/`, then delete from root. This file was previously flagged on 2026-06-14 and appears to have regressed.

---

## Issue 2: Heartbeat artifact in wiki/reviews/

**Path:** `wiki/reviews/HEARTBEAT.md`
**Severity:** ERROR
**Category:** Path
**Issue:** Heartbeat artifact leaked outside agent home
**Current:** `wiki/reviews/HEARTBEAT.md` exists
**Expected:** HEARTBEAT.md should be in `.hermes/` or at root (as symlink), never in `wiki/reviews/`
**Suggested fix:** Remove `wiki/reviews/HEARTBEAT.md`. This was previously fixed on 2026-06-16 (from 06-15 report) but has reappeared.

---

## Issue 3: Duplicate output report with -v2 suffix

**Path:** `wiki/reviews/2026-06-01_output-report-v2.md`
**Severity:** WARNING
**Category:** Naming
**Issue:** Review file naming convention violated — `-v2` suffix not in canonical format
**Current:** `2026-06-01_output-report-v2.md`
**Expected:** `2026-06-01_output-report.md` (merge v2 into canonical, then remove v2)
**Suggested fix:** Merge content into `2026-06-01_output-report.md` or archive the v2 variant

---

## Issue 4: Duplicate output report with -v2 suffix

**Path:** `wiki/reviews/2026-06-03_output-report-v2.md`
**Severity:** WARNING
**Category:** Naming
**Issue:** Review file naming convention violated — `-v2` suffix not in canonical format
**Current:** `2026-06-03_output-report-v2.md`
**Expected:** `2026-06-03_output-report.md` (merge v2 into canonical, then remove v2)
**Suggested fix:** Merge content into `2026-06-03_output-report.md` or archive the v2 variant

---

## Issue 5: Duplicate format report with -v2 suffix

**Path:** `wiki/reviews/2026-06-01_format-report-v2.md`
**Severity:** WARNING
**Category:** Naming
**Issue:** Review file naming convention violated — `-v2` suffix not in canonical format
**Current:** `2026-06-01_format-report-v2.md`
**Expected:** `2026-06-01_format-report.md` (merge v2 into canonical, then remove v2)
**Suggested fix:** Merge content into `2026-06-01_format-report.md` or archive the v2 variant

---

## Issue 6: Duplicate hygiene report with -v2 suffix

**Path:** `wiki/reviews/2026-06-01_hygiene-report-v2.md`
**Severity:** WARNING
**Category:** Naming
**Issue:** Review file naming convention violated — `-v2` suffix not in canonical format
**Current:** `2026-06-01_hygiene-report-v2.md`
**Expected:** `2026-06-01_hygiene-report.md` (merge v2 into canonical, then remove v2)
**Suggested fix:** Merge content into `2026-06-01_hygiene-report.md` or archive the v2 variant

---

## Issue 7: Non-standard report type in archive

**Path:** `wiki/reviews/archive/2026-06/2026-06-15_spot-check-report.md`
**Severity:** WARNING
**Category:** Naming
**Issue:** Archived report uses unrecognized type `spot-check` — only `format`, `output`, `hygiene` are canonical
**Current:** `2026-06-15_spot-check-report.md`
**Expected:** `spot-check` → should use canonical type or be renamed. If this is a legitimate new report type, `folder-structure.md` should be updated.
**Suggested fix:** Either rename to a canonical type (if content fits) or propose addition to `folder-structure.md` whitelist

---

## Notes

- **Recurring issues:** RAW_BACKLOG.md (regression from 06-14 fix) and HEARTBEAT.md (regression from 06-15 fix). These suggest an agent or process is recreating these files after cleanup.
- **v2 duplicates:** Four `-v2` reports from early June sit alongside their canonical counterparts. Recommend one-time merge + archive pass.
- **Overall structural health:** Core folder structure is compliant. No new unknown folders. No naming violations in `raw/`, `concepts/`, `sources/`, `tag/`, `topic/`, or `drafts/`.

---

**Commands:**
- `approve hygiene` — approve this report
- `reject hygiene` — reject this report
- `show hygiene` — show full report details
