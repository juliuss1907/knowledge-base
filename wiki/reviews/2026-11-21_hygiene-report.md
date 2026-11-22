# Hygiene Inspection — 2026-11-21

**Status:** approved  
**Approved by:** Julius  
**Issues found:** 7 nhóm (4 ERROR, 3 WARNING, 0 INFO)  
**Created:** 2026-11-21 23:30:24 +0700  
**Validator:** hygiene-inspector  
**Paths checked:** 234853 tên tệp được bộ quét tham chiếu đếm trước ghi; không phải số đường dẫn đã kiểm tra theo quy chuẩn.

## Phạm vi và giới hạn

Đối chiếu `wiki/meta/folder-structure.md` v1.2. Bộ quét đi qua cây và tính cả nhiều nội bộ agent home; con số máy không biểu thị phạm vi kiểm tra thực tế. Không đọc nội dung bộ nhớ hoặc nhật ký OpenClaw. Trong bốn vùng `raw/`, `wiki/`, `context/`, `scripts/`, lượt đếm tên tệp trước ghi là 1.806 (240 + 1.559 + 2 + 5); dùng `os.walk`, cắt mọi thư mục `.git`, `.obsidian`, `node_modules`, tính tên tệp và symlink tệp. Số này tăng khi báo cáo mới được ghi. Đây là số được duyệt qua, không phải khẳng định mọi quy tắc đã được kiểm tra.

Bộ quét ghi **308 phát hiện máy**: 4 ERROR và 304 WARNING. Trong đó 289 WARNING tệp con `memory/` gộp vào Issue 2, 15 WARNING backup gộp vào Issue 5. Hai WARNING bổ sung là kiểm tra Git và giới hạn bộ quét. Bảy nhóm khác đơn vị với 308 phát hiện máy. Hôm trước tương ứng 304 phát hiện máy, gồm 285 cảnh báo tệp con `memory/`; tăng bốn cảnh báo loại này, không suy ra nguyên nhân tạo tệp. Báo cáo 2026-11-20 đã được duyệt; duyệt không đồng nghĩa đã sửa. Các vấn đề dưới đây tiếp diễn, không phát lại escalation cũ.

## Issue 1: Tệp ngoài whitelist ở root

**Path:** `DREAMS.md`  
**Severity:** ERROR  
**Category:** Path  
**Issue:** Tệp tồn tại nhưng không thuộc whitelist §2.  
**Current:** Có tệp ở root.  
**Expected:** Root chỉ chứa các tên được phép.  
**Suggested fix:** Giữ dữ liệu theo ghi chú duyệt; xác định và xử lý tiến trình ghi trước khi Fix Agent xử lý vị trí.

## Issue 2: Bộ nhớ ngoài whitelist

**Path:** `memory/`  
**Severity:** ERROR  
**Category:** Orphan  
**Issue:** Thư mục root không được §2 cho phép; 289 WARNING máy về tệp con được gộp vào đây.  
**Current:** Thư mục tồn tại; ngày trước có 285 WARNING tệp con.  
**Expected:** Bộ nhớ tác nhân thuộc agent home theo §3.  
**Suggested fix:** Giữ dữ liệu theo phê duyệt; xử lý tiến trình tạo trước, sau đó Fix Agent thực hiện phương án được duyệt. Không xóa dữ liệu để làm sạch báo cáo.

## Issue 3: Marker di chuyển ở root

**Path:** `openclaw-workspace-state.json.migrated.43c9aa3dead1239e131cfd1ddf1a21fed91f1640ba72aeaf94714c3a31d1c72b.e79d1c6c-d9cd-4f3c-b9eb-65b970017373`  
**Severity:** ERROR  
**Category:** Path  
**Issue:** Marker ngoài whitelist §2. `git ls-files` xác nhận marker này và biến thể `.openclaw/workspace-state.json.migrated.43c9aa3dead1239e131cfd1ddf1a21fed91f1640ba72aeaf94714c3a31d1c72b.fb077b94-2792-4ca2-b7d8-fc10c5575d51` còn được Git theo dõi.  
**Current:** Hai đường dẫn còn trong index Git.  
**Expected:** Không có marker runtime ngoài whitelist root; xử lý trạng thái Git theo phê duyệt.  
**Suggested fix:** Kiểm tra rule cho biến thể và bổ sung nếu cần trước khi gỡ khỏi index theo phê duyệt; không chỉ xóa bản trên đĩa.

## Issue 4: Symlink HEARTBEAT sai vị trí và bị đứt

**Path:** `wiki/HEARTBEAT.md`  
**Severity:** ERROR  
**Category:** Orphan  
**Issue:** Liên kết không thuộc whitelist wiki root §7.  
**Current:** Là symlink, đích thô `../../.openclaw/HEARTBEAT.md` phân giải thành `/home/julius/.openclaw/HEARTBEAT.md`, không tồn tại.  
**Expected:** Không đặt HEARTBEAT tại wiki root.  
**Suggested fix:** Xác định và sửa tiến trình tạo liên kết; Fix Agent xử lý liên kết sau phê duyệt. Không suy đoán tác nhân tạo.

## Issue 5: Bản sao archive chưa được quy định

**Path:** `wiki/reviews/archive/2026-09/`  
**Severity:** WARNING  
**Category:** Naming  
**Issue:** [SPEC CONFLICT] Có 15 bản `*-backup-*.md`; §7 không quy định rõ bản sao workflow trong archive.  
**Current:** Ví dụ `memory-backup-2026-06-15.md`, `2026-08-30_archify-backup-2026-09-01.md`.  
**Expected:** Vị trí và loại bản sao được quy định rõ.  
**Suggested fix:** Quyết định cho phép tại đây hoặc chọn nơi lưu hợp lệ; không tự đổi tên hay xóa.

## Issue 6: Artifact runtime được Git theo dõi

**Path:** `.hermes/config.yaml.bak.*`, `.hermes/kanban.db*`, `.hermes/MEMORY.md`  
**Severity:** WARNING  
**Category:** Path  
**Issue:** `git ls-files` xác nhận 20 backup config, 5 mục `kanban.db*` và `MEMORY.md` còn tracked, như ngày 2026-11-20. Đây là rủi ro quản lý runtime, không tự kết luận là orphan theo §3.  
**Current:** 26 đường dẫn trong index Git.  
**Expected:** Xác định dữ liệu runtime nào được phép theo dõi; ignore không có tác dụng hồi tố.  
**Suggested fix:** Rà soát độ nhạy và lịch sử Git; nếu được duyệt, thêm rule phù hợp trước khi gỡ index. Không công bố nội dung tệp.

## Issue 7: Giới hạn bộ quét so với quy chuẩn

**Path:** `.hermes/skills/hygiene-inspector/references/scan-script.py`; `wiki/meta/folder-structure.md` §6–§8  
**Severity:** WARNING  
**Category:** Naming  
**Issue:** Bộ quét tham chiếu không tự xác nhận đầy đủ thư mục, tệp bắt buộc, tập ký tự slug, giới hạn 80 ký tự và loại báo cáo so với §7–§8; cho phép `spot-check-report` mà §7 không liệt kê.  
**Current:** Bộ quét chỉ phân loại theo các quy tắc được lập trình; không thể khẳng định toàn bộ quy chuẩn đã được kiểm tra đầy đủ.  
**Expected:** Phân biệt ngoại lệ workflow với quy chuẩn và thực thi đủ các quy tắc.  
**Suggested fix:** [SPEC CONFLICT] Làm rõ loại báo cáo thực tế; bổ sung kiểm tra thư mục, tệp bắt buộc, slug và loại báo cáo.

## Hành động

Chờ Julius duyệt báo cáo. Không sửa cấu trúc, di chuyển hoặc xóa dữ liệu. Xem `wiki/reviews/_action-required.md`.
