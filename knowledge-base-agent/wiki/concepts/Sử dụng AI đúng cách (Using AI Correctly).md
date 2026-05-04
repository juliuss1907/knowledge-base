---
type: concept
status: draft
tags: [#ai, #productivity]
updated: 2026-05-04
---

# Sử dụng AI đúng cách (Using AI Correctly)

## Mô tả
Một tư duy tiếp cận AI tập trung vào việc sử dụng AI như một công cụ khuếch đại chuyên môn hiện có, thay vì dùng nó để thay thế các kỹ năng còn thiếu.

### 1. Nghịch lý của Sự Tự tin (The Confidence Paradox)
- **Hiện tượng:** AI luôn tạo ra văn bản sạch sẽ, tự tin và có tổ chức, khiến người dùng dễ tin rằng AI đang đúng (Confident $\neq$ Competent).
- **Rủi ro:** Nếu dùng AI cho lĩnh vực mình không giỏi, người dùng sẽ không thể nhận ra các lỗi sai về logic, sự thiếu hụt chi tiết hoặc các "mẫu sai" (wrong pattern-matching).

### 2. Sự khác biệt giữa AI và Chuyên gia
AI cung cấp kết quả ở mức trung bình (statistical average, ~70th percentile). Trong khi đó, chất lượng chuyên gia (~95th percentile) được định nghĩa bởi 4 yếu tố mà AI không có:
- **Taste (Gu):** Khả năng cảm nhận chất lượng ngay lập tức dựa trên hàng ngàn lần thực hành.
- **Constraints/Scars (Vết sẹo kinh nghiệm):** Những quy tắc ngầm được học từ những thất bại thực tế.
- **Landmines (Mìn rủi ro):** Hiểu rõ những rủi ro ngầm định trong thực tế (ví dụ: chính trị nội bộ) mà lý thuyết không đề cập.
- **Audience Understanding (Hiểu đối tượng):** Sự thấu cảm sâu sắc về nỗi sợ và phản đối ngầm của một đối tượng cụ thể.

### 3. Quy trình làm việc cho Chuyên gia (Expert-AI Workflow)
Thay vì yêu cầu AI làm toàn bộ, hãy dùng quy trình "Điều hướng" (Steering):
1. **Thiết lập Ngữ cảnh (Contextualization):** Xây dựng context file gồm các ví dụ xuất sắc, quy tắc "Always/Never" và các ràng buộc (constraints) cá nhân.
2. **Khởi tạo (Initialization):** Upload context file và yêu cầu AI tóm tắt lại các quy tắc quan trọng nhất trước khi thực hiện task.
3. **Điều hướng (Steering):**
    - AI tạo v1 ($\sim 60\%$).
    - Chuyên gia dùng "Taste" và "Landmines" để chỉ ra lỗi sai cụ thể.
    - AI viết lại $\rightarrow$ kết quả đạt mức $\sim 95\%$.
    - Chuyên gia viết nốt $5\%$ cuối cùng để thổi hồn vào (Voice).

### 4. Các câu hỏi điều hướng (Steering Prompts)
Để đẩy output của AI vượt qua mức trung bình, hãy hỏi:
- "Điều gì bạn đã bỏ sót?" (What did you leave out?)
- "Hãy lập luận ngược lại quan điểm này." (Argue against this)
- "Sự thật khó chịu nào mà bạn đang né tránh trong bài viết này?" (What's the uncomfortable truth you're avoiding?)

## Liên quan
- [[Tối ưu hóa Claude (Claude Optimization)]] — Các công cụ kỹ thuật để thực hiện workflow điều hướng.
- [[Bản chất của LLM và AI (Nature of LLMs & AI)]] — Hiểu tại sao AI chỉ cung cấp kết quả ở mức trung bình.

## Nguồn tham khảo
- [[src_using-ai-backwards]] — You're Using AI Backwards by Ruben.
