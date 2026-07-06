---
type: source
original: "[[2026-07-05_rag-is-dead-kuba-turbopuffer]]"
main_tag: ai
sub_tags: [tools, research, coding]
topic: hybrid-retrieval-agentic-search
date_compiled: 2026-07-06
url: https://www.youtube.com/watch?v=UM6sFg_jdlE
author: Kuba (Turbopuffer) / Julius (notes)
---

# RAG is Dead — Kuba @ Turbopuffer

## Metadata

- **Author:** Kuba (Deployed Engineer, Turbopuffer)
- **Published:** 2026-07
- **Source:** YouTube (Turbopuffer)
- **URL:** https://www.youtube.com/watch?v=UM6sFg_jdlE
- **Type:** video

## Summary

Bài talk phân tích sự chuyển đổi từ RAG truyền thống sang Agentic Retrieval, nơi retrieval không còn là one-shot vector search đơn thuần mà là vòng lặp nhiều bước với nhiều công cụ. Kuba lập luận rằng semantic search thực chất là "cached compute" — đầu tư chi phí index upfront một lần để tiết kiệm đáng kể runtime về sau, như cách Cursor index toàn bộ codebase với Merkle trees để phát hiện trùng lặp. Dữ liệu từ Cursor cho thấy semantic search cải thiện +12.5% độ chính xác câu trả lời và giảm dissatisfied requests. Quote từ Jeff Dean nhấn mạnh staged retrieval quan trọng hơn context window khổng lồ: "You don't need a trillion at once, you need the right million."

## Key points

- RAG truyền thống bị hiểu nhầm là vector search one-shot đơn giản, nhưng thực chất retrieval còn bao gồm full-text (BM25), grep, glob, regex, và filters
- Agentic search không chỉ là filesystem grep — agent được trao bộ công cụ để suy luận tiến bộ và tìm kiếm lặp đi lặp lại over context
- Case study Cursor: index toàn bộ codebase với semantic search → +12.5% accuracy, +2.6% code retention, -2.2% dissatisfied user requests
- Cursor dùng Merkle trees để phát hiện codebase trùng lặp giữa các dev trong cùng team, sao chép data cũ thay vì re-index → tiết kiệm chi phí khổng lồ
- Semantic search là "cached compute": trả upfront cost một lần, retrieval nhẹ lúc runtime — team Turbopuffer đang chuyển từ Claude Code sang Cursor vì tốc độ và semantic understanding
- Từ 2025, retrieval trở thành vòng lặp multi-step: agent hiểu mình đang search gì, và search để hiểu thêm
- Quote Jeff Dean: "You don't need a trillion at once, you need the right million" — staged retrieval với cơ chế nhẹ để thu hẹp context quan trọng hơn context window khổng lồ
- Hybrid retrieval (semantic + full-text + filters) đang trở thành tiêu chuẩn cho agentic search

## Concepts referenced

- [[hybrid-retrieval]]
- [[cached-compute-retrieval]]
- [[agentic-retrieval]]

## Original excerpts

> "You don't need a trillion at once, you need the right million."
> — Jeff Dean (Google)

> "Take that, Twitter."
> — Kuba, về việc Google search volume cho "RAG" tăng vọt dù Twitter nói RAG đã chết

**Data:** Cursor semantic search → +12.5% accuracy, +24% với Composer cũ, +2.6% code retention, -2.2% dissatisfied requests
