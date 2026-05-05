---
type: raw
source_type: repo
source_url: https://github.com/CJackHwang/ds2api
date_ingested: 2026-05-05
tags: [#coding, #ai]
status: unprocessed
---

# DS2API — DeepSeek-Compatible Middleware Interface

**Owner:** CJackHwang  
**Repo:** ds2api  
**Link:** https://github.com/CJackHwang/ds2api

---

## Tóm tắt

DS2API là **middleware** chuyển đổi DeepSeek Web dialogue capability thành API compatible vớI **OpenAI, Claude và Gemini**.

**Stack:**
- **Backend:** Go (high-concurrency, không cần Python runtime)
- **Frontend:** React WebUI (trong `webui/`, auto-build vào `static/admin`)
- **Vercel bridge:** Node Runtime cho streaming (ít dùng)

---

## Core Capabilities

| Tính năng | Mô tả |
|---|---|
| **OpenAI compatible** | `/v1/models`, `/v1/chat/completions`, `/v1/responses`, `/v1/embeddings`, `/v1/files` |
| **Claude compatible** | `/anthropic/v1/messages`, `/v1/messages` |
| **Gemini compatible** | `/v1beta/models/{model}:generateContent`, `:streamGenerateContent` |
| **Multi-account rotation** | Auto token refresh, email/phone login |
| **Concurrency control** | Per-account in-flight limit + queue |
| **DeepSeek PoW** | Pure Go implementation (DeepSeekHashV1), millisecond response |
| **Tool Calling** | Anti-leak, DSML format, canonical XML support |
| **Admin API** | Config management, hot reload, account testing |
| **WebUI** | `/admin` SPA (Chinese/English, dark mode) |

---

## Model Support

**OpenAI interface:**
- `deepseek-v4-flash` / `-nothinking`
- `deepseek-v4-pro` / `-nothinking`
- `deepseek-v4-flash-search` / `-nothinking`
- `deepseek-v4-pro-search` / `-nothinking`
- `deepseek-v4-vision` / `-nothinking`

→ Cũng support alias: `gpt-4.1`, `gpt-5`, `o3`, `claude-*`, `gemini-*`

**Claude interface mapping:**
- `claude-sonnet-4-6` → `deepseek-v4-flash`
- `claude-opus-4-6` → `deepseek-v4-pro`

---

## Deployment Options

1. **Download Release** — Pre-built binaries (khuyến nghị)
2. **Docker** — `docker-compose up -d`
3. **Vercel** — Serverless deployment
4. **Local source** — `go run ./cmd/ds2api`

---

## Platform Compatibility

| Level | Platform | Status |
|---|---|---|
| P0 | Codex CLI/SDK | ✅ |
| P0 | OpenAI SDK (JS/Python) | ✅ |
| P0 | Vercel AI SDK | ✅ |
| P0 | Anthropic SDK | ✅ |
| P0 | Google Gemini SDK | ✅ |
| P1 | LangChain / LlamaIndex / OpenWebUI | ✅ |

---

## Key Metrics

- **Mind2Web accuracy:** 89.9%
- **Browser cold start:** <250ms
- **Anti-bot pass rate:** 85%
- **Detection coverage:** 99.3%
