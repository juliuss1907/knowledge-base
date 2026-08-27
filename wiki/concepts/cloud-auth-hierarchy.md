---
type: concept
status: draft
main_tag: tech
sub_tags: [tools, hack]
topic: cloud-auth-hierarchy
sources:
  - "[[src_10-questions-for-your-startup-developers]]"
last_updated: 2026-08-27
---

# Cloud Auth Hierarchy

## Definition

Thứ bậc an toàn của các phương thức xác thực trên Google Cloud — từ dễ nhất tới an toàn nhất: raw API keys, user credentials qua OAuth, và service accounts với least-privilege IAM roles. Mục tiêu cuối cùng là code không bao giờ nhìn thấy key trực tiếp, chỉ đọc Application Default Credentials (ADC) từ môi trường.

## Key ideas

- **Raw API keys:** chỉ cho local prototyping. Nguy hiểm trong production vì long-lived, dễ lộ vào client bundle/public repo, cấp truy cập không giới hạn tới khi phát hiện
- **User credentials qua OAuth (ADC):** phù hợp cho interactive tools, CLIs, code trên laptop developer
- **Service accounts + least-privilege IAM roles:** đúng cho mọi thứ chạy trên server, container, hoặc scheduled job. Thường chỉ cần `roles/aiplatform.user`, không phải role admin rộng hơn
- **Mục tiêu pattern:** code gọi Google Auth library, library tự đọc ADC môi trường — short-lived token minted cho service account gắn với Cloud Run/GKE workload/Compute Engine VM
- **Google Auth library** đọc ADC từ môi trường, loại bỏ key khỏi codebase
- **Least privilege > convenience:** "Say least privileged / narrowest access" khi dùng Gemini role picker để trả về granular roles thay vì Admin/Editor/Viewer mặc định

## Related concepts

- [[gcp-ai-platform-migration]]
- [[secrets-management]]
- [[oauth-security-risks]]

## Sources

- [[src_10-questions-for-your-startup-developers]]

## Notes

