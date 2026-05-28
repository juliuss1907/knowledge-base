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

# LLM Sleep

## Definition

"LLM Sleep" là cơ chế trong mô hình ngôn ngữ lớn (LLM) lấy cảm hứng từ quá trình củng cố ký ức trong giấc ngủ sinh học. Thay vì chỉ sử dụng recurrence trong phase prediction, cơ chế này áp dụng N lần forward pass recurrent trong phase consolidation ("sleep") để cập nhật fast weights từ context bị evict, giúp cải thiện deep reasoning mà không tăng latency ở phase wake.

## Key ideas

- **Sleep phase:** Khi context window đầy, model thực hiện N recurrent passes để cập nhật fast weights (S) trước khi clear KV cache
- **Wake phase:** Prediction chỉ cần single forward pass, duy trì latency thấp
- **Fast weights:** Sử dụng State-Space Models (SSMs) như Gated Delta Networks để lưu trữ thông tin với fixed-size state
- **Trade-off:** Training cost tăng tuyến tính với N, nhưng inference latency không đổi
- **Biological analogy:** Tương tự hippocampal replay chuyển short-term memories thành long-term cortical weights
- **Hiệu quả:** Càng nhiều sleep loops (N) → deep reasoning càng tốt; cải thiện 47% trên GSM-Infinite 6-operation

## Related concepts

- [[memory-consolidation-offline]]
- [[state-space-models-ssm]]
- [[fast-weights]]
- [[kv-cache-eviction]]
- [[hippocampal-replay]]
- [[gated-delta-networks]]

## Sources

- [[src_llm-need-sleep-consolidation]]

## Notes
