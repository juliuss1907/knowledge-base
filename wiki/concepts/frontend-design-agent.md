---
type: concept
status: draft
main_tag: tech
sub_tags: [tools, coding, vibecode]
topic: ai-frontend-design-guidance
sources:
  - "[[src_impeccable]]"
  - "[[src_unreasonable-effectiveness-of-html]]"
last_updated: 2026-10-03
---

# Frontend Design Agent

## Definition

Frontend design agent là pattern dùng AI coding agent làm công cụ thiết kế frontend — agent viết code, tạo components, và iterate dựa trên design feedback. Impeccable mở rộng pattern này từ frontend-design skill ban đầu của Anthropic thành hệ thống hoàn chỉnh: 23 commands cho từ vựng thiết kế, 59 quy tắc phát hiện tất định, vòng lặp trình duyệt trực tiếp, và thiết lập ngữ cảnh giúp agent biết khách hàng, thương hiệu, giọng điệu. Khác với vibe coding thuần túy, frontend design agent có từ vựng thiết kế để phê bình, rà soát và hoàn thiện một cách có chủ đích.

## Key ideas

- **Từ frontend-design skill đến Impeccable:** Anthropic's frontend-design là skill đầu tiên, Impeccable mở rộng thành hệ thống đầy đủ
- **Design commands:** critique (UX review), audit (technical checks), polish (final pass), distill (strip to essence), bolder/quieter
- **Deterministic + LLM rules:** 59 rules chạy không cần LLM cho technical checks, LLM-only critique cho UX
- **Live browser mode:** Visual variant iteration không cần reload
- **Anti-patterns:** Explicit guidance chống design tells phổ biến của AI-generated frontend
- **Context system:** PRODUCT.md + DESIGN.md giúp agent hiểu brand, audience, voice, colors
- **HTML là canvas tự nhiên cho design exploration:** Claude Design bản chất dựa trên HTML vì HTML biểu diễn design rất giàu sức tải, kể cả khi sản phẩm cuối không phải HTML — Claude phác thảo design bằng HTML rồi viết ra React, Swift hay ngôn ngữ khác
- **Prototype interaction bằng tham số thay vì bằng lời:** slider, knob để tune animation hoặc component, kèm nút copy tham số đã chọn — nhanh hơn mô tả bằng text, xem [[throwaway-editing-interface]]
- **Artifact làm design system reference:** design token và component được render đúng như chúng sẽ xuất hiện thật, thay vì mô tả bằng code block

## Related concepts

- [[ai-frontend-design-guidance]]
- [[design-systems]]
- [[vibe-coding]]
- [[html-as-agent-output-format]]
- [[throwaway-editing-interface]]

## Sources

- [[src_impeccable]]
- [[src_unreasonable-effectiveness-of-html]] — Thariq Shihipar, Anthropic (2026-05-20)

## Notes
