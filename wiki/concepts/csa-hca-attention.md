---
type: concept
status: reviewed
main_tag: ai
sub_tags: [research, tools]
topic: deepseek-v4-architecture
sources:
  - "[[src_deepseek-v4-architecture]]"
last_updated: 2026-05-29
---

# CSA + HCA Attention

## Definition

Hybrid attention mechanism trong DeepSeek V4: **Compressed Sparse Attention (CSA)** nén local context ~4× trước khi compute attention, **Heavily Compressed Attention (HCA)** nén ~128× dọc sequence dimension. Khác với sliding window attention — CSA nén token, không bỏ qua.

## Key ideas

- CSA nén local context để giảm computational cost mà không mất thông tin như sliding window
- HCA xử lý global attention trên context cực lớn (1M+ tokens) bằng cách nén cực mạnh sequence dimension
- Tối ưu hóa KV cache và FLOPs đáng kể so với attention truyền thống (giảm ~27% FLOPs)
- Kết hợp CSA và HCA tạo ra khả năng reasoning dài hạn hiệu quả hơn GQA
- V4 Pro và Flash có tỷ lệ CSA:HCA khác nhau tùy theo mục tiêu latency vs reasoning

## How it works

- **CSA:** Thay vì O(n·w), giảm effective dimensionality của compressed context. Kết hợp với FP4 Lightning Indexer cho block selection.
- **HCA:** Sau nén, sequence đủ ngắn → dense attention trở lại. Xử lý global attention trên 1M token mà không cần quadratic attention.
- **Interleaving:** V4 Pro ~3:1 CSA-to-HCA; V4 Flash ~4:1 (ít HCA hơn)

## Comparison with GQA

- **GQA (Claude/OpenAI):** Tối ưu trong fixed computational graph — giảm memory cost nhưng vẫn O(n²)
- **CSA + HCA:** Thay đổi computation — CSA thay thế full local attention, HCA thay thế full-sequence global attention

## Results

- V4 Pro ở 1M token context: ~27% FLOPs và ~10% KV cache so với V3.2

## Related concepts

- [[fp4-lightning-indexer]]
- [[long-context-models]]

## Sources

- [[src_deepseek-v4-architecture]]

## Notes

