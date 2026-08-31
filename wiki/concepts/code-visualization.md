---
type: concept
status: draft
main_tag: tech
sub_tags: [tools, coding]
topic: code-visualization
sources:
  - "[[src_archify]]"
last_updated: 2026-08-31
---

# Code Visualization

## Definition

Code visualization là việc chuyển đổi codebase hoặc mô tả hệ thống thành diagram trực quan có thể tương tác, giúp hiểu cấu trúc, luồng dữ liệu và mối quan hệ giữa các thành phần. Archify tiên phong mô hình "agent-produced": coding agent phân tích repository hoặc description, tạo typed JSON IR, sau đó deterministic render thành HTML/SVG. Khác với công cụ auto-layout truyền thống, agent có layout judgment nên chọn hierarchy, routes và emphasis phù hợp với intent thay vì chỉ dàn đều nodes.

## Key ideas

- **5 loại diagram:** Architecture · Workflow · Sequence · Data Flow · Lifecycle — mỗi loại có prompt guidance riêng
- **Agent-produced visualization:** Agent phân tích rồi tạo IR, không cần repository (mô tả trực tiếp cũng được)
- **Truthful interaction:** Search nodes, upstream/downstream reach, route trace, role compare, stories — đều grounded trong authored nodes
- **Interactive** : Focus với `/`, trace route `R`, radar map `M`, guided story `P`, presentation stage `F`
- **Stable deep links:** `#focus=id`, `#route=src~tgt`, `#lens=kind~kind` restore trạng thái xem
- **Share cards:** 1200×630 canonical image cho README/release/social

## Related concepts

- [[architecture-as-code]]
- [[system-map]]
- [[diagram-as-code]]

## Sources

- [[src_archify]]

## Notes