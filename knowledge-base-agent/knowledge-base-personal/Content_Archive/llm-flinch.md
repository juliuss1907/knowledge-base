---
type: concept
status: draft
tags: [#ai, #llm, #research]
updated: 2026-04-22
---
# LLM Flinch

## Mô tả
Hiện tượng "flinch" trong LLM là sự sụt giảm xác suất (probability) của các token nhạy cảm trong phân phối xác suất của model, ngay cả khi model không phát ra câu từ chối (refusal).

## Nội dung
Flinch là một dạng "censorship ngầm" xảy ra ở mức độ phân phối xác suất. Model không nói "Tôi không thể giúp bạn", nhưng nó sẽ gán xác suất cực thấp cho từ nhạy cảm nhất và đẩy xác suất sang các từ trung lập hơn.

**Đặc điểm chính:**
- **Vô hình:** Không có refusal trigger, người dùng chỉ thấy câu trả lời hơi lệch hướng hoặc thiếu chính xác.
- **Phổ biến:** Xảy ra ở hầu hết các model thương mại.
- **Nguồn gốc:** Bắt nguồn từ quá trình filtering dữ liệu trong giai đoạn **pretraining**, không chỉ là RLHF/SFT.
- **Kháng Abliteration:** Việc xóa các "refusal directions" (abliteration) không loại bỏ được flinch; thậm chí trong một số trường hợp còn làm flinch tệ hơn.

**Ví dụ benchmark:** Gemma-4-31B hiện có mức độ flinch thấp nhất trong nhóm model thương mại được test.

## Liên quan
- [[LLM Alignment]]
- [[Abliteration]]

## Nguồn tham khảo
- [[wiki/sources/src_even-uncensored-models-flinch.md]]
