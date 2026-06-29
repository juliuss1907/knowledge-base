# Hygiene Inspection — 2026-06-28

**Status:** approved
**Approved by:** Julius — 2026-06-29
**Issues found:** 2
**Created:** 2026-06-28 23:30:00 +07
**Validator:** hygiene-inspector

**Paths checked:** 51,528

---

## Issue 1: Repos file naming — missing owner segment

**Path:** `raw/repos/2026-06-27_personal-mba-generator-skill.md`
**Severity:** WARNING
**Category:** Naming
**Issue:** Repos file naming: expected YYYY-MM-DD_\<owner\>_\<repo\>.md — current filename has only a single slug segment
**Current:** `2026-06-27_personal-mba-generator-skill.md`
**Expected:** `2026-06-27_<owner>_<repo>.md` (e.g. `2026-06-27_aiskilloftheweek_personal-mba-generator-skill.md`)
**Suggested fix:** Rename to `2026-06-27_aiskilloftheweek_personal-mba-generator-skill.md`

---

## Issue 2: Repos file naming — missing owner segment

**Path:** `raw/repos/2026-06-27_sop-writer-skill.md`
**Severity:** WARNING
**Category:** Naming
**Issue:** Repos file naming: expected YYYY-MM-DD_\<owner\>_\<repo\>.md — current filename has only a single slug segment
**Current:** `2026-06-27_sop-writer-skill.md`
**Expected:** `2026-06-27_<owner>_<repo>.md` (e.g. `2026-06-27_aiskilloftheweek_sop-writer-skill.md`)
**Suggested fix:** Rename to `2026-06-27_aiskilloftheweek_sop-writer-skill.md`

---

## Summary

| Severity | Count |
|---|---|
| ERROR | 0 |
| WARNING | 2 |
| INFO | 0 |
| **Total** | **2** |

**Structural health:** Excellent. 51,528 paths checked, only 2 WARNING-level naming issues.

**Delta from 2026-06-27 (pending):**
- ✅ `wiki/reviews/HEARTBEAT.md`: **resolved** — HEARTBEAT leak has been fixed. No HEARTBEAT.md in wiki/reviews/ on this run. Root-level symlink (`HEARTBEAT.md → .openclaw/HEARTBEAT.md`) is correct.
- ✅ `memory/` root folder: not present (resolved in prior run)
- ✅ `state/` root folder: not present (resolved in prior run)
- ✅ `wiki/reviews/_approval-log.md`: not present (resolved in prior run)
- ✅ `raw/papers/` naming: all compliant
- ✅ `wiki/drafts/`: clean, no .bak/.tmp files, no backup subfolders
- ⚠️ NEW: 2 `raw/repos/` files missing owner segment in filename (both ingested 2026-06-27)

**Structural zones all clean:**
- Root level: whitelist-compliant (9 symlinks/files + 4 agent homes + 4 folders)
- `context/`: exactly 2 files (context.md, USER.md)
- `raw/`: 6 subfolders, all index files present, no root-level files
- `wiki/meta/`: exactly 3 files (format-spec.md, folder-structure.md, index-spec.md)
- `wiki/sources/`: all `src_*` prefixed
- `wiki/concepts/`: all lowercase-hyphen slugs
- `wiki/tag/` + `wiki/topic/`: auto-generated, compliant
- `wiki/drafts/`: 4 markdown files, all lowercase-hyphen
- `wiki/reviews/`: active reports all follow `YYYY-MM-DD_<type>-report.md`
- `wiki/reviews/archive/`: all in `YYYY-MM/` subfolders
- `.hermes/` + `.openclaw/`: agent runtime workspaces, no user content leakage
