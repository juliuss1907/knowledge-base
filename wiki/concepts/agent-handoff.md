---
type: concept
status: reviewed
main_tag: ai
sub_tags: [automation, tools]
topic: multi-agent-architecture
sources:
  - "[[src_luke-alvoeiro-multi-agent-architecture-factory]]"
last_updated: 2026-05-28
---

# Agent Handoff

## Definition

Process chuyển control từ agent này sang agent khác trong multi-agent system — critical cho workflow orchestration. Handoff đảm bảo state transfer (memory, context, progress) được truyền tải chính xác giữa các agents. Protocol definition xác định những gì được chuyển giao và cách thức thực hiện. Các handoff triggers bao gồm completion, escalation, và error conditions. Đây là pattern cơ bản được sử dụng rộng rãi trong Factory Missions cho complex workflows.

## Key ideas

- State transfer: memory, context, progress
- Protocol definition: what gets passed
- Handoff triggers: completion, escalation, error
- Synchronous vs asynchronous handoffs
- Used trong Factory Missions cho complex workflows

## Related concepts

- [[orchestrator-worker-validator]]
- [[factory-missions]]
- [[validation-contract]]

## Sources

- [[src_luke-alvoeiro-multi-agent-architecture-factory]]

## Notes
