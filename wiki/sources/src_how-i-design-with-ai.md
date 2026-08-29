---
type: source
original: "[[2026-08-28_how-i-design-with-ai]]"
main_tag: tech
sub_tags: [tools, vibecode, opinion]
topic: ai-design-workflow
date_compiled: 2026-08-29
url: https://ref.tools/blog/how-i-design-with-ai
author: Matt Dailey
---

# How I Design with AI

## Metadata

- **Author:** Matt Dailey (Founder & CEO Ref.)
- **Published:** [unknown]
- **Source:** ref.tools
- **URL:** https://ref.tools/blog/how-i-design-with-ai
- **Type:** Article

## Summary

Matt Dailey chia sẻ 7 nguyên tắc thiết kế sản phẩm khi dùng AI, từ góc nhìn của một engineer không phải designer nhưng ghét slop. Bài viết nhấn mạnh vấn đề cốt lõi: AI làm cho việc "design wackamole" (sửa từng phần nhỏ lẻ) trở nên quá dễ, dẫn đến sản phẩm rời rạc, thiếu cohesion. Giải pháp là quay lại design process có cấu trúc: xác định constraints trước, thiết kế tổng thể, và chỉ AI hỗ trợ trong khuôn khổ đó.

Các nguyên tắc bao gồm: luôn xem xét tổng thể (constraints → solutions → feedback loop), loại bỏ những thứ không cần thiết (agents thích thêm stuff), iterate trong design tool (không phải trong codebase để tránh prototype gravity), dùng components và preview deploys, "ăn cắp" solution từ product khác, và cuối cùng là explore taste của bản thân.

## Key points

- **Design process 3 bước (Christopher Alexander):** (1) lay out constraints, (2) consider solutions thỏa constraints, (3) nếu phát hiện constraint mới/cần bỏ → quay lại bước 1
- **AI làm trầm trọng "design wackamole":** prompting "Make X more prominent" dẫn đến patchwork disjoint, thiếu tổng thể
- **Giải pháp cho wackamole:** keep một document tracking papercuts và annoyances, xử lý đồng bộ một lần thay vì reactive từng cái
- **Agents thích add stuff:** UI thừa copy, lines, icons — hãy hỏi "Do I actually need that?" cho mọi element
- **Prototype gravity:** khi AI build version đầu trong codebase, có cảm giác dễ refine hơn là khám phá option khác — iterate trong design tool (Figma, Claude Design, HTML prototypes)
- **Components & preview deploys:** views và logic riêng, /showcase page để test UI component trước khi connect main app, preview deploy với real data
- **"Steal stuff":** hầu hết UX problems đã được giải — collect screenshots từ product khác, dùng làm context cho agent
- **Taste là reflection:** "throwing a design in the middle and beat it with sticks until we feel good about it" — cần reps trying things và reflecting
- **Product engineers thiếu solution library:** họ giỏi identify khi design không work nhưng thiếu experience để biết cách fix

## Concepts referenced

- [[codified-taste]]
- [[taste-judgment]]
- [[product-vs-prototype]]
- [[vibe-coding]]
- [[ai-productivity]]
- [[design-process]]

## Original excerpts

> "The design process is roughly 3 steps: (1) Lay out all the constraints you are designing for. (2) Consider an array of solutions that satisfy those constraints. (3) If you realize a constraint must be added or one can be removed, go to #1."

> "Prototype gravity is the silent killer. This is when you have the agent build the first version in your code base then it feels easier to just refine that instead of exploring other options."

> "At Ref we don't have a full-time designer so we resort to an agricultural threshing approach to refining our taste. We throw a design in the middle and beat it with sticks until we feel good about it."

> "Taste is reflecting on your own reaction to something. [...] It's necessary to create and not create slop."