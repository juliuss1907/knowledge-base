# Hygiene Inspection — 2026-11-26

**Status:** pending  
**Issues found:** 7 nhóm (4 ERROR, 3 WARNING, 0 INFO)  
**Created:** 2026-11-26 23:30 +0700  
**Validator:** hygiene-inspector  
**Paths checked:** 234885 tên tệp được bộ quét tham chiếu đếm trước khi ghi; không phải số đường dẫn được kiểm tra đầy đủ.

## Phạm vi và giới hạn

Đối chiếu `wiki/meta/folder-structure.md` v1.2. Bộ quét đi từ root, miễn phân loại sâu trong agent home; mã không thực sự cắt toàn bộ `.git`, `.obsidian` và `node_modules` trước khi duyệt. Vì vậy 234885 không phải số đường dẫn được xác nhận tuân thủ. Bộ quét ghi 312 phát hiện máy chưa gộp: 4 ERROR và 308 WARNING, chỉ xuất chi tiết 20 phát hiện đầu. Bảy nhóm dưới đây là đơn vị báo cáo, không phải số phát hiện máy. Các kiểm tra bổ sung không cộng vào số máy.

Phép đếm độc lập trước khi ghi, loại các thư mục `.git`, `.obsidian`, `node_modules` ở mọi độ sâu: `raw/` 242, `wiki/` 1582, `context/` 2, `scripts/` 5 tên tệp; có thể bao gồm symlink. Trong `memory/` có 293 tên tệp; archive có 15 tên chứa `-backup-`. Do chi tiết máy bị cắt, không khẳng định đã xác minh từng WARNING máy.

Các vấn đề dưới đây tiếp tục từ [báo cáo 2026-11-25](2026-11-25_hygiene-report.md), đã được duyệt để xử lý; chưa có bằng chứng đã sửa. Không đọc nội dung bộ nhớ hoặc nhật ký OpenClaw. Không phát lại cảnh báo hệ thống cũ như một vấn đề mới.

## Issue 1: Tệp root ngoài whitelist

**Path:** `DREAMS.md`  
**Severity:** ERROR  
**Category:** Path  
**Issue:** Tệp root không được §2 cho phép.  
**Current:** Tệp tồn tại, bộ quét ghi nhận.  
**Expected:** Chỉ các tệp root được liệt kê trong §2.  
**Suggested fix:** Giữ dữ liệu theo phê duyệt; xác định và xử lý tiến trình tạo trước khi xử lý vị trí.

## Issue 2: Thư mục bộ nhớ ngoài whitelist

**Path:** `memory/`  
**Severity:** ERROR  
**Category:** Orphan  
**Issue:** Thư mục root không được §2 cho phép.  
**Current:** 293 tên tệp trong cây, gộp vào một nhóm.  
**Expected:** Bộ nhớ tác nhân thuộc agent home theo §3.  
**Suggested fix:** Giữ dữ liệu; xử lý tiến trình tạo trước và thực hiện phương án đã duyệt, không xóa để làm sạch báo cáo.

## Issue 3: Marker di chuyển ngoài whitelist

**Path:** `openclaw-workspace-state.json.migrated.43c9aa3dead1239e131cfd1ddf1a21fed91f1640ba72aeaf94714c3a31d1c72b.e79d1c6c-d9cd-4f3c-b9eb-65b970017373`  
**Severity:** ERROR  
**Category:** Path  
**Issue:** Marker root không được §2 cho phép.  
**Current:** Quét tên toàn cây, loại `.git`, `.obsidian`, `node_modules`, thấy hai marker; cả marker root và `.openclaw/workspace-state.json.migrated.43c9aa3dead1239e131cfd1ddf1a21fed91f1640ba72aeaf94714c3a31d1c72b.fb077b94-2792-4ca2-b7d8-fc10c5575d51` đều được Git theo dõi.  
**Expected:** Không có marker ngoài whitelist root; quản lý trạng thái Git theo phê duyệt.  
**Suggested fix:** Kiểm tra rule wildcard cho cả hai vị trí trước khi gỡ khỏi index nếu được duyệt; không chỉ xóa bản trên đĩa.

## Issue 4: Symlink sai vị trí và đứt

**Path:** `wiki/HEARTBEAT.md`  
**Severity:** ERROR  
**Category:** Orphan  
**Issue:** Liên kết không thuộc whitelist wiki root §7.  
**Current:** Symlink trỏ `../../.openclaw/HEARTBEAT.md`, phân giải thành `/home/julius/.openclaw/HEARTBEAT.md`; đích không tồn tại.  
**Expected:** Không đặt HEARTBEAT tại wiki root.  
**Suggested fix:** Xác định và xử lý tiến trình tạo trước; Fix Agent xử lý liên kết sau phê duyệt. Không suy đoán tác nhân tạo.

## Issue 5: Bản sao archive chưa được quy định

**Path:** `wiki/reviews/archive/2026-09/`  
**Severity:** WARNING  
**Category:** Naming  
**Issue:** [SPEC CONFLICT] §7 không quy định rõ bản sao workflow trong archive.  
**Current:** Có 15 tên tệp chứa `-backup-` trong toàn cây archive.  
**Expected:** Vị trí và loại bản sao được quy định rõ.  
**Suggested fix:** Quyết định cho phép hoặc chọn nơi lưu hợp lệ; không tự đổi tên hay xóa.

## Issue 6: Artifact runtime được Git theo dõi

**Path:** `.hermes/config.yaml.bak.*`, `.hermes/kanban.db*`, `.hermes/MEMORY.md`  
**Severity:** WARNING  
**Category:** Path  
**Issue:** Git theo dõi dữ liệu runtime; đây là rủi ro quản lý, không tự kết luận là orphan theo §3.  
**Current:** `git ls-files` cho thấy 20 backup config, 5 mục `kanban.db*` và `MEMORY.md`: 26 đường dẫn, bằng báo cáo 11-25.  
**Expected:** Xác định dữ liệu runtime nào được phép theo dõi; ignore không có tác dụng hồi tố.  
**Suggested fix:** Rà soát độ nhạy và lịch sử Git; nếu được duyệt, thêm rule phù hợp trước khi gỡ index. Không công bố nội dung.

## Issue 7: Giới hạn bộ quét và loại báo cáo

**Path:** `.hermes/skills/hygiene-inspector/references/scan-script.py`; `wiki/reviews/archive/2026-06/2026-06-15_spot-check-report.md`  
**Severity:** WARNING  
**Category:** Naming  
**Issue:** [SPEC CONFLICT] Bộ quét cho phép `spot-check-report`, nhưng §7 không liệt kê loại này. Bộ quét chưa kiểm tra đầy đủ tên thư mục, tệp bắt buộc, tập ký tự slug và giới hạn 80 ký tự; kết quả chi tiết bị cắt.  
**Current:** Tệp và quy tắc bộ quét vẫn tồn tại; đây là tồn đọng đã báo, không phải tệp mới.  
**Expected:** Ngoại lệ workflow được quy định rõ; phép kiểm tra khớp quy chuẩn.  
**Suggested fix:** Làm rõ loại báo cáo và hoàn thiện bộ quét; §6–7 vừa yêu cầu `raw/raw.md`, `wiki/wiki.md` vừa cấm tệp tại root tương ứng, không coi hai chỉ mục bắt buộc là orphan.

## Hành động

Chờ Julius duyệt báo cáo. Giữ dữ liệu và xử lý tiến trình tạo trước. Không sửa cấu trúc, di chuyển hoặc xóa dữ liệu trong lượt kiểm tra này. Xem `wiki/reviews/_action-required.md`.
