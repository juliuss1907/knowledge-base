---
type: concept
status: draft
main_tag: ai
sub_tags: [research, tech]
topic: deepseek-v4-architecture
sources:
  - "[[src_deepseek-v4-architecture]]"
last_updated: 2026-05-29
---

# Manifold-Constrained Hyper-Connections (MCHC)

## Definition

Innovation trong DeepSeek V4 thay thế standard residual connections. MCHC parameterize connectivity giữa các sublayer → model học input-dependent weighting, với manifold constraint ép learned weights vào lower-dimensional manifold.

## Key ideas

- **Standard residual:** Mỗi sublayer output cộng vào residual stream với uniform weight
- **MCHC:** Learned connectivity weights, constrained vào manifold ổn định
- **Result:** Output variance thấp hơn trên các input tương tự → behavior production predictable hơn
- **Critical for multi-agent:** Trong deployments với hàng chục model calls, variance accumulation là quality degradation mechanism

## Fine-tuning implications

- Standard LoRA có thể không tôn trọng manifold geometry → giảm inference consistency
- Dùng MCHC-aware fine-tuning guidelines từ DeepSeek

## Related concepts

- [[csa-hca-attention]]
- [[deepseek-v4-flash-vs-pro]]

## Sources

- [[src_deepseek-v4-architecture]]

## Notes

