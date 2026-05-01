---
type: raw
source_type: article
source_url: 
date_ingested: 2026-05-01
tags: [#ai, #productivity]
status: unprocessed
---

# Giải thích chi tiết hệ thống 8 thành phần di động trong AI

**Nguồn:** Giải thích từ bài viết của Gideon Ng về "Thoát khỏi cuộc chiến chi phí AI"  
**Ngày:** 2026-05-01

---

## 1. Context cá nhân (Personalised context)

**Là gì:** Một hệ thống file chứa toàn bộ "bối cảnh" về bạn — who you are, what you do, how you think.

**Ví dụ thực tế:**
```
~/knowledge-base/
├── Context/
│   ├── Learning/          # Bạn đang học gì
│   ├── Custom_Prompts/    # Cách bạn thích AI trả lờI
│   ├── Vibe_Coding/       # Style coding của bạn
│   └── Reference_Material/# TàI liệu tham khảo
```

**Tác dụng:** Khi switch sang model mớI, chỉ cần nói "đọc folder Context" — model đó biết ngay bạn là ai, đang focus lĩnh vực gì, thích output như thế nào. Không cần explain lạI từ đầu.

---

## 2. Own your keys (BYOK - Bring Your Own Keys)

**Là gì:** Dùng API keys riêng thay vì subscribe qua nền tảng. Cho phép chuyển đổi provider dễ dàng.

**Ví dụ:**
- Thay vì mua Claude Pro $20/tháng → Dùng Anthropic API key
- Thay vì ChatGPT Plus → Dùng OpenAI API key
- Hoặc dùng aggregator như OpenRouter, Together AI

**Tác dụng:**
- Chuyển model trong cùng một chat: "Switch sang Gemini đi"
- Không bị lock-in vào một nhà cung cấp
- Tính cost theo usage thực tế, không phảI flat fee

---

## 3. Requests (Input commands)

**Là gì:** Cách bạn ra lệnh cho AI — có thể là voice hoặc text.

**Ví dụ:**
```
❌ "Viết giúp tôi một bàI về AI" (vague)

✅ "@skill-summarize-article https://techcrunch.com/..." 
    → AI biết phảI invoke skill cụ thể

✅ Voice: "Thêm bàI này vào knowledge base vớI tag #ai"
```

**Key point:** Requests rõ ràng → AI biết phảI làm gì, không phảI đoán.

---

## 4. Thought processor (LLM as brain)

**Là gì:** LLM đóng vai trò "bộ não" — nhận input từ Requests, process thông qua Context, rồI cho output.

**Ví dụ workflow:**
```
Input: "Tóm tắt bàI này"
    ↓
[Thought processor nhận input]
    ↓
Đọc Context/Learning/ để biết Julius focus gì
    ↓
Đọc article content
    ↓
Tóm tắt theo style Julius thích (ngắn, tiếng Việt, không bullet point)
    ↓
Output: Bản tóm tắt phù hợp
```

---

## 5. Actionable workflows (Skills)

**Là gì:** Các workflow có thể lặp lạI, được viết thành SOP (Standard Operating Procedure) trong file `.md`.

**Ví dụ Skills của bạn hiện tạI:**
- `skill-summarize-article.md` — Tóm tắt bàI viết
- `skill-ingest-to-raw.md` — Lưu vào raw folder
- `skill-compile-concept.md` — Compile sang wiki

**Cấu trúc một Skill:**
```markdown
# Skill: Tóm tắt bàI viết

## Trigger
Khi Julius gửI link bàI viết

## Steps
1. Fetch content từ URL
2. Đọc Context/Learning/ để biết focus
3. Tóm tắt bằng tiếng Việt, ngắn gọn
4. Lưu vào raw/articles/

## Output format
- Tiêu đề
- Tóm tắt 3-5 bullet
- Tags phù hợp
```

---

## 6. Building capabilities (MCPs/APIs)

**Là gì:** Kết nốI AI vớI thế giớI bên ngoàI thông qua tools.

**Ví dụ:**
- **MCP filesystem:** Cho phép AI đọc/ghi files trong máy
- **MCP web fetch:** Lấy content từ URLs
- **API DeBank:** Lấy onchain data
- **API Telegram:** GửI messages

**Trong hệ thống của anh:**
- `web_fetch` + `web_search` để lấy thông tin
- `read/write/edit` để quản lý files
- `cron` để schedule tasks

---

## 7. Link across devices (Sync)

**Là gì:** Đồng bộ toàn bộ hệ thống qua nhiều thiết bị.

**Ví dụ:**
- Git repo cho `knowledge-base/` → Sync qua laptop, desktop, cloud
- Telegraph/Telegram Bot → Truy cập từ phone
- VS Code + Claude Code → Làm việc trên desktop

**Key point:** Data là của bạn, không bị khóa vào một device.

---

## 8. Edit and manage (Markdown editor)

**Là gì:** Dùng markdown editor để quản lý toàn bộ hệ thống.

**Ví dụ:**
- **Obsidian:** Quản lý knowledge base vớI graph view
- **VS Code:** Edit code + skills
- **Telegram:** Quick notes và requests

**TạI sao markdown:**
- Plain text → không bị lock-in vào app nào
- Easy to version control (git)
- AI đọc hiểu dễ dàng

---

## Tóm lại: TạI sao 8 thành phần này quan trọng

| Vấn đề | Giải pháp |
|---|---|
| Rate limits tăng | Skills tiết kiệm token bằng cách automate workflows |
| Model providers đổi giá | BYOK cho phép switch provider dễ dàng |
| PhảI explain lạI từ đầu mỗI lần | Context cá nhân giúp model hiểu bạn ngay |
| Bị lock-in vào một ecosystem | Portable system — data là của bạn |

→ **Kết quả:** Dùng model rẻ như GLM 4.7-Flash cũng cho kết quả tốt vì workflow đã được optimize.
