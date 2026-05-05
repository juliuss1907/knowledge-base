---
type: raw
source_type: article
source_url: https://open.substack.com/pub/emergingai/p/how-to-build-your-own-llm-knowledge
date_ingested: 2026-05-05
tags: [#ai, #productivity]
status: unprocessed
---

# How to Build Your Own LLM Knowledge Base — Emerging AI

**Tác giả:** Emerging AI  
**Nguồn:** Substack  
**Ngày:** 2026-04-18  
**Link gốc:** https://open.substack.com/pub/emergingai/p/how-to-build-your-own-llm-knowledge

---

## Tóm tắt

Bài viết hướng dẫn cách xây dựng **LLM knowledge base** (external brain) — cách sử dụng AI như "thủ thư" thay vì "máy trả lờI".

---

## Vấn đề hiện tại

> "You use AI like a search engine with memory loss."

HỏI → nhận câu trả lờI → đóng tab. Ngày mai hỏI liên quan → bắt đầu từ con số 0. **Không có gì tích lũy, không có gì kết nốI.**

---

## Insight từ Andrej Karpathy

Sử dụng LLMs **như thủ thư (librarians)** thay vì máy trả lờI:
- Feed raw stuff (articles, PDFs, notes)
- AI xây dựng **personal wiki** ngầm
- Wiki phát triển, ideas liên kết vớI nhau
- Khi hỏI sau này, AI research dựa trên knowledge đã compile thay vì đoán từ đầu

---

## Cách xây dựng (20 phút, no code)

**Hai folder — đó là tất cả:**

| Folder | Mục đích | Quy tắc |
|---|---|---|
| **`raw/`** | Chứa raw stuff: articles, notes, PDFs | Untouched — AI chỉ đọc, không sửa |
| **`wiki/`** | AI vIết: summaries, concept articles, index | AI's job — bạn không đụng vào |

**Workflow:**
1. Bạn feed vào `raw/`
2. AI build `wiki/`
3. Bạn hỏI dựa trên `wiki/`

**Công cụ:** Obsidian (free, cross-platform)

---

## Note

*Content truncated during fetch — full article may require subscription or direct access.*
