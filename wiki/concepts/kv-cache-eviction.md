---
type: concept
status: stub
main_tag: ai
sub_tags: [research]
topic: llm-memory-consolidation
sources:
  - [[src_llm-need-sleep-consolidation]]
last_updated: 2026-05-28
---

# KV Cache Eviction

## Definition

Chiến lược xóa hoặc compress attention KV cache khi context window đầy — hard eviction (clear hoàn toàn) hoặc sliding-window (giữ L-1 tokens).

## Key ideas

- Hard eviction: Clear toàn bộ KV cache, dựa vào SSM fast weights
- Sliding-window: Giữ recent tokens, evict oldest
- Warm-up phase cần thiết cho sliding-window
- Trade-off: memory vs access to distant context

## Related concepts

- [[llm-sleep]]
- [[memory-consolidation-offline]]
- [[state-space-models-ssm]]

## Sources

- [[src_llm-need-sleep-consolidation]]

## Notes
