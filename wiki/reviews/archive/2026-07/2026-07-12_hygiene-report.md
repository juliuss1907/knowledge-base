# Hygiene Inspection — 2026-07-12

**Status: applied
**Issues found:** 1
**Created:** 2026-07-12 23:30:00
**Validator:** hygiene-inspector

**Paths checked:** 51808

---

## Issue 1: File not in root whitelist

**Path:** `selected_concepts.txt`
**Severity:** ERROR
**Category:** Path
**Issue:** File not in root whitelist
**Current:** `selected_concepts.txt`
**Expected:** Only AGENTS.md, TAGS.md, README.md, knowledge-base.md, symlinks, .gitignore allowed
**Suggested fix:** Move to appropriate subfolder or delete

---

## Summary

| Severity | Count |
|---|---|
| ERROR | 1 |
| WARNING | 0 |
| INFO | 0 |

**Recurring issues resolved this run:**
- `memory/` root folder: not present (recurring pattern 07-03 through 07-11 — not detected today)
- `state/` root folder: not present (recurring pattern last seen 07-02 — not detected today)
- `wiki/reviews/HEARTBEAT.md`: not present (last seen 06-27 — resolved since 06-28)
- `raw/.last_heartbeat`: not present

**New issue:** `selected_concepts.txt` at KB root — likely a temporary work file. Move or delete.
