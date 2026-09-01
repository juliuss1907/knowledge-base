---
type: source
original: "[[2026-08-30_ai-engineering-skills-map-software-engineering-fundamentals]]"
main_tag: ai
sub_tags: [coding, research]
topic: ai-engineering-skills
date_compiled: 2026-08-31
url: https://www.deeplearning.ai/the-batch/the-ai-engineering-skills-map-in-detail-software-engineering-fundamentals
author: Andrew Ng
---

# The AI Engineering Skills Map In Detail — Software Engineering Fundamentals

## Metadata

- **Author:** Andrew Ng (The Batch — deeplearning.ai)
- **Published:** [unknown]
- **Source:** deeplearning.ai
- **URL:** https://www.deeplearning.ai/the-batch/the-ai-engineering-skills-map-in-detail-software-engineering-fundamentals
- **Type:** article

## Summary

Andrew Ng phân tích cách software engineering fundamentals thay đổi khi agentic coding xuất hiện. Ngay cả khi coding agent viết toàn bộ code, hiểu fundamentals vẫn quan trọng để steer agent ra tradeoffs đúng (latency, availability, consistency, reliability, maintainability, simplicity, cost) — hoặc thậm chí biết tradeoffs nào tồn tại. Developer vibe code thiếu fundamentals thường không biết các tradeoff này, dẫn đến agent ra quyết định kém. Kỹ năng gồm 5 mảng: building full-stack applications, managing data, designing system architectures, making systems secure and reliable, scaling and operating in production. Coding agents đã thay đổi cách build software, một phần kiến thức như memorizing syntax trở nên lỗi thời, nhưng developer hiểu sâu cách software hoạt động vẫn vượt trội so với người vibe code không hiểu.

## Key points

- **5 mảng fundamentals:** Building full-stack apps · Managing data · Designing system architectures · Making systems secure/reliable · Scaling & operating in production
- **Steering là chìa khóa:** Hiểu fundamentals để steer agent ra tradeoffs bạn muốn, hoặc biết tradeoffs nào tồn tại để đưa ra quyết định
- **Vibe coding thiếu fundamentals = bad tradeoffs:** Developer không biết tradeoff nào tồn tại thì không steer được agent → agent chọn latency/availability/cost kém
- **Full-stack broadening:** Agentic coding giúp developer chuyên môn hóa (front-end, mobile) đóng vai trò full-stack rộng hơn
- **Data là nền tảng khó thay đổi:** Quản lý data quyết định speed, scalability, availability, reliability, cost; cần hiểu access patterns, data models, storage types, transactions
- **System architecture moving target:** Kiến trúc phù hợp phụ thuộc phase project — prototype đơn giản ≠ production system đầu tiên ≠ scaled system
- **Shift-left security:** "Shift left" đưa security sớm vào lifecycle; mọi developer giờ cũng một phần là security engineer
- **Scaling & production:** SDLC, deployment environment, release strategy, CI/CD, IaaS, observability, load-balancing, sharding/indexing/replication
- **Syntax memorization lỗi thời:** Nhưng hiểu sâu cách software hoạt động vẫn vượt trội — chọn tradeoffs đúng cho application context
- **Fundamentals + AI:** Giúp hiểu software có thể và không thể làm gì, là context quan trọng khi dùng coding agents

## Concepts referenced

- [[ai-engineering-skills]]
- [[agentic-coding]]
- [[vibe-coding]]
- [[shift-left-testing]]

## Original excerpts

> "A novice who vibe codes without understanding software fundamentals can create simple applications, but this often leads to the coding agent making bad tradeoffs in latency, availability, consistency, reliability, maintainability, simplicity, and/or cost."

> "Developers who deeply understand how software works vastly outperform those who vibe code without understanding."