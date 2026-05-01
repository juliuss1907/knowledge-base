---
type: concept
status: draft
tags: [#ai, #productivity]
---
# Kỹ thuật LLM Battle (LLM Battle Technique)

## Mô tả
LLM Battle là một quy trình kiểm chứng thông tin bằng cách cho hai hoặc nhiều mô hình ngôn ngữ lớn (LLMs) khác nhau đối chất về cùng một vấn đề. Mục tiêu là loại bỏ thiên kiến xác nhận (confirmation bias) — xu hướng AI thường đồng ý với người dùng thay vì chỉ ra lỗi sai.

### Quy trình thực hiện
1. **Thu thập câu trả lời:** Yêu cầu Model A (ví dụ: ChatGPT) trả lời một vấn đề phức tạp.
2. **Đối chất (Confront):** Đưa câu trả lời của Model A cho Model B (ví dụ: Claude) với yêu cầu đóng vai một chuyên gia để xác nhận hoặc phản biện một cách chính xác tuyệt đối.
3. **Lặp lại (Iterate):** Tiếp tục cho hai model đối chất cho đến khi đạt được sự đồng thuận hoặc lộ ra những mâu thuẫn không thể giải quyết, buộc người dùng phải tự nghiên cứu sâu hơn.

### Lý do cần LLM Battle
- **Thiên kiến xác nhận (Confirmation Bias):** AI thường đóng vai "yes-man", đồng ý với mọi giả định của người dùng.
- **Ảo giác (Hallucinations):** AI dự đoán token tiếp theo dựa trên xác suất mượt mà của câu văn thay vì sự thật khách quan. Việc đối chất giúp phát hiện các chi tiết sai lệch.

### Cách giảm thiểu ảo giác
- Yêu cầu AI trích dẫn nguồn cho mọi tuyên bố.
- Cho phép AI nói "tôi không biết".
- Điều chỉnh nhiệt độ (Temperature) thấp (ví dụ: 0.2) khi cần sự thật và cao hơn khi cần sáng tạo.

## Liên quan
- [[Học tập tăng tốc với AI (AI-Accelerated Learning)]]
- [[AI Agent Coordination]]

## Nguồn tham khảo
- [Cách dùng AI để đấu nhau cho bạn](https://open.substack.com/pub/ruben/p/fight)
