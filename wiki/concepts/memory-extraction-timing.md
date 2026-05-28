---
type: concept
status: draft
main_tag: ai
sub_tags: [research, tools]
topic: agent-memory-systems
sources:
  - [[src_agent-memory-anatomy]]
last_updated: 2026-05-27
---

# Memory Extraction Timing

## Definition

Quyết định khi nào trích xuất thông tin từ conversation thành memory statements — một trong những lựa chọn thiết kế quan trọng nhất trong agent memory systems.

## Key ideas

- **Eager extraction**: Sau mỗi message — tốn token trên small talk, không mất ngữ cảnh
- **Lazy extraction**: Cuối session — tiết kiệm token, nhưng pronoun resolution context đã mất
- Mỗi cách đều mất thứ còn lại giữ — không có "đúng" tuyệt đối
- Casualties của aggressive compression: coreference cues, temporal anchors, disambiguating context
- Extraction = compression từ "situated event" thành "decontextualized fact"
- "user mentioned over coffee on Tuesday that they prefer TypeScript" → "user prefers TypeScript"
- Độ aggressive của compression là central design decision

## Related concepts

- [[agent-memory-taxonomy]]
- [[consolidation-offline-processing]]

## Sources

- [[src_agent-memory-anatomy]]

## Notes
