---
type: concept
status: draft
main_tag: ai
sub_tags: [automation, tools, tutorial]
topic: hermes-workflow-optimization
sources:
  - [[wiki/sources/src_hermes-analyst-workflow-essentials]]
last_updated: 2026-05-19
---

# Agent Skill Management

## Definition

Quản lý skills trong Hermes — agent tự động tạo skill khi thấy task lặp lại, nhưng cần best practices để tránh mess và optimize token usage.

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

- [[wiki/sources/src_hermes-analyst-workflow-essentials]]

## Notes
