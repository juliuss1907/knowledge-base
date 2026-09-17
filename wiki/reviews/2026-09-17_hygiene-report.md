# Hygiene Inspection — 2026-09-17

**Status:** pending
**Issues found:** 8 nhóm (4 ERROR, 3 WARNING, 1 INFO)
**Created:** 2026-09-17 23:33:50 +0700
**Validator:** hygiene-inspector
**Paths checked:** 1753 (1681 tệp, 72 thư mục)
**Machine findings:** 57 (4 ERROR, 53 WARNING), được đối chiếu và gom theo nguyên nhân; không phải 57 lỗi độc lập.

---

## Phạm vi và bằng chứng

1. Đọc toàn bộ `wiki/meta/folder-structure.md`, phiên bản 1.2; đối chiếu `TAGS.md` và báo cáo ngày 09-16 đã được Julius duyệt lúc 08:57 ngày 09-17. Duyệt không đồng nghĩa sửa xong.
2. Quét từ gốc kho, không theo liên kết thư mục. Loại `.git/`, `.obsidian/`, `node_modules/`; chỉ kiểm tra tầng đầu nhà tác nhân `.hermes/` và `.openclaw/`. Không đọc nội dung bộ nhớ hay nhật ký OpenClaw. Không lỗi quyền truy cập; không thiếu tệp bắt buộc; không thư mục rỗng trong phạm vi.
3. Bộ quét tham chiếu đếm 233787 tệp, gồm nhiều phần nội bộ tác nhân được miễn kiểm tra. **1753 là số đường dẫn thực sự thuộc phạm vi kiểm tra lần này.** Không so trực tiếp với 233751 của báo cáo trước để suy ra kho tăng/giảm.
4. Bộ quét tham chiếu cho 56 phát hiện; đối chiếu chặt quy chuẩn cho 57: thêm một báo cáo `spot-check` không có trong danh sách cho phép. 53 cảnh báo gồm 37 tệp dưới `memory/` và 16 tệp lưu trữ. Không bỏ qua 15 bản sao lưu chỉ vì tên chứa `-backup-`.
5. Gom 37 tệp `memory/` vào vấn đề thư mục gốc; gom 15 bản sao lưu thành một xung đột quy chuẩn. Bổ sung một nhóm mâu thuẫn trong quy chuẩn và một nhóm báo cáo cũ cần xem xét lưu trữ. Tổng: 8 nhóm, dưới giới hạn 20 mục/ngày.
6. Git tại thời điểm đối chiếu: `57e1c8b3d6da489139841e6f9dd72a3ca59ee1c3`. Từ mốc quét 09-16 23:31:00, Git ghi nhận 6 tệp mới: 3 bài gốc, 1 khái niệm, 1 nguồn, 1 chủ đề. Theo thời gian sửa tệp: 279 tệp wiki, 5 tệp raw, 5 tệp memory thay đổi. Thời gian sửa không đồng nghĩa tệp mới.

## Thay đổi so với 09-16

1. Bốn đường dẫn lỗi chính vẫn tồn tại. Chưa xác minh sửa xong mục nào trong bốn mục này.
2. `memory/`: 32 → 37 tệp. Năm đường dẫn có thời gian sửa sau mốc quét trước:
   - `memory/.dreams/session-corpus/2026-09-16.txt`
   - `memory/2026-09-17.md`
   - `memory/dreaming/deep/2026-09-17.md`
   - `memory/dreaming/light/2026-09-17.md`
   - `memory/dreaming/rem/2026-09-17.md`
3. Không phát hiện lỗi tên mới trong các vùng nội dung raw/wiki. Các cảnh báo lưu trữ là tồn đọng hoặc khoảng trống quy chuẩn, không khẳng định được tạo hôm nay.
4. Không phát lại cảnh báo hệ thống cho bốn lỗi đã biết. Tiếp tục theo dõi từ báo cáo 09-16 đã duyệt, chưa xác minh áp dụng. Sửa các kết luận quá mức của báo cáo trước: không khẳng định nguyên nhân tạo liên kết là công cụ đồng bộ; không khẳng định đích liên kết tồn tại khi kiểm tra thực tế cho kết quả ngược lại.

---

## Issue 1: DREAMS.md ngoài danh sách gốc — tiếp tục theo dõi

**Path:** `DREAMS.md`
**Severity:** ERROR
**Category:** Path
**Issue:** Tệp ở gốc không được §2 cho phép. Lịch sử báo cáo nhận diện đây là sản phẩm của chức năng dreaming; chức năng vận hành và danh sách đường dẫn chưa thống nhất.
**Current:** Tồn tại, được Git theo dõi; `git ls-files -s` trả về mục tương ứng.
**Expected:** Chỉ các tệp gốc được §2 liệt kê; dữ liệu tác nhân thuộc nhà tác nhân.
**Suggested fix:** Giữ nguyên dữ liệu theo ghi chú duyệt 09-17. Fix Agent/Julius xác định nơi ghi phù hợp hoặc cập nhật quy chuẩn nếu chủ ý giữ tại gốc. Không đề xuất xóa đơn thuần; lần kiểm tra này không truy cập bộ nhớ để suy diễn nguyên nhân.
**Theo dõi:** `2026-09-16_hygiene-report.md`, mục 1; đã duyệt, chưa xác minh sửa xong. Xung đột vận hành–quy chuẩn đã có bằng chứng lịch sử, không báo thành sự cố mới.

---

## Issue 2: memory/ ngoài danh sách gốc — 37 tệp phụ thuộc

**Path:** `memory/`
**Severity:** ERROR
**Category:** Orphan
**Issue:** Thư mục không nằm trong danh sách gốc §2; §3 quy định dữ liệu vận hành nằm trong nhà tác nhân. 37 cảnh báo tệp con có cùng nguyên nhân vị trí, không tính thành 37 lỗi độc lập.
**Current:** 37 tệp; 5 đường dẫn thay đổi sau mốc quét trước. Git không theo dõi tệp dưới thư mục; `.gitignore:84` khớp `memory/`.
**Expected:** Đường dẫn dữ liệu thống nhất với §2–3 hoặc ngoại lệ được Julius phê chuẩn và ghi vào quy chuẩn.
**Suggested fix:** Giữ `memory/` theo ghi chú duyệt 09-17. Xử lý tiến trình tạo dữ liệu trước; chỉ di chuyển sau khi xác nhận không mất dữ liệu. **Không chạy `rmdir memory/`, không xóa nội dung.**
**Theo dõi:** Báo cáo 09-16, mục 2; đã duyệt nhưng chưa có bằng chứng sửa vị trí. Tên và thời gian sửa được kiểm tra; nội dung bộ nhớ không được đọc.

---

## Issue 3: Dấu di chuyển dữ liệu còn ở gốc và trong Git

**Path:** `openclaw-workspace-state.json.migrated.43c9aa3dead1239e131cfd1ddf1a21fed91f1640ba72aeaf94714c3a31d1c72b.e79d1c6c-d9cd-4f3c-b9eb-65b970017373`
**Severity:** ERROR
**Category:** Path
**Issue:** Tệp phụ ngoài danh sách §2, vẫn được Git theo dõi.
**Current:** `git ls-files -s` xác nhận có mục; `git check-ignore -v --no-index` không trả về quy tắc khớp. Tệp gốc `openclaw-workspace-state.json` vắng mặt; biến thể `.migrated.*` vẫn tồn tại.
**Expected:** Không đưa dấu vận hành ngoài danh sách vào kho Git.
**Suggested fix:** Fix Agent thêm quy tắc `openclaw-workspace-state.json.migrated.*`, bỏ theo dõi bằng `git rm --cached` đúng tệp rồi tạo commit; giữ bản trên đĩa nếu runtime cần. Chỉ thêm `.gitignore` không làm tệp đang được theo dõi biến khỏi Git.
**Theo dõi:** Phụ lục báo cáo 09-08 và mục 3 báo cáo 09-16. Không có bằng chứng đã áp dụng sửa.

---

## Issue 4: Liên kết HEARTBEAT sai vùng, đích không tồn tại

**Path:** `wiki/HEARTBEAT.md`
**Severity:** ERROR
**Category:** Orphan
**Issue:** Tệp nằm ở gốc wiki ngoài ngoại lệ `wiki.md`; đồng thời là liên kết hỏng.
**Current:** Liên kết → `../../.openclaw/HEARTBEAT.md`; kiểm tra đích trả về không tồn tại. Không được Git theo dõi; `.gitignore:78` khớp `HEARTBEAT.md`.
**Expected:** HEARTBEAT thuộc nhà tác nhân; chỉ ngoại lệ liên kết tại gốc kho được §2 cho phép.
**Suggested fix:** Fix Agent xác định tác nhân tạo liên kết rồi xử lý liên kết sai vùng. Chưa có bằng chứng trực tiếp để kết luận công cụ đồng bộ nào tạo nó. Không cần `git rm --cached` cho liên kết không được Git theo dõi.
**Theo dõi:** Báo cáo 09-16, mục 4. Liên kết gốc `HEARTBEAT.md` không tồn tại là hợp lệ vì chỉ là mục tùy chọn; bốn liên kết định danh gốc còn lại đúng đích và hoạt động.

---

## Issue 5: [SPEC CONFLICT] Bản sao lưu không phải báo cáo trong vùng lưu trữ

**Path:** `wiki/reviews/archive/2026-09/`
**Severity:** WARNING
**Category:** Path
**Issue:** Có 15 tệp `*-backup-*.md`. Báo cáo trước gọi chúng là báo nhầm, nhưng §7 nói vùng reviews chỉ chứa đầu ra Hermes; không có ngoại lệ rõ cho bản sao nội dung. Không được âm thầm cho qua hoặc đổi tên chúng thành báo cáo.
**Current:** 15 bản sao, đã tồn tại theo báo cáo trước:

1. `2026-08-30_anthropic-cybersecurity-skills-backup-2026-09-01.md`
2. `2026-08-30_archify-backup-2026-09-01.md`
3. `2026-08-30_impeccable-backup-2026-09-01.md`
4. `2026-08-30_openviking-backup-2026-09-01.md`
5. `2026-08-30_posthog-backup-2026-09-01.md`
6. `2026-08-30_threeui-backup-2026-09-01.md`
7. `destination-vs-vehicle-backup-2026-07-20.md`
8. `is-there-anything-left-to-build-in-crypto-wintermute-backup-2026-07-20.md`
9. `memory-backup-2026-06-15.md`
10. `psychic-energy-backup-2026-07-20.md`
11. `raw-backlog-backup-2026-06-15.md`
12. `social-attraction-backup-2026-07-20.md`
13. `src_ai-engineering-skills-map-building-deploying-ai-applications-backup-2026-09-01.md`
14. `src_ai-engineering-skills-map-software-engineering-fundamentals-backup-2026-09-01.md`
15. `temp-content-backup-2026-06-15.md`

**Expected:** Quy tắc lưu bản sao rõ ràng, khác quy tắc tên báo cáo; thống nhất vị trí với §7.
**Suggested fix:** Julius quyết định cho phép loại bản sao này bằng quy chuẩn, hoặc Fix Agent đưa về nơi sao lưu phù hợp sau khi kiểm chứng an toàn dữ liệu. Không xóa, không đổi tên đại trà. Lần này chỉ kiểm tra đường dẫn, không đọc nội dung các bản sao.

---

## Issue 6: [SPEC CONFLICT] Loại báo cáo kiểm tra mẫu chưa được cho phép

**Path:** `wiki/reviews/archive/2026-06/2026-06-15_spot-check-report.md`
**Severity:** WARNING
**Category:** Naming
**Issue:** Bộ quét tham chiếu cho phép `spot-check`; §7 chỉ liệt kê `output`, `format`, `hygiene`. Hai danh sách lệch nhau.
**Current:** Tệp lưu trữ mang loại `spot-check`; lần đối chiếu chặt này mới đưa khoảng trống quy chuẩn vào thống kê. Không coi là tệp mới tạo hôm nay.
**Expected:** Danh sách loại báo cáo trong công cụ khớp quy chuẩn.
**Suggested fix:** Julius xác nhận loại báo cáo kiểm tra mẫu; cập nhật quy chuẩn nếu cần giữ. Không tự đổi loại báo cáo lịch sử chỉ để qua biểu thức kiểm tra.

---

## Issue 7: [SPEC CONFLICT] Các điều khoản quy chuẩn tự mâu thuẫn

**Path:** `wiki/meta/folder-structure.md`
**Severity:** WARNING
**Category:** Path
**Issue:** Một số câu cấm chung xung đột với ngoại lệ và quyền sở hữu nhà tác nhân.
**Current:** §6 liệt kê `raw.md` nhưng dòng 160 cấm tệp tại gốc raw; §7 liệt kê `wiki.md` nhưng dòng 201 cấm tệp tại gốc wiki. Cây meta dòng 170–173 chỉ cho hai tệp, nhưng dòng 195 yêu cầu ba tệp gồm `index-spec.md`. §3 cho phép dữ liệu runtime tự do, §4 lại cấm thư mục con và tệp không phải Markdown trong skills.
**Expected:** Mỗi ngoại lệ và phạm vi áp dụng được nêu nhất quán.
**Suggested fix:** Fix Agent/Julius thống nhất văn bản. Lần này ưu tiên danh sách ngoại lệ cụ thể và quyền sở hữu runtime §3; không báo sai các chỉ mục hợp lệ hay nội bộ kỹ năng. Không sửa quy chuẩn trong lần kiểm tra.

---

## Issue 8: Báo cáo cũ có thể đưa vào lưu trữ

**Path:** `wiki/reviews/`
**Severity:** INFO
**Category:** Orphan
**Issue:** 38 báo cáo tên chuẩn đã quá 30 ngày, vẫn ở vùng hoạt động.
**Current:** Đếm từ ngày trong tên tệp, mốc 2026-09-17; không dùng thời gian sửa để suy ra tuổi báo cáo.
**Expected:** Xem xét chuyển các báo cáo đã hoàn tất vào `archive/YYYY-MM/`; không mặc định tất cả 38 báo cáo đủ điều kiện.
**Suggested fix:** Fix Agent đối chiếu trạng thái từng báo cáo trước khi chuyển. Báo cáo còn chờ duyệt hoặc chưa xử lý phải giữ truy vết. Đây là đề xuất dọn, không phải lỗi chặn.

---

## Việc cần làm

1. Giữ nguyên `DREAMS.md` và `memory/`; xử lý nguồn tạo trước. Không nhầm “đã duyệt” với “đã sửa”.
2. Fix Agent xử lý theo dõi Git của dấu `.migrated.*` và nguồn tạo liên kết HEARTBEAT sai vùng.
3. Julius chốt các xung đột quy chuẩn tại mục 5–7. Không tự nới danh sách để làm số lỗi giảm.
4. Xem xét lưu trữ báo cáo cũ sau khi xác nhận trạng thái; không xóa tự động.

Chỉ ghi báo cáo và cập nhật `wiki/reviews/_action-required.md`. Không sửa khái niệm, nguồn, dữ liệu bộ nhớ, quy chuẩn, Git hay cấu trúc thư mục.
