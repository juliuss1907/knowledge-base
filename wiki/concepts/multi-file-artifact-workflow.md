---
type: concept
status: draft
main_tag: ai
sub_tags: [coding, tools]
topic: html-as-agent-output
sources:
  - "[[src_unreasonable-effectiveness-of-html]]"
last_updated: 2026-10-03
---

# Multi-File Artifact Workflow

## Definition

Multi-file artifact workflow là cách tổ chức công việc với coding agent theo nhiều file artifact riêng theo từng stage, thay vì một tài liệu plan duy nhất. Mỗi file giữ một loại nội dung (exploration, UI mockup, implementation plan, danh sách design) và được giữ lại làm reference cho các session sau, kể cả session verification.

## Key ideas

- **Một plan không đủ:** tác giả bỏ hẳn mô hình single-plan, tách theo từng phần/stage — implementation plan một file, UI exploration một file, danh sách design một file khác
- **Trình tự điển hình:** brainstorm nhiều hướng khác biệt → mở rộng hướng đã chọn thành mockup/ví dụ → viết implementation plan → mở session mới và đưa toàn bộ file vào để implement
- **Giai đoạn exploration tận dụng điểm mạnh HTML:** nhiều hướng cạnh nhau trong một trang, mỗi hướng gắn nhãn trade-off của nó — so sánh bằng mắt nhanh hơn đọc tuần tự
- **Implementation plan có mockup, data flow và code snippet:** các phần khó diễn tả bằng chữ được chuyển sang hình và code để review nhanh
- **File được tái sử dụng làm context cho session sau:** cùng bộ đó được đưa vào session implement và cả cho verification agent — verification agent đọc chúng sẽ có context rộng hơn nhiều về yêu cầu
- **Tách theo stage giúp mỗi file nhỏ và dễ đọc:** giải quyết trực tiếp giới hạn ~100 dòng Markdown — nhiều file ngắn hơn một file dài
- **Phụ thuộc khả năng sinh artifact phong phú:** pattern này chỉ có giá trị khi agent xuất được HTML/SVG thay vì text — xem [[html-as-agent-output-format]]

## Related concepts

- [[html-as-agent-output-format]]
- [[plan-execute-verify-loop]]
- [[code-visualization]]
- [[context-window-management]]
- [[product-vs-prototype]]

## Sources

- [[src_unreasonable-effectiveness-of-html]] — Thariq Shihipar, Anthropic (2026-05-20)

## Notes
