# Hygiene Inspection — 2026-08-03

**Status:** pending
**Issues found:** 3 (1 ERROR, 1 WARNING, 1 INFO)
**Created:** 2026-08-03 23:30:00
**Validator:** hygiene-inspector

**Paths checked:** 53,480

---

## Issue 1: Recurring root folder `state/`

**Path:** state/
**Severity:** ERROR
**Category:** Orphan
**Issue:** Recurring root folder not in whitelist: `state/`. Folder recreated 2026-08-02 — had been absent since 2026-06-27 (over a month clean). Empty directory — no files inside.

**Current:** `state/` (empty, created 2026-08-02)
**Expected:** `state/` should not exist at KB root. If state is needed, move inside `.hermes/` or `.openclaw/`.
**Suggested fix:** `rmdir state/`. Then identify and fix the process that recreated it on 08-02.

**Delta from 08-01:** `state/` was absent from 08-01 run (and all runs since late June). This is a **regression** — a process created an empty `state/` on Aug 2.

---

## Issue 2: Leftover index file from `raw/tools/` migration

**Path:** raw/websites/tools.md
**Severity:** WARNING
**Category:** Naming
**Issue:** Leftover index file from `raw/tools/` migration by Fix Agent (morning 08-01 batch). The old `tools.md` index was moved along with content files but does not follow `YYYY-MM-DD_<slug>.md` naming convention. File exists since 2026-07-26. Its 2 items are already tracked in `raw/websites/websites.md`.

**Current:** `raw/websites/tools.md` (686 bytes, dated 2026-07-26)
**Expected:** All content files in `raw/websites/` must match `YYYY-MM-DD_<slug>.md`. Index files should be named `<type>.md` (`websites.md`).
**Suggested fix:** Verify no unique items → delete `raw/websites/tools.md`. Update Fix Agent migration procedure to also handle leftover index files.

**Delta from 08-01:** Unchanged — same issue, not yet actioned.

---

## Issue 3: Empty directory `state/`

**Path:** state/
**Severity:** INFO
**Category:** Orphan
**Issue:** Empty directory — same `state/` as Issue 1. No files inside.

**Current:** `state/` (empty)
**Expected:** Non-empty directory or removed
**Suggested fix:** `rmdir state/`

---

## Summary

| Count | Severity |
|---|---|
| 1 | ERROR |
| 1 | WARNING |
| 1 | INFO |

**Delta from 2026-08-01 (1 WARNING):**
- `raw/websites/tools.md` — same WARNING persists (not yet actioned)
- `state/` — **REGRESSION**: root folder recreated 2026-08-02 after being absent since late June. Empty. New ERROR + INFO pair.
- Clean: No `memory/` root folder, no HEARTBEAT leaks, no naming violations elsewhere.

**Actions needed:**
1. **Fix Agent:** Verify `raw/websites/tools.md` items are in `raw/websites/websites.md` → delete the leftover
2. **Julius:** `rmdir state/` then investigate what process recreated it on 08-02
3. **Fix Agent:** Update migration procedure — when removing a raw subfolder, also handle the leftover index file name
