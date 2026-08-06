# Hygiene Inspection — 2026-08-05

**Status:** approved
**Approved by:** Julius
**Approved date:** 2026-08-05
**Issues found:** 5 (2 ERROR + 2 WARNING + 1 INFO)
**Created:** 2026-08-05 23:30:00
**Validator:** hygiene-inspector

**Paths checked:** 53,487

---

## Issue 1: Recurring root folder — memory/

**Path:** memory/
**Severity:** ERROR
**Category:** Orphan
**Issue:** Recurring root folder not in whitelist. `memory/` has RETURNED after being absent on 08-03 and 08-04. Contains `memory/2026-08-05.md` (2.6KB, created 08:35 today).
**Current:** `memory/` directory at KB root containing `memory/2026-08-05.md`
**Expected:** Memory logs must go to `.openclaw/memory/` per folder-structure.md v1.2 (change log: "Migrated `memory/` from root to `.openclaw/memory/`"). A process writes memory logs to the old path.
**Suggested fix:** Move `memory/2026-08-05.md` → `.openclaw/memory/`, then `rmdir memory/`. Fix the writing process to target `.openclaw/memory/` instead of `memory/`.

---

## Issue 2: Recurring root folder — state/

**Path:** state/
**Severity:** ERROR
**Category:** Orphan
**Issue:** Recurring root folder not in whitelist. 3rd consecutive run flagged (08-03, 08-04, 08-05). Recreated 2026-08-02 after ~5 weeks absent. Currently empty directory.
**Current:** `state/` (empty directory, recreated ~2026-08-02)
**Expected:** No `state/` at KB root. If a state directory is needed, it belongs inside `.hermes/` or `.openclaw/`.
**Suggested fix:** `rmdir state/`. Identify the process recreating it ~monthly.

---

## Issue 3: Orphan file inside memory/ folder

**Path:** memory/2026-08-05.md
**Severity:** WARNING
**Category:** Path
**Issue:** Path not classified by any rule — file lives inside unwhitelisted `memory/` root folder. Content is today's memory log that should be in `.openclaw/memory/`.
**Current:** `memory/2026-08-05.md` (2.6KB, written 08:35 today)
**Expected:** Memory logs belong in `.openclaw/memory/`
**Suggested fix:** Move to `.openclaw/memory/2026-08-05.md`. Then `rmdir memory/`.

---

## Issue 4: Leftover index file from migration — raw/websites/tools.md

**Path:** raw/websites/tools.md
**Severity:** WARNING
**Category:** Naming
**Issue:** Leftover index file from `raw/tools/` migration by Fix Agent (2026-08-01 batch). 4th consecutive run flagged (08-01, 08-03, 08-04, 08-05). File is 686 bytes — contains 2 items already tracked in `raw/websites/websites.md`. Does not follow `YYYY-MM-DD_<slug>.md` naming convention.
**Current:** `raw/websites/tools.md`
**Expected:** `YYYY-MM-DD_<slug>.md` naming convention. File should be deleted after verifying items are in `websites.md`.
**Suggested fix:** Verify items are in `raw/websites/websites.md`, then delete `raw/websites/tools.md`. Update migration procedure to handle leftover index files.

---

## Issue 5: Empty directory — state/

**Path:** state/
**Severity:** INFO
**Category:** Orphan
**Issue:** Empty directory at KB root. Companion info-level flag for the ERROR above (Issue 2).
**Current:** `state/` (empty)
**Expected:** Non-empty directory or removed
**Suggested fix:** `rmdir state/`

---

## Delta from 2026-08-04

| Change | Detail |
|---|---|
| **+2 issues** | 08-04 had 3 issues (1E+1W+1I); today has 5 (2E+2W+1I) |
| **⚠️ REGRESSION** | `memory/` root folder returned after being absent on 08-03 and 08-04. Contains today's memory log (2026-08-05.md). |
| **↔️ Persisting** | `state/` root folder: 3rd consecutive run (08-03, 08-04, 08-05). Still empty. |
| **↔️ Persisting** | `raw/websites/tools.md`: 4th consecutive run (08-01, 08-03, 08-04, 08-05). Fix Agent hasn't actioned yet. |
| **✅ Resolved** | No HEARTBEAT leaks. No naming violations in `raw/<type>/` or `wiki/` zones. KB otherwise clean. |

---

## Notes

- **`memory/` regression is process-level**: same root cause as flagged since 07-03 — a process writes to `memory/` instead of `.openclaw/memory/`. File deletion is transient; the writing process must be updated.
- **`state/` empty directory**: recreated ~2026-08-02. Process identity unknown. Recommend Julius investigate.
- **`raw/websites/tools.md`**: now on its 4th run without Fix Agent action. Low priority — no new content, just a leftover rename artifact.
- **KB otherwise clean**: 53,487 paths scanned. All `raw/<type>/` content files, `wiki/concepts/`, `wiki/sources/`, `wiki/tag/`, `wiki/topic/`, `wiki/reviews/` active reports — all compliant. No new orphans, no naming drift, no structural violations anywhere else.
