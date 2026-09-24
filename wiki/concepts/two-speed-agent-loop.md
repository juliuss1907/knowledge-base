---
type: concept
status: draft
main_tag: ai
sub_tags: [automation, tools, hack]
topic: ai-trading-agent-safety
sources:
  - "[[src_alex-saint-ai-trading-bot-jev-solana]]"
last_updated: 2026-09-24
---

# Vòng lặp Agent Hai Tốc Độ

## Definition

Vòng lặp Agent Hai Tốc Độ tách quy trình tần suất cao thành một model quyết định nhanh và một model phản tư chậm để cải thiện rules từ dữ liệu vận hành. Fast model đáp ứng latency của giao dịch, còn slow model chạy theo lịch để tìm lỗi, nén feedback và đề xuất thay đổi.

## Key ideas

- Fast model tối ưu cho structured decision trong một latency window nhỏ; slow model tối ưu cho reasoning và sửa chữa hệ thống.
- Slow model nên đọc disagreement và outcome có chọn lọc thay vì toàn bộ log, tránh tốn token và học lại các quyết định đã thống nhất.
- Quyền hạn phải bị giới hạn: slow model tạo proposal, còn approval gate mới quyết định có phát hành version mới hay không.
- Mỗi prompt version cần được versioned để có thể audit, so sánh và rollback thay đổi.
- Tách hai tốc độ tránh việc một model vừa tối ưu cho quyết định tức thời vừa tối ưu cho việc tái thiết kế quy trình của chính nó.

## Related concepts

- [[calibrated-decision-models]]
- [[wallet-isolation-for-ai-agents]]
- [[ai-trading-agent]]
- [[multi-agent-risk-review]]

## Sources

- [[src_alex-saint-ai-trading-bot-jev-solana]]
