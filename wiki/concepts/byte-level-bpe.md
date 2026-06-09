---
type: concept
status: draft
main_tag: ai
sub_tags: [research, coding]
topic: tokenization-llm
sources:
  - "[[src_tokens-and-tokenization]]"
last_updated: 2026-06-09
---

# Byte-Level BPE

## Definition

Biến thể BPE được GPT-2 giới thiệu: bắt đầu với 256 bytes thay vì các ký tự riêng biệt. Đảm bảo mọi text có thể biểu diễn trên máy tính đều có thể tokenize được — loại bỏ vấn đề out-of-vocabulary. Tuy nhiên, text non-ASCII (tiếng Trung, Ả Rập, Hindi) sẽ tốn nhiều token hơn khi dùng model train chủ yếu trên English.

## Key ideas

- Bắt đầu với 256 bytes — vocabulary initial cố định, không phụ thuộc corpus
- Mọi byte đều có trong vocabulary by definition
- Mọi text biểu diễn được trên máy tính đều tokenize được — out-of-vocabulary = eliminated
- UTF-8 encoding: mỗi Unicode character = 1-4 bytes:
  - ASCII (A): 1 byte
  - European scripts (é): 2 bytes
  - Asian scripts (中): 3 bytes
  - Emoji (🍓): 4 bytes
- Chi phí: non-ASCII text dùng nhiều token hơn khi model train trên English-heavy corpus
- Đây là lý do API pricing thường đắt hơn cho Chinese, Arabic, Hindi so với English

## Related concepts

- [[tokenization]]
- [[bpe-algorithm]]
- [[vocabulary-size-tradeoff]]

## Sources

- [[src_tokens-and-tokenization]]

## Notes
