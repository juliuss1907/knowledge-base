# Output Validation — 2026-11-21

**Status:** approved
**Approved by:** Julius
**Issues found:** 3 (0 ERROR, 3 WARNING, 0 INFO)
**Created:** 2026-11-21 23:00:24 +0700
**Validator:** output-validator

## Phạm vi và giới hạn

- Quét cơ học 875 tệp: 231 sources và 644 concepts. Kiểm tra chi tiết 12 tệp mang ngày biên soạn hoặc cập nhật 2026-11-21: 6 sources và 6 concepts. Báo cáo trước ngày 11-20 không có nội dung mới cần kiểm tra chi tiết.
- Đã đối chiếu 12 tệp với sáu bản raw tương ứng; riêng bản chép Pstack chứa dòng transcript quá dài bị công cụ đọc rút gọn, nên chưa xác minh toàn bộ nội dung video. Chưa xác minh độc lập các trang web, video hay tuyên bố của nhà cung cấp. Không thể kết luận toàn bộ 875 tệp đã được kiểm tra chi tiết về sự kiện, tính đầy đủ, mạch lạc và tiếng Việt.
- Không phát hiện mẫu mất chữ i trong bốn nhóm quét bổ sung. Các đích wikilink trong thân 12 tệp đều tồn tại theo tên chính xác. Quick-scan báo 117 định nghĩa một câu và 77 concepts ít ý theo heuristic; chưa xác minh từng tệp và không tính là lỗi mới.
- Sáu concept mới đều có trạng thái `draft`; không tự thay đổi trạng thái hay sửa nội dung.

## Issue 1: Khái quát khả năng hoạt động của điện thoại cố định khi mất điện

**File:** wiki/concepts/black-sky-resilience.md:21
**Severity:** WARNING
**Dimension:** Factual
**Issue:** Điện thoại cố định được nêu như lớp liên lạc dự phòng mà không phân biệt đường dây đồng truyền thống với điện thoại qua Internet hoặc thiết bị cần nguồn điện tại chỗ. Người đọc có thể hiểu mọi điện thoại cố định đều hoạt động khi mất điện.
**Evidence:** “FM radio, điện thoại cố định và các kênh vệ tinh là lớp liên lạc hữu ích khi hạ tầng số hoặc Internet suy giảm.” Raw BBC dòng 32 nêu cụ thể “copper wire landline telephones”; dòng 88 nói mạng dây đồng tại Anh sẽ ngừng hoạt động.
**Suggested fix:** Giới hạn nhận định vào điện thoại dây đồng và thiết bị thực sự có nguồn dự phòng; nhấn mạnh phải kiểm tra hạ tầng và nguồn điện thực tế.

## Issue 2: Nhận định sức khỏe dựa vào nguồn quảng bá duy nhất

**File:** wiki/concepts/digital-eye-strain.md:15,19–21
**Severity:** WARNING
**Dimension:** Factual
**Issue:** Các nhận định về chớp mắt, theo dõi nhịp và lời nhắc được trình bày như kiến thức sức khỏe chung, nhưng nguồn duy nhất là trang giới thiệu sản phẩm. Trang này nêu tuyên bố của nhà sản xuất, không cung cấp trong bản raw bằng chứng lâm sàng cho hiệu quả theo dõi hoặc can thiệp.
**Evidence:** “Theo dõi cả tần suất lẫn độ đều của chớp mắt cho hình ảnh hữu ích hơn chỉ đếm tổng số lần chớp”; `## Sources` chỉ có `[[src_eyesrhythm]]`. Raw EyesRhythm dòng 41 và 84 xác định sản phẩm không phải thiết bị y tế.
**Suggested fix:** Gắn các nhận định so sánh và lợi ích với nhà sản xuất, tránh khẳng định hiệu quả lâm sàng; bổ sung nguồn y khoa độc lập cho định nghĩa, cơ chế và hiệu quả nếu có.

## Issue 3: Định nghĩa rule file quá hẹp và khái quát cách nạp

**File:** wiki/concepts/rule-files-ai-coding.md:15
**Severity:** WARNING
**Dimension:** Factual
**Issue:** Định nghĩa coi mọi rule file đều được quản lý phiên bản và được nạp như ngữ cảnh thường trực. Raw cũng mô tả hướng dẫn ở thư mục người dùng và quy tắc theo thư mục; việc quản lý phiên bản và cơ chế nạp phụ thuộc vị trí và công cụ.
**Evidence:** “Rule files for AI coding là các tài liệu version-controlled, được nạp làm persistent context”; raw video dòng 64–66 phân biệt các tầng home, repository, subdirectory và khuyến nghị version control.
**Suggested fix:** Viết rằng rule file cung cấp hướng dẫn theo cơ chế của từng công cụ; tài liệu trong repository thường nên được quản lý phiên bản, còn tệp cá nhân và quy tắc theo phạm vi có thể khác.
