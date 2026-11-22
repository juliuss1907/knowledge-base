---
type: source
original: "[[2026-11-14_all-code-is-slop-except-mine]]"
main_tag: ai
sub_tags: [coding, automation, research]
topic: deterministic-agent-guardrails
date_compiled: 2026-11-21
url: https://youtu.be/O_zcc6Xl12g
author: AI Engineer
---

# All Code Is Slop (Except Mine) — Lauren Tan, SpaceXSI

## Metadata

- **Source type:** Video
- **Published:** 2026-11-14
- **Author:** AI Engineer
- **URL:** https://youtu.be/O_zcc6Xl12g

## Summary

Lauren Tan lập luận rằng năng suất agent chỉ bền vững khi chất lượng được xây bằng môi trường có thể kiểm chứng, thay vì tin mù quáng vào output. Kim tự tháp niềm tin bắt đầu bằng API, kiến trúc, type system, lint và test có tính deterministic; sau đó mới đến runtime và formal verification, rồi mới tới prose như rules hay skills. Các lỗi lặp lại nên được triệt tiêu bằng thiết kế hoặc ràng buộc máy có thể thực thi, không chỉ thêm comments. Với nền tảng này, nhóm Grok Bot báo cáo 11.000 PR trong một tháng, tỷ lệ revert khoảng 0,5% và hiệu năng sản phẩm vẫn cải thiện.

## Key points

- Codebase là input lớn của agent; technical debt và anti-pattern dễ bị agent sao chép hàng loạt.
- API rõ ràng, kiến trúc, type system, compiler, lint rules và test là các tầng kiểm soát deterministic ưu tiên cao.
- Có thể cấm hẳn các primitive thường bị lạm dụng, như `useEffect` trong product code, thay vì dựa vào review.
- Cấu trúc thư mục và dependency rules có thể ngăn import sai giữa Electron main và renderer.
- Comments dễ stale và không enforceable; lint với thông báo hướng tới root cause đáng tin cậy hơn.
- Runtime verification dùng feature map, CLI tái sử dụng và bằng chứng như video hoặc screenshot.
- Formal verification, TLA+ và Lean là lớp bổ sung để kiểm tra invariant và luồng quan trọng.
- Tự động hóa outer loop chỉ đáng tin khi codebase và verification loop đã đủ mạnh.

## Concepts referenced

- [[deterministic-agent-guardrails]]
- [[agentic-coding]]

