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

# Tokenization

## Definition

Quá trình chuyển đổi text thành các token — đơn vị nhỏ nhất mà model cụ thể có thể nhận biết. Token không phải ký tự, không phải từ, mà là các chunk subword được định nghĩa trong vocabulary của model. Mỗi model có vocabulary riêng, do đó cùng một câu sẽ được tokenize thành số lượng token khác nhau trên các model khác nhau.

## Key ideas

- Token là đơn vị nhỏ nhất model có thể nhận biết
- Không phải ký tự, không phải từ — là subword chunks
- Mỗi model có vocabulary riêng (V entries) — GPT-4 khác Claude khác Llama
- Ví dụ "strawberry": GPT-4 = ["str", "aw", "berry"] = 3 tokens; Llama 3 = ["straw", "berry"] = 2 tokens
- Cùng câu "I love strawberry milkshakes!": GPT-4 = 9 tokens, Llama 3 = 7 tokens
- Model không bao giờ thấy text — chỉ thấy sequence of integer IDs
- Tokenization ảnh hưởng mọi thứ: context window, pricing, model behavior
- "strawberry problem": GPT-4 không thể đếm chữ 'r' vì không thấy ký tự riêng lẻ

## Related concepts

- [[bpe-algorithm]]
- [[byte-level-bpe]]
- [[vocabulary-size-tradeoff]]

## Sources

- [[src_tokens-and-tokenization]]

## Notes
