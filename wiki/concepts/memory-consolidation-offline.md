---
type: concept
status: draft
main_tag: ai
sub_tags: [research, tools]
topic: llm-memory-consolidation
sources:
  - "[[src_llm-need-sleep-consolidation]]"
last_updated: 2026-05-28
---

# Memory Consolidation (Offline Processing)

## Definition

Quá trình xử lý "offline" trong hệ thống nhớ của LLM — khi model không nhận input mới mà tập trung tổ chức và củng cố thông tin đã thu thập. Khác với online processing (xử lý real-time), consolidation cho phép deep computation over evicted context mà không ảnh hưởng đến prediction latency.

## Key ideas

- **Bottleneck:** Không phải memory capacity mà là computational capacity cho việc transform evicted context thành internal state hữu ích
- **Recurrence for consolidation:** Áp dụng N lần forward pass để cập nhật fast weights, tương tự gradient descent iterative
- **Eviction strategies:** Hard eviction (clear hoàn toàn) vs sliding-window (giữ L-1 tokens gần nhất)
- **Warm-up phase:** Cần thiết cho sliding-window eviction để model học fast-weight refinement
- **Deep reasoning:** Consolidation tốt hơn → khả năng reasoning sâu hơn trên thông tin đã bị evict khỏi active context

## Related concepts

- [[llm-sleep]]
- [[fast-weights]]
- [[kv-cache-eviction]]
- [[state-space-models-ssm]]

## Sources

- [[src_llm-need-sleep-consolidation]]

## Notes
