# Hygiene Inspection — 2026-09-24

**Status:** pending
**Issues found:** 83 (4 ERROR + 79 WARNING + 0 INFO)
**Created:** 2026-09-24 08:50:08 +0700
**Validator:** hygiene-inspector
**Paths checked:** 234,133

---

## Summary

**0 issue được giải quyết so với 09-22.** Tổng phát hiện tăng 76→83 (+7), hoàn toàn do `memory/` tăng 57→64 file (+7).

| Severity | 09-22 | 09-24 | Delta |
|---|---:|---:|---:|
| ERROR | 4 | 4 | 0 |
| WARNING | 72 | 79 | +7 |
| INFO | 0 | 0 | 0 |
| **Total** | **76** | **83** | **+7** |

- `paths_checked`: 234,083→234,133 (+50)
- `memory/`: 57→64 file (+7), 6 subdirectory
- 4 ERROR: unchanged
- 79 WARNING: 64 memory sub-files + 15 archive backup noncanonical

---

## Issue 1: DREAMS.md ở root — CARRY-FORWARD

**Path:** `DREAMS.md`
**Severity:** ERROR
**Category:** Path
**Issue:** File không thuộc root whitelist.
**Current:** File thường, 8,932 bytes, git-tracked; mtime 2026-09-24 03:00 +0700.
**Expected:** Chỉ các file root được whitelist.
**Suggested fix:** Giữ dữ liệu; sửa writer OpenClaw để ghi vào vùng agent đúng. Chỉ xử lý file ở root sau khi có phương án giữ dữ liệu và Julius duyệt.

---

## Issue 2: memory/ ở root — CARRY-FORWARD, ĐANG TĂNG

**Path:** `memory/`
**Severity:** ERROR
**Category:** Orphan
**Issue:** Root folder ngoài whitelist; writer vẫn tạo file mới hằng ngày.
**Current:** 64 file, 6 subdirectory; +7 so với 09-22. Folder bị `.gitignore`, không git-tracked.
**Expected:** Memory nằm trong `.openclaw/memory/` hoặc vùng agent tương ứng.
**Suggested fix:** Không xóa dữ liệu. Sửa output path của writer trước; sau đó mới lập kế hoạch migrate/cleanup có xác minh.

---

## Issue 3: Migration marker ở root — CARRY-FORWARD

**Path:** `openclaw-workspace-state.json.migrated.43c9aa3dead1239e131cfd1ddf1a21fed91f1640ba72aeaf94714c3a31d1c72b.e79d1c6c-d9cd-4f3c-b9eb-65b970017373`
**Severity:** ERROR
**Category:** Path
**Issue:** Marker migration của OpenClaw nằm ở root và đã bị Git theo dõi.
**Current:** 69 bytes; mtime 2026-09-08 20:42 +0700; git-tracked.
**Expected:** Không có file runtime tạm ở root; wildcard migration artifact phải được ignore.
**Suggested fix:** Fix Agent sau khi được duyệt: thêm `openclaw-workspace-state.json.migrated.*` vào `.gitignore`, `git rm --cached` marker và commit.

---

## Issue 4: wiki/HEARTBEAT.md dangling symlink — CARRY-FORWARD

**Path:** `wiki/HEARTBEAT.md`
**Severity:** ERROR
**Category:** Orphan
**Issue:** Heartbeat bị mirror sai vào `wiki/`; target không tồn tại.
**Current:** Symlink → `../../.openclaw/HEARTBEAT.md`; target missing; mtime 2026-08-26 17:01 +0700; ignored, không git-tracked.
**Expected:** Heartbeat chỉ nằm trong agent home.
**Suggested fix:** Sửa tiến trình mirror/sync trước. Xóa symlink chỉ là cleanup, không phải root-cause fix.

---

## WARNING Breakdown (79)

1. **64 `memory/` sub-files** — cùng root cause với Issue 2; +7 so với 09-22.
2. **15 archive backup files** trong `wiki/reviews/archive/2026-09/` không theo canonical report filename. Đây là process/quy chuẩn conflict carry-forward, không phải file có thể âm thầm bỏ qua. Fix Agent nên đặt backup ngoài KB hoặc cleanup sau khi xác minh, chỉ khi Julius duyệt.

---

## Passing / Delta

- Không có lỗi path/naming mới ngoài hai nhóm carry-forward.
- Không có empty directory.
- Không có file mới trong `wiki/drafts/`.
- `openclaw-workspace-state.json` gốc vẫn vắng mặt; marker migration vẫn là artifact cần xử lý.
- 4 file wiki mới không tạo lỗi hygiene.

---

## Actions Needed

1. Không xóa `DREAMS.md` hoặc `memory/` trước khi xử lý writer và bảo toàn dữ liệu.
2. Sửa writer tạo `DREAMS.md` và `memory/`.
3. Sau approval, xử lý migration marker bằng `.gitignore` wildcard + `git rm --cached`.
4. Sửa process mirror tạo `wiki/HEARTBEAT.md`; không coi xóa symlink là giải pháp cuối.
5. Chốt chính sách cho 15 archive backup; không tự rename/xóa.

---

*Validator chỉ đọc path và metadata; không đọc nội dung memory/log và không sửa cấu trúc.*
