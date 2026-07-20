# Hygiene Inspection — 2026-07-16

**Status:** applied
**Issues found:** 4
**Created:** 2026-07-16 23:30:00
**Approved by:** Julius
**Approved on:** 2026-07-20
**Validator:** hygiene-inspector

**Paths checked:** 51,861

---

## Issue 1: Recurring root folder — memory/

**Path:** memory/
**Severity:** ERROR
**Category:** Orphan
**Issue:** Recurring root folder not in whitelist: memory/
**Current:** memory/ (directory at KB root)
**Expected:** Root contains only: .git, .obsidian, .openclaw, .hermes, context, raw, wiki, scripts. memory/ belongs in .openclaw/memory/.
**Suggested fix:** Move `memory/2026-07-15.md` to `.openclaw/memory/`, then `rmdir memory/`. Identify and fix the process writing to `memory/` instead of `.openclaw/memory/`.

---

## Issue 2: Recurring root folder — state/

**Path:** state/
**Severity:** ERROR
**Category:** Orphan
**Issue:** Recurring root folder not in whitelist: state/
**Current:** state/ (empty directory at KB root)
**Expected:** Root-level directories limited to whitelist. state/ belongs inside .hermes/ or .openclaw/ if needed.
**Suggested fix:** `rmdir state/`. Identify the process recreating this empty directory.

---

## Issue 3: Orphan file in non-whitelisted root folder

**Path:** memory/2026-07-15.md
**Severity:** WARNING
**Category:** Path
**Issue:** Path not classified by any rule — file inside non-whitelisted `memory/` folder
**Current:** memory/2026-07-15.md
**Expected:** Memory log files belong in `.openclaw/memory/`
**Suggested fix:** Move to `.openclaw/memory/2026-07-15.md`, then remove `memory/` directory.

---

## Issue 4: Empty directory

**Path:** state
**Severity:** INFO
**Category:** Orphan
**Issue:** Empty directory
**Current:** state/ (empty)
**Expected:** Non-empty directory or removed
**Suggested fix:** `rmdir state/` (redundant with Issue 2)

---

## Summary

| Severity | Count |
|---|---|
| ERROR | 2 |
| WARNING | 1 |
| INFO | 1 |

**Pattern:** Identical to 2026-07-15 run (4 issues, same categories). Both `memory/` and `state/` continue to recur — file deletions are transient without process-level fixes.

**Delta vs 07-15:** 0 change (same 4 issues, paths_checked +16 from report file writes).
