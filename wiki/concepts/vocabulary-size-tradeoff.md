---
type: concept
status: draft
main_tag: ai
sub_tags: [research, tools]
topic: tokenization-llm
sources:
  - "[[src_tokens-and-tokenization]]"
last_updated: 2026-06-09
---

# Vocabulary Size Tradeoff

## Definition

Trade-off trong việc chọn vocabulary size V cho LLM. Vocabulary size ảnh hưởng đến nén (compression), parameter cost, training quality, và inference speed. Lớn hơn không phải lúc nào cũng tốt hơn.

## Key ideas

- **Lợi ích (bigger V):** nén tốt hơn — common substrings collapse thành single tokens
- **Chi phí 1: embedding matrices** — 2 × V × d parameters
  - V=32K, d=4,096 → 262M parameters
  - V=128K → 1.05B parameters
  - V=1M → 8.19B parameters (bằng cả một model 8B-class)
- **Chi phí 2: rare tokens không được train đủ** — Zipf's law: top 1K tokens cover ~80%, top 10K cover ~95%
  - V=1M trên 1T corpus: hàng trăm nghìn tokens chỉ thấy 10-100 lần
- **Chi phí 3: inference expensive** — mỗi prediction = probability distribution over V tokens
  - V×d matrix multiplication là một trong những operation đắt nhất
- **Trade-off:** parameter cost ∝ V, compression gain ∝ log V
- **Real models:**
  - LLaMA 1/2: 32K (English-focused)
  - GPT-4: ~100K
  - LLaMA 3: 128K (multilingual)
  - Gemini: 256K (heavy multilingual)

## Related concepts

- [[tokenization]]
- [[bpe-algorithm]]

## Sources

- [[src_tokens-and-tokenization]]

## Notes
