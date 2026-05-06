---
type: concept
status: draft
tags: [#coding, #ai]
---

# DS2API

## Mô tả
Một lớp middleware mã nguồn mở cho phép chuyển đổi giao diện Web dialogue của DeepSeek thành một API tương thích với các chuẩn phổ biến như OpenAI, Anthropic (Claude) và Google (Gemini).

## Nội dung chính
- **Chức năng chính**: 
    - **API Translation**: Chuyển đổi request từ chuẩn OpenAI/Claude/Gemini sang format mà DeepSeek Web hiểu và ngược lại.
    - **Account Management**: Quản lý nhiều tài khoản, tự động xoay vòng token và refresh để tránh giới hạn rate limit.
    - **Performance**: Sử dụng Go để tối ưu hóa concurrency và triển khai Proof of Work (PoW) nội bộ để giảm latency.
    - **Compatibility**: Tương thích với hầu hết các SDK AI phổ biến (Vercel AI SDK, LangChain, LlamaIndex) và các giao diện như OpenWebUI.
- **Ứng dụng**: Cho phép người dùng tận dụng sức mạnh của DeepSeek (ví dụ: DeepSeek-v4 Pro/Flash) trong các ứng dụng vốn chỉ hỗ trợ OpenAI API hoặc Claude API.

## Liên quan
- [[Middleware for LLMs]]
- [[OpenWebUI]]

## Nguồn tham khảo
- [[src_ds2api]]
