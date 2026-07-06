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

# Hybrid Retrieval

## Definition

Hybrid retrieval là phương pháp kết hợp nhiều kỹ thuật tìm kiếm — vector search (semantic embedding), full-text search (BM25), grep, glob, regex, và metadata filters — trong cùng một pipeline retrieval. Khác với RAG truyền thống vốn chỉ dùng vector search one-shot, hybrid retrieval cho phép agent chọn công cụ phù hợp theo từng bước truy vấn, cải thiện độ chính xác và giảm token lãng phí.

## Key ideas

- Retrieval không chỉ là vector search mà là tổ hợp các công cụ: semantic + full-text + pattern matching + filters
- Jeff Dean: "You don't need a trillion at once, you need the right million" — staged retrieval dùng cơ chế nhẹ để thu hẹp từ hàng nghìn tỷ token xuống đúng vài trăm nghìn token cần thiết
- Agentic search dùng hybrid retrieval như một vòng lặp: agent hiểu mình đang tìm gì, chọn công cụ phù hợp, search để hiểu thêm, rồi lặp lại
- Cursor là case study tiêu biểu: index toàn bộ codebase với semantic search kết hợp Merkle trees → +12.5% accuracy
- Từ 2025, xu hướng chuyển từ one-shot retrieval sang iterative, tool-rich retrieval

## Related concepts

- [[cached-compute-retrieval]]
- [[agentic-retrieval]]

## Sources

- [[src_rag-is-dead-kuba-turbopuffer]]

## Notes

