---
type: source
original: "[[2026-05-22_luke-alvoeiro-multi-agent-architecture-factory]]"
main_tag: ai
sub_tags: [tools, automation]
topic: factory-missions-architecture
date_compiled: 2026-05-23
url: https://www.youtube.com/watch?v=ow1we5PzK-o
author: Luke Alvoeiro (Factory)
---

# The Multi-Agent Architecture That Actually Ships — Luke Alvoeiro, Factory

## Metadata

- **Author:** Luke Alvoeiro (Factory)
- **Published:** 2026-05-22
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=ow1we5PzK-o
- **Type:** video

## Summary

Factory trình bày "Missions" — kiến trúc multi-agent thực tế cho SDLC (Software Development Life Cycle). Thay vì human attention là bottleneck, hệ thống cho phép kỹ sư định nghĩa **cái gì** cần xây dựng, để agent tự tìm cách **làm thế nào**.

## Key points

- **Nút thắt cổ chai:** Không phải trí tuệ mà là **sự chú ý của con người** — kỹ sư chỉ xử lý được vài tác vụ cùng lúc
- **Ba vai trò cốt lõi:** Orchestrator (lập kế hoạch), Worker (thực thi), Validator (kiểm tra)
- **Validation Contract:** Định nghĩa "hoàn thành" **trước** khi viết code — hợp đồng xác thực rõ ràng
- **Multi-Agent Taxonomy:** 5 mô hình — Delegation, Creator-Verifier, Direct Communication, Negotiation, Broadcast
- **Worker isolation:** Mỗi Worker bắt đầu với context sạch, commit qua Git, Worker tiếp theo kế thừa mã sạch
- **Validator adversarial:** Scrutiny Validator (lint, type, tests) và User Testing Validator (tương tác UI), chưa bao giờ thấy code trước đó
- **Kết quả:** Hệ thống chạy liên tục lên đến **16 ngày** (tiềm năng 30 ngày), tạo code sạch với độ bao phủ test cao

## Concepts referenced

- [[factory-missions]]
- [[multi-agent-taxonomy]]
- [[validation-contract]]
- [[orchestrator-worker-validator]]
- [[agent-handoff]]

## Original excerpts

> "The bottleneck isn't intelligence. It's **human attention**. Even the best engineers can only handle a few tasks at once."

> "Shift from human doing the work to human deciding **what** to build, while the system figures out **how**."

> "We write the Validation Contract **before** any code is written — we define what done looks like."

> "Detailed notes: https://docs.google.com/document/d/e/2PACX-1vQTt9ppCFv0Mb97gbUIF4hbdmLWaktb4NqNwNT985kmlGbKlBcEq8CGZ92PtvJWHDOYbvHp922lOkQB/pub"
