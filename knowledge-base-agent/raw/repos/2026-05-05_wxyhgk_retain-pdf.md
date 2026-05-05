---
type: raw
source_type: repo
source_url: https://github.com/wxyhgk/retain-pdf
date_ingested: 2026-05-05
tags: [#coding, #ai]
status: unprocessed
---

# RetainPDF — PDF 保留排版翻译工具

**Owner:** wxyhgk  
**Repo:** retain-pdf  
**License:** MIT  
**Stars:** 1.4k  
**Forks:** 167  
**Link:** https://github.com/wxyhgk/retain-pdf

---

## Tóm tắt

**RetainPDF** là công cụ dịch PDF **giữ nguyên layout, công thức và cấu trúc** — đặc biệt cho tài liệu nghiên cứu khoa học và kỹ thuật.

---

## Vấn đề cần giải quyết

Các dự án open-source khác chủ yếu xử lý PDF **có thể copy, edit được**, và công thức inline đơn giản.

**RetainPDF** target:
- ✅ **PDF dạng ảnh/scan**
- ✅ **Công thức inline phức tạp**
- ✅ **Giữ nguyên layout sau dịch**
- ✅ **Tối ưu dung lượng PDF output**

---

## So sánh

| Tính năng | PDFMathTranslate | PolyglotPDF | Doc2X | **RetainPDF** |
|---|---|---|---|---|
| PDF scan | ❌ | ❌ | ✅ | ✅ |
| Công thức inline phức tạp | ❌ | ❌ | ✅ | ✅ |
| Code không dịch nhầm | ❌ | ❌ | ❌ | ✅ |
| Bảng biểu | Yếu | Yếu | Trung bình | ✅ Có thể tắt/bật |
| Custom translation strategy | Yếu | Yếu | Yếu | ✅ Cấu hình theo rule |
| Giữ layout | Trung bình | Trung bình | Mạnh | Mạnh |
| Nén PDF | Trung bình | Trung bình | Yếu | ✅ Liên tục tối ưu |
| API automation | ✅ | ✅ | ❌ | ✅ |

---

## Kiến trúc

**Full-stack, decoupled:**
- **Backend:** Python (OCR, translation, typesetting, delivery)
- **Frontend:** Web UI
- **Desktop:** Tauri/Electron app
- **OCR:** PaddleOCR / Rust OCR
- **Translation:** Multiple providers (configurable)

→ Dễ dùng, dễ extend, dễ thay thế module.

---

## Use cases

- SCI papers
- PDF scan/ảnh
- Sách kỹ thuật

---

## Deployment

| Cách | Platform |
|---|---|
| Desktop app | Windows (.exe), macOS (.dmg), Linux (.deb) |
| Docker | `docker compose up -d` → ports 40001 (web), 41000 (API), 42000 (sync) |

---

## Docker Images

- `wxyhgk/retainpdf-app`
- `wxyhgk/retainpdf-web`

---

## Community

- QQ Group: `1101779791`
