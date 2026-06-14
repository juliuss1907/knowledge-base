---
type: concept
status: reviewed
main_tag: ai
sub_tags: [research, coding]
topic: llm-capabilities
sources:
  - "[[src_deepseek-v4-architecture]]"
last_updated: 2026-05-29
---

# Long Context Models

## Definition

LLMs có khả năng xử lý context window lớn (100K+ tokens). DeepSeek V4 đạt 1M tokens, vượt xa Claude Opus (200K max) và phần lớn frontier models.

## Key ideas

- Thách thức lớn nhất là sự tăng trưởng quadratic của attention (O(n²)) và kích thước KV cache khổng lồ
- Giải pháp trong V4 là dùng hybrid attention (CSA + HCA) để nén context, giảm FLOPs và bộ nhớ
- Khả năng xử lý 1M tokens cho phép model đọc toàn bộ codebase lớn hoặc hàng chục tài liệu dài cùng lúc
- Hiệu suất (RULER benchmark) của V4 Pro vượt trội so với các model closed-source ở cùng độ dài context
- Chia sẻ compressed KV giúp tối ưu hóa tài nguyên trong môi trường multi-agent

## Key challenges

- **KV cache size:** 1M tokens = hàng trăng GB mỗi request
- **Quadratic attention:** Traditional attention có complexity O(n²)
- **Compute cost:** Per-token cost tăng theo sequence length

## Solutions in V4

- **CSA + HCA:** Hybrid attention với compression để giảm FLOPs và KV cache
- **FP4 Lightning Indexer:** Efficient block selection cho sparse attention
- **Shared compressed KV:** Multi-agent deployments có thể share representation

## Benchmark results

| Model | RULER (128K) | Long-ROPE (1M) |
|-------|--------------|----------------|
| V4 Pro | ~95 | ~89 |
| Claude Opus | ~87 | N/A (200K max) |
| OpenAI | ~90 | N/A |
| V4 Flash | ~88 | ~79 |

**Advantage:** V4 Pro không có đối thủ closed-source ở 1M tokens. Auditability cho phép kiểm tra tại sao performance degrade ở context length cụ thể.

## Related concepts

- [[csa-hca-attention]]
- [[fp4-lightning-indexer]]

## Sources

- [[src_deepseek-v4-architecture]]

## Notes

