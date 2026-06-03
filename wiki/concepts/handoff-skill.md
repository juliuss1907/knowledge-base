---
type: concept
status: draft
main_tag: ai
sub_tags: [tools, productivity, coding]
topic: ai-coding-context-handoff
sources:
  - "[[src_handoff-skill-context-window-management]]"
last_updated: 2026-06-03
---

# Handoff Skill

## Definition

Một kỹ thuật (và công cụ) tùy chỉnh để quản lý context window khi làm việc với AI coding agents. Thay vì tóm tắt toàn bộ conversation (compact), handoff tách 1 phần công việc cụ thể sang session riêng biệt, giữ session gốc sạch sẽ và tập trung.

## Key ideas

- Handoff file là markdown bridge giữa các session/agent khác nhau
- Chuyển specific context (1 bug fix, 1 feature) sang session mới thay vì compact toàn bộ
- Session gốc giữ được tập trung, session handoff xử lý chi tiết riêng
- Có thể handoff giữa các agent khác nhau: Claude Code → Codex → Copilot CLI
- File handoff lưu trong temp directory và xóa sau khi dùng
- Redact sensitive info trước khi handoff

## Related concepts

- [[context-window-management]]
- [[ai-coding-agents]]
- [[session-separation]]
- [[cross-agent-workflow]]
- [[compact-vs-handoff]]

## Sources

- [[src_handoff-skill-context-window-management]]

## Notes
