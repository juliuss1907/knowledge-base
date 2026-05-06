---
type: concept
status: draft
tags: [#coding, #ai]
---

# Middleware cho LLM (Middleware for LLMs)

## Mô tả
Các lớp phần mềm trung gian nằm giữa ứng dụng cuối (End-user application) và API của nhà cung cấp mô hình (Model Provider API), nhằm mục đích chuyển đổi giao thức, quản lý chi phí, tối ưu hóa hiệu suất hoặc tăng cường bảo mật.

## Nội dung chính
- **Chức năng phổ biến**:
    - **API Translation (Chuẩn hóa)**: Chuyển đổi request từ một chuẩn (ví dụ: OpenAI API) sang chuẩn của nhà cung cấp khác (ví dụ: DeepSeek, Claude), giúp ứng dụng dễ dàng thay đổi model mà không cần viết lại code.
    - **Load Balancing & Rotation**: Phân phối request qua nhiều tài khoản hoặc nhiều API key để vượt qua rate limit.
    - **Caching**: Lưu trữ các câu trả lời phổ biến để giảm chi phí và tăng tốc độ phản hồi.
    - **Security & Filtering**: Kiểm tra nội dung đầu vào/đầu ra để đảm bảo an toàn hoặc chống leak dữ liệu.
- **Ví dụ điển hình**:
    - **DS2API**: Chuyển đổi DeepSeek Web dialogue thành API tương thích OpenAI/Claude/Gemini.
    - **OpenRouter**: Một middleware khổng lồ cho phép truy cập nhiều model từ nhiều provider qua một API duy nhất.

## Liên quan
- [[DS2API]]
- [[OpenWebUI]]

## Nguồn tham khảo
- [[src_ds2api]]
