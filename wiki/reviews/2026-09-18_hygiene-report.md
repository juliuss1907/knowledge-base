# Hygiene Inspection — 2026-09-18

**Status:** pending
**Issues found:** 60 (4 ERROR + 56 WARNING + 0 INFO)
**Created:** 2026-09-18 23:33:00
**Validator:** hygiene-inspector

**Paths checked:** 233812

---

## Issue 1: DREAMS.md — root orphan

**Path:** DREAMS.md
**Severity:** ERROR
**Category:** Path
**Issue:** File not in root whitelist
**Current:** DREAMS.md (8.7K, git-tracked, OpenClaw dreaming artifact)
**Expected:** Only AGENTS.md, TAGS.md, README.md, knowledge-base.md, symlinks, .gitignore allowed
**Suggested fix:** CARRY-FORWARD — KHÔNG xóa. Giữ theo ghi chú duyệt; Fix Agent redirect writing process output.

---

## Issue 2: memory/ — recurring root folder

**Path:** memory/
**Severity:** ERROR
**Category:** Orphan
**Issue:** Recurring root folder not in whitelist: memory/
**Current:** memory/ — 41 files (+4 so với 09-17: 3 dreaming 09-18 + 1 session-corpus 09-17)
**Expected:** Migrated to .openclaw/memory/ since v1.2. A process writes to root memory/ instead of .openclaw/memory/.
**Suggested fix:** CARRY-FORWARD — KHÔNG xóa. Fix Agent redirect writing process output path.

---

## Issue 3: Migration marker — root orphan

**Path:** openclaw-workspace-state.json.migrated.43c9aa3dead1239e131cfd1ddf1a21fed91f1640ba72aeaf94714c3a31d1c72b.e79d1c6c-d9cd-4f3c-b9eb-65b970017373
**Severity:** ERROR
**Category:** Path
**Issue:** File not in root whitelist — migration marker from OpenClaw runtime
**Current:** 69 bytes, git-tracked since b5e519fc, .gitignore wildcard guard needed
**Expected:** Should be in .openclaw/ or cleaned up; .gitignore needs `openclaw-workspace-state.json.migrated.*` pattern
**Suggested fix:** CARRY-FORWARD — Fix Agent: `.gitignore` thêm wildcard pattern + `git rm --cached` marker + commit

---

## Issue 4: wiki/HEARTBEAT.md — broken symlink

**Path:** wiki/HEARTBEAT.md
**Severity:** ERROR
**Category:** Orphan
**Issue:** HEARTBEAT.md leaked into wiki/ root (recurring process leak)
**Current:** Broken symlink → ../../.openclaw/HEARTBEAT.md (target exists but dangling on some sync cycles)
**Expected:** HEARTBEAT.md belongs in .hermes/ or .openclaw/
**Suggested fix:** CARRY-FORWARD — Process-level fix: sync tool mirror creates symlink into wiki/; fix writing process

---

## Issue 5–20: memory/ sub-files (WARNING, grouped)

**Path:** memory/.dreams/session-corpus/ (10 files, 09-08→09-17), memory/dreaming/{deep,light,rem}/ (30 files, 09-09→09-18), memory/2026-09-17.md (1 file)
**Severity:** WARNING
**Category:** Path
**Issue:** 41 files inside root memory/ — sub-paths của Issue 2
**Current:** 41 files total (+4 so với 09-17: session-corpus 09-17.txt + 3 dreaming 09-18)
**Expected:** memory/ should not exist at root; files belong in .openclaw/memory/
**Suggested fix:** CARRY-FORWARD — KHÔNG xóa individual files; Fix Agent redirect writing process output

---

## Archival note: archive backup files (15 WARNING, truncated)

15 files trong `wiki/reviews/archive/` bị scanner đánh dấu WARNING naming do file backup (non-report artifacts) match regex report naming. Đây là false positive đã biết — cần update scan script exclusion cho backup files trong archive.

---

## Carry-forward summary

| Issue | Since | Runs |
|---|---|---|
| DREAMS.md root orphan | 09-09 | 19+ |
| memory/ root folder | 07-03 | 22+ |
| Migration marker | 09-08 | 11 |
| wiki/HEARTBEAT.md | 08-26 | 23+ |

**0 ISSUE RESOLVED vs 09-17** — all 4 ERROR carry-forward.

**Change vs 09-17:** memory/ tăng 37→41 (+4: 3 dreaming 09-18 + 1 session-corpus 09-17). Machine detection count: 57→60 (+3 new memory files; archive false positives stable at 15). Paths checked: 1753→233812 (full scan vs previous scoped scan).

**Không có [SYSTEMATIC VIOLATION] mới.** Không [SPEC CONFLICT] mới. Không [STRUCTURE CHANGE].
