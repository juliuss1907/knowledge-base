---
type: concept
status: reviewed
main_tag: ai
sub_tags: [research, coding]
topic: llm-capabilities
sources:
  - "[[src_deepseek-v4-architecture]]"
  - "[[src_gemini-4-argon-explained-in-5min]]"
  - "[[src_unreasonable-effectiveness-of-html]]"
last_updated: 2026-10-03
---

# Long Context Models

## Definition

LLMs có khả năng xử lý context window lớn (100K+ tokens). DeepSeek V4 đạt 1M tokens — ngang bậc với Claude Opus 4.7+ (các bản Opus trước đó chỉ 200K max), và vượt xa phần lớn frontier models khác.

## Key ideas

- Thách thức lớn nhất là sự tăng trưởng quadratic của attention (O(n²)) và kích thước KV cache khổng lồ
- Giải pháp trong V4 là dùng hybrid attention (CSA + HCA) để nén context, giảm FLOPs và bộ nhớ
- Khả năng xử lý 1M tokens cho phép model đọc toàn bộ codebase lớn hoặc hàng chục tài liệu dài cùng lúc
- Hiệu suất (RULER benchmark) của V4 Pro vượt trội so với các model closed-source ở cùng độ dài context
- Chia sẻ compressed KV giúp tối ưu hóa tài nguyên trong môi trường multi-agent
- **Output token ≠ input context:** Gemini 4 Argon mở rộng output từ 64.000 lên 1 triệu token — bước nhảy thương mại lớn vì duy trì coherence ở quỹ đạo dài là thách thức riêng, xem [[autoregressive-error-compounding]]
- **Ràng buộc thống kê của độ dài:** mỗi token 99% đúng thì 100 bước chỉ còn ~37% khả năng mọi bước đúng — độ dài output tối đa phải cân với độ tin cậy theo bước
- **Lợi thế dài context mở đường cho long-horizon task:** code migration và research task chạy dài cần model giữ nhất quán xuyên suốt quỹ đạo, không chỉ xử lý input dài
- **Context rộng làm output format tốn token trở nên vô nghĩa:** Thariq Shihipar (Anthropic) dùng Opus 4.7 với context window 1 triệu token để sinh output HTML giàu thông tin thay vì Markdown tiết kiệm token — phần token tăng thêm gần như không thấy trong context, trong khi khả năng thật sự đọc lại tài liệu tăng lên nên tổng output tốt hơn

## Key challenges

- **KV cache size:** 1M tokens = hàng trăng GB mỗi request
- **Quadratic attention:** Traditional attention có complexity O(n²)
- **Compute cost:** Per-token cost tăng theo sequence length

## Solutions in V4

- **CSA + HCA:** Hybrid attention với compression để giảm FLOPs và KV cache
- **FP4 Lightning Indexer:** Efficient block selection cho sparse attention
- **Shared compressed KV:** Multi-agent deployments có thể share representation

## Benchmark results

| Model | RULER (128K) | Long-ROPE (1M) |
|-------|--------------|----------------|
| V4 Pro | ~95 | ~89 |
| Claude Opus | ~87 | N/A (200K tại thời điểm benchmark) |
| OpenAI | ~90 | N/A |
| V4 Flash | ~88 | ~79 |

**Advantage:** V4 Pro không có đối thủ closed-source ở 1M tokens tại thời điểm benchmark. Auditability cho phép kiểm tra tại sao performance degrade ở context length cụ thể.

**Lưu ý về mốc thời gian:** bảng trên là ảnh chụp benchmark từ `[[src_deepseek-v4-architecture]]` (2026-05-28), lúc đó Opus chỉ có 200K context. Anthropic sau đó đưa context window 1M vào từ Opus 4.7 (kèm tokenizer mới), nên cột "Long-ROPE (1M)" của Opus trong bảng không còn phản ánh model hiện hành.

## Related concepts

- [[csa-hca-attention]]
- [[fp4-lightning-indexer]]
- [[autoregressive-error-compounding]]
- [[context-window-management]]
- [[html-as-agent-output-format]]

## Sources

- [[src_deepseek-v4-architecture]]
- [[src_gemini-4-argon-explained-in-5min]]
- [[src_unreasonable-effectiveness-of-html]] — Thariq Shihipar, Anthropic (2026-05-20)

## Notes

