---
type: concept
status: draft
main_tag: ai
sub_tags: [research, tools]
topic: retrieval-augmented-generation
sources:
  - [[src_google-generative-ai-search-guide]]
last_updated: 2026-05-24
---

# Retrieval-Augmented Generation (RAG)

## Definition

Retrieval-Augmented Generation (RAG) là kỹ thuật kết hợp information retrieval với text generation trong AI systems. Thay vì chỉ dựa vào parametric knowledge của model, RAG retrieve thông tin từ external knowledge base để augment và ground responses.

## Key ideas

- RAG giúp reduce hallucination bằng cách grounding AI responses trong retrieved factual information
- Google's AI search features sử dụng RAG để pull content từ Search index và highlight trong AI Overviews
- Query fan-out là một implementation detail — breaking queries into sub-queries để retrieve từ multiple sources
- Content phải rank tốt trong traditional search để được retrieve và cite trong RAG-based responses
- RAG không chỉ là technical technique mà còn là architectural pattern cho enterprise AI applications

## Related concepts

- [[ai-overviews]]
- [[generative-search-results]]
- [[vector-database]]
- [[embedding-search]]

## Sources

- [[src_google-generative-ai-search-guide]]

## Notes
