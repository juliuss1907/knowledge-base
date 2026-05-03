---
type: raw
source_type: article
source_url: https://www.youtube.com/watch?v=S_oN3vlzpMw
date_ingested: 2026-05-03
tags: [#ai, #productivity]
status: unprocessed
---

# Tối ưu hóa AI Agents — Greg Isenberg x Ross Mike

**Tác giả:** Greg Isenberg và Ross Mike  
**Nguồn:** YouTube  
**Link gốc:** https://www.youtube.com/watch?v=S_oN3vlzpMw

---

## Thesis chính

Các mô hình AI hiện nay (Opus 4.6, GPT 5.4) đã cực kỳ tốt. **Vấn đề không nằm ở mô hình mà ở bối cảnh (Context)** — cách xây dựng context sẽ quyết định kết quả là chất lượng hay "rác" (slop).

---

## 1. Context và Mô hình AI

- Context window: Nhồi nhét quá nhiều thông tin ngay từ đầu → lãng phí token và khiến AI trở nên "ngu" khi đạt giới hạn
- Cách xây dựng context đúng cách sẽ quyết định chất lượng output

---

## 2. Sự khác biệt giữa agent.md và Skills

| File | Vấn đề | Giải pháp |
|---|---|---|
| **agent.md / claude.md** | 95% người không cần file này; lặp lại hàng ngàn dòng mỗi cuộc hội thoại gây lãng phí | Skills dùng **progressive disclosure** |
| **Skills** | Chỉ cung cấp tên và mô tả ngắn ban đầu; AI chỉ truy cập chi tiết khi CẦN | Tiết kiệm token, AI nhạy bén hơn |

---

## 3. Quy trình 3 bước tạo "Kỹ năng hoàn hảo"

### Bước 1: Xác định Workflow
- Bắt đầu với một tác vụ cụ thể (ví dụ: nghiên cứu đối tác tài trợ YouTube)

### Bước 2: Walkthrough (Làm cùng AI từng bước)
- Đừng giao việc rồi thôi
- Hướng dẫn AI từng bước, sửa lỗi khi sai, dạy cách tư duy đúng

### Bước 3: Hóa thân thành Skill
- Sau khi có một lần chạy thành công
- Yêu cầu AI xem lại toàn bộ lịch sử và tự viết ra tệp skill.md

---

## 4. Xây dựng kỹ năng đệ quy (Recursive Building)

- Khi AI gặp lỗi (vd: API 500) → hỏi nguyên nhân
- Sau khi sửa thành công → yêu cầu AI cập nhật skill để không bao giờ lặp lại lỗi đó
- Ví dụ: Skill báo cáo tự động lấy dữ liệu từ 8 nguồn — hoàn hảo sau 5 vòng cải tiến

---

## 5. Tư duy làm việc với AI

| Nguyên tắc | Chi tiết |
|---|---|
| **CoI AI như nhân viên mới** | Đào tạo theo cách riêng, khẩu vị riêng, quy trình riêng |
| **Bottom-up** | Đừng vội cài đặt hàng chục sub-agents hay tải skills có sẵn. Bắt đầu với MỘT đại lý, tự xây kỹ năng cho mình |
| **Vượt qua "vùng đầu tư"** | 2 tuần đầu với Claude Code sẽ nản lòng vì AI chưa hiểu ý bạn. Khi vượt qua bằng cách xây dựng kỹ năng → hiệu suất tăng vọt |

---

## Kết luận

> **"Less is More"** — Tập trung vào việc mã hóa (codify) quy trình và chiến lược độc nhất của bạn thành các Kỹ năng, thay vì dựa vào các hướng dẫn chung chung.

---

## Lưu ý từ Julius

*(Julius hỏi trước đó về "4 thứ trước khi xây dựng bất kỳ điều gì" — nội dung này liên quan đến việc xây dựng AI agents và skills)*
