---
type: source
source_url: https://dev.to/owen_fox/deepseek-v4-released-open-source-16t-moe-1m-context-apache-20-and-its-already-on-the-api-14d6
date_ingested: 2026-04-24
tags: [#ai, #llm]
---
# DeepSeek V4 Released: Open-Source 1.6T MoE, 1M Context, Apache 2.0

Thông tin ra mắt DeepSeek V4 với hiệu suất mạnh mẽ và chi phí cực thấp.

## Key Points
- **Phiên bản**: 
    - **V4-Pro**: 1.6T total params (49B activated), chuyên cho lập trình cạnh tranh và reasoning phức tạp.
    - **V4-Flash**: 284B total (13B activated), tối ưu cho ngân sách thấp.
- **Thông số kỹ thuật**:
    - Context window: 1M tokens.
    - License: Apache 2.0 (Open-source).
    - Kiến trúc: MoE, training với FP4 + FP8 mixed precision trên 32T+ tokens.
    - Tối ưu: Sử dụng CSA và HCA để giảm FLOPs (27%) và KV cache (10%) so với V3.2.
- **Chi phí**: Rẻ hơn đáng kể so với GPT-5.5 (8.6x) và Opus 4.7 (21x).
- **Hiệu suất**:
    - Đạt #3 Arena Code (Thinking mode).
    - Vượt GPT-5.4 trên Codeforces.
    - Vẫn kém hơn Opus 4.6 về khả năng retrieval long-context (>1M).
- **Chế độ**: Có Thinking mode (CoT reasoning) và Non-thinking mode.
