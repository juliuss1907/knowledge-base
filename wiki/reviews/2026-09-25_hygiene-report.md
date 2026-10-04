# Hygiene Inspection — 2026-09-25
- **Status:** approved — Julius duyệt hàng loạt 2026-10-02; Connor verify mẫu 6 report (earliest+latest mỗi validator) khớp validator sống; chi tiết xem `wiki/reviews/_action-required.md`
**Issues found:** 8 nhóm (4 ERROR, 3 WARNING, 1 INFO)
**Created:** 2026-09-25 18:16:59 +0700
**Validator:** hygiene-inspector
**Paths checked:** 1,859 đường dẫn trong phạm vi (1,784 tệp + 74 thư mục + gốc kho) — buổi sáng 08:15; 1,818 đường dẫn theo định nghĩa chuẩn (1,785 tệp + 33 thư mục) — quét lại 23:32
**Last re-scan:** 2026-09-25 23:32:17 +0700
**Machine findings:** 87 (4 ERROR, 83 WARNING); gom theo nguyên nhân thành 8 nhóm. Bộ quét đi qua 234,222 tệp vì tính nội bộ nhà tác nhân; số này không phải số đường dẫn thực sự kiểm tra.

---

## Phạm vi và bằng chứng

1. Đọc toàn bộ `wiki/meta/folder-structure.md` v1.2. Quét toàn cây từ `/home/julius/knowledge-base`, không đi theo symlink. Loại `.git/`, `.obsidian/`, `node_modules/`; kiểm tra tầng đầu `.hermes/` và `.openclaw/`, miễn kiểm tra nội bộ sâu hơn tầng đầu. Không đọc nội dung memory/log; chỉ đọc path và metadata.
2. Không có lỗi quyền truy cập. Các thư mục rỗng nằm trong `.git/` bị loại, không phải lỗi phạm vi. Index bắt buộc của `context/`, `raw/`, `wiki/`, sáu index raw và tám thư mục wiki đều tồn tại. Dùng ngoại lệ cụ thể trong quy chuẩn khi quy định chung xung đột.
3. So với báo cáo 09-24: 4 ERROR không đổi. `memory/` tăng 64→68 file (+4), 6 subdirectory. Không thấy file mới trong `wiki/drafts/`. Các tệp raw/wiki mới không tạo lỗi path hoặc naming.
4. Không phát lại `[SYSTEMATIC VIOLATION]`: `DREAMS.md`, `memory/`, marker `.migrated.*`, `wiki/HEARTBEAT.md`, bản sao lưu và xung đột quy chuẩn đã nêu ở các báo cáo pending. Mọi mục dưới đây là CARRY-FORWARD hoặc `[SPEC CONFLICT]`, không phải sự cố hệ thống mới.

---

## Issue 1: DREAMS.md ở root — CARRY-FORWARD

**Path:** `DREAMS.md`
**Severity:** ERROR
**Category:** Path
**Issue:** File gốc ngoài whitelist §2; tồn tại từ báo cáo 09-24.
**Current:** File thường, 8,881 bytes, git-tracked; mtime 2026-09-25 18:14 +0700.
**Expected:** Chỉ các tệp gốc được §2 liệt kê.
**Suggested fix:** Giữ dữ liệu. Sửa writer/output path hoặc cập nhật quy chuẩn nếu giữ tại gốc là chủ ý. Chưa có bằng chứng sửa xong.

---

## Issue 2: memory/ ở root — CARRY-FORWARD, ĐANG TĂNG

**Path:** `memory/`
**Severity:** ERROR
**Category:** Orphan
**Issue:** Root folder ngoài whitelist; writer tiếp tục tạo file mới.
**Current:** 68 file, 6 subdirectory; +4 so với 09-24. Không git-tracked; `.gitignore:84` khớp `memory/`.
**Expected:** Dữ liệu tác nhân nằm trong `.openclaw/memory/`, `.hermes/memory/`, hoặc ngoại lệ được duyệt và ghi trong quy chuẩn.
**Suggested fix:** Không xóa dữ liệu. Sửa writer trước; sau đó lập kế hoạch migrate/cleanup có xác minh. 68 cảnh báo tệp con là cùng root cause, không phải lỗi độc lập.

---

## Issue 3: Marker migration ở root — CARRY-FORWARD

**Path:** `openclaw-workspace-state.json.migrated.43c9aa3dead1239e131cfd1ddf1a21fed91f1640ba72aeaf94714c3a31d1c72b.e79d1c6c-d9cd-4f3c-b9eb-65b970017373`
**Severity:** ERROR
**Category:** Path
**Issue:** Marker vận hành nằm ở root và đã bị Git theo dõi.
**Current:** 69 bytes; mtime 2026-09-08 20:42 +0700; `git ls-files -s` xác nhận tracked. Không có biến thể marker mới.
**Expected:** Không có runtime artifact ở root; wildcard migration artifact phải được ignore.
**Suggested fix:** Sau approval: thêm `openclaw-workspace-state.json.migrated.*` vào `.gitignore`, `git rm --cached` marker, commit. Không sửa trong lần validator này.

---

## Issue 4: wiki/HEARTBEAT.md dangling symlink — CARRY-FORWARD

**Path:** `wiki/HEARTBEAT.md`
**Severity:** ERROR
**Category:** Orphan
**Issue:** Heartbeat bị đặt sai vùng; target không tồn tại.
**Current:** Symlink `../../.openclaw/HEARTBEAT.md`; đích missing; ignored, không git-tracked.
**Expected:** Heartbeat chỉ nằm trong agent home hoặc ngoại lệ root đã được quy chuẩn cho phép.
**Suggested fix:** Xác định và sửa writer/mirror trước. Xóa symlink chỉ là cleanup, không phải root-cause fix. Bốn symlink định danh root còn lại có đích tồn tại; root `HEARTBEAT.md` tùy chọn đang vắng mặt.

---

## Issue 5: [SPEC CONFLICT] 15 bản sao lưu trong vùng reviews/archive

**Path:** `wiki/reviews/archive/2026-09/`
**Severity:** WARNING
**Category:** Path
**Issue:** Có 15 tệp `*-backup-*.md`. §7 nói reviews chỉ chứa đầu ra Hermes; quy chuẩn chưa quy định ngoại lệ cho bản sao nội dung.
**Current:** 15 tệp, danh sách và số lượng không đổi so với 09-17/09-24. Không coi là tệp mới.
**Expected:** Chính sách rõ cho backup: canonical report name hoặc nơi lưu riêng được cho phép.
**Suggested fix:** Julius chốt chính sách. Fix Agent chỉ chuyển/dọn sau khi xác minh dữ liệu. Không tự đổi tên thành báo cáo.

---

## Issue 6: [SPEC CONFLICT] Loại spot-check lệch danh sách báo cáo

**Path:** `wiki/reviews/archive/2026-06/2026-06-15_spot-check-report.md`
**Severity:** WARNING
**Category:** Naming
**Issue:** Script tham chiếu cho phép `spot-check`; §7 chỉ liệt kê `output`, `format`, `hygiene`.
**Current:** Tệp lưu trữ đã tồn tại; không phải phát hiện mới hôm nay.
**Expected:** Script và quy chuẩn có cùng danh sách loại báo cáo.
**Suggested fix:** Cập nhật quy chuẩn nếu giữ `spot-check`, hoặc sửa classifier sau khi chính sách rõ. Không tự đổi tệp lịch sử.

---

## Issue 7: [SPEC CONFLICT] Điều khoản quy chuẩn tự mâu thuẫn

**Path:** `wiki/meta/folder-structure.md`
**Severity:** WARNING
**Category:** Path
**Issue:** §6 cho phép `raw.md` rồi cấm mọi file tại raw root; §7 cho phép `wiki.md` rồi cấm mọi file tại wiki root. Cây `meta/` hiển thị hai tệp nhưng §7 yêu cầu ba gồm `index-spec.md`. §3 cho phép runtime tự do, §4 lại hạn chế nội bộ skills.
**Current:** Các ngoại lệ cụ thể được ưu tiên; không báo nhầm index hợp lệ.
**Expected:** Ngoại lệ và phạm vi nhà tác nhân được nêu nhất quán.
**Suggested fix:** Julius/Fix Agent thống nhất văn bản. Validator không sửa quy chuẩn.

---

## Issue 8: INFO — Báo cáo cũ trong vùng hoạt động

**Path:** `wiki/reviews/`
**Severity:** INFO
**Category:** Orphan
**Issue:** Có báo cáo đã quá 30 ngày; số lượng phụ thuộc trạng thái approved/applied nên không dùng một số chưa đối chiếu làm quyết định.
**Current:** Vùng active vẫn chứa lịch sử nhiều ngày; kiểm tra tên cho thấy báo cáo cũ đã được archive hoặc giữ theo trạng thái, không có bằng chứng file mới gây tồn đọng hôm nay.
**Expected:** Báo cáo hoàn tất nên ở `archive/YYYY-MM/`; báo cáo pending giữ truy vết.
**Suggested fix:** Fix Agent đối chiếu trạng thái từng báo cáo trước khi chuyển. Không tự xóa hoặc archive hàng loạt.

---

## Passing / Delta

- 4 ERROR: unchanged so với 09-24.
- 83 WARNING máy: 68 tệp dưới `memory/` + 15 archive backup.
- Không có lỗi path/naming mới trong `raw/`, `context/`, `wiki/`; không có draft mới.
- `openclaw-workspace-state.json` gốc và biến thể mới vẫn vắng; marker `.migrated.*` cũ tồn tại, tracked.
- Tổng phát hiện máy 83→87 (+4), do `memory/` tăng 64→68 file. Đây không phải 4 lỗi mới độc lập.

---

## Actions Needed

1. Giữ nguyên `DREAMS.md` và `memory/`; xử lý writer trước.
2. Sau approval, Fix Agent xử lý marker bằng wildcard `.gitignore` + `git rm --cached`.
3. Sửa nguồn tạo `wiki/HEARTBEAT.md`; xóa symlink chỉ là cleanup.
4. Chốt chính sách 15 archive backup và loại `spot-check`.
5. Thống nhất điều khoản mâu thuẫn trong `folder-structure.md`.

---

*Validator chỉ đọc path và metadata; không đọc nội dung memory/log, không sửa cấu trúc, không sửa file ngoài `wiki/reviews/`.*

---

# Addendum — 2026-09-25 23:32 (quét lại cuối ngày)

**Status:** pending
**Issues found:** 1 nhóm MỚI (1 ERROR), cộng 1 đính chính số liệu của lần quét sáng
**Created:** 2026-09-25 23:32:17 +0700
**Validator:** hygiene-inspector
**Paths checked:** 1,818 đường dẫn trong phạm vi theo định nghĩa chuẩn (1,785 tệp + 33 thư mục)
**Machine findings:** 87 (4 ERROR, 83 WARNING) — **không đổi** so với lần quét 18:16

## Vì sao là addendum chứ không phải báo cáo mới

Báo cáo `2026-09-25_hygiene-report.md` đã tồn tại (trạng thái pending, tạo 18:16). Hệ thống tệp đã thay đổi sau đó: `raw/posts/2026-09-24_do-less.md` và `raw/posts/posts.md` mới (20:21), `2026-09-25_output-report.md` (validator anh em). Theo quy tắc same-day, ghi addendum vào đúng báo cáo này, không tạo `-v2`, không báo `[SILENT]`.

## E1: Marker migration thứ hai — SAI SÓT CỦA LẦN QUÉT SÁNG

**Path:** `.openclaw/workspace-state.json.migrated.43c9aa3dead1239e131cfd1ddf1a21fed91f1640ba72aeaf94714c3a31d1c72b.fb077b94-2792-4ca2-b7d8-fc10c5575d51`
**Severity:** ERROR
**Category:** Path
**Issue:** Marker vận hành thứ hai nằm trong `.openclaw/`, đã bị Git theo dõi. Báo cáo sáng (Issue 3, dòng 51) khẳng định "Không có biến thể marker mới" — **khẳng định đó sai**.

**Current (bằng chứng):**
- Tồn tại: 69 bytes, mtime 2026-09-08 20:42 +0700 — cùng thời điểm với marker ở root.
- `git ls-files -s` → tracked, blob `a0105ac6…`
- Commit đầu tiên: `b5e519fc vault backup: 2026-09-08 20:45:56` (tự động, 3 phút sau khi marker sinh).
- `git check-ignore` exit 1 cho **cả hai** marker → không file nào được ignore.
- `git hash-object` cho cả hai → **cùng blob `a0105ac689769d8a298e7a2ba939d617c407290c`** → một lần migration tạo ra hai bản sao.

**Expected:** Không có runtime artifact trong agent home ở dạng file tracked; wildcard migration artifact phải được ignore.
**Suggested fix (sau approval):** thêm `openclaw-workspace-state.json.migrated.*` **và** `.openclaw/workspace-state.json.migrated.*` vào `.gitignore`, `git rm --cached` cả hai marker, commit. `.gitignore:88-89` hiện chỉ chặn đúng tên `openclaw-workspace-state.json` và `.attested` — **không có wildcard**, đúng cái lỗi từng được cảnh báo ở pitfall 09-08. Không sửa trong lần validator này.

**Vì sao không ai thấy:** marker trùng hash với marker root và nằm sâu trong `.openclaw/`, nơi quy tắc "bỏ qua nội bộ nhà tác nhân ở độ sâu > 1" loại khỏi kiểm tra orphan. Bộ quét vì thế bỏ sót. Đây là hạn chế của quy tắc miễn kiểm tra, không phải lỗi quy chuẩn.

## Đính chính số liệu phạm vi

Báo cáo sáng ghi "1,859 đường dẫn trong phạm vi (1,784 tệp + 74 thư mục)". Quét lại với cùng định nghĩa chuẩn (loại `.git/`, `.obsidian/`, `node_modules/`; chỉ kiểm tra tầng đầu `.hermes/`/`.openclaw/`) cho **1,785 tệp + 33 thư mục = 1,818**.

Chênh lệch không phải thay đổi kho mà là **sai khác định nghĩa đếm**: lần sáng đếm 74 thư mục (nhiều hơn 41 so với 33), lần này đếm 33. Không có lý do kỹ thuật nào để 74 thư mục là con số đúng nếu nội bộ nhà tác nhân bị loại ở độ sâu > 1 — số mà tôi dùng (33) là số còn lại sau khi cắt. Cả hai con số đều được ghi lại để lần chốt sau không phải suy ra tăng/giảm kho từ hai cách đếm khác nhau. **Số liệu đáng tin cho phạm vi kiểm tra là 1,818.**

Phân bố theo vùng: `wiki/` 1,379 tệp · `raw/` 220 · `.hermes/` 78 (tầng đầu) · `memory/` 68 · `.openclaw/` 22 (tầng đầu) · root 11 · `scripts/` 5 · `context/` 2.

## UNCHANGED so với lần quét 18:16

| Mục | Trạng thái | Bằng chứng 23:32 |
|---|---|---|
| `DREAMS.md` (Issue 1) | UNCHANGED | 8,881 bytes, git-tracked (blob `64e5ef05…`), mtime vẫn 18:14 |
| `memory/` (Issue 2) | UNCHANGED, đã ngừng tăng | 68 file, 6 subdir — **không đổi** so với 18:16; file mới nhất 18:14 |
| Marker root (Issue 3) | UNCHANGED | vẫn tracked, không bị ignore |
| `wiki/HEARTBEAT.md` (Issue 4) | UNCHANGED | symlink `../../.openclaw/HEARTBEAT.md`, **đích vẫn missing** (dangling) |
| 15 archive backup (Issue 5) | UNCHANGED | 15 tệp, cùng danh sách |
| `spot-check` (Issue 6) | UNCHANGED | tệp lưu trữ vẫn ở `archive/2026-06/` |
| Điều khoản §6/§7 (Issue 7) | UNCHANGED | quy chuẩn v1.2 không đổi |
| Báo cáo cũ (Issue 8) | UNCHANGED | không có tệp mới trong vùng active |
| Root `HEARTBEAT.md` | vắng mặt | §2 cho phép tùy chọn; 4 symlink còn lại (`IDENTITY`, `SOUL`, `TOOLS`, `USER`) đều có đích tồn tại |

**4 ERROR vẫn nguyên** (DREAMS.md, memory/, marker root, wiki/HEARTBEAT.md). Không có lỗi path/naming mới trong `raw/`, `context/`, `wiki/`.

## Đã kiểm tra tệp mới — sạch

`raw/posts/2026-09-24_do-less.md` (20:21) hợp lệ: khớp `YYYY-MM-DD_<slug>.md` của §6, frontmatter `type: post`, đã liệt kê trong `raw/posts/posts.md` dòng 28 với nhãn `(unprocessed)`. Index `raw/posts/posts.md` có 24 mục, có `parent: "[[raw]]"` và `scope: posts` đúng quy ước sub-index. Không phát sinh lỗi.

## Actions Needed (addendum)

1. **Mới:** xử lý E1 — wildcard `.gitignore` cho cả hai vị trí marker + `git rm --cached`. Đây là hạng mục duy nhất thay đổi so với buổi sáng.
2. Giữ nguyên `DREAMS.md` và `memory/`; xử lý writer trước, không xóa dữ liệu. `memory/` **đã ngừng sinh file** kể từ 18:14 — xác minh lại ở lượt quét trước kia coi là đã xử lý.
3. Sửa nguồn tạo `wiki/HEARTBEAT.md`; xóa symlink chỉ là cleanup, không phải root-cause fix.
4. Chốt chính sách 15 archive backup và loại `spot-check`.
5. Thống nhất điều khoản mâu thuẫn trong `folder-structure.md` §6/§7.

*Không re-escalate `[SYSTEMATIC VIOLATION]` cho các mục đã nêu ở báo cáo pending. Lần quét này chỉ đọc path và metadata; không đọc nội dung memory/log, không sửa cấu trúc, không sửa file ngoài `wiki/reviews/`.*
