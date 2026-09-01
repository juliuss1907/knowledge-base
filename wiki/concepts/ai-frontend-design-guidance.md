---
type: concept
status: draft
main_tag: tech
sub_tags: [tools, coding, vibecode]
topic: ai-frontend-design-guidance
sources:
  - "[[src_impeccable]]"
last_updated: 2026-08-31
---

# AI Frontend Design Guidance

## Definition

AI frontend design guidance là bộ công cụ và quy tắc giúp AI coding agents tạo ra thiết kế frontend chất lượng, nhất quán, tránh các "design tells" phổ biến khi mọi model trained trên cùng SaaS templates. Impeccable tiêu biểu cho xu hướng này: cung cấp design vocabulary chung (23 commands) giữa developer và AI, context setup (PRODUCT.md, DESIGN.md) và 59 deterministic detector rules chạy không cần LLM. Mục tiêu là biến AI-generated frontend từ "cùng một handful tells" thành thiết kế có cá tính và có chủ đích.

## Key ideas

- **Design vocabulary chung:** 23 commands (polish, audit, critique, distill, animate, bolder, quieter...) tạo ngôn ngữ chung với AI
- **Context-driven:** `/impeccable init` ghi PRODUCT.md + DESIGN.md — mọi command đọc context về audience, brand, voice, colors, type
- **Deterministic rules:** 59 detector rules chạy không cần LLM/API key — kiểm tra a11y, performance, responsive
- **Anti-patterns rõ ràng:** Chống Inter-for-everything, gradient tím-xanh, cards lồng cards, gray text, bounce easing
- **Live iteration:** `/impeccable live` visual variant mode iterate trong browser
- **Command composition:** craft = full shape-then-build flow; kết hợp audit/polish/critique cho từng giai đoạn
- **Shortcut pinning:** `/impeccable pin audit` tạo `/audit` standalone

## Related concepts

- [[frontend-design-agent]]
- [[design-systems]]
- [[vibe-coding]]
- [[ai-assisted-development]]

## Sources

- [[src_impeccable]]
