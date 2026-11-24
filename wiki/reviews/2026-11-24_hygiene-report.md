# Hygiene Inspection — 2026-11-24

**Status:** pending  
**Issues found:** 7 nhóm (4 ERROR, 3 WARNING, 0 INFO)  
**Created:** 2026-11-24 23:30 +0700  
**Validator:** hygiene-inspector  
**Paths checked:** 234872 tên tệp bộ quét đếm trước khi ghi; không phải số đường dẫn được kiểm tra đầy đủ.

## Phạm vi và phương pháp

Đối chiếu `wiki/meta/folder-structure.md` v1.2. Bộ quét tham chiếu duyệt cây, bỏ `.git`, `.obsidian`, `node_modules`; nội bộ agent home được miễn kiểm tra orphan ở độ sâu lớn. Số đếm máy bao gồm nội bộ agent home, không phải số đường dẫn được kiểm tra đầy đủ. Trước khi ghi, phép đếm riêng bằng `os.walk` cùng các thư mục loại trừ trên ghi nhận `raw/` 241, `wiki/` 1574, `context/` 2, `scripts/` 5 tên tệp; có thể bao gồm symlink tệp.

Bộ quét ghi 312 phát hiện: 4 ERROR, 308 WARNING. Trong đó 293 cảnh báo tệp con `memory/` được gộp vào Issue 2; 15 cảnh báo bản sao archive gộp vào Issue 5. Issue 6 và 7 là kiểm tra bổ sung ngoài số máy. Bảy nhóm không phải 312 phát hiện riêng lẻ. Tổng máy bằng ngày 11-23; số bằng nhau không chứng minh từng đường dẫn không đổi. Bộ quét chỉ xuất tối đa 20 phát hiện chi tiết; không coi đây là chứng nhận toàn bộ quy tắc đã được kiểm tra. Không đọc nội dung bộ nhớ hoặc nhật ký OpenClaw.

Các vấn đề tương ứng đã nêu tại `2026-11-23_hygiene-report.md`, đang chờ duyệt: **CARRIED FORWARD từ 2026-11-23**. Các đường dẫn chính vẫn tồn tại; chưa có bằng chứng sửa các vấn đề này. Không phát lại escalation cũ. Duyệt không đồng nghĩa đã sửa.

## Issue 1: Tệp root ngoài whitelist

**Path:** `DREAMS.md`  
**Severity:** ERROR  
**Category:** Path  
**Issue:** Tệp tồn tại tại root nhưng không có trong whitelist §2.  
**Current:** `DREAMS.md` tồn tại.  
**Expected:** Root chỉ chứa đường dẫn được phép.  
**Suggested fix:** Giữ dữ liệu theo phê duyệt; xác định và xử lý tiến trình ghi trước khi xử lý vị trí.

## Issue 2: Thư mục bộ nhớ ngoài whitelist

**Path:** `memory/`  
**Severity:** ERROR  
**Category:** Orphan  
**Issue:** Thư mục root không được §2 cho phép; gộp 293 cảnh báo máy về tệp con.  
**Current:** Có 293 tên tệp trong cây `memory/` theo phép đếm `os.walk`.  
**Expected:** Bộ nhớ tác nhân thuộc agent home theo §3.  
**Suggested fix:** Giữ dữ liệu; xử lý tiến trình tạo trước rồi thực hiện phương án đã duyệt. Không xóa dữ liệu chỉ để làm sạch báo cáo.

## Issue 3: Marker di chuyển ngoài whitelist

**Path:** `openclaw-workspace-state.json.migrated.43c9aa3dead1239e131cfd1ddf1a21fed91f1640ba72aeaf94714c3a31d1c72b.e79d1c6c-d9cd-4f3c-b9eb-65b970017373`  
**Severity:** ERROR  
**Category:** Path  
**Issue:** Marker root không được §2 cho phép.  
**Current:** Marker root và `.openclaw/workspace-state.json.migrated.43c9aa3dead1239e131cfd1ddf1a21fed91f1640ba72aeaf94714c3a31d1c72b.fb077b94-2792-4ca2-b7d8-fc10c5575d51` tồn tại và được Git theo dõi; quét tên toàn cây, trừ các thư mục loại trừ, thấy hai marker này.  
**Expected:** Không có marker runtime ngoài whitelist root; trạng thái Git được xử lý theo phê duyệt.  
**Suggested fix:** Kiểm tra rule wildcard trước khi gỡ khỏi index nếu được duyệt; không chỉ xóa bản trên đĩa.

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
**Issue:** [SPEC CONFLICT] Có 15 bản `*-backup-*.md` trong cây archive; §7 không quy định rõ bản sao workflow trong archive.  
**Current:** Có 15 tên tệp chứa `-backup-` trong archive; bộ quét ghi 15 cảnh báo liên quan.  
**Expected:** Vị trí và loại bản sao được quy định rõ.  
**Suggested fix:** Quyết định cho phép hoặc chọn nơi lưu hợp lệ; không tự đổi tên hay xóa.

## Issue 6: Artifact runtime được Git theo dõi

**Path:** `.hermes/config.yaml.bak.*`, `.hermes/kanban.db*`, `.hermes/MEMORY.md`  
**Severity:** WARNING  
**Category:** Path  
**Issue:** Git theo dõi dữ liệu runtime; đây là rủi ro quản lý, không tự kết luận là orphan theo §3.  
**Current:** `git ls-files -s` ghi 20 backup config, 5 mục `kanban.db*` và `MEMORY.md`: 26 đường dẫn, bằng số ngày 11-23.  
**Expected:** Xác định dữ liệu runtime nào được phép theo dõi; ignore không có tác dụng hồi tố.  
**Suggested fix:** Rà soát độ nhạy và lịch sử Git; nếu được duyệt, thêm rule phù hợp trước khi gỡ index. Không công bố nội dung.

## Issue 7: Giới hạn bộ quét và loại báo cáo

**Path:** `.hermes/skills/hygiene-inspector/references/scan-script.py`; `wiki/reviews/archive/2026-06/2026-06-15_spot-check-report.md`  
**Severity:** WARNING  
**Category:** Naming  
**Issue:** [SPEC CONFLICT] Bộ quét cho phép `spot-check-report`, nhưng §7 không liệt kê loại này. Bộ quét không tự xác nhận đầy đủ tên thư mục, tệp bắt buộc, tập ký tự slug và giới hạn 80 ký tự.  
**Current:** Biểu thức trong script cho phép `spot-check`; đây là tồn đọng đã báo ngày 11-23, không khẳng định là tệp mới.  
**Expected:** Ngoại lệ workflow được quy định rõ và phép kiểm tra khớp quy chuẩn.  
**Suggested fix:** Làm rõ loại báo cáo và hoàn thiện kiểm tra; quy chuẩn §6–7 cũng vừa yêu cầu `raw/raw.md`, `wiki/wiki.md` vừa cấm tệp tại root tương ứng, nên không coi hai chỉ mục bắt buộc là orphan.

## Hành động

Chờ Julius duyệt. Giữ dữ liệu và xử lý tiến trình tạo trước. Không sửa cấu trúc, di chuyển hoặc xóa dữ liệu trong lượt kiểm tra này. Xem `wiki/reviews/_action-required.md`.
