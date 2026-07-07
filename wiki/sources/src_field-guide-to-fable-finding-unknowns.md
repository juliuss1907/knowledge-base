---
type: source
original: "[[2026-07-06_field-guide-to-fable-finding-unknowns]]"
main_tag: ai
sub_tags: [coding, tools]
topic: fable-finding-unknowns
date_compiled: 2026-07-07
url: https://x.com/trq212/status/2073100352921215386
author: Thariq (@trq212)
---

# A Field Guide to Fable: Finding Your Unknowns

## Metadata

- **Author:** Thariq (@trq212)
- **Published:** 2026-07-03
- **Source:** X Article
- **URL:** https://x.com/trq212/status/2073100352921215386
- **Type:** article

## Summary

Thariq trình bày một framework toàn diện để giảm thiểu "unknowns" khi làm việc với Claude Fable 5 — một kỹ năng mà anh cho rằng là bottleneck chính quyết định chất lượng output của agentic coding. Bài viết áp dụng Rumsfeld matrix (known knowns, known unknowns, unknown knowns, unknown unknowns) vào lập trình với AI agent, chia thành ba giai đoạn: pre-implementation (blindspot pass, brainstorms, interviews, references, implementation plans), during implementation (implementation notes để track deviations), và post-implementation (pitches, quizzes trước khi merge). Thariq nhấn mạnh rằng những coder giỏi nhất trong kỷ nguyên agentic là những người có ít unknowns nhất — họ đồng bộ sâu với cả codebase và hành vi của model. Anh minh họa toàn bộ quy trình bằng chính trải nghiệm edit video launch Fable hoàn toàn bằng Claude Code, từ cut video, transcription, đến color grading.

## Key points

- "The map is not the territory" — map là prompt/skills/context bạn đưa cho Claude, territory là codebase thực tế và constraints của nó
- Rumsfeld framework áp dụng vào coding: Known Knowns (những gì có trong prompt), Known Unknowns (điều bạn biết mình chưa rõ), Unknown Knowns (điều hiển nhiên với bạn đến mức không viết ra), Unknown Unknowns (điều bạn chưa từng nghĩ đến)
- Chất lượng work với Fable bị bottleneck bởi khả năng làm rõ unknowns — không phải bởi model
- **Blindspot Pass:** Yêu cầu Claude tìm unknown unknowns trước khi bắt đầu implementation — "I know nothing about this codebase, do a blindspot pass"
- **Interviews:** Yêu cầu Claude phỏng vấn bạn từng câu một về ambiguities, ưu tiên câu hỏi mà câu trả lời sẽ thay đổi kiến trúc
- **References:** Reference tốt nhất là source code — chỉ Fable vào folder/library và bảo nó tìm pattern cần reimplement
- **Implementation Plans:** Yêu cầu Claude đưa ra plan làm lộ những decisions bạn dễ thay đổi nhất (data models, type interfaces, UX flows)
- **Implementation Notes:** Claude Code giữ file tạm `implementation-notes.md` tracking decisions, edge cases, và deviations — chọn conservative option khi gặp edge case
- **Quizzes:** Sau session dài, yêu cầu Claude quiz bạn về changes — chỉ merge sau khi trả lời đúng hoàn toàn
- Các coder agentic giỏi nhất (như Boris, Jarred) có rất ít unknowns — họ đồng bộ sâu với codebase và model behaviors

## Concepts referenced

- [[agentic-coding]]
- [[map-is-not-territory]]
- [[vibe-coding]]

## Original excerpts

> "The map is not the territory. The map = your prompts, skills, context — what you give Claude. The territory = the codebase, real world, its actual constraints. The gap between them = unknowns."

> "Every explainer, brainstorm, interview, prototype, and reference is a cheap way to find out what you didn't know before it gets expensive to fix."

> "Fable is the first model where the quality of work is bottlenecked by your ability to clarify its unknowns."
