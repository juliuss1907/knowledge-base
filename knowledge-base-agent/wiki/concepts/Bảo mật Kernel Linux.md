---
type: concept
status: draft
tags: [#tech]
---
# Bảo mật Kernel Linux

## Mô tả
Bảo mật Kernel Linux tập trung vào việc phát hiện và vá các lỗ hổng trong nhân hệ điều hành, nơi quản lý tài nguyên phần cứng và phân quyền hệ thống. Lỗ hổng kernel thường cho phép leo thang đặc quyền (Privilege Escalation) hoặc thực thi mã từ xa.

### Các vấn đề phổ biến
- **Lỗ hổng giao diện (Interface Vulnerabilities):** Các lỗi trong giao diện mạng hoặc hệ thống tệp (ví dụ: AF_ALG).
- **Thời gian vá (Patching Lag):** Khoảng thời gian từ khi lỗ hổng được phát hiện đến khi các bản phân phối (Debian, Red Hat, Ubuntu) cập nhật bản vá cho người dùng.
- **Giảm thiểu rủi ro:** Khi bản vá chính thức chưa có, quản trị viên phải sử dụng các kỹ thuật hạn chế quyền truy cập hoặc cấu hình lại hệ thống để ngăn chặn khai thác.

## Liên quan
- [[Cybersecurity]]
- [[Linux Kernel]]

## Nguồn tham khảo
- [Lỗ hổng Kernel Linux CVE-2026-31431 chưa được vá](https://copy.fail/)
