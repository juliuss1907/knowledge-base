# Output Validation — 2026-11-24

**Status:** hoàn tất — không có vấn đề mới chờ duyệt
**Issues found:** 0 mới (0 ERROR, 0 WARNING, 0 INFO)
**Created:** 2026-11-24 23:00 +0700
**Validator:** output-validator

## Phạm vi và kết quả

- Quét cơ học 880 tệp: 232 sources và 648 concepts. Không có tệp mang ngày biên soạn hoặc cập nhật 2026-11-24; không có tệp nào có thời gian sửa mới hơn báo cáo Output ngày 2026-11-23.
- Không có tệp mới để kiểm tra chi tiết theo bốn chiều. Không xác minh độc lập các nguồn gốc; kết quả quét không chứng minh toàn bộ nội dung chính xác, đầy đủ, mạch lạc hoặc đúng tiếng Việt.
- Quick-scan báo 117 định nghĩa một câu và 77 concept ít ý theo heuristic. Chưa xác minh từng trường hợp; không tính đây là phát hiện mới. Không phát hiện thiếu mục hoặc cắt cụt theo các phép kiểm của quick-scan.
- Quét bổ sung bốn nhóm mẫu mất chữ i, không phân biệt hoa thường: một dòng khớp mẫu `ngườ`, ba nhóm còn lại không có kết quả. Bốn nhóm lỗi chính tả của quick-scan đều không có kết quả.

## Vấn đề tồn đọng đã báo

`wiki/concepts/internal-locus-of-control.md:16` vẫn chứa “Ngườ có internal locus of control”. Đây là lỗi cũ đã ghi trong [báo cáo 2026-11-23](2026-11-23_output-report.md), không tính lại là vấn đề mới. Không sửa tệp nội dung trong lượt này.
