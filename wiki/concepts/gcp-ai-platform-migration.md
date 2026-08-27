---
type: concept
status: draft
main_tag: tech
sub_tags: [tools, tutorial]
topic: gcp-ai-platform-migration
sources:
  - "[[src_10-questions-for-your-startup-developers]]"
last_updated: 2026-08-27
---

# GCP AI Platform Migration

## Definition

Quá trình chuyển ứng dụng AI từ Google AI Studio (Gemini Developer API) sang Gemini Enterprise Agent Platform (trước đây là Vertex AI) — bước đệm do startup cần khi prototype muốn trở thành production thật. Đây không chỉ là đổi endpoint mà là bước nhảy operational từ "có một API key" lên cloud project đầy đủ với folders, service accounts, org policies, logging và IAM bindings.

## Key ideas

- **AI Studio vs Agent Platform:** hai surface cùng dùng family model Gemini nhưng giải quyết bài toán khác nhau. AI Studio là đường nhanh nhất ý tưởng → code (browser IDE, API key, free tier); Agent Platform thêm enterprise controls: IAM + service-account auth, VPC Service Controls, Cloud Logging/Monitoring, reserved capacity, regional endpoints, compliance
- **Nguy hiểm là coi chúng thay thế được:** model key đơn giản của AI Studio không translate sang enterprise controls; IAM của Agent Platform trông như overkill cho tới ngày cứu bạn khỏi incident stolen-credential
- **Thứ tự đúng:** prototype trên AI Studio trước, migrate trước khi có user thật — không phải khi nó hỏng
- **Rút ngắn setup bằng opinionated project template:** Cloud Setup checklist + Architecture Framework cho sẵn folder hierarchy (prod/non-prod/dev), central logging + monitoring project, Security Command Center, baseline org policies
- **Trigger migration:** key đã rời laptop (repo/Slack/mobile app), team hơn một người, chi tiêu vài trăm USD/tháng, sắp onboard khách trả tiền
- **Solo founder:** tránh build trong personal GCP account — tạo organization đúng rồi mới tạo project bên trong
- **Unified SDK:** `google-genai` target cả hai surface

## Related concepts

- [[cloud-auth-hierarchy]]
- [[dynamic-shared-quota]]
- [[llm-consumption-modes]]

## Sources

- [[src_10-questions-for-your-startup-developers]]

## Notes

