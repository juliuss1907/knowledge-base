---
type: concept
status: draft
main_tag: ai
sub_tags: [tools, research, coding]
topic: hybrid-retrieval-agentic-search
sources:
  - "[[src_rag-is-dead-kuba-turbopuffer]]"
last_updated: 2026-07-06
---

# Cached Compute (Retrieval)

## Definition

Cached compute retrieval là cách nhìn coi semantic search và embedding index như một khoản đầu tư upfront — trả chi phí index một lần duy nhất để tiết kiệm đáng kể computation lúc runtime. Thay vì mỗi agent phải grep → read → assess → repeat từ đầu cho mỗi session (như Claude Code), việc pre-index cho phép retrieval siêu nhẹ và tái sử dụng kết quả cho nhiều truy vấn khác nhau.

## Key ideas

- Semantic search/embedding là "cached compute": chi phí trả trước một lần, runtime query nhẹ hơn grep-loop rất nhiều
- Claude Code (theo Boris Cherney) từng thử RAG với local vector DB nhưng không hoạt động, phải dùng grep → read → assess → repeat mỗi session
- 10 agent × 10 ngày × 10 developer hỏi cùng một câu → lặp lại y hệt các bước, tốn token vô ích nếu không có cached compute
- Cursor ngược lại: upfront cost index → runtime query nhẹ, team Turbopuffer đang chuyển từ Claude Code sang Cursor vì lý do này
- Merkle trees (crypto hash tree) được Cursor dùng để phát hiện codebase trùng lặp → copy data cũ, chỉ re-index file thay đổi

## Related concepts

- [[hybrid-retrieval]]
- [[agentic-retrieval]]

## Sources

- [[src_rag-is-dead-kuba-turbopuffer]]

## Notes

