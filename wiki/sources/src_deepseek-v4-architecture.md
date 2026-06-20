---
type: source
original: "[[2026-05-28_deepseek-v4-architecture-deep-dive]]"
main_tag: ai
sub_tags: [research, tools]
topic: deepseek-v4-architecture
date_compiled: 2026-05-29
url: https://boringbot.substack.com/p/deepseek-v4-architecture-deep-dive
author: Hamza Farooq (UCLA, MAVEN, Traversaal.ai)
---

# DeepSeek V4 Architecture Deep Dive

## Metadata

- **Author:** Hamza Farooq (UCLA, MAVEN, Traversaal.ai)
- **Published:** 2026-05-13
- **Source:** Substack — Boring Bot
- **URL:** https://boringbot.substack.com/p/deepseek-v4-architecture-deep-dive
- **Type:** article

## Summary

Phân tích kiến trúc DeepSeek V4 Pro (1.6T tham số) và V4 Flash (284B). Tập trung vào architectural innovations: CSA/HCA hybrid attention, FP4 Lightning Indexer, MCHC — những thứ quyết định production deployment, không chỉ benchmark.

## Key points

- **CSA + HCA hybrid attention:** Compressed Sparse Attention (~4× nén) + Heavily Compressed Attention (~128× nén). Không giống sliding window — CSA nén token, không bỏ qua
- **Interleaving ratio:** V4 Pro ~3:1 CSA-to-HCA; V4 Flash ~4:1 CSA-to-HCA (ít HCA hơn → latency thấp hơn)
- **Muon optimizer:** Thay thế AdamW, train trên 32T+ tokens
- **MCHC (Manifold-Constrained Hyper-Connections):** Parameterize connectivity giữa các sublayer → behavior production predictable hơn, giảm variance trong multi-agent deployments
- **Lightning Indexer:** Scoring network chạy ở FP4, chọn top-k compressed blocks cho sparse attention
- **Context window:** 1M tokens cho cả hai biến thể (vs Claude Opus max 200K)
- **Activation ratio cực thấp:** V4 Pro ~3.1% (49B/1.6T), cho phép inference rẻ hơn dù model lớn

## Specs comparison

| Thông số | V4 Pro | V4 Flash |
|----------|--------|----------|
| Tổng tham số | 1.6T | 284B |
| Activated/token | ~49B (3.1%) | ~13B (4.6%) |
| Context window | 1M tokens | 1M tokens |
| Precision | FP8/FP4 (QAT) | FP8/FP4 |
| CSA:HCA ratio | ~3:1 | ~4:1 |

## Practitioner guidance

- **V4 Pro:** Workload >200K tokens, yêu cầu 3+ H200 nodes, break-even >500M tokens/tháng
- **V4 Flash:** GPU memory là constraint, tail latency SLAs khắt khe, single/dual-node deployments
- **Data sovereignty:** Deploy trên infrastructure của bạn — critical cho regulated industries
- **Fine-tuning:** Standard LoRA có thể không tôn trọng manifold geometry → dùng MCHC-aware guidelines

## Concepts referenced

- [[csa-hca-attention]]
- [[manifold-constrained-hyper-connections]]
- [[fp4-lightning-indexer]]
- [[mixture-of-experts-moe]]
- [[deepseek-v4-flash-vs-pro]]
- [[long-context-models]]

## Original excerpts

> "CSA + HCA không chỉ giảm cache size — nó thay đổi những gì model tính toán. Đây là genuine structural differentiator, không phải quantization shortcut."

> "Với 10-agent architecture xử lý 1M-token document, đây là khác biệt giữa feasible memory budget và infeasible."

> "Câu hỏi 'open-weights có đạt frontier quality không' đã được giải quyết. V4 Pro's benchmark parity với Claude Opus xác nhận điều đó."
