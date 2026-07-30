---
type: concept
status: draft
main_tag: ai
sub_tags: [tools, research]
topic: agent-memory-systems
sources:
  - "[[src_agent-memory-7-types-substack.md]]"
last_updated: 2026-07-30
---

# External / Retrieval Memory

## Definition

External memory (hay retrieval memory) là pattern lấy information từ outside sources — APIs, databases, search engines, documents — và đưa vào working memory khi cần. Khác với semantic memory ở chỗ external memory không lưu trữ permanent, mà retrieve on-demand từ external systems.

## Key ideas

- Pattern: retrieve → inject vào context → model uses it → discard sau khi xong
- Sources: web search, company databases, CRM systems, document stores, APIs
- Không phải "memory" trong traditional sense mà là access pattern
- Phân biệt với semantic: semantic là stored knowledge, external là retrieved knowledge
- Key design question: when to trigger retrieval và how to format retrieved content
- Risk: retrieval latency, API failures, information staleness

## Related concepts

- [[in-context-memory]]
- [[semantic-memory]]
- [[rag-pattern]]
- [[tool-use]]

## Sources

- [[src_agent-memory-7-types-substack.md]]

## Notes
