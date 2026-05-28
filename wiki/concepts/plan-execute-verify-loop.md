---
type: concept
status: draft
main_tag: ai
sub_tags:
  - research
  - coding
topic: code-as-agent-harness
sources:
  - "[[src_code-as-agent-harness-arxiv-2605-18747]]"
last_updated: 2026-05-23
---

# Plan-Execute-Verify Loop

## Definition

Vòng lặp Plan-Execute-Verify (PEV) là cơ chế điều khiển (control process) biến debugging thành quy trình chuyển đổi trạng thái (state transition) có cấu trúc cho agent systems. Mỗi phase có guardrails và verification criteria rõ ràng.

## Key ideas

- **Planning as Contract Formation:** Định nghĩa thay đổi dự định trước khi thực thi — pre-conditions rõ ràng
- **Sandboxed Execution:** Kiểm tra trong môi trường cô lập trước khi áp dụng
- **Permissioned State Transition:** Thay đổi được kiểm soát qua role-based permissions
- **Deterministic Verification:** Kiểm tra tính đúng đắn khách quan — linters, tests, type checkers

## Related concepts

- [[agent-harness]]
- [[code-as-substrate]]
- [[harness-control]]

## Sources

- [[src_code-as-agent-harness-arxiv-2605-18747]]

