---
type: concept
status: draft
main_tag: tech
sub_tags: [tools, hack]
topic: dynamic-shared-quota
sources:
  - "[[src_10-questions-for-your-startup-developers]]"
last_updated: 2026-08-27
---

# Dynamic Shared Quota

## Definition

Dynamic Shared Quota (DSQ) là cơ chế quota của Gemini Agent Platform dùng một pool chia sẻ có kích thước dựa trên lịch sử project — không có con số cố định per-project. Project mới bắt đầu với giới hạn khiêm tốn có chủ đích để ngăn chặn abuse trên nền tảng. Hệ quả: bạn không thể build alert "cảnh báo ở 80% quota" vì không tồn tại một con số để đo.

## Key ideas

- **429 gần như luôn do hai nguyên nhân:** chạm DSQ ceiling của tier project, hoặc gọi global endpoint khi global demand spike phải cạnh tranh dung lượng
- **Fix nhanh hơn ticket tăng quota:**
  - **Pin regional endpoint** — hơn nửa traffic startup mặc định dùng global routing; pin region (như us-central1) tránh contention, cải thiện latency. (Ngoại lệ: Priority PayGo hiện chỉ có trên `global`)
  - **Retry + backoff với jitter** — 429 là retryable; dùng google-genai SDK tích hợp sẵn. Tránh decorator `google.api_core.retry.if_transient_error` (cũ, không nhận `google.genai.errors.APIError`, sẽ âm thầm bỏ qua 429)
- **Metric đúng để alert:** `aiplatform.googleapis.com/publisher/online_serving/model_invocation_count` với label `error_category` = `user`/`system`/`capacity`. Alerting trên `capacity` phân tách throttling thật khỏi bad request của bạn (mà raw 429 count không làm được)
- **DSQ không có per-project fixed number** — percent-of-limit alerting chỉ ý nghĩa khi đã lên Provisioned Throughput (có real limit metrics)
- **Quota overrides** (đặt per-model, per-region dưới platform default) là lớp cơ học chặn cost tích tụ — key bị lộ không thể burn thứ quota từ chối phục vụ

## Related concepts

- [[llm-consumption-modes]]
- [[batch-vs-live-inference]]
- [[cloud-cost-governance]]

## Sources

- [[src_10-questions-for-your-startup-developers]]

