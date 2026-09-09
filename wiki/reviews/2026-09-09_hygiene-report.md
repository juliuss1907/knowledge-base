# Hygiene Inspection — 2026-09-09

**Status:** pending
**Issues found:** 7 (4 ERROR + 3 WARNING)
**Created:** 2026-09-09 23:30:34
**Validator:** hygiene-inspector

**Paths checked:** ~56,100 (estimated; scan script counted 233,647 due to directory entries being included — see note below)

**Context:** Fresh run for 09-09 (report trước: 09-08 addendum 23:31). Giữa 09-08 evening và 09-09 23:30:
- **repos casing RESOLVED** — Fix Agent đã rename `MengTo_threeui` → `mengto_threeui` và `PostHog_posthog` → `posthog_posthog` (lowercase, compliance). Đã deferred từ 09-02, nay done.
- **8 backup files đã moved** từ `wiki/drafts/` → `wiki/reviews/archive/2026-09/` (Fix Agent). Draft naming violations resolved — `wiki/drafts/` giờ chỉ còn 1 file legit (`analysis-2026-advice.md`).
- **MỚI: `DREAMS.md`** — file 228B tại KB root, git-tracked (committed `261ce5f2` 09-09 03:01). OpenClaw dreaming artifact.
- **MỚI: `memory/`** — root folder recurring, nay có nội dung dreaming (4 files: `.dreams/session-corpus/2026-09-08.txt`, `dreaming/{deep,light,rem}/2026-09-09.md`). Git-tracked.
- `openclaw-workspace-state.json` root — **VẪN VẮNG MẶT** (migrated 09-08, streak 12 run kết thúc ✅). Migration marker `.migrated.*` vẫn ở root.
- `wiki/HEARTBEAT.md` — broken symlink vẫn hiện diện, untracked + unignored.

---

## Issue 1: Root file — DREAMS.md (MỚI)

**Path:** DREAMS.md
**Severity:** ERROR
**Category:** Path
**Issue:** File not in root whitelist
**Current:** File 228B tại KB root, git-tracked (commit `261ce5f2` 09-09 03:01:58). Nội dung: OpenClaw deep sleep dreaming log (recall artifacts, candidate ranking).
**Expected:** Only AGENTS.md, TAGS.md, README.md, knowledge-base.md, symlinks, .gitignore allowed at root
**Suggested fix:** Move to `.openclaw/memory/` hoặc `.openclaw/` (agent-owned content). Nếu cần giữ, update folder-structure.md whitelist. Git-tracked → cần `git rm` + commit nếu xóa.

---

## Issue 2: Recurring root folder — memory/ (MỚI — nay có nội dung)

**Path:** memory/
**Severity:** ERROR
**Category:** Orphan
**Issue:** Recurring root folder not in whitelist: memory/
**Current:** Folder với 4 files dreaming content: `memory/.dreams/session-corpus/2026-09-08.txt`, `memory/dreaming/{deep,light,rem}/2026-09-09.md`. Git-tracked (folder). Created 09-09 03:00.
**Expected:** `.openclaw/memory/` hoặc `.hermes/memory/` — agent-owned content trong agent home
**Suggested fix:** A process (OpenClaw dreaming) writes to KB root `memory/` thay vì `.openclaw/memory/`. Redirect process output path. Git-tracked → cần `git rm -r memory/` + commit. Lần đầu flagged: 07-03; nay tái xuất với nội dung dreaming.

---

## Issue 3: Migration marker — openclaw-workspace-state.json.migrated.* (CARRY-FORWARD từ 09-08)

**Path:** openclaw-workspace-state.json.migrated.43c9aa3dead1239e131cfd1ddf1a21fed91f1640ba72aeaf94714c3a31d1c72b.e79d1c6c-d9cd-4f3c-b9eb-65b970017373
**Severity:** ERROR
**Category:** Orphan (Path whitelist)
**Issue:** File not in root whitelist — migration marker artifact từ OpenClaw 09-08 20:42
**Current:** File 69 bytes tại root. KHÔNG gitignored (git check-ignore fails). ĐÃ bị commit `b5e519fc` 09-08 20:45.
**Expected:** Không file lạ tại root
**Suggested fix:** (1) `.gitignore` thêm `openclaw-workspace-state.json.migrated.*`; (2) `git rm --cached` + commit. Fix Agent owns execution. Đã carry-forward từ 09-08 addendum, chưa có action.

---

## Issue 4: HEARTBEAT.md broken symlink — wiki/HEARTBEAT.md (CARRY-FORWARD từ 09-08)

**Path:** wiki/HEARTBEAT.md
**Severity:** ERROR
**Category:** Orphan
**Issue:** HEARTBEAT.md leaked into wiki/ root (recurring process leak) — broken symlink
**Current:** Broken symlink `wiki/HEARTBEAT.md → ../../.openclaw/HEARTBEAT.md`. Target không tồn tại (symlink resolves to `/home/julius/.openclaw/HEARTBEAT.md` — sai path; actual file tại `/home/julius/knowledge-base/.openclaw/HEARTBEAT.md`). Untracked + unignored — sẽ bị auto-commit bởi vault backup.
**Expected:** Không HEARTBEAT artifact tại wiki/ root
**Suggested fix:** Process-level fix: sync tool mirror symlink HEARTBEAT vào wiki/ cần được redirect. File deletion transient nếu writer active. Đã carry-forward từ 09-08 evening, lần 10 liên tiếp (08-26 → 09-09).

---

## Issues 5-7: Backup files in archive/2026-09/ — RESOLVED (moved from drafts/)

**Path:** `wiki/reviews/archive/2026-09/*-backup-*.md` (15 files, 12 truncated from report limit)
**Severity:** WARNING
**Category:** Naming
**Issue:** Backup files moved from `wiki/drafts/` to `wiki/reviews/archive/2026-09/` by Fix Agent — draft naming violations RESOLVED, but archive files still flagged by scanner (false positive: scanner applies report naming convention to all archive files)
**Current:** 15 backup files in archive (6 repos + 2 src_ + 4 older + 1 temp)
**Expected:** Archive naming YYYY-MM-DD_<type>-report.md only applies to actual reports
**Suggested fix:** These are backup artifacts, not reports. Archive naming convention false positive. Consider adding backup file exclusion to scan script or moving backups out of `wiki/reviews/archive/`.

---

## Carry-forward log

| Issue nhóm | Original escalation | Trạng thái 09-09 |
|---|---|---|
| `DREAMS.md` (Issue 1) | **MỚI** — first occurrence 09-09 | Root file, git-tracked — move or whitelist |
| `memory/` folder (Issue 2) | Recurring từ 07-03; nay populated | Redirect process output path |
| Migration marker `.migrated.*` (Issue 3) | Carry-forward từ 09-08 addendum | Chưa có Fix Agent action |
| `wiki/HEARTBEAT.md` (Issue 4) | Process leak lần 10 liên tiếp (08-26→09-09) | Chờ process-level fix |
| 2 repos casing files | **RESOLVED** — lowercase rename done ✅ | Closed |
| 8 backup files `wiki/drafts/` | **RESOLVED** — moved to archive ✅ | Closed (archive naming false positive) |

**Tin tốt:**
- `openclaw-workspace-state.json` root — **VẮNG MẶT** streak 13 (migrated 09-08, resolved ✅)
- 2 repos casing files — **RESOLVED** (lowercase rename done by Fix Agent)
- 8 backup files — **MOVED** from `wiki/drafts/` → `wiki/reviews/archive/2026-09/` (Fix Agent action done)
- `memory/` + `state/` ở root đều flagged — không bị bỏ sót
- 0 empty directory. 0 new naming violations trong wiki/ content files.

**Actions needed (cho Julius):**
1. Fix Agent: (1) `git rm DREAMS.md` + commit (hoặc move về `.openclaw/`); (2) `git rm -r memory/` + commit; (3) `.gitignore` thêm `openclaw-workspace-state.json.migrated.*` + `git rm --cached` marker + commit.
2. `wiki/HEARTBEAT.md` — cần process-level fix (sync tool mirror). Untracked + unignored → sẽ bị commit bởi vault backup sớm.
3. ARCHIVE naming false positive: 15 backup files trong `archive/2026-09/` không phải reports — scanner flagged nhầm. Optional: update scan script exclusion.
