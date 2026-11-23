# Output Validation — 2026-11-23

**Status:** pending
**Issues found:** 1 (0 ERROR, 1 WARNING, 0 INFO)
**Created:** 2026-11-23 23:01:03 +0700
**Validator:** output-validator

## Phạm vi và giới hạn

- Quét cơ học 880 tệp: 232 sources và 648 concepts. Không có tệp mang ngày biên soạn hoặc cập nhật 2026-11-23; không có tệp nào có thời gian sửa mới hơn báo cáo Output ngày 2026-11-22.
- Không kiểm tra chi tiết từng tệp theo bốn chiều, không xác minh độc lập các nguồn gốc. Kết quả quét không chứng minh toàn bộ nội dung chính xác hoặc đầy đủ.
- Quick-scan báo 117 định nghĩa một câu và 77 concept ít ý theo heuristic; chưa xác minh từng trường hợp, không tính là lỗi mới. Không có dấu hiệu thiếu mục hoặc tệp bị cắt cụt theo quick-scan.
- Quét bốn nhóm mẫu mất chữ i, không phân biệt hoa thường: một kết quả cũ ở dòng 16 được mô tả bên dưới; ba nhóm còn lại không có kết quả. Đây là phát hiện tồn đọng, không phải lỗi phát sinh hôm nay.
- Báo cáo 2026-11-22 ghi không có kết quả ở bốn nhóm mẫu. Kết quả đó không bao phủ chữ hoa `Ngườ`; không thể kết luận kết quả đã báo khi đó chính xác cho toàn bộ biến thể hoa thường.

## Issue 1: Lỗi mất chữ i ở đầu câu còn tồn đọng

**File:** wiki/concepts/internal-locus-of-control.md:16
**Severity:** WARNING
**Dimension:** Vietnamese
**Issue:** Từ `Ngườ` thiếu chữ `i`. Biến thể viết hoa ở đầu câu lọt khỏi mẫu tìm kiếm phân biệt hoa thường. Lỗi này đã được ghi trong `wiki/reviews/archive/2026-07/2026-07-21_output-report.md:32` và vẫn còn trên đĩa; không phải lỗi mới của lô hôm nay.
**Evidence:** “Ngườ có internal locus of control tin rằng họ tạo ra kết quả”.
**Suggested fix:** Sau khi được duyệt, sửa `Ngườ` thành `Người` tại dòng 16; khi quét biến thể mất chữ i, kiểm tra cả chữ hoa và chữ thường. Không tự động sửa nội dung trong lượt kiểm tra này.
