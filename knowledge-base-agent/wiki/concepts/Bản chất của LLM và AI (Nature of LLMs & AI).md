---
type: concept
status: draft
tags: [#ai, #mindset]
updated: 2026-05-04
---

# Bản chất của LLM và AI (Nature of LLMs & AI)

## Mô tả
Phân tích về thực thể kỹ thuật của AI, phân biệt giữa khả năng thực tế và những kỳ vọng (hype) về trí tuệ nhân tạo tổng quát (AGI).

### 1. LLM là "Máy dự đoán văn bản" (Text-Prediction Engines)
- **Cơ chế:** AI không thực sự "hiểu" theo nghĩa con người. "Học" trong AI thực chất là điều chỉnh các ma trận số thông qua phép nhân ma trận lặp đi lặp lại dựa trên dữ liệu.
- **Hạn chế:** Thiếu khả năng suy luận nhân quả (causal reasoning), kiến thức thực tế về thế giới vật lý (common sense) và mô hình vật lý.
- **Giới hạn của Scaling:** Việc tăng kích thước model và dữ liệu (scaling) có thể cải thiện hiệu suất nhưng không thể tự thân tạo ra trí tuệ thực sự (genuine intelligence).

### 2. AI Agent dưới góc nhìn kỹ thuật
Một AI agent không phải là một thực thể có ý thức, mà là sự kết hợp của:
$$\text{AI Agent} = \text{LLM} + \text{To-do List} + \text{Tools}$$

### 3. AI và Sự sáng tạo (The Statistical Trap)
- **Tóm tắt thống kê:** AI là bản tóm tắt thống kê của quá khứ (statistical summary of the past).
- **Định kiến chống lại cái mới:** Khi AI đánh giá một ý tưởng là "tệ" hoặc "không khả thi", điều đó thường có nghĩa là ý tưởng đó *không giống với dữ liệu mà nó được huấn luyện*.
- **Hệ quả:** AI có xu hướng kéo người dùng về phía trung bình (regression to the mean) và phản đối các ý tưởng đột phá thực sự "ngoài khung" (outside the box).

### 4. Phân biệt Hype và Khoa học
- **Marketing Hype:** Những tuyên bố về sự kỳ diệu, ý thức hoặc sự thay thế con người thường phục vụ mục đích gây quỹ và bán sản phẩm.
- **Tiếp cận Khoa học:** Tập trung vào việc xây dựng các "Kỹ năng" (Skills) có giới hạn và có thể kiểm chứng được (verifiable capabilities) thay vì theo đuổi những bước nhảy vọt huyền bí về ý thức.

## Liên quan
- [[Tối ưu hóa Claude (Claude Optimization)]] — Cách sử dụng AI hiệu quả khi hiểu rõ bản chất của nó.
- [[Phát hiện văn bản AI (AI Text Detection)]] — Lý do tại sao AI viết giống người là do tối ưu hóa thống kê.

## Nguồn tham khảo
- [[src_burst-your-bubble-ai]] — I'm Sorry to Burst Your Bubble: You Are Being Fooled About AI.
