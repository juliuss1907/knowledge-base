---
type: source
original: "[[2026-10-15_pstack-cursor-engineer-ships-code-with-ai]]"
main_tag: ai
sub_tags: [coding, tools, automation]
topic: pstack-agent-workflow
date_compiled: 2026-11-21
url: https://www.youtube.com/watch?v=4wBVuj2an8E
author: Eric Tech
---

# Pstack: How a Cursor Engineer Ships Code With AI

## Metadata

- **Source type:** Video
- **Published:** 2026-10-15
- **Author:** Eric Tech
- **URL:** https://www.youtube.com/watch?v=4wBVuj2an8E

## Summary

Video giới thiệu Pstack, bộ skills và nguyên tắc phát triển phần mềm với AI của Lauren Tan, trải rộng từ tìm hiểu codebase đến triển khai và bảo trì. Điểm nổi bật là dùng nhiều model/agent để tạo phương án thiết kế rồi phản biện, tổng hợp trước khi code. Quy trình kết hợp TDD, TypeScript practices, dọn diff, end-to-end verification và review nhằm làm thay đổi nhỏ, có bằng chứng và dễ merge. Pstack cũng tách các nguyên tắc khỏi system prompt khổng lồ để chỉ nạp hướng dẫn đúng lúc, giảm chi phí context.

## Key points

- Pstack hướng tới brownfield codebase qua các workflow tìm hiểu “how”, “why” và chia nhỏ công việc.
- Giai đoạn thiết kế dùng nhiều model tạo phương án, sau đó một bước interrogate so sánh và tổng hợp.
- TDD, TypeScript practices và cleanup diff giúp loại bỏ code AI kém chất lượng mà vẫn giữ hành vi qua test.
- Verification skill bao gồm dựng môi trường, chạy ứng dụng như người dùng, thu bằng chứng và dọn tài nguyên.
- Swarm phân rã kiểm thử end-to-end cho nhiều agent rồi tổng hợp báo cáo.
- Review thay đổi có thể dùng agent để cố phá diff và tìm cách đơn giản hóa implementation.
- Nguyên tắc nên được đóng gói thành skills có điều kiện kích hoạt thay vì một system prompt luôn nạp.

## Concepts referenced

- [[pstack-agent-workflow]]
- [[agentic-coding]]

