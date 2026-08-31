---
type: concept
status: draft
main_tag: tech
sub_tags: [tools, coding]
topic: design-systems
sources:
  - "[[src_threeui]]"
last_updated: 2026-08-31
---

# Design Systems

## Definition

Design system là bộ quy chuẩn thống nhất về components, tokens, patterns và guidelines giúp xây dựng sản phẩm nhất quán và có thể scale. ThreeUI thể hiện mô hình design system hiện đại: thư viện components tái sử dụng với live renderers, variant picker, themes và responsive behavior đóng gói trong một gói npm. Design system hiệu quả không chỉ là style guide mà là hệ thống có thể code được, version được và tự động hóa được — từ sync pipeline đến trusted publishing.

## Key ideas

- **Components tái sử dụng + variants:** Cùng một component có nhiều variants và controls để linh hoạt
- **Theme và responsive:** Hỗ trợ themes và responsive behavior trong cùng application shell
- **Live renderers:** Preview component trực tiếp, không chỉ xem code
- **Tự động hóa lifecycle:** Sync pipeline, version bump tự động (minor/major/patch), trusted publishing
- **Source control:** Phân quyền access (Community free vs Pro có xác thực)
- **Sharing design tokens:** `extract` reusable components và tokens vào design system

## Related concepts

- [[ui-component-library]]
- [[design-process]]

## Sources

- [[src_threeui]]

## Notes