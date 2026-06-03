---
type: concept
status: draft
main_tag: ai
sub_tags: [tools, automation]
topic: ai-coding-context-handoff
sources:
  - "[[src_handoff-skill-context-window-management]]"
last_updated: 2026-06-03
---

# Cross-Agent Workflow

## Definition

Phương pháp làm việc liền mạch giữa nhiều AI coding agents khác nhau (Claude Code, Codex, Copilot CLI) bằng cách sử dụng markdown files làm bridge để truyền context. Cho phép adversarial review và leverage strengths của từng agent.

## Key ideas

- Markdown là format universal cho việc trao đổi context giữa agents
- Có thể bắt đầu với Claude Code, handoff sang Codex, rồi Copilot CLI
- Mỗi agent có strengths riêng: cross-agent workflow tận dụng tối đa
- Adversarial review: để các agents "kiểm tra" lẫn nhau
- Workflow này mở rộng khả năng làm việc với AI agents vượt quá giới hạn của một tool duy nhất

## Related concepts

- [[handoff-skill]]
- [[context-window-management]]
- [[ai-coding-agents]]
- [[session-separation]]

## Sources

- [[src_handoff-skill-context-window-management]]

## Notes
