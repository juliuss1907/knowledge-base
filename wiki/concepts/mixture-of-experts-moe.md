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

# Mixture of Experts (MoE) - DeepSeek V4

## Definition

Kiến trúc MoE trong DeepSeek V4 với routing innovations: adaptive routing temperature tự điều chỉnh độ sharpness của routing distribution dựa trên token-level uncertainty, plus shared experts pool.

## Key innovations

- **Auxiliary-loss-free load balancing:** Từ V3
- **Adaptive routing temperature:** Tự động điều chỉnh dựa trên token uncertainty
- **Shared experts:** Pool nhỏ nhận routing probability mass từ mọi token — đảm bảo universal language capability không bị mất

## Comparison

| Model | Total params | Activated/token | Ratio |
|-------|--------------|-----------------|-------|
| Mixtral 8×22B | 176B | ~28% | - |
| V3 | 671B | ~37B (5.5%) | - |
| V4 Pro | 1.6T | ~49B (3.1%) | Higher sparsity |
| V4 Flash | 284B | ~13B (4.6%) | Lower per-token cost |

## Related concepts

- [[csa-hca-attention]]
- [[deepseek-v4-flash-vs-pro]]

## Sources

- [[src_deepseek-v4-architecture]]

## Notes

