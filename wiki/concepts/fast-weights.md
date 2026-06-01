---
type: concept
status: draft
main_tag: ai
sub_tags: [research, tools]
topic: llm-memory-consolidation
sources:
  - "[[src_llm-need-sleep-consolidation]]"
last_updated: 2026-05-28
---

# Fast Weights

## Definition

Fixed-size learned memory matrices trong SSM layers — cập nhật recurrently để store compressed information từ context.

## Key ideas

- Alternative to KV cache — không grow với sequence length
- Updated via recurrence: S_t = α_t S_{t-1} + β_t v_t k_t^T
- Cho phép information retrieval và reasoning over long context
- Central to LLM Sleep mechanism

## Related concepts

- [[llm-sleep]]
- [[state-space-models-ssm]]
- [[kv-cache-eviction]]

## Sources

- [[src_llm-need-sleep-consolidation]]

## Notes
