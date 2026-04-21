---
type: source
source_type: repo
source_url: https://github.com/juliuss1907/firecrawl
date_ingested: 2026-04-20
date_compiled: 2026-04-21
tags: [#ai, #coding, #web3]
status: active
---

# Firecrawl — AI Web Scraping API

## Tóm tắt

Firecrawl là API để scrape và tương tác với web ở scale. Mã nguồn mở, có hosted service tại firecrawl.dev. Đặc biệt phù hợp cho AI agents vì output ra clean markdown, structured JSON.

## Tính năng chính

- **Độ tin cậy cao:** Cover 96% web, kể cả JS-heavy pages
- **Nhanh:** P95 latency 3.4s
- **LLM-ready output:** Clean markdown, structured JSON, screenshots
- **Agent ready:** Kết nối với bất kỳ AI agent nào qua MCP server
- **Media parsing:** PDF, DOCX
- **Actions:** Click, scroll, write, wait, press trước khi extract

## Core Endpoints

| Feature | Description |
|---|---|
| Search | Search web + lấy full page content |
| Scrape | Convert URL sang markdown, HTML, screenshots, JSON |
| Interact | Scrape rồi tương tác với AI prompts |
| Agent | Automated data gathering |
| Crawl | Scrape tất cả URLs của một website |
| Map | Discover tất cả URLs |
| Batch Scrape | Scrape hàng nghìn URLs async |

## SDKs

Python, Node.js, Java, Elixir, Go, Rust.

## License

AGPL-3.0 (core), MIT (SDKs và một số UI components)

## Links

- Docs: https://docs.firecrawl.dev
- Website: https://firecrawl.dev