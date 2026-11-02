---
type: concept
status: draft
main_tag: ai
sub_tags: [tools, automation]
topic: claude-power-user-system
sources:
  - "[[src_claude-best-practices-power-user-guide]]"
last_updated: 2026-11-02
---

# Claude Cowork

## Definition

Claude Cowork là môi trường agent trên máy tính cho phép Claude tương tác trực tiếp với hệ thống tệp cục bộ, kết nối các công cụ ngoài qua connector và thực thi các tác vụ tự động dài hạn. Môi trường này biến Claude từ một chatbot hội thoại thông thường thành một trợ lý hệ thống làm việc với cấu trúc dự án và ngữ cảnh chuyên biệt.

## Key ideas

- **Cấu trúc thư mục chuẩn:** Tối ưu hiệu quả qua mô hình 4 thư mục chính: ABOUT ME (nhận diện cá nhân và quy tắc viết), PROJECTS (không gian từng dự án), TEMPLATES (mẫu chuẩn tái sử dụng) và CLAUDE OUTPUTS (nơi duy nhất xuất kết quả).
- **Global Instructions:** Cấu hình quy tắc bất biến trước mọi phiên làm việc như luôn đọc tài liệu bối cảnh, giữ quy ước đặt tên và phân lập nơi lưu tệp.
- **Mô tả hướng kết quả (outcome-based):** Định nghĩa kết quả mong đợi thay vì chỉ dẫn từng bước chi tiết, để mô hình tự lập kế hoạch và phân rã các bước thực hiện.
- **Xử lý song song:** Tận dụng các sub-agent để đọc, phân tích hoặc tóm tắt đồng thời nhiều tệp dữ liệu, giảm thời gian xử lý tổng thể.
- **Phân lập không gian dự án (Projects):** Ngăn chặn context bleeding giữa các luồng công việc khác nhau bằng cách gán bối cảnh và bộ nhớ riêng cho từng dự án.

## Related concepts

- [[context-engineering]]
- [[context-window-management]]
- [[socratic-prompting]]

## Sources

- [[src_claude-best-practices-power-user-guide]]

## Notes
