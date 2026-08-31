---
type: concept
status: draft
main_tag: tech
sub_tags: [tools, coding, automation]
topic: architecture-as-code
sources:
  - "[[src_archify]]"
last_updated: 2026-08-31
---

# Architecture as Code

## Definition

Architecture as code là phương pháp biểu diễn kiến trúc hệ thống dưới dạng typed JSON IR mà agent và công cụ có thể validate, render và so sánh một cách deterministic — thay vì vẽ diagram thủ công hoặc tin vào auto-layout. Archify minh họa mô hình này: agent sản xuất JSON IR có schema, Archify compile thành HTML/SVG với atomic validation trước khi deliver. Điểm cốt lõi là mọi artifact đều grounded trong authored nodes và có receipt, đảm bảo kiến trúc hiển thị khớp với intent, không tự bịa topology.

## Key ideas

- **Typed JSON IR là nguồn sự thật:** Diagram là output compile từ IR, không phải vẽ tay
- **Atomic validation trước khi deliver:** Schema, layout, HTML/SVG, route, clearance phải pass; failures kèm repair receipt
- **Layout judgment của agent:** Agent chọn hierarchy/routes/emphasis thay vì generic auto-layout
- **Before/Delta/After compare:** So sánh snapshots kiến trúc với receipt trước khi merge
- **Evidence-backed:** Có thể mở Git-verified source files pinned commit khi cần
- **Deterministic output:** Cùng IR → cùng artifact, không biến thiên
- **Portable:** Kết quả 1 HTML file, export PNG/SVG/WebM/share cards

## Related concepts

- [[code-visualization]]
- [[system-map]]
- [[architecture-diagram]]
- [[diagram-as-code]]

## Sources

- [[src_archify]]

## Notes