# News Brief Skill

Automated news aggregator and brief generator for Crypto & Tech news.

**⚡ Fully Agent-Automated Setup** — Just answer questions, the agent handles everything.

## Features

- **Multi-source scraping**: Telegram channels + X/Twitter (via thefeed.today) + RSS feeds
- **Keyword-first prioritization**: Filter by topics you care about
- **Smart deduplication**: Merge items from multiple sources
- **Automated brief generation**: 100% Vietnamese language output
- **Telegram delivery**: Send formatted briefs to Telegram chat
- **Markdown archive**: Save briefs to files with auto-generated index

---

## 🚀 Setup Process (Fully Automated)

**You don't need to run any commands or edit any files.** The agent handles everything.

### What the Agent Does For You

| Step | Agent Action | Your Role |
|------|--------------|-----------|
| 1 | Create Python 3.11 virtualenv | Just confirm |
| 2 | Install all dependencies (Telethon, Playwright, feedparser) | Wait |
| 3 | Ask for your Telegram credentials | **Provide info** |
| 4 | Ask which topics & channels you want | **Answer questions** |
| 5 | Ask for your keywords (Tier 1/2/3) | **Answer questions** |
| 6 | Auto-generate `config.py` with your settings | Wait |
| 7 | Authenticate Telegram with your phone number | **Provide OTP** |
| 8 | Test scrape + synthesize pipeline | Wait |
| 9 | Setup cron jobs (optional) | **Confirm** |

### What You Need to Prepare

Before starting, have these ready:

1. **Telegram API credentials** (from [my.telegram.org/apps](https://my.telegram.org/apps)):
   - `API_ID` (a number, e.g., 35676903)
   - `API_HASH` (a hex string)

2. **Telegram Bot credentials** (from [@BotFather](https://t.me/BotFather)):
   - `Bot Token` (e.g., `1234567890:ABCDEF...`)
   - `Chat ID` (your Telegram chat ID)

3. **Your phone number** (for Telegram user account authentication):
   - Format: `+xxxxxxxxxxxx` (required for scraping channels)
   
4. **Add this skill to your agent's skills folder, then required agent to load this skill and run setup automatically**

> **Note:** You need a **user account** (phone + OTP) for scraping, NOT just a bot. Bots cannot read channel history.

> **About thefeed.today:** It aggregates trending posts from X (Twitter) — no X account needed. You pick a filter: `Crypto`, `Tech`, `AI`, or `General`.


## Architecture

```
scrape.py → .state/raw-YYYY-MM-DD_HHmm.json → synthesize.py → Telegram + Markdown
```

### Scrape Phase
- Scrape Telegram channels (Telethon with user account)
- Scrape X/Twitter trends (via thefeed.today — no auth needed, filter by Crypto/Tech/AI)
- Scrape RSS feeds (feedparser)
- Merge + dedup
- Save JSON

### Synthesize Phase
- Load JSON
- Prioritize by keywords + engagement
- Select top stories + worth reading
- Format brief (Vietnamese)
- Send to Telegram + save Markdown

---

## Manual Setup (Advanced Users Only)

If you prefer to set up manually instead of using the agent:

### 1. Install dependencies (Python 3.11 required)

**Note:** Python 3.14 is NOT supported due to greenlet compilation issues. Use Python 3.11 virtualenv.

```bash
cd news-brief-skill
python3.11 -m venv venv-3.11
source venv-3.11/bin/activate
pip install -r requirements.txt
playwright install chromium
mkdir -p .state logs
```

### 2. Edit config.py

Add your credentials, topics, sources, and keywords. See `SKILL.md` for detailed config reference.

### 3. Authenticate Telegram

```bash
./venv-3.11/bin/python auth_telegram.py +84xxxxxxxxxx
# Enter OTP when prompted
```

### 4. Test pipeline

```bash
./venv-3.11/bin/python scrape.py
./venv-3.11/bin/python synthesize.py
```

### 5. Setup cron (optional)

```bash
crontab -e
```

Add:

```bash
# Scrape 3x daily (10 min before synthesize)
50 6,12,20 * * * cd /path/to/news-brief-skill && ./venv-3.11/bin/python scrape.py >> logs/scrape.log 2>&1

# Synthesize & deliver 3x daily
0 7,13,21 * * * cd /path/to/news-brief-skill && ./venv-3.11/bin/python synthesize.py >> logs/synthesize.log 2>&1
```

---

## Output Format

### Telegram Brief Example

```
📰 *TIN TỨC TỔNG HỢP*
_07:00 24/05/2026_

━━━━━━━━━━━━━━

🔥 *TIN NÓNG*

*1. 🔴 BREAKING — Bitcoin surges to $77K after Trump announces Iran nuclear deal*
Bitcoin surges to a new all-time high of $77,000 following President Trump's announcement of a...
🌐 thefeed.today · 👁 1.2M
🔗 [Xem thêm](https://thefeed.today/item/abc)

*2. $180M in shorts liquidated as BTC rallies 8%*
Over $180 million in short positions were liquidated across major exchanges...
📱 @ahboyashreads · 👁 45.2K
🔗 [Xem thêm](https://t.me/ahboyashreads/12345)

━━━━━━━━━━━━━━

🪙 *CRYPTO — ĐANG ĐỌC*

1. [Nick says 30-40% gains until taxed, claims crypto unfair treatment](https://t.me/ahboyashreads/12346) — 📱 Ahboyash Reads · 👁 28.3K
2. [Essential bemoans $4K bounty going viral on CT](https://t.me/ahboyashreads/12347) — 📱 Ahboyash Reads · 👁 32.1K
3. [Kaleo says ETH down near FTX price levels, questions capitulation](https://t.me/CoinDeskGlobal/789) — 📱 CoinDesk · 👁 15.8K

💻 *TECH — ĐANG ĐỌC*

1. [Anthropic releases Claude 3.5 with 500K context window](https://thefeed.today/item/def) — 🌐 thefeed.today · 👁 890.0K
2. [Cursor adds multi-file AI editing for 50+ files](https://thefeed.today/item/ghi) — 🌐 thefeed.today · 👁 450.0K

━━━━━━━━━━━━━━
_Được tạo bởi Hermes · 10 tin_
```

### Markdown File Output

Files saved to your configured path:
```
~/julius-workspace/personal/
├── index.md
├── 2026-05-24/
│   ├── 0700.md
│   ├── 1300.md
│   └── 2100.md
└── 2026-05-25/
    └── ...
```

---

## Configuration Guide

### Priority System

**Keyword matching** (0-100 points):
- Tier 1: 100 points (breaking news, major protocols)
- Tier 2: 70 points (emerging trends)
- Tier 3: 40 points (general topics)
- Negative: -50 points (spam, low quality)

**Engagement** (0-50 points):
- Telegram: normalized by views (1K-100K)
**thefeed.today** (X/Twitter aggregator): normalized by views (5K-5M) + engagement rate bonus
- RSS: based on source priority (10-30 points)

**Source authority** (0-15 points):
- Priority: high (1.5x), medium (1.0x), low (0.7x)
- Type: research (1.3x), news (1.0x), alpha (1.1x)

**Recency** (0-10 points):
- Last 3h: 10 points
- Last 6h: 7 points
- Last 12h: 3 points

### Selection Criteria

**Top stories** (3-5 items):
- Min score: 80
- Require keyword match: Yes
- Flexible category mix

**Đáng đọc** (3-5 per topic):
- Min score: 40
- Require keyword match: No (allow high engagement)

---

## Troubleshooting

### No items scraped

- Check if sources are enabled in config
- Verify Telegram authentication: `ls hermes_session.session`
- Check logs: `tail -f logs/scrape.log`

### Brief not sent

- Verify bot token and chat ID in config
- Check Telegram API limits
- Check logs: `tail -f logs/synthesize.log`

### Low quality items

- Add negative keywords to filter spam
- Increase `min_keyword_score` threshold
- Adjust `QUALITY_FILTERS` (min_text_length, min_views)

### Too few/many items

- Adjust `SELECTION_CRITERIA` min/max counts
- Lower/raise score thresholds
- Add/remove keywords

---

## File Structure

```
news-brief-skill/
├── config.py                    # Main configuration (auto-generated by agent)
├── config_helpers.py            # Config utilities
├── scrape.py                    # Main scraper
├── scrape_telegram.py           # Telegram scraper (user account)
├── scrape_thefeed.py            # thefeed.today scraper (X/Twitter trends aggregator)
├── scrape_rss.py                # RSS feed scraper
├── merge.py                     # Dedup logic
├── prioritize.py                # Keyword + engagement scoring
├── format.py                    # Brief formatting (Vietnamese)
├── send.py                      # Telegram sender
├── save_markdown.py             # Markdown file output
├── synthesize.py                # Main synthesizer
├── auth_telegram.py             # Telegram user account auth (OTP-based)
├── setup_telegram.py            # Legacy one-time auth
├── manage_topics.py             # Topic management CLI
├── manage_briefs.py             # Brief archive management CLI
├── requirements.txt             # Python dependencies
├── .gitignore                   # Git ignore rules
├── README.md                    # This file
├── SKILL.md                     # Agent setup guide (for AI agents)
├── workflow.md                  # Detailed workflow
├── examples.md                  # Example briefs
├── .state/                      # Generated JSON files
│   ├── raw-YYYY-MM-DD_HHmm.json
│   └── last-run-timestamp.txt
├── logs/                        # Log files
│   ├── scrape.log
│   └── synthesize.log
└── hermes_session.session       # Telegram session (gitignored)
```

---

## Future Expansion

- Reddit scraper
- Custom website scraper (generic)
- Sentiment analysis
- Trend detection
- Multi-language support
- Web dashboard

---

## License

MIT
