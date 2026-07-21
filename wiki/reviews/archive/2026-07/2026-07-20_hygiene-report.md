# Hygiene Inspection — 2026-07-20

**Status:** applied
**Applied by:** Fix Agent
**Applied at:** 2026-07-21 08:40
**Approved by:** Julius
**Issues found:** 3
**Created:** 2026-07-20 23:30:00
**Validator:** hygiene-inspector

**Paths checked:** 51912

---

## Issue 1: Recurring root folder — memory/

**Path:** memory/
**Severity:** ERROR
**Category:** Orphan
**Issue:** Recurring root folder not in whitelist: memory/
**Current:** memory/ directory with 1 file (2026-07-20.md, 2697 bytes)
**Expected:** This folder was migrated to `.openclaw/memory/` in v1.2. Flagged every run since 07-03 (10th occurrence as of 07-18, now 11th). Bulk Fix Agent run on 2026-07-20 removed it, but a process recreated it today (2026-07-20 10:49). File `2026-07-20.md` was modified at 21:42 — the writing process is actively targeting `memory/` instead of `.openclaw/memory/`.
**Suggested fix:** Move contents to `.openclaw/memory/`, then `rmdir memory/`. Identify and fix the process writing to `memory/` instead of `.openclaw/memory/`. This is a **process-level fix** — file deletion alone will not resolve it.

---

## Issue 2: Orphan file inside memory/

**Path:** memory/2026-07-20.md
**Severity:** WARNING
**Category:** Path
**Issue:** Path not classified by any rule (parent folder `memory/` not whitelisted)
**Current:** memory/2026-07-20.md
**Expected:** Should be in a known location or whitelisted
**Suggested fix:** Move to `.openclaw/memory/` before removing the `memory/` directory

---

## Issue 3: Draft file naming — underscores in slug

**Path:** wiki/drafts/src_is-there-anything-left-to-build-in-crypto-wintermute-backup-2026-07-20.md
**Severity:** WARNING
**Category:** Naming
**Issue:** Draft filename uses underscores instead of hyphens
**Current:** src_is-there-anything-left-to-build-in-crypto-wintermute-backup-2026-07-20.md
**Expected:** `<lowercase-hyphen-slug>.md`
**Suggested fix:** Rename to `src-is-there-anything-left-to-build-in-crypto-wintermute-backup-2026-07-20.md` (hyphens). Note: this is a backup file created by Fix Agent — the original file was already renamed to `src_is-there-anything-left-build-crypto-wintermute.md`. Consider deleting this backup if no longer needed.

---

## Delta from previous run (07-19)

- **07-19:** 4 issues (memory/ ERROR, memory/2026-07-15.md WARNING, state/ ERROR, drafts/backup WARNING)
- **07-20:** 3 issues (−1)
- **Resolved:** `state/` directory — removed by Fix Agent bulk application 2026-07-20 ✓
- **Recurring:** `memory/` root folder — 11th occurrence. Was removed by bulk Fix Agent run but recreated same day at 10:49. File contents updated at 21:42, confirming active process leak.
- **New:** `wiki/drafts/src_is-there-anything-left-to-build-in-crypto-wintermute-backup-2026-07-20.md` — backup file from Fix Agent's source rename operation. Filename uses underscores.

---

## Notes

- No HEARTBEAT leaks detected — `wiki/reviews/HEARTBEAT.md` and `raw/.last_heartbeat` remain resolved (fixed 2026-06-28).
- No `state/` folder — resolved by Fix Agent bulk application.
- The `memory/` root folder leak is the only remaining process-level issue. All previous fixes (HEARTBEAT, state/) have held.
- Overall KB hygiene is excellent: 3 issues out of 51,912 paths (0.006%).
