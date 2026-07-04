# Hygiene Inspection — 2026-07-04

**Status:** pending
**Issues found:** 4 (2 ERROR, 1 WARNING, 1 INFO)
**Created:** 2026-07-04 23:30:00
**Validator:** hygiene-inspector

**Paths checked:** 51,661

---

## Issue 1: Recurring root folder — memory/

**Path:** `memory/`
**Severity:** ERROR
**Category:** Path
**Issue:** Folder not in root whitelist. `memory/` was migrated to `.openclaw/memory/` in folder-structure.md v1.2 (2026-05-17). The folder has reappeared with a content file inside, indicating a running process is still targeting the old path.
**Current:** `memory/` exists at root level with content file `2026-07-03.md`
**Expected:** Memory files belong in `.openclaw/memory/` (per folder-structure.md v1.2)
**Suggested fix:** Move `memory/2026-07-03.md` to `.openclaw/memory/`, fix the process to write to `.openclaw/memory/` instead of `memory/`, then `rmdir memory/`

---

## Issue 2: Recurring root folder — state/

**Path:** `state/`
**Severity:** ERROR
**Category:** Orphan
**Issue:** Recurring root folder not in whitelist. Previously resolved 2026-06-27, recreated 2026-07-02. Empty directory — no content inside.
**Current:** `state/` (empty)
**Expected:** No such folder at root. If needed, move inside `.hermes/` or `.openclaw/`.
**Suggested fix:** `rmdir state/`

---

## Issue 3: Content file inside orphaned memory/ folder

**Path:** `memory/2026-07-03.md`
**Severity:** WARNING
**Category:** Path
**Issue:** Content file found inside the orphaned `memory/` folder. This file was written by a process targeting the old `memory/` path instead of `.openclaw/memory/`.
**Current:** `memory/2026-07-03.md` — content file dated 2026-07-03
**Expected:** All memory files belong in `.openclaw/memory/`
**Suggested fix:** Move to `.openclaw/memory/2026-07-03.md`; fix the writing process to target the correct output path

---

## Issue 4: Empty directory — state/

**Path:** `state/`
**Severity:** INFO
**Category:** Orphan
**Issue:** Empty directory. Already flagged as ERROR above. Redundant INFO for visibility.
**Current:** `state/` (empty)
**Expected:** Non-empty directory or removed
**Suggested fix:** `rmdir state/`
