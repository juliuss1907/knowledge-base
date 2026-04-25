---
type: source
source_url: https://github.com/Infisical/agent-vault
date_ingested: 2026-04-24
tags: [#coding, #security]
---
# Infisical/agent-vault

Một công cụ quản lý credentials cho AI Agents dưới dạng HTTP proxy.

## Key Points
- **Vấn đề**: AI agents dễ bị prompt injection $\rightarrow$ rò rỉ secrets nếu credentials được cung cấp trực tiếp cho agent.
- **Giải pháp**: Agent Vault đóng vai trò là proxy trung gian. Agent gửi request qua proxy $\rightarrow$ Vault inject credentials ở network layer $\rightarrow$ Credentials không bao giờ quay trở lại agent.
- **Đặc điểm chính**:
    - **Brokered Access**: Cấp quyền truy cập thay vì cung cấp thông tin truy cập.
    - **Khả năng tương thích**: Hoạt động với mọi agent (Claude Code, Cursor, OpenClaw, v.v.).
    - **Bảo mật**: Mã hóa AES-256-GCM, Argon2id cho master password.
    - **Giám sát**: Log chi tiết mọi request (method, host, path, status, latency).
- **Triển khai**: Hỗ trợ cài đặt qua script, Docker, hoặc SDK cho các agent chạy trong sandbox (E2B, Daytona).
- **Tech stack**: Go (backend), TypeScript (SDK), MIT License.
