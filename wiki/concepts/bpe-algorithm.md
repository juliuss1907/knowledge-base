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

# BPE Algorithm

## Definition

Byte Pair Encoding — thuật toán xây dựng vocabulary cho LLM. Bắt đầu với vocabulary là các ký tự (hoặc bytes), sau đó lặp đi lặp lại việc merge cặp ký tự phổ biến nhất cho đến khi đạt vocabulary size target V. Không có neural network, không có clever scoring — chỉ đơn giản là đếm tần suất và merge.

## Key ideas

- **Thuật toán:**
  1. Initialize vocabulary = mỗi ký tự riêng biệt trong corpus (hoặc 256 bytes)
  2. Đến mọi cặp adjacent tokens trong corpus
  3. Merge cặp phổ biến nhất thành token mới
  4. Lặp lại cho đến khi vocabulary có V entries
- Original tokens không biến mất — khi merge "t" + "h" → "th", cả "t", "h", "th" đều còn trong vocabulary
- Pairs được re-count sau mỗi merge — khi "th" là token, iteration tiếp sẽ đếm "th" + "e"
- Đơn giản nhưng hiệu quả — tạo vocabulary cân bằng giữa coverage và compression
- Các biến thể: WordPiece (Google, dùng likelihood thay vì frequency), SentencePiece (treat input như raw character stream, không preprocessing)

## Related concepts

- [[tokenization]]
- [[byte-level-bpe]]

## Sources

- [[src_tokens-and-tokenization]]

## Notes
