---
type: concept
status: reviewed
main_tag: ai
sub_tags: [automation, tools, tutorial]
topic: hermes-workflow-optimization
sources:
  - "[[src_hermes-analyst-workflow-essentials]]"
last_updated: 2026-05-19
---

# Agent Skill Management

## Definition

Quản lý skills trong Hermes — agent tự động tạo skill khi thấy task lặp lại, nhưng cần best practices để tránh mess và optimize token usage. Skill trong Hermes đóng vai trò như recipes — workflows được thiết kế để thực thi không cần giải thích lại mỗi lần. Tuy nhiên, auto-creation có thể dẫn đến too many skills và ineffective tools gây lãng phí tokens. Best practices bao gồm việc remember good tools, explicitly request update cron jobs, và health check định kỳ. Skill management là critical component cho việc maintain efficient agent operations.

## Key ideas

- **Auto-creation:** Agent tự tạo skill khi thấy task lặp lại
- **Skill = recipe:** Workflow để thực thi không cần giải thích lại
- **Pitfall — Too many skills:** Quá nhiều skills + cron jobs → messy & chaotic
- **Pitfall — Ineffective tools:** Tools không hiệu quả lãng phí tokens

**Best practices:**
- Nhớ tools tốt, chỉnh agent khi dùng tool kém hiệu quả
- Explicitly yêu cầu update cron jobs khi thay đổi tool
- Health check định kỳ bằng delegate task cho sub-agent

## Related concepts

- [[hermes-three-layers]]
- [[browser-harness-tool]]

## Sources

- [[src_hermes-analyst-workflow-essentials]]

## Notes
