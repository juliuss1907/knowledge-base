---
type: raw
source_type: article
source_url: https://open.substack.com/pub/defi0xjeff/p/1-month-with-hermes-ive-been-using
date_ingested: 2026-05-05
tags: [#ai, #productivity]
status: unprocessed
---

# 1 Month with Hermes — I've Been Using Hermes Wrong All Along — DeFi 0xJeff

**Tác giả:** DeFi 0xJeff  
**Nguồn:** Substack  
**Ngày:** 2026-04-27  
**Link gốc:** https://open.substack.com/pub/defi0xjeff/p/1-month-with-hermes-ive-been-using

---

## Tóm tắt

Sau 1 tháng sử dụng Hermes, tác giả nhận ra mình đã dùng sai cách: **Hermes không phảI builder, mà là operator.**

---

## Learning journey

| Tuần | Tiến độ |
|---|---|
| **Week 1** | Học cách configure model/inference. Thử nhiều setup (OpenRouter, Anthropic API) → **Opencode Go là tốt nhất cho ngườI mớI** |
| **Week 2-3** | Học delegate work, tasks rõ ràng. PhảI very specific ("remember", "make sure to adjust"). Implement health check trước cron jobs |
| **Week 4** | Realization: **Đã dùng Hermes wrong all along** |

---

## Hermes = Operator, không phảI Builder

**Điểm mạnh Hermes:**
- Persistent memory + self-learning loop
- Nhớ across sessions
- Tự động setup skills nếu thấy cần thiết
- Giảm thờI gian task lần sau

→ **Perfect cho recurring automated jobs** (reports, alerts) — "second brain that look out for you"

**Hermes KHÔNG giỏI:**
- Building (dashboard, website) — slow, clunky, aesthetics kém
- Claude/Codex build 10x faster vớI kết quả tốt hơn

---

## Cách phân chia roles

| Role | Tool | Mô tả | Use case |
|---|---|---|---|
| **The Builder** | Claude | Build dashboard/websites, UI/UX changes, developer/engineer work | One-time building tasks |
| **The Operator** | Hermes | Deliver reports, analyze data, glean & pull data, learn from it | On-going tasks tailored to preference |

---

## Ví dụ thực tế: PolyBond

**PolyBond:** Personal prediction market dashboard
- Pick up sharp/whale signals
- Potential insiders
- Track LLM forecasters (Prediction Arena)
- Opportunities từ SN6 Numinous, Manifold

**Setup:**
- **Claude** build dashboard (10x faster, better aesthetics)
- **Hermes** là prediction market analyst — deliver brief report mỗI sáng/ vài giờ

---

## Các dashboard khác

| Dashboard | Mô tả |
|---|---|
| **Bangkok This Weekend** | Track fun activities (cập nhật mỗI thứ 6). Covers Bangkok, Singapore, Tokyo, Hong Kong |
| **Personal x402 + 8004** | Track positions |
| **Bittensor dashboard** | Track subnet owner selling/buying back |
| **Travel dashboard** | — |

---

## Bottom line

> "You have to steer the AI. Not let it steer you."

> "Use the AI to augment learning. Not the other way around."

Nếu có clear useful idea, rất dễ build things bring value — regardless of whether it's a wrapper or slop.
