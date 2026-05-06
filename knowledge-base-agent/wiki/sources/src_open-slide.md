---
type: source
source_url: https://github.com/juliuss1907/open-slide
date_ingested: 2026-05-05
tags: [#ai, #coding]
status: processed
---

# Open Slide — A Slide Framework Built for Agents

Owner: juliuss1907 (Julius)
Repo: open-slide
Link: https://github.com/juliuss1907/open-slide

## Ghi chú chính
- **Mục đích**: Một slide framework được thiết kế đặc biệt để các AI Agent có thể tạo ra bài thuyết trình (presentation).
- **Đặc điểm Agent-native**:
    - Tích hợp sẵn hệ thống skills cho agent (trong `.agents/skills/` và `.claude/skills/`).
    - Sử dụng file `AGENTS.md` làm chuẩn chung cho nhiều agent khác nhau thay vì chỉ dành riêng cho Claude.
- **Kiến trúc**:
    - Monorepo sử dụng Turborepo và pnpm workspace.
    - Cung cấp CLI tool (`openslide`) để scaffold workspace từ template.
- **Tech Stack**: TypeScript, pnpm, Turborepo, Changesets.
- **Điểm nổi bật**: Cho phép agent tự động xây dựng cấu trúc slide thông qua các skills modular và theme tùy chỉnh.
