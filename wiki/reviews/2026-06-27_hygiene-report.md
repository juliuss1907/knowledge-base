# Hygiene Inspection — 2026-06-27

**Status:** approved
**Approved by:** Julius — 2026-06-29
**Issues found:** 1
**Created:** 2026-06-27 23:30:12 +07
**Validator:** hygiene-inspector

**Paths checked:** 17,526

---

## Issue 1: HEARTBEAT.md leaked outside agent home

**Path:** `wiki/reviews/HEARTBEAT.md`
**Severity:** ERROR
**Category:** Orphan
**Issue:** HEARTBEAT.md artifact leaked outside agent home
**Current:** `wiki/reviews/HEARTBEAT.md` exists in Hermes review output zone
**Expected:** HEARTBEAT.md belongs inside `.openclaw/` or `.hermes/` agent homes only. `wiki/reviews/` is for Hermes validation reports (`_action-required.md`, `YYYY-MM-DD_<type>-report.md`) and archives.
**Suggested fix:** Delete `wiki/reviews/HEARTBEAT.md`. Identify which process re-creates this file (it was removed by Fix Agent on 2026-06-27 09:34 but has reappeared), and prevent it from writing heartbeat artifacts outside agent homes.

---

## Summary

| Severity | Count |
|---|---|
| ERROR | 1 |
| WARNING | 0 |
| INFO | 0 |
| **Total** | **1** |

**Structural health:** Clean except 1 recurring HEARTBEAT leak.

**Recurring issue:** `wiki/reviews/HEARTBEAT.md` has been flagged on every hygiene run since 2026-06-25. Fix Agent removed it 2026-06-27 09:34, but it has been re-created. Root cause: a runtime process (likely Hermes cron daemon or heartbeat writer) is writing to `wiki/reviews/` instead of the agent home directory. This needs a process-level fix, not another file deletion.

**Delta from 2026-06-26 (APPROVED):**
- `memory/` root folder: resolved (no longer present)
- `state/` root folder: resolved (no longer present)
- `wiki/reviews/_approval-log.md`: resolved (no longer present)
- `raw/papers/` naming: verified compliant (papers use `YYYY-MM-DD_<author>_<title>.md`)
- `wiki/drafts/` cleanup: `.bak` files and backup subfolders resolved
- `wiki/reviews/HEARTBEAT.md`: **recurring — re-appeared after Fix Agent cleanup**
