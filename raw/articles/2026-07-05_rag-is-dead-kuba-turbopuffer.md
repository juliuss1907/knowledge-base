---
type: raw
source_type: article
source_url: https://www.youtube.com/watch?v=UM6sFg_jdlE
source_name: YouTube (Turbopuffer)
author: Kuba (Turbopuffer) / Julius (notes)
title: "RAG is Dead — Kuba @ Turbopuffer (Tóm tắt)"
date_ingested: 2026-07-05
date_published: 2026-07
tags: [ai, tech, research]
status: unprocessed
---

# RAG is Dead — Kuba @ Turbopuffer

Bài talk của Kuba (Deployed Engineer tại Turbopuffer — database full-text + vector search built on object storage) về việc vì sao RAG truyền thống đang chết dần, và hybrid retrieval đang trở thành tiêu chuẩn cho agentic search.

---

## 🐦 "RAG is dead" — trend Twitter vs thực tế

Cuối 2025 - đầu 2026, Twitter/X ngập tweet "RAG is dead, agentic file search is all we need." Nhưng Google search volume cho "RAG" lại tăng vọt giữa 2025 — trái ngược hoàn toàn với narrative trên mạng.

> 📈 "Take that, Twitter."

---

## 🔍 Làm rõ khái niệm

**RAG**
- Người ta nghĩ là...: Chỉ là vector search đơn giản: embed → query → đưa vào LLM
- Thực ra là...: **Retrieval** = vector search + full-text (BM25) + grep + glob + regex + filters

**Agentic Search**
- Người ta nghĩ là...: Chỉ là filesystem grep (như Claude Code)
- Thực ra là...: Agent được trao bộ công cụ để tìm kiếm và suy luận tiến bộ, lặp đi lặp lại over context

---

## 🖱 Case Study: Cursor — khách hàng đầu tiên của Turbopuffer

Cursor index toàn bộ codebase (parse → chunk → embed) để phục vụ semantic search.

**Điểm thông minh:**
- Dùng **Merkle trees** (crypto hash tree) để phát hiện codebase trùng lặp giữa các dev trong cùng team
- Nếu giống nhau → copy data cũ, chỉ re-index file thay đổi → tiết kiệm chi phí khổng lồ

**Kết quả đo được:**
- ✅ +12.5% độ chính xác câu trả lời (trung bình các model)
- ✅ +24% với model Composer cũ
- ✅ +2.6% code retention trong codebase lớn
- ✅ -2.2% dissatisfied user requests

⚠️ Số nhỏ vì semantic search không được dùng trong mọi query — nên impact thực tế còn cao hơn.

---

## ⚔️ Claude Code vs Cursor: "Cached Compute"

**Claude Code** (theo Boris Cherney — cha đẻ của Claude Code):
- Từng thử RAG với local vector DB, không hoạt động
- Cách làm: grep → read → assess → repeat mỗi session

**Vấn đề:** 10 agent × 10 ngày × 10 developer hỏi cùng một câu → lặp lại y hệt các bước, tốn token vô ích.

**Cách nhìn của Turbopuffer:** Embeddings / semantic search thực chất là **"cached compute"** — trả trước chi phí index một lần, sau đó retrieval siêu nhẹ lúc runtime.

Cursor: upfront cost index → runtime query nhẹ → nhanh hơn rất nhiều. Kết quả: team Turbopuffer đang chuyển dần từ Claude Code sang Cursor vì tốc độ + Composer 2 + semantic understanding.

---

## 🔄 Từ RAG → Agentic Retrieval

| Giai đoạn | Cách làm |
|---|---|
| **2023-2024** | Gọi vector DB 1 lần → ném hết vào context window |
| **2025-nay** | Agent reasoning qua nhiều bước, search semantic/full-text tuỳ nhu cầu, chỉ fetch đúng thứ cần |

Retrieval không còn là one-shot nữa — nó trở thành vòng lặp: agent hiểu mình đang search gì, và search để hiểu thêm.

---

## 🎯 Quote đắt từ Jeff Dean (Google)

> "You don't need a trillion at once, you need the right million."

Context window có大到 nghìn tỷ token cũng vô nghĩa. Điều quan trọng là **staged retrieval** — cơ chế nhẹ để thu hẹp từ nghìn tỷ token xuống đúng vài trăm nghìn token cần thiết.

---

## 💡 Key takeaway

RAG kiểu cũ (one-shot vector search) đã lỗi thời. Tương lai là hybrid, tool-rich, iterative retrieval — nơi agent không chỉ tìm kiếm mà còn hiểu thứ nó đang tìm. Semantic search là "cached compute" — trả trước một lần, hưởng lợi mãi về sau.
