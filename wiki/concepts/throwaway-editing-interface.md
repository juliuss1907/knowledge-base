---
type: concept
status: draft
main_tag: ai
sub_tags: [tools, coding]
topic: html-as-agent-output
sources:
  - "[[src_unreasonable-effectiveness-of-html]]"
last_updated: 2026-10-03
---

# Throwaway Editing Interface

## Definition

Throwaway editing interface là pattern nhờ agent build một giao diện chỉnh sửa dùng một lần, viết bằng một file HTML đơn lẻ, được thiết kế riêng cho đúng piece of data đang làm việc — không phải product, không phải tool tái sử dụng. Pattern này giải quyết trường hợp không mô tả được ý mình chỉ bằng text box, và luôn kết thúc bằng một nút export đưa thay đổi ngược lại thành prompt hoặc file.

## Key ideas

- **Điểm khởi động:** có những thứ "khó nói bằng text box" — cần xem nhiều option cạnh nhau thấy trade-off, cần kéo-thả xếp hạng, cần bật/tắt hàng loạt config
- **Ranh giới với sản phẩm:** một file HTML, purpose-built cho một mảnh data cụ thể, không phải reusable tool, không có người dùng ngoài tác giả
- **Luôn kết thúc bằng export:** "copy as JSON" hoặc "copy as prompt" để chuyển trạng thái UI thành thứ dán ngược vào Claude Code hoặc commit vào file — bỏ bước này thì vòng lặp bị đứt
- **Tinh thần "bạn vẫn ở trong loop, nhưng loop hẹp lại":** người dùng thao tác trực tiếp, agent không phải đoán ý từ mô tả chữ, và thay đổi quay lại được dưới dạng prompt
- **Bốn use case tiêu biểu:** reordering/triaging/bucketing (Linear tickets thành cột Now/Next/Later/Cut), chỉnh structured config (feature flags có dependency, cảnh báo khi bật flag mà prerequisite đang tắt), tuning prompt/template với live preview và token counter, curate dataset (approve/reject row, tag, export)
- **Kỹ thuật hay dùng:** sliders, knobs để tune animation hoặc thuật toán; collapsible sections, tabbed snippets, side-by-side editor để so sánh; nút copy cho tham số đã tìm được
- **Điểm khác biệt so với prototype:** không cần đẹp, cần chạy và export đúng; giá trị nằm ở vòng tương tác ngắn, không nằm ở sản phẩm cuối — xem [[product-vs-prototype]]
- **Phụ thuộc output format giàu tương tác:** chỉ khả thi khi agent xuất được HTML có JS/CSS thay vì text — xem [[html-as-agent-output-format]]

## Related concepts

- [[html-as-agent-output-format]]
- [[multi-file-artifact-workflow]]
- [[frontend-design-agent]]
- [[product-vs-prototype]]
- [[human-judgment-ai]]

## Sources

- [[src_unreasonable-effectiveness-of-html]] — Thariq Shihipar, Anthropic (2026-05-20)

## Notes
