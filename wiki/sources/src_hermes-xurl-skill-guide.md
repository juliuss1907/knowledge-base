---
type: source
original: "[[raw/posts/2026-05-20_xdevelopers-hermes-xurl-skill-guide.md]]"
main_tag: ai
sub_tags: [tools, tutorial, automation]
topic: hermes-xurl-x-api-integration
date_ingested: 2026-05-20
date_compiled: 2026-05-21
url: https://x.com/XDevelopers/status/2056871280599847054
author: Developers on X (@XDevelopers)
---

# X API + Hermes via xurl skill

## Metadata

- **Author:** Developers on X (@XDevelopers)
- **Published:** 2026-05-20
- **Source:** X / Twitter
- **URL:** https://x.com/XDevelopers/status/2056871280599847054
- **Type:** post

## Summary

Hướng dẫn cài đặt và sử dụng skill xurl trong Hermes Agent — cho phép agent đọc và viết lên X (Twitter) qua natural language. Hướng dẫn bao gồm: cài đặt Hermes, cấu hình xAI Grok OAuth, cài đặt xurl CLI, xác thực X API, và các lệnh xurl trong Hermes.

## Key points

- **Hermes** là open-source AI agent từ Nous Research chạy trong terminal
- **xurl** là standalone CLI cho X API — Hermes dùng nó under the hood khi invoke skill
- **Yêu cầu:** macOS/Linux, SuperGrok subscription, X Developer App với OAuth 2.0 credentials
- **Cài đặt Hermes:** One-line curl script → quick setup wizard → chọn xAI Grok OAuth → browser login → auto-save tokens tại `~/.hermes/auth.json`
- **Cài đặt xurl:** 4 options (shell script, Homebrew, npm, Go) — shell script cài vào `~/.local/bin`
- **Xác thực xurl:** Tạo X developer app → set redirect URI `http://localhost:8080/callback` → OAuth flow qua browser → link to specific username
- **Lệnh xurl trong Hermes:** Post, get bookmarks, search, lookup profile, reply, quote, like/unlike, timeline, post with media
- **Chain actions:** Hermes agent có thể "search → summarize → draft reply" trong một lần
- **Config location:** Tất cả trong `~/.hermes/` — config.yaml, auth.json, .env, cron/, sessions/, logs/
- **Troubleshooting:** PATH issues, OAuth completion, 401 errors (sử dụng `--app` flag), port conflicts

## Concepts referenced

- [[hermes-agent]]
- [[xurl-cli]]
- [[x-api-oauth2]]
- [[supergrok-subscription]]
- [[nous-research]]

## Original excerpts