# Hygiene Inspection — 2026-08-07

**Status:** approved
**Approved by:** Julius
**Approved date:** 2026-08-10
**Issues found:** 3 (2 ERROR, 0 WARNING, 1 INFO)
**Created:** 2026-08-07 23:31:54
**Validator:** hygiene-inspector

**Paths checked:** 53,499

---

## Issue 1: Recurring root folder — state/

**Path:** state/
**Severity:** ERROR
**Category:** Orphan
**Issue:** Recurring root folder not in whitelist: state/
**Current:** state/ (empty directory)
**Expected:** Not present at root level. Previously resolved 2026-06-27, recreated 2026-07-02, resolved again 07-20 through 08-06. Reappeared 08-07.
**Suggested fix:** Remove directory: `rmdir state/`. If a process recreates it, move inside .hermes/ or .openclaw/ and fix the writing process.

---

## Issue 2: HEARTBEAT.md at wiki/ root level

**Path:** wiki/HEARTBEAT.md
**Severity:** ERROR
**Category:** Path
**Issue:** File at wiki/ root level — only wiki.md is allowed at wiki/ root
**Current:** wiki/HEARTBEAT.md
**Expected:** wiki/ root may only contain wiki.md. HEARTBEAT.md belongs in .hermes/ or .openclaw/ (or as a symlink at KB root).
**Suggested fix:** Delete `wiki/HEARTBEAT.md`. This is a new leak pattern — previously HEARTBEAT.md leaked to `wiki/reviews/` (resolved 2026-06-28). Now it's leaking to `wiki/` root. Identify the writing process and fix its output path.

---

## Issue 3: Empty directory — state/

**Path:** state/
**Severity:** INFO
**Category:** Orphan
**Issue:** Empty directory
**Current:** state/ (contains no files or subdirectories)
**Expected:** Non-empty directory or removed
**Suggested fix:** Remove directory: `rmdir state/`

---

## Notes

- **state/ reappeared** after being absent from 07-21 through 08-06. This is the first recurrence since the Fix Agent bulk apply (07-20). May indicate a process is still creating it.
- **wiki/HEARTBEAT.md** is a new leak pattern. The previous `wiki/reviews/HEARTBEAT.md` leak was resolved 2026-06-28. This is leaking to `wiki/` root — a different location. Root cause: a process writes HEARTBEAT.md to the wrong directory.
- No other violations detected across 53,499 paths. Folder structure is otherwise clean.