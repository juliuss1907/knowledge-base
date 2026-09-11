# Hygiene Inspection — 2026-09-11

**Status:** pending
**Issues found:** 31 (4 ERROR + 27 WARNING)
**Created:** 2026-09-11 23:31:00
**Validator:** hygiene-inspector

**Paths checked:** 233669

---

## Issue 1: Known root orphan — DREAMS.md

**Path:** `DREAMS.md`
**Severity:** ERROR
**Category:** Orphan
**Issue:** Known root orphan: DREAMS.md — OpenClaw dreaming artifact
**Current:** DREAMS.md at KB root, git-tracked (commit 261ce5f2)
**Expected:** Should be in `.openclaw/` or `.hermes/`
**Suggested fix:** `git rm DREAMS.md` + commit (hoặc move về `.openclaw/`)
**Carry-forward:** Lần 3 liên tiếp (09-09 → 09-11). Chưa Fix Agent action.

---

## Issue 2: Recurring root folder — memory/

**Path:** `memory/`
**Severity:** ERROR
**Category:** Orphan
**Issue:** Recurring root folder not in whitelist: memory/
**Current:** memory/ populated with dreaming content (12 files: .dreams/session-corpus/ 3 txt + dreaming/{deep,light,rem} 9 md)
**Expected:** Old folder migrated to `.openclaw/memory/` in v1.2
**Suggested fix:** `git rm -r memory/` + commit; redirect writing process output path
**Carry-forward:** Lần 3 liên tiếp (09-09 → 09-11). **+3 files 09-11** (deep/light/rem dreaming logs cho ngày 09-11). OpenClaw pipeline tiếp tục viết vào root `memory/`.

---

## Issue 3: Migration marker .migrated.* at root

**Path:** `openclaw-workspace-state.json.migrated.43c9aa3dead1239e131cfd1ddf1a21fed91f1640ba72aeaf94714c3a31d1c72b.e79d1c6c-d9cd-4f3c-b9eb-65b970017373`
**Severity:** ERROR
**Category:** Path
**Issue:** File not in root whitelist — migration marker artifact
**Current:** Marker file at root, git-tracked (commit `b5e519fc`)
**Expected:** `.gitignore` pattern `openclaw-workspace-state.json.migrated.*` + `git rm --cached`
**Suggested fix:** `.gitignore` thêm wildcard pattern + `git rm --cached` marker + commit
**Carry-forward:** Lần 4 liên tiếp (09-08 addendum → 09-11). Chưa Fix Agent action.

---

## Issue 4: HEARTBEAT.md leaked into wiki/ root

**Path:** `wiki/HEARTBEAT.md`
**Severity:** ERROR
**Category:** Orphan
**Issue:** HEARTBEAT.md leaked into wiki/ root — recurring process leak
**Current:** wiki/HEARTBEAT.md (broken symlink hoặc regular file)
**Expected:** HEARTBEAT.md belongs in `.hermes/` or `.openclaw/`
**Suggested fix:** Identify and fix the process writing HEARTBEAT.md to wiki/; then delete this file
**Carry-forward:** Lần 12 liên tiếp (08-26 → 09-11). Process-level leak — file deletion là transient.

---

## Issue 5-16: memory/ sub-files (12 WARNINGs)

**Path:** `memory/.dreams/session-corpus/2026-09-{08,09,10}.txt`, `memory/dreaming/{deep,light,rem}/2026-09-{09,10,11}.md`
**Severity:** WARNING
**Category:** Path
**Issue:** Path not classified by any rule — sub-paths of root `memory/` folder (Issue 2)
**Current:** 12 files inside root `memory/` (OpenClaw dreaming pipeline output)
**Expected:** Content should be in `.openclaw/memory/` or removed
**Suggested fix:** Resolved by fixing Issue 2 (remove `memory/` root folder)
**Note:** +3 files so với 09-10 (deep/light/rem dreaming logs 09-11 mới nhất)

---

## Issue 17-27: Archive backup files (11 WARNINGs)

**Path:** `wiki/reviews/archive/2026-09/*-backup-2026-09-01.md` (and similar)
**Severity:** WARNING
**Category:** Naming
**Issue:** Archived report naming — scanner applies report naming convention to non-report backup files
**Current:** Fix Agent pre-rename backups in archive zone
**Expected:** N/A — false positive (backup artifacts, not reports)
**Suggested fix:** Update scan script to exclude non-report files from archive naming check
**Note:** Known false positive since 09-09. These are Fix Agent backup artifacts moved to archive — not hygiene violations.

---

## Summary

**100% carry-forward từ 09-10 — 0 issue mới resolved.**

| Issue | Status | Runs |
|---|---|---|
| DREAMS.md root orphan | CARRY (lần 3) | 09-09 → 09-11 |
| memory/ root folder | CARRY (lần 3, +3 files) | 09-09 → 09-11 |
| Migration marker .migrated.* | CARRY (lần 4) | 09-08 → 09-11 |
| wiki/HEARTBEAT.md | CARRY (lần 12) | 08-26 → 09-11 |

**Tin tốt:**
- `openclaw-workspace-state.json` gốc vắng mặt streak 15+ (08-24 → 09-11)
- 0 new naming violations trong wiki/ hoặc raw/
- 0 empty directories
- Pipeline active — 275 files changed since 09-10 (Compile Agent quay lại)

**Không [SYSTEMATIC VIOLATION] mới.** KHÔNG re-escalate các orphan đã biết.

---

## Actions needed

1. **Fix Agent:** `git rm DREAMS.md` + commit (hoặc move về `.openclaw/`)
2. **Fix Agent:** `git rm -r memory/` + commit; redirect OpenClaw dreaming pipeline output path
3. **Fix Agent:** `.gitignore` thêm `openclaw-workspace-state.json.migrated.*` + `git rm --cached` marker + commit
4. **Process-level fix:** `wiki/HEARTBEAT.md` — xác định process tạo symlink/file HEARTBEAT vào wiki/, redirect output
5. **Optional:** Update scan script archive exclusion cho non-report backup files
