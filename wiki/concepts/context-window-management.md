---
type: concept
status: draft
main_tag: ai
sub_tags: [tools, automation]
topic: ai-coding-context-handoff
sources:
  - "[[src_handoff-skill-context-window-management]]"
  - "[[src_claude-best-practices-power-user-guide]]"
last_updated: 2026-11-02
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
- **Chủ động tách session theo chủ đề:** Khởi tạo conversation mới cho từng chủ đề riêng biệt hoặc khi context chạm ngưỡng suy giảm (~90%), tránh việc hướng dẫn quan trọng bị vùi lấp
- **Tài liệu bàn giao (Handoff Document):** Tạo văn bản tóm tắt công việc đã xong, giải pháp hiệu quả và bước tiếp theo để một session mới tiếp quản liền mạch mà không làm mất tính liên tục

## Related concepts

- [[handoff-skill]]
- [[ai-coding-agents]]
- [[session-separation]]
- [[compact-vs-handoff]]
- [[context-engineering]]
- [[claude-cowork]]

## Sources

- [[src_handoff-skill-context-window-management]]
- [[src_claude-best-practices-power-user-guide]]

## Notes
