---
type: analysis
title: "Workflow 'Learn to Figure Anything Out with AI' — Chi tiết từng bước"
url: https://letters.thedankoe.com/p/how-average-people-will-get-rich
author: Markus (Analysis)
original_author: Dan Koe
date_published: 2026-06-17
date_ingested: 2026-06-17
status: processed
compiled_at: 2026-06-17
compiled_to: "[[src_dan-koe-workflow-analysis-markus]]"
source: Forwarded Analysis
---

# Workflow "Learn to Figure Anything Out with AI" — Chi tiết từng bước

**Phân tích bởi:** Markus  
**Nguồn bài viết gốc:** Dan Koe — "how average people will get rich with AI"  
**URL:** https://letters.thedankoe.com/p/how-average-people-will-get-rich

---

## Triết lý nền

Dan không đưa prompt có sẵn. Anh ấy dạy cách tự tạo ra prompt từ bất kỳ nguồn expert nào. Đây là meta-skill.

**Công thức chung áp dụng cho cả 4 focus areas (Brand, Content, Product, Promotions):**

```
Tìm expert resource → Feed vào AI → Extract action plan → Biến thành AI coach prompt → Dùng nó
```

---

## Bước 0: Chuẩn bị tư duy

Trước khi bắt đầu, Dan nhấn mạnh:

1. **AI không phải magic** — nó là leverage để làm nhanh hơn thứ đã được chứng minh là hiệu quả
2. **Intelligence needs context** — nếu chỉ hỏi AI "xây personal brand cho tôi", output sẽ vô dụng vì thiếu context
3. **Có nhiều "cách đúng"** — personal branding, content, product đều không có một công thức duy nhất
4. **AI có thể vừa dạy bạn, vừa làm việc cho bạn** — miễn là bạn feed đúng thông tin

---

## FOCUS 1: BRAND — Tạo Personal Brand Coach (chi tiết nhất)

### Bước 1.1: Tìm expert resource

- Lên YouTube, search: "How to build a profitable personal brand", "Personal brand Alex Hormozi", "Full guide to building a personal brand"
- Dan chọn video 6 tiếng của Caleb Ralston (strategist đứng sau Gary V và Alex Hormozi)
- **Tiêu chí chọn:** trustworthy + đủ detailed để ra kết quả

### Bước 1.2: Extract action plan từ resource

**Prompt:**

```text
I want to build a personal brand. Break this video down into a comprehensive
action plan. Write the action plan as if you are teaching me how to build a
personal brand from scratch.

[link to the video]
```

- Dùng reasoning model (Gemini 2.5 Pro) vì video 6 tiếng = context rất dài
- Output: một guide cực kỳ chi tiết

### Bước 1.3: Biến guide thành prompt 2-phase

Đây là bước quan trọng nhất — dùng meta-prompt (Write Incredible AI Prompts) để tạo prompt từ guide.

**Prompt để tạo coach:**

```text
I want to create an AI prompt that acts as my personal brand coach.

Structure your prompt in 2 phases.

Phase 1 – context gathering: interview the user one question at a time
to acquire all details necessary to build a personal brand. At the end
of phase 1, provide a detailed step-by-step action plan.

Phase 2 – personal brand coach: start with the first set of actionable
steps the user should take for their personal brand and encourage the
user to check in frequently with everything they have done. For every
check in, give them tips on how to make their work more impactful and
follow up with the next set of actionable steps.

Base each phase of the prompt on this information on personal branding:

[Paste the full guide from Step 1.2]
```

Output: một prompt dài, siêu chi tiết, đóng vai personal brand coach cá nhân hóa.

### Bước 1.4: Dùng coach

- Mở new chat, paste prompt coach vào
- **Phase 1:** AI phỏng vấn từng câu — dành thờigian trả lờikỹ
- Cuối Phase 1: nhận step-by-step action plan cá nhân hóa
- **Phase 2:** check in hàng tuần, AI cho feedback và next steps

**Kết quả:** Chiến lược cá nhân hóa + expert coach trong ~30 phút, không tốn $10K.

---

## FOCUS 2: CONTENT — Copy What Works, With Your Strategy

### Bước 2.1: Generate content ideas từ strategy

Sau khi có personal brand strategy doc từ Phase 1, tạo list ý tưởng:

```text
Generate 30 validated content ideas based on my personal brand strategy:
[link personal brand strategy document from last step]

The ideas should be a balance between high-performing and authoritative,
pulling from my audiences pain points, popular topics in my niche, and
unique perspectives that separate me from other brands.
```

### Bước 2.2: Break down high-performing content

Chọn một post/video thành công trong niche của bạn:

- **YouTube:** filter by most popular → chọn video có style muốn emulate
- **Twitter:** paste nhiều tweet
- **LinkedIn:** paste post
- **Newsletter:** paste newsletter

**Prompt phân tích:**

```text
Give me a comprehensive breakdown of why this video works:
- The overall structure of the video as a framework
- The psychological patterns used to hold attention
- The structure of each section's ideas and why they're impactful

Structure your output as if you are teaching me how to recreate this
video step by step.
```

### Bước 2.3: Biến breakdown thành content-generation prompt

Dùng lại **meta-prompt** (Write Incredible AI Prompts), feed output từ bước 2.2, yêu cầu tạo prompt:

- **Phase 1:** Tạo outline YouTube video (hoặc tweet/LinkedIn post)
- **Phase 2:** Viết full script

### Bước 2.4: Tạo content hàng loạt

- Gửi content-generation prompt
- Feed 1 content idea từ list 30 ý tưởng
- AI tạo outline → script → bạn chỉnh sửa

---

## FOCUS 3: PRODUCT — Stealing Like An AI Artist

### Triết lý phần này

- Không thể hỏi AI chung chung "tạo cho tôi một product" — kết quả sẽ generic
- Product cần **uniqueness và novelty**, phải đến từ não bạn
- Nhưng AI có thể được **biến thành expert** với đúng prompting

### Các mini-workflow trong Product

**3a. Tìm loại product phù hợp:**

Tìm YouTube video "best types of digital products to sell as a beginner" → extract action plan → biến thành prompt phỏng vấn bạn xem loại nào hợp nhất.

**3b. Chọn topic:**

```text
Based on the type of product, ask AI what topic you should create the
product around — feed it your personal brand strategy from before as context.
```

**3c. Tạo offer (theo Alex Hormozi framework):**

```text
Ask AI to give you a comprehensive breakdown of Alex Hormozi's offer
creation framework. Turn that into a prompt that guides you through
creating your own offer out of your product idea.
```

**3d. Viết landing page copy:**

Break down PDF như *Breakthrough Advertising* (Eugene Schwartz) → extract guide → biến thành prompt viết landing page, feed vào offer của bạn.

**3e. Reverse-engineer competitor product:**

Mua product của đối thủ → paste từng section vào AI → breakdown cấu trúc → biến thành prompt guide bạn tạo product tương tự **nhưng với idea của riêng bạn**.

---

## FOCUS 4: PROMOTIONS — Repeating The Process

### Bước 4.1: Học copywriting frameworks

```text
What are the most effective copywriting frameworks for promoting my
product on social media?
```

→ AI trả về PAS (Problem-Agitate-Solution), AIDA (Attention-Interest-Desire-Action), etc.

### Bước 4.2: Hiểu psychology đằng sau

```text
Ask why those frameworks work and the psychology behind them.
```

### Bước 4.3: Tạo promotions cụ thể

```text
Here is my product details: [link or paste your product details]

Write me three 280 character or less promotions using the PAS framework
and direct response marketing principles. The promotions should link
to my product.
```

### Bước 4.4: Cycle and test

- Xoay vòng các promotion variants mỗi ngày
- Test xem cái nào dẫn đến click-through cao hơn
- Iterate

### Chiến thuật phân phối:

- Link product trong **mọi YouTube description**
- Reply 1 lần/ngày với link product trên tweet/thread/LinkedIn/IG story
- Guide viewers về bio link cho Shorts/Reels/TikTok

---

## Tổng kết: Full pipeline

```
┌─────────────────────────────────────────────────────┐
│ Tìm expert resource (YouTube, PDF, course, book)    │
│ ↓                                                   │
│ Extract thành comprehensive action plan             │
│ ↓                                                   │
│ Biến plan thành AI prompt 2-phase (meta-prompt)     │
│ ↓                                                   │
│ Phase 1: AI phỏng vấn → personalized strategy       │
│ Phase 2: AI coach/generator → làm việc hàng tuần    │
│ ↓                                                   │
│ Áp dụng cho cả 4 focus areas:                       │
│ Brand → Content → Product → Promotions              │
└─────────────────────────────────────────────────────┘
```

**Điểm mấu chốt:** Đây không phải "dùng prompt này để có kết quả." Đây là cách tự build system cho riêng mình dựa trên expert knowledge + AI reasoning. Mỗi người sẽ có coach/content/product khác nhau vì strategy cá nhân hóa khác nhau.
