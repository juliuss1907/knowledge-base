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

# Agent Memory Taxonomy

## Definition

Phân loại bộ nhớ trong hệ thống agent dựa trên khoa học nhận thức (cognitive science), gồm 4 loại chính: episodic (sự kiện), semantic (kiến thức), procedural (kỹ năng), và prospective (kế hoạch tương lai). Trong thực tế, hầu hết thư viện agent memory chỉ triển khai một phần nhỏ — chủ yếu là semantic memory dạng autobiographical.

## Key ideas

- **Episodic memory**: Sự kiện cụ thể gắn với thời gian/địa điểm — "coffee với Aleksandra thứ Ba tuần trước"
- **Semantic memory**: Kiến thức không gắn sự kiện — "Berlin là thủ đô Đức"
- **Procedural memory**: Biết "cách làm" — đi xe đạp, gõ phím tắt, không thể verbalize
- **Prospective memory**: Nhớ làm gì trong tương lai — "gửi hợp đồng ngày mai"
- **Autobiographical memory**: Tập con của semantic — thông tin về bản thân người dùng mà agent giữ hộ
- **Working memory**: Context window — tách biệt với long-term memory systems
- Production libraries thường nén episodic → semantic tại extraction
- Procedural thường bị mislabeled (Mem0: metadata.memory_type="procedural" nhưng storage giống semantic)
- Prospective gần như absent — chỉ có scheduled triggers, không có "when condition X appears"

## Related concepts

- [[memory-extraction-timing]]
- [[consolidation-offline-processing]]
- [[autobiographical-memory-systems]]

## Sources

- [[src_agent-memory-anatomy]]

## Notes
