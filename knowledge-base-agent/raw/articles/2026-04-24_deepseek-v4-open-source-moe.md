---
type: raw
source_type: article
source_url: https://dev.to/owen_fox/deepseek-v4-released-open-source-16t-moe-1m-context-apache-20-and-its-already-on-the-api-14d6
date_ingested: 2026-04-24
tags: [#ai, #llm]
status: processed
processed_date: 2026-04-25
---
# DeepSeek V4 Released: Open-Source 1.6T MoE, 1M Context, Apache 2.0

## Tóm tắt

DeepSeek release V4 ngày 24/04/2026 — cùng ngày GPT-5.5, cạnh tranh trực tiếp. Hai biến thể: deepseek-v4-pro (1.6T total params, 49B activated) và deepseek-v4-flash (284B total, 13B activated). Cả hai hỗ trợ 1M-token context với 384K max output, open-source Apache 2.0, và đã available trên API.

## Điểm nổi bật

**Hiệu quả long-context:**
- 27% inference FLOPs so với V3.2
- 10% KV cache so với V3.2
- CSA (Compressed Sparse Attention) + HCA (Heavily Compressed Attention) + mHC

**Giá:**
- V4-Pro: $1.74/$3.48 per million tokens (input/hit vs output)
- V4-Flash: $0.14/$0.28 per million tokens

So với GPT-5.5 ($5/$30) → tiết kiệm 8.6×. So với Opus 4.7 ($15/$75) → tiết kiệm 21×.

**Benchmark:**
- Arena Code: V4-Pro Thinking đạt #3 với 1,456 Elo (88 điểm cao hơn V3.2)
- Codeforces: 3206 — vượt GPT-5.4 (3168)
- SWE-Bench Pro: 55.4 vs K2.6's 58.6 (thua 3 điểm)

**Giới hạn:**
- Long-context retrieval (MRCR 1M): 83.5 vs Opus 4.6's 92.9 — Opus vẫn thắng
- GDPval (knowledge work): Vẫn thua closed frontier models

## Hai chế độ

- **Thinking mode** — có chain-of-thought reasoning
- **Non-thinking mode** — không reasoning

## Khuyến nghị

- Switch sang V4-Pro nếu: Chinese-heavy apps, competitive programming, Codeforces-grade reasoning
- Switch sang V4-Flash nếu: budget $1-2 per million output tokens
- Stay on K2.6 nếu: SWE-Bench-style codebase resolution
- Stay on closed frontier nếu: long-context retrieval >1M tokens, hoặc GDPval-grade knowledge work

## Tech stack

- MoE (Mixture of Experts)
- FP4 + FP8 mixed precision training
- 32T+ tokens pre-trained
- Apache 2.0 license