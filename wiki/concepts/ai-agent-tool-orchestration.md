---
type: concept
status: draft
main_tag: ai
sub_tags: [tools, automation]
topic: ai-agent-tool-platform
sources:
  - "[[src_monid-ai-agent-tool-platform.md]]"
last_updated: 2026-07-26
---

# AI Agent Tool Orchestration

## Definition

AI Agent Tool Orchestration là phương pháp cho phép AI agents tự động khám phá, chọn lựa và sử dụng các external tools để hoàn thành nhiệm vụ. Thay vì hard-code tích hợp với từng tool riêng lẻ, agent được trang bị khả năng dynamic tool selection dựa trên context và yêu cầu cụ thể.

## Key ideas

- **Dynamic discovery**: Agent có thể tự động tìm kiếm và so sánh các tool phù hợp mà không cần developer cấu hình trước
- **Self-service integration**: Agent đọc skill.md hoặc documentation để hiểu cách sử dụng tool mới
- **Context-aware selection**: Agent chọn tool dựa trên fit score và pricing, không chỉ dựa trên tên gọi
- **Unified interface**: Tất cả các tool được truy cập qua một interface nhất quán, giảm cognitive load cho agent
- **Cost optimization**: Agent có thể so sánh giữa nhiều alternatives và chọn giải pháp cost-effective nhất

## Related concepts

- [[unified-api-gateway]]
- [[mcp-protocol]]
- [[agent-capability-discovery]]

## Sources

- [[src_monid-ai-agent-tool-platform.md]] — Monid platform cho phép agents discover và sử dụng 1,300+ tools

## Notes

