---
type: raw
source_type: repo
source_url: https://github.com/juliuss1907/Agent-Reach
date_ingested: 2026-04-20
tags: []
status: processed
processed_date: 2026-04-21
---
# Agent Reach

Give your AI agent eyes to see the entire internet. Read & search Twitter, Reddit, YouTube, GitHub, Bilibili, XiaoHongShu — one CLI, zero API fees.

## Problem It Solves

AI agents can code, edit docs, manage projects — but when asked to find info online, they hit walls:
- YouTube: can't read subtitles
- Twitter: API is paid
- Reddit: 403 blocked
- 小红书: requires login
- B站: blocked overseas

Each platform has its own hurdles — paid APIs, blocks, logins, data cleaning. Agent Reach turns this into one sentence for the agent to handle.

## How It Works

Install once: `agent-reach install` → Agent auto-installs CLI tools + config
Then Agent calls upstream tools directly (yt-dlp, bird, gh CLI...) — no wrapper layer
Each channel is a single file, swappable

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

- **Web**: Jina Reader (9.8K stars, free, no API key)
- **Twitter**: bird CLI (Cookie auth, free)
- **Video subtitles**: yt-dlp (148K stars)
- **Search**: Exa via MCP (AI semantic search, free, no key)
- **GitHub**: gh CLI (official tool)
- **RSS**: feedparser
- **小红书**: xiaohongshu-mcp (Docker, 9K+ stars)
- **抖音**: douyin-mcp-server (MCP, no login)
- **LinkedIn**: linkedin-scraper-mcp

## Key Features

- **100% free** — only ~$1/month for proxy if running on server
- **Local-only cookies** — stored in `~/.agent-reach/config.yaml`, never uploaded
- **agent-reach doctor** — check each channel status
- **安全模式** — only lists what needs installing, doesn't auto-install
- **Compatible**: Claude Code, OpenClaw, Cursor, Windsurf, Codex

## Installation

```bash
pip install agent-reach
agent-reach install --env=auto
```

OpenClaw users: enable exec first:
```bash
openclaw config set tools.profile "coding"
```

## Architecture

Agent Reach is a scaffolding tool, not a framework.
Each `channels/` file only checks if upstream tool is available (check() method).
Actual read/search done by Agent calling upstream tools directly.

## License

MIT
