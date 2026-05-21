---
type: concept
status: draft
main_tag: tech
sub_tags: [tools, automation]
topic: hermes-xurl-x-api-integration
sources:
  - [[wiki/sources/src_hermes-xurl-skill-guide.md]]
last_updated: 2026-05-21
---

# xurl CLI

## Definition

xurl là standalone CLI (command-line interface) cho X (Twitter) API, cho phép tương tác với X qua terminal: posting, searching, pulling bookmarks, managing lists. Hermes Agent dùng xurl under the hood khi invoke xurl skill.

## Key ideas

- **Tác giả:** X Developers / X Developer Platform
- **Các cách cài đặt:**
  - Shell script (no sudo, `~/.local/bin`)
  - Homebrew (`brew install --cask xdevplatform/tap/xurl`)
  - npm (`npm install -g @xdevplatform/xurl`)
  - Go (`go install github.com/xdevplatform/xurl@latest`)
- **Xác thực:** OAuth 2.0 — cần X Developer App với Client ID, Client Secret, redirect URI `http://localhost:8080/callback`
- **Lưu ý quan trọng:** Sử dụng `--app my-app` flag khi authenticate, nếu không token lưu vào default profile thay vì app → API calls fail với 401
- **Lệnh xurl:** Post, get bookmarks, search, lookup profile, reply, quote, like/unlike, manage bookmarks, get timeline, post with media
- **Integration:** Được sử dụng bởi Hermes Agent qua `/xurl` skill

## Related concepts

- [[hermes-agent]]
- [[x-api-oauth2]]

## Sources

- [[wiki/sources/src_hermes-xurl-skill-guide.md]]

## Notes