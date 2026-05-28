---
type: concept
status: stub
main_tag: ai
sub_tags: [research, tools]
topic: llm-memory-consolidation
sources:
  - "[[src_llm-need-sleep-consolidation]]"
last_updated: 2026-05-28
---

# State Space Models (SSM)

## Definition

Loại mô hình sequence sử dụng fixed-size fast weight memories thay vì KV cache — giải quyết vấn đề quadratic scaling của attention.

## Key ideas

- Fixed-size state (S_t) thay vì growing KV cache
- Linear complexity với sequence length
- Hybrid architectures: SSM + attention interleaved
- Examples: Mamba, Gated Delta Networks
- Cho phép long-range dependencies efficiently

## Related concepts

- [[llm-sleep]]
- [[fast-weights]]
- [[kv-cache-eviction]]

## Sources

- [[src_llm-need-sleep-consolidation]]

## Notes
