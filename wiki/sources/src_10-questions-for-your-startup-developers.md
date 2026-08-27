---
type: source
original: "[[2026-08-26_10-questions-for-your-startup-developers]]"
main_tag: tech
sub_tags: [tools, tutorial, hack]
topic: gcp-ai-startup-governance
date_compiled: 2026-08-27
url: https://cloud.google.com/blog/topics/developers-practitioners/10-questions-for-your-startup-developers
author: Google Cloud (Developers & Practitioners)
---

# 10 questions for your startup developers

## Metadata

- **Author:** Google Cloud (Developers & Practitioners)
- **Published:** [unknown]
- **Source:** Google Cloud blog
- **URL:** https://cloud.google.com/blog/topics/developers-practitioners/10-questions-for-your-startup-developers
- **Type:** article

## Summary

Bài viết của Google Cloud hướng dẫn các AI startup xây dựng ứng dụng trên nền tảng Gemini/Vertex AI, tập trung vào giai đoạn chuyển từ prototype sang production. Nội dung chia thành ba phase: Onboard (thiết lập project và identity đúng ngay từ đầu), Scale (lấy thêm throughput mà không phá vỡ ngân sách), và Govern (kiểm soát chi phí, secret và agent). Tác giả xác định những failure mode mặc định — API key bị lộ, migration từ AI Studio sang Agent Platform bị stall, HTTP 429 do quota — và đưa ra 10 câu hỏi kèm snippet thực thi được. Bài nhấn mạnh rằng vấn đề không phải là thiếu code mà là thiếu operational discipline: authentication đúng, chọn consumption mode phù hợp, và defense-in-depth cho agent.

## Key points

- **Ba phase quyết định tương lai startup:** Onboard (setup project/identity), Scale (throughput trong ngân sách), Govern (kiểm soát cost/key/agent)
- **AI Studio vs Agent Platform:** AI Studio (Gemini Developer API) là đường nhanh nhất từ ý tưởng đến code — browser IDE, API key, free tier. Agent Platform (trước đây là Vertex AI) có cùng model Gemini nhưng thêm enterprise controls: IAM, VPC Service Controls, Cloud Logging, reserved capacity
- **Thứ tự đúng là "cả hai, tuần tự":** prototype trên AI Studio trước, migrate sang Agent Platform trước khi có người dùng thật
- **Ba thao tác rút ngắn setup:** dùng project template opinionated (Cloud Setup checklist / Architecture Framework), batch-enable API, để Gemini chọn IAM role hẹp (quick nói "least privilege")
- **Auth hierarchy:** raw API keys chỉ dùng cho local prototyping; user credentials qua OAuth cho interactive tools/CLI; service accounts với least-privilege IAM cho server/container/scheduled job. Code lý tưởng không bao giờ thấy key — dùng Google Auth library đọc ADC
- **429 từ Agent Platform** gần như luôn do Dynamic Shared Quota (DSQ) ceiling hoặc gọi global endpoint khi cao điểm. Fix bằng cách pin regional endpoint + thêm retry/backoff với jitter (google-genai SDK tích hợp sẵn nhưng phải bật). Metric đúng để alert là `model_invocation_count` với label `error_category`
- **Ba consumption mode:** Standard PayGo (DSQ, cho traffic thấp/spiky), Priority PayGo (1.8x giá, cho traffic revenue-critical không chịu được 429), Provisioned Throughput (cho traffic ổn định, phí dù không dùng, overflow sang PayGo khi spike)
- **Nhiều workload là batch giả danh real-time:** nếu user chờ được "email khi xong" thì chuyển sang Batch prediction — queue riêng, không tốn interactive DSQ, giá ~50%
- **Ba lớp spend control:** spend cap budget (enforce, pause service), billing budget + Pub/Sub trigger tắt billing (mạnh nhưng nguy hiểm), quota overrides (cap cơ học)
- **Secrets:** dùng Secret Manager, không để trong .env/repo. Rotation theo schedule + detection (notification + Sensitive Data Protection). Với agent hành động thay user → dùng OAuth 2.0 short-lived access token + refresh flow, không bao giờ lưu token dài hạn
- **Agent cần defense-in-depth 4 lớp:** identity riêng cho agent (service account scoped), sandboxed code execution, prompt/response filtering (Model Armor), behavioral monitoring (Security Command Center)

## Concepts referenced

- [[gcp-ai-platform-migration]]
- [[cloud-auth-hierarchy]]
- [[dynamic-shared-quota]]
- [[llm-consumption-modes]]
- [[batch-vs-live-inference]]
- [[cloud-cost-governance]]
- [[secrets-management]]
- [[agent-defense-in-depth]]

## Original excerpts

> "The biggest reason startups stall on the migration to Agent Platform isn't the code — it's the operational leap from 'here's an API key' to a cloud project with folders, service accounts, org policies, logging, and IAM bindings."

> "Budgets only notify — you have to build your own brake pedal."

> "An agent that can call tools, browse the web, or execute code needs the same defense-in-depth thinking as any other production service — arguably more, because it makes decisions neither you nor the model can fully predict in advance."

> "You cannot build a 'warn me at 80% of my quota' alert for Standard PayGo. Under DSQ there is no fixed per-project number to be at 80% of."
