# Hygiene Inspection — 2026-08-10

**Status:** approved
**Approved by:** Julius
**Approved date:** 2026-08-10
**Issues found:** 5 (3 ERROR, 1 WARNING, 1 INFO)
**Created:** 2026-08-10 23:30:00
**Validator:** hygiene-inspector

**Paths checked:** 53,518

---

## Issue 1: Recurring root folder — memory/

**Path:** memory/
**Severity:** ERROR
**Category:** Orphan
**Issue:** Recurring root folder not in whitelist: memory/
**Current:** memory/ (contains 1 file: `2026-08-10-1258.md` — a session log written today at 19:58 ICT)
**Expected:** Old folder migrated to .openclaw/memory/ in v1.2. A process still writes to `memory/` instead of `.openclaw/memory/`.
**Suggested fix:** Move contents to `.openclaw/memory/`, then `rmdir memory/`. Fix the writing process output path.

**Recurrence history:** Flagged 07-03, 07-06, 07-07, 07-08, 07-11. Reappeared 08-10 with fresh content.

---

## Issue 2: Recurring root folder — state/

**Path:** state/
**Severity:** ERROR
**Category:** Orphan
**Issue:** Recurring root folder not in whitelist: state/
**Current:** state/ (empty directory)
**Expected:** Previously resolved 2026-06-27, recreated 2026-07-02. Move inside .hermes/ or .openclaw/ if needed; otherwise rmdir.
**Suggested fix:** Remove directory: `rmdir state/`

**Recurrence history:** Flagged every run since 2026-07-02. Previously resolved 2026-06-27, recreated 2026-07-02. Consistently empty.

---

## Issue 3: Heartbeat file at wiki/ root level

**Path:** wiki/HEARTBEAT.md
**Severity:** ERROR
**Category:** Path
**Issue:** File at wiki/ root level — wiki/ root may only contain wiki.md
**Current:** wiki/HEARTBEAT.md (OpenClaw heartbeat file, last updated 2026-08-06 10:00)
**Expected:** wiki/ root may only contain wiki.md
**Suggested fix:** Delete this file. Identify and fix the process writing HEARTBEAT.md to wiki/ root (not wiki/reviews/ — this is a different leak path from the known `wiki/reviews/HEARTBEAT.md` recurrence).

**Note:** This is distinct from the `wiki/reviews/HEARTBEAT.md` recurrence. The leak target is `wiki/HEARTBEAT.md` (wiki root), which is a new variant.

---

## Issue 4: Orphaned file inside memory/

**Path:** memory/2026-08-10-1258.md
**Severity:** WARNING
**Category:** Path
**Issue:** Path not classified by any rule — file inside orphaned memory/ root folder
**Current:** memory/2026-08-10-1258.md (session log: agent:main:main, source: telegram, 2026-08-10 12:58 UTC)
**Expected:** Should be in `.openclaw/memory/` or `.hermes/memory/`
**Suggested fix:** Move to `.openclaw/memory/` along with parent folder cleanup

---

## Issue 5: Empty directory — state/

**Path:** state/
**Severity:** INFO
**Category:** Orphan
**Issue:** Empty directory
**Current:** state/ (no files, no subdirectories)
**Expected:** Non-empty directory or removed
**Suggested fix:** Add content or remove directory

---

## Summary

| Severity | Count |
|---|---|
| ERROR | 3 |
| WARNING | 1 |
| INFO | 1 |
| **Total** | **5** |

**Delta from 2026-08-09 (previous run):** +2 issues (was 3 → now 5). `memory/` root folder and its contents reappeared after being absent 08-08 through 08-09. A process wrote a new session log (`2026-08-10-1258.md`) to `memory/` at 19:58 ICT today, recreating the folder. `state/` and `wiki/HEARTBEAT.md` remain unresolved from previous runs.

**Repeated issues (carried over from 08-07, 08-08, 08-09):**
- `state/` (ERROR + INFO) — 4th consecutive run
- `wiki/HEARTBEAT.md` (ERROR) — 4th consecutive run

**New in this run:**
- `memory/` (ERROR) — reappeared after 2-run absence with fresh content
- `memory/2026-08-10-1258.md` (WARNING) — new session log written today