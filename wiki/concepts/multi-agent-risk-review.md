---
type: concept
status: reviewed
main_tag: ai
sub_tags: [automation, tools]
topic: ai-trading-agent-claude-code
sources:
  - "[[src_build-ai-trading-agent-claude-code-alpaca]]"
  - "[[src_alex-saint-ai-trading-bot-jev-solana]]"
last_updated: 2026-09-24
---

# Multi-Agent Risk Review

## Definition

Pattern sử dụng multiple agents trong trading: Agent A (Trader) propose trades, Agent B (Risk Reviewer) approve hoặc reject — thêm layer of oversight.

## Key ideas

- Agent B chạy sau Agent A, đọc journal và quyết định
- Có thể flag `review_required` để human intervene
- Thêm latency nhưng giảm risk của bad decisions
- Same principle: workflow controls agent, not agent controls workflow
- **Two-speed review:** Fast model đưa quyết định; slow model rà soát disagreement và đề xuất cải thiện decision rules
- **Human or test gate:** Mọi rule rewrite chỉ được phát hành sau approval, tránh model tự thay đổi quyền hành động
- **Separation of authority:** Decision model không cần private-key access; chữ ký và wallet transfer được giữ trong code ngoài tầm model
- **Fail-closed default:** API failure, timeout hoặc confidence không hợp lệ phải tạo `hold`, không được suy đoán rồi giao dịch

## Related concepts

- [[ai-trading-agent]]
- [[agent-journal-pattern]]
- [[two-speed-agent-loop]]
- [[calibrated-decision-models]]
- [[wallet-isolation-for-ai-agents]]

## Sources

- [[src_build-ai-trading-agent-claude-code-alpaca]]
- [[src_alex-saint-ai-trading-bot-jev-solana]]

## Notes
