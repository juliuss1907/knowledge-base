---
type: source
original: "[[2026-08-30_openviking]]"
main_tag: ai
sub_tags: [tools, automation]
topic: agent-context-database
date_compiled: 2026-08-31
url: https://github.com/volcengine/OpenViking
author: volcengine
---

# OpenViking: The Context Database for AI Agents

## Metadata

- **Author:** volcengine
- **Published:** [unknown]
- **Source:** github.com
- **URL:** https://github.com/volcengine/OpenViking
- **Type:** repo

## Summary

OpenViking là một open-source context database dành riêng cho AI agents, lưu trữ memories, resources và skills như một virtual filesystem dưới giao thức `viking://`. Thay vì truy vấn một vector store dạng black-box, agent duyệt context của chính mình bằng `ls`, `tree`, `find` — xử lý mang tính deterministic giống developer làm việc với files. Mỗi entry được xử lý thành ba tầng L0 (abstract), L1 (overview), L2 (details) và chỉ load sâu theo mức cần thiết để cắt giảm token spend. Mỗi lần retrieval đều để lại trajectory có thể quan sát và debug. Kết quả đánh giá trên LoCoMo và tau2-bench cho thấy độ chính xác tăng đáng kể (24–57% lên 80–83%) đồng thời giảm token input 34.3–91.0%.

## Key points

- **Context là virtual filesystem:** Memories, resources, skills mỗi loại có một `viking://` URI riêng; agent locate và manipulate context deterministic
- **Tiered loading cắt token spend:** Mỗi entry xử lý thành L0/L1/L2 ngay khi write, chỉ load sâu theo task yêu cầu
- **Directory recursive retrieval:** Vector search tìm directory điểm cao nhất rồi drill-down từng lớp, kết quả mang theo context xung quanh
- **Observable retrieval:** Mỗi query giữ lại directory-browsing trajectory; kết quả sai thì thấy chính xác path nào tạo ra
- **Sessions thành memory:** Sau khi session commit, OpenViking async trích xuất user preferences + agent experience vào long-term memory
- **Kết quả LoCoMo:** 3 agent integration đạt 80–83% accuracy (từ 24–57% native memory), input tokens giảm 34.3–91.0%, query latency giảm 58.45–66.10%
- **Kết quả tau2-bench:** Experience memory nâng task success +6.87pp (retail) và +11.87pp (airline)
- **Nhiều integration:** Claude Code, Codex, OpenClaw, Hermes, Cursor, MCP clients, LangChain/LangGraph
- **Nền tảng nghiên cứu:** Open-sources subset từ paper VikingMem (arXiv:2605.29640, VLDB 2026)
- **Commercial không cripple:** Edition open-source đầy đủ dưới AGPLv3, commercial editions chỉ trả lời "ai vận hành và chạy ở đâu"

## Concepts referenced

- [[context-database]]
- [[agent-memory-taxonomy]]
- [[progressive-disclosure]]
- [[context-window-management]]

## Original excerpts

> "One filesystem for all context. Memories, resources, and skills each get a `viking://` URI. Agents locate and manipulate context deterministically, like a developer working with files."

> "Tiered loading cuts token spend. Every entry is processed into L0 (abstract), L1 (overview), and L2 (details) on write, then loaded only as deep as the task requires."
