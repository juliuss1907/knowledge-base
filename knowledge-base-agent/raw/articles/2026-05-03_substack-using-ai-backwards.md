---
type: raw
source_type: article
source_url: https://open.substack.com/pub/ruben/p/youre-using-ai-backwards
date_ingested: 2026-05-03
tags: [#ai, #productivity]
status: processed
processed_date: 2026-05-04
---

# You're Using AI Backwards — Ruben

**Tác giả:** Ruben  
**Nguồn:** Substack  
**Ngày:** 2026-02-01  
**Link gốc:** https://open.substack.com/pub/ruben/p/youre-using-ai-backwards

---

## Vấn đề: Cách sai lầm phổ biến

> "Tôi không biết viết sales copy → nhờ AI"  
> "Tôi chưa từng làm financial model → AI sẽ làm"

**Đây là sai lầm.** Bạn không thể phát hiện lỗi nếu không phải chuyên gia.

---

## AI thực sự là gì?

- LLMs không "biết" gì — chúng **predict**
- Predict "từ nào xuất hiện tiếp theo dựa trên toàn bộ text đã từng được viết"
- → **Statistical average** → median → thứ chấp nhận được với số đông → **70th percentile**

**Bạn muốn 95th percentile, nhưng AI luôn cho 70th.**

---

## Vấn đề của "sự tự tin"

AI luôn tự tin, sạch sẽ, well-organized. Nhưng **chuyên môn thực sự rất messy** — "it depends", ngoại lệ, hỏi lại.

Bạn đọc output và nghĩ "nghe có vẻ biết mình đang nói gì" — nhưng đang **pattern-match sai**. Confident ≠ competent.

---

## Chuyên môn là gì? (4 yếu tố)

| Yếu tố | Mô tả | Ví dụ |
|---|---|---|
| **Taste** | Cảm nhận chất lượng từ hàng ngàn reps | Designer thấy spacing sai trước khi đo |
| **Constraints/Scars** | Quy tắc học từ thất bại | "Không cam kết timeline nếu không có 40% buffer" |
| **Landmines** | Hiểu rủi ro thực tế | Consultant biết rủi ro không phải strategy mà là internal politics |
| **Audience understanding** | Sợ hãi, phản đối ngầm của ngườI cụ thể | Không phảI "marketers" chung chung |

**AI không có gì trong số này.**

---

## Cách đúng: AI cho những gì bạn GIỎI

**Workflow:**

1. **Xây context file** (2-3 giờ, một lần):
   - 5 ví dụ xuất sắc → AI phân tích pattern → rules "Always/Never"
   - Trích xuất constraints cá nhân qua Q&A
   - Định nghĩa audience cụ thể

2. **Upload context file** trước mọI task

3. **Steer vớI follow-ups:**
   - AI viết v1 (60%)
   - Bạn chỉ lỗI bằng expertise (step 2 — taste)
   - AI rewrite (60% → 95%)
   - Bạn viết 5% cuốI (step 4 — voice)

---

## Prompt mẫu

```
[Upload context file]
Đọc đầy đủ trước khi bắt đầu. List 3 rules quan trọng nhất cho task này. 
Sau đó đưa ra execution plan.

[Claude responds]

Good. Now làm [task]. Follow context file nghiêm ngặt. 
Nếu sắp break rule nào, dừng lạI và báo tôi.
```

**Follow-up examples:**
- "Paragraph 2 quá chung chung, làm cụ thể cho B2B SaaS"
- "Bạn miss rủI ro, thêm section what could go wrong"
- "What did you leave out?"
- "Argue against this"
- "What's the uncomfortable truth you're avoiding?"

---

## Bottom line

> **Stop using AI for things you're bad at. You can't tell if it's wrong.**  
> **Start using AI for things you're great at. You'll catch every mistake.**

AI is a mirror. Bring something worth reflecting.
