# Hygiene Inspection — 2026-07-13

**Status:** pending
**Issues found:** 1
**Created:** 2026-07-13 23:30:00
**Validator:** hygiene-inspector (v1.11)

**Paths checked:** 51,825

---

## Summary

| Severity | Count |
|---|---|
| ERROR | 1 |
| WARNING | 0 |
| INFO | 0 |
| **Total** | **1** |

---

## Issue 1: Unauthorized file at KB root

**Path:** `selected_concepts.txt`
**Severity:** ERROR
**Category:** Path
**Issue:** File not in root whitelist
**Current:** `selected_concepts.txt` at KB root — not in root whitelist
**Expected:** Only AGENTS.md, TAGS.md, README.md, knowledge-base.md, symlinks (HEARTBEAT.md, IDENTITY.md, SOUL.md, TOOLS.md, USER.md), .gitignore at root level
**Suggested fix:** Move to appropriate subfolder (`wiki/drafts/`, `raw/`, or `scripts/`) or delete

**Note:** This is the same issue flagged on 2026-07-12 (still unresolved). Recurring — has persisted through at least one prior run. If this file is a workflow artifact, update `folder-structure.md` to whitelist it or move it to `scripts/`.

---

## Delta vs Previous Run (2026-07-12)

| Metric | 07-12 | 07-13 | Δ |
|---|---|---|---|
| Paths checked | 51,808 | 51,825 | +17 |
| Issues total | 1 | 1 | 0 |
| ERRORs | 1 | 1 | 0 |
| WARNINGs | 0 | 0 | 0 |
| Recurring issues | — | `selected_concepts.txt` (2nd run) | — |

**Notable:** Clean scan except for the single recurring root-level file. No HEARTBEAT leaks, no root folder orphans (`memory/`, `state/`), no naming violations, no empty directories.

---

## Historical Context

- **`selected_concepts.txt`**: First flagged 2026-07-12. Still present 2026-07-13. Needs Julius decision — move, delete, or whitelist.
- **`memory/` root folder**: Resolved 2026-07-11. Not present this run. ✅
- **`state/` root folder**: Resolved 2026-06-27. Not present this run. ✅
- **HEARTBEAT.md leak (wiki/reviews/)**: Resolved 2026-06-28. Not present since. ✅
