---
type: source
original: "[[2026-09-19_ai-ui-design-8-ways-vibe-coded-apps]]"
main_tag: tech
sub_tags: [vibecode, tutorial]
topic: ai-ui-design
date_compiled: 2026-09-20
url: https://aistudio.google.com/learn/ai-ui-design-google-ai-studio
author: Geneviève Huskens
---

# AI UI design: 8 ways to make vibe-coded apps look better

## Metadata

- **Source type:** Article
- **Published:** 2026-09-16
- **Author:** Geneviève Huskens — Staff Developer Relations Engineer
- **Platform:** Google AI Studio Blog
- **URL:** https://aistudio.google.com/learn/ai-ui-design-google-ai-studio

## Summary

Bài viết hướng dẫn 8 cách cụ thể để cải thiện giao diện của các ứng dụng vibe-coded trong Google AI Studio. Tác giả nhấn mạnh rằng việc tạo app hoạt động đúng dễ hơn nhiều so với việc tạo app trông đẹp — và AI models khi để tự do thường tạo ra giao diện generic, cliché, hoặc cluttered.

8 tips bao gồm: dùng screenshot tham khảo để hướng dẫn aesthetic, generate ảnh UI cohesive với Nano Banana, retouch/restyle ảnh bằng Edit tool, test-drive typography qua Google Fonts, tạo Design Variations toàn bộ, inspect trực tiếp elements để tinh chỉnh pixel-perfect, dùng Annotate mode để dọn UI clutter, và remix apps từ Gallery. Mỗi tip đi kèm prompt ví dụ cụ thể có thể dùng ngay.

## Key points

- Upload reference screenshots để Gemini phân tích layout, color palette, spacing patterns — models mới (Gemini 3.8 Flash, 3.7 Flash) đặc biệt giỏi tái tạo UI từ screenshots
- Dùng prompt template trong AI Studio Playground để extract design language từ screenshots trước khi dùng trong Build
- `generate_image` tool trong Build cho phép tạo custom images trực tiếp — cần paid API key cho image generation
- Edit tool cho phép 3 option với images: generate edits với Nano Banana, tạo image mới hoàn toàn, hoặc upload từ device
- Google Fonts integration cho phép preview live typefaces (Space Grotesk, Playfair Display, DM Sans...) trước khi commit
- Design Variations tạo complete HTML/CSS redesigns giữ nguyên text, forms, interactive logic — có thể guide với custom prompt
- Direct element inspection cho phép tinh chỉnh padding, margins, dimensions, hex colors pixel-perfect
- Annotate mode: draw circles quanh elements cần xóa → prompt "Remove all circled elements" → Gemini đọc visual markup và strip clutter
- Remix từ AI Studio App Gallery: inspect prompts + UI components có sẵn, rồi customize

## Concepts referenced

- [[ai-frontend-design-guidance]]
- [[vibe-coding]]
- [[google-ai-studio]]
