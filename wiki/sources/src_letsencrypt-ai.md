---
type: source
original: "[[2026-11-08_letsencrypt-ai]]"
main_tag: ai
sub_tags: [research, system, law]
topic: confidential-computing-ai
date_compiled: 2026-11-21
url: https://letsencrypt.ai/
author: Let's Encrypt AI
---

# Let's Encrypt AI — A position paper on private AI

## Metadata

- **Source type:** Website
- **Published:** N/A
- **Author:** Let's Encrypt AI
- **URL:** https://letsencrypt.ai/

## Summary

Position paper kêu gọi đưa confidential computing thành mặc định cho AI chat trên phần lớn AI GPU vào cuối năm 2027. Luận điểm trung tâm là prompt, response và context thuộc quyền kiểm soát của người dùng; việc dùng dữ liệu để training phải là thỏa thuận riêng có informed consent. Bài viết đề xuất một protected path từ client qua CPU/GPU được attestation đến phản hồi, cùng phần mềm có thể kiểm tra và chính sách logging/reuse được enforce. Nó cũng nhấn mạnh rằng TEE không đủ một mình: client, firmware, external tools và policy của workload vẫn là các điểm cần kiểm soát.

## Key points

- Confidential computing mở rộng bảo vệ từ data at rest/in transit sang nơi AI thực thi trên CPU và GPU.
- TEE cô lập execution khỏi host operator, còn remote attestation cho client xác minh phần cứng và phần mềm trước khi gửi dữ liệu.
- Bảo vệ cần bao phủ prompts, responses, caches và transfers trong toàn bộ đường đi.
- Phần mềm security-critical, build measurements và công cụ kiểm chứng cần được công khai để người dùng kiểm tra workload.
- Enclave vẫn có thể chạy code sao chép dữ liệu; logging và reuse policy phải được enforce trong phần mềm đã review.
- Hardening được đề xuất gồm tắt SSH/debug shell, dùng image bất biến và chỉ phát hành secrets sau khi verification đạt policy.
- Người mua và developer có thể tạo áp lực thị trường bằng cách yêu cầu attestation và bằng chứng bảo vệ.

## Concepts referenced

- [[confidential-computing-ai]]

