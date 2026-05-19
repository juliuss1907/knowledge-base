---
type: concept
status: draft
main_tag: ai
sub_tags: [tools, automation]
topic: hermes-operator-builder-pattern
sources:
  - [[wiki/sources/src_1-month-with-hermes-ive-been-using-wrong]]
last_updated: 2026-05-19
---

# Hermes Operator Role

## Definition

Hermes (và các AI agent tương tự) đóng vai trò **Operator** — chuyên xử lý các công việc định kỳ, tự động phân tích dữ liệu, và deliver tailored reports. Đây là cách sử dụng hiệu quả nhất, khác biệt với vai trò "Builder" của các tool như Claude.

## Key ideas

- **Không phải Builder**: Hermes build chậm, aesthetics kém hơn Claude, thiếu UI features
- **Phù hợp recurring tasks**: Deliver reports, analyze data, pull & learn từ dashboard
- **Self-learning loop**: Tự động setup skills nếu thấy cần, giảm thời gian task lần sau
- **Persistent memory**: Nhớ context và preferences qua các phiên làm việc
- **Cần specific instructions**: Phải rõ ràng khi chỉ định "remember", "make sure to adjust [x] cron job"
- **Kết hợp với Builder**: Xây dashboard bằng Claude, Hermes chạy analyze định kỳ

## Related concepts

- [[claude-builder-role]]
- [[ai-tool-role-separation]]
- [[persistent-memory-ai]]

## Sources

- [[wiki/sources/src_1-month-with-hermes-ive-been-using-wrong]]

## Notes
