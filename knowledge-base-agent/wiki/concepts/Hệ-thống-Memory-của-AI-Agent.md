---
type: concept
status: draft
tags: [#ai, #productivity]
---

# Hệ thống Memory của AI Agent (AI Agent Memory System)

## Mô tả
Cách thức AI Agent (như Hermes) lưu trữ, truy xuất và tổng hợp thông tin theo thời gian để tạo ra một "bộ não" có khả năng học hỏi liên tục thay vì bắt đầu lại từ đầu trong mỗi session.

## Nội dung chính
- **Vòng lặp Memory (Memory Loop)**:
    - **Ingest**: Thu thập dữ liệu thông qua các cron jobs hằng ngày (ví dụ: đọc tin tức, track dữ liệu).
    - **Hindsight/Reflection**: AI xem xét lại các insights đã thu thập được trong ngày/tuần.
    - **Synthesis**: Kết nối các mẩu thông tin rời rạc thành các pattern (mẫu) hoặc luận điểm (theses) dài hạn.
- **Moat thông qua Ngữ cảnh (Contextual Moat)**: Lợi thế của một AI Agent không nằm ở model (vì model có thể thay thế), mà nằm ở dữ liệu cá nhân hóa mà nó lưu trữ:
    - Luận điểm đầu tư (Investment Theses).
    - Sở thích cá nhân và khẩu vị rủi ro.
    - Lịch sử các quyết định và lý do (rationale) đằng sau chúng.
- **Truy xuất liên session**: Khả năng recall lại các session cũ để rút ra mối quan hệ giữa các sự kiện diễn ra ở những thời điểm khác nhau.

## Liên quan
- [[Hermes: Operator vs Builder]]
- [[Xây dựng Knowledge Base cho LLM (LLM Knowledge Base Construction)]]

## Nguồn tham khảo
- [[src_hermes-ultimate-analyst]]
