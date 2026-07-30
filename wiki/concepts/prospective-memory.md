---
type: concept
status: draft
main_tag: ai
sub_tags: [tools, research]
topic: agent-memory-systems
sources:
  - "[[src_agent-memory-7-types-substack.md]]"
last_updated: 2026-07-30
---

# Prospective Memory

## Definition

Prospective memory là khả năng nhớ các tasks cần thực hiện trong tương lai — scheduling, reminders, follow-ups. Khác với retrospective memory (nhớ quá khứ), prospective memory hướng về future actions.

## Key ideas

- "Remember to do X at time Y" — future-oriented memory
- Use cases: scheduled tasks, follow-up reminders, deadline tracking, recurring workflows
- Implementation: job schedulers (like cron), reminder queues, calendar integrations
- Challenge: agent cần "check" prospective memory regularly (not purely event-driven)
- Integration với other memory types: prospective trigger → retrieve relevant context → execute
- Risk: missed reminders, timezone issues, scheduling conflicts

## Related concepts

- [[task-scheduling]]
- [[workflow-automation]]
- [[reminder-systems]]

## Sources

- [[src_agent-memory-7-types-substack.md]]

## Notes
