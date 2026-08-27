---
type: concept
status: draft
main_tag: tech
sub_tags: [tools]
topic: llm-consumption-modes
sources:
  - "[[src_10-questions-for-your-startup-developers]]"
last_updated: 2026-08-27
---

# LLM Consumption Modes

## Definition

Các chế độ thanh toán/consumption khi gọi model trên Gemini Agent Platform — Standard PayGo, Priority PayGo, và Provisioned Throughput — mỗi chế độ đánh đổi giữa giá, độ tin cậy và tính dự đoán được của traffic. Chọn sai chế độ là lỗi startup phổ biến, đặc biệt là mua Provisioned Throughput quá sớm.

## Key ideas

- **Standard PayGo (DSQ):** cho traffic giai đoạn đầu, low-QPS, spiky prototype. Watch out: 429 khi spike, không có reliability SLO
- **Priority PayGo:** cho bursty, revenue-critical traffic không chịu được 429. Giá ~1.8x standard token price. Là config change, không phải purchase order
- **Provisioned Throughput (PT):** cho steady, predictable, high-volume production traffic. Wasted spend nếu utilization dưới ~40%; overflow sang PayGo khi spike
- **Lỗi phổ biến nhất:** mua PT quá sớm — thường ngay tuần sau launch lớn khi cảm giác traffic chỉ tăng. PT là reserved capacity, trả tiền dù dùng hay không, chỉ bắt đầu đáng giá khi baseline thật sự predictable
- **Trình tự thực dụng:**
  - Tuần 1–4 trên Standard PayGo, đo shape request thật (tokens/min ở p50 và p99, bursts, batchable vs real-time)
  - 429 storm đầu tiên → bật Priority PayGo cho traffic quan trọng
  - Khi dự đoán được baseline TPM → mua PT cover baseline, phần trên overflow sang PayGo

## Related concepts

- [[dynamic-shared-quota]]
- [[batch-vs-live-inference]]
- [[cloud-cost-governance]]

## Sources

- [[src_10-questions-for-your-startup-developers]]

## Notes

