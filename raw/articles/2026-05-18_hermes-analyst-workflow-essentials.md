---
type: raw
source_type: article
source_url: https://defi0xjeff.substack.com/p/hermes-analyst-workflow-essentials
date_ingested: 2026-05-18
status: processed
compiled_at: 2026-05-19
compiled_to: [[wiki/sources/src_hermes-analyst-workflow-essentials]]
---

# Hermes Analyst Workflow Essentials

**Tác giả:** defi0xjeff  
**Nguồn:** Substack — defi0xjeff  
**Ngày đăng:** 2026-05-18

---

## Tóm tắt

Bài viết chia sẻ workflow tối ưu để sử dụng Hermes (agent harness) như một analyst cá nhân, dựa trên kinh nghiệm thực tế của tác giả trong việc xếp hạng #1 trên OpenRouter.

## Ba lớp của một agent hữu ích

### Layer 1 — Identity (Soul.md) — ROI cao nhất
- **Định nghĩa:** Agent LÀ AI — tính cách, giọng nói, ràng buộc, giá trị, kiến thức về user
- **Thời gian:** 2-3 giờ viết, sửa 5+ lần
- **Tác động:** Quyết định mọi thứ downstream

### Layer 2 — Knowledge (User.md + Memory)
- **Định nghĩa:** Agent BIẾT GÌ về bạn — portfolio, thesis, sign-offs, lỗi lầm trước đây
- **Thời gian:** 30 phút bản nháp đầu, cập nhật hàng ngày
- **Đặc điểm:** Compound mỗi session — càng sửa càng hay

### Layer 3 — Tools (Config + Skills)
- **Định nghĩa:** Agent CÓ THỂ LÀM GÌ — API keys, cron jobs, browser, Dune queries
- **Đánh giá:** Table stakes — làm agent capable nhưng không differentiated

## Model Configuration

### Khuyến nghị
| Provider | Model | Use case |
|----------|-------|----------|
| OpenCode Go | MiniMax 2.7 | Basic tasks (rất nhanh) |
| OpenCode Go | Kimi k2.6 / GLM5.1 | Delegate task (complex) |
| DeepSeek | DeepSeek v4 Flash | Basic tasks (nhanh & hiệu quả) |
| DeepSeek | DeepSeek v4 Pro | Complex tasks (75% discount trong tháng 5) |

### File cần chú ý
- `config.yaml` — điều chỉnh model provider, API key
- `.env` — environment variables cho tools & models

### Privacy
- **@AskVenice** — zero data retention + TEE, tokenized inference DIEM
- **@dphnAI POD** — sắp có platform credits cho Dolphin inference network

## Soul & User Configuration

### Soul.md — "Who the agent is"
- Mục tiêu sử dụng agent
- Vai trò: analyst, writer, coder, assistant
- Cách nói chuyện: professional, casual (tác giả feed articles để agent nói như mình)
- Operating constraints: unit economics lens (tác giả có 10+ năm PE/VC/IB)
- Investment theses, portfolio positions, risk tolerance

### Quá trình
- Không bao giờ "hoàn thành" — Soul sửa 5-6 lần, User config cập nhật hàng ngày
- Reflection: nói chuyện với agent để hiểu bản thân hơn

## Skill Management

### Tự động tạo skill
- Agent tự tạo skill khi thấy task lặp lại
- Skill = recipe để thực thi workflow không cần giải thích lại

### Pitfalls
- Quá nhiều skills + cron jobs → messy & chaotic
- Tools không hiệu quả lãng phí tokens

### Best practices
- Nhớ tools tốt, chỉnh agent khi dùng tool kém hiệu quả
- Explicitly yêu cầu update cron jobs khi thay đổi tool
- Health check định kỳ bằng delegate task cho sub-agent

## Tools

### Browser Harness (@browser_use)
- **Ưu:** Flexible nhất, surf web như human, không bị block
- **Nhược:** Chậm hơn direct tool cho task cụ thể

### X Bookmark Workflow
- X API v2 pull bookmarks 10am hàng ngày
- Deduplicate URL 30-day rolling window
- Deliver listing (titles, handles, links) tới Discord
- Browser Harness extract X articles content nếu cần summarize

## Memory

### Hindsight (external memory provider)
- Knowledge ingestion: reports → learn → ingest to Hindsight
- Agent ngày càng thông minh từ top analysts + discussions

### Memory.md
- Explicitly nói "remember this" cho thông tin quan trọng
- File nhỏ — chỉ nhớ những gì nên nhớ
- Tự động trim stale memory

## Các bài viết liên quan

- Hermes as the Ultimate Analyst
- 1 Month with Hermes — I've been using Hermes wrong all along
- Hermes, $200 and 30 skills later — here are the 3 skills that're worth it
- 3 Things I learnt after 3 weeks of using Hermes as a personal analyst
