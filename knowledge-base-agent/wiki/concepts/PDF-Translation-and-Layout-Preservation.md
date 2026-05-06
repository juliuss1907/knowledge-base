---
type: concept
status: draft
tags: [#coding, #ai]
---

# Dịch thuật PDF và Bảo toàn Bố cục (PDF Translation & Layout Preservation)

## Mô tả
Thách thức kỹ thuật trong việc chuyển đổi ngôn ngữ của một tài liệu PDF trong khi vẫn giữ nguyên định dạng hình ảnh, vị trí văn bản và các thành phần phi văn bản (như công thức toán học, bảng biểu).

## Nội dung chính
- **Thách thức kỹ thuật**:
    - **Thiếu cấu trúc**: PDF không lưu trữ văn bản theo đoạn hay trang như Word mà lưu theo tọa độ tuyệt đối của từng ký tự, khiến việc thay thế văn bản bằng ngôn ngữ khác (có độ dài khác) dễ làm hỏng layout.
    - **OCR (Optical Character Recognition)**: Đối với PDF scan, cần một lớp OCR chính xác để chuyển ảnh thành text trước khi dịch.
    - **Typesetting**: Quá trình vẽ lại văn bản đã dịch vào đúng vị trí cũ với font chữ và kích thước phù hợp.
- **Các chiến lược xử lý**:
    - **In-place Replacement**: Thay thế text trực tiếp tại tọa độ cũ (dễ gây tràn lề).
    - **Re-rendering**: Phân tích cấu trúc trang và vẽ lại toàn bộ trang với nội dung mới.
    - **Formula Protection**: Nhận diện các vùng chứa công thức toán học để loại bỏ khỏi quy trình dịch, tránh làm sai lệch ký hiệu.
- **Công cụ tiêu biểu**: RetainPDF là một ví dụ điển hình về việc kết hợp OCR mạnh mẽ và typesetting chính xác để giải quyết các bài toán này.

## Liên quan
- [[RetainPDF]]
- [[nano-pdf]]

## Nguồn tham khảo
- [[src_retain-pdf]]
