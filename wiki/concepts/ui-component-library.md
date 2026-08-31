---
type: concept
status: draft
main_tag: tech
sub_tags: [tools, coding]
topic: ui-component-library
sources:
  - "[[src_threeui]]"
last_updated: 2026-08-31
---

# UI Component Library

## Definition

UI component library là tập hợp các component giao diện dùng lại được, đóng gói dưới dạng thư viện cài qua package manager, giúp developer xây dựng UI nhanh và nhất quán. ThreeUI là một ví dụ tiêu biểu: thư viện React components với live interactive components, đầy đủ source, variants và controls, phân phối qua npm (`@designcodeio/threeui`) kèm shared styles. Mô hình Community/Pro split cho phép bản open-source miễn phí trong khi source nâng cao được bán qua CLI có xác thực.

## Key ideas

- **Community vs Pro split:** Bản open-source giữ toàn bộ free variants; Pro/Beta components bị loại khỏi catalog
- **Live interactive components:** Components render trực tiếp, có thể thao tác, không chỉ là static code
- **Subpath import:** Import component con (`@designcodeio/threeui/components/AtTheHorizon`) để tối giản dependency graph
- **Source distribution model:** Pro source không publish npm, cung cấp qua CLI với OAuth + PKCE và entitlement check mỗi request
- **Automated sync pipeline:** Private repo sync public subset sau mỗi push — fails closed, filter Pro/Beta, tự động version bump
- **Asset handling:** Components render full HTML documents cần runtime files ở root-relative URLs
- **Sponsorship-driven maintenance:** Mô hình tài trợ duy trì thư viện open-source

## Related concepts

- [[design-systems]]
- [[vibe-coding]]

## Sources

- [[src_threeui]]

## Notes