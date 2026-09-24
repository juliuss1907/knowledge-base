---
type: concept
status: reviewed
main_tag: ai
sub_tags: [automation, tools, opinion]
topic: ai-trading-agent-claude-code
sources:
  - "[[src_build-ai-trading-agent-claude-code-alpaca]]"
  - "[[src_alex-saint-ai-trading-bot-jev-solana]]"
last_updated: 2026-09-24
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
- **Two-speed operation:** Fast model quyết định theo latency window; slow model rà soát log và đề xuất sửa rules theo lịch
- **Calibrated confidence:** Confidence và outcome thực tế cần được log để kiểm thử calibration, đặt threshold và tìm high-confidence mistakes
- **Wallet isolation:** Bot wallet chỉ giữ stake, lợi nhuận được sweep sang signing wallet và model không đọc private key
- **Approval gate:** Night model chỉ tạo proposal; human hoặc test suite phải phê duyệt trước khi prompt mới được deploy

## Related concepts

- [[claude-code-routines]]
- [[alpaca-api]]
- [[paper-trading]]
- [[agent-journal-pattern]]
- [[multi-agent-risk-review]]
- [[two-speed-agent-loop]]
- [[calibrated-decision-models]]
- [[wallet-isolation-for-ai-agents]]

## Sources

- [[src_build-ai-trading-agent-claude-code-alpaca]]
- [[src_alex-saint-ai-trading-bot-jev-solana]]

## Notes
