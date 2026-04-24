---
type: raw
source_type: repo
source_url: https://github.com/refactoringhq/tolaria
date_ingested: 2026-04-24
tags: [#coding, #productivity]
status: unprocessed
---
# Tolaria — macOS App Quản Lý Markdown Knowledge Base

## Tóm tắt

Tolaria là open-source macOS app để quản lý large Markdown knowledge base, được tạo bởi tác giả refactoring.fm newsletter (Luca). Tác giả có workspace 10,000+ notes qua 6 năm.

## Tính năng chính

- **Files-first** — Plain markdown files, portable, không proprietary format
- **Git-first** — Mỗi vault là git repository, full version history
- **Offline-first** — Không accounts, không subscriptions, không cloud dependencies
- **AI-first but not AI-only** — Hỗ trợ Claude Code và Codex CLI, edit vault với bất kỳ AI nào
- **Keyboard-first** — Thiết kế cho power users
- **Types as lenses** — Types là navigation aids, không phải enforcement mechanisms

## So sánh với Obsidian

Tolaria khác Obsidian ở:
- Offline-first architecture (Obsidian có sync paid)
- Git-versioned plain Markdown files
- AI-context optimization cho agents
- Consistent frontmatter schema cho tất cả notes

## Tech stack

- Tauri (Rust backend)
- React
- TypeScript
- AGPL-3.0 license

## Yêu cầu development

- Node.js 20+
- pnpm 8+
- Rust stable
- macOS

```bash
pnpm install
pnpm dev  # browser-based mock mode
pnpm tauri dev  # native desktop app
```

## Lưu ý

- Tác giả dùng cho "personal vault of 10,000+ notes, use every day"
- Có getting started vault để clone
- Loom walkthroughs available trên GitHub