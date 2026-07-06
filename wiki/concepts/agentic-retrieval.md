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

# Agentic Retrieval

## Definition

Agentic retrieval là mô hình retrieval đa bước (multi-step), iterative, nơi AI agent không chỉ thực hiện một lần truy vấn rồi ném toàn bộ kết quả vào context window, mà chủ động suy luận về nhu cầu thông tin, chọn công cụ tìm kiếm phù hợp (semantic, full-text, grep, filters), đánh giá kết quả, và quyết định bước tiếp theo. Đây là sự tiến hóa từ RAG one-shot (2023-2024) sang mô hình retrieval có reasoning (2025-nay).

## Key ideas

- Giai đoạn 2023-2024: gọi vector DB một lần → ném hết vào context window (one-shot retrieval)
- Giai đoạn 2025-nay: agent reasoning qua nhiều bước, search semantic/full-text tùy nhu cầu, chỉ fetch đúng thứ cần
- Retrieval trở thành vòng lặp: agent hiểu mình đang search gì, và search để hiểu thêm
- Khác với Claude Code (grep loop thủ công mỗi session), agentic retrieval có thể tận dụng pre-indexed semantic search như cached compute
- Đích đến là hybrid, tool-rich, iterative retrieval — nơi agent không chỉ tìm kiếm mà còn hiểu thứ nó đang tìm

## Related concepts

- [[hybrid-retrieval]]
- [[cached-compute-retrieval]]

## Sources

- [[src_rag-is-dead-kuba-turbopuffer]]

## Notes

