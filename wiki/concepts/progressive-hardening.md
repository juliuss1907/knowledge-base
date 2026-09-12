---
type: concept
status: draft
main_tag: ai
sub_tags: [coding, tools]
topic: harness-engineering-ai-coding
sources:
  - "[[src_harness-engineering-ai-coding]]"
last_updated: 2026-09-12
---

# Progressive Hardening

## Definition

Progressive hardening là promotion ladder mô tả cách architectural constraints mature từ initial declaration sang deterministic enforcement. Đây là nguyên tắc thiết kế cốt lõi của harness engineering: không phải tất cả constraints đều có thể enforce deterministically ngay từ đầu, và agent-based enforcement không nên là permanent state.

## Key ideas

- **Ba giai đoạn:** (1) Unverified — constraint đã declared trong HARNESS.md nhưng chưa có mechanism check; (2) Agent — constraint được enforce bởi LLM judgment trong PR review hoặc scheduled inspection; (3) Deterministic — constraint express đủ precise để encode thành script/linter rule/structural check, chạy trong CI, pass hoặc block merge.
- **Direction is always toward deterministic:** Khi agent repeatedly catches cùng một class violation, đó là signal pattern đã understood đủ để automate — viết script, retire agent check, move sang deterministic status.
- **Unverified không phải failure:** Trạng thái unverified là honest accounting — team recognize constraint quan trọng nhưng chưa có mechanism check. Đây là starting point hợp lệ, không phải thiếu sót.
- **Ngăn hai failure modes:** (1) Trying enforce everything deterministically từ đầu (impossible với novel constraints); (2) Accepting agent-based enforcement làm permanent state (expensive và unreliable).
- **Progressive và adaptive:** Constraints mature theo trải nghiệm thực tế — team learn từ violations, gradually express rules precise hơn, migrate từ judgment-based sang rule-based.

## Related concepts

- [[harness-engineering]]
- [[context-engineering]]
- [[three-enforcement-loops]]

## Sources

- "[[src_harness-engineering-ai-coding]]"

## Notes
