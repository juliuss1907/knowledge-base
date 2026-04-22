---
type: concept
status: draft
tags: [#ai, #llm]
updated: 2026-04-22
---
# Ternary Weight LLMs (1.58-bit)

## Mô tả
Kiến trúc LLM sử dụng trọng số ternary (-1, 0, +1) thay vì float 16-bit, cho phép giảm cực lớn footprint bộ nhớ và tăng tốc độ inference mà vẫn giữ được hiệu năng cao.

## Nội dung
Mục tiêu của ternary weights là đưa các LLM lớn xuống các thiết bị edge (điện thoại, laptop) mà không cần quantization phức tạp sau training.

**Ưu điểm nổi bật (ví dụ Ternary Bonsai):**
- **Bộ nhớ:** Giảm footprint xuống ~9 lần (ví dụ bản 8B chỉ tốn 1.75 GB RAM).
- **Tốc độ:** Tăng throughput đáng kể (ví dụ 82 toks/sec trên M4 Pro).
- **Năng lượng:** Hiệu suất năng lượng tốt hơn 3-4 lần so với model 16-bit.
- **Hiệu năng:** Tiệm cận các model full-precision cùng phân khúc (ví dụ Ternary 8B đạt score 75.5, gần với Qwen3 8B).

**Lựa chọn:**
- **1-bit:** Tối ưu tuyệt đối cho footprint.
- **Ternary (1.58-bit):** Cân bằng tốt hơn giữa memory và năng lực thông minh.

## Liên quan
- [[Model Quantization]]
- [[Edge AI]]

## Nguồn tham khảo
- [[wiki/sources/src_ternary-bonsai.md]]
