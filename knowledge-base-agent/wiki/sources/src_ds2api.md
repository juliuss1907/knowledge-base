---
type: source
source_url: https://github.com/CJackHwang/ds2api
date_ingested: 2026-05-05
tags: [#coding, #ai]
status: processed
---

# DS2API — DeepSeek-Compatible Middleware Interface

Owner: CJackHwang
Repo: ds2api
Link: https://github.com/CJackHwang/ds2api

## Ghi chú chính
- **Mục đích**: Là lớp trung gian (middleware) chuyển đổi khả năng hội thoại Web của DeepSeek thành API tương thích với các chuẩn của OpenAI, Claude và Gemini.
- **Đặc điểm kỹ thuật**:
    - Viết bằng Go (hiệu suất cao, đồng thời tốt).
    - Hỗ trợ xoay vòng nhiều tài khoản (multi-account rotation), tự động refresh token.
    - Kiểm soát đồng thời (concurrency control) với hàng đợi (queue).
    - Triển khai DeepSeek PoW bằng Go nguyên bản để phản hồi trong mili giây.
    - Hỗ trợ Tool Calling với định dạng DSML và XML.
- **Khả năng tương thích**: Hoạt động tốt với Codex CLI/SDK, OpenAI SDK, Vercel AI SDK, Anthropic SDK, Google Gemini SDK, LangChain, LlamaIndex và OpenWebUI.
- **Model Mapping**: Cho phép map các model DeepSeek v4 (Flash, Pro) sang các alias của GPT-4, GPT-5, Claude-Sonnet/Opus và Gemini.
- **Triển khai**: Hỗ trợ binary, Docker, Vercel và chạy từ source.
