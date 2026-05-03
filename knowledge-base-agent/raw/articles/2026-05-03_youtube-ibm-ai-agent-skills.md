---
type: raw
source_type: article
source_url: https://www.youtube.com/watch?v=Lg-meK5IU8Q
date_ingested: 2026-05-03
tags: [#ai]
status: unprocessed
---

# Kỹ năng của Đại lý AI (AI Agent Skills) — IBM Technology

**Nguồn:** YouTube (IBM Technology)  
**Link gốc:** Video về AI Agent Skills

---

## 1. Tại sao cần AI Agent Skills?

**Vấn đề:** LLMs có nhiều kiến thức nền tảng (sự thật, lịch sử, khái niệm) nhưng **thiếu kiến thức thủ tục (procedural knowledge)** — tức là biết *cách* làm một việc theo từng bước cụ thể.

**Ví dụ:** Quy trình 47 bước để tạo báo cáo tài chính.

**Giải pháp:** Skills cung cấp kiến thức thủ tục cho AI agents, giúp chúng không phải đoán mò hoặc cần người dùng nhắc lại từng bước.

---

## 2. Cấu trúc của một Skill

Mỗi Skill là một thư mục chứa tệp `skill.md`:

| Thành phần | Chi tiết |
|---|---|
| **YAML Front Matter** | Name (bắt buộc), Description (đóng vai trò "trigger condition" cho AI biết khi nào dùng) |
| **Body** | Hướng dẫn chi tiết, quy trình từng bước, quy tắc, ví dụ |
| **scripts/** (tùy chọn) | Mã thực thi (JavaScript, Python, Bash) |
| **references/** (tùy chọn) | Tài liệu tham khảo bổ sung |
| **assets/** (tùy chọn) | Tài nguyên tĩnh (templates, file dữ liệu) |

---

## 3. Cơ chế Tiết lộ Dần dần (Progressive Disclosure)

AI chỉ tải những gì CẦN thiết, tiết kiệm token:

| Cấp độ | Nội dung | Khi nào tải |
|---|---|---|
| **Level 1 (Metadata)** | Chỉ Tên và Mô tả của tất cả skills | Khởi động — như "Mục lục" |
| **Level 2 (Instructions)** | Toàn bộ Body của skill.md | Khi yêu cầu người dùng khớp với mô tả skill |
| **Level 3 (Resources)** | Script và file tham khảo | Khi tác vụ thực sự cần đến |

---

## 4. Skills vs các phương pháp khác

| Công nghệ | Chức năng | Thiếu |
|---|---|---|
| **MCP** | Truy cập công cụ/API bên ngoài | Không dạy AI *khi nào* hay *làm thế nào* dùng chúng |
| **RAG** | Cung cấp kiến thức *dữ kiện/sự thật* từ database | Không dạy cách làm |
| **Fine-tuning** | Gắn kiến thức vào trọng số mô hình | Tốn kém, khó thay đổi |
| **Skills** | Cung cấp kiến thức thủ tục | Dễ cập nhật, dễ chia sẻ, linh hoạt |

---

## 5. Tiêu chuẩn mở và Bảo mật

| Khía cạnh | Chi tiết |
|---|---|
| **Tiêu chuẩn mở** | skill.md là định dạng mở (agentskills.io, Apache 2.0) — skill tạo cho Claude Code có thể hoạt động trên nền tảng khác |
| **Rủi ro bảo mật** | Skills chứa mã thực thi có thể chạy trên máy tính cục bộ → nguy cơ mã độc, prompt injection → **Cần kiểm tra mã nguồn trước khi cài** |

---

## Kết luận

> Skills hoạt động như **"trí nhớ thủ tục" (procedural memory)** của AI Agent — giúp biến một mô hình lý luận chung chung thành công cụ có thể **thực hiện chính xác các quy trình phức tạp, lặp đi lặp lại**.
