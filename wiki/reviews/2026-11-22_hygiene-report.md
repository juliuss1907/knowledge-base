# Hygiene Inspection — 2026-11-22

**Status:** pending  
**Issues found:** 7 nhóm (4 ERROR, 3 WARNING, 0 INFO)  
**Created:** 2026-11-22 23:30:34 +0700  
**Validator:** hygiene-inspector  
**Paths checked:** 234865 tên tệp được bộ quét tham chiếu đếm trước khi ghi báo cáo; không phải số đường dẫn thực sự được kiểm tra đầy đủ.

## Phạm vi và đối chiếu

Đối chiếu `wiki/meta/folder-structure.md` v1.2. Bộ quét đi qua cây, kể cả nhiều nội bộ agent home; con số máy không phải phạm vi kiểm tra theo quy chuẩn. Trong `raw/`, `wiki/`, `context/`, `scripts/`, trước khi ghi có 1815 tên tệp (240 + 1568 + 2 + 5), theo `os.walk`, loại các thư mục `.git`, `.obsidian`, `node_modules`; gồm tên tệp và symlink tệp. Không đọc nội dung bộ nhớ hoặc nhật ký OpenClaw.

Bộ quét ghi **312 phát hiện máy: 4 ERROR, 308 WARNING**. Trong đó 293 WARNING là tệp con `memory/`, gộp vào Issue 2; 15 WARNING là bản sao archive, gộp vào Issue 5. Issue 6 và 7 là kiểm tra bổ sung, không nằm trong số máy. So với báo cáo 2026-11-21: 308 → 312 phát hiện máy; riêng cảnh báo tệp con `memory/` tăng 289 → 293. Không suy đoán nguyên nhân tạo tệp. Báo cáo trước đã được duyệt để xử lý; không có nghĩa là đã sửa.

Kiểm tra bổ sung thư mục và slug trong vùng nội dung không phát hiện trường hợp sai theo phép kiểm tra đã chạy. Các tệp bắt buộc root, context, raw index và wiki meta được kiểm tra đều tồn tại. Đây không phải chứng nhận mọi quy tắc được kiểm tra đầy đủ; xem Issue 7.

## Issue 1: Tệp ngoài whitelist ở root

**Path:** `DREAMS.md`  
**Severity:** ERROR  
**Category:** Path  
**Issue:** Tệp tồn tại ngoài whitelist §2.  
**Current:** Có tệp tại root.  
**Expected:** Root chỉ chứa các tên được phép.  
**Suggested fix:** Giữ dữ liệu theo ghi chú duyệt; xác định và xử lý tiến trình ghi trước khi Fix Agent xử lý vị trí.

## Issue 2: Bộ nhớ ngoài whitelist

**Path:** `memory/`  
**Severity:** ERROR  
**Category:** Orphan  
**Issue:** Thư mục root không được §2 cho phép; 293 WARNING máy về tệp con được gộp ở đây.  
**Current:** Thư mục tồn tại; lượt trước có 289 WARNING tệp con.  
**Expected:** Bộ nhớ tác nhân thuộc agent home theo §3.  
**Suggested fix:** Giữ dữ liệu theo phê duyệt; xử lý tiến trình tạo trước, sau đó Fix Agent thực hiện phương án được duyệt. Không xóa dữ liệu để làm sạch báo cáo.

## Issue 3: Marker di chuyển ngoài whitelist

**Path:** `openclaw-workspace-state.json.migrated.43c9aa3dead1239e131cfd1ddf1a21fed91f1640ba72aeaf94714c3a31d1c72b.e79d1c6c-d9cd-4f3c-b9eb-65b970017373`  
**Severity:** ERROR  
**Category:** Path  
**Issue:** Marker ngoài whitelist §2. Marker này và biến thể `.openclaw/workspace-state.json.migrated.43c9aa3dead1239e131cfd1ddf1a21fed91f1640ba72aeaf94714c3a31d1c72b.fb077b94-2792-4ca2-b7d8-fc10c5575d51` còn trong index Git.  
**Current:** Hai đường dẫn trên đĩa và được Git theo dõi.  
**Expected:** Không có marker runtime ngoài whitelist root; xử lý trạng thái Git theo phê duyệt.  
**Suggested fix:** Kiểm tra và bổ sung rule cho biến thể nếu cần trước khi gỡ khỏi index theo phê duyệt; không chỉ xóa bản trên đĩa.

## Issue 4: Symlink HEARTBEAT sai vị trí và bị đứt

**Path:** `wiki/HEARTBEAT.md`  
**Severity:** ERROR  
**Category:** Orphan  
**Issue:** Liên kết không thuộc whitelist wiki root §7.  
**Current:** Là symlink, đích thô `../../.openclaw/HEARTBEAT.md` phân giải thành `/home/julius/.openclaw/HEARTBEAT.md`, không tồn tại; bản thân liên kết tồn tại.  
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
**Issue:** `git ls-files -s` xác nhận 20 backup config, 5 mục `kanban.db*` và `MEMORY.md` còn được theo dõi, không đổi so với 2026-11-21. Đây là rủi ro quản lý runtime, không tự kết luận là orphan theo §3.  
**Current:** 26 đường dẫn trong index Git. Mẫu backup config được kiểm tra không khớp rule ignore.  
**Expected:** Xác định dữ liệu runtime nào được phép theo dõi; ignore không có tác dụng hồi tố.  
**Suggested fix:** Rà soát độ nhạy và lịch sử Git; nếu được duyệt, thêm rule phù hợp trước khi gỡ index. Không công bố nội dung tệp.

## Issue 7: Giới hạn bộ quét và loại báo cáo chưa được quy định

**Path:** `.hermes/skills/hygiene-inspector/references/scan-script.py`; `wiki/reviews/archive/2026-06/2026-06-15_spot-check-report.md`  
**Severity:** WARNING  
**Category:** Naming  
**Issue:** [SPEC CONFLICT] Bộ quét cho phép loại `spot-check-report`, nhưng §7 không liệt kê loại này. Tệp thực tế đã tồn tại, không phải phát hiện mới. Bộ quét cũng không tự xác nhận đầy đủ thư mục, tệp bắt buộc, tập ký tự slug và giới hạn 80 ký tự.  
**Current:** Có tệp spot-check trong archive; lượt này đã bổ sung kiểm tra tên và một số tệp bắt buộc, nhưng không chứng minh toàn bộ quy tắc.  
**Expected:** Ngoại lệ workflow được quy định rõ và các phép kiểm tra khớp quy chuẩn.  
**Suggested fix:** Làm rõ loại báo cáo thực tế; hoàn thiện bộ quét và đối chiếu các ngoại lệ có chủ đích.

## Hành động

Chờ Julius duyệt báo cáo. Các vấn đề tồn đọng không được phát lại như một escalation mới. Không sửa cấu trúc, di chuyển hoặc xóa dữ liệu. Xem `wiki/reviews/_action-required.md`.
