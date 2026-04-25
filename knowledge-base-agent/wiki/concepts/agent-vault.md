---
type: concept
status: draft
tags: [#coding, #security]
---
# Agent Vault

## Mô tả
Agent Vault là một giải pháp quản lý bí mật (secrets management) chuyên biệt dành cho các AI agents. Thay vì cung cấp API keys hoặc credentials trực tiếp cho mô hình AI (điều này gây rủi ro rò rỉ dữ liệu qua prompt injection), Agent Vault hoạt động như một HTTP proxy trung gian. Khi agent thực hiện một yêu cầu API, yêu cầu đó sẽ đi qua vault; tại đây, vault sẽ tự động chèn (inject) các credentials cần thiết vào header của request ở tầng mạng trước khi gửi đến đích. Kết quả là agent có thể thực hiện tác vụ nhưng không bao giờ thực sự "biết" hoặc "nhìn thấy" các secret keys.

## Liên quan
- #coding
- #security

## Nguồn tham khảo
- [Infisical/agent-vault](https://github.com/Infisical/agent-vault)
