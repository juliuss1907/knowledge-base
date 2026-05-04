---
type: concept
status: draft
tags: [#ai, #productivity]
updated: 2026-05-04
---

# Tối ưu hóa Claude (Claude Optimization)

## Mô tả
Hệ thống tối ưu hóa việc sử dụng Claude AI để tăng hiệu suất làm việc, từ thiết lập môi trường, quản lý ngữ cảnh (context), cho đến kỹ thuật prompt và quản lý tài nguyên (token).

### 1. Thiết lập môi trường & Ngữ cảnh (Setup & Context)
- **Công cụ hỗ trợ:** Sử dụng desktop app, kết hợp Wispr Flow.ai cho voice input và Obsidian để quản lý folder Cowork.
- **Cấu trúc Folder Cowork:**
    - `ABOUT ME`: Lưu thông tin cá nhân, style viết bài (anti-AI style) để Claude hiểu user.
    - `OUTPUTS`: Lưu kết quả đầu ra.
    - `TEMPLATES`: Lưu các mẫu output chuẩn (gold-standard).
- **Global Instructions:** Thiết lập hướng dẫn chung trong Settings để áp dụng cho mọi chat.

### 2. Kỹ thuật Prompting hiệu quả
- **Định nghĩa thành công:** Bắt đầu prompt bằng mục tiêu cụ thể và tiêu chí đánh giá thành công.
- **Tương tác hai chiều:** Sử dụng câu lệnh `use AskUserQuestion before you start` để AI làm rõ yêu cầu trước khi thực hiện.
- **Ví dụ mẫu:** Cung cấp ví dụ về output mong muốn thay vì chỉ mô tả bằng lời.
- **Quản lý luồng:** Nhóm các task liên quan vào một message, sửa message cũ thay vì gửi follow-up liên tục, và mở chat mới khi thay đổi chủ đề.

### 3. Quản lý Skills & Projects
- **Skills:** Xây dựng các skill tùy chỉnh, test với nhiều cách diễn đạt khác nhau và lưu vào Capabilities.
- **Projects:** Tạo project riêng cho mỗi loại đầu ra định kỳ, upload ví dụ mẫu chuẩn và thiết lập các tác vụ định kỳ (scheduled tasks).

### 4. Lập trình & Thiết kế (Design & Code)
- **Vibe Coding:** Sử dụng Claude Code cho website, kết nối GitHub cho live deployment, và duy trì file `CLAUDE.md` trong mọi project code để lưu context.
- **Design:** Sử dụng `claude.ai/design` kết hợp với brand file (`DESIGN.md`).

### 5. Nghiên cứu & Tiết kiệm Token (Research & Token Economy)
- **Nghiên cứu sâu:** Sử dụng Research mode, yêu cầu thực hiện nhiều search đa dạng để tìm khoảng trống thông tin (gaps) và gắn cờ các nguồn mâu thuẫn.
- **Tối ưu Token:** 
    - Chuyển PDF/ảnh sang Markdown trước khi upload.
    - Reset hội thoại sau mỗi ~20 messages.
    - Sử dụng Sonnet cho các tác vụ ngắn/đơn giản thay vì Opus.

## Liên quan
- [[AI-Workflow-Automation]] — Tối ưu hóa Claude là một phần của tự động hóa quy trình làm việc AI.
- [[mcp-vs-skills]] — Sự khác biệt giữa MCP và các skills tùy chỉnh trong Claude.
- [[tokenmaxxing]] — Kỹ thuật tối ưu hóa sử dụng token.

## Nguồn tham khảo
- [[src_claude-checklist-ruben-hassid]] — Claude Checklist by Ruben Hassid.
