---
type: concept
status: draft
main_tag: ai
sub_tags: [automation, coding]
topic: loop-engineering
sources:
  - "[[src_loop-engineering-14-step-roadmap]]"
last_updated: 2026-06-30
---

# Comprehension Debt

## Definition

Comprehension debt (nợ hiểu biết) là khoảng cách ngày càng lớn giữa những gì repository chứa và những gì developer thực sự hiểu, được gia tốc bởi loop engineering ship code nhanh hơn khả năng đọc và comprehend của con người. Khác với technical debt (nợ kỹ thuật — code cần refactor), comprehension debt là nợ về mặt nhận thức: hệ thống hoạt động nhưng không ai trong team thực sự hiểu nó.

## Key ideas

- Loop càng hiệu quả trong việc ship code, comprehension debt tích lũy càng nhanh
- "The bill that hurts is not the token bill. It is the day you have to debug a system no one on the team has read."
- Mitigation: đọc diffs (nếu không đọc là thuê nợ với lãi kép), spot-check gate, block loop khỏi architecture work, pair-design loops
- Không phải vấn đề kỹ thuật mà là vấn đề kỷ luật — không có công cụ nào tự động giải quyết được
- Comprehension debt là lãi kép (compound interest): càng để lâu càng đắt khi phải trả

## Related concepts

- [[loop-engineering]]
- [[cognitive-surrender]]
- [[ralph-wiggum-loop]]

## Sources

- "[[src_loop-engineering-14-step-roadmap]]"

## Notes
