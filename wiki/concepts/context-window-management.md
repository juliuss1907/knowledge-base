---
type: concept
status: draft
main_tag: ai
sub_tags: [tools, productivity]
topic: ai-coding-context-handoff
sources:
  - "[[src_handoff-skill-context-window-management]]"
last_updated: 2026-06-03
---

# Context Window Management

## Definition

Các kỹ thuật và chiến lược để tối ưu hóa việc sử dụng context window của Large Language Models (LLMs) khi làm việc với AI coding agents. Mục tiêu: duy trì chất lượng output cao bằng cách tránh "dumb zone" khi context quá đầy.

## Key ideas

- Context window có giới hạn, chất lượng output giảm khi tiến gần giới hạn
- Claude Code có 1M tokens nhưng chỉ ~120K tokens là "smart zone" thực tế
- Các phương pháp quản lý: compact (tóm tắt), handoff (tách session), session separation
- "Dumb zone": khi context đầy, agent trở nên "confused", output chất lượng thấp
- Quản lý chủ động giúp duy trì hiệu quả làm việc với AI agents trong các session dài

## Related concepts

- [[handoff-skill]]
- [[ai-coding-agents]]
- [[session-separation]]
- [[compact-vs-handoff]]

## Sources

- [[src_handoff-skill-context-window-management]]

## Notes
