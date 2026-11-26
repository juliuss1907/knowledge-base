# Hygiene Inspection — 2026-11-23

**Status:** approved
**Approved by:** Julius
**Issues found:** 7 nhóm (4 ERROR, 3 WARNING, 0 INFO)  
**Created:** 2026-11-23 23:31 +0700  
**Validator:** hygiene-inspector  
**Paths checked:** 234867 tên tệp được bộ quét tham chiếu đếm trước khi ghi; không phải số đường dẫn được kiểm tra đầy đủ.

## Phạm vi và đối chiếu

Đối chiếu `wiki/meta/folder-structure.md` v1.2. Bộ quét duyệt cây và bỏ qua `.git`, `.obsidian`, `node_modules`; nội bộ agent home được miễn kiểm tra orphan ở độ sâu lớn. Số máy bao gồm nội bộ agent home, không phải phạm vi kiểm tra đầy đủ. Trước khi ghi báo cáo: `raw/` 240, `wiki/` 1571, `context/` 2, `scripts/` 5 tên tệp và symlink tệp theo `os.walk`, cùng các thư mục bị loại nêu trên.

Bộ quét ghi **312 phát hiện máy: 4 ERROR, 308 WARNING**. Trong đó 293 cảnh báo về tệp con `memory/` gộp vào Issue 2; 15 cảnh báo về bản sao archive gộp vào Issue 5. Issue 6 và 7 là kiểm tra bổ sung ngoài số máy. Tổng nhóm không tương đương số phát hiện máy. Số máy và số tệp con `memory/` không đổi so với báo cáo 2026-11-22 đang chờ duyệt; điều đó không chứng minh từng tệp không đổi. Không đọc nội dung bộ nhớ hay nhật ký OpenClaw.

Kiểm tra bổ sung không phát hiện slug sai trong `wiki/concepts/`, `wiki/sources/`, `wiki/tag/`, `wiki/topic/`, `wiki/drafts/`, hoặc tên thư mục sai trong bốn vùng nội dung theo phép kiểm tra đã chạy. Các tệp bắt buộc root, context, raw index và wiki meta được chọn đều tồn tại. Quy chuẩn còn mâu thuẫn: §6 và §7 cấm tệp ở root nhưng yêu cầu lần lượt `raw/raw.md` và `wiki/wiki.md`; hai tệp chỉ mục không bị tính là lỗi. Không coi lượt này là chứng nhận mọi quy tắc đã được tự động kiểm tra.

## Issue 1: Tệp ngoài whitelist ở root

**Path:** `DREAMS.md`  
**Severity:** ERROR  
**Category:** Path  
**Issue:** Tệp tồn tại ngoài whitelist §2.  
**Current:** Tệp tồn tại ở root.  
**Expected:** Root chỉ chứa các tên được cho phép.  
**Suggested fix:** Giữ dữ liệu theo ghi chú duyệt; xác định và xử lý tiến trình ghi trước khi Fix Agent xử lý vị trí.

## Issue 2: Bộ nhớ ngoài whitelist

**Path:** `memory/`  
**Severity:** ERROR  
**Category:** Orphan  
**Issue:** Thư mục root không được §2 cho phép; gộp 293 cảnh báo máy về tệp con.  
**Current:** Thư mục và 293 tên tệp tồn tại.  
**Expected:** Bộ nhớ tác nhân thuộc agent home theo §3.  
**Suggested fix:** Giữ dữ liệu theo phê duyệt; xử lý tiến trình tạo trước, sau đó thực hiện phương án được duyệt. Không xóa dữ liệu để làm sạch báo cáo.

## Issue 3: Marker di chuyển ngoài whitelist

**Path:** `openclaw-workspace-state.json.migrated.43c9aa3dead1239e131cfd1ddf1a21fed91f1640ba72aeaf94714c3a31d1c72b.e79d1c6c-d9cd-4f3c-b9eb-65b970017373`  
**Severity:** ERROR  
**Category:** Path  
**Issue:** Marker ở root không được §2 cho phép.  
**Current:** Marker này và `.openclaw/workspace-state.json.migrated.43c9aa3dead1239e131cfd1ddf1a21fed91f1640ba72aeaf94714c3a31d1c72b.fb077b94-2792-4ca2-b7d8-fc10c5575d51` tồn tại trên đĩa và trong index Git. Quét tên marker trong cây, loại các thư mục miễn quét, chỉ tìm thấy hai đường dẫn này.  
**Expected:** Không có marker runtime ngoài whitelist root; xử lý trạng thái Git theo phê duyệt.  
**Suggested fix:** Kiểm tra rule wildcard trước khi gỡ khỏi index theo phê duyệt; không chỉ xóa bản trên đĩa.

## Issue 4: Symlink HEARTBEAT sai vị trí và bị đứt

**Path:** `wiki/HEARTBEAT.md`  
**Severity:** ERROR  
**Category:** Orphan  
**Issue:** Liên kết không thuộc whitelist wiki root §7.  
**Current:** Symlink có đích thô `../../.openclaw/HEARTBEAT.md`, phân giải thành `/home/julius/.openclaw/HEARTBEAT.md`; đích không tồn tại.  
**Expected:** Không đặt HEARTBEAT tại wiki root.  
**Suggested fix:** Xác định và sửa tiến trình tạo liên kết; Fix Agent xử lý liên kết sau phê duyệt. Không suy đoán tác nhân tạo.

## Issue 5: Bản sao archive chưa được quy định

**Path:** `wiki/reviews/archive/2026-09/`  
**Severity:** WARNING  
**Category:** Naming  
**Issue:** [SPEC CONFLICT] Có 15 bản `*-backup-*.md`; §7 không quy định rõ bản sao workflow trong archive.  
**Current:** Ví dụ `memory-backup-2026-06-15.md` và `2026-08-30_archify-backup-2026-09-01.md`.  
**Expected:** Vị trí và loại bản sao được quy định rõ.  
**Suggested fix:** Quyết định cho phép tại đây hoặc chọn nơi lưu hợp lệ; không tự đổi tên hay xóa.

## Issue 6: Artifact runtime được Git theo dõi

**Path:** `.hermes/config.yaml.bak.*`, `.hermes/kanban.db*`, `.hermes/MEMORY.md`  
**Severity:** WARNING  
**Category:** Path  
**Issue:** Git theo dõi dữ liệu runtime; đây là rủi ro quản lý, không tự kết luận là orphan theo §3.  
**Current:** `git ls-files -s` xác nhận 20 backup config, 5 mục `kanban.db*` và `MEMORY.md`: 26 đường dẫn, không đổi về số so với 2026-11-22. Một backup config được kiểm tra không khớp rule ignore; `MEMORY.md` khớp rule nhưng vẫn tracked.  
**Expected:** Xác định dữ liệu runtime nào được phép theo dõi; ignore không có tác dụng hồi tố.  
**Suggested fix:** Rà soát độ nhạy và lịch sử Git; nếu được duyệt, thêm rule phù hợp trước khi gỡ index. Không công bố nội dung tệp.

## Issue 7: Giới hạn bộ quét và loại báo cáo chưa được quy định

**Path:** `.hermes/skills/hygiene-inspector/references/scan-script.py`; `wiki/reviews/archive/2026-06/2026-06-15_spot-check-report.md`  
**Severity:** WARNING  
**Category:** Naming  
**Issue:** [SPEC CONFLICT] Bộ quét cho phép `spot-check-report`, nhưng §7 không liệt kê loại này. Tệp thực tế đã tồn tại, không phải phát hiện mới. Bộ quét không tự xác nhận đầy đủ thư mục, tệp bắt buộc, tập ký tự slug và giới hạn 80 ký tự.  
**Current:** Có tệp spot-check trong archive; kiểm tra bổ sung chỉ bao phủ các vùng và tệp nêu trong phần phạm vi.  
**Expected:** Ngoại lệ workflow được quy định rõ và phép kiểm tra khớp quy chuẩn.  
**Suggested fix:** Làm rõ loại báo cáo thực tế; hoàn thiện bộ quét và đối chiếu các ngoại lệ có chủ đích.

## Hành động

Chờ Julius duyệt báo cáo. Các vấn đề đã nêu trong báo cáo 2026-11-22 đang chờ được chuyển tiếp, không phát lại thành escalation mới. Việc duyệt các báo cáo cũ không đồng nghĩa đã sửa. Không sửa cấu trúc, di chuyển hoặc xóa dữ liệu. Xem `wiki/reviews/_action-required.md`.
