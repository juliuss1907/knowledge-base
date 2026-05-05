---
type: raw
source_type: article
source_url: https://open.substack.com/pub/defi0xjeff/p/hermes-as-the-ultimate-analyst-ive
date_ingested: 2026-05-05
tags: [#ai, #finance]
status: unprocessed
---

# Hermes as the Ultimate Analyst — DeFi 0xJeff

**Tác giả:** DeFi 0xJeff  
**Nguồn:** Substack  
**Ngày:** 2026-05-04  
**Link gốc:** https://open.substack.com/pub/defi0xjeff/p/hermes-as-the-ultimate-analyst-ive

---

## Tóm tắt

Bài viết chia sẻ cách tác giả setup **Hermes** (AI agent) như một **investment analyst** cá nhân, với hệ thống daily briefings và memory.

---

## Setup evolution

**Từ Claude + Hermes → Hermes standalone:**

| Cách | Ưu điểm | Nhược điểm |
|---|---|---|
| Claude (builder) + Hermes (operator) | Visuals tốt, artifacts, site previews, Claude Design | Claude expensive — $20 Pro chỉ là teaser, cần $100 Max |
| Hermes standalone | Dùng OpenWebUI → experience như ChatGPT/Claude | — |

**OpenWebUI:** Transform experience — seamless, great for building/designing. Hermes có thể design HTML và show trong cùng chat.

**Hermes Workspace:** Chưa explore fully — có Swarm (multiple agents), edit Skills/Tasks/Memory/Soul trực tiếp.

---

## Current workflows (Daily briefings)

| Report | Nguồn | Mô tả |
|---|---|---|
| **Tech Report** | @SemiAnalysis_ và others | Track tech accounts, synthesize |
| **Macro Report** | @KobeissiLetter và news sources | Macro insights |
| **X Bookmark Briefing** | X bookmarks (24hr) | Query, scoring, prioritize which to read |
| **Top 5 Daily Synthesis** | Tổng hợp các briefing | Pick top 5 insights, explain why it matters |
| **Polybond Morning Brief** | Polybond (Polymarket dashboard) | Surface potential insiders, sharp signals, trends |
| **Equities Research** | Key stocks tracking | Update prices + stress test analysis |

**Moat:** Hermes nhớ 3 key theses, preferences, risk appetite, current positions (crypto, equities, prediction markets), rationale → tìm investment/research tailored.

---

## Memory system

```
Daily cron jobs → Hindsight ingests insights → Pull patterns & synthesizes across any time period
```

→ Recalls past sessions, draw conclusions/relationships.

---

## Cost & Model setup

| Item | Chi phí |
|---|---|
| Claude subscription (dashboards) | $20/month |
| DeepSeek API (Hermes) | ~$60/month (~$2/day) |
| **Tổng** | ~$80/month |

**Models:**
- DeepSeek v4 Pro: 75% discount till end of May
- DeepSeek v4 Flash: Cheap, efficient for simple tasks
- Opencode Go: #1 choice cho first-time setup ($5 first month)

---

## Bottom line

> "The moat is in the data/context."

Using AI as **learning augment** — không còn dùng Google cho research, chỉ hỏi Hermes hoặc Grok (Grok giỏi X search).
