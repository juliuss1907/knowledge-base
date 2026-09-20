# Hygiene Inspection — 2026-09-20

**Status:** pending
**Issues found:** 68 (4 ERROR + 64 WARNING + 0 INFO)
**Created:** 2026-09-20 23:30:50
**Validator:** hygiene-inspector

**Paths checked:** 233845

---

## Issue 1: DREAMS.md — root orphan (carry-forward)

**Path:** DREAMS.md
**Severity:** ERROR
**Category:** Path
**Issue:** File not in root whitelist
**Current:** DREAMS.md (8.7K, git-tracked, OpenClaw dreaming artifact)
**Expected:** Only AGENTS.md, TAGS.md, README.md, knowledge-base.md, symlinks, .gitignore allowed
**Suggested fix:** CARRY-FORWARD — KHÔNG xóa. Giữ theo ghi chú duyệt; Fix Agent redirect writing process output. Lần 22 liên tiếp (09-09→09-20).

---

## Issue 2: memory/ — recurring root folder (carry-forward)

**Path:** memory/
**Severity:** ERROR
**Category:** Orphan
**Issue:** Recurring root folder not in whitelist: memory/
**Current:** memory/ — 49 files (+4 so với 09-19: 3 dreaming 09-20 deep/light/rem + 1 session-corpus 09-19)
**Expected:** Migrated to .openclaw/memory/ since v1.2. A process writes to root memory/ instead of .openclaw/memory/.
**Suggested fix:** CARRY-FORWARD — KHÔNG xóa. Fix Agent redirect writing process output path. Lần 24+ liên tiếp từ 07-03.

---

## Issue 3: Migration marker — root orphan (carry-forward)

**Path:** openclaw-workspace-state.json.migrated.43c9aa3dead1239e131cfd1ddf1a21fed91f1640ba72aeaf94714c3a31d1c72b.e79d1c6c-d9cd-4f3c-b9eb-65b970017373
**Severity:** ERROR
**Category:** Path
**Issue:** File not in root whitelist — migration marker from OpenClaw runtime
**Current:** 69 bytes, git-tracked since b5e519fc, .gitignore wildcard guard needed
**Expected:** Should be in .openclaw/ or cleaned up; .gitignore needs `openclaw-workspace-state.json.migrated.*` pattern
**Suggested fix:** CARRY-FORWARD — Fix Agent: `.gitignore` thêm wildcard pattern + `git rm --cached` marker + commit. Lần 13 từ 09-08 addendum.

---

## Issue 4: wiki/HEARTBEAT.md — broken symlink (carry-forward)

**Path:** wiki/HEARTBEAT.md
**Severity:** ERROR
**Category:** Orphan
**Issue:** HEARTBEAT.md leaked into wiki/ root (recurring process leak)
**Current:** Broken symlink → ../../.openclaw/HEARTBEAT.md
**Expected:** HEARTBEAT.md belongs in .hermes/ or .openclaw/
**Suggested fix:** CARRY-FORWARD — Process-level fix: sync tool mirror creates symlink into wiki/; fix writing process. Lần 25+ liên tiếp (08-26→09-20).

---

## Issue 5–20: memory/ sub-files (WARNING, grouped)

**Path:** memory/.dreams/session-corpus/ (12 files, 09-08→09-19), memory/dreaming/deep/ (6 files, 09-09→09-20), memory/dreaming/light/ and memory/dreaming/rem/ (+3 files 09-20), memory/2026-09-17.md (1 file)
**Severity:** WARNING
**Category:** Path
**Issue:** 49 files inside root memory/ — sub-paths của Issue 2
**Current:** 49 files total (+4 so với 09-19: session-corpus 09-19 + dreaming deep/light/rem 09-20)
**Expected:** memory/ should not exist at root; files belong in .openclaw/memory/
**Suggested fix:** CARRY-FORWARD — KHÔNG xóa individual files; Fix Agent redirect writing process output

---

## Carry-forward summary

| Issue | Since | Runs |
|---|---|---|
| DREAMS.md root orphan | 09-09 | 22 |
| memory/ root folder | 07-03 | 24+ |
| Migration marker | 09-08 | 13 |
| wiki/HEARTBEAT.md | 08-26 | 25+ |

**0 ISSUE RESOLVED vs 09-19** — all 4 ERROR carry-forward.

**Change vs 09-19:** memory/ tăng 45→49 (+4: 3 dreaming 09-20 deep/light/rem + 1 session-corpus 09-19). Machine detection count: 64→68 (+4 new memory files; archive false positives stable at 15). Paths checked: 233822→233845 (+23, expected drift from new raw ingest files).

**Pipeline activity:** 2 articles + 4 videos ingested raw/ 09-19→09-20 (properly named); 2 format reports + 1 output report written. No new naming violations.

**Không có [SYSTEMATIC VIOLATION] mới.** Không [SPEC CONFLICT] mới. Không [STRUCTURE CHANGE].
