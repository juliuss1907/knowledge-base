---
type: concept
status: reviewed
main_tag: ai
sub_tags: [automation, tools, opinion]
topic: ai-trading-agent-claude-code
sources:
  - "[[src_build-ai-trading-agent-claude-code-alpaca]]"
last_updated: 2026-05-28
---

# AI Trading Agent

## Definition

Agent tự động giao dịch tài chính sử dụng LLM (như Claude) để research thị trường, đưa ra quyết định mua/bán/bán, và thực thi lệnh qua brokerage API (Alpaca). Agent chạy theo schedule với structured logging và safety guardrails.

## Key ideas

- **3-phase workflow:** Research → Trade → Journal
- **Safety first:** Paper trading mặc định, position limits, stop-losses
- **Claude Code integration:** Sử dụng CLAUDE.md làm system prompt + scheduled routines
- **Structured logging:** Journal format giúp audit, debug, và improve
- **Tool use:** Python scripts gọi API, agent orchestrate qua Claude Code
- **Multi-agent option:** Risk reviewer agent có thể approve/reject trade proposals
- **Key trade-offs:** Token costs vs coverage, automation vs oversight

## Related concepts

- [[claude-code-routines]]
- [[alpaca-api]]
- [[paper-trading]]
- [[agent-journal-pattern]]
- [[multi-agent-risk-review]]

## Sources

- [[src_build-ai-trading-agent-claude-code-alpaca]]

## Notes
