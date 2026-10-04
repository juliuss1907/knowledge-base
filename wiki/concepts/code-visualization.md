---
type: concept
status: draft
main_tag: tech
sub_tags: [tools, coding]
topic: code-visualization
sources:
  - "[[src_archify]]"
  - "[[src_unreasonable-effectiveness-of-html]]"
last_updated: 2026-10-03
---

# Code Visualization

## Definition

Code visualization là việc chuyển đổi codebase hoặc mô tả hệ thống thành diagram trực quan có thể tương tác, giúp hiểu cấu trúc, luồng dữ liệu và mối quan hệ giữa các thành phần. Archify tiên phong mô hình "agent-produced": coding agent phân tích repository hoặc mô tả hệ thống, tạo typed JSON IR, sau đó kết xuất tất định thành HTML/SVG. Khác với công cụ tự sắp xếp bố cục truyền thống, agent có phán đoán bố cục nên chọn phân cấp, các tuyến và điểm nhấn phù hợp với ý đồ thay vì chỉ dàn đều các nút.

## Key ideas

- **5 loại diagram:** Architecture · Workflow · Sequence · Data Flow · Lifecycle — mỗi loại có prompt guidance riêng
- **Agent-produced visualization:** Agent phân tích rồi tạo IR, không cần repository (mô tả trực tiếp cũng được)
- **Truthful interaction:** Search nodes, upstream/downstream reach, route trace, role compare, stories — đều grounded trong authored nodes
- **Interactive**: Focus với `/`, trace route `R`, radar map `M`, guided story `P`, presentation stage `F`
- **Stable deep links:** `#focus=id`, `#route=src~tgt`, `#lens=kind~kind` restore trạng thái xem
- **Share cards:** 1200×630 canonical image cho README/release/social
- **HTML như canvas cho diagram sinh bởi agent:** Thariq Shihipar (Anthropic) liệt kê workflow, data flow và spatial layout như những dạng HTML biểu diễn tốt — thay cho ASCII diagram hoặc ước lượng màu bằng unicode mà model buộc phải làm trong Markdown
- **Code review bằng HTML:** render diff với inline margin annotations, color-code finding theo severity, thành explainer với navigation, collapsible steps, tabbed code snippets
- **Nguồn dữ liệu cho diagram:** Claude Code đọc codebase thật, gom nhóm các artifact đã sinh rồi dựng diagram đại diện cho từng nhóm — xem [[html-as-agent-output-format]]

## Related concepts

- [[architecture-as-code]]
- [[system-map]]
- [[html-as-agent-output-format]]
- [[multi-file-artifact-workflow]]

## Sources

- [[src_archify]]
- [[src_unreasonable-effectiveness-of-html]] — Thariq Shihipar, Anthropic (2026-05-20)

## Notes
