---
type: concept
tags: [#ai, #coding]
status: draft
sources:
  - src_openclaw-studio
date_created: 2026-04-21
---

# OpenClaw Studio

## Tóm tắt

Studio là web UI để quản lý OpenClaw Gateway. Chạy trên Node.js (localhost:3000), kết nối đến Gateway qua WebSocket.

## Tính năng chính

- Kết nối Gateway từ xa qua Tailscale hoặc SSH tunnel
- Xem và quản lý agents
- Chat interface
- Quản lý exec approvals
- Cấu hình cron jobs
- Lưu settings trong `~/.openclaw/openclaw-studio/settings.json`

## Kiến trúc

- Browser → Studio: HTTP + SSE
- Studio → Gateway: WebSocket
- SQLite (`runtime.db`) lưu runtime history và replay

## 3 Scenario kết nối

| Scenario | Gateway | Studio |
|---|---|---|
| A | Local | Local (cùng máy) |
| B | Cloud | Local (laptop) |
| C | Cloud | Cloud |

## Cài đặt

```bash
npx -y openclaw-studio@latest
cd openclaw-studio
npm run dev
```

## Links

- GitHub: https://github.com/juliuss1907/openclaw-studio