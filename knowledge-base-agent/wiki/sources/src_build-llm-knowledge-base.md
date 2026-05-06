---
type: source
source_url: https://open.substack.com/pub/emergingai/p/how-to-build-your-own-llm-knowledge
date_ingested: 2026-05-05
tags: [#ai, #productivity]
status: processed
---

# How to Build Your Own LLM Knowledge Base — Emerging AI

Nguồn: Emerging AI (Substack)
Ngày: 2026-04-18

## Ghi chú chính
- **Triết lý "Thủ thư" (Librarian Model)**: Thay vì dùng AI như một máy trả lời (hỏi-đáp rồi quên), hãy dùng AI như một thủ thư quản lý tri thức tích lũy.
- **Vấn đề**: Cách dùng AI truyền thống khiến tri thức bị phân mảnh, không có sự kết nối và tích lũy theo thời gian.
- **Mô hình vận hành**:
    - `raw/`: Nơi chứa dữ liệu thô (bài viết, PDF, ghi chú). Không chỉnh sửa.
    - `wiki/`: Nơi AI tổng hợp thành các bài viết concept, tóm tắt và mục lục.
- **Luồng công việc**: Feed dữ liệu thô $\rightarrow$ AI build wiki $\rightarrow$ Truy vấn dựa trên wiki.
- **Kết quả**: Tạo ra một "bộ não thứ hai" (external brain) nơi các ý tưởng được liên kết và phát triển liên tục.
