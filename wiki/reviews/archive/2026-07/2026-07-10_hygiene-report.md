# Hygiene Inspection — 2026-07-10

**Status: applied
**Approved by:** Julius
**Issues found:** 1
**Created:** 2026-07-10 23:30:00
**Validator:** hygiene-inspector

**Paths checked:** 51,741

---

## Issue 1: Root-level file not in whitelist

**Path:** `index_kb.py`
**Severity:** ERROR
**Category:** Path
**Issue:** File not in root whitelist
**Current:** `index_kb.py` at knowledge base root
**Expected:** Only AGENTS.md, TAGS.md, README.md, knowledge-base.md, symlinks, .gitignore allowed
**Suggested fix:** Move to `scripts/` or delete

**Context:**
- File created 2026-07-10 at 21:03 via vault backup (git: `895aae6d vault backup: 2026-07-10 21:05:36`)
- 280 lines, 11,171 bytes — appears to be a Python indexing script
- Likely should live in `scripts/` if it's a KB tool, or under `.hermes/` if it's an agent script

---

## Result

⚠️ **1 ERROR** — `index_kb.py` at root level.

All other 51,740 paths validated clean:
- Root level — all other files and folders within whitelist
- `context/` — exactly `context.md` + `USER.md`
- `raw/` — all 6 subfolders present, naming conventions followed
- `wiki/` — all 7 subfolders present, naming conventions followed
- Agent homes — no user content leaks
- No HEARTBEAT artifacts outside agent homes
- No `state/` root orphan
- No empty directories outside archive

---

## Delta vs previous run (2026-07-09)

| Metric | 2026-07-09 | 2026-07-10 | Change |
|---|---|---|---|
| Issues | 0 | 1 (1 ERROR) | +1 ⚠️ |
| Paths checked | 51,724 | 51,741 | +17 |

**New since 07-09:**
- `index_kb.py` at root — introduced 2026-07-10 via vault backup. Move to `scripts/`.
