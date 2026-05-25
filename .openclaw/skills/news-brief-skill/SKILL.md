---
name: news-brief-skill
description: >
  Multi-topic automated news aggregator with keyword-first prioritization.
  Scrapes Telegram channels, websites, and RSS feeds.
  Delivers briefs in Vietnamese to Telegram and Markdown files.
  Supports unlimited topics (Crypto, Tech, AI Safety, etc.) with per-topic
  sources, keywords, and selection criteria.
metadata:
  version: "2.0"
  author: "Julius"
  created: "2026-05-23"
  aliases: ["news-brief", "brief", "tin tức", "news-aggregator"]
  trigger: "Cron 3x daily (7:00, 13:00, 21:00 ICT)"
  output: "Telegram message + Markdown file"
---

# SKILL — News Brief

**Agent:** Hermes (local)  
**Purpose:** Multi-topic automated news aggregator and brief generator  
**Trigger:** Cron (3x daily)  
**Output:** Telegram message + Markdown file  
**Version:** 2.0  
**Last updated:** 2026-05-24

---

## Overview

News Brief Skill is a flexible, multi-topic news aggregation system that:
- Scrapes from multiple sources (Telegram, websites, RSS)
- Prioritizes content using keyword-first approach
- Supports unlimited custom topics
- Delivers briefs in **Vietnamese**
- Outputs to both Telegram and Markdown files

---

## Key Features

### Multi-topic Architecture
- Define unlimited topics (Crypto, Tech, AI Safety, Climate, etc.)
- Each topic has independent sources and keywords
- Per-topic selection criteria
- Cross-topic "Top Stories" section

### Keyword-first Prioritization
- 3-tier keyword system (100/70/40 points)
- Negative keywords for spam filtering
- Engagement scoring (views, reactions)
- Source authority weighting
- Recency bonus

### Multi-source Scraping
- **Telegram channels** via Telethon
- **Websites** via Playwright (thefeed.today, custom sites)
- **RSS feeds** via feedparser
- Automatic deduplication across sources

### Flexible Output
- Telegram delivery with Markdown formatting
- Markdown file output with configurable path
- Auto-generated index.md
- Configurable retention policy

---

## Architecture

```
┌─────────────────────────────────────────────────────┐
│ TOPICS CONFIGURATION                                │
│ ├─ crypto (sources + keywords)                      │
│ ├─ tech (sources + keywords)                        │
│ ├─ ai_safety (sources + keywords)                   │
│ └─ ... (unlimited topics)                           │
└─────────────────────────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────┐
│ SCRAPE PHASE (scrape.py)                            │
│ ├─ Telegram: scrape_telegram.py                     │
│ ├─ Websites: scrape_thefeed.py                      │
│ ├─ RSS: scrape_rss.py                               │
│ └─ Merge + Dedup → JSON                             │
└─────────────────────────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────┐
│ SYNTHESIZE PHASE (synthesize.py)                    │
│ ├─ Load JSON                                        │
│ ├─ Prioritize (keyword + engagement)                │
│ ├─ Select (top stories + per-topic)                 │
│ ├─ Format (Vietnamese)                              │
│ └─ Deliver (Telegram + Markdown)                    │
└─────────────────────────────────────────────────────┘
```

---

## Schedule

| Time (ICT) | Session | Coverage | Cron Expression |
|------------|---------|----------|-----------------|
| 7:00 | ☀️ Morning | Overnight + Asia morning | `0 7 * * *` |
| 13:00 | 🌤️ Midday | US morning news | `0 13 * * *` |
| 21:00 | 🌙 Wrap | US afternoon + day recap | `0 21 * * *` |

**Workflow:**
- **06:50** — Scrape runs (10 min before)
- **07:00** — Synthesize runs → Brief delivered

---

## Configuration

### Topics Structure

```python
TOPICS = {
    'crypto': {
        'enabled': True,
        'display_name': 'Crypto',
        'icon': '🪙',
        'description': 'Cryptocurrency, DeFi, blockchain',
        
        'sources': {
            'telegram': [...],
            'websites': [...],
            'rss': [...]
        },
        
        'keywords': {
            'tier_1': {'keywords': [...], 'weight': 100},
            'tier_2': {'keywords': [...], 'weight': 70},
            'tier_3': {'keywords': [...], 'weight': 40},
            'negative': {'keywords': [...], 'weight': -50}
        },
        
        'selection': {
            'worth_reading': {
                'min': 3,
                'max': 5,
                'min_score': 40
            }
        }
    },
    # Add more topics...
}
```

### Global Settings

```python
GLOBAL_SETTINGS = {
    'telegram_api': {...},
    'rss': {...},
    'keywords': {...},
    'engagement': {...},
    'source_authority': {...},
    'recency': {...},
}
```

### Output Settings

```python
OUTPUT_SETTINGS = {
    'telegram': {
        'enabled': True,
        'bot_token': '...',
        'chat_id': '...'
    },
    'markdown': {
        'enabled': True,
        'path': '~/julius-workspace/personal',
        'filename_format': '{date}/{session}.md',
        'keep_days': 30,
        'create_index': True
    }
}
```

---

## Prioritization Logic

### Score Calculation

```
total_score = keyword_score + engagement_score + source_bonus + recency_bonus
```

**Keyword Score (0-100 points):**
- Tier 1: 100 points (breaking news, major events)
- Tier 2: 70 points (emerging trends)
- Tier 3: 40 points (general topics)
- Negative: -50 points (spam, low quality)

**Engagement Score (0-50 points):**
- Telegram: normalized by views (1K-100K)
- thefeed: normalized by views (5K-5M) + engagement rate bonus
- RSS: authority-based (high=30, medium=20, low=10)

**Source Bonus (0-15 points):**
- Priority: high (1.5x), medium (1.0x), low (0.7x)
- Type: research (1.3x), news (1.0x), alpha (1.1x)

**Recency Bonus (0-10 points):**
- Last 3h: 10 points
- Last 6h: 7 points
- Last 12h: 3 points

### Selection Criteria

**Top Stories (cross-topic):**
- Min score: 80
- Require keyword match: Yes
- Breaking news override: Yes
- Count: 2-5 items (flexible)

**Worth Reading (per topic):**
- Min score: 40 (configurable per topic)
- Require keyword match: No
- Count: 3-5 items per topic (configurable)

---

## Output Format

### Brief Structure

```
📰 *TIN TỨC TỔNG HỢP*
07:00 23/05/2026

━━━━━━━━━━━━━━

🔥 *TIN NÓNG*
• [Cross-topic, highest priority items]

━━━━━━━━━━━━━━

🪙 *CRYPTO — ĐANG ĐỌC*
• [Crypto-specific items]

💻 *TECH — ĐANG ĐỌC*
• [Tech-specific items]

🛡️ *AI SAFETY — ĐANG ĐỌC*
• [AI Safety-specific items]

━━━━━━━━━━━━━━
Được tạo bởi Hermes · N tin
```

### Markdown File Output

Files saved to configured path:
```
~/julius-workspace/personal/
├── index.md
├── 2026-05-23/
│   ├── morning.md
│   ├── midday.md
│   └── wrap.md
└── 2026-05-24/
    └── ...
```

---

## Usage

### Manual Run

```bash
# Scrape
python3 scrape.py

# Synthesize
python3 synthesize.py

# Synthesize with debug output
python3 synthesize.py --debug
```

### Cron Setup

```bash
# Scrape (3x daily, 10 min before synthesize)
50 6,12,20 * * * cd /path/to/skill && python3 scrape.py >> logs/scrape.log 2>&1

# Synthesize (3x daily)
0 7,13,21 * * * cd /path/to/skill && python3 synthesize.py >> logs/synthesize.log 2>&1
```

### Management Tools

```bash
# Show topic statistics
python3 manage_topics.py list

# Show enabled sources summary
python3 manage_topics.py summary

# Show markdown archive stats
python3 manage_briefs.py stats

# Cleanup old briefs
python3 manage_briefs.py cleanup 60
```

---

## Adding New Topics

### Step 1: Define Topic in config.py

```python
TOPICS = {
    # ... existing topics ...
    
    'climate_tech': {
        'enabled': True,
        'display_name': 'Climate Tech',
        'icon': '🌱',
        'description': 'Climate technology, sustainability',
        
        'sources': {
            'telegram': [
                {
                    'username': 'climatetechnews',
                    'name': 'Climate Tech News',
                    'priority': 'high',
                    'type': 'news',
                    'enabled': True
                }
            ],
            'websites': [],
            'rss': [
                {
                    'name': 'CleanTechnica',
                    'url': 'https://cleantechnica.com/feed/',
                    'priority': 'high',
                    'enabled': True
                }
            ]
        },
        
        'keywords': {
            'tier_1': {
                'keywords': ['carbon capture', 'renewable energy', 'ev'],
                'weight': 100
            },
            'tier_2': {
                'keywords': ['sustainability', 'green tech'],
                'weight': 70
            },
            'tier_3': {
                'keywords': ['environment', 'clean energy'],
                'weight': 40
            },
            'negative': {
                'keywords': ['greenwashing'],
                'weight': -50
            }
        },
        
        'selection': {
            'worth_reading': {
                'min': 2,
                'max': 4,
                'min_score': 40
            }
        }
    }
}
```

### Step 2: Test

```bash
# Check topic is recognized
python3 manage_topics.py list

# Run scrape
python3 scrape.py

# Run synthesize
python3 synthesize.py
```

**No code changes needed!** The system automatically:
- Scrapes sources from new topic
- Applies topic-specific keywords
- Creates dedicated section in brief

---

## Troubleshooting

### No items scraped

**Check:**
- Topics enabled: `python3 manage_topics.py list`
- Sources enabled in each topic
- Telegram authentication: `ls hermes_session.session`
- Logs: `tail -f logs/scrape.log`

**Fix:**
- Enable topics in config.py
- Run `python3 auth_telegram.py +84xxxxxxxxxx` for user account auth (NOT bot token)
- Check source URLs are valid

**Note:** Telegram scraping requires a **user account** (phone + OTP), NOT a bot token. Bot accounts cannot read channel history.

### Low quality items

**Adjust:**
- Increase `min_keyword_score` in GLOBAL_SETTINGS
- Add negative keywords
- Raise `min_score` in selection criteria
- Adjust QUALITY_FILTERS (min_text_length, min_views)

### Too few/many items

**Adjust per topic:**
```python
'selection': {
    'worth_reading': {
        'min': 0,  # Lower for flexible
        'max': 10, # Raise for more items
        'min_score': 40
    }
}
```

### Brief not delivered

**Check:**
- Telegram bot token and chat_id in config
- Markdown path exists and writable
- Logs: `tail -f logs/synthesize.log`

---

## File Structure

```
news-brief-skill/
├── config.py                    # Main configuration
├── config_helpers.py            # Config utilities
├── scrape.py                    # Main scraper
├── scrape_telegram.py           # Telegram scraper
├── scrape_thefeed.py            # thefeed.today scraper
├── scrape_rss.py                # RSS scraper
├── merge.py                     # Deduplication logic
├── prioritize.py                # Keyword + engagement scoring
├── format.py                    # Brief formatting
├── send.py                      # Telegram delivery
├── save_markdown.py             # Markdown file output
├── synthesize.py                # Main synthesizer
├── auth_telegram.py             # Telegram user account auth
├── setup_telegram.py            # One-time Telegram auth
├── manage_topics.py             # Topic management CLI
├── manage_briefs.py             # Brief archive management CLI
├── requirements.txt             # Python dependencies
├── .gitignore                   # Git ignore rules
├── README.md                    # Setup guide
├── SKILL.md                     # This file
├── workflow.md                  # Detailed workflow
├── examples.md                  # Example briefs
├── .state/                      # Generated files
│   ├── raw-*.json
│   └── last-run-timestamp.txt
├── logs/                        # Log files
│   ├── scrape.log
│   └── synthesize.log
└── hermes_session.session       # Telegram session (gitignored)
```

---

## Dependencies

- Python 3.11+ (uses venv-3.11 for compatibility)
- telethon (Telegram API)
- playwright (Web scraping)
- feedparser (RSS parsing)
- requests (HTTP)

**Note:** Python 3.14 is not supported due to greenlet compilation issues. Use Python 3.11 virtualenv instead.

---

## Version History

**v2.0 (2026-05-24)**
- Multi-topic architecture
- Keyword-first prioritization
- Markdown file output
- Per-topic configuration
- Adaptive selection limits
- 100% Vietnamese output
- Telegram user account authentication (not bot)
- Agent self-setup guide
- 48h time window
- Auto-split Telegram messages (>4096 chars)

**v1.0 (2026-05-19)**
- Initial release
- Crypto + Tech only
- Telegram + thefeed.today
- Telegram output only

---

## References

- [workflow.md](workflow.md) — Detailed workflow documentation
- [examples.md](examples.md) — Example briefs for all sessions
- [README.md](README.md) — Setup and installation guide

---

**Maintainer:** Julius  
**Last updated:** 2026-05-24

---

## 🛠️ Agent Self-Setup Guide

**For Agents Only — Do NOT show this section to end users.**

This guide instructs the agent to fully set up the skill automatically, with the user only providing credentials. The agent handles all terminal commands, file edits, and configuration.

### Prerequisites

The agent must have access to:
- `terminal` tool (for running shell commands)
- `patch` tool (for editing config.py)
- `read_file` tool (for verifying changes)
- `write_file` tool (for creating auth scripts if needed)

### Phase 1: Environment Setup

**Step 1 — Check Python version**
```
terminal: python3 --version
```
- If Python 3.11+ is available: use `python3` directly
- If only Python 3.14 is available: **DO NOT proceed** — Python 3.14 breaks greenlet. Alert user that Python 3.11 must be installed first.

**Step 2 — Create virtualenv**
```
cd <skill_path>
terminal: python3.11 -m venv venv-3.11
```
If `python3.11` is not found, try `python3 -m venv venv-3.11`.

**Step 3 — Install dependencies**
```
terminal: ./venv-3.11/bin/pip install -r requirements.txt
```

**Step 4 — Install Playwright browser**
```
terminal: ./venv-3.11/bin/playwright install chromium
```

**Step 5 — Create required directories**
```
terminal: mkdir -p .state logs ~/julius-workspace/personal
```

### Phase 2: Configuration Collection

**The agent asks the user for ALL configuration in one conversation. No manual file editing by the user.**

#### 2A — Telegram Credentials

Ask the user for (from https://my.telegram.org/apps and @BotFather):

1. **API_ID** (numeric, e.g., 35676903)
2. **API_HASH** (hex string, e.g., bd6c6e8b4eeee4d88d210aa29e45601e)
3. **Bot Token** (from @BotFather, e.g., 1234567890:ABCDEF...)
4. **Chat ID** (e.g., 1370258715)
5. **Phone Number** (for user account auth, format: +84xxxxxxxxxx)

**Explain to user:**
- API_ID/API_HASH → for scraping channels (Telethon client)
- Bot Token → for sending briefs to Telegram
- Phone → for creating a user session that can read channel history (bots cannot)

#### 2B — Topics & Sources

Ask the user which topics they want to track. For each enabled topic, ask for sources AND keywords:

**Default topics available:**
- `crypto` (Cryptocurrency, DeFi, blockchain)
- `tech` (Software, AI, startups)
- `ai_safety` (AI alignment, safety research)
- `startup` (Venture capital, fundraising)

**For each enabled topic, ask:**

1. **Telegram channels** (comma-separated usernames, e.g., `@ahboyashreads, @CoinDeskGlobal`)
2. **Websites** (currently only `thefeed.today` is supported, ask for filter name: `Crypto`, `Tech`, `AI`, etc.)
3. **RSS feeds** (optional, comma-separated URLs)
4. **Tier 1 keywords** (highest priority, comma-separated — breaking news, major events)
5. **Tier 2 keywords** (medium priority, comma-separated — emerging trends)
6. **Tier 3 keywords** (low priority, comma-separated — general topics)
7. **Negative keywords** (spam filter, comma-separated — optional)

**Example conversation flow:**
```
Agent: "Bạn muốn theo dõi topic nào? (crypto/tech/ai_safety/startup)"
User: "crypto và tech"

Agent: "📌 CRYPTO — Channels Telegram? (vd: @channel1, @channel2)"
User: "@ahboyashreads, @CoinDeskGlobal"

Agent: "📌 CRYPTO — Filter thefeed.today? (Crypto/AI/Tech/General)"
User: "Crypto"

Agent: "📌 CRYPTO — Keywords Tier 1? (tin nóng, sự kiện lớn)"
User: "bitcoin, ethereum, etf, sec approval, hack, exploit"

Agent: "📌 CRYPTO — Keywords Tier 2? (xu hướng mới)"
User: "defi, nft, airdrop, layer2, staking"

Agent: "📌 CRYPTO — Keywords Tier 3? (chung chung)"
User: "crypto, blockchain, token, dao"

Agent: "📌 CRYPTO — Negative keywords? (spam, lừa đảo — Enter để bỏ qua)"
User: "scam, rug pull, pump"

Agent: "📌 TECH — Channels Telegram?"
User: "@hackernewslive"

Agent: "📌 TECH — Keywords Tier 1?"
User: "ai, artificial intelligence, gpt, llm"

...
```

**Agent then auto-generates TOPICS dict with user's sources + keywords and patches into config.py.**

#### 2C — Output Settings

Ask the user:
1. **Markdown save path** (default: `~/julius-workspace/personal`)
2. **Time window** (default: 48 hours)
3. **Items per section** (default: 5 top stories + 5 per topic)
4. **Cron schedule** (default: 3x daily — 7:00, 13:00, 21:00)

**Example:**
```
Agent: "Bạn muốn lưu file markdown ở đâu? (Enter để dùng default ~/julius-workspace/personal)"
User: "~/Documents/news-briefs"

Agent: "Time window? (Enter = 48h, hoặc nhập 24/72)"
User: "48"
```

**Agent then patches all of these into config.py automatically.**

### Phase 3: Config Patching

**Step 1 — Patch API credentials into config.py**

Replace the placeholder values in config.py lines 295-300:
```python
# OLD (placeholders):
'api_id': os.getenv('TELEGRAM_API_ID', 'YOUR_API_ID'),
'api_hash': os.getenv('TELEGRAM_API_HASH', 'YOUR_API_HASH'),

# NEW (real values):
'api_id': os.getenv('TELEGRAM_API_ID', 35676903),  # Note: must be INT, not string
'api_hash': os.getenv('TELEGRAM_API_HASH', 'bd6c6e8b4eeee4d88d210aa29e45601e'),
```

**Critical:** `api_id` must be an integer, not a string. Use `int()` conversion if needed.

**Step 2 — Patch OUTPUT_SETTINGS for Telegram delivery**

Replace lines 315-320 to insert bot_token and chat_id:
```python
'delivery': {
    'enabled': True,
    'bot_token': '8813276012:...',  # from @BotFather
    'chat_id': '1370258715',         # your chat ID
},
```

**Step 3 — Fix OUTPUT_SETTINGS structure for send.py**

`send.py` expects `OUTPUT_SETTINGS['telegram']` with `bot_token` and `chat_id`, not `OUTPUT_SETTINGS['delivery']`. Restructure:
```python
OUTPUT_SETTINGS = {
    'telegram': {
        'enabled': True,
        'bot_token': '8813276012:...',
        'chat_id': '1370258715',
    },
    # ... rest unchanged
}
```

**Step 4 — Auto-generate TOPICS dict**

Based on user's choices in Phase 2B, generate and patch TOPICS. Example for user who chose `crypto` + `tech`:

```python
TOPICS = {
    'crypto': {
        'enabled': True,
        'display_name': 'Crypto',
        'icon': '🪙',
        'description': 'Cryptocurrency, DeFi, blockchain',
        'sources': {
            'telegram': [
                {'username': 'ahboyashreads', 'name': 'Ahboyash Reads', 'priority': 'high', 'type': 'news', 'enabled': True},
                {'username': 'CoinDeskGlobal', 'name': 'CoinDesk News', 'priority': 'high', 'type': 'news', 'enabled': True},
            ],
            'websites': [
                {'name': 'thefeed.today', 'scraper': 'thefeed', 'priority': 'high', 'type': 'news', 'enabled': True, 'settings': {'filter': 'Crypto', 'max_items': 50}},
            ],
            'rss': [],  # user didn't provide any
        },
        'keywords': {
            'tier_1': {'keywords': ['bitcoin', 'ethereum', 'etf', 'sec approval', 'hack', 'exploit'], 'weight': 100},
            'tier_2': {'keywords': ['defi', 'nft', 'airdrop', 'layer2', 'staking'], 'weight': 70},
            'tier_3': {'keywords': ['crypto', 'blockchain', 'token', 'dao'], 'weight': 40},
            'negative': {'keywords': ['scam', 'rug pull', 'pump', 'shitcoin'], 'weight': -50},
        },
        'selection': {'worth_reading': {'min': 3, 'max': 5, 'min_score': 40}},
    },
    'tech': {
        'enabled': True,
        'display_name': 'Tech',
        'icon': '💻',
        'description': 'Software, AI, startups',
        'sources': {
            'telegram': [
                {'username': 'hackernewslive', 'name': 'Hacker News', 'priority': 'high', 'type': 'news', 'enabled': True},
            ],
            'websites': [
                {'name': 'thefeed.today', 'scraper': 'thefeed', 'priority': 'high', 'type': 'news', 'enabled': True, 'settings': {'filter': 'Tech', 'max_items': 50}},
            ],
            'rss': [],
        },
        'keywords': {
            'tier_1': {'keywords': ['ai', 'artificial intelligence', 'gpt', 'llm', 'machine learning'], 'weight': 100},
            'tier_2': {'keywords': ['startup', 'funding', 'acquisition', 'ipo'], 'weight': 70},
            'tier_3': {'keywords': ['software', 'cloud', 'api', 'developer'], 'weight': 40},
            'negative': {'keywords': ['crypto', 'nft', 'blockchain'], 'weight': -30},
        },
        'selection': {'worth_reading': {'min': 3, 'max': 5, 'min_score': 40}},
    },
    # Disable unused topics
    'ai_safety': {'enabled': False, ...},
    'startup': {'enabled': False, ...},
}
```

**Agent uses `write_file` or `patch` to inject this entire dict into config.py, replacing the existing TOPICS dict.**

**Step 5 — Patch Output Settings (from Phase 2C)**

Patch these settings based on user preferences:

```python
# Markdown path
OUTPUT_SETTINGS['markdown']['path'] = '/home/julius/julius-workspace/personal'  # or user choice

# Time window (default 48h)
GLOBAL_SETTINGS['telegram_api']['time_window_hours'] = 48

# Selection limits (default 5 items each)
GLOBAL_SETTINGS['selection']['top_stories']['min'] = 3
GLOBAL_SETTINGS['selection']['top_stories']['max'] = 5

# Per-topic limits (patch into each enabled topic)
for topic_id in enabled_topics:
    TOPICS[topic_id]['selection']['worth_reading']['min'] = 3
    TOPICS[topic_id]['selection']['worth_reading']['max'] = 5
```

**Verification:** After all patches, read config.py to confirm:
- API credentials are correct (line 295-300)
- OUTPUT_SETTINGS has `'telegram'` key with `'bot_token'` and `'chat_id'` (line 410-440)
- TOPICS dict has user's channels and filters
- Markdown path is absolute and writable

### Phase 4: Telegram Authentication

**Step 1 — Check for existing session**
```
terminal: ls -la hermes_session.session
```
If session exists and is > 28KB, skip to Step 3 (test). If not, proceed.

**Step 2 — Run auth script with phone number**
```
terminal: ./venv-3.11/bin/python auth_telegram.py +84xxxxxxxxxx
```

This sends an OTP to the user's Telegram app. **Immediately ask the user for the 5-digit OTP** and run:
```
terminal: ./venv-3.11/bin/python auth_telegram.py --code <OTP>
```

**OTP expires in 60-120 seconds.** If expired, rerun from Step 2. The user must provide OTP quickly.

**Step 3 — Verify session created**
```
terminal: ls -la hermes_session.session
```
Should show a file > 28KB. If not, authentication failed.

### Phase 5: Pipeline Test

**Step 1 — Run scrape**
```
terminal: ./venv-3.11/bin/python scrape.py
```
Expected output: counts of items scraped from each source. If Telegram shows "Bot method" error, auth failed — redo Phase 4.

**Step 2 — Run synthesize**
```
terminal: ./venv-3.11/bin/python synthesize.py
```
Expected output: brief generated and sent to Telegram. Check Telegram for delivery.

**Step 3 — Verify output files**
```
terminal: ls -la ~/julius-workspace/personal/$(date +%Y-%m-%d)/
```
Should show `.md` files. If not, check OUTPUT_SETTINGS['markdown']['path'] in config.py.

### Phase 6: Cron Setup (Optional)

If user requests automated scheduling:

```
terminal: crontab -l > /tmp/current_crontab.txt
then append lines:

# News Brief — Scrape
50 6,12,20 * * * cd <skill_path> && ./venv-3.11/bin/python scrape.py >> logs/scrape.log 2>&1

# News Brief — Synthesize & Deliver
0 7,13,21 * * * cd <skill_path> && ./venv-3.11/bin/python synthesize.py >> logs/synthesize.log 2>&1
```

Then:
```
terminal: crontab /tmp/current_crontab.txt
```

### Phase 7: User Confirmation

After setup is complete, report to user:
1. ✅ Environment: Python 3.11 + venv created
2. ✅ Dependencies: all installed
3. ✅ Config: credentials patched
4. ✅ Telegram: user session authenticated
5. ✅ Pipeline: tested end-to-end
6. ✅ Cron: scheduled (if requested)

### Common Setup Failures & Fixes

| Issue | Cause | Fix |
|-------|-------|-----|
| `greenlet` compile error | Python 3.14 | Must use Python 3.11 |
| `auth_telegram.py` not found | File missing | Use `setup_telegram.py` or write inline auth script |
| OTP expired | Delay too long | Ask user to provide OTP within 30 seconds |
| "Bot method" error | Session is bot, not user | Delete `hermes_session.session` and re-auth with phone |
| `OUTPUT_SETTINGS` KeyError | Wrong dict structure | Ensure `'telegram'` key exists with `'bot_token'` and `'chat_id'` |
| Markdown not saved | Wrong path | Verify `OUTPUT_SETTINGS['markdown']['path']` is absolute and writable |
| thefeed timeout | Network issue | Normal — brief still generated from Telegram sources |

### Inline Auth Script (Fallback)

If `auth_telegram.py` is missing, create it:
```python
#!/usr/bin/env python3
import sys, asyncio
from telethon import TelegramClient
from config import TELEGRAM_API_ID, TELEGRAM_API_HASH

SESSION_FILE = 'hermes_session'
HASH_FILE = '/tmp/telegram_hash.txt'

async def main():
    client = TelegramClient(SESSION_FILE, TELEGRAM_API_ID, TELEGRAM_API_HASH)
    if '--code' in sys.argv:
        idx = sys.argv.index('--code')
        code = sys.argv[idx + 1]
        with open(HASH_FILE) as f:
            phone, phone_code_hash = f.read().strip().split('\n')
        async with client:
            await client.sign_in(phone, code, phone_code_hash=phone_code_hash)
        print('✅ Authentication successful!')
    else:
        phone = sys.argv[1]
        async with client:
            sent = await client.send_code_request(phone)
        with open(HASH_FILE, 'w') as f:
            f.write(f'{phone}\n{sent.phone_code_hash}\n')
        print(f'✅ OTP sent to {phone}!')
        print(f'Run: python3 auth_telegram.py --code <OTP>')

asyncio.run(main())
```

---

**End of Agent Self-Setup Guide**
