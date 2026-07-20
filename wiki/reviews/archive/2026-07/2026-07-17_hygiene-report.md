# Hygiene Inspection — 2026-07-17

**Status:** applied
**Issues found:** 4
**Created:** 2026-07-17 23:30:00
**Approved by:** Julius
**Approved on:** 2026-07-20
**Validator:** hygiene-inspector

**Paths checked:** 51,883

---

## Summary

| Severity | Count |
|---|---|
| ERROR | 2 |
| WARNING | 1 |
| INFO | 1 |

**Delta vs 07-16:** 0 change (identical issues, paths_checked +22 from report/action file writes). Third consecutive run with the same 4 issues — no new violations, no regressions, no resolutions.

---

## Issue 1: Recurring root folder — `memory/`

**Path:** memory/
**Severity:** ERROR
**Category:** Orphan
**Issue:** Recurring root folder not in whitelist: memory/
**Current:** `memory/` directory at KB root containing `2026-07-15.md`
**Expected:** Memory logs belong in `.openclaw/memory/` (migrated in v1.2). Root-level `memory/` is forbidden.
**Suggested fix:** Move `memory/2026-07-15.md` to `.openclaw/memory/`, then `rmdir memory/`. Identify and fix the process writing to `memory/` instead of `.openclaw/memory/`.

**Recurrence history:** 9th occurrence since 2026-07-03. Flagged every run: 07-03, 07-06, 07-07, 07-08, 07-11, 07-15, 07-16, and now 07-17. This is a **process-level leak** — a writer targets `memory/` instead of `.openclaw/memory/`. File deletion alone will not resolve it.

---

## Issue 2: Recurring root folder — `state/`

**Path:** state/
**Severity:** ERROR
**Category:** Orphan
**Issue:** Recurring root folder not in whitelist: state/
**Current:** Empty `state/` directory at KB root
**Expected:** If needed, `state/` belongs inside `.hermes/` or `.openclaw/`. Not at KB root.
**Suggested fix:** `rmdir state/`. Identify and fix the process creating empty `state/` at KB root.

**Recurrence history:** 5th recurrence since original 2026-06-25 resolution. Reappeared 07-02, 07-03, 07-15, 07-16, and persists 07-17. Process recreates an empty directory — file deletion alone will not resolve it.

---

## Issue 3: Orphan file inside non-whitelisted root folder

**Path:** memory/2026-07-15.md
**Severity:** WARNING
**Category:** Path
**Issue:** Path not classified by any rule — file inside non-whitelisted `memory/` root folder
**Current:** `memory/2026-07-15.md` — a memory log (Index Agent Stability Success entry)
**Expected:** Memory logs belong in `.openclaw/memory/2026-07-15.md`
**Suggested fix:** Move to `.openclaw/memory/2026-07-15.md`

---

## Issue 4: Empty directory at KB root

**Path:** state/
**Severity:** INFO
**Category:** Orphan
**Issue:** Empty directory
**Current:** `state/` — empty directory at KB root
**Expected:** Non-empty directory or removed
**Suggested fix:** Add content or remove directory (`rmdir state/`)

---

## Notes

- All 4 issues are identical to the 07-15 and 07-16 hygiene runs — no new violations, no regressions, no resolutions.
- Neither `memory/` nor `state/` is in the root whitelist (section 2 of folder-structure.md v1.2).
- No HEARTBEAT leaks detected — the 06-28 resolution is holding.
- No naming convention violations in `wiki/reviews/`, `wiki/drafts/`, or `raw/` content.
- All `wiki/reviews/` report files use canonical `YYYY-MM-DD_<type>-report.md` naming.
- KB structure is otherwise fully compliant.
