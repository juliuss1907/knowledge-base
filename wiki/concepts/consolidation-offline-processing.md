---
type: concept
status: draft
main_tag: ai
sub_tags: [research, automation]
topic: agent-memory-systems
sources:
  - [[src_agent-memory-anatomy]]
last_updated: 2026-05-27
---

# Consolidation (Offline Processing)

## Definition

Quá trình xử lý offline trên accumulated memory — rewrite, deduplicate, resolve contradictions — tương đương với quá trình "consolidation" trong giấc ngủ của con người.

## Key ideas

- **Biological analog**: Giấc ngủ replay experiences, prune redundant — slow compression từ event → knowledge
- **Agent implementations**: 
  - Anthropic Dreams (mid-2026): offline pipeline ingests memory store + past sessions, writes new store
  - Letta sleep-time compute: background subagents rewrite archival memory during idle time
- Chạy scheduled passes over accumulated material
- Có thể deduplicate, resolve contradictions on latest value, surface patterns
- Structural argument: cleaner than synchronous extraction dưới latency pressure
- Hiệu quả thực tế vẫn là open empirical question
- Alternative to biological-style forgetting: non-destructive reorganization giữ đầy đủ history

## Related concepts

- [[agent-memory-taxonomy]]
- [[memory-extraction-timing]]

## Sources

- [[src_agent-memory-anatomy]]

## Notes
