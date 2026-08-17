# Hygiene Inspection — 2026-08-17

**Status:** pending
**Issues found:** 9
**Created:** 2026-08-17 23:31:42
**Validator:** hygiene-inspector

**Paths checked:** 53578

---

## Issue 1: Recurring root folder not in whitelist: memory/

**Path:** memory/
**Severity:** ERROR
**Category:** Orphan
**Issue:** Recurring root folder `memory/` not in whitelist. Resurfaced for the 4th consecutive run (08-14, 08-15, 08-16, 08-17). Contains **6 files, all created today (2026-08-17)** — session logs, heartbeat, and fetch-status artifacts. All 6 files are **git-tracked** (confirmed via `git ls-files memory/`), so the leak persists across the auto-commit `vault backup` (~every 10 min). Process-level leak, not a stray artifact.
**Current:** `memory/2026-08-17-1325.md`, `-1327.md`, `-1329.md`, `2026-08-17-fetch-status.md`, `2026-08-17-heartbeat-ok.md`, `2026-08-17-heartbeat-poll.md`
**Expected:** `memory/` does not belong at KB root — memory logs go to `.openclaw/memory/` only (AGENTS.md §4.4)
**Suggested fix:** Root-cause fix — redirect the writing process output path from KB root `memory/` to `.openclaw/memory/`, then `git rm -r memory/` + commit. File deletion alone is a stopgap (files are git-tracked and recreated each run).

---

## Issue 2: Recurring root folder not in whitelist: state/

**Path:** state/
**Severity:** ERROR
**Category:** Orphan
**Issue:** Recurring root folder `state/` not in whitelist. Resurfaced for the 4th consecutive run (08-14, 08-15, 08-16, 08-17). Currently empty, not git-tracked.
**Current:** `state/` (empty directory)
**Expected:** No `state/` folder at KB root — not in folder-structure.md whitelist
**Suggested fix:** `rmdir state/` (stopgap). Identify and fix the process recreating it, or move state inside `.hermes/` if it holds real runtime state.

---

## Issue 3: Path not classified by any rule

**Path:** memory/2026-08-17-1325.md
**Severity:** WARNING
**Category:** Path
**Issue:** File under the orphaned `memory/` root folder — not classified by any rule (direct consequence of Issue 1).
**Current:** `memory/2026-08-17-1325.md`
**Expected:** Should be in a known location — belongs in `.openclaw/memory/` (OpenClaw session log)
**Suggested fix:** Resolve Issue 1 (fix writing process path, then remove `memory/`).

---

## Issue 4: Path not classified by any rule

**Path:** memory/2026-08-17-1327.md
**Severity:** WARNING
**Category:** Path
**Issue:** File under the orphaned `memory/` root folder — not classified by any rule (direct consequence of Issue 1).
**Current:** `memory/2026-08-17-1327.md`
**Expected:** Should be in a known location — belongs in `.openclaw/memory/` (OpenClaw session log)
**Suggested fix:** Resolve Issue 1 (fix writing process path, then remove `memory/`).

---

## Issue 5: Path not classified by any rule

**Path:** memory/2026-08-17-1329.md
**Severity:** WARNING
**Category:** Path
**Issue:** File under the orphaned `memory/` root folder — not classified by any rule (direct consequence of Issue 1).
**Current:** `memory/2026-08-17-1329.md`
**Expected:** Should be in a known location — belongs in `.openclaw/memory/` (OpenClaw session log)
**Suggested fix:** Resolve Issue 1 (fix writing process path, then remove `memory/`).

---

## Issue 6: Path not classified by any rule

**Path:** memory/2026-08-17-fetch-status.md
**Severity:** WARNING
**Category:** Path
**Issue:** File under the orphaned `memory/` root folder — not classified by any rule (direct consequence of Issue 1).
**Current:** `memory/2026-08-17-fetch-status.md`
**Expected:** Should be in a known location — belongs in `.openclaw/memory/` (fetch-status artifact)
**Suggested fix:** Resolve Issue 1 (fix writing process path, then remove `memory/`).

---

## Issue 7: Path not classified by any rule

**Path:** memory/2026-08-17-heartbeat-ok.md
**Severity:** WARNING
**Category:** Path
**Issue:** File under the orphaned `memory/` root folder — not classified by any rule (direct consequence of Issue 1).
**Current:** `memory/2026-08-17-heartbeat-ok.md`
**Expected:** Should be in a known location — heartbeat artifact belongs in `.openclaw/`
**Suggested fix:** Resolve Issue 1 (fix writing process path, then remove `memory/`).

---

## Issue 8: Path not classified by any rule

**Path:** memory/2026-08-17-heartbeat-poll.md
**Severity:** WARNING
**Category:** Path
**Issue:** File under the orphaned `memory/` root folder — not classified by any rule (direct consequence of Issue 1).
**Current:** `memory/2026-08-17-heartbeat-poll.md`
**Expected:** Should be in a known location — heartbeat artifact belongs in `.openclaw/`
**Suggested fix:** Resolve Issue 1 (fix writing process path, then remove `memory/`).

---

## Issue 9: Empty directory

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
Pattern: `memory/` AND `state/` root orphans resurfaced for the 4th consecutive run (08-14 → 08-17). memory/ now holds 6 files, all created 2026-08-17.
Evidence: memory/2026-08-17-1325/1327/1329.md (OpenClaw session logs, agent:main:main), heartbeat-ok.md, heartbeat-poll.md, fetch-status.md — all git-tracked, pushed to commits via auto `vault backup` (git ls-files memory/ confirmed).
Likely cause: A writing process (session/heartbeat/status writer) emits to KB root `memory/` instead of `.openclaw/memory/`. `state/` is a phantom empty dir with its own writer.
Recommendation: Root-cause fix — redirect the session/heartbeat/fetch writer output path from KB root `memory/` to `.openclaw/memory/`, then `git rm -r memory/` + commit. `rmdir state/`. Deletion without a writer fix is futile — the files reappear every run and are resurrected by commits.
```

---

## Run notes

- Recurring leaks: `memory/` (root) + `state/` (root) — 4th consecutive run (08-14 → 08-17). Broke the 08-11 → 08-13 clean streak (which is now 3 runs behind).
- `memory/` this run holds **6 files**, all created 08-17 — more files than previous runs, confirming an active writer that runs multiple times daily.
- **Not a single-file artifact:** session logs (`2026-08-17-13xx.md`) are OpenClaw session records spawned by the runtime; heartbeat + fetch-status are status writers. All git-tracked.
- `wiki/HEARTBEAT.md` and `wiki/reviews/HEARTBEAT.md` leaks remain absent (no new leaks in the wiki layer).
- HEARTBEAT leaks in `raw/.last_heartbeat` also absent.