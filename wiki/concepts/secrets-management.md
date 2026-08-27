---
type: concept
status: draft
main_tag: tech
sub_tags: [tools, hack]
topic: secrets-management
sources:
  - "[[src_10-questions-for-your-startup-developers]]"
last_updated: 2026-08-27
---

# Secrets Management

## Definition

Quy trình lưu trữ, xoay vòng và phát hiện rò rỉ secret (API keys, tokens) trong hệ thống AI — thay cho thói quen để trong .env files hoặc repository. Với agent hành động thay user, nguyên tắc còn chặt hơn: không bao giờ lưu long-lived token, dùng OAuth 2.0 với short-lived access token + refresh flow.

## Key ideas

- **Secret Manager thay cho .env/repo:** lưu secret ở Secret Manager, cấp read access qua IAM chỉ cho service account cần nó. Không bao giờ để trong environment variables, .env files, hoặc repo
- **Rotation** — theo schedule và khi nghi ngờ. Secret Manager versions rẻ — coi như immutable, roll forward
- **Detection khi leak** — Secret Manager notifications + Google Cloud Sensitive Data Protection bắt key check vào repo hoặc log stream trước khi attacker
- **Hai kỷ luật tự trả tiền lần đầu dùng** — rotation + detection, áp dụng ngay từ ngày đầu chứ không chờ tới lúc leak
- **Agent hành động thay user (gọi Gmail, đọc Drive, hit SaaS với credential user):** không lưu long-lived token — dùng OAuth 2.0 short-lived access token + refresh flow. Khi user rage-quit hoặc account bị revoke, agent mất access cùng lúc
- **Kinh tế của rò rỉ:** key Gemini lộ từ repo công khai dùng để chạy distillation attack có thể tích vài chục nghìn đô trước khi chủ thấy billing alert đầu tiên

## Related concepts

- [[cloud-auth-hierarchy]]
- [[cloud-cost-governance]]
- [[oauth-security-risks]]

## Sources

- [[src_10-questions-for-your-startup-developers]]

