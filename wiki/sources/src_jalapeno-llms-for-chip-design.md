---
type: source
original: "[[2026-09-19_jalapeno-llms-for-chip-design]]"
main_tag: ai
sub_tags: [research, tools]
topic: llm-chip-design
date_compiled: 2026-09-20
url: https://spectrum.ieee.org/llms-for-chip-design
author: IEEE Spectrum
---

# Jalapeño Shows Power of LLMs for Chip Design

## Metadata

- **Source type:** Article
- **Published:** 2026-09-19
- **Author:** IEEE Spectrum
- **Platform:** IEEE Spectrum
- **URL:** https://spectrum.ieee.org/llms-for-chip-design

## Summary

OpenAI ra mắt Jalapeño — chip AI accelerator đầu tiên của hãng — đạt 13.4 petaflops 4-bit compute, 232GB memory, 15.4 TB/s bandwidth. Jalapeño giảm end-to-end latency đến 3.6 lần so với Nvidia GB300 đồng thời tiêu thụ ít điện năng hơn. Điểm nổi bật không chỉ là hiệu suất mà là quy trình thiết kế: từ first architecture concept đến first silicon chưa đến 20 tháng, và chỉ 9 tháng từ first RTL đến tape-out.

Đội thiết kế Jalapeño trung bình dưới 100 người, kết hợp với Broadcom cho physical design. LLMs được sử dụng chủ yếu ở front-end workflow — Accelerated Hardware Synthesis (XLS) từ Google cho phép viết chip trong môi trường lập trình quen thuộc (DSLX, C++) rồi convert sang Verilog. DeepSeek kernel benchmark cho thấy performance tăng từ 0.31% lên 88.94% theoretical ceiling trong khoảng 40 giờ — kết quả repeatable. OpenAI tin rằng các model tương lai (Astra và beyond) sẽ rất giỏi về chip design.

## Key points

- Jalapeño: 13.4 petaflops 4-bit, 232GB memory, 15.4 TB/s bandwidth — giảm latency 3.6x so với Nvidia GB300
- Từ concept đến silicon dưới 20 tháng; 9 tháng từ RTL đến tape-out — "likely best in class today" theo Andrew Kahng (UCSD)
- Đội thiết kế trung bình dưới 100 người, hợp tác với Broadcom cho physical design
- Front-end workflow dựa trên XLS (Accelerated Hardware Synthesis) — open-source từ Google, cho phép viết chip bằng DSLX/C++ rồi convert sang Verilog
- LLM hiệu quả nhất với code/software-looking tasks — XLS fits vì nó "looks like software"
- DeepSeek multi-head latent attention kernel: 0.31% → 88.94% theoretical ceiling trong ~40 giờ — repeatable
- AI-guided physical design optimization: giảm 10% area cho matrix multiplication units so với human baseline
- Model tiến hóa từ o3 (2025) → precursors to GPT-6 Astra (Sep 2026) — model mới làm việc trực tiếp trong Verilog
- Backend optimization (routing, clock, power) vẫn phần lớn do Broadcom xử lý — nhưng models 2026 đã cải thiện khả năng này
- Ho và Leary hint rằng gen-2 workflow sẽ "look old-fashioned" so với next efforts — more AI trong verification và physical design

## Concepts referenced

- [[ai-chip-design]]
- [[openai-jalapeno]]
