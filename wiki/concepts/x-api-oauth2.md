---
type: concept
status: draft
main_tag: tech
sub_tags: [tools, tutorial]
topic: hermes-xurl-x-api-integration
sources:
  - [[wiki/sources/src_hermes-xurl-skill-guide.md]]
last_updated: 2026-05-21
---

# X API OAuth 2.0

## Definition

X API OAuth 2.0 là phương thức xác thực để ứng dụng third-party (như Hermes Agent qua xurl) truy cập X (Twitter) API. Yêu cầu X Developer App với Client ID, Client Secret, và redirect URI được cấu hình đúng.

## Key ideas

- **Requirements:** X Developer account, OAuth 2.0 credentials, redirect URI `http://localhost:8080/callback`
- **Flow:**
  1. Tạo app tại developer.x.com
  2. Cấu hình User authentication settings với redirect URI
  3. Copy Client ID và Client Secret
  4. Register app với xurl: `xurl auth apps add my-app --client-id ... --client-secret ...`
  5. OAuth flow: `xurl auth oauth2 --app my-app` → mở browser → authorize → tokens auto-save
- **Auto-refresh:** Tokens tự động refresh, lưu tại `~/.hermes/auth.json` (Hermes) hoặc xurl config
- **Hermes integration:** Hermes tự động mở browser cho xAI Grok OAuth, lưu tokens và refresh
- **Lưu ý:** Sử dụng `--app` flag để tránh 401 errors; có thể link specific username

## Related concepts

- [[xurl-cli]]
- [[hermes-agent]]

## Sources

- [[wiki/sources/src_hermes-xurl-skill-guide.md]]

## Notes