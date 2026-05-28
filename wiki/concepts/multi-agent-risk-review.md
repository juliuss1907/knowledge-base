---
type: concept
status: stub
main_tag: ai
sub_tags: [automation, tools]
topic: ai-trading-agent-claude-code
sources:
  - "[[src_build-ai-trading-agent-claude-code-alpaca]]"
last_updated: 2026-05-28
---

# Multi-Agent Risk Review

## Definition

Pattern sử dụng multiple agents trong trading: Agent A (Trader) propose trades, Agent B (Risk Reviewer) approve hoặc reject — thêm layer of oversight.

## Key ideas

- Agent B chạy sau Agent A, đọc journal và quyết định
- Có thể flag `review_required` để human intervene
- Thêm latency nhưng giảm risk của bad decisions
- Same principle: workflow controls agent, not agent controls workflow

## Related concepts

- [[ai-trading-agent]]
- [[agent-journal-pattern]]

## Sources

- [[src_build-ai-trading-agent-claude-code-alpaca]]

## Notes
