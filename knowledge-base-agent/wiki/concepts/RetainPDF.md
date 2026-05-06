---
type: concept
status: draft
tags: [#coding, #ai]
---

# RetainPDF

## Mô tả
Một công cụ dịch thuật PDF tiên tiến tập trung vào việc bảo toàn bố cục (layout), các công thức toán học phức tạp và cấu trúc tài liệu, đặc biệt hữu ích cho việc đọc các bài báo khoa học và tài liệu kỹ thuật.

## Nội dung chính
- **Khả năng xử lý đặc thù**:
    - **PDF Scan/Image**: Tích hợp OCR (PaddleOCR, Rust OCR) để xử lý các tệp PDF không có text (dạng ảnh), cho phép dịch cả các tài liệu scan.
    - **Complex Inline Formulas**: Bảo toàn và dịch chính xác các công thức toán học lồng trong văn bản mà không làm hỏng định dạng.
    - **Layout Preservation**: Đảm bảo văn bản sau khi dịch vẫn nằm đúng vị trí như bản gốc, không làm xô lệch trang.
    - **Code Protection**: Có cơ chế nhận diện và không dịch nhầm các đoạn mã nguồn (code blocks).
- **Kiến trúc hệ thống**: Tách biệt backend (Python) để xử lý tác vụ nặng về typesetting và frontend (Web/Desktop) để cung cấp trải nghiệm người dùng.
- **Ứng dụng**: Phù hợp cho sinh viên, nhà nghiên cứu cần dịch nhanh các bài báo SCI hoặc sách kỹ thuật từ nhiều ngôn ngữ khác nhau.

## Liên quan
- [[PDF Translation & Layout Preservation]]
- [[nano-pdf]]

## Nguồn tham khảo
- [[src_retain-pdf]]
