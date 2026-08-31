---
type: concept
status: draft
main_tag: tech
sub_tags: [tools, automation]
topic: self-driving-products
sources:
  - "[[src_posthog]]"
last_updated: 2026-08-31
---

# Self-Driving Products

## Definition

Self-driving products là mô hình sản phẩm tự chủ động chẩn đoán vấn đề, khám phá cơ hội và đưa ra giải pháp dựa trên dữ liệu product — thay vì chờ developer tìm ra. PostHog tiên phong với chế độ "self-driving mode": tín hiệu từ product data (errors, rage clicks, failed queries, và nhiều hơn) được chuyển thành researched reports và pull requests mà developer chỉ cần review và merge. Đây là bước dịch chuyển từ "reactive analytics" (con người query dữ liệu) sang "proactive product automation" (dữ liệu drive hành động).

## Key ideas

- **Tín hiệu dữ liệu → hành động:** Errors, rage clicks, failed queries tự động chuyển thành reports và PR có thể review
- **Vòng lặp khép kín:** Phát hiện vấn đề → research → đề xuất fix → con người merge
- **Bộ công cụ nền tảng:** Product analytics, session replay, feature flags, experiments, error tracking, logs, surveys, data warehouse, pipelines, AI observability
- **Phản ứng nhanh với lỗi:** Phát hiện và đề xuất fix sớm hơn so với chờ issue report
- **Điều khiển đa nơi:** Slack, web, desktop, MCP (đưa vào Claude Code/Cursor)

## Related concepts

- [[product-analytics]]
- [[ai-observability]]
- [[ai-vulnerability-discovery]]

## Sources

- [[src_posthog]]

## Notes