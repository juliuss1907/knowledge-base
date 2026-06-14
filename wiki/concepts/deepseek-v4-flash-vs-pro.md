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

# DeepSeek V4 Pro vs Flash

## Definition

Hai biến thể của DeepSeek V4 với attention topology, KV cache pressure profile, và memory access patterns khác nhau — có cascading effects lên GPU memory budgeting, batching strategy, và multi-agent serving infrastructure.

## Key ideas

- V4 Pro tập trung vào long-context reasoning cao cấp (>200K tokens), yêu cầu hạ tầng GPU lớn (3+ H200 nodes)
- V4 Flash tối ưu cho latency và throughput, phù hợp với workload 32K-200K tokens trên 1-2 nodes
- Sự khác biệt chính nằm ở interleaving ratio của CSA và HCA
- V4 Flash không phải bản distilled mà là thiết kế độc lập về MoE config và routing
- Việc chọn phiên bản phụ thuộc vào break-even point về chi phí tokens/tháng và yêu cầu về tail latency

## Comparison

| Thông số | V4 Pro | V4 Flash |
|----------|--------|----------|
| **Tổng tham số** | 1.6T | 284B |
| **Activated/token** | ~49B (3.1%) | ~13B (4.6%) |
| **Context window** | 1M tokens | 1M tokens |
| **CSA:HCA ratio** | ~3:1 | ~4:1 |
| **Hardware** | 3+ H200 nodes (BF16) / 2 nodes (FP8) | Single/dual 8-GPU H200 node |
| **Break-even** | >500M tokens/tháng | Lower throughput workloads |
| **Best for** | >200K tokens, long-session | 32K-200K, latency-sensitive |

## Key differences

- **V4 Flash không phải distilled/compressed:** Được thiết kế độc lập với MoE config, interleaving ratio, routing parameters riêng
- **Interleaving ratio:** V4 Flash ít HCA hơn → latency thấp hơn nhưng trade-off về long-context reasoning

## Practitioner guidance

**V4 Pro khi nào:**
- Workload >200K tokens
- Documents, codebases, legal corpora, long-horizon agentic sessions
- Yêu cầu: tối thiểu 3 H200 nodes (BF16) hoặc 2 nodes (FP8)
- Break-even: >500M tokens/tháng

**V4 Flash khi nào:**
- GPU memory là binding constraint
- Tail latency SLAs khắt khe
- Single/dual-node deployments
- Workload 32K-200K token (extraction, summarization — không multi-hop reasoning)

## Related concepts

- [[csa-hca-attention]]
- [[fp4-lightning-indexer]]
- [[long-context-models]]

## Sources

- [[src_deepseek-v4-architecture]]

## Notes

