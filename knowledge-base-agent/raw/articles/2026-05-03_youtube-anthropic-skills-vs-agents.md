---
type: raw
source_type: article
source_url: https://www.youtube.com/watch?v=???
date_ingested: 2026-05-03
tags: [#ai]
status: processed
processed_date: 2026-05-04
---

# Skills vs Agents — Tư duy mới trong phát triển AI

**Tác giả:** Barry Zhang và Mahesh Murag (Anthropic)  
**Nguồn:** YouTube  
**Link gốc:** (Anthropic video about Skills architecture)

---

## Thesis chính

Thay vì xây dựng các tác nhân (agents) riêng biệt cho từng nhiệm vụ (gây lãng phí và khó bảo trì), hướng đi mới là: **giữ nguyên một tác nhân nền tảng có khả năng suy luận tốt và nạp thêm các "gói chuyên môn" gọi là Skills.**

---

## Vấn đề: Chuyên môn thực tế

Các tác nhân AI hiện nay rất thông minh nhưng thường thiếu chuyên môn thực tế cho các nhiệm vụ cụ thể.

- Mô hình AI hiện tại thiếu chuyên môn sâu và bối cảnh cụ thể của từng công việc thực tế

---

## Giải pháp: Skills (Kỹ năng)

**Skills là gì:**
- Thư mục chứa các tệp tin, tập lệnh (scripts) và hướng dẫn được đóng gói
- Cung cấp kiến thức thủ tục (procedural knowledge) cho AI
- Đơn giản, có thể tái sử dụng, dễ chia sẻ và phiên bản hóa

**Đặc điểm kỹ thuật:**

| Thành phần | Mô tả |
|---|---|
| **Định dạng** | Mỗi Skill là một thư mục (folder) chứa các tệp tin |
| **Công cụ** | Scripts làm công cụ "tự ghi chép" — dễ điều chỉnh khi cần |
| **Progressive Disclosure** | AI chỉ nhận metadata khi mới bắt đầu; khi cần mới đọc sâu vào skill.md |

---

## Hệ sinh thái Skills

| Loại | Ví dụ |
|---|---|
| **Foundational Skills** | Cung cấp khả năng mới (tạo tài liệu văn phòng, phân tích dữ liệu sinh học) |
| **Integration Skills** | Tích hợp công cụ bên thứ ba (Browserbase, Notion) |
| **Enterprise Skills** | Dạy AI về quy trình nội bộ của công ty ( Fortune 100 đang dùng) |

---

## Kiến trúc tổng thể (3 lớp)

| Lớp | Tên | Chức năng |
|---|---|---|
| **Lớp 1** | Agent Loop | Lớp tư duy cốt lõi |
| **Lớp 2** | MCP (Model Context Protocol) | Lớp kết nối dữ liệu và công cụ thế giới thực |
| **Lớp 3** | Skills Library | Lớp tri thức và chuyên môn giúp AI thực hiện tác vụ phức tạp một cách nhất quán |

→ Một tác nhân duy nhất có thể thích nghi với nhiều lĩnh vực khác nhau

---

## Tầm nhìn dài hạn: AI tự tạo Skills

| Khả năng | Mô tả |
|---|---|
| **Học liên tục** | Nếu AI phải viết đi viết lại một đoạn code, nó có thể lưu lại thành một Skill |
| **Chuyển giao** | Kiến thức không bị mất — trở thành phần của thư viện tri thức chung |

→ Thay vì xây dựng lại tác nhân từ đầu, tổ chức xây dựng **kho lưu trữ kiến thức phát triển không ngừng**

---

## Kết luận

> Thay vì cố gắng tạo ra các tác nhân mới cho mọi vấn đề, hướng đi hiệu quả hơn là tạo ra các thư viện kỹ năng có thể nạp vào các tác nhân, giúp chúng làm việc **hiệu quả và nhất quán hơn** trong mọi lĩnh vực.
