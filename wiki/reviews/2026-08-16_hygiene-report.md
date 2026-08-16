# Hygiene Inspection — 2026-08-16

**Status:** pending
**Issues found:** 4
**Created:** 2026-08-16 23:45
**Validator:** hygiene-inspector

**Paths checked:** 53570

---

## Issue 1: Recurring root folder not in whitelist: memory/

**Path:** memory/
**Severity:** ERROR
**Category:** Orphan
**Issue:** Recurring root folder not in whitelist — `memory/` reappeared at KB root. Confirmed live process leak: it contains `2026-08-16-heartbeat-status.md` (root-owned, created today 21:51), a heartbeat/session-status file that the writing process emits to KB root `memory/` instead of `.openclaw/memory/`. The file is even git-tracked, so the leak persists across commits.
**Current:** `memory/2026-08-16-heartbeat-status.md` (git-tracked)
**Expected:** `memory/` does not belong at KB root — memory logs go to `.openclaw/memory/` only (AGENTS.md §4.4); heartbeat/session-status belongs in `.openclaw/`
**Suggested fix:** Process-level fix — redirect the writing process output path from `memory/` to `.openclaw/memory/`. Then `rm -rf memory/` and commit the removal. File deletion is a stopgap; the writer will recreate it.

---

## Issue 2: Recurring root folder not in whitelist: state/

**Path:** state/
**Severity:** ERROR
**Category:** Orphan
**Issue:** Recurring root folder `state/` not in whitelist. Resurfaced for the 3rd consecutive run (08-14, 08-15, 08-16). Currently empty.
**Current:** `state/` (empty directory)
**Expected:** No `state/` folder at KB root — not in folder-structure.md whitelist
**Suggested fix:** `rmdir state/` (stopgap). The folder keeps being recreated — identify and fix the process creating it, or move state inside `.hermes/` if needed.

---

## Issue 3: Path not classified by any rule

**Path:** memory/2026-08-16-heartbeat-status.md
**Severity:** WARNING
**Category:** Path
**Issue:** File under the orphaned `memory/` root folder — not classified by any rule (direct consequence of Issue 1).
**Current:** `memory/2026-08-16-heartbeat-status.md`
**Expected:** Should be in a known location or whitelisted — belongs in `.openclaw/` (heartbeat/session-status artifact)
**Suggested fix:** Resolve Issue 1 (fix the writing process path, then remove `memory/`).

---

## Issue 4: Empty directory

**Path:** state/
**Severity:** INFO
**Category:** Orphan
**Issue:** Empty directory at KB root.
**Current:** `state/` (no contents)
**Expected:** Non-empty directory or removed
**Suggested fix:** `rmdir state/`

---

## Escalation

```
[SYSTEMATIC VIOLATION]
Pattern: `memory/` root orphan recreated with a fresh heartbeat-status file every run (via process leak)
Evidence: memory/2026-08-16-heartbeat-status.md created today 21:51, git-tracked, writers emits to KB root `memory/` instead of `.openclaw/memory/`
Likely cause: The heartbeat-status/session writer's output path points at KB root `memory/` instead of `.openclaw/memory/`
Recommendation: Fix the writing process output path (root-cause fix, not file deletion). `state/` is a secondary phantom directory also needing a writer fix or removal.
```

---

## Run notes

- Recurring leaks: `memory/` (root) + `state/` (root) resurfaced for 3rd consecutive run — broke the 08-11→08-13 clean streak.
- `memory/` is NOT a single-file artifact this run — the heartbeat-status file proves an active process leak each time it runs.
- `wiki/HEARTBEAT.md` and `wiki/reviews/HEARTBEAT.md` leaks remain absent (no new leaks in the wiki layer).