
# HEARTBEAT – Agent KB daily checklist

Mỗi lần heartbeat (30 phút), chỉ làm check nhẹ, an toàn.
Không tốn quá nhiều token. Không tự bịa task mới.
Nếu KHÔNG có gì cần làm → trả về `HEARTBEAT_OK`.

---

## 1. Inbox & cảnh báo nhanh
- [ ] Có NOTE mới gắn tag `#agent/inbox` trong Tasks/ không?
      → Nếu có, tạo 1 mục TODO ngắn trong file đó (không xử lý sâu).
- [ ] Có log nào trong agents/openclaw/memory/ đánh dấu `#urgent` chưa xử lý?

---

## 2. Health check raw & wiki (nhẹ)
- [ ] Đếm file mới trong raw/ trong 24h qua.
      → Nếu > 0 mà chưa có wiki/sources/ tương ứng:
        Ghi vào agents/openclaw/memory/RAW_BACKLOG.md: "Còn X nguồn chưa compile."
- [ ] Chọn ngẫu nhiên 1-2 file trong wiki/concepts/ gần đây:
      → Kiểm tra có mục "Liên quan" và link tới wiki/sources/ không.
      → Nếu thiếu, note vào RAW_BACKLOG.md (không tự sửa trong heartbeat).

---

## 3. Nhắc việc nhẹ
- [ ] Nếu có file Tasks/review_today.md → đọc phần đầu, ghi 1 dòng update tiến độ.
- [ ] Kiểm tra wiki/reviews/_pending.md có entries mới không?
      → Nếu có và chưa gửi notification → gửi Telegram cho Julius:
        "Hermes review xong, có X bài cần xử lý. Đọc _pending.md vào sáng T2."

---

## 4. Điều kiện kết thúc
Không có gì mới → `HEARTBEAT_OK`.
Có việc cần chú ý → tóm tắt tối đa 3 bullet:
  1. Backlog trong raw/
  2. Concept thiếu liên kết
  3. Task overdue rõ ràng
