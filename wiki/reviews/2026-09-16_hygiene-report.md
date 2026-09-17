# Hygiene Inspection — 2026-09-16

**Status:** approved
**Approved by:** Julius
**Approved at:** 2026-09-17 08:57 +0700
**Ghi chú duyệt:** Đã duyệt; chưa xác minh áp dụng sửa lỗi. Connor chỉ cập nhật báo cáo. Giữ nguyên DREAMS.md và memory/; xử lý tiến trình tạo lại trước. Không xóa dữ liệu theo đề xuất rmdir. Các sửa đổi ngoài wiki/reviews/ chuyển Fix Agent hoặc Julius.
**Issues found:** 51 (4 ERROR, 47 WARNING)
**Created:** 2026-09-16 23:31:00
**Validator:** hygiene-inspector

**Paths checked:** 233751

---

## Summary

**0 ISSUE RESOLVED vs 09-15** — toàn bộ 4 ERROR là carry-forward từ các runs trước:

1. **`DREAMS.md`** root orphan — git-tracked, lần 8 liên tiếp (09-09→09-16). OpenClaw dreaming artifact.
2. **`memory/`** root folder — lần 8 liên tiếp (09-09→09-16). **+4 new dreaming files since 09-15** (deep/light/rem 2026-09-16 logs + session-corpus 2026-09-15). OpenClaw dreaming pipeline tiếp tục viết vào root `memory/`. Tổng 32 sub-files (was 28 on 09-15).
3. **Migration marker** `openclaw-workspace-state.json.migrated.*` — git-tracked since `b5e519fc`, lần 9 liên tiếp từ 09-08 addendum.
4. **`wiki/HEARTBEAT.md`** — broken symlink lần 17 liên tiếp (08-26→09-16).

**WARNING:** 32 memory/ sub-files (sub-paths của Issue 2, +4 since 09-15) + ~15 backup files trong archive (false positive — non-report artifacts, scanner áp report naming convention cho tất cả archive files).

**Tin tốt:** `openclaw-workspace-state.json` gốc vắng mặt streak 20+ runs. 0 naming violations mới. 0 empty dir. 0 new root-level orphans. Pipeline quiet — +7 paths since 09-15 (233,744→233,751).

Không `[SYSTEMATIC VIOLATION]` mới. Không `[SPEC CONFLICT]`. Không `[STRUCTURE CHANGE]`.

---

## Issue 1: Known root orphan — DREAMS.md

**Path:** `DREAMS.md`
**Severity:** ERROR
**Category:** Orphan
**Issue:** Known root orphan: DREAMS.md
**Current:** `DREAMS.md` at KB root (7.0K, git-tracked)
**Expected:** Should be in `wiki/drafts/` or `.openclaw/` (OpenClaw dreaming artifact)
**Suggested fix:** See known issue — no action (proven futile)
**Carry-forward:** Lần 8 liên tiếp (09-09→09-16). Root cause = OpenClaw dreaming pipeline.

---

## Issue 2: Recurring root folder — memory/

**Path:** `memory/`
**Severity:** ERROR
**Category:** Orphan
**Issue:** Recurring root folder not in whitelist: memory/
**Current:** `memory/` at KB root — 32 files (8 session-corpus + 8 deep + 8 light + 8 rem)
**Expected:** Root cause = OpenClaw dreaming pipeline writes to root `memory/` instead of `.openclaw/memory/`
**Suggested fix:** Remove directory: rmdir memory/
**Carry-forward:** Lần 8 liên tiếp (09-09→09-16). +4 files since 09-15.

---

## Issue 3: Migration marker at root

**Path:** `openclaw-workspace-state.json.migrated.43c9aa3dead1239e131cfd1ddf1a21fed91f1640ba72aeaf94714c3a31d1c72b.e79d1c6c-d9cd-4f3c-b9eb-65b970017373`
**Severity:** ERROR
**Category:** Path
**Issue:** File not in root whitelist
**Current:** Migration marker at root (69B, git-tracked since `b5e519fc`)
**Expected:** Only AGENTS.md, TAGS.md, README.md, knowledge-base.md, symlinks, .gitignore allowed
**Suggested fix:** `.gitignore` thêm `openclaw-workspace-state.json.migrated.*` + `git rm --cached` + commit
**Carry-forward:** Lần 9 liên tiếp từ 09-08 addendum. Root cause: OpenClaw runtime tự migrate file tại 20:42 ngày 09-08.

---

## Issue 4: HEARTBEAT.md leaked into wiki/ root

**Path:** `wiki/HEARTBEAT.md`
**Severity:** ERROR
**Category:** Orphan
**Issue:** HEARTBEAT.md leaked into wiki/ root (recurring process leak)
**Current:** Broken symlink → `../../.openclaw/HEARTBEAT.md` (target exists)
**Expected:** HEARTBEAT.md belongs in .hermes/ or .openclaw/
**Suggested fix:** Fix the process writing HEARTBEAT.md to wiki/; then delete this file
**Carry-forward:** Lần 17 liên tiếp (08-26→09-16). Process-level fix needed (sync tool mirroring).

---

## Action items

1. **KHÔNG xóa `DREAMS.md`** — carry-forward. Root cause = OpenClaw dreaming pipeline.
2. **KHÔNG xóa `memory/`** — carry-forward. Root cause = OpenClaw dreaming pipeline.
3. **KHÔNG re-escalate `[SYSTEMATIC VIOLATION]`** — all carry-forwards.
4. **Fix Agent:** `.gitignore` thêm `openclaw-workspace-state.json.migrated.*` + `git rm --cached` marker + commit.
5. **`wiki/HEARTBEAT.md`** — process-level fix (sync tool mirroring).
