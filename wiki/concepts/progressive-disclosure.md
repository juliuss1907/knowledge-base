---
type: concept
status: draft
main_tag: ai
sub_tags: [tools, automation]
topic: agent-context-optimization
sources:
  - "[[src_openviking]]"
last_updated: 2026-08-31
---

# Progressive Disclosure

## Definition

Progressive disclosure là kỹ thuật tổ chức nội dung thành nhiều tầng độ chi tiết, chỉ "mở khóa" tầng sâu hơn khi cần thiết. Trong ngữ cảnh AI agents, OpenViking triển khai dưới dạng L0 (abstract — một câu tóm tắt), L1 (overview — thông tin cốt lõi), L2 (details — dữ liệu gốc đầy đủ). Agent scan nhanh tầng nhẹ để đánh giá relevance, chỉ load tầng nặng khi task yêu cầu — giúp cắt giảm token spend đáng kể trong khi vẫn giữ khả năng truy cập toàn bộ context.

## Key ideas

- **Ba tầng tiêu chuẩn:** L0 abstract (1 câu) cho relevance check nhanh · L1 overview (thông tin + use case) cho planning · L2 details (toàn bộ dữ liệu gốc) chỉ đọc khi cần
- **Mỗi directory mang L0/L1 riêng:** Relevance đánh giá được trước khi đọc bất kỳ file đầy đủ nào
- **Giảm token đáng kể:** Input tokens giảm 34.3–91.0% trong đánh giá LoCoMo nhờ load on-demand
- **Tương tự progressive disclosure trong agent skills:** Metadata → instructions → supporting files (agentskills.io standard)
- **Tư duy cốt lõi:** Nguyên tắc "tiết lộ dần" — đưa đúng lượng thông tin phù hợp với ngữ cảnh hiện tại, tránh tràn ngập context

## Related concepts

- [[context-database]]
- [[context-window-management]]
- [[agent-skill-management]]

## Sources

- [[src_openviking]]

## Notes