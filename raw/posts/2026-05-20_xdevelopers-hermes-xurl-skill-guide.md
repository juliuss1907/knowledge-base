---
type: post
title: "X API + Hermes via xurl skill"
url: https://x.com/XDevelopers/status/2056871280599847054
author: Developers on X (@XDevelopers)
date_published: 2026-05-20
date_ingested: 2026-05-20
status: processed
compiled_at: 2026-05-21
compiled_to: [[wiki/sources/src_hermes-xurl-skill-guide.md]]
source: X / Twitter
---

# X API + Hermes via xurl skill

**Tác giả:** Developers on X (@XDevelopers)  
**Nguồn:** X / Twitter  
**Ngày đăng:** 2026-05-20

---

## Tổng quan

**Hermes** là open-source AI agent từ Nous Research chạy trong terminal. Out of the box có skill **xurl** cho phép agent đọc và viết lên X — posting, searching, pulling bookmarks, managing lists — tất cả qua natural language.

## Yêu cầu

| Item | Chi tiết |
|------|----------|
| OS | macOS hoặc Linux |
| Terminal | iTerm2, Ghostty, Terminal app, etc. |
| Subscription | Active SuperGrok subscription |
| X Developer App | OAuth 2.0 credentials từ developer.x.com |

## Bước 1: Cài đặt Hermes

```bash
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
```

Tải Hermes binary và đặt vào PATH. Sau khi xong, chạy `hermes` để xác nhận và bắt đầu setup wizard.

### Setup Wizard

```
How would you like to set up Hermes?
 → (●) Quick setup — provider, model & messaging (recommended)
   (○) Full setup — configure everything
```

**Quick setup** là đường nhanh nhất — cấu hình 3 thứ cần thiết: model provider, default model, messaging integration (Telegram/Discord).

### Chọn provider

Hermes hỗ trợ nhiều inference providers. Guide này dùng **xAI Grok OAuth**.

```
Select provider:
  (○) OpenRouter (100+ models, pay-per-use)
   ...
 → (●) **xAI Grok OAuth (SuperGrok Subscription)**
   (○) xAI (direct API key – legacy)
```

Khi chọn xAI Grok OAuth, Hermes tự động mở browser đến `api.x.ai`:
- Sign in với X account liên kết SuperGrok
- Approve permissions
- Hermes nhận tokens qua local callback → lưu tại `~/.hermes/auth.json` (auto-refresh)

### Chọn default model

```
Select default model:
->   grok-4.3
     ...
```

### Messaging (optional)

```
Connect a messaging platform? (Telegram, Discord, etc.)

   (○) Set up messaging now (recommended)
 → (●) Skip — set up later with 'hermes setup gateway'
```

### Xác nhận setup hoàn tất

```
✓ Setup complete! You're ready to go.

    Configure all settings:    hermes setup
    Connect Telegram/Discord:  hermes setup gateway
    Switch model/provider:     hermes model
```

## Bước 2: Cài đặt xurl

**xurl** là standalone CLI cho X API. Hermes dùng nó under the hood khi invoke xurl skill.

### Các cách cài đặt

```bash
# Shell script (no sudo, installs to ~/.local/bin)
curl -fsSL https://raw.githubusercontent.com/xdevplatform/xurl/main/install.sh | bash

# Homebrew (macOS)
brew install --cask xdevplatform/tap/xurl

# npm (requires Node.js)
npm install -g @xdevplatform/xurl

# Go (requires Go)
go install github.com/xdevplatform/xurl@latest
```

Nếu dùng shell script, cần thêm `~/.local/bin` vào PATH:

```bash
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

Xác nhận cài đặt: `xurl --help`

## Bước 3: Xác thực xurl

xurl cần OAuth 2.0 credentials từ X developer app.

### Tạo X developer app

1. Vào `developer.x.com`
2. Tạo new app (hoặc dùng existing)
3. Under **User authentication settings**, set redirect URI: `http://localhost:8080/callback`
4. Copy Client ID và Client Secret

### Register app với xurl

```bash
xurl auth apps add my-app \
  --client-id YOUR_CLIENT_ID \
  --client-secret YOUR_CLIENT_SECRET
```

### Authenticate qua OAuth

```bash
xurl auth oauth2 --app my-app
```

Mở browser cho OAuth flow → authorize app với X account.

> **Important:** Giữ flag `--app my-app`. Nếu skip `--app`, token có thể lưu vào default profile thay vì app chứa client credentials → API calls fail với 401 errors.

### Link specific username (nếu cần)

```bash
xurl auth oauth2 --app my-app YOUR_USERNAME
```

### Set default app và verify

```bash
xurl auth default my-app
xurl auth status
xurl whoami  # Should print your X username
```

## Bước 4: Sử dụng xurl trong Hermes

Start Hermes:

```bash
hermes
```

Sau khi vào, gõ `/help` để xem available commands. Bạn sẽ thấy `/xurl` trong list — đó là skill cần dùng.

Gõ `/xurl` để load skill. Hermes sẽ verify xurl đã install và authenticate.

### Các lệnh có thể làm

| Lệnh | Ví dụ |
|------|-------|
| **Post** | `post "Hello from Hermes"` |
| **Get bookmarks** | `get all of my bookmarks` |
| **Search** | `"search for posts about Hermes AI"` |
| **Get profile** | `"look up @username"` |
| **Reply** | `"reply to post 2047107136023650625 with 'great thread'"` |
| **Quote** | `"quote post 2047107136023650625 with my thoughts"` |
| **Like/unlike** | `"like post 2047107136023650625"` |
| **Manage bookmarks** | `"unbookmark 2047107136023650625"` |
| **Get timeline** | `"show my latest timeline"` |
| **Post with media** | `"post this image with the caption 'sunset'"` |

Vì Hermes là agent, bạn có thể chain actions trong một câu: *"search for posts about a topic, summarize them, and then draft a reply"* — tất cả trong một lần.

## Cấu trúc config

Tất cả config Hermes nằm trong `~/.hermes/`:

| File | Mục đích |
|------|----------|
| `config.yaml` | Main settings (model, provider, agent behavior) |
| `auth.json` | OAuth tokens — auto-managed |
| `.env` | API keys (XAI_API_KEY, etc.) |
| `cron/` | Scheduled tasks |
| `sessions/` | Chat history |
| `logs/` | Logs |

### Useful commands

```bash
hermes setup              # Re-run wizard
hermes setup model        # Change model/provider
hermes setup gateway      # Configure messaging
hermes setup tools        # Configure tool providers
hermes config             # View settings
hermes config edit        # Open in editor
hermes doctor             # Check issues
hermes model              # Change model
hermes auth add xai-oauth # Manual OAuth login
hermes auth list          # View stored credentials
hermes auth logout xai-oauth  # Remove OAuth credentials
```

## Troubleshooting

| Vấn đề | Giải pháp |
|--------|-----------|
| `xurl: command not found` | Thêm `~/.local/bin` vào PATH, restart Hermes |
| OAuth không complete | Confirm redirect URI đúng `http://localhost:8080/callback`. Đảm bảo port 8080 không bị chiếm |
| 401 errors sau OAuth | Chạy lại `xurl auth oauth2 --app my-app` rồi `xurl auth default my-app` |
| API key có non-ASCII characters | Copy lại từ provider dashboard |
| No active session | Re-run `xurl auth oauth2 --app my-app` |

## Tóm tắt quy trình

1. ✅ Cài Hermes với one-line script
2. ✅ Run setup wizard → chọn xAI Grok OAuth → browser login → chọn model
3. ✅ Cài xurl riêng
4. ✅ Authenticate xurl với X developer app credentials
5. ✅ Launch Hermes, load `/xurl`, bắt đầu tương tác với X qua natural language
