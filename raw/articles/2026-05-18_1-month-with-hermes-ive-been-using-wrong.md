---
type: raw
source_type: article
source_url: https://defi0xjeff.substack.com/p/1-month-with-hermes-ive-been-using
date_ingested: 2026-05-18
status: processed
compiled_at: 2026-05-19
compiled_to: "[[/wiki/sources/src_1-month-with-hermes-ive-been-using-wrong]]"
---

# 1 Month with Hermes — I've Been Using Hermes Wrong All Along

**Tác giả:** defi0xjeff  
**Nguồn:** Substack — defi0xjeff  
**Ngày đăng:** 2026-05-18

---

## Tóm tắt

Sau 1 tháng sử dụng Hermes, tác giả nhận ra đã dùng sai cách — Hermes không phải "builder" mà là "operator". Bài viết chia sẻ cách phân chia vai trò giữa Claude (builder) và Hermes (operator) để tối ưu workflow.

## Tuần 1-3: Learning Curve

**Tuần 1:** Cấu hình model/inference provider. Tác giả thử nhiều setup (Anthropic API, OpenRouter) và kết luận **OpenCode Go** là subscription tốt nhất để bắt đầu.

**Tuần 2-3:** Học cách delegate work đúng cách:
- Phải **rất specific** khi chỉ định "remember", "make sure to adjust [x] cron job"
- Implement **health check** để detect bugs trước cron jobs

## Tuần 4: Epiphany — Hermes là Operator, không phải Builder

**Đặc điểm làm Hermes khác biệt:**
- Persistent memory + self-learning loop
- Tự động setup skills nếu thấy cần thiết
- Giảm thời gian task lần sau

**So sánh:**

| Tool | Vai trò | Use case |
|------|---------|----------|
| **Claude** | **The Builder** | Build dashboard, websites, slides, excel, UI/UX changes — one-time building tasks |
| **Hermes** | **The Operator** | Deliver reports, analyze data, pull & learn from dashboard — recurring automated jobs |

**Lý do phân chia:**
- Hermes build chậm, aesthetics kém hơn Claude
- Claude/Codex có built-in features giúp non-technical navigate dễ hơn
- Hermes không có UI features như Claude

## Ví dụ thực tế: PolyBond

**PolyBond** — prediction market dashboard cá nhân:

**Chức năng:**
- Aggregated sharp/whale signals
- Track insiders betting big
- LLM forecasters từ predictionarena
- Opportunities từ SN6 Numinous, Manifold

**Workflow:**
1. **Claude (Builder):** Xây dựng dashboard — nhanh gấp 10x, ít debug
2. **Hermes (Operator):** Mỗi sáng và vài giờ/lần, analyze dashboard → deliver brief report → expand nếu cần

## Ví dụ khác: Bangkok This Weekend

Dashboard track fun activities cuối tuần, tự update mỗi thứ Sáu:
- Xây dựng bởi **Claude**
- Cover 4 cities: Bangkok, Singapore, Tokyo, Hong Kong
- Hiện tại là sub-page trên Substack tác giả

## Các dashboard khác

- Personal x402 + 8004 dashboard
- Bittensor dashboard (track subnet owner selling/buying)
- Travel dashboard

**Note:** Dễ build nhưng data "premium"/hữu ích thường tốn $$$.

## Takeaway chính

> "You have to steer the AI. Not let it steer you."
> "Use the AI to augment learning. Not the other way around."

**Phân chia rõ ràng:**
- **Claude = Builder** → One-time building tasks
- **Hermes = Operator** → Ongoing tasks, tailored reports, analysis

**Lựa chọn linh hoạt:**
- Một số người chỉ cần Hermes deliver daily briefing
- Một số chỉ cần human-readable dashboard không cần Hermes
- Kết hợp cả hai cho workflow phức tạp

---

## Bài viết liên quan

- Hermes, $200 and 30 skills later — here are the 3 skills that're worth it
- 3 Things I learnt after 3 weeks of using Hermes as a personal analyst
- The Compute, the Intelligence, and the Inference
- Inference is the New Oil - The Economics of AI
