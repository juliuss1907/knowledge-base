---
type: raw
source_type: repo
source_url: https://github.com/niri-wm/niri/releases/tag/v26.04
date_ingested: 2026-04-26
tags: [#coding, #linux, #productivity]
status: processed
processed_date: 2026-04-27
---
# Niri v26.04 — Wayland Compositor

## Thông tin cơ bản

Niri là scrollable-tiling Wayland compositor cho Linux. Windows xếp theo columns trên một strip vô hạn sang phải. Mở window mới không làm existing windows bị resize.

**Repo:** https://github.com/niri-wm/niri
**Stars:** 20,000+ (đạt hồi tháng 2/2026)
**Language:** Rust
**License:** GPL

---

## Điểm chính v26.04

### 1. Chuyển sang GitHub Organization
- Repo chuyển từ tài khoản cá nhân @YaLTeR sang github.com/niri-wm
- Lý do: cho phép assign issue triage permissions cho cộng đồng
- Cảm ơn @Sempyos đã triage tất cả issues và PRs
- Đạt 20,000 stars hồi tháng 2

### 2. Blur — tính năng được request nhiều nhất

**Blur giờ đã có trong mainline!**

Hai loại blur:
- **Xray blur** (mặc định): blur wallpaper phía sau, rất hiệu quả vì tính 1 lần rồi reuse như static image. Chỉ recompute khi wallpaper đổi.
- **Non-xray blur**: blur pixels thật của window — tốn kém hơn vì đọc lại pixels sau khi render mỗi frame.

**Cách bật blur trong config:**
```niri
window-rule {
  match app-id="^Alacritty$"
  background-effect { blur true }
}
```

**Apps đã hỗ trợ ext-background-effect:**
- foot terminal v1.26 (set `blur=true` trong colors config)
- kitty terminal v0.46.2 (set `background_blur 1`)
- Ghostty terminal (sẽ có trong v1.4)
- Dank Material Shell v1.4.5
- Noctalia shell
- Vicinae launcher
- Quickshell (sẽ có trong v0.3)
- winit (sẽ có trong v0.31)

**Tính năng liên quan:**
- Xray blur có thể dùng một mình, không cần blur (để hiệu ứng wallpaper đẹp)
- Pop-up menus giờ configure được transparency và background effects riêng

### 3. Packagers update
- Minimum Rust version: 1.85
- `niri.service` không còn hardcode `/usr/bin/` trong binary path
- @markK24 đã restructure dinit service files

---

## Niri khác gì các tiling WM khác

Không giống bspwm, i3, sway — niri dùng **scrollable tiling**: các windows xếp theo chiều ngang vô hạn, không chia viewport. Strip kéo dài sang phải và cuộn được.

---

## Thông tin thêm
- [awesome-niri](https://github.com/niri-wm/awesome-niri) — list các project liên quan
- [artwork repo](https://github.com/niri-wm/artwork) — wallpaper và logo
