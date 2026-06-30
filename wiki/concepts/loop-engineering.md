---
type: concept
status: draft
main_tag: ai
sub_tags: [automation, coding]
topic: loop-engineering
sources:
  - "[[src_loop-engineering-14-step-roadmap]]"
last_updated: 2026-06-30
---

# Loop Engineering

## Definition

Loop engineering là phương pháp thiết kế hệ thống tự động (loop) thay thế con người trong vai trò prompter cho coding agent. Thay vì ngồi gõ prompt, đọc diff, gõ prompt tiếp theo, developer thiết kế một hệ thống tự động tìm việc, giao cho agent, kiểm tra kết quả, ghi lại trạng thái và quyết định bước tiếp theo — tất cả tự động. Leverage point chuyển từ "viết prompt hay" sang "thiết kế loop hay."

## Key ideas

- Loop gồm 6 thành phần theo Addy Osmani: Automations (heartbeat), Worktrees (parallel không conflict), Skills (context viết một lần), Connectors (MCP kết nối tool thật), Sub-agents (tách maker khỏi checker), State files (agent quên, file không)
- 4 điều kiện tiên quyết để loop có lợi: task lặp lại, verification tự động, token budget đủ, agent có môi trường chạy code
- Minimum viable loop: 1 automation + 1 skill + 1 state file + 1 gate — manual reliable trước khi wrap vào loop
- Metric quan trọng nhất: cost per accepted change, không phải tokens spent hay tasks attempted
- Anthropic engineers merge code gấp 8 lần so với 2024 nhờ loop engineering
- Loop phù hợp cho CI failure triage, dependency bumps, lint-and-fix; không phù hợp cho architecture, auth, payments, production deploys
- Công cụ chính: Codex (Automations tab) và Claude Code (`/loop`, `/goal`, Routines)

## Related concepts

- [[ralph-wiggum-loop]]
- [[comprehension-debt]]
- [[cognitive-surrender]]

## Sources

- "[[src_loop-engineering-14-step-roadmap]]"

## Notes
