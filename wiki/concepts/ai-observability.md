---
type: concept
status: draft
main_tag: ai
sub_tags: [tools, automation]
topic: ai-observability
sources:
  - "[[src_posthog]]"
last_updated: 2026-08-31
---

# AI Observability

## Definition

AI observability là bộ công cụ và phương pháp theo dõi, đo lường hiệu suất của LLM-powered applications trong production. PostHog cung cấp khả năng capture traces, generations, latency và cost cho ứng dụng dùng LLM. Do output của LLM không đoán trước được và có chi phí/latency riêng, AI observability khác với observability truyền thống: cần theo dõi model performance, phát hiện drift, và phản ứng với model failures cùng security incidents như adversarial prompt injections.

## Key ideas

- **Capture toàn diện:** Traces, generations, latency, cost cho LLM-powered app
- **Khác biệt với observability truyền thống:** Do unpredictability, cost và latency đặc thù của LLM
- **Phát hiện vấn đề sớm:** Drift detection, model failures, prompt injection incidents
- **Tích hợp nền tảng:** Nằm trong cùng hệ sinh thái với product analytics
- **Tối ưu cost/latency:** Hỗ trợ quyết định model choice, distillation, fine-tuning

## Related concepts

- [[self-driving-products]]
- [[product-analytics]]
- [[ai-evals]]

## Sources

- [[src_posthog]]

## Notes