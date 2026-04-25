---
type: raw
source_type: article
source_url: https://dev.to/owen_fox/gpt-55-released-first-fully-retrained-base-model-since-gpt-45-1m-context-530-pricing-4nj0
date_ingested: 2026-04-24
tags: [#ai, #llm]
status: processed
processed_date: 2026-04-25
---
# GPT-5.5 Released: First Fully Retrained Base Model Since GPT-4.5, 1M Context, $5/$30 Pricing

## Tóm tắt

OpenAI release GPT-5.5 ngày 23/04/2026 — first fully retrained base model kể từ GPT-4.5 (5.1→5.4 chỉ là post-training iterations). Features: 1M-token context, agent-oriented training, two variants: GPT-5.5 Thinking ($5/$30) và GPT-5.5 Pro ($30/$180).

## Điểm nổi bật

**Benchmark:**
- Terminal-Bench 2.0: 82.7% —领先 Opus 4.7 đến 13 điểm
- Artificial Analysis Intelligence Index: 60 điểm — end 3-way tie
- GDPval (knowledge work): 84.9%

**Giới hạn:**
- SWE-Bench Pro: Opus 4.7 thắng 64.3% vs 58.6%
- Hallucination rate cao nhất: 86% (AA-Omniscience) — cao hơn Opus 4.7 (36%) và Gemini 3.1 Pro (50%)

**Giá:**
- GPT-5.4: $2.50/$15 per million tokens
- GPT-5.5: $5/$30 per million tokens — tăng 2×

OpenAI argument: GPT-5.5 dùng ít tokens hơn ~40% cho cùng task → net ~20% cost increase.

## Hai variants

| Variant | Context | Input/Output |
|---|---|---|
| GPT-5.5 Thinking | 1M | $5/$30 |
| GPT-5.5 Pro | 1M | $30/$180 |

## Khuyến nghị

- Upgrade nếu: agent workflows với multi-step tool calls, terminal automation, browsing, computer use
- Upgrade nếu: long-context analysis >200K tokens
- Test trước nếu: codebase-resolution tasks (SWE-Bench Pro vẫn thua Opus 4.7)
- Stay put nếu: high-volume, latency-sensitive chat at GPT-5.4 price points
- Test trước nếu: hallucination là failure mode (factual Q&A, citation generation, compliance)

## Điểm đáng chú ý

GPT-5.5 là agent model — "takes a sequence of actions, uses tools, checks its own work, and keeps going until a task is finished" mà không cần human re-prompt ở mỗi step. Đây là hướng đi rõ ràng của OpenAI.