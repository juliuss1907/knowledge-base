# Hygiene Inspection — 2026-08-08

**Status:** approved
**Approved by:** Julius
**Approved date:** 2026-08-10
**Issues found:** 3 (2 ERROR, 0 WARNING, 1 INFO)
**Created:** 2026-08-08 23:30:00
**Validator:** hygiene-inspector

**Paths checked:** 53502

---

## Issue 1: Recurring root folder `state/` not in whitelist

**Path:** `state/`
**Severity:** ERROR
**Category:** Orphan
**Issue:** Recurring root folder not in whitelist: `state/`
**Current:** `state/` (empty directory, created 2026-08-06)
**Expected:** Recurring empty directory — previously resolved 2026-06-27, recreated 2026-07-02. Move inside `.hermes/` or `.openclaw/` if needed; otherwise rmdir.
**Suggested fix:** `rmdir state/`

---

## Issue 2: HEARTBEAT.md at wiki/ root level

**Path:** `wiki/HEARTBEAT.md`
**Severity:** ERROR
**Category:** Path
**Issue:** File at wiki/ root level — `wiki/` root may only contain `wiki.md`
**Current:** `wiki/HEARTBEAT.md` (889 bytes, created 2026-08-06)
**Expected:** wiki/ root may only contain wiki.md
**Suggested fix:** Move to appropriate subfolder. HEARTBEAT.md belongs in `.hermes/` or `.openclaw/`. Identify and fix the writing process that creates this file.

---

## Issue 3: Empty directory `state/`

**Path:** `state/`
**Severity:** INFO
**Category:** Orphan
**Issue:** Empty directory
**Current:** `state/` (0 files, 0 subdirs)
**Expected:** Non-empty directory or removed
**Suggested fix:** Add content or remove directory (`rmdir state/`)

---

## Summary

| Severity | Count |
|---|---|
| ERROR | 2 |
| WARNING | 0 |
| INFO | 1 |
| **Total** | **3** |

**Notes:**
- `state/` is a recurring empty folder — previously resolved 2026-06-27, recreated. Persistent via some process.
- `wiki/HEARTBEAT.md` is a new leak pattern — not the previously tracked `wiki/reviews/HEARTBEAT.md` but a new file at `wiki/` root. Same root cause: a process writing HEARTBEAT.md to the wrong location.
- `memory/` root folder previously flagged as recurring is absent this run — may finally be resolved.