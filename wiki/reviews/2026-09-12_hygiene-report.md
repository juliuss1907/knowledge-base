# Hygiene Inspection — 2026-09-12

**Status:** pending
**Issues found:** 35 (4 ERROR + 31 WARNING)
**Created:** 2026-09-12 23:32:13
**Validator:** hygiene-inspector

**Paths checked:** 233,688

---

## Changes vs 09-11

**RESOLVED:** Repos naming violations (6 files `MengTo`/`PostHog` casing + related warnings) — FIXED since 09-11 run. All 8 repos files now use lowercase owner segments. `[SYSTEMATIC VIOLATION]` from 08-31 — **RESOLVED**.

**NEW:** 3 dreaming files dated 09-12 appeared in `memory/dreaming/{deep,light,rem}/`. OpenClaw dreaming pipeline continues writing to root `memory/` instead of `.openclaw/memory/`. `memory/` sub-file count: 12 (09-11) → 16 (09-12).

**UNCHANGED:** All 4 ERRORs carry-forward (DREAMS.md, memory/ folder, migration marker, wiki/HEARTBEAT.md broken symlink). 15 archive backup false positives unchanged. Repos naming violations resolved (-6 WARNING).

**Net change:** +4 WARNING (31 vs 27 on 09-11) despite repos fix (-6): +4 new dreaming files > repos resolution.

---

## Issue 1: DREAMS.md root orphan

**Path:** `DREAMS.md`
**Severity:** ERROR
**Category:** Path
**Issue:** File not in root whitelist — OpenClaw dreaming artifact at KB root
**Current:** `DREAMS.md` (3915 bytes, git-tracked, mtime 09-12 03:00)
**Expected:** Only AGENTS.md, TAGS.md, README.md, knowledge-base.md, symlinks, .gitignore allowed
**Suggested fix:** `git rm DREAMS.md` + commit (or move to `.openclaw/`)
**Status:** CARRY-FORWARD từ 09-09. Git-tracked: `100644 4086b7a`. Latest write 09-12 03:00 — dreaming pipeline still active.

---

## Issue 2: memory/ root folder (recurring)

**Path:** `memory/`
**Severity:** ERROR
**Category:** Orphan
**Issue:** Recurring root folder not in whitelist
**Current:** `memory/` with 16 files across `.dreams/session-corpus/`, `dreaming/{deep,light,rem}/` — **+3 files since 09-11** (09-12 dreaming logs)
**Expected:** Folder migrated to `.openclaw/memory/` in v1.2
**Suggested fix:** `git rm -r memory/` + commit; fix writing process output path
**Status:** CARRY-FORWARD. Process continues writing dreaming content to root `memory/` (last write 09-12 03:00). Flagged since 07-03. New files: `dreaming/deep/2026-09-12.md`, `dreaming/light/2026-09-12.md`, `dreaming/rem/2026-09-12.md`.

---

## Issue 3: Migration marker (git-tracked)

**Path:** `openclaw-workspace-state.json.migrated.43c9aa3dead...`
**Severity:** ERROR
**Category:** Path
**Issue:** File not in root whitelist — migration marker from 09-08 OpenClaw runtime self-migration
**Current:** 69 bytes, git-tracked: `100644 a0105ac`, mtime 09-08 20:42
**Expected:** Not gitignored; marker persists in repo since commit `b5e519fc`
**Suggested fix:** `.gitignore` add `openclaw-workspace-state.json.migrated.*` + `git rm --cached` + commit
**Status:** CARRY-FORWARD từ 09-08 addendum (lần 5). Root `openclaw-workspace-state.json` itself absent 14+ runs streak (resolved by runtime migration). Marker remains git-tracked.

---

## Issue 4: wiki/HEARTBEAT.md broken symlink

**Path:** `wiki/HEARTBEAT.md`
**Severity:** ERROR
**Category:** Orphan
**Issue:** HEARTBEAT.md leaked into wiki/ root — broken symlink (target `../../.openclaw/HEARTBEAT.md` does not resolve from wiki/)
**Current:** Broken symbolic link → `../../.openclaw/HEARTBEAT.md`
**Expected:** HEARTBEAT.md belongs in `.hermes/` or `.openclaw/`; file deletion is transient
**Suggested fix:** Process-level fix for the writing process; then delete
**Status:** CARRY-FORWARD lần 13 liên tiếp (08-26→09-12). `.openclaw/HEARTBEAT.md` exists (664 permissions) but symlink path resolves incorrectly from `wiki/`.

---

## Issue 5-20: memory/ sub-files (16 WARNING)

**Severity:** WARNING
**Category:** Path
**Issue:** Files inside root `memory/` — unclassified paths (sub-items of Issue 2)
**Files:** `.dreams/session-corpus/{2026-09-08..11}.txt` (4), `dreaming/deep/{2026-09-09..12}.md` (4), `dreaming/light/{2026-09-09..12}.md` (4), `dreaming/rem/{2026-09-09..12}.md` (4)
**Status:** Sub-items of Issue 2. +3 files since 09-11 (09-12 dreaming logs). 16 total (was 12 on 09-11).

---

## Truncated WARNINGs (15 additional)

15 backup files in `wiki/reviews/archive/2026-09/` flagged as "Archived report naming" — false positives (non-report artifacts: Fix Agent pre-rename backups `*-backup-YYYY-MM-DD.md`). Same 15 files flagged since 09-09. Scanner treats them as report files but they are draft/source backups relocated by Fix Agent. **Recommendation:** Update scan script to exclude non-report files from archive naming check (or move backups to a dedicated non-archive location).

---

## Resolved since 09-11

1. **repos naming violations** (6 files) — FIXED: All repos files now use `<owner>_<repo>` two-segment lowercase format. `[SYSTEMATIC VIOLATION]` from 08-31 is RESOLVED. Fix Agent applied lowercase owner rename.

---

## Actions needed

1. **Fix Agent:** `git rm DREAMS.md` + commit (Dreaming pipeline still active — may recreate)
2. **Fix Agent:** `git rm -r memory/` + commit; root cause = OpenClaw dreaming process writes to root `memory/` instead of `.openclaw/memory/`
3. **Fix Agent:** `.gitignore` add `openclaw-workspace-state.json.migrated.*` + `git rm --cached` the marker + commit (git-tracked since `b5e519fc`)
4. **Process fix needed:** `wiki/HEARTBEAT.md` broken symlink — 13th consecutive run. File deletion is transient if writer still active; identify and fix the sync tool mirroring root HEARTBEAT into wiki/
5. **Optional:** Update scan script to exclude non-report backup files from `wiki/reviews/archive/` naming check

**Tin tốt:** `openclaw-workspace-state.json` gốc vắng mặt streak 14+; repos naming RESOLVED; 0 empty dir; 0 new wiki naming violations; pipeline active — 272 wiki files changed, 2 raw files ingested since 09-11.
