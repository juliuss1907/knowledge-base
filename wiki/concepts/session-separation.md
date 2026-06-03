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

# Session Separation

## Definition

Chiến lược tách một công việc coding phức tạp thành nhiều session riêng biệt, mỗi session tập trung vào một mục tiêu cụ thể. Giúp duy trì chất lượng output của AI agents bằng cách giữ mỗi session trong "smart zone" của context window.

## Key ideas

- Thay vì 1 session dài đầy context, tách thành nhiều session ngắn tập trung
- Mỗi session có purpose rõ ràng và scope hẹp
- Session prototype có thể lên đến ~169K tokens vẫn hiệu quả
- Main session giữ flow tổng thể, handoff sessions xử lý chi tiết
- Kết nối giữa các session qua handoff files (markdown bridges)

## Related concepts

- [[handoff-skill]]
- [[context-window-management]]
- [[ai-coding-agents]]
- [[cross-agent-workflow]]

## Sources

- [[src_handoff-skill-context-window-management]]

## Notes
