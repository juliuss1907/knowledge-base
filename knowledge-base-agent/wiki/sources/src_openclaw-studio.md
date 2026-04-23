---
type: source
source_type: repo
source_url: https://github.com/juliuss1907/openclaw-studio
date_ingested: 2026-04-20
date_compiled: 2026-04-21
tags: [#ai, #coding, #research]
status: active
---

# OpenClaw Studio — Web Dashboard for OpenClaw

## Tóm tắt

Studio là web UI chạy trên Node.js (localhost:3000), kết nối đến OpenClaw Gateway qua WebSocket. Giúp quản lý Gateway, agents, chat, approvals và jobs từ một giao diện duy nhất.

## Tính năng

- Kết nối Gateway từ xa qua Tailscale hoặc SSH tunnel
- Xem và quản lý agents
- Chat interface
- Quản lý exec approvals
- Cấu hình cron jobs
- Lưu settings trong `~/.openclaw/openclaw-studio/settings.json`

## Cách cài đặt

```bash
npx -y openclaw-studio@latest
cd openclaw-studio
npm run dev
# Mở http://localhost:3000
```

## 3 Scenario kết nối

| Scenario | Gateway | Studio |
|---|---|---|
| A | Local | Local (cùng máy) |
| B | Cloud | Local (laptop) |
| C | Cloud | Cloud |

## Kiến trúc

- Browser → Studio: HTTP + SSE
- Studio → Gateway: WebSocket
- SQLite (`runtime.db`) lưu runtime history và replay

## Links

- Docs: docs/ui-guide.md, docs/pi-chat-streaming.md, docs/permissions-sandboxing.md
- Settings: ~/.openclaw/openclaw-studio/settings.json
- Runtime DB: ~/.openclaw/openclaw-studio/runtime.db