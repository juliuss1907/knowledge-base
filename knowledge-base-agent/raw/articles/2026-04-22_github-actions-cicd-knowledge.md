---
type: raw
source_type: article
source_url: local
date_ingested: 2026-04-22
tags: [#coding, #research]
status: unprocessed
---
# Tổng hợp kiến thức: GitHub Actions & CI/CD

## 1. GitHub Actions là gì?

GitHub Actions là hệ thống CI/CD (Continuous Integration / Continuous Deployment) được tích hợp sẵn trong GitHub. Nó cho phép bạn tự động hoá các tác vụ khi có sự kiện xảy ra trên repository.

Ví dụ: Mỗi ngày, GitHub Actions tự động chạy Horizon để fetch tin tức, dùng AI chấm điểm, rồi deploy báo cáo lên GitHub Pages.

### CI/CD là gì?

| Khái niệm | Giải thích | Ví dụ |
|---|---|---|
| CI (Continuous Integration) | Tự động build + test mỗi khi có code mới | Push code → server tự động chạy test |
| CD (Continuous Deployment) | Tự động deploy sau khi test thành công | Code pass test → tự động deploy lên production |

## 2. Cấu trúc một Workflow

Workflow là file YAML nằm trong `.github/workflows/`.

```yaml
name: Horizon Daily News Digest

on:
  schedule:
    - cron: '30 23 * * *'
  workflow_dispatch:
    inputs:
      batch:
        type: choice
        options: [morning, crypto, tech, f1, evening]

jobs:
  generate-digest:
    runs-on: ubuntu-latest
    permissions:
      contents: write

    steps:
      - name: Checkout repo
        uses: actions/checkout@v4

      - name: Run Horizon
        run: uv run horizon
```

## 3. Triggers

### 3.1 Schedule (Cron)

Cron expression: `phút giờ ngày_trong_tháng tháng ngày_trong_tuần`

| Cron | Ý nghĩa |
|---|---|
| 0 * * * * | Mỗi giờ, phút 0 |
| 0 8 * * 1-5 | 8:00 UTC, thứ 2 đến thứ 6 |
| */15 * * * * | Mỗi 15 phút |

### 3.2 Push / Pull Request

```yaml
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
```

### 3.3 Manual (workflow_dispatch)

Cho phép chạy thủ công từ GitHub UI.

## 4. Jobs & Steps

### Runner

| Runner | Hệ điều hành |
|---|---|
| ubuntu-latest | Ubuntu Linux |
| windows-latest | Windows |
| macos-latest | macOS |

### Step — 2 loại

**Dùng Action (uses):**
```yaml
- name: Setup Python
  uses: actions/setup-python@v5
  with:
    python-version: '3.11'
```

**Chạy lệnh (run):**
```yaml
- name: Run Horizon
  run: uv run horizon --hours 8
```

## 5. Variables & Secrets

### Secrets — Dữ liệu nhạy cảm

Thêm tại: Repository Settings → Secrets → Actions

```yaml
- name: Run Horizon
  env:
    MINIMAX_API_KEY: ${{ secrets.MINIMAX_API_KEY }}
  run: uv run horizon
```

## 6. GitHub Pages

GitHub Pages là dịch vụ hosting tĩnh miễn phí của GitHub.

```yaml
- name: Deploy to GitHub Pages
  uses: peaceiris/actions-gh-pages@v4
  with:
    github_token: ${{ secrets.GITHUB_TOKEN }}
    publish_dir: ./data/summaries
```

URL: `https://juliuss1907.github.io/Horizon/filename.md`

## 7. Git commands

| Lệnh | Ý nghĩa |
|---|---|
| git add <file> | Đánh dấu file để commit |
| git commit -m "msg" | Lưu thay đổi vào lịch sử |
| git push origin main | Đẩy commit lên GitHub |
| git pull --rebase origin main | Kéo thay đổi từ remote + đặt commit local lên trên |
| git stash | Cất tạm thay đổi chưa commit |
| git stash pop | Lấy lại thay đổi đã cất |
| git reset --hard origin/main | Reset về đúng trạng thái remote |

### Detached HEAD

Fix:
```bash
git checkout -f main
git reset --hard origin/main
```

## 8. Kiến trúc tổng thể

```
┌─── MÁY WINDOWS ───────────────────────────────┐
│ D:\Code Space\Lab\Horizon │
│ Edit configs + workflow → git push → GitHub │
└─────────────────┬────────────────────────────────┘
                  │
                  ▼
┌─── GITHUB (Cloud) ─────────────────────────────┐
│ GitHub Actions (Cron 5 lần/ngày) │
│ Horizon: fetch → AI score → summarize │
│ GitHub Pages (Static hosting) │
└─────────────────┬────────────────────────────────┘
                  │
                  ▼
┌─── VPS LINUX ──────────────────────────────────┐
│ OpenClaw Gateway │
│ Cron Jobs (10 jobs) │
│ Telegram Bot (long polling) │
└─────────────────┬────────────────────────────────┘
                  │
                  ▼
┌─── TELEGRAM ───────────────────────────────────┐
│ Julius nhận digest 📱 │
└─────────────────────────────────────────────────┘
```

## 9. Tổng kết

| Kiến thức | Đã thực hành |
|---|---|
| GitHub Actions | Tạo workflow, cron schedule, deploy GitHub Pages |
| CI/CD | Auto build + deploy pipeline |
| GitHub Pages | Host static files, deploy từ gh-pages branch |
| Git | push, pull, rebase, stash, reset, fix conflict |
| YAML | Viết workflow config |
| JSON | Viết Horizon config, OpenClaw cron jobs |
| Cron expressions | Schedule cho cả GitHub Actions và OpenClaw |
| API | MiniMax AI API, CoinGecko API |
| OpenClaw | Cron system, Telegram delivery, web fetch |
