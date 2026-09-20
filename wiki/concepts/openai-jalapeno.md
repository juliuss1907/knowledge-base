---
type: concept
status: draft
main_tag: ai
sub_tags: [tools, research]
topic: llm-chip-design
sources:
  - "[[src_jalapeno-llms-for-chip-design]]"
last_updated: 2026-09-20
---

# OpenAI Jalapeño

## Definition

Jalapeño là chip AI accelerator đầu tiên của OpenAI, ra mắt ngày 25 tháng 8 năm 2026. Chip đạt 13.4 petaflops 4-bit compute, 232GB memory, 15.4 TB/s bandwidth, và giảm end-to-end latency đến 3.6 lần so với Nvidia GB300. Điểm đặc biệt nhất: chip được thiết kế với sự hỗ trợ lớn từ LLMs của chính OpenAI.

## Key ideas

- **Performance:** 13.4 petaflops 4-bit compute; 232GB advanced memory; 15.4 TB/s memory bandwidth — giảm latency 3.6x so với Nvidia GB300 với ít điện năng hơn
- **Thiết kế bởi đội nhỏ:** Trung bình dưới 100 người, kết hợp với Broadcom cho physical design — proof of concept cho "small team + AI = frontier chip"
- **Timeline kỷ lục:** Concept → silicon dưới 20 tháng; RTL → tape-out 9 tháng — "likely best in class today"
- **Front-end AI workflow:** Dùng XLS (open-source từ Google) cho high-level synthesis; LLMs assist trong writing, debugging, optimization code chip
- **Backend optimization:** AI-guided physical design giảm 10% area cho matrix multiplication units; software optimization từ 0.31% lên 88.94% theoretical ceiling
- **Model progression:** Sử dụng o3 (2025) → precursors to GPT-6 Astra (2026); models mới làm việc trực tiếp trong Verilog
- **Gen-2 pipeline:** Đang phát triển second và third-generation designs với AI nhiều hơn trong verification và physical design

## Related concepts

- [[ai-chip-design]]

## Sources

- [[src_jalapeno-llms-for-chip-design]]
