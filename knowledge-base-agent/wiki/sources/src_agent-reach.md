---
type: source
source_type: repo
source_url: https://github.com/juliuss1907/Agent-Reach
date_ingested: 2026-04-20
date_compiled: 2026-04-21
tags: [#ai, #llm, #coding]
status: active
---

# Agent Reach — Multi-Platform Data Ingestion cho AI Agents

## Tóm tắt

Agent Reach giúp AI agent đọc và search trên 17 nền tảng (Twitter, Reddit, YouTube, GitHub, B站, 小红书, 抖音...) chỉ qua một CLI, không tốn phí API.

## Problem It Solves

AI agents gặp khó khi tìm info online:
- YouTube: can't read subtitles
- Twitter: API is paid
- Reddit: 403 blocked
- 小红书: requires login

Agent Reach biến tất cả thành một câu lệnh cho agent xử lý.

## Supported Platforms

| Platform | Read | Search | Extra Config |
|---|---|---|---|
| Web (Jina Reader) | ✅ | — | None |
| YouTube | ✅ subtitles | ✅ | None |
| Twitter/X | ✅ single tweet | ✅ | Cookie |
| Reddit | ✅ | ✅ (Exa) | Proxy (server) |
| GitHub | ✅ public repos | ✅ | None |
| B站 | ✅ subtitles | ✅ | Proxy (server) |
| 小红书 | ✅ | ✅ | Cookie + Docker |
| 抖音 | ✅ | ✅ | No login needed |
| RSS | ✅ | — | None |
| 微信公众号 | ✅ | ✅ | None |
| 雪球 | ✅ | ✅ | None |
| LinkedIn | ✅ | ✅ | Cookie |
| V2EX | ✅ | ✅ | None |

## Tech Stack (Upstream Tools)

- Web: Jina Reader (free, no API key)
- Twitter: bird CLI (Cookie auth, free)
- Video subtitles: yt-dlp
- Search: Exa via MCP (AI semantic search, free)
- GitHub: gh CLI

## Key Features

- 100% free — chỉ ~$1/month cho proxy nếu chạy trên server
- Local-only cookies — không upload lên đâu
- `agent-reach doctor` check từng channel
- Compatible: Claude Code, OpenClaw, Cursor, Windsurf, Codex

## License

MIT

## Links

- GitHub: Agent-Reach
- Install: `pip install agent-reach`