---
type: concept
status: draft
main_tag: tech
sub_tags: [tools, vibecode]
topic: ai-ui-design
sources:
  - "[[src_ai-ui-design-8-ways-vibe-coded-apps]]"
last_updated: 2026-09-20
---

# Google AI Studio

## Definition

Google AI Studio là nền tảng IDE của Google cho phép developers build, test và deploy AI-powered web apps. Nền tảng tích hợp các tool visual như Edit tool, Design Variations, và Annotate mode cho phép người dùng tương tác trực tiếp với giao diện mà không cần sửa code thủ công.

## Key ideas

- **AI Studio Build:** Chế độ chính để tạo web apps — tích hợp Gemini models, `generate_image` tool (Nano Banana), và visual editing
- **Edit tool:** Click trực tiếp lên DOM elements để tinh chỉnh padding, margins, dimensions, hex colors — pixel-perfect adjustments
- **Design Variations:** Tạo complete HTML/CSS redesigns giữ nguyên content và interactive logic — có thể guide bằng custom prompts
- **Annotate mode:** Draw circles quanh elements cần xóa/sửa — Gemini đọc visual markup kết hợp code để thực hiện thay đổi
- **Google Fonts integration:** Preview live typefaces trực tiếp trên canvas trước khi commit
- **Nano Banana:** Image generation engine tích hợp sẵn — tạo custom images, retouch, restyle ngay trong Build mode
- **AI Studio Gallery:** App gallery với các featured apps có thể remix — inspect prompts + UI components rồi customize
- **Reference screenshot analysis:** Upload screenshots → Gemini extract design language (color palette, typography, spacing) thành prompt sử dụng được

## Related concepts

- [[ai-frontend-design-guidance]]
- [[vibe-coding]]

## Sources

- [[src_ai-ui-design-8-ways-vibe-coded-apps]]
