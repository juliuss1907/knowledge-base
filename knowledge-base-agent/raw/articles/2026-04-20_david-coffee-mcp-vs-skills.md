---
type: raw
source_type: article
source_url: https://david.coffee/i-still-prefer-mcp-over-skills/
date_ingested: 2026-04-20
tags: [#ai, #llm, #coding]
status: unprocessed
---
# I Still Prefer MCP Over Skills

## Tóm tắt

Tác giả là người dùng AI nặng (Claude Code, Codex, Gemini, ChatGPT, Claude, Perplexity). Anh không thích cách giới AI đang đẩy "Skills là tiêu chuẩn mới" và cho rằng MCP vẫn tốt hơn cho việc kết nối dịch vụ.

## MCP là gì

MCP là một API abstraction — LLM không cần hiểu "how", chỉ cần biết "what". Muốn tương tác với DEVONthink? Gọi `devonthink.do_x()`, MCP server lo phần còn lại.

## Ưu điểm của MCP

- **Dùng remote MCP server:** không cần cài đặt local, chỉ cần trỏ đến URL là chạy
- **Cập nhật tự động:** khi server cập nhật tính năng mới, mọi client đều được hưởng ngay
- **Auth dễ hơn:** thường dùng OAuth, không cần quản lý token thủ công
- **Portable:** dùng được từ Mac, điện thoại, web
- **Sandboxing:** remote MCP tự nhiên an toàn, không trao quyền thực thi trực tiếp cho LLM
- **Tiết kiệm context:** client chỉ load tools thực sự cần dùng

## Vấn đề với Skills

Skills thực sự tốt khi chỉ dạy kiến thức thuần túy. Nhưng bắt đầu phiền khi Skills yêu cầu cài CLI.

**Các vấn đề chính:**

- **Giả định sai:** Không phải môi trường nào cũng chạy được CLI — ChatGPT, Perplexity, Claude web không hỗ trợ
- **Quản lý phiên bản lộn xộn:** Cập nhật skill phải cài lại, mỗi tool quản lý khác nhau
- **Secret management:** API tokens để đâu? File .env? Môi trường ephemeral thì tokens biến mất
- **Context bloat:** Phải load cả SKILL.md vào context thay vì chỉ cần signature của function
- **Ecosystem phân mảnh:** Skill marketplace không thống nhất

## Khi nào nên dùng cái nào

**Dùng MCP khi:** Cần kết nối LLM với một dịch vụ — Google Calendar, Chrome, Notion. Dịch vụ đó nên tự expose MCP endpoint.

**Dùng Skills khi:** Dạy kiến thức thuần túy — cách dùng git, cách đặt tên commit, quy tắc riêng của team, cách xử lý file PDF.

## Ý tưởng hay từ bài viết

Tác giả gợi ý đặt tên lại:
- Skills → `LLM_MANUAL.md`
- MCP → `Connectors`

Pattern hay: sau khi khám phá một MCP server và phát hiện gotchas (ví dụ date format phải YYYY-MM-DD), nhờ Claude viết Skills để ghi lại. Skills đóng vai trò "cheat sheet" cho MCP, không phải thay thế nó.

## Sản phẩm tác giả tự làm

- **microfn** — remote MCP tại mcp.microfn.dev
- **Kikuyo** — remote MCP tại mcp.kikuyo.app
- **MCP Nest** — tunnel local MCP ra cloud để truy cập từ xa tại mcp.mcpnest.dev
