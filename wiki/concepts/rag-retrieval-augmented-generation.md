---
type: concept
status: draft
main_tag: ai
sub_tags: [research, tools]
topic: generative-ai-seo
sources:
  - [[wiki/sources/src_google-guide-optimizing-generative-ai-search]]
last_updated: 2026-05-19
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

## Related concepts

- [[generative-ai-search-optimization]]
- [[query-fan-out]]

## Sources

- [[wiki/sources/src_google-guide-optimizing-generative-ai-search]]

## Notes
