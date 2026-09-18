---
type: concept
status: reviewed
main_tag: ai
sub_tags: [research, tools]
topic: generative-ai-seo
sources:
  - "[[src_google-guide-optimizing-generative-ai-search]]"
  - "[[src_50-system-design-concepts-explained-simply]]"
last_updated: 2026-09-18
---

# RAG (Retrieval-Augmented Generation)

## Definition

Kỹ thuật (còn gọi là grounding) để cải thiện quality, accuracy, và freshness của AI-generated responses bằng cách retrieve thông tin từ external knowledge sources trước khi generate response.

## Key ideas

- **Grounding**: Kết hợp retrieval với generation để đảm bảo responses dựa trên factual, up-to-date information
- **Retrieve relevant pages**: Dùng Search ranking systems để tìm pages phù hợp
- **Review retrieved information**: AI model đọc và tổng hợp thông tin từ các sources
- **Generate reliable response**: Response được generate dựa trên retrieved content
- **Prominent clickable links**: Hiển thị links tới relevant web pages trong output
- **Used by Google AI Overviews**: Core technique cho AI features trên Google Search
- **Two-phase pipeline**: Ingestion (chunk → embed → store in vector DB) và Query (embed question → search vector DB → include in prompt)
- **Challenges**: Chunking strategy, embedding quality, context window limits, latency in real-time retrieval

## Related concepts

- [[generative-ai-search-optimization]]
- [[query-fan-out]]
- [[vectors]]
- [[rag-retrieval-augmented-generation]]

## Sources

- [[src_google-guide-optimizing-generative-ai-search]]
- [[src_50-system-design-concepts-explained-simply]]

## Notes
