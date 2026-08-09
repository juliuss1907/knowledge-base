# Hygiene Inspection — 2026-08-09

**Status:** pending
**Issues found:** 3
**Created:** 2026-08-09 23:31:00
**Validator:** hygiene-inspector

**Paths checked:** 53,507

---

## Issue 1: Recurring root folder not in whitelist — state/

**Path:** `state/`
**Severity:** ERROR
**Category:** Orphan
**Issue:** Recurring root folder not in whitelist: state/
**Current:** `state/` (empty directory)
**Expected:** Root folders limited to: `.git`, `.obsidian`, `.openclaw`, `.hermes`, `context`, `raw`, `wiki`, `scripts`
**Suggested fix:** `rmdir state/` — this is the 4th consecutive run (08-07, 08-08, 08-09) where this folder has been flagged. Previously resolved 2026-06-27, recreated 2026-07-02. A process keeps recreating this empty directory.

---

## Issue 2: HEARTBEAT.md leaked to wiki/ root

**Path:** `wiki/HEARTBEAT.md`
**Severity:** ERROR
**Category:** Path
**Issue:** File at wiki/ root level — HEARTBEAT.md leaked outside agent home
**Current:** `wiki/HEARTBEAT.md`
**Expected:** `wiki/` root may only contain `wiki.md`. HEARTBEAT.md belongs in `.hermes/` or `.openclaw/`.
**Suggested fix:** Delete `wiki/HEARTBEAT.md` and identify the process writing HEARTBEAT.md to `wiki/` root. This is the 3rd consecutive run (08-07, 08-08, 08-09) with this new leak location. File deletion is transient — the writing process must be fixed.

---

## Issue 3: Empty directory — state/

**Path:** `state/`
**Severity:** INFO
**Category:** Orphan
**Issue:** Empty directory
**Current:** `state/` (contains no files)
**Expected:** Non-empty directory or removed
**Suggested fix:** `rmdir state/`

---

## Summary

| Severity | Count |
|---|---|
| ERROR | 2 |
| WARNING | 0 |
| INFO | 1 |
| **Total** | **3** |

**No WARNINGs.** 3rd consecutive run with identical results (08-07, 08-08, 08-09). Both ERRORs are recurring — `state/` has been flagged every run since 07-02, and `wiki/HEARTBEAT.md` is a new leak location first detected on 08-07.

**Delta from 2026-08-08:** 0 new issues, 0 resolved issues — identical scan.