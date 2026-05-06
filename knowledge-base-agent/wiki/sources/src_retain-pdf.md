---
type: source
source_url: https://github.com/wxyhgk/retain-pdf
date_ingested: 2026-05-05
tags: [#coding, #ai]
status: processed
---

# RetainPDF — PDF Layout-Preserving Translation Tool

Owner: wxyhgk
Repo: retain-pdf
Link: https://github.com/wxyhgk/retain-pdf

## Ghi chú chính
- **Mục đích**: Công cụ dịch PDF giữ nguyên layout, công thức và cấu trúc, đặc biệt tối ưu cho các tài liệu nghiên cứu khoa học và kỹ thuật.
- **Ưu điểm vượt trội**:
    - Hỗ trợ PDF dạng ảnh/scan (điều mà nhiều công cụ khác không làm được).
    - Xử lý tốt các công thức toán học inline phức tạp.
    - Giữ nguyên bố cục trang sau khi dịch.
    - Tránh dịch nhầm các đoạn mã code.
    - Tối ưu dung lượng PDF output.
- **Kiến trúc**: Full-stack và decouple:
    - Backend: Python (xử lý OCR, dịch thuật, typesetting).
    - OCR: Sử dụng PaddleOCR hoặc Rust OCR.
    - Frontend: Web UI và ứng dụng Desktop (Tauri/Electron).
- **Triển khai**: Hỗ trợ ứng dụng Desktop cho Windows/macOS/Linux và Docker.
