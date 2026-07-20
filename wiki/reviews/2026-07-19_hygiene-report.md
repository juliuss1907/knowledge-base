# Hygiene Inspection — 2026-07-19

**Status:** approved
**Issues found:** 4 (2 ERROR, 1 WARNING, 1 INFO)
**Created:** 2026-07-19 23:30
**Approved by:** Julius
**Approved on:** 2026-07-20
**Validator:** hygiene-inspector

**Paths checked:** 51899

---

## Issue 1: Recurring root folder `memory/`

**Path:** memory/
**Severity:** ERROR
**Category:** Orphan
**Issue:** Recurring root folder not in whitelist: `memory/` — 11th occurrence since 2026-07-03
**Current:** `memory/` directory containing `2026-07-15.md` (memory log)
**Expected:** Memory logs belong in `.openclaw/memory/` (migrated in folder-structure.md v1.2)
**Suggested fix:** Move `memory/2026-07-15.md` to `.openclaw/memory/`, then `rmdir memory/`. Identify and fix the process targeting `memory/` instead of `.openclaw/memory/` — file deletions are transient without a process-level fix.

**Context:** File `memory/2026-07-15.md` is a Memory Log (2,665 bytes) covering "Index Agent Stability Success" from Jul 12-15, 2026. The root folder `memory/` has been flagged 11 times (07-03, 07-06, 07-07, 07-08, 07-11, 07-15, 07-16, 07-17, 07-18, 07-19). The contained file was originally created 2026-07-15 08:58 and has not been updated since.

---

## Issue 2: Recurring root folder `state/`

**Path:** state/
**Severity:** ERROR
**Category:** Orphan
**Issue:** Recurring root folder not in whitelist: `state/` — 7th recurrence since original 2026-06-25 resolution
**Current:** Empty `state/` directory at KB root
**Expected:** If state persistence is needed, it should live inside `.hermes/` or `.openclaw/`
**Suggested fix:** `rmdir state/`. Identify and fix the process recreating an empty `state/` directory at KB root.

**Context:** First flagged 2026-06-25, resolved 2026-06-27, recreated 2026-07-02 onwards. Directory has been empty every single run. The process creating it doesn't populate it — the process fix should be trivial once identified.

---

## Issue 3: Orphan file inside non-whitelisted `memory/`

**Path:** memory/2026-07-15.md
**Severity:** WARNING
**Category:** Path
**Issue:** Memory log file inside non-whitelisted root folder `memory/`
**Current:** `memory/2026-07-15.md` — a memory log at the wrong path
**Expected:** Should be in `.openclaw/memory/2026-07-15.md`
**Suggested fix:** `mv memory/2026-07-15.md .openclaw/memory/2026-07-15.md` (and then `rmdir memory/`)

---

## Issue 4: Empty directory `state/`

**Path:** state/
**Severity:** INFO
**Category:** Orphan
**Issue:** Empty directory at KB root
**Current:** `state/` — zero files, zero subdirectories
**Expected:** Non-empty directory or removed
**Suggested fix:** `rmdir state/`

---

## Summary

| | Count |
|---|---|
| 🔴 ERROR | 2 |
| 🟡 WARNING | 1 |
| 🔵 INFO | 1 |
| **Total** | **4** |

**Delta vs 07-18:** Identical — 5th consecutive run with the same 4 issues. No new violations, no regressions, no resolutions.

**Systemic note:** Both `memory/` and `state/` are process-level leaks — file/directory deletions are transient because the writing process(es) recreate them. These issues have persisted since 2026-07-15 and will continue until the root causes are addressed:
- **`memory/`**: A writer process targets `memory/` at KB root instead of `.openclaw/memory/`. The created file (`2026-07-15.md`) is a legitimate Hermes memory log that should live inside the agent home.
- **`state/`**: An empty directory is created at KB root. The creating process hasn't been identified. The directory serves no purpose since it's never populated.

**Previous resolution (07-14):** The KB was clean (0 issues across 51,831 paths). The regression started 07-15 and has been stable ever since — no new violations beyond these two root folders.
