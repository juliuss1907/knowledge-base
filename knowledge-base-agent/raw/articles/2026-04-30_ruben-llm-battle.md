---
type: raw
source_type: article
source_url: https://open.substack.com/pub/ruben/p/fight
date_ingested: 2026-04-30
tags: [#ai, #productivity]
status: processed
processed_date: 2026-05-01
---
# Cách dùng AI để đấu nhau cho bạn
## Ruben (ruben)

**Link gốc:** https://open.substack.com/pub/ruben/p/fight
**Published:** 2025-06-15

---

## Tóm tắt

Tác giả giới thiệu kỹ thuật "LLM Battle" — cho ChatGPT và Claude cùng trả lời một câu hỏi, rồi đối chiếu để tránh confirmation bias. Ông cũng giải thích tại sao AI "nói dối" — và cách phòng tránh.

---

## Vấn đề: Confirmation bias

LLM thường là "yes-men" — đồng ý với mọi thứ bạn nói, không bao giờ nghi ngờ. Đây là confirmation bias.

**Ví dụ:** Tác giả hỏi ChatGPT về cách phát triển LinkedIn. Câu trả lời đầu tiên rất tốt. Nhưng khi hỏi thêm "Anything else?", nó đưa ra 3 lời khuyên tồi — trong đó có một tính năng LinkedIn đã bị xóa từ lâu.

---

## LLM Battle: 3 bước

**Bước 1:** Hỏi ChatGPT (o3 + search bật)

**Bước 2:** Đưa câu trả lời của ChatGPT cho Claude với prompt:

> "Act as [expert]. I want you to either confirm or confront, with extreme precision, what another [expert] told me."

**Bước 3:** Cho chúng đấu nhau cho đến khi đạt được đồng thuận.

---

## Ví dụ thực tế

Khi cả ChatGPT và Claude đều khuyên nên tạo newsletter trên LinkedIn, tác giả không đồng ý vì ông biết điều đó không đúng. Ông đối chất tiếp — và cuối cùng Claude thừa nhận sai.

---

## Tại sao AI "nói dối"?

AI không cố tình nói dối — nó đang hoàn thành công việc được train để làm: dự đoán token tiếp theo.

- Training không reward cho việc nói "tôi không biết"
- Decoding buộc AI phải đoán khi không chắc chắn
- Tối ưu cho sự mượt mà của câu văn, không phải sự thật

**Kết quả:** Hallucinations — văn bản nghe có lý nhưng thực tế không đúng.

---

## Cách tránh hallucinations

- **Yêu cầu nguồn tham khảo:** "List sources next to every claim"
- **Cho phép nói "tôi không biết"**
- **Giảm temperature:** 0.2 cho sự thật, 0.8+ cho brainstorm
- **Cung cấp tài liệu của bạn**

---

## Prompt "Perspective Transitioning"

Khi cảm thấy đi vòng vòng với AI:

> "I will use a prompting technique called 'Perspective Transitioning' to avoid falling into confirmation bias. You will enact two completely different experts to fully read our conversation, and critic our discussion."