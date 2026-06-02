---
type: concept
status: reviewed
main_tag: ai
sub_tags: [research, opinion]
topic: agent-memory-systems
sources:
  - "[[src_agent-memory-anatomy]]"
last_updated: 2026-05-27
---

# Autobiographical Memory Systems

## Definition

Hệ thống bộ nhớ mà agent dùng để lưu trữ thông tin về người dùng thay cho họ — where they live, what they're working on, what they've decided. Đây là subset của semantic memory, và là thực chất của hầu hết "agent memory libraries" hiện nay.

## Key ideas

- Không phải "cognitive memory system" đầy đủ — narrower than the word suggests
- Agent không nhớ "cuộc đời của chính nó" — mà giữ "cuộc đời của user" by proxy
- Scope: user preferences, personal facts, ongoing tasks, relationships
- Contrast với full episodic/semantic/procedural/prospective taxonomy
- Khi người ta nói "agent should remember the user" — thường mean đây
- Triển khai: vector index + relational table + knowledge graph
- Key challenge: handling contradictions ("lived in Paris until April, then moved to Amsterdam")

## Related concepts

- [[agent-memory-taxonomy]]
- [[memory-extraction-timing]]

## Sources

- [[src_agent-memory-anatomy]]

## Notes
