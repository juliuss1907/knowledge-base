---
type: concept
status: draft
tags: [#coding, #productivity]
---
# GitHub Actions & CI/CD Pipeline

## Mô tả
Hệ thống tự động hóa quy trình build, test và deploy code, giúp tăng tốc độ phát triển và giảm sai sót con người.

## Chi tiết
- **CI (Continuous Integration):** Tự động tích hợp và test code mỗi khi có thay đổi.
- **CD (Continuous Deployment):** Tự động deploy code lên môi trường production sau khi pass test.
- **GitHub Actions Workflow:** 
    - Sử dụng file YAML trong `.github/workflows/`.
    - Có các trigger như `schedule` (cron), `push`, `pull_request`, và `workflow_dispatch` (manual).
    - Sử dụng Runner (Ubuntu, Windows, macOS) để thực thi các Step.
- **GitHub Pages:** Hosting tĩnh miễn phí, thường được dùng để deploy báo cáo hoặc documentation từ CI/CD pipeline.

## Liên quan
- [[Automation]]
- [[DevOps]]

## Nguồn tham khảo
- [[wiki/sources/src_github-actions-cicd.md]]
