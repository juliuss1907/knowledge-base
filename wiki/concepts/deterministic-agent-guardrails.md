---
type: concept
status: draft
main_tag: ai
sub_tags: [coding, automation, research]
topic: deterministic-agent-guardrails
sources: ["[[src_all-code-is-slop-except-mine]]"]
last_updated: 2026-11-21
---

# Deterministic Agent Guardrails

## Definition

Deterministic agent guardrails là các ràng buộc thực thi được trong codebase—như API design, type system, dependency rules, lint và test—để agent mặc định làm đúng. Chúng thay thế dần việc dựa vào prose, comments hoặc review thủ công cho các lỗi đã biết.

## Key ideas

- Sửa một lỗi agent lặp lại nên dẫn đến một invariant, API hoặc rule có thể kiểm tra tự động.
- Code sạch là context có tính khuếch đại vì agent thường tái sử dụng pattern hiện hữu.
- Hạn chế primitive khó dùng đúng giúp loại cả một lớp lỗi thay vì phát hiện muộn trong review.
- Runtime và formal verification cung cấp evidence về hành vi, không chỉ niềm tin vào diff hoặc mô tả.
- Verification mạnh là điều kiện để agent tự xử lý nhiều PR mà không làm tăng revert rate.

## Related concepts

- [[agentic-coding]]
- [[agent-harness]]
- [[shift-left-testing]]
- [[validation-contract]]

## Sources

- [[src_all-code-is-slop-except-mine]]

