---
type: concept
status: draft
main_tag: ai
sub_tags: [coding, tools]
topic: fable-finding-unknowns
sources:
  - "[[src_field-guide-to-fable-finding-unknowns]]"
  - "[[src_ai-engineering-skills-map]]"
last_updated: 2026-08-23
---

# Agentic Coding

## Definition

Agentic Coding là kỹ năng lập trình với AI agent — không chỉ đơn thuần là "vibe coding" bằng ngôn ngữ tự nhiên, mà là khả năng giảm thiểu và quản lý unknowns (những điều chưa biết) trong quá trình tương tác với AI coding agent. Trong đó, chất lượng output không bị bottleneck bởi khả năng của model, mà bởi khả năng của con người làm rõ những điều họ chưa biết về codebase, constraints, và hành vi của model.

## Key ideas

- Bottleneck chính trong agentic coding không phải là model — Fable là model đầu tiên mà chất lượng work bị giới hạn bởi khả năng của người dùng trong việc làm rõ unknowns của chính họ
- Rumsfeld framework áp dụng vào coding: Known Knowns (có trong prompt), Known Unknowns (biết mình chưa rõ gì), Unknown Knowns (điều hiển nhiên không viết ra nhưng sẽ nhận ra khi thấy), Unknown Unknowns (điều chưa từng cân nhắc)
- Các coder agentic giỏi nhất có rất ít unknowns — họ đồng bộ sâu với cả codebase và model behaviors
- **Blindspot Pass** là kỹ thuật pre-implementation: yêu cầu Claude tìm unknown unknowns trước khi bắt đầu code
- **Interviews:** Yêu cầu Claude phỏng vấn bạn từng câu một về ambiguities, ưu tiên những câu mà câu trả lời sẽ thay đổi kiến trúc
- **References qua source code:** Reference tốt nhất là chính source code — chỉ model vào folder/library và yêu cầu reimplement pattern tương tự
- **Implementation Notes:** Giữ file tạm tracking tất cả decisions, edge cases, và deviations trong quá trình implementation — chọn conservative option khi gặp edge case
- **Post-implementation quizzes:** Sau session dài, yêu cầu Claude quiz bạn về tất cả changes trước khi merge
- **Steering agent là kỹ năng cốt lõi (Andrew Ng):** biết khi nào can thiệp khi nào buông, quản lý context của agent, cân bằng planning vs execution, cung cấp verifiers/evals để agent tự close loop, orchestrate multi-agent; developer thiếu software fundamentals sẽ không biết cung cấp đúng context → agent ra poor tradeoffs
- **Spec-first shift:** khi agent giỏi deliver theo spec, giá trị engineer dịch chuyển sang shaping the build — quyết định cái gì nằm trong spec bằng product sense và business context

## Related concepts

- [[vibe-coding]]
- [[map-is-not-territory]]
- [[ai-coach-prompting]]
- [[ai-engineering-skills]]

## Sources

- [[src_field-guide-to-fable-finding-unknowns]]
- [[src_ai-engineering-skills-map]] — Andrew Ng 2026-08-14: using coding agents là 1/4 kỹ năng AI engineering cốt lõi

## Notes
