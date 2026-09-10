# Hygiene Inspection — 2026-09-10

**Status:** pending
**Issues found:** 27 total (4 ERROR + 23 WARNING; 20 reported, 7 truncated)
**Created:** 2026-09-10 23:30:52
**Validator:** hygiene-inspector

**Paths checked:** 233,656 (includes directory entries — file-only estimate ~56,200)

**Context:** Fresh run for 09-10 (report trước: 09-09 pending). Giữa 09-09 23:30 và 09-10 23:30:
- **MỚI: 3 dreaming files** — `memory/dreaming/{deep,light,rem}/2026-09-10.md` (OpenClaw daily dreaming pipeline continues writing to root `memory/`)
- **MỚI: 1 corpus file** — `memory/.dreams/session-corpus/2026-09-09.txt`
- **09-09 report VẪN PENDING** — không có Fix Agent action trên bất kỳ issue nào
- `DREAMS.md`, `memory/`, `.migrated.*` marker, `wiki/HEARTBEAT.md` — tất cả carry-forward, chưa action
- `openclaw-workspace-state.json` gốc — vẫn vắng mặt (streak 14+), migration marker vẫn ở root
- Pipeline idle day 9: 0 concepts/sources compiled, 0 raw ingested since 09-02

---

## Issue 1: Root file — DREAMS.md (CARRY-FORWARD từ 09-09)

**Path:** DREAMS.md
**Severity:** ERROR
**Category:** Orphan
**Issue:** Known root orphan — file 228B tại KB root, git-tracked (committed `261ce5f2` 09-09 03:01)
**Current:** File vẫn ở root, không có action từ Fix Agent
**Expected:** Only AGENTS.md, TAGS.md, README.md, knowledge-base.md, symlinks, .gitignore allowed at root
**Suggested fix:** `git rm DREAMS.md` + commit (hoặc move về `.openclaw/`). Lần 2 liên tiếp chưa action.

---

## Issue 2: Recurring root folder — memory/ (CARRY-FORWARD + MỚI content 09-10)

**Path:** memory/
**Severity:** ERROR
**Category:** Orphan
**Issue:** Recurring root folder not in whitelist — nay có thêm 3 file dreaming 09-10
**Current:** Folder với 7+ files: `memory/.dreams/session-corpus/{2026-09-08.txt, 2026-09-09.txt}`, `memory/dreaming/deep/{2026-09-09.md, 2026-09-10.md}`, `memory/dreaming/light/{2026-09-09.md, 2026-09-10.md}`, `memory/dreaming/rem/{2026-09-09.md, 2026-09-10.md}`. Git-tracked. Lần đầu flagged 07-03; tái xuất populated 09-09.
**Expected:** `.openclaw/memory/` hoặc `.hermes/memory/`
**Suggested fix:** Process (OpenClaw dreaming) viết vào KB root `memory/` thay vì `.openclaw/memory/`. Redirect output path. `git rm -r memory/` + commit. Lần 2 liên tiếp chưa action.

---

## Issue 3: Migration marker — openclaw-workspace-state.json.migrated.* (CARRY-FORWARD từ 09-08)

**Path:** openclaw-workspace-state.json.migrated.43c9aa3dead1239e131cfd1ddf1a21fed91f1640ba72aeaf94714c3a31d1c72b.e79d1c6c-d9cd-4f3c-b9eb-65b970017373
**Severity:** ERROR
**Category:** Path
**Issue:** File not in root whitelist — migration marker từ OpenClaw 09-08 20:42, đã commit `b5e519fc`
**Current:** File 69 bytes tại root. KHÔNG gitignored. Git-tracked.
**Expected:** Không file lạ tại root
**Suggested fix:** (1) `.gitignore` thêm `openclaw-workspace-state.json.migrated.*`; (2) `git rm --cached` + commit. Lần 3 liên tiếp chưa action (từ 09-08 addendum).

---

## Issue 4: HEARTBEAT.md broken symlink — wiki/HEARTBEAT.md (CARRY-FORWARD, lần 11)

**Path:** wiki/HEARTBEAT.md
**Severity:** ERROR
**Category:** Orphan
**Issue:** HEARTBEAT.md leaked into wiki/ root — broken symlink lần 11 liên tiếp (08-26 → 09-10)
**Current:** Broken symlink `wiki/HEARTBEAT.md → ../../.openclaw/HEARTBEAT.md`. Target sai path. Untracked + unignored — sẽ bị commit bởi vault backup.
**Expected:** Không HEARTBEAT artifact tại wiki/ root
**Suggested fix:** Process-level fix: sync tool mirror symlink cần redirect. Lần 11 liên tiếp chưa action.

---

## Issue 5: memory/ sub-paths — unclassified (CARRY-FORWARD + MỚI 09-10)

**Path:** memory/.dreams/session-corpus/2026-09-08.txt, memory/.dreams/session-corpus/2026-09-09.txt, memory/dreaming/deep/2026-09-09.md, memory/dreaming/deep/2026-09-10.md, memory/dreaming/light/2026-09-09.md, memory/dreaming/light/2026-09-10.md, memory/dreaming/rem/2026-09-09.md, memory/dreaming/rem/2026-09-10.md
**Severity:** WARNING
**Category:** Path
**Issue:** 8 files trong root `memory/` — all unclassified paths. +3 files 09-10 (deep/light/rem dreaming logs)
**Current:** Agent-owned content nằm ngoài agent home
**Expected:** `.openclaw/memory/` hoặc `.hermes/memory/`
**Suggested fix:** Liên quan Issue 2 — redirect process output path cho toàn bộ `memory/` folder

---

## Issue 6: Archive naming — backup files (CARRY-FORWARD, false positive — KHÔNG RE-ESCALATE)

**Path:** wiki/reviews/archive/2026-09/*-backup-*.md (8 files: anthropic-cybersecurity-skills, archify, impeccable, openviking, posthog, threeui, destination-vs-vehicle, is-there-anything-left-to-build-in-crypto-wintermute)
**Severity:** WARNING
**Category:** Naming
**Issue:** Backup files trong archive flagged "Archived report naming" — scanner áp report naming convention cho tất cả archive files. Đây là backup artifacts, KHÔNG phải reports. False positive đã ghi nhận từ 09-09.
**Current:** 8 backup files trong `wiki/reviews/archive/2026-09/`
**Expected:** Backup files là non-report artifacts — scanner nên exclude
**Suggested fix:** Optional: update scan script archive exclusion cho backup files. KHÔNG escalate lại (đã ghi nhận 09-09).

---

## Carry-forward log

| Issue nhóm | Original escalation | Trạng thái 09-10 |
|---|---|---|
| `DREAMS.md` (Issue 1) | First occurrence 09-09 | Carry-forward lần 2, chưa action |
| `memory/` folder (Issue 2) | Recurring từ 07-03; populated 09-09 | Carry-forward lần 2, +3 files 09-10 |
| Migration marker `.migrated.*` (Issue 3) | Carry-forward từ 09-08 addendum | Carry-forward lần 3, chưa action |
| `wiki/HEARTBEAT.md` (Issue 4) | Process leak lần 11 liên tiếp (08-26→09-10) | Chờ process-level fix |
| Archive backup naming (Issue 6) | False positive từ 09-09 | Unchanged, không escalate |

**Tin tốt:**
- `openclaw-workspace-state.json` gốc — **VẮNG MẶT** streak 14+ (migrated 09-08, resolved ✅)
- 2 repos casing files — **RESOLVED** (lowercase rename done by Fix Agent)
- 8 backup files wiki/drafts/ — **MOVED** to archive (Fix Agent action done)
- 0 empty directory
- 0 new naming violations trong wiki/ content files
- Pipeline idle day 9: 0 new concepts/sources → 0 new issues

**Actions needed (cho Julius):**
1. Fix Agent: (1) `git rm DREAMS.md` + commit; (2) `git rm -r memory/` + commit; (3) `.gitignore` thêm `openclaw-workspace-state.json.migrated.*` + `git rm --cached` marker + commit.
2. `wiki/HEARTBEAT.md` — cần process-level fix (sync tool mirror). Untracked + unignored → sẽ bị commit bởi vault backup.
3. ARCHIVE naming false positive: 8 backup files trong `archive/2026-09/` không phải reports — scanner flagged nhầm. Optional: update scan script exclusion.
