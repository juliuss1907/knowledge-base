---
type: source
original: "[[2026-09-16_googletech-behavioral-evals-harness-engineering]]"
main_tag: ai
sub_tags: [coding, tools]
topic: behavioral-evals-harness-engineering
date_compiled: 2026-09-17
url: https://x.com/GoogleCloudTech/status/2099946653134229721
author: "@GoogleCloudTech (N Taylor Mullen & C G Underman)"
---

# Behavioral Evaluations for Harness Engineering in Agentic Coding

## Metadata

- **Author:** N Taylor Mullen & C G Underman (@GoogleCloudTech)
- **Published:** 2026-09-16
- **Source:** X (Twitter)
- **URL:** https://x.com/GoogleCloudTech/status/2099946653134229721
- **Type:** social media post

## Summary

Khi phát triển harness engineering cho agentic coding, nhiều đội developer mắc sai lầm chạy các end-to-end benchmark như Terminal-Bench hay DeepSWE, quan sát composite score thay đổi vài phần trăm nhưng không hiểu tại sao. Behavioral evaluations — các phép test ở cấp độ nhỏ hơn, đo lường các hành vi cụ thể của agent — là công cụ tốt hơn để xác định chính xác hành vi nào hoạt động đúng và hành vi nào cần cải thiện. Bài viết phân biệt giữa hai paradigm: end-to-end benchmarks giống "thi cuối kỳ" cho thấy kết quả tổng thể nhưng không giải thích lý do, trong khi behavioral evals giống integration tests giúp xác định nguyên nhân cụ thể của sự thay đổi. Phương pháp bắt đầu với dogfooding, chuyển sang evals khi agent đã đủ trưởng thành, và xây dựng behavioral suite với ba bước: chọn một failure mode, viết assertions phù hợp, và tự động hóa batch evaluations.

## Key points

- **End-to-end benchmark có limit:** cho thấy composite score thay đổi nhưng không trả lời được tại sao — cần behavioral evals để hiểu nguyên nhân
- **Behavioral evals = integration tests cho agent:** đo lường các hành vi cụ thể như hỏi clarifying question khi prompt ambiguous, chạy validator trước khi declare done, cung cấp canonical repo links khi tạo documentation
- **Dogfooding trước, evals sau:** khi bootstrapping agent mới, dùng developer instinct + dogfooding; evals thuộc phase hai — đảm bảo forward progress và guard against regressions
- **Evals không phải để ăn mừng improvement 2%:** purpose chính là tạo confidence rằng prompt tweak, tool schema change, hoặc model upgrade không làm agent worse
- **Viết behavioral evals:** assert trên intermediate execution steps (tool calls, file modifications) thay vì final string equality; có thể tự động hóa prompt engineering với loop LLM tự tweak system prompt
- **Ba bước build behavioral suite:** (1) Chọn 1 failure mode cụ thể, (2) Viết assertions phù hợp — strict single-turn cho simple tasks, fuzzy outcome-based cho complex tasks, (3) Tự động hóa batch evals để monitor stability theo thời gian thay vì block PR trên single eval run
- **Behavioral evals bổ sung cho end-to-end benchmarks:** macro benchmarks verify final destination, micro behavioral evals enable safe rapid iteration

## Concepts referenced

- [[harness-engineering]]
- [[behavioral-evals]]
- [[agentic-coding]]
- [[ai-evals]]
