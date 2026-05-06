---
type: concept
status: draft
tags: [#ai, #productivity]
---

# Hermes: Operator vs Builder

## Mô tả
Sự phân biệt giữa vai trò "Người vận hành" (Operator) và "Người xây dựng" (Builder) khi sử dụng các AI Agent như Hermes so với các LLM thuần túy như Claude/Codex.

## Nội dung chính
- **Hermes là Operator**:
    - **Đặc điểm**: Có bộ nhớ bền vững (persistent memory), khả năng tự học loop, nhớ ngữ cảnh qua nhiều session, tự động hóa các tác vụ định kỳ.
    - **Use case lý tưởng**: Lập báo cáo hàng ngày, phân tích dữ liệu định kỳ, theo dõi tín hiệu (alerts), quản lý "bộ não thứ hai".
    - **Ví dụ Daily Briefings**: Thiết lập hệ thống tự động thu thập tin tức Tech, Macro, X-bookmarks $\rightarrow$ Tổng hợp Top 5 insights $\rightarrow$ Gửi báo cáo tóm tắt hàng sáng.
    - **Hạn chế**: Tốc độ build UI/UX chậm, thẩm mỹ kém, không tối ưu cho việc phát triển sản phẩm từ zero-to-one.
- **Claude/Codex là Builder**:
    - **Đặc điểm**: Tốc độ generate code cực nhanh, hiểu biết sâu về UI/UX, khả năng xây dựng cấu trúc sản phẩm nhanh chóng.
    - **Use case lý tưởng**: Xây dựng dashboard, website, viết app, thay đổi giao diện.
- **Chiến lược phối hợp (Hybrid Approach)**:
    - Bước 1: Dùng **Builder** để xây dựng công cụ/hạ tầng (ví dụ: Xây dashboard theo dõi Crypto).
    - Bước 2: Dùng **Operator** để vận hành công cụ đó (ví dụ: Hermes hằng ngày phân tích dữ liệu từ dashboard và gửi báo cáo tóm tắt).

## Liên quan
- [[AI-Workflow-Automation]]
- [[Xây dựng Knowledge Base cho LLM (LLM Knowledge Base Construction)]]

## Nguồn tham khảo
- [[src_hermes-builder-operator]]
