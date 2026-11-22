---
type: concept
status: draft
main_tag: ai
sub_tags: [research, system, law]
topic: confidential-computing-ai
sources: ["[[src_letsencrypt-ai]]"]
last_updated: 2026-11-21
---

# Confidential Computing for AI

## Definition

Confidential computing for AI bảo vệ dữ liệu trong lúc inference bằng trusted execution environments trên CPU/GPU, kết hợp remote attestation để client xác minh workload trước khi gửi prompts hoặc secrets. Mục tiêu là một đường xử lý có thể kiểm chứng, trong đó quyền riêng tư không chỉ dựa vào lời hứa của nhà cung cấp.

## Key ideas

- Bảo vệ phải bao trùm prompts, responses, caches và các transfer, không chỉ mã hóa dữ liệu trên đĩa hoặc đường truyền.
- Remote attestation gắn việc phát hành dữ liệu hoặc khóa với bằng chứng về phần cứng và workload đã được phê duyệt.
- Source, build measurement và công cụ verification cần inspectable để khách hàng kiểm tra tuyến xử lý thực tế.
- TEE chỉ là một lớp; firmware, client bị compromise, external tool và policy logging vẫn là bề mặt rủi ro.
- Chính sách không log hoặc không tái sử dụng dữ liệu phải được enforce bằng software đã review, không suy ra từ enclave.

## Related concepts

- [[secrets-management]]
- [[network-egress-default-deny]]
- [[progressive-hardening]]

## Sources

- [[src_letsencrypt-ai]]

