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

# Cách Ly Ví Cho AI Agent

## Definition

Cách ly ví cho AI Agent là kiến trúc giới hạn số vốn, authority và private-key access mà model hoặc prompt có thể chạm tới. Mục tiêu là đảm bảo lỗi model, prompt injection hoặc rule rewrite không thể ngay lập tức chiếm hết tài sản hoặc ký giao dịch từ server.

## Key ideas

- Hot wallet chỉ nên giữ stake được chủ định chấp nhận mất; cold hoặc signing wallet giữ tài sản chính.
- Model không cần đọc private key: key và logic ký nằm trong code mà model không truy cập trực tiếp.
- Authority phải được thu hẹp theo wallet và operation, thay vì để cùng một key có quyền chuyển toàn bộ số dư.
- Lợi nhuận được sweep định kỳ ra nơi lưu ký riêng để giới hạn blast radius của hot wallet.
- Phần tử có khả năng thay đổi dòng tiền cần human approval hoặc test gate giữa proposal và execution.
- Wallet isolation không thay thế position limits, fail-closed defaults, monitoring hay rollback; đây là một lớp defense trong nhiều lớp.

## Related concepts

- [[two-speed-agent-loop]]
- [[calibrated-decision-models]]
- [[ai-trading-agent]]
- [[multi-agent-risk-review]]

## Sources

- [[src_alex-saint-ai-trading-bot-jev-solana]]
