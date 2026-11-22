# Hygiene Inspection — 2026-11-20

**Status:** approved  
**Approved by:** Julius  
**Issues found:** 7 nhóm (4 ERROR, 3 WARNING, 0 INFO)  
**Created:** 2026-11-20 23:30:36 +0700  
**Validator:** hygiene-inspector  
**Paths checked:** 234826 lượt đếm tên tệp của bộ quét tham chiếu trước khi ghi; không phải số đường dẫn thực sự kiểm tra theo quy chuẩn.

## Phạm vi và phương pháp

Đọc toàn bộ `wiki/meta/folder-structure.md` v1.2. Bộ quét đi qua cây nhưng không cắt triệt để `.git/`, `.obsidian/`, `node_modules/` và nội bộ agent home trước khi đếm. Nội bộ `.hermes/` và `.openclaw/` ở độ sâu lớn hơn một được miễn kiểm tra orphan; kiểm tra bổ sung chỉ dùng đường dẫn, trạng thái Git và metadata, không đọc bộ nhớ hoặc nhật ký OpenClaw. Không coi 234826 là quy mô KB. Có 1784 tệp theo lượt đếm trước ghi trong bốn vùng: `raw/` 239, `wiki/` 1538, `context/` 2, `scripts/` 5; tính tên tệp và symlink tệp theo `os.walk`, bỏ `.git`, `.obsidian`, `node_modules` ở các vùng đó. Sau ghi thêm báo cáo, số này có thể tăng.

Bộ quét ghi 304 phát hiện máy: 4 ERROR và 300 WARNING, trong đó 285 cảnh báo tệp con `memory/` gộp vào Issue 2 và 15 cảnh báo backup gộp vào Issue 5. Hai WARNING bổ sung là kiểm tra metadata runtime và hạn chế bộ quét. Bảy nhóm không đồng nhất với 304 phát hiện máy. Kiểm tra bổ sung không thấy thư mục con trái whitelist tại bốn vùng, thư mục rỗng, tên slug không hợp lệ trong các vùng nội dung được kiểm tra, hoặc thiếu các index và tệp lõi được liệt kê trong tập kiểm tra. Không khẳng định toàn bộ quy chuẩn đã được kiểm tra đầy đủ: bộ quét không tự kiểm tra hoàn chỉnh các trường hợp thư mục, slug, loại báo cáo và tệp bắt buộc.

Báo cáo 2026-11-19 đã được duyệt, không đồng nghĩa đã sửa. Các tồn tại dưới đây được đo lại; không phát lại escalation cũ.

## Issue 1: Tệp ngoài whitelist ở root

**Path:** `DREAMS.md`  
**Severity:** ERROR  
**Category:** Path  
**Issue:** Tệp tồn tại nhưng không nằm trong whitelist §2; tiếp diễn từ báo cáo 2026-11-19 đã duyệt.  
**Current:** Tệp ở root.  
**Expected:** Root chỉ chứa các tên được phép.  
**Suggested fix:** Giữ dữ liệu theo ghi chú duyệt; xác định và xử lý tiến trình ghi trước khi Fix Agent xử lý vị trí.

## Issue 2: Thư mục bộ nhớ ngoài whitelist

**Path:** `memory/`  
**Severity:** ERROR  
**Category:** Orphan  
**Issue:** Root không cho phép thư mục này; 285 WARNING máy về tệp con được gộp vào đây. Tiếp diễn từ báo cáo 2026-11-19 đã duyệt.  
**Current:** Thư mục và tệp con tồn tại; hôm trước bộ quét đếm 281 WARNING tệp con.  
**Expected:** Bộ nhớ tác nhân nằm trong agent home theo §3.  
**Suggested fix:** Giữ dữ liệu theo ghi chú duyệt; xử lý tiến trình tạo trước, sau đó Fix Agent áp dụng phương án đã duyệt. Không xóa dữ liệu chỉ để làm sạch báo cáo.

## Issue 3: Marker di chuyển ngoài whitelist

**Path:** `openclaw-workspace-state.json.migrated.43c9aa3dead1239e131cfd1ddf1a21fed91f1640ba72aeaf94714c3a31d1c72b.e79d1c6c-d9cd-4f3c-b9eb-65b970017373`  
**Severity:** ERROR  
**Category:** Path  
**Issue:** Marker ở root không được §2 cho phép. Marker này và `.openclaw/workspace-state.json.migrated.43c9aa3dead1239e131cfd1ddf1a21fed91f1640ba72aeaf94714c3a31d1c72b.fb077b94-2792-4ca2-b7d8-fc10c5575d51` đều còn được Git theo dõi; `git check-ignore --no-index` không tìm thấy rule cho từng đường dẫn.  
**Current:** Cả hai marker tồn tại và tracked; tiếp diễn từ 2026-11-19.  
**Expected:** Không có marker runtime ngoài whitelist root; trạng thái Git của artifact runtime cần được xử lý theo phê duyệt.  
**Suggested fix:** Thêm rule bao phủ biến thể trước khi gỡ khỏi index theo phê duyệt; không chỉ xóa bản trên đĩa.

## Issue 4: Symlink HEARTBEAT ngoài vị trí và bị đứt

**Path:** `wiki/HEARTBEAT.md`  
**Severity:** ERROR  
**Category:** Orphan  
**Issue:** Liên kết tại wiki root không thuộc whitelist §7; tiếp diễn từ 2026-11-19.  
**Current:** `is_symlink=true`, `lexists=true`; đích thô `../../.openclaw/HEARTBEAT.md` phân giải thành `/home/julius/.openclaw/HEARTBEAT.md`, không tồn tại.  
**Expected:** Không đặt HEARTBEAT tại wiki root.  
**Suggested fix:** Xác định và sửa tiến trình tạo liên kết; Fix Agent xử lý liên kết sau phê duyệt. Không suy đoán tác nhân tạo.

## Issue 5: Bản sao trong archive chưa được quy định

**Path:** `wiki/reviews/archive/2026-09/`  
**Severity:** WARNING  
**Category:** Naming  
**Issue:** [SPEC CONFLICT] Có 15 bản `*-backup-*.md`; §7 không quy định rõ bản sao workflow trong archive. Đây là một nhóm, không phải 15 nhóm. Tiếp diễn từ 2026-11-19.  
**Current:** Ví dụ `memory-backup-2026-06-15.md` và `2026-08-30_archify-backup-2026-09-01.md`.  
**Expected:** Vị trí và loại bản sao được quy định rõ.  
**Suggested fix:** Quyết định cho phép bản sao tại đây hoặc chọn nơi lưu hợp lệ; không tự đổi tên hay xóa.

## Issue 6: Artifact runtime còn được Git theo dõi

**Path:** `.hermes/config.yaml.bak.*`, `.hermes/kanban.db*`, `.hermes/MEMORY.md`  
**Severity:** WARNING  
**Category:** Path  
**Issue:** `git ls-files -s` xác nhận 20 backup config, 5 mục `kanban.db*` và `MEMORY.md` còn tracked, giống số đo 2026-11-19. Đây là rủi ro quản lý runtime, không tự kết luận là orphan theo §3.  
**Current:** `MEMORY.md` có rule ignore nhưng vẫn tracked; không tìm thấy rule qua `git check-ignore --no-index` cho backup `20261113_200709` và `kanban.db`.  
**Expected:** Quyết định dữ liệu runtime nào được phép theo dõi; ignore không có tác dụng hồi tố đối với tệp đã tracked.  
**Suggested fix:** Rà soát độ nhạy và lịch sử Git; nếu được duyệt, thêm rule trước khi gỡ index. Không công bố nội dung tệp.

## Issue 7: Hạn chế bộ quét so với quy chuẩn

**Path:** `.hermes/skills/hygiene-inspector/references/scan-script.py`; `wiki/meta/folder-structure.md` §6–§8  
**Severity:** WARNING  
**Category:** Naming  
**Issue:** Bộ quét cho phép `spot-check-report` dù §7 không liệt kê; regex slug chấp nhận dải Unicode rộng, không yêu cầu đầy đủ đuôi `.md` và không kiểm tra giới hạn 80 ký tự. Bộ quét cũng không tự xác nhận đầy đủ thư mục và tệp bắt buộc.  
**Current:** Phương pháp kiểm tra bổ sung đã kiểm tra slug ở các vùng nội dung và một tập tệp bắt buộc, nhưng không thay thế mọi quy tắc chưa được thực thi.  
**Expected:** Phân biệt ngoại lệ workflow và quy chuẩn; thực thi đầy đủ tập ký tự, độ dài, đuôi và whitelist.  
**Suggested fix:** [SPEC CONFLICT] Làm rõ loại báo cáo thực tế rồi sửa bộ quét theo quy chuẩn; bổ sung kiểm tra thư mục và tệp bắt buộc.

## Hành động

Chờ Julius duyệt báo cáo. Không sửa cấu trúc, di chuyển hoặc xóa dữ liệu. Tình trạng duyệt của báo cáo cũ không chứng minh Fix Agent đã áp dụng sửa chữa. Xem `wiki/reviews/_action-required.md`.
