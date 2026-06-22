# Hygiene Inspection — 2026-06-22

**Status:** pending
**Issues found:** 1
**Created:** 2026-06-22 23:30
**Validator:** hygiene-inspector

**Paths checked:** 29

---

## Summary

| Severity | Count |
|---|---|
| ERROR | 0 |
| WARNING | 1 |
| INFO | 0 |

---

## Issue 1: Hidden file at root `.last_heartbeat`

**Path:** `.last_heartbeat`
**Severity:** WARNING
**Category:** Naming / Orphan
**Issue:** Hidden file at root level — only `.gitignore` is whitelisted for hidden root files.
**Current:** `.last_heartbeat` file exists at knowledge base root
**Expected:** Only `.gitignore` allowed as hidden file at root. Heartbeat artifacts should live in `.hermes/` or `.openclaw/`.
**Suggested fix:** Move to `.hermes/.last_heartbeat` (or `.openclaw/.last_heartbeat`) and update any process that writes to this path.

---

## Clean zones (verified compliant)

| Zone | Status |
|---|---|
| Root structure | ✅ All 8 folders compliant, all 9 whitelisted files present |
| `context/` | ✅ Exactly 2 files (`context.md`, `USER.md`), no subfolders |
| `raw/` | ✅ 6 subfolders all whitelisted, all have index files, no root orphans |
| `wiki/meta/` | ✅ 3 required files present (`format-spec.md`, `folder-structure.md`, `index-spec.md`) |
| `wiki/sources/` | ✅ All files match `src_<slug>.md` pattern |
| `wiki/concepts/` | ✅ All files match `<slug>.md` pattern |
| `wiki/tag/` | ✅ All files match naming convention |
| `wiki/topic/` | ✅ All files match naming convention |
| `wiki/drafts/` | ✅ All files match naming convention |
| `wiki/reviews/` | ✅ All active reports use canonical `YYYY-MM-DD_<type>-report.md` format |
| `wiki/reviews/archive/` | ✅ All archived in `YYYY-MM/` subfolders with correct format |
| `scripts/` | ✅ Present, no violations |
| `.openclaw/`, `.hermes/` | ✅ Skipped (agent runtime zones) |
| Known orphans | ✅ `RAW_BACKLOG.md`, `MEMORY.md`, `search/`, `state/`, `temp_content/`, `memory/` — all absent |
| Heartbeat leaks | ✅ `raw/.last_heartbeat` absent, `wiki/reviews/HEARTBEAT.md` absent |

---

## Notes

- This is the first run where **0 naming convention violations** were detected across all active content zones (raw/, wiki/concepts/, wiki/sources/, wiki/tag/, wiki/topic/, wiki/drafts/, wiki/reviews/). The `.last_heartbeat` at root is the sole remaining issue — a minor orphan from what appears to be a background process writing to the wrong location.
- The previous batch's 4 `-v2` duplicate reports in `archive/2026-06/` are the only known technical debt — carried over from prior reports, approved by Julius on 2026-06-22.
