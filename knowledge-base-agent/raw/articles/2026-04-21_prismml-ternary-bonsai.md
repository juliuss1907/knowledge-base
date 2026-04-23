---
type: raw
source_type: article
source_url: https://prismml.com/news/ternary-bonsai
date_ingested: 2026-04-21
tags: [#ai, #llm]
status: processed
processed_date: 2026-04-22
---
# Ternary Bonsai — 1.58-bit Language Models by PrismML

## Tóm tắt

Ternary Bonsai là model 1.58-bit (ternary: -1, 0, +1) từ PrismML (Caltech researchers, backed by Khosla Ventures, Google). Mục tiêu: footprint nhỏ nhưng hiệu năng cao.

## Điểm nổi bật

**3 size options:** 8B, 4B, 1.7B parameters

**Benchmark (8B model):**
- Đạt 75.5 avg score — chỉ thua Qwen3 8B (16.38 GB)
- Nhỏ hơn 9-10x so với các models cùng tier
- 1-bit Bonsai 8B: 70.5 → Ternary 8B: 75.5 (+5 điểm), chỉ tốn thêm 600MB

**Memory footprint:**
- Ternary Bonsai 8B: 1.75 GB (~9x nhỏ hơn 16-bit models)

**Throughput:**
- M4 Pro: 82 toks/sec (5x nhanh hơn 16-bit 8B)
- iPhone 17 Pro Max: 27 toks/sec

**Energy efficiency:**
- 3-4x better energy efficiency vs 16-bit
- M4 Pro: 0.105 mWh/tok
- iPhone 17 Pro Max: 0.132 mWh/tok

## Platform

- Chạy native trên Apple devices qua MLX
- Apache 2.0 License

## So với 1-bit Bonsai

1-bit Bonsai vẫn là lựa chọn khi footprint tối thiểu là ưu tiên. Ternary Bonsai là alternative khi có thể trade thêm chút memory cho model mạnh hơn.

## Links

- Website: https://prismml.com/news/ternary-bonsai
- Whitepaper: https://github.com/PrismML-Eng/Bonsai-demo/blob/main/ternary-bonsai-8b-whitepaper.pdf
