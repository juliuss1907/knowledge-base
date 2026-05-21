---
type: concept
status: draft
main_tag: ai
sub_tags: [tools, automation, vibecode]
topic: hermes-polymarket-trading-agent
sources:
  - [[wiki/sources/src_hermes-polymarket-btc-trading-agent.md]]
last_updated: 2026-05-21
---

# Hermes Agent

## Definition

Hermes Agent là framework AI agent tự học mã nguồn mở được phát triển bởi NousResearch, đạt hơn 100,000 GitHub stars trong chưa đầy 2 tháng (vượt qua Claude Code vào 27/04/2026). Đây là autonomous agent với built-in self-learning loop giúp agent càng chạy càng thông minh.

## Key ideas

- **Phát triển bởi:** NousResearch (AI research lab được Paradigm đầu tư $70M), creators của Nomos & Psyche
- **Ra mắt:** 25/02/2026
- **Kiến trúc 3 lớp:**
  - Knowledge Layer: Built-in memory, session search, LLM-Wiki skill, optional Honcho integration
  - Execution Layer: Multi-agent profiles, child agents, tool system, MCP support, persistent machine access
  - Output Layer: Cron jobs, gateway delivery (Telegram/Slack/Discord), Web UI, file output
- **Self-learning loop:** Agent tự động cải thiện từ live trades thay vì chỉ follow hard-coded instructions
- **Có thể chạy qua:** Atomic (native macOS AI assistant) hoặc cloud
- **Hỗ trợ models:** Local (Gemma, Qwen, GLM) miễn phí hoặc paid APIs (Claude, OpenAI Codex, Gemini)
- Khác với ChatGPT hay browser tab — Hermes có "tay, mắt, bộ nhớ, và workspace thực"

## Related concepts

- [[atomic-mac-agent]]
- [[self-learning-agents]]
- [[mcp-model-context-protocol]]

## Sources

- [[wiki/sources/src_hermes-polymarket-btc-trading-agent.md]]

## Notes