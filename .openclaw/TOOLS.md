# TOOLS.md — OpenClaw Environment Notes

> Những thứ đặc thù cho setup này — không share được.

---

## API Routing

| Task | Model | Provider |
|------|-------|----------|
| Complex operations, Compile | MiniMax | MiniMax API |
| Light tasks, Heartbeat | OpenRouter | Free models |
| Never use in automation | Z.ai | Julius only |

---

## External Integrations

### Telegram
- **Channel:** Primary input for links/files
- **Notification:** Sent after Hermes review

### Readwise
- **Sync time:** Daily 07:00
- **Output:** `raw/articles/`

---

## Workspace Paths

| Purpose | Path |
|---------|------|
| Root workspace | `/home/julius/knowledge-base/` |
| Agent config | `.openclaw/` |
| Raw sources | `raw/{repos,articles,papers,posts,videos,websites}/` |
| Compiled wiki | `wiki/{sources,concepts,tag,topic}/` |
| Reviews | `wiki/reviews/` |
| Hermes config | `.hermes/` (read-only for OpenClaw) |

---

## Environment

- **Host:** julius-vps
- **OS:** Linux 6.14.0-37-generic (x64)
- **Node:** v24.14.1
- **Shell:** bash

---

## Notes

- 

---

*Last updated by: OpenClaw*  
*Update rule: Append-only*