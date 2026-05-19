---
type: raw
source_type: article
source_url: https://defi0xjeff.substack.com/p/hermes-as-a-real-time-analyst
date_ingested: 2026-05-18
status: processed
compiled_at: 2026-05-19
compiled_to: "[[2026-05-18_hermes-as-a-real-time-analyst]]"
---

# Hermes as a Real-time Analyst

**Tác giả:** defi0xjeff  
**Nguồn:** Substack — defi0xjeff  
**Ngày đăng:** 2026-05-18

---

## Tóm tắt

Nous Research hợp tác với xAI để tích hợp Grok subscription vào Hermes. Bài viết chia sẻ cách sử dụng `x_search` tool để nâng cao khả năng research trên X (Twitter) và tiết kiệm chi phí.

## Update quan trọng: xAI x Hermes

**Highlights:**
- **Direct Grok subscription:** X Premium/Premium+ users có Grok subs có thể plug vào Hermes
- **x_search tool live:** Cho phép Hermes search X natively như SuperGrok

**Ý nghĩa:**
- X là "town square" cho macro, geopolitics, tech, AI, crypto
- Trước đây cần X API để fetch data — hạn chế research capability
- Giờ Hermes có thể làm deep research trực tiếp trên X

## Use case: X Article Analysis

**Vấn đề cũ:** X API chỉ đọc được headline, author, vài dòng — không đọc được X article content.

**Giải pháp mới:**
1. Drop X article link
2. Nói "summarize with x_search"
3. `x_search` tự động dùng Grok 4.3 fetch content
4. Base model (DeepSeek-v4-flash) analyze và summarize

**Lưu ý setup:**
- Dùng `xai-oauth` thay vì `xai` (nếu không sẽ đi vào xAI API thay vì Grok subscription)
- Đăng ký Grok subscription và authenticate với `hermes model` command

## 6-Stage Research Pipeline

Tác giả brainstorm với Claude Opus 4.7 để tạo pipeline tận dụng `x_search`:

| Stage | Tool | Chức năng |
|-------|------|-----------|
| 1 | `x_search` | Targeted search trên X |
| 2 | @cookiedotfun MCP | Sentiment trend, KOL discussions |
| 3 | Browser CDP | Mở Grok trên Chrome, prompt SuperGrok trực tiếp |
| 4 | DeepSeek | Synthesize thông tin |
| 5 | Hindsight | Recall/reflect, cross-reference với insights cũ |
| 6 | Report | Comprehensive end-to-end report |

**Kết quả:** Report capture past, present, future dựa trên knowledge base cá nhân.

**Lưu ý:** Grok 4.3 kém với browser harness, reasoning, multi-turn agent tool → Nên dùng DeepSeek v4 làm base model.

## Cost Optimization

**Trước:** X API fetch smart accounts (~7-8 people) → ~$0.5/ngày

**Sau:** Switch sang `x_search` → ~$0.1/ngày (chỉ dùng cho X bookmark cron job)

**Grok subscription hack:**
1. Đăng ký Grok $30/tháng → Cancel
2. Nhận offer 3 tháng chỉ $30 (thêm $0.30 cho 3 tháng)
→ Chỉ trả ~$10/tháng thay vì $30

## Tool Comparison: Cookie vs x_search

| Tool | Mạnh | Yếu |
|------|------|-----|
| **Cookie** | Structured data (KOL leaderboards, mindshare timeseries, social decay metrics), project analytics | Real-time news, "why" explanations, search reliability |
| **x_search** | Real-time search, deep research, X article analysis | Raw output, cần post-processing |

## Config x_search

```yaml
x_search:
  timeout_seconds: 240 # hoặc 300 để tránh timeout
  retries: 2
  model: grok-4.3
```

## Evolving Workflow

Sau gần 2 tháng, tác giả chuyển từ:
- **Cũ:** Rely on Hermes to think & execute
- **Mới:** Identify problems → Setup hypothesis → Test with agent

AI như learning augment giúp:
- Hiểu tools nhanh hơn
- Đạt desired outcome
- Tiếp tục học và kiếm tiền từ strategies
- Không tốn hàng trăm/thousands trong inference costs

---

## Bài viết liên quan

- Hermes analyst workflow essentials
- Hermes as the Ultimate Analyst — I've found the gist for my ultimate analyst
- 1 Month with Hermes — I've been using Hermes wrong all along
- Hermes, $200 and 30 skills later — here are the 3 skills that're worth it
