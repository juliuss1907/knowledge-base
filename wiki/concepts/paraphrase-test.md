---
type: concept
status: draft
main_tag: ai
sub_tags: [opinion]
topic: ai-writing-habits
sources:
  - "[[src_habits-of-ai-writing-a16z-crypto]]"
last_updated: 2026-08-26
---

# Paraphrase Test

## Definition

Bộ test biên tập để đánh giá câu văn độc lập với nguồn gốc human/AI, gồm ba phép thử chính: paraphrase (nói lại bằng từ khác — nếu rút gọn còn "stuff exists" thì xóa), transplant (câu có thể bị nhổ cắm sang bài của người khác không), và read-aloud (đọc thành tiếng dùng dấu câu như stage directions).

## Key ideas

- Paraphrase test: nếu câu paraphrase được sang version tốt hơn thì giữ version đó; nếu boil down thành "stuff exists" hoặc "things are changing" thì xóa hẳn và xem bài có sống thiếu nó không
- Transplant test: phát hiện tính fungible của voice — câu generic có thể xuất hiện trong bất kỳ bài viết nào về bất kỳ topic nào mà không gây ra consequence
- Read-aloud test: punctuation như stage directions; mọi thứ nghe không tự nhiên sẽ đứng ra với reader y như vậy
- Cách chạy bằng LLM: yêu cầu viết "boring version" của đoạn mình, hoặc prompt model flag hedging/fungible phrasing thay vì tự dò
- Mục tiêu chung của cả ba test: văn bản information-dense nhưng dễ đọc, cụ thể thay vì generic — "The Ethereum ecosystem is expanding" trở thành "Developers are building more wallets, exchanges, and lending markets around Ethereum"

## Related concepts

- [[ai-writing-hallmarks]]
- [[non-commodity-content]]

## Sources

- [[src_habits-of-ai-writing-a16z-crypto]]
