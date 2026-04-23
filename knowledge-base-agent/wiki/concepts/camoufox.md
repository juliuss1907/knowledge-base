---
type: concept
tags: [#ai, #coding, #research]
status: draft
sources:
  - src_camoufox
date_created: 2026-04-21
---

# Camoufox — Anti-detect Browser

## Tóm tắt

Trình duyệt anti-detect mã nguồn mở, dựa trên Firefox được patch để spoof fingerprint và ẩn dấu vết automation. Intercepts data ở level C++ thay vì JavaScript.

## Tính năng chính

**Ẩn dấu vết automation:**
- Playwright code bị sandbox hoàn toàn
- Sửa navigator.webdriver detection
- Không có main world execution leaks

**Fingerprint spoofing:**
- Navigator properties (device, OS, browser, locale...)
- Screen size, resolution, viewport
- Geolocation, timezone, locale, Intl
- WebGL parameters, supported extensions
- Font spoofing + chống font metrics fingerprinting
- WebRTC IP spoofing

**Human-like mouse movement** viết lại bằng C++

**Proxy integration:** Tự động tính toán geolocation, timezone, locale từ proxy.

## Nhược điểm

- Không hỗ trợ đầy đủ Chromium fingerprints
- 1 năm gap maintenance
- Vẫn có thể bị phát hiện với sophisticated fingerprint analysis

## Cài đặt

```bash
pip install camoufox
python -m camoufox sync
```

## Links

- Website: https://camoufox.com
- PyPI: https://pypi.org/project/camoufox/