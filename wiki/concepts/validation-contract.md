---
type: concept
status: draft
main_tag: ai
sub_tags: [automation]
topic: factory-missions-architecture
sources:
  - [[src_luke-alvoeiro-multi-agent-architecture-factory]]
last_updated: 2026-05-23
---

# Validation Contract

## Definition

Hợp đồng xác thực là định nghĩa rõ ràng về "hoàn thành" được viết **trước** khi bất kỳ dòng code nào được viết. Đóng vai trò như tiêu chí kiểm tra khách quan cho agent output.

## Key ideas

- **Định nghĩa trước thực thi:** Viết contract trước khi code — tránh scope creep
- **Tiêu chí khách quan:** Cung cấp ground truth cho validator đánh giá
- **Clarity over ambiguity:** "Done" có nghĩa cụ thể, không chủ quan
- **Integration với planning:** Orchestrator tạo contract như một phần của kế hoạch

## Related concepts

- [[factory-missions]]
- [[orchestrator-worker-validator]]
- [[plan-execute-verify-loop]]

## Sources

- [[src_luke-alvoeiro-multi-agent-architecture-factory]]

