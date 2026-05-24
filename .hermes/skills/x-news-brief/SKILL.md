---
name: x-news-brief
aliases: ["x-morning-news", "brief CT", "tin sáng", "x-news"]
agent: Hermes (local)
description: Automated crypto + tech news briefing from X via thefeed.today — 3x daily cron, dual-category extraction, 3-tier prioritization, Vietnamese output to Telegram.
purpose: Automated crypto + tech news briefing from X via thefeed.today
trigger: Cron (3x daily — 7:00, 13:00, 21:00 ICT)
output: Telegram message
version: 1.1
last_updated: 2026-05-23
---

# SKILL — X News Brief

**Agent:** Hermes (local)  
**Purpose:** Automated crypto + tech news briefing from X (via thefeed.today)  
**Trigger:** Cron (3x daily)  
**Output:** Telegram message  
**Version:** 1.0  
**Last updated:** 2026-05-19

---

## Role

Monitor crypto and tech news on X via thefeed.today and deliver concise briefings to Julius 3 times per day. Each brief covers new developments since last run, prioritized by breaking news, engagement, and narrative shifts.

Hermes handles:
- Browser automation (Playwright)
- Dual-category extraction (Crypto + Tech)
- Content filtering and deduplication
- Prioritization (3-tier logic)
- Brief synthesis (separate narratives)
- Telegram delivery

---

## Schedule

| Time (ICT) | Session | Coverage | Cron Expression |
|---|---|---|---|
| 7:00 | ☀️ Morning | Overnight + Asia morning | `0 7 * * *` |
| 13:00 | 🌤 Midday | US morning news | `0 13 * * *` |
| 21:00 | 🌙 Wrap | US afternoon + day recap | `0 21 * * *` |

**Deduplication:** Each run only reports items newer than last run's timestamp.

---

## Data Source

**thefeed.today**

**Categories covered:**
- **Crypto:** DeFi, tokens, blockchain, exchanges, protocols
- **Tech:** AI, startups, products, developer tools, launches

**Why this source:**
- ✅ No rate limits (vs X API free tier exhausted)
- ✅ No authentication required
- ✅ Pre-summarized tweets (1-line per item)
- ✅ Category filters (Crypto + Tech buttons)
- ✅ Engagement metrics (views, likes, engagement rate)
- ✅ Breaking news tags

**Extraction order:**
1. Crypto filter first
2. Tech filter second
3. Merge and deduplicate

---

## Output Specification

**Format:** Telegram message (Markdown)

**Ngôn ngữ: TIẾNG VIỆT 100%.** Tất cả nội dung brief phải bằng tiếng Việt. Tên riêng, tên sản phẩm, tên công ty giữ nguyên tiếng Anh. Thuật ngữ kỹ thuật có thể để tiếng Anh nếu không có bản dịch phổ biến.

**Structure:**
```
✖️ X News Brief [☀️ / 🌤 / 🌙] — [Thứ], [Ngày tháng]

🔥 Top 2-5 stories (linh hoạt)
• [Story] — [Tóm tắt 1 dòng] ([lượt xem])

🧠 Narrative pulse
Crypto: [1-2 câu]
Tech: [1-2 câu]

📌 Đáng đọc (7-10 mục, chia đều 50/50)

Crypto:
• [Mục] — [Tại sao đáng đọc] [Link]
• [Mục] — [Tại sao đáng đọc] [Link]

Tech:
• [Mục] — [Tại sao đáng đọc] [Link]
• [Mục] — [Tại sao đáng đọc] [Link]

TL;DR: [1 dòng tóm tắt cả hai mảng]
```

**Length targets:**
- Top stories: 2-5 items (flexible, highest priority wins)
- Đáng đọc Crypto: 3-5 items
- Đáng đọc Tech: 3-5 items
- Total đáng đọc: 7-10 items (50/50 split)
- Total message: ~500-800 words

**CT Voice:**
- Casual, informative tone — bằng tiếng Việt tự nhiên
- Minimal slang (1-2 terms max: ser, alpha, based)
- Emoji for section markers only
- No hype, no speculation

---

## Prioritization Logic

**3-tier priority system (applied to both categories):**

### Tier 1: Breaking News (Highest)
- Items tagged "Breaking" on thefeed
- Always include if present
- No view threshold

### Tier 2: High Engagement
- Views > 5K
- Engagement rate > 5%
- Sort by views descending

**⚠️ Practical note (2026-05-23):** On thefeed.today, engagement rates are exceptionally low (0.1-2% typical) because "views" are impression counts, not unique viewers. The 5% threshold almost never fires. **Fallback:** When the 5% threshold produces zero or <3 items, fall back to pure views-based ranking. Tier 2 effectively becomes "highest views descending, no rate cutoff." This is expected — do not inflate selections to hit a target.

### Tier 3: Narrative Shift
- New topics not seen in previous runs
- Emerging trends
- Lower views but interesting angle

**Selection algorithm:**

**Top stories (2-5 total, flexible mix):**
- Include all Tier 1 (Breaking) from both categories
- Fill remaining slots with highest Tier 2 (regardless of category)
- Natural mix emerges (not forced 50/50)

**Đáng đọc (7-10 total, 50/50 split):**
- Crypto: 3-5 items (Tier 2 + interesting Tier 3)
- Tech: 3-5 items (Tier 2 + interesting Tier 3)
- Adjust if one category has significantly more breaking news

**Narrative pulse:**
- Separate synthesis for each category
- Crypto: 1-2 sentences on DeFi/blockchain trends
- Tech: 1-2 sentences on AI/product trends

---

## State Management

**Location:**
```
/home/julius/knowledge-base/.hermes/skills/x-news-brief/.state/
└── last-run-timestamp.txt
```

**Format:**
```
2026-05-19T07:00:00+07:00
```

**Behavior:**
- Read at start of each run
- Update after successful extraction
- If missing (first run): set to 24 hours ago
- Single timestamp for both categories (simpler dedup)

**⚠️ Timestamp edge case (observed 2026-05-23):** The state file may contain the cron *trigger* time rather than when content was last captured. All thefeed items are 8-23h old relative to any given run — a strict `item_time > last_run` filter rejects everything. **Solution:** Always use a 24-hour sliding window for dedup (`cutoff = now - timedelta(hours=24)`). The purpose is overnight coverage, not precise wall-clock filtering. Update timestamp to `now` after brief delivery; this becomes the boundary for `now - 24h` in the next run.

---

## Error Handling

### Scenario A: No new items
**Action:** Send brief with message:
```
Không có tin crypto/tech mới từ lần kiểm tra trước (7:00 AM).

Lần cuối: [timestamp]
```

### Scenario B: thefeed.today down
**Action:**
1. Retry once after 30 seconds
2. If still fails: Send error notification
3. Skip this run, try again next cron

### Scenario C: One category fails
**Action:**
1. Continue with successful category
2. Note in brief: "Tech news unavailable this run"
3. Don't skip entire brief

### Scenario D: Extraction fails
**Action:**
1. Log error locally
2. Retry once
3. If still fails: Send error notification
4. Skip this run

### Scenario E: Telegram delivery fails
**Action:**
1. Log locally
2. Retry on next cron run
3. Don't update timestamp (will re-send same items)

---

## Dependencies

**Required:**
- Playwright (browser automation)
- Python 3.9+
- Telegram bot (Hermes has credentials)

**Optional:**
- BeautifulSoup (HTML parsing fallback)

---

## Workflow

See [workflow.md](workflow.md) for detailed 10-phase process.

**Quick summary:**
1. Load last run timestamp
2. Launch browser → thefeed.today
3. Extract Crypto filter (scroll & extract)
4. Extract Tech filter (scroll & extract)
5. Merge & dedup vs timestamp
6. Prioritize (3-tier, both categories)
7. Synthesize brief (separate narratives)
8. Deliver to Telegram
9. Update timestamp

### Known Issue: Context exhaustion (v1.1, observed 2026-05-23)

**Problem:** Scraping and synthesizing in a single agent session fails. Two categories × ~50 items each = too much data. Agent exhausts all turns on browser automation, leaving zero context for prioritization and synthesis. Observed on 3 consecutive runs (morning 07:25, midday 13:10, attempted manual run).

**Proposed fix (not yet implemented):** Split into 2 steps:
1. **Scrape step** — Python script (no LLM turns): Playwright → thefeed.today → extract both categories → save JSON to `.state/raw-YYYY-MM-DD_HHmm.json`.
2. **Synthesize step** — Agent reads JSON (small, clean data) → dedup 24h window → prioritize 3-tier → synthesize Vietnamese brief → Telegram.

Requires 6 cron jobs (3 sessions × 2 steps) or chained execution.

---

## Quality Standards

Before delivering brief, verify:

**Content:**
- [ ] All items newer than last run
- [ ] Breaking news included (if any, both categories)
- [ ] Top stories flexible mix (highest priority)
- [ ] Đáng đọc split 50/50 (Crypto 3-5, Tech 3-5)
- [ ] Narrative pulse separate (Crypto + Tech)
- [ ] TL;DR covers both categories

**Format:**
- [ ] Session icon correct (☀️🌤🌙)
- [ ] Date/day correct
- [ ] Sections clearly separated (Crypto / Tech)
- [ ] All links working
- [ ] Markdown formatted properly
- [ ] CT voice appropriate (minimal slang)

**Delivery:**
- [ ] Telegram message sent successfully
- [ ] Timestamp updated
- [ ] No errors logged

---

## Escalation

Escalate to Julius when:
- thefeed.today structure changes (extraction breaks)
- Consistent delivery failures (3+ runs)
- Unclear how to prioritize (all items low engagement)
- Narrative pulse unclear (no obvious trend)
- Category imbalance extreme (e.g., 0 crypto items)

---

## References

- [workflow.md](workflow.md) — Detailed 10-phase process
- [output-template.md](output-template.md) — Template with examples
- [examples.md](examples.md) — Sample briefs (3 sessions)
- [references/thefeed-guide.md](references/thefeed-guide.md) — Using thefeed.today
- [references/prioritization.md](references/prioritization.md) — 3-tier logic details

---

**Maintainer:** Julius  
**Last updated:** 2026-05-19