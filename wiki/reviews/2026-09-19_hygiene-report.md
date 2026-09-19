# Hygiene Inspection — 2026-09-19

**Status:** pending
**Issues found:** 64 (4 ERROR + 60 WARNING + 0 INFO)
**Created:** 2026-09-19 23:30:20
**Validator:** hygiene-inspector

**Paths checked:** 233822

---

## Issue 1: DREAMS.md — root orphan (carry-forward)

**Path:** DREAMS.md
**Severity:** ERROR
**Category:** Path
**Issue:** File not in root whitelist
**Current:** DREAMS.md (8.7K, git-tracked, OpenClaw dreaming artifact)
**Expected:** Only AGENTS.md, TAGS.md, README.md, knowledge-base.md, symlinks, .gitignore allowed
**Suggested fix:** CARRY-FORWARD — KHÔNG xóa. Giữ theo ghi chú duyệt; Fix Agent redirect writing process output. Lần 21 liên tiếp (09-09→09-19).

---

## Issue 2: memory/ — recurring root folder (carry-forward)

**Path:** memory/
**Severity:** ERROR
**Category:** Orphan
**Issue:** Recurring root folder not in whitelist: memory/
**Current:** memory/ — 45 files (+4 so với 09-18: 3 dreaming 09-19 + 1 session-corpus 09-18)
**Expected:** Migrated to .openclaw/memory/ since v1.2. A process writes to root memory/ instead of .openclaw/memory/.
**Suggested fix:** CARRY-FORWARD — KHÔNG xóa. Fix Agent redirect writing process output path. Lần 23+ liên tiếp từ 07-03.

---

## Issue 3: Migration marker — root orphan (carry-forward)

**Path:** openclaw-workspace-state.json.migrated.43c9aa3dead1239e131cfd1ddf1a21fed91f1640ba72aeaf94714c3a31d1c72b.e79d1c6c-d9cd-4f3c-b9eb-65b970017373
**Severity:** ERROR
**Category:** Path
**Issue:** File not in root whitelist — migration marker from OpenClaw runtime
**Current:** 69 bytes, git-tracked since b5e519fc, .gitignore wildcard guard needed
**Expected:** Should be in .openclaw/ or cleaned up; .gitignore needs `openclaw-workspace-state.json.migrated.*` pattern
**Suggested fix:** CARRY-FORWARD — Fix Agent: `.gitignore` thêm wildcard pattern + `git rm --cached` marker + commit. Lần 12 từ 09-08 addendum.

---

## Issue 4: wiki/HEARTBEAT.md — broken symlink (carry-forward)

**Path:** wiki/HEARTBEAT.md
**Severity:** ERROR
**Category:** Orphan
**Issue:** HEARTBEAT.md leaked into wiki/ root (recurring process leak)
**Current:** Broken symlink → ../../.openclaw/HEARTBEAT.md
**Expected:** HEARTBEAT.md belongs in .hermes/ or .openclaw/
**Suggested fix:** CARRY-FORWARD — Process-level fix: sync tool mirror creates symlink into wiki/; fix writing process. Lần 24+ liên tiếp (08-26→09-19).

---

## Issue 5–20: memory/ sub-files (WARNING, grouped)

**Path:** memory/.dreams/session-corpus/ (12 files, 09-08→09-18), memory/dreaming/deep/ (5 files, 09-09→09-19), memory/dreaming/light/ and memory/dreaming/rem/ (+3 files 09-19), memory/2026-09-17.md (1 file)
**Severity:** WARNING
**Category:** Path
**Issue:** 45 files inside root memory/ — sub-paths của Issue 2
**Current:** 45 files total (+4 so với 09-18: session-corpus 09-18 + dreaming deep/light/rem 09-19)
**Expected:** memory/ should not exist at root; files belong in .openclaw/memory/
**Suggested fix:** CARRY-FORWARD — KHÔNG xóa individual files; Fix Agent redirect writing process output

---

## Carry-forward summary

| Issue | Since | Runs |
|---|---|---|
| DREAMS.md root orphan | 09-09 | 21 |
| memory/ root folder | 07-03 | 23+ |
| Migration marker | 09-08 | 12 |
| wiki/HEARTBEAT.md | 08-26 | 24+ |

**0 ISSUE RESOLVED vs 09-18** — all 4 ERROR carry-forward.

**Change vs 09-18:** memory/ tăng 41→45 (+4: 3 dreaming 09-19 deep/light/rem + 1 session-corpus 09-18). Machine detection count: 60→64 (+4 new memory files; archive false positives stable at ~15). Paths checked: 233812→233822 (+10, expected drift from new raw ingest files).

**Pipeline activity:** 2 articles + 2 videos ingested raw/ 09-19 (properly named); 1 format report written. No new naming violations.

**Không có [SYSTEMATIC VIOLATION] mới.** Không [SPEC CONFLICT] mới. Không [STRUCTURE CHANGE].
