---
type: source
original: "[[2026-06-08_tokens-and-tokenization]]"
main_tag: ai
sub_tags: [research, tools]
topic: tokenization-llm
date_compiled: 2026-06-09
url: https://bearisland.dev/posts/tokens-and-tokenization/
author: "Bear Island"
---

# Tokens and Tokenization

## Metadata

- **Author:** Bear Island
- **Published:** Unknown
- **Source:** Bear Island (bearisland.dev)
- **URL:** https://bearisland.dev/posts/tokens-and-tokenization/
- **Type:** article

## Summary

Bài viết giải thích chi tiết cách LLM xử lý text thông qua tokenization. Token là đơn vị nhỏ nhất mà model cụ thể có thể nhận biết — không phải ký tự, không phải từ. Mỗi model có vocabulary riêng, được xây dựng qua thuật toán BPE (Byte Pair Encoding). Ví dụ điển hình: GPT-4 trả lời "strawberry" có 2 chữ 'r' vì nó thực sự thấy 3 token ["str", "aw", "berry"] thay vì các ký tự riêng lẻ. Bài viết cũng phân tích trade-off của vocabulary size: lớn hơn = nén tốt hơn nhưng tốn nhiều parameter, training kém cho token hiếm, và inference chậm hơn.

## Key points

- Token là đơn vị nhỏ nhất model có thể nhận biết — không phải ký tự, không phải từ
- Mỗi model có vocabulary riêng (V entries) — GPT-4 khác Claude khác Llama
- Ví dụ "I love strawberry milkshakes!": GPT-4 = 9 tokens, Llama 3 = 7 tokens
- GPT-4 không thấy chữ 'r' trong "strawberry" vì tokenize thành ["str", "aw", "berry"]
- BPE (Byte Pair Encoding): merge cặp ký tự phổ biến nhất lặp đi lặp lại để xây vocabulary
- Byte-level BPE (GPT-2): bắt đầu từ 256 bytes — loại bỏ out-of-vocabulary, nhưng non-ASCII text tốn nhiều token hơn
- Vocabulary size là trade-off: compression vs parameter cost vs training quality vs inference speed
- Cost lớn nhất của vocabulary lớn: embedding matrices (2 × V × d parameters)
- Token hiếm (long tail) trong vocabulary lớn gần như không được train đủ

## Concepts referenced

- [[tokenization]]
- [[bpe-algorithm]]
- [[vocabulary-size-tradeoff]]
- [[byte-level-bpe]]

## Original excerpts

> "A token is the smallest unit of input a specific model can perceive."

> "The model never sees text. It sees a sequence of integer indices into its own private alphabet."

> "The fastest way to kill what you love is to try to get paid for it."

> "Vocabulary size is a tradeoff: compression vs. parameter cost vs. training quality vs. inference speed."
