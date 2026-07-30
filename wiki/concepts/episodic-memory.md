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

# Episodic Memory

## Definition

Episodic memory lưu trữ specific experiences, interactions, và events — những kỷ niệm gắn với context cụ thể như "user này thích Python hơn JavaScript" hay "lần trước task này failed vì lý do X". Giúp agent personalize responses và học từ history với từng user cụ thể.

## Key ideas

- Lưu trữ dạng "when/where/what happened" — experiences có context
- Cho phép personalization: agent nhớ preferences và history của từng user
- Khác với semantic memory ở chỗ gắn với specific instances thay vì general facts
- Implementation: conversation logs, user profiles, interaction history databases
- Challenge: quyết định what to remember (tất cả interactions hay chỉ significant ones?)
- Risk: outdated preferences có thể persist quá lâu, hoặc information từ user A leak sang user B

## Related concepts

- [[semantic-memory]]
- [[procedural-memory]]
- [[personalization]]

## Sources

- [[src_agent-memory-7-types-substack.md]]

## Notes
