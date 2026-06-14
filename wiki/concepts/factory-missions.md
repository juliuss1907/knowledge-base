---
type: concept
status: reviewed
main_tag: ai
sub_tags: [automation, research, tools]
topic: factory-missions-architecture
sources:
  - "[[src_luke-alvoeiro-multi-agent-architecture-factory]]"
last_updated: 2026-05-23
---

# Factory Missions

## Definition

"Missions" là kiến trúc multi-agent được Factory phát triển nhằm mang lại khả năng tự trị hoàn toàn cho vòng đời phát triển phần mềm (SDLC). Hệ thống chuyển đổi từ human doing sang human deciding — kỹ sư định nghĩa **cái gì** cần xây dựng, agent tự tìm cách **làm thế nào**.

## Key ideas

- **Human attention bottleneck:** Kỹ sư giỏi nhất cũng chỉ xử lý được vài tác vụ cùng lúc do nhu cầu giám sát liên tục
- **Ba vai trò:** Orchestrator (lập kế hoạch), Worker (thực thi), Validator (kiểm tra)
- **Validation Contract:** Định nghĩa "hoàn thành" trước khi viết code
- **Worker isolation:** Context sạch cho mỗi Worker, commit qua Git
- **Adversarial validation:** Validator chưa từng thấy code trước đó — đảm bảo tính khách quan
- **Thực tế:** Chạy liên tục 16-30 ngày, tạo code sạch với test coverage cao

## Related concepts

- [[multi-agent-taxonomy]]
- [[validation-contract]]
- [[orchestrator-worker-validator]]
- [[agent-handoff]]

## Sources

- [[src_luke-alvoeiro-multi-agent-architecture-factory]]

