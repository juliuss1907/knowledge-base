---
type: concept
status: draft
main_tag: ai
sub_tags: [coding, tools]
topic: behavioral-evals-harness-engineering
sources:
  - "[[src_googletech-behavioral-evals-harness-engineering]]"
last_updated: 2026-09-17
---

# Behavioral Evals

## Definition

Behavioral evals là các phép đánh giá AI agent ở cấp độ nhỏ, đo lường các hành vi quan sát được (observable actions) thay vì kết quả cuối cùng. Khác với end-to-end benchmarks cho thấy tổng thể performance nhưng không giải thích lý do, behavioral evals giống integration tests giúp xác định chính xác hành vi nào hoạt động đúng và hành vi nào cần cải thiện — từ đó cho phép iteration nhanh và an toàn hơn.

## Key ideas

- **Đo lường intermediate steps:** Behavioral evals assert trên tool calls, file modifications, và các hành vi trung gian thay vì final string equality — ví dụ: agent có hỏi clarifying question khi prompt ambiguous không, có chạy validator trước khi declare done không
- **Phân biệt với end-to-end benchmarks:** Macro benchmarks verify final destination; behavioral evals serve as iteration partner giúp hiểu tại sao score thay đổi và ngăn regressions
- **Dogfooding trước, evals sau:** Giai đoạn đầu dùng developer instinct + dogfooding; evals thuộc phase hai khi agent đủ trưởng thành — purpose không phải ăn mừng improvement 2% mà là đảm bảo prompt tweak/model upgrade không làm agent worse
- **Hai loại assertions:** Strict single-turn assertions cho simple tasks có 1 optimal solution; fuzzy outcome-based checks (bao gồm LLM-as-a-judge) cho complex tasks nơi agent có thể đi đường khác nhưng vẫn đúng
- **Batch evals > single eval runs:** Thay vì block PR trên single eval run (noisy do nondeterminism), tự động hóa batch evals để track aggregate pass rates theo thời gian — directional signal cho phép tweak prompts và upgrade models an toàn
- **Tự động hóa prompt engineering:** Có thể setup loop LLM tự tweak system prompt, iterate cho đến khi failing test pass, với rest of test suite hoạt động như CI/CD guardrail

## Related concepts

- [[ai-evals]]
- [[harness-engineering]]
- [[agentic-coding]]

## Sources

- "[[src_googletech-behavioral-evals-harness-engineering]]"

## Notes
