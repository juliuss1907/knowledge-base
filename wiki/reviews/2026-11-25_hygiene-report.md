# Hygiene Inspection — 2026-11-25

**Status:** approved
**Approved by:** Julius
**Issues found:** 7 nhóm (4 ERROR, 3 WARNING, 0 INFO)  
**Created:** 2026-11-25 23:30 +0700  
**Validator:** hygiene-inspector  
**Paths checked:** 234879 tên tệp được bộ quét đếm trước khi ghi; không phải số đường dẫn được kiểm tra đầy đủ.

## Phạm vi và giới hạn

Đối chiếu `wiki/meta/folder-structure.md` v1.2. Bộ quét tham chiếu duyệt cây từ root; bỏ qua phân loại sâu trong agent home. Lưu ý: mã bộ quét không thực sự cắt `node_modules/` hay `.obsidian/` khỏi `os.walk`; nó cũng không cắt cây `.git` trước khi duyệt, dù bỏ qua các thư mục con `.git` trong vòng xử lý. Do đó số 234879 là số tên tệp máy đếm theo chính mã bộ quét, bao gồm nội bộ agent home và không phải phạm vi xác nhận tuân thủ. Không so sánh số này với một phép đếm có quy tắc loại trừ khác.

Bộ quét ghi 312 phát hiện chưa gộp: 4 ERROR và 308 WARNING; chỉ xuất chi tiết 20 phát hiện đầu. Phép đếm độc lập ghi 293 tên tệp dưới `memory/` và 15 tên tệp chứa `-backup-` trong archive. Hai nhóm cảnh báo này tương ứng với tổng 308 WARNING, nhưng do kết quả chi tiết bị cắt, không khẳng định đã xác minh từng cảnh báo máy. Hai nhóm WARNING bổ sung dưới đây được kiểm tra riêng, không cộng vào số máy. Bảy nhóm không phải 312 phát hiện. Trước khi ghi, phép đếm tên tệp tại `raw/`, `wiki/`, `context/`, `scripts/` lần lượt là 241, 1579, 2, 5; phép đếm này loại thư mục `.git`, `.obsidian`, `node_modules` ở mọi độ sâu và có thể tính symlink tệp.

**CARRIED FORWARD từ 2026-11-24**, báo cáo còn pending: bốn đường dẫn chính vẫn tồn tại, hai marker vẫn được Git theo dõi, và tồn đọng runtime vẫn còn. Chưa có bằng chứng Fix Agent đã xử lý. Duyệt không đồng nghĩa đã sửa. Không đọc nội dung bộ nhớ hoặc nhật ký OpenClaw.

## Issue 1: Tệp root ngoài whitelist

**Path:** `DREAMS.md`  
**Severity:** ERROR  
**Category:** Path  
**Issue:** Tệp tồn tại ở root nhưng không có trong whitelist §2.  
**Current:** Tệp tồn tại.  
**Expected:** Root chỉ chứa đường dẫn được phép.  
**Suggested fix:** Giữ dữ liệu theo phê duyệt; xác định và xử lý tiến trình tạo trước khi xử lý vị trí.

## Issue 2: Thư mục bộ nhớ ngoài whitelist

**Path:** `memory/`  
**Severity:** ERROR  
**Category:** Orphan  
**Issue:** Thư mục root không được §2 cho phép; 293 tên tệp con được gộp vào nhóm này.  
**Current:** Có 293 tên tệp trong cây theo `os.walk`.  
**Expected:** Bộ nhớ tác nhân thuộc agent home theo §3.  
**Suggested fix:** Giữ dữ liệu; xử lý tiến trình tạo trước rồi thực hiện phương án đã duyệt. Không xóa dữ liệu chỉ để làm sạch báo cáo.

## Issue 3: Marker di chuyển ngoài whitelist

**Path:** `openclaw-workspace-state.json.migrated.43c9aa3dead1239e131cfd1ddf1a21fed91f1640ba72aeaf94714c3a31d1c72b.e79d1c6c-d9cd-4f3c-b9eb-65b970017373`  
**Severity:** ERROR  
**Category:** Path  
**Issue:** Marker root không được §2 cho phép.  
**Current:** Marker root và `.openclaw/workspace-state.json.migrated.43c9aa3dead1239e131cfd1ddf1a21fed91f1640ba72aeaf94714c3a31d1c72b.fb077b94-2792-4ca2-b7d8-fc10c5575d51` tồn tại và được Git theo dõi. Quét tên toàn cây trừ `.git` và `node_modules` thấy hai marker. Với marker root, `git check-ignore --no-index -v` không trả rule.  
**Expected:** Không có marker runtime ngoài whitelist root; trạng thái Git được xử lý theo phê duyệt.  
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
**Issue:** [SPEC CONFLICT] Có 15 bản `*-backup-*.md` trong cây archive; §7 không quy định rõ bản sao workflow trong archive.  
**Current:** Có 15 tên tệp chứa `-backup-` trong archive.  
**Expected:** Vị trí và loại bản sao được quy định rõ.  
**Suggested fix:** Quyết định cho phép hoặc chọn nơi lưu hợp lệ; không tự đổi tên hay xóa.

## Issue 6: Artifact runtime được Git theo dõi

**Path:** `.hermes/config.yaml.bak.*`, `.hermes/kanban.db*`, `.hermes/MEMORY.md`  
**Severity:** WARNING  
**Category:** Path  
**Issue:** Git theo dõi dữ liệu runtime; đây là rủi ro quản lý, không tự kết luận là orphan theo §3.  
**Current:** `git ls-files -s` ghi 20 backup config, 5 mục `kanban.db*` và `MEMORY.md`: 26 đường dẫn, bằng số ngày 11-24. `git check-ignore --no-index -v` không trả rule cho backup config mới nhất trong danh sách.  
**Expected:** Xác định dữ liệu runtime nào được phép theo dõi; ignore không có tác dụng hồi tố.  
**Suggested fix:** Rà soát độ nhạy và lịch sử Git; nếu được duyệt, thêm rule phù hợp trước khi gỡ index. Không công bố nội dung.

## Issue 7: Giới hạn bộ quét và loại báo cáo

**Path:** `.hermes/skills/hygiene-inspector/references/scan-script.py`; `wiki/reviews/archive/2026-06/2026-06-15_spot-check-report.md`  
**Severity:** WARNING  
**Category:** Naming  
**Issue:** [SPEC CONFLICT] Bộ quét cho phép `spot-check-report`, nhưng §7 không liệt kê loại này. Bộ quét có giới hạn về kiểm tra tên thư mục, tệp bắt buộc, tập ký tự slug và giới hạn 80 ký tự; kết quả chi tiết bị cắt sau 20 phát hiện.  
**Current:** Đây là tồn đọng đã báo ngày 11-24, không khẳng định là tệp mới. Quy tắc cắt thư mục trong mô tả cũ cũng không khớp mã bộ quét như nêu ở phần phạm vi.  
**Expected:** Ngoại lệ workflow được quy định rõ và phép kiểm tra khớp quy chuẩn.  
**Suggested fix:** Làm rõ loại báo cáo và hoàn thiện kiểm tra; §6–7 vừa yêu cầu `raw/raw.md`, `wiki/wiki.md` vừa cấm tệp tại root tương ứng, nên không coi hai chỉ mục bắt buộc là orphan.

## Hành động

Chờ Julius duyệt. Giữ dữ liệu và xử lý tiến trình tạo trước. Không sửa cấu trúc, di chuyển hoặc xóa dữ liệu trong lượt kiểm tra này. Xem `wiki/reviews/_action-required.md`.
