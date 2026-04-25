---
type: source
source_url: https://github.com/refactoringhq/tolaria
date_ingested: 2026-04-24
tags: [#coding, #productivity]
---
# Tolaria — macOS App Quản Lý Markdown Knowledge Base

Một ứng dụng macOS mã nguồn mở để quản lý kho tri thức bằng Markdown.

## Key Points
- **Triết lý thiết kế**:
    - **Files-first**: Sử dụng tệp Markdown thuần túy, không định dạng độc quyền, dễ dàng di chuyển.
    - **Git-first**: Mỗi vault là một git repository, cung cấp lịch sử phiên bản đầy đủ.
    - **Offline-first**: Không tài khoản, không subscription, không phụ thuộc cloud.
    - **AI-first**: Tối ưu hóa ngữ cảnh để làm việc với các AI agents (Claude Code, Codex CLI).
    - **Keyboard-first**: Thiết kế tối ưu cho power users.
- **Khác biệt với Obsidian**: Tập trung tuyệt đối vào offline-first, quản lý phiên bản bằng Git và schema frontmatter nhất quán cho toàn bộ ghi chú.
- **Tech stack**: Tauri (Rust backend), React, TypeScript.
- **License**: AGPL-3.0.
