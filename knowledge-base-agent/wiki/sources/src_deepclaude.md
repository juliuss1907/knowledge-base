---
type: source
source_type: repo
source_url: https://github.com/aattaran/deepclaude
date_ingested: 2026-05-04
tags: [#ai, #coding]
---

# deepclaude — Use Claude Code with DeepSeek V4 Pro

Sử dụng agent loop tự trị của Claude Code với các backend rẻ hơn như DeepSeek V4 Pro, OpenRouter hoặc bất kỳ backend nào tương thích với Anthropic.

**Điểm chính:**
- **Tiết kiệm chi phí:** Rẻ hơn tới 17 lần so với dùng trực tiếp Anthropic.
- **Hiệu năng:** DeepSeek V4 Pro đạt 96.4% trên LiveCodeBench, tương đương Claude Opus cho 80% tác vụ coding thông thường.
- **Backend hỗ trợ:** DeepSeek (mặc định), OpenRouter, Fireworks AI, Anthropic.
- **Hạn chế:** Không hỗ trợ vision, parallel tool use, và MCP servers qua lớp tương thích.
- **Cơ chế:** Chạy proxy tại `localhost:3200` để đánh chặn và điều hướng API calls.
