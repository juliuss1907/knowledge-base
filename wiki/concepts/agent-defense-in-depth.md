---
type: concept
status: draft
main_tag: tech
sub_tags: [tools, hack, system]
topic: agent-defense-in-depth
sources:
  - "[[src_10-questions-for-your-startup-developers]]"
last_updated: 2026-08-27
---

# Agent Defense in Depth

## Definition

Chiến lược bảo vệ nhiều lớp cho AI agent — cho agent có khả năng gọi tool, duyệt web, hoặc chạy code — tương tự defense-in-depth của production service, nhưng cần hơn vì agent ra quyết định mà cả bạn lẫn model không thể dự đoán hết trước. Bốn lớp, không lớp nào tùy chọn khi đã có user thật.

## Key ideas

- **Lớp 1 — Identity cho agent:** mỗi agent có service account riêng, scope chỉ tới resource/tool thực sự cần. Agent Engine hỗ trợ agent identity first-class để mọi hành động quy về một agent instance trong audit logs
- **Lớp 2 — Sandboxed code execution:** nếu agent chạy code sinh ra, không chạy trong application process. Dùng isolated sandbox để tổ hợp xấu không chạm production data
- **Lớp 3 — Prompt và response filtering:** Model Armor đặt trước model calls, screen prompt injection, jailbreaks, sensitive-data exfiltration, off-brand output
- **Lớp 4 — Behavioral monitoring:** Security Command Center với threat detection flag anomaly — service account đột nhiên gọi API chưa từng chạm, agent reach external host lạ, spike bất thường trong privileged operations
- **Nguyên tắc nền:** defense-in-depth nghĩa là không lớp nào là điểm chết duy nhất — kết hợp identity split + sandbox + filtering + monitoring

## Related concepts

- [[secrets-management]]
- [[cloud-auth-hierarchy]]
- [[oauth-security-risks]]
- [[ai-safety-monitoring]]

## Sources

- [[src_10-questions-for-your-startup-developers]]

## Notes

