---
type: raw
source_type: repo
source_url: https://github.com/juliuss1907/firecrawl
date_ingested: 2026-04-20
tags: []
status: unprocessed
---
# Firecrawl

Power AI agents with clean web data. The API to search, scrape, and interact with the web at scale. Open source and available as a hosted service at firecrawl.dev.

## Key Features

- **Industry-leading reliability**: Covers 96% of the web, including JS-heavy pages
- **Blazingly fast**: P95 latency of 3.4s across millions of pages
- **LLM-ready output**: Clean markdown, structured JSON, screenshots
- **We handle the hard stuff**: Rotating proxies, rate limits, JS-blocked content — zero configuration
- **Agent ready**: Connect to any AI agent or MCP client with a single command
- **Media parsing**: Parse PDFs, DOCX, and more
- **Actions**: Click, scroll, write, wait, and press before extracting content

## Core Endpoints

| Feature | Description |
|---|---|
| Search | Search the web and get full page content from results |
| Scrape | Convert any URL to markdown, HTML, screenshots, or structured JSON |
| Interact | Scrape a page, then interact with it using AI prompts or code |
| Agent | Automated data gathering — describe what you need |
| Crawl | Scrape all URLs of a website with a single request |
| Map | Discover all URLs on a website instantly |
| Batch Scrape | Scrape thousands of URLs asynchronously |

## SDKs

- Python: `pip install firecrawl-py`
- Node.js: `npm install @mendable/firecrawl-js`
- Java: Maven/Gradle
- Elixir: Mix
- Go, Rust

## AI Integration

- MCP server: `@mendable/firecrawl-mcp`
- Claude Code, OpenCode, antigravity compatible
- Single command init: `npx -y firecrawl-cli@latest init --all --browser`

## Agent Mode

Two models:

| Model | Cost | Best For |
|---|---|---|
| spark-1-mini (default) | 60% cheaper | Most tasks |
| spark-1-pro | Standard | Complex research, critical extraction |

## License

AGPL-3.0 (core), MIT (SDKs and some UI components)

## Links

- Docs: https://docs.firecrawl.dev
- API Reference: https://docs.firecrawl.dev/api-reference/introduction
- Playground: https://firecrawl.dev/playground
- Website: https://firecrawl.dev
