# Hygiene Inspection — 2026-11-28

**Status:** pending  
**Issues found:** 8 nhóm (4 ERROR, 4 WARNING, 0 INFO)  
**Created:** 2026-11-28 23:30 +0700  
**Validator:** hygiene-inspector  
**Paths checked:** 234895 tên tệp bộ quét tham chiếu đếm trước khi ghi, không phải số đường dẫn được kiểm tra đầy đủ.

## Phạm vi và phương pháp

Đối chiếu `wiki/meta/folder-structure.md` v1.2. Bộ quét tham chiếu đi từ root, miễn phân loại sâu nhà tác nhân nhưng không cắt hoàn toàn `.git`, `.obsidian`, `node_modules` trước khi duyệt; con số trên bao gồm nhiều tên trong cây cài đặt, không phản ánh phạm vi KB thực sự được kiểm tra. Bộ quét ghi **313 phát hiện máy: 4 ERROR, 309 WARNING**. Chạy lại cùng mã với giới hạn xuất được bỏ trong bản chạy tạm để kiểm tra toàn bộ: 293 cảnh báo tệp con `memory/`, 15 bản sao archive, 1 tệp reviews; 4 ERROR riêng. Tám nhóm bên dưới không phải 313 phát hiện máy; hai nhóm về tồn đọng runtime và giới hạn đặc tả là kiểm tra bổ sung.

Đếm độc lập trước khi ghi, loại `.git`, `.obsidian`, `node_modules` ở mọi độ sâu, không theo symlink thư mục: `raw/` 242, `wiki/` 1592, `context/` 2, `scripts/` 5 tên tệp; `memory/` 293 tên. Đây là số tại thời điểm quét, không gồm báo cáo đang tạo. Kiểm tra bổ sung slug trong năm vùng `wiki/concepts`, `sources`, `tag`, `topic`, `drafts`: không thấy tên không đạt theo tập chữ Latin thường, chữ số ASCII, gạch nối, đuôi `.md` và tối đa 80 ký tự. Không có lỗi quyền truy cập trong phép đếm bổ sung. Bộ quét không xác minh đầy đủ mọi thư mục, tệp bắt buộc hay tên trong toàn bộ vùng; không khẳng định toàn bộ cây tuân thủ.

Các nhóm 1–7 tiếp tục từ [2026-11-27](2026-11-27_hygiene-report.md), đang chờ duyệt; không phát lại cảnh báo hệ thống cũ. Duyệt không đồng nghĩa đã sửa. Không đọc nội dung bộ nhớ hay nhật ký OpenClaw.

## Issue 1: Tệp root ngoài whitelist

**Path:** `DREAMS.md`  
**Severity:** ERROR  
**Category:** Path  
**Issue:** §2 không cho phép tệp này ở root.  
**Current:** Tệp tồn tại.  
**Expected:** Chỉ các tệp root liệt kê trong §2.  
**Suggested fix:** Giữ dữ liệu; xác định và xử lý tiến trình tạo trước khi xử lý vị trí.

## Issue 2: Thư mục bộ nhớ ngoài whitelist

**Path:** `memory/`  
**Severity:** ERROR  
**Category:** Orphan  
**Issue:** Thư mục root không được §2 cho phép.  
**Current:** 293 tên tệp con; 293 cảnh báo máy được gộp vào nhóm này.  
**Expected:** Bộ nhớ tác nhân thuộc nhà tác nhân theo §3.  
**Suggested fix:** Giữ dữ liệu theo phê duyệt; xử lý tiến trình tạo trước, không xóa để làm sạch báo cáo.

## Issue 3: Marker di chuyển ngoài whitelist

**Path:** `openclaw-workspace-state.json.migrated.43c9aa3dead1239e131cfd1ddf1a21fed91f1640ba72aeaf94714c3a31d1c72b.e79d1c6c-d9cd-4f3c-b9eb-65b970017373`  
**Severity:** ERROR  
**Category:** Path  
**Issue:** Marker root không được §2 cho phép.  
**Current:** Quét tên toàn cây, loại các thư mục nêu trên, thấy thêm `.openclaw/workspace-state.json.migrated.43c9aa3dead1239e131cfd1ddf1a21fed91f1640ba72aeaf94714c3a31d1c72b.fb077b94-2792-4ca2-b7d8-fc10c5575d51`. Cả hai được Git theo dõi; `git check-ignore --no-index -v` không trả rule cho từng đường dẫn. Marker trong nhà tác nhân không tự động là orphan theo §3.  
**Expected:** Không có marker ngoài whitelist root; quản lý trạng thái Git theo phê duyệt.  
**Suggested fix:** Xem xét rule wildcard cho cả hai vị trí trước khi gỡ khỏi index nếu được duyệt; không chỉ xóa bản trên đĩa.

## Issue 4: Symlink sai vị trí và đứt

**Path:** `wiki/HEARTBEAT.md`  
**Severity:** ERROR  
**Category:** Orphan  
**Issue:** Liên kết không thuộc whitelist wiki root §7.  
**Current:** Là symlink; `readlink` trả `../../.openclaw/HEARTBEAT.md`, `realpath` là `/home/julius/.openclaw/HEARTBEAT.md`; đích không tồn tại và `lexists` của liên kết là đúng.  
**Expected:** Không đặt HEARTBEAT tại wiki root.  
**Suggested fix:** Xác định và xử lý tiến trình tạo trước; Fix Agent xử lý liên kết sau phê duyệt. Không suy đoán tác nhân tạo.

## Issue 5: Bản sao archive chưa được quy định

**Path:** `wiki/reviews/archive/2026-09/`  
**Severity:** WARNING  
**Category:** Naming  
**Issue:** [SPEC CONFLICT] §7 không quy định rõ bản sao workflow trong archive.  
**Current:** 15 tên `*-backup-*.md` được bộ quét báo; không xác định là tệp mới.  
**Expected:** Vị trí và loại bản sao được quy định rõ.  
**Suggested fix:** Quyết định cho phép hoặc chọn nơi lưu hợp lệ; không tự đổi tên hay xóa.

## Issue 6: Artifact runtime được Git theo dõi

**Path:** `.hermes/config.yaml.bak.*`, `.hermes/kanban.db*`, `.hermes/MEMORY.md`  
**Severity:** WARNING  
**Category:** Path  
**Issue:** Git theo dõi dữ liệu runtime; đây là rủi ro quản lý, không tự kết luận là orphan theo §3.  
**Current:** `git ls-files` ghi 20 backup config, 5 mục `kanban.db*` và 1 `MEMORY.md`: 26 đường dẫn, bằng lượt 11-27.  
**Expected:** Xác định dữ liệu runtime nào được phép theo dõi; ignore không có tác dụng hồi tố.  
**Suggested fix:** Rà soát độ nhạy và lịch sử Git; nếu được duyệt, thêm rule phù hợp trước khi gỡ index. Không công bố nội dung.

## Issue 7: Giới hạn bộ quét và loại báo cáo

**Path:** `.hermes/skills/hygiene-inspector/references/scan-script.py`; `wiki/reviews/archive/2026-06/2026-06-15_spot-check-report.md`  
**Severity:** WARNING  
**Category:** Naming  
**Issue:** [SPEC CONFLICT] Bộ quét cho phép `spot-check-report`, nhưng §7 không liệt kê loại này.  
**Current:** Tệp spot-check tồn tại. Bộ quét không kiểm tra đầy đủ tên thư mục, tệp bắt buộc, tập ký tự slug và giới hạn 80 ký tự.  
**Expected:** Ngoại lệ workflow được quy định rõ; phép kiểm tra khớp quy chuẩn.  
**Suggested fix:** Làm rõ loại báo cáo và hoàn thiện bộ quét. §6–7 vừa yêu cầu `raw/raw.md`, `wiki/wiki.md` vừa cấm tệp tại root tương ứng; không coi hai chỉ mục bắt buộc là orphan.

## Issue 8: Tệp kết quả tạm ngoài whitelist reviews

**Path:** `wiki/reviews/.format-validation-current.txt`  
**Severity:** WARNING  
**Category:** Path  
**Issue:** [SPEC CONFLICT] Tệp kết quả mang tên công việc Format xuất hiện trong vùng reviews nhưng §7 không liệt kê loại `.txt` này. Đây là phát hiện mới so với báo cáo 11-27, không khẳng định thời điểm tạo.  
**Current:** Tệp 44.229 byte, mtime 2026-11-28 23:15:40 +0700, được Git theo dõi; `git check-ignore --no-index -v` không trả rule. Chưa xác minh tiến trình đang dùng tệp.  
**Expected:** Artifact công việc có vị trí và quy tắc lưu rõ ràng, không nằm ngoài whitelist.  
**Suggested fix:** Xác định thành phần sử dụng; làm rõ hoặc thay đổi vị trí lưu và rule Git sau khi được duyệt. Không xóa tệp trong lượt kiểm tra.

## Hành động

Chờ Julius duyệt. Giữ dữ liệu và xử lý tiến trình tạo trước. Không sửa cấu trúc, di chuyển hoặc xóa dữ liệu trong lượt này. Xem `wiki/reviews/_action-required.md`.
