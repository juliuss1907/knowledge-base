# Hygiene Inspection — 2026-09-21

**Status:** pending
**Issues found:** 72 (4 ERROR + 68 WARNING)
**Created:** 2026-09-21 23:31:22
**Validator:** hygiene-inspector

**Paths checked:** 233868

---

## ISSUE E1: DREAMS.md root orphan (CARRY-FORWARD)

**Path:** `DREAMS.md`
**Severity:** ERROR
**Category:** Path
**Issue:** Known root orphan — file not in root whitelist
**Current:** `DREAMS.md` at KB root (600 bytes, git-tracked)
**Expected:** Only AGENTS.md, TAGS.md, README.md, knowledge-base.md, symlinks, .gitignore allowed
**Suggested fix:** KHÔNG xóa — carry-forward từ 09-09 (lần 23 liên tiếp). OpenClaw dreaming artifact, git-tracked. Chờ process-level fix.
**Lần:** 23 liên tiếp (09-09→09-21)

---

## ISSUE E2: memory/ root folder (CARRY-FORWARD)

**Path:** `memory/`
**Severity:** ERROR
**Category:** Orphan
**Issue:** Recurring root folder not in whitelist
**Current:** `memory/` tại root — 53 sub-files (40 dreaming + 13 session-corpus/logs)
**Expected:** Migrated to .openclaw/memory/ in v1.2
**Suggested fix:** KHÔNG xóa — carry-forward từ 07-03 (lần 27+ liên tiếp). OpenClaw dreaming pipeline tiếp tục viết daily. +4 files since 09-20 (session-corpus 09-20 + dreaming deep/light/rem 09-21).
**Lần:** 27+ liên tiếp (07-03→09-21)

**memory/ breakdown:**
- dreaming/deep/ = 13 files (lần 22 liên tiếp)
- dreaming/light/ = 13 files (lần 22 liên tiếp)
- dreaming/rem/ = 13 files (lần 22 liên tiếp)
- .dreams/session-corpus/ = 13 files (lần 14 liên tiếp)
- 2026-09-17.md = 1 file (session log, static since 09-17)

---

## ISSUE E3: Migration marker .migrated.* (CARRY-FORWARD)

**Path:** `openclaw-workspace-state.json.migrated.43c9aa3dead1239e131cfd1ddf1a21fed91f1640ba72aeaf94714c3a31d1c72b.e79d1c6c-d9cd-4f3c-b9eb-65b970017373`
**Severity:** ERROR
**Category:** Path
**Issue:** Known root orphan — migration marker file
**Current:** Marker at root (69 bytes, git-tracked since `b5e519fc`)
**Expected:** Should be gitignored and git-removed
**Suggested fix:** Fix Agent: `.gitignore` thêm `openclaw-workspace-state.json.migrated.*` + `git rm --cached` marker + commit. Carry-forward từ 09-08 addendum (lần 14).
**Lần:** 14 liên tiếp (09-08→09-21)

---

## ISSUE E4: wiki/HEARTBEAT.md leak (CARRY-FORWARD)

**Path:** `wiki/HEARTBEAT.md`
**Severity:** ERROR
**Category:** Orphan
**Issue:** HEARTBEAT.md leaked into wiki/ root — recurring process leak
**Current:** `wiki/HEARTBEAT.md` → `../../.openclaw/HEARTBEAT.md` (broken symlink)
**Expected:** HEARTBEAT.md belongs in .hermes/ or .openclaw/
**Suggested fix:** Process-level fix cần xác định sync tool đang mirror HEARTBEAT vào wiki/. File deletion là transient.
**Lần:** 26+ liên tiếp (08-26→09-21)

---

## ISSUE W1: memory/ sub-files (CARRY-FORWARD, 53 files)

**Path:** `memory/*`
**Severity:** WARNING
**Category:** Path
**Issue:** 53 sub-paths inside non-whitelisted `memory/` root folder
**Current:** 53 files (sub-paths of E2)
**Expected:** Content in .openclaw/memory/
**Suggested fix:** KHÔNG xóa — sub-paths của E2. +4 since 09-20 (session-corpus 09-20 + dreaming deep/light/rem 09-21). Same as09-20 machine count.

---

## ISSUE W2: Archive backup false positives (15 files)

**Path:** `wiki/reviews/archive/2026-09/*-backup-*.md`
**Severity:** WARNING
**Category:** Naming
**Issue:** 15 backup files in archive flagged by scanner report naming convention (non-report artifacts)
**Current:** Backup files from Fix Agent rename operations
**Expected:** Scanner archives exclusion for non-report backup files
**Suggested fix:** False positive — unchanged from 09-20. Update scan script archive exclusion cho backup files (optional).

---

## So sánh vs 09-20

| Chỉ số | 09-20 | 09-21 | Thay đổi |
|---|---|---|---|
| Paths checked | 233,845 | 233,868 | +23 |
| Tổng issues | 72 | 72 | 0 |
| ERROR | 4 | 4 | 0 |
| WARNING | 68 | 68 | 0 |
| memory/ sub-files | 49 | 53 | +4 |
| Wiki files mới | — | 294 | Tag regeneration + concepts |
| Raw files mới | — | 2 | Videos |
| Issues resolved | — | 0 | — |

**Kết luận:** 0 ISSUE RESOLVED vs 09-20 — toàn bộ 4 ERROR carry-forward. memory/ tăng +4 files (session-corpus 09-20 + dreaming deep/light/rem 09-21). openclaw-workspace-state.json gốc vẫn vắng mặt streak 26+ runs. Wiki layer active: tag files regenerated (25+) + 2 videos ingested raw/. 0 new naming violations, 0 empty dir.

---

## Actions needed

1. KHÔNG xóa `DREAMS.md` — carry-forward
2. KHÔNG xóa `memory/` — carry-forward
3. KHÔNG re-escalate `[SYSTEMATIC VIOLATION]` — all carry-forwards
4. Fix Agent: `.gitignore` thêm `openclaw-workspace-state.json.migrated.*` + `git rm --cached` marker + commit
5. `wiki/HEARTBEAT.md` — process-level fix (sync tool mirroring)
6. Optional: update scan script archive exclusion cho backup files trong `wiki/reviews/archive/`
