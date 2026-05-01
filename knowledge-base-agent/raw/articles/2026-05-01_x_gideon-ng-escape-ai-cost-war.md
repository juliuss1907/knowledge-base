---
type: raw
source_type: article
source_url: https://x.com/i/status/2048745108582105155
date_ingested: 2026-05-01
tags: [#ai, #productivity]
status: unprocessed
---

# Thoát khỏi "cuộc chiến chi phí AI" — Cách duy nhất để không bị rate limit dìm chết

**Tác giả:** Gideon Ng (@gideonfip)  
**Nguồn:** X/Twitter  
**Link gốc:** https://x.com/i/status/2048745108582105155

---

## Vấn đề

Rate limit đang trở thành kẻ thù lớn nhất của ngườI dùng AI. Các nhà cung cấp model không còn "hào phóng" như trước — họ đang cắt giảm chi phí để thu hút user, nhưng sớm muộn cũng phảI tăng giá để có lãi.

**Tương laI:** 
- $10/tháng sẽ chẳng mua được gì
- Một cuộc trò chuyện đơn giản có thể "đốt" 20% giới hạn tuần
- AI sẽ chỉ dành cho những ngườI trả được tiền subscription cao cấp

**Kẻ thua:** Những ngườI dùng AI như chatbot đơn thuần, không xây dựng gì có thể lặp lại được.

**Kẻ thắng:** Những ngườI biết tiêu token một cách khôn ngoan — xây dựng workflows có thể lặp lại vớI hướng dẫn rõ ràng cho bất kỳ model nào thực thi.

---

## Giải pháp: Hệ thống 8 thành phần "di động"

| Thành phần | Mô tả |
|---|---|
| **Context cá nhân** | File system chứa context, tasks để model biết bạn là ai, làm gì, nghĩ như thế nào |
| **Own your keys** | BYOK provider cho phép chuyển đổi model dễ dàng |
| **Requests** | Input (voice/text) để ra lệnh cho AI |
| **Thought processor** | LLM làm "bộ não" nhận input và cho output |
| **Workflows có thể thực thi** | Skills có thể lặp lại, được gọi bởI bất kỳ LLM nào |
| **Building capabilities** | MCPs hoặc APIs mở rộng khả năng ra nền tảng bên ngoàI |
| **Link across devices** | Đồng bộ qua nhiều thiết bị |
| **Edit và manage** | Dùng markdown editor để quản lý |

→ Bất kỳ thành phần bên ngoàI nào (như model) cũng có thể thay thế, hệ thống vẫn hoạt động.

---

## Framework SIGNAL để xây dựng Skills

**S** — **Spot the bottleneck:** Xác định vấn đề nhỏ, lặp đi lặp lại mà bạn ghét làm  
**I** — **Integrate the stack:** Kết nốI các công cụ cần thiết (APIs, MCPs)  
**G** — **Guide the LLM:** Chạy workflow cùng AI từng bước, không kỳ vọng hoàn hảo ngay  
**N** — **Nail the standard:** Lặp lạI nhiều lần, ghi nhận lỗi để tránh sau này  
**A** — **Automate the logic:** Chuyển thành Skill.md file  
**L** — **Loop recursively:** Liên tục cập nhật Skill khi có vấn đề mớI  

---

## Ví dụ Skills thực tế

- Chuyển bài viết dạng dài thành HTML cho Substack, Medium, LinkedIn
- Lấy onchain summary từ DeBank
- Đồng bộ lead magnets vớI email platform
- Tạo color palettes cho brand
- Thêm YouTube transcripts vào knowledge base
- Chuyển file sang markdown

---

## Ý chính

> Models giờ là commodity — quá nhiều model tốt. Điểm khác biệt duy nhất là **workflow và instructions** bạn cho AI.

Giống như McDonald's: Họ xây dựng hệ thống dễ lặp lạI đến mức bất kỳ nhân viên nào cũng có thể làm việc ngay. Skills của bạn cũng vậy — employee (model) có thể thay đổI, nhưng output vẫn giống nhau vì bạn đã cho họ hướng dẫn rõ ràng.

---

## Kết luận

Thay vì lo lắng về rate limits và chi phí model, hãy xây dựng **Skills** — SOPs rõ ràng có thể chạy trên bất kỳ model nào. Khi đó bạn không bị khóa vào một nhà cung cấp, và có thể dùng cả model rẻ như GLM 4.7-Flash mà vẫn cho kết quả tốt.
