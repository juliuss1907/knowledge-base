---
type: concept
tags: [#ai, #llm, #coding]
status: draft
sources:
  - src_mcp-vs-skills
date_created: 2026-04-21
---

# MCP vs Skills

## Tóm tắt

MCP (Model Context Protocol) vẫn tốt hơn Skills cho việc kết nối dịch vụ. Skills phù hợp khi dạy kiến thức thuần túy.

## MCP là gì

MCP là một API abstraction — LLM chỉ cần biết "what", không cần biết "how". Muốn tương tác với DEVONthink? Gọi `devonthink.do_x()`, MCP server lo phần còn lại.

## Ưu điểm của MCP

- **Remote MCP server:** không cần cài đặt local, chỉ cần trỏ đến URL
- **Cập nhật tự động:** khi server cập nhật, mọi client đều được hưởng
- **Auth dễ hơn:** thường dùng OAuth
- **Portable:** dùng được từ Mac, điện thoại, web
- **Sandboxing:** remote MCP tự nhiên an toàn
- **Tiết kiệm context:** chỉ load tools thực sự cần

## Vấn đề với Skills

- **Giả định sai:** không phải môi trường nào cũng chạy được CLI
- **Quản lý phiên bản lộn xộn:** cập nhật phải cài lại
- **Secret management:** API tokens để đâu?
- **Context bloat:** phải load cả SKILL.md
- **Ecosystem phân mảnh:** Skill marketplace không thống nhất

## Khi nào nên dùng cái nào

- **MCP:** Cần kết nối LLM với một dịch vụ — Google Calendar, Chrome, Notion
- **Skills:** Dạy kiến thức thuần túy — cách dùng git, quy tắc team, cách xử lý file PDF

## Đề xuất đặt tên lại

- Skills → `LLM_MANUAL.md`
- MCP → `Connectors`

## Sản phẩm liên quan

- **microfn** — remote MCP tại mcp.microfn.dev
- **Kikuyo** — remote MCP tại mcp.kikuyo.app
- **MCP Nest** — tunnel local MCP ra cloud tại mcp.mcpnest.dev

## Source

https://david.coffee/i-still-prefer-mcp-over-skills/