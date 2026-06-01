---
type: concept
status: reviewed
main_tag: ai
sub_tags: [research, tools]
topic: deepseek-v4-architecture
sources:
  - "[[src_deepseek-v4-architecture]]"
last_updated: 2026-05-29
---

# FP4 Lightning Indexer

## Definition

Scoring network trong DeepSeek V4 chạy ở FP4 precision, chọn top-k compressed blocks cho sparse attention. Giải quyết vấn đề KV cache ở 1M tokens = hàng trăm GB mỗi request.

## Three-layer compression

1. CSA compression ~4× dọc sequence dimension
2. HCA compression ~128×
3. FP4 Lightning Indexer — scoring + top-k block selection

## Multi-agent advantage

- **Naive full KV caching:** Mỗi agent giữ KV cache riêng → memory footprint × số agent
- **V4 approach:** Shared compressed KV giữa các agents — multiple agents access cùng document có thể share compressed block representation

## Economic profile

- Capital cost cao (multi-node GPU) nhưng per-token compute cost thấp
- Lý tưởng cho high-throughput, long-session workloads
- KHÔNG lý tưởng cho low-throughput workloads ngắn

## Related concepts

- [[csa-hca-attention]]
- [[long-context-models]]

## Sources

- [[src_deepseek-v4-architecture]]

## Notes

