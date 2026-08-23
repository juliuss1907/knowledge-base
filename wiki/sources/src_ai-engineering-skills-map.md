---
type: source
original: "[[2026-08-14_ai-engineering-skills-map]]"
main_tag: ai
sub_tags: [coding, vibecode]
topic: ai-engineering-skills
date_compiled: 2026-08-23
url: https://x.com/AndrewYNg/status/2088302050706686198
author: AndrewYNg
---

# The AI Engineering Skills Map

## Metadata

- **Author:** Andrew Ng (@AndrewYNg)
- **Platform:** X (post)
- **Published:** 2026-08-14
- **Ingested:** 2026-08-22
- **URL:** https://x.com/AndrewYNg/status/2088302050706686198
- **Type:** post
- **Series:** AI Engineering Skills Map (part 1)

## Summary

Andrew Ng công bố AI Engineering Skills Map, tổng hợp từ phân tích hơn 10.000 job postings, hàng chục cuộc phỏng vấn chuyên gia/hiring manager/recruiter và survey, nhằm giúp developer ưu tiên thứ cần học và employer tuyển đúng người. Ông xác định 4 kỹ năng AI engineering quan trọng nhất: building and deploying AI applications, software engineering fundamentals, using coding agents, và shaping the build. Ng nhấn mạnh "AI engineering skills" rộng hơn chức danh "AI Engineer" — giống như mọi developer ngày nay đều cần biết cloud dù không phải Cloud Engineer. Luận điểm xuyên suốt: AI cho phép build software hoàn toàn khác so với 2022 nhờ output khó đoán của model, nên kỹ năng cốt lõi là dùng statistical techniques (evals, error analysis) để đo lường, điều khiển và govern hệ thống AI; kèm đó là mindset continuous learning vì best practices thay đổi liên tục.

## Key points

- Kỹ năng #1 — Building and deploying AI applications: hiểu building blocks (LLM, context engineering, RAG, agentic workflows, ML/DL) và biết dùng statistical techniques để đo lường, steer, govern hệ thống có output không đoán trước; core skill là disciplined evals + error analysis loops
- Kỹ năng #2 — Software engineering fundamentals: hiểu sâu software giúp nhận ra các tradeoffs (cost, scalability, reliability, speed, security, privacy); developer vibe code thiếu fundamentals sẽ đưa context kém cho coding agent và nhận quyết định tradeoff tồi
- Kỹ năng #3 — Using coding agents: mental model về cách agent vận hành, giới hạn và cách work around; biết khi nào can thiệp khi nào buông, quản lý context, cân bằng planning vs execution, cung cấp verifiers/evals để agent tự close loop, orchestrate multi-agent, tránh pitfall như agent hỏng production database
- Kỹ năng #4 — Shaping the build: khi agent đã giỏi deliver theo spec, công việc engineer dịch chuyển sang quyết định cái gì nằm trong spec; đòi hỏi product sense, business context, customer goals, và ownership (khi nào build MVP nhanh, khi nào chậm mà chắc)
- Thuật ngữ: "AI Engineering skills" ≠ role "AI Engineer" — toàn bộ developer (full-stack, data, DevOps, ML) đều cần, tương tự cloud skills
- Developer vibe code thiếu fundamentals sẽ bị agent đưa ra poor tradeoffs vì họ không biết cung cấp đúng context — steering bằng "precise language of software engineering" cho kết quả tốt hơn hẳn
- Dùng coding agent thành thạo bao gồm routines cập nhật tool mới liên tục vì lĩnh vực tiến hóa quá nhanh
- Methodology: clustering trên massive dataset gồm job postings + expert interviews + surveys → chọn skill quan trọng nhất hiện tại và gần tương lai

## Concepts referenced

- [[ai-engineering-skills]]
- [[agentic-coding]]
- [[vibe-coding]]

## Original excerpts

> All developers today should know how to work with the cloud, and only a smaller number have a "Cloud engineer" title. Similarly, all developers... will need AI engineering skills.

> Understanding software engineering fundamentals lets you make good tradeoffs by steering coding agents using the precise language of software engineering.
