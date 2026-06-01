---
type: concept
status: reviewed
main_tag: ai
sub_tags: [automation, tools]
topic: ai-trading-agent-claude-code
sources:
  - "[[src_build-ai-trading-agent-claude-code-alpaca]]"
last_updated: 2026-05-28
---

# Agent Journal Pattern

## Definition

Pattern yêu cầu agent ghi lại structured log entry cho mọi decision — bao gồm cả những ngày không có action. Đây là cơ chế accountability và audit trail cho AI agents hoạt động trong production environments. Journal entries được viết ở structured markdown format bao gồm portfolio status, market research, trades, và reflection. Pattern này đảm bảo rằng mọi quyết định đều có thể được trace và review sau này. Đặc biệt quan trọng cho việc debugging và continuous improvement của agent behavior.

## Key ideas

- Structured markdown format: portfolio status, market research, trades, reflection
- Mandatory — không optional ngay cả khi no trades
- Audit trail cho debugging và improvement
- Cross-session memory nếu journal được reference

## Related concepts

- [[ai-trading-agent]]
- [[claude-code-routines]]

## Sources

- [[src_build-ai-trading-agent-claude-code-alpaca]]

## Notes
