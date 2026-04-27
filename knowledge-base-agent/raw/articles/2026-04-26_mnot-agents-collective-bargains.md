---
type: raw
source_type: article
source_url: https://www.mnot.net/blog/2026/04/24/agents_as_collective_bargains
date_ingested: 2026-04-26
tags: [#research, #ai, #web3]
status: processed
processed_date: 2026-04-27
---
# What's Missing in the 'Agentic' Story
## Mark Nottingham

**Link gốc:** https://www.mnot.net/blog/2026/04/24/agents_as_collective_bargains
**Published:** 2026-04-24

---

## Tóm tắt

Mark Nottingham — chuyên gia Web & Internet protocols — phân tích rằng AI agents hiện tại thiếu khái niệm "User Agent" (lớp đại diện lợi ích user) như Web browser. Bài viết đặt câu hỏi: nếu không có cơ chế cân bằng lợi ích, AI agent sẽ trở thành công cụ của bất cứ ai muốn khai thác user.

---

## Các điểm chính

### 1. Niềm tin vào máy tính không còn đúng

- Ngày xưa: máy tính local, chạy đúng thứ nó nói
- Giờ: mọi thứ kết nối cloud, ta đang trust nhiều bên mà không hay

**Ví dụ vi phạm trust:**
- TV thu thập dữ liệu users không xin phép
- Meta decrypt private traffic của users
- Microsoft gửi passwords sang cloud cho 700+ data brokers
- Hãng xe chia sẻ dữ liệu với công ty bảo hiểm
- Ring để lộ camera nội bộ cho hacker

### 2. Web Browser là hình thức của "Collective Bargaining"

Trình duyệt web là phần mềm **đại diện cho lợi ích user** khi tương tác với website:
- Cân bằng lợi ích user vs website trong framework chuẩn
- Tạo "hiệp ước toàn cầu" — không ai phải đàm phán riêng
- Có nhiều trình duyệt để user chọn cái đại diện mình tốt nhất
- Market pressure buộc trình duyệt phải bảo vệ user

Nếu không có browser → users phải đàm phán với từng website riêng → sites có quá nhiều quyền → users thua.

### 3. AI Agents thiếu "User Agent"

AI agent hiện tại **không có lớp đại diện lợi ích** như browser:

- Không định nghĩa được agent làm được gì / không làm được gì
- Dữ liệu và services không biết agent sẽ dùng data ra sao
- Agent có thể làm bất cứ điều gì — không guard rails
- Không có tiêu chuẩn công khai để kiểm tra

→ Khó hình thành marketplace vì thiếu trust từ cả users lẫn services.

### 4. Giải pháp: Định nghĩa "User Agent" cho AI

Cần tạo "browser-like" layer giữa AI agent và thế giới bên ngoài:
- Standard tool APIs với constraints rõ ràng
- Permission models chuẩn
- Sandboxing (TEE hoặc equivalent)
- Framework pháp lý để regulation

**Mục tiêu:** Agent không thể tùy tiện dùng data — tạo trust từ cả hai phía.

### 5. Quote đáng chú ý

> "Security is a defensive posture; agency is a functional right."

---

## Liên quan đến

- OpenClaw: là nền tảng agent, cần quan tâm đến vấn đề agency
- Web3 / crypto: các platform phi tập trung cũng đối mặt với vấn đề trust và agency
