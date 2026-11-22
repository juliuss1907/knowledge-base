# Hygiene Inspection — 2026-11-19

**Status:** approved
**Approved by:** Julius
**Issues found:** 7 nhóm (4 ERROR, 3 WARNING, 0 INFO)
**Created:** 2026-11-19 23:30:22 +07
**Validator:** hygiene-inspector
**Paths checked:** 234819 lượt đếm tên tệp của bộ quét trước khi ghi báo cáo; không phải số đường dẫn thực sự được kiểm tra theo quy chuẩn.

## Phạm vi và giới hạn

Bộ quét tham chiếu đi qua cây, nhưng không cắt hẳn `.git/`, `.obsidian/`, `node_modules/` và nội bộ agent home trước khi đếm; số 234819 bao gồm nội bộ runtime và không dùng làm quy mô KB. Nội bộ `.hermes/` và `.openclaw/` được miễn kiểm tra orphan ở độ sâu lớn hơn một. Kiểm tra bổ sung chỉ dùng tên đường dẫn và metadata, không đọc bộ nhớ hay nhật ký OpenClaw. Bốn vùng `raw/`, `wiki/`, `context/`, `scripts/` có lần lượt 239, 1535, 2, 5 tệp thường hoặc symlink trước khi ghi báo cáo; bao gồm vùng reviews. Bộ quét không kiểm tra đầy đủ whitelist thư mục con, giới hạn slug 80 ký tự, tập ký tự chính xác và tệp bắt buộc. Vì vậy không khẳng định toàn bộ cây tuân thủ. Số phát hiện máy là 300: 4 ERROR, 296 WARNING, không phải 7 nhóm báo cáo; 281 WARNING là tệp con của `memory/`, 15 là bản sao trong archive. Giới hạn 20 nhóm/ngày được giữ.

## Issue 1: Tệp ngoài whitelist ở root

**Path:** `DREAMS.md`  
**Severity:** ERROR  
**Category:** Path  
**Issue:** Tệp không nằm trong whitelist §2. CARRIED FORWARD từ báo cáo 2026-11-07 còn pending; chưa có bằng chứng xử lý triệt để.  
**Current:** Tệp tồn tại tại root.  
**Expected:** Root chỉ chứa các tên được cho phép.  
**Suggested fix:** Giữ dữ liệu theo ghi chú duyệt; xác định và sửa tiến trình ghi trước khi Fix Agent xử lý vị trí.

## Issue 2: Thư mục bộ nhớ ngoài whitelist

**Path:** `memory/`  
**Severity:** ERROR  
**Category:** Orphan  
**Issue:** Thư mục ở root không được §2 cho phép; bộ quét báo thêm 281 WARNING cho các tệp con. CARRIED FORWARD từ 2026-11-07 pending, không phát lại escalation.  
**Current:** `memory/` và các tệp con tồn tại.  
**Expected:** Bộ nhớ tác nhân nằm trong agent home theo §3.  
**Suggested fix:** Giữ dữ liệu theo ghi chú duyệt; xử lý tiến trình tạo trước, sau đó Fix Agent thực hiện phương án đã duyệt. Không xóa dữ liệu chỉ để làm sạch báo cáo.

## Issue 3: Marker di chuyển tại root

**Path:** `openclaw-workspace-state.json.migrated.43c9aa3dead1239e131cfd1ddf1a21fed91f1640ba72aeaf94714c3a31d1c72b.e79d1c6c-d9cd-4f3c-b9eb-65b970017373`  
**Severity:** ERROR  
**Category:** Path  
**Issue:** Không có trong §2; `git ls-files -s` xác nhận đã tracked. CARRIED FORWARD 2026-11-07 pending.  
**Current:** Marker tồn tại tại root; `git check-ignore --no-index` không tìm được rule cho đường dẫn này.  
**Expected:** Không có marker runtime ngoài whitelist.  
**Suggested fix:** Sau phê duyệt, thêm rule bao phủ biến thể trước khi gỡ khỏi index; kiểm tra cả marker tương ứng ở `.openclaw/` đã tracked. Không chỉ xóa bản trên đĩa.

## Issue 4: Symlink HEARTBEAT ngoài vị trí

**Path:** `wiki/HEARTBEAT.md`  
**Severity:** ERROR  
**Category:** Orphan  
**Issue:** Symlink tại wiki root không thuộc whitelist §7. CARRIED FORWARD 2026-11-07 pending.  
**Current:** `readlink` là `../../.openclaw/HEARTBEAT.md`, `realpath` là `/home/julius/.openclaw/HEARTBEAT.md`; đích không tồn tại.  
**Expected:** Không đặt HEARTBEAT tại wiki root.  
**Suggested fix:** Xác định và sửa tiến trình tạo symlink; Fix Agent xử lý liên kết sau phê duyệt. Không suy đoán tác nhân tạo.

## Issue 5: Bản sao trong archive không được quy định

**Path:** `wiki/reviews/archive/2026-09/`  
**Severity:** WARNING  
**Category:** Naming  
**Issue:** [SPEC CONFLICT] 15 bản `*-backup-*.md` được bộ quét báo sai tên báo cáo. §7 chỉ nêu archive báo cáo; chưa có ngoại lệ rõ cho bản sao của workflow. Đây là phát hiện gộp, không phải 15 nhóm độc lập.  
**Current:** 15 tệp backup hiện diện, bao gồm `memory-backup-2026-06-15.md` và `2026-08-30_archify-backup-2026-09-01.md`.  
**Expected:** Tên và loại trong archive có quy định rõ.  
**Suggested fix:** Julius quyết định cho phép bản sao tại đây hoặc chọn nơi lưu hợp lệ; không tự đổi tên hay xóa.

## Issue 6: Nội bộ runtime còn được Git theo dõi

**Path:** `.hermes/config.yaml.bak.*`, `.hermes/kanban.db*`, `.hermes/MEMORY.md`  
**Severity:** WARNING  
**Category:** Path  
**Issue:** Kiểm tra metadata bổ sung cho thấy 20 backup config, 5 mục `kanban.db*` và `MEMORY.md` vẫn tracked. So với 19 backup config được báo 2026-11-06, có thêm `config.yaml.bak.20261113_200709`. Đây là rủi ro quản lý runtime, không tự kết luận là vi phạm orphan của §3.  
**Current:** Rule `MEMORY.md` tồn tại nhưng không loại tệp đã tracked; không tìm thấy rule qua `git check-ignore --no-index` cho backup config được kiểm tra và `kanban.db`.  
**Expected:** Quyết định rõ dữ liệu runtime nào được phép theo dõi; rule ignore không có tác dụng hồi tố với tệp đã tracked.  
**Suggested fix:** Rà soát nhạy cảm và lịch sử Git; thêm rule trước khi gỡ index theo phê duyệt. Không công bố nội dung các tệp.

## Issue 7: Giới hạn bộ quét đối với whitelist

**Path:** `wiki/meta/folder-structure.md` §6–§8; `.hermes/skills/hygiene-inspector/references/scan-script.py`  
**Severity:** WARNING  
**Category:** Naming  
**Issue:** Bộ quét chấp nhận `spot-check-report` dù §7 không liệt kê loại này; regex slug dùng dải Unicode rộng và không thực thi giới hạn 80 ký tự. Chưa thấy `spot-check` ở reviews root trong lượt kiểm tra.  
**Current:** Bộ quét và quy chuẩn không hoàn toàn đồng bộ.  
**Expected:** Kiểm tra tập ký tự chữ thường, độ dài và danh sách loại báo cáo theo quy chuẩn.  
**Suggested fix:** [SPEC CONFLICT] Làm rõ ngoại lệ workflow rồi cập nhật bộ quét tương ứng; kiểm tra lại tên trên toàn bộ vùng nội dung.

## Đối chiếu và hành động

Báo cáo 2026-11-07 ghi 4 ERROR và 16 WARNING trong 20 phát hiện đầu, nhưng phần thân gộp 16 WARNING thành một mục; đây không phải 20 nhóm độc lập. Lượt này không suy ra đã sửa các mục cũ chỉ từ trạng thái phê duyệt. Không sửa cấu trúc, không di chuyển hoặc xóa dữ liệu. Xem `_action-required.md` để duyệt.
