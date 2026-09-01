---
type: source
original: "[[2026-08-30_MengTo_threeui]]"
main_tag: tech
sub_tags: [tools, coding]
topic: ui-component-library
date_compiled: 2026-08-31
url: https://github.com/MengTo/threeui
author: MengTo
---

# ThreeUI Community

## Metadata

- **Author:** MengTo
- **Published:** [unknown]
- **Source:** github.com
- **URL:** https://github.com/MengTo/threeui
- **Type:** repo

## Summary

ThreeUI Community là bản open-source, không cần login của ThreeUI — một thư viện UI components cho React với live interactive components và đầy đủ source. Catalog là điểm khác biệt duy nhất: các Pro và Beta components bị loại bỏ, còn mọi Community component giữ nguyên free variants và controls. Gói gồm 50 parent components, 111 routes, 141 free variant records cùng 23 singleton components. Nó hỗ trợ cài qua npm (`@designcodeio/threeui`), chạy local với `npm run dev`, và Pro source được cung cấp qua CLI riêng với OAuth + PKCE. Hệ thống synchronization tự động giữ repository public đồng bộ với main project.

## Key points

- **50 Community parent components + 111 routes:** 141 free variants + 23 singletons (164 browse results)
- **Không cần login:** Bản Community open-source, Pro/Beta components bị loại
- **Cài đặt npm:** `npm install @designcodeio/threeui`, import component + shared styles
- **Subpath import:** Import component con để tối giản dependency graph
- **Pro access qua CLI:** `npx @designcodeio/threeui-cli add <component>` — OAuth + PKCE, owner-only session, không overwrite file chưa cho phép
- **Synchronization tự động:** Private repo sync Community subset sau mỗi push, sync fails closed, filter Pro/Beta
- **Versioning:** New components/variants → minor release, removals → major, compatible source → patch
- **npm trusted publishing:** Merging versioned sync PR publish package với provenance
- **License:** Application + Community code MIT; open fonts SIL OFL 1.1; Three.js MIT

## Concepts referenced

- [[ui-component-library]]
- [[design-systems]]

## Original excerpts

> "The catalog is the only product-level difference: Pro and Beta components are removed. Every Community component keeps all of its free variants and controls."
