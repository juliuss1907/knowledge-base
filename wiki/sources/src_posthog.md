---
type: source
original: "[[2026-08-30_PostHog_posthog]]"
main_tag: tech
sub_tags: [tools, automation]
topic: self-driving-products
date_compiled: 2026-08-31
url: https://github.com/PostHog/posthog
author: PostHog
---

# PostHog

## Metadata

- **Author:** PostHog
- **Published:** [unknown]
- **Source:** github.com
- **URL:** https://github.com/PostHog/posthog
- **Type:** repo

## Summary

PostHog là nền tảng open-source để xây dựng "self-driving products" — sản phẩm tự chẩn đoán vấn đề, khám phá cơ hội và ship fixes. Nó cung cấp bộ công cụ toàn diện: product analytics, web analytics, session replays, feature flags, experiments, error tracking, logs, surveys, data warehouse, data pipelines, AI observability và workflows. Điểm đặc biệt là chế độ "self-driving mode" chuyển tín hiệu từ product data (errors, rage clicks, failed queries) thành các research reports và pull requests mà developer chỉ cần review và merge. Toàn bộ có thể điều khiển từ Slack, web, desktop hoặc qua MCP. Có bản cloud free tier hào phóng và bản self-host open-source (MIT).

## Key points

- **Self-driving mode:** Tín hiệu trong product data (errors, rage clicks, failed queries) được chuyển thành researched reports và pull requests để review/merge
- **Product analytics:** Autocapture hoặc manual instrumentation event-based analytics, phân tích bằng visualization hoặc SQL
- **Session replays:** Xem lại session thật của user để chẩn đoán issue và hiểu hành vi
- **Feature flags + Experiments:** Roll out an toàn và đo statistical impact, hỗ trợ no-code setup
- **AI observability:** Capture traces, generations, latency, cost cho LLM-powered app
- **Data warehouse + pipelines:** Sync dữ liệu từ Stripe/Hubspot... và chạy transformations, export real-time hoặc batch
- **Workflows:** Tự động hóa hành động hoặc gửi message tới user
- **Điều khiển đa nơi:** Slack, web, desktop (PostHog Desktop), hoặc editor riêng qua MCP
- **Free tier:** 1M events, 5k recordings, 1M flag requests, 100k exceptions, 1500 survey responses miễn phí mỗi tháng
- **Self-host:** Deploy hobby instance 1 lệnh Docker (~4GB memory), scale ~100k events/tháng rồi nên migrate sang cloud

## Concepts referenced

- [[self-driving-products]]
- [[product-analytics]]
- [[ai-observability]]

## Original excerpts

> "Self-driving mode: Turn signals in your product data (errors, rage clicks, failed queries, and more) into researched reports and pull requests you review and merge."
