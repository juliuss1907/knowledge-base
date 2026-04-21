---
type: raw
source_type: repo
source_url: https://github.com/juliuss1907/camoufox
date_ingested: 2026-04-20
tags: [#coding, #ai, #research]
status: processed
processed_date: 2026-04-21
---
# Camoufox — Anti-detect Browser

## Tóm tắt

Camoufox là trình duyệt anti-detect mã nguồn mở, dựa trên Firefox được patch để spoof fingerprint và ẩn dấu vết automation. Intercepts data ở level C++ thay vì JavaScript — khiến mọi thay đổi trông như native code.

## Tính năng chính

**Ẩn dấu vết automation:**
- Playwright code bị sandbox hoàn toàn — trang web không thấy JS injection
- Sửa navigator.webdriver detection
- Không có main world execution leaks, frame execution context leaks

**Fingerprint spoofing:**
- Navigator properties (device, OS, browser, locale...)
- Screen size, resolution, viewport
- Geolocation, timezone, locale, Intl
- WebGL parameters, supported extensions, shader precision formats
- Font spoofing + chống font metrics fingerprinting
- WebRTC IP spoofing (protocol level)
- AudioContext, device voices, playback rates
- Battery API

**Anti-graphical fingerprinting:**
- WebGL parameters spoofing
- Font spoofing

**Di chuyển chuột như người thật:**
- Human-like mouse movement viết lại bằng C++

**Tối ưu:**
- Bỏ CSS animations, debloat Firefox
- Memory usage ~200MB
- Loại bỏ hầu hết Mozilla telemetry
- Bundled system fonts cho Windows, Mac, Linux

**Proxy integration:**
- Tự động tính toán geolocation, timezone, locale từ proxy

## Cách hoạt động

Dùng BrowserForge để generate fingerprints theo phân bố thống kê real-world traffic. Properties phải internally consistent — không thể có Windows UA với Apple M1 GPU.

## Nhược điểm

- Không hỗ trợ đầy đủ Chromium fingerprints (Spidermonkey engine behavior)
- 1 năm gap maintenance nên fingerprints có thể chưa hoàn hảo
- Vẫn có thể bị phát hiện với sophisticated fingerprint analysis

## Cài đặt

```bash
pip install camoufox
# hoặc prerelease
pip install cloverlabs-camoufox
python -m camoufox sync
```

## Links

- Website: https://camoufox.com
- PyPI: https://pypi.org/project/camoufox/
- Docs: https://camoufox.com/python/
