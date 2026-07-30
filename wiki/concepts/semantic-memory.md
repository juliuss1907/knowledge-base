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

# Semantic Memory

## Definition

Semantic memory lưu trữ facts, concepts, và general knowledge — kiểu thông tin bạn có thể tra cứu mà không cần nhớ context cụ thể khi học nó. Trong AI agents, thường được implement bằng vector databases để lưu và retrieve relevant information dựa trên semantic similarity.

## Key ideas

- Lưu trữ dạng "what" — facts và knowledge không gắn với specific experiences
- Thường implement bằng vector DBs (Pinecone, Weaviate, pgvector, etc.)
- Cần careful chunking strategy — chunks quá nhỏ mất context, quá lớn khó retrieve precisely
- Retrieval quality phụ thuộc vào embedding model và similarity metric
- Phải được đưa vào working memory (qua retrieval) trước khi model có thể sử dụng
- Risk: irrelevant information retrieved có thể confuse model hoặc làm tăng token cost

## Related concepts

- [[in-context-memory]]
- [[episodic-memory]]
- [[vector-database]]
- [[embedding-models]]

## Sources

- [[src_agent-memory-7-types-substack.md]]

## Notes
