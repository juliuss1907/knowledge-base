# Agent Guide — News Brief Skill

> Hướng dẫn sử dụng skill cho các agent khác.
> Updated: 2026-05-25

---

## Quick Start

```bash
cd /path/to/news-brief-skill
./venv-3.12/bin/python scrape.py   # Scrape data
./venv-3.12/bin/python synthesize.py  # Generate & send brief
```

---

## Common Pitfalls (Đã gặp)

### 1. RSS URLs phải là feed URL, không phải webpage

❌ **Sai:**
```python
'url': 'https://techcrunch.com/category/artificial-intelligence/'
```

✅ **Đúng:**
```python
'url': 'https://techcrunch.com/feed/'
```

**Cách nhận biết feed URL:**
- Thường kết thúc bằng `/feed/`, `/rss/`, `.xml`
- Khi mở trong browser, hiển thị XML thay vì HTML

**Feed URL patterns phổ biến:**
| Site | Feed URL |
|------|----------|
| TechCrunch | `https://techcrunch.com/feed/` |
| The Verge | `https://www.theverge.com/rss/index.xml` |
| Ars Technica | `https://feeds.arstechnica.com/arstechnica/index` |
| Hacker News | `https://news.ycombinator.com/rss` |
| Reddit | `https://www.reddit.com/r/subreddit/.rss` |

---

### 2. Luôn import `re` khi xử lý text

Nếu thêm code xử lý string, nhớ import:

```python
import re  # BẮT BUỘC cho regex
```

**Lỗi đã gặp:**
```
❌ Hacker News: name 're' is not defined
```

---

### 3. Clean HTML từ RSS feeds

RSS feeds thường chứa HTML tags. Phải clean trước khi dùng:

```python
# Clean HTML tags
text = re.sub(r'<[^>]+>', '', text)

# Decode HTML entities
text = text.replace('&lt;', '<').replace('&gt;', '>').replace('&amp;', '&')
```

---

## Debug Commands

### Kiểm tra RSS feed hoạt động

```bash
./venv-3.12/bin/python -c "
import feedparser
feed = feedparser.parse('https://techcrunch.com/feed/')
print(f'Entries: {len(feed.entries)}')
for e in feed.entries[:3]:
    print(f'  - {e.get(\"title\", \"\")[:50]}')
"
```

### Kiểm tra cấu hình RSS

```bash
./venv-3.12/bin/python check_rss.py
```

### Test scrape không gửi Telegram

```bash
./venv-3.12/bin/python scrape.py
# Kiểm tra output, không chạy synthesize.py
```

---

## File Structure (Sau cleanup)

```
news-brief-skill/
├── scrape.py           # Entry point: scrape data
├── synthesize.py       # Entry point: generate brief
├── telegram_auth.py    # Auth script (nếu cần)
├── config.py           # Cấu hình topics, sources, keywords
├── requirements.txt    # Dependencies
├── src/                # Core modules (đã tách)
│   ├── scrape_telegram.py
│   ├── scrape_rss.py
│   └── ...
├── tests/              # Test files
├── docs/               # Documentation
│   ├── AGENT_GUIDE.md  # ← File này
│   ├── examples.md
│   └── workflow.md
└── archive/            # Temp files, backups
```

---

## Adding New RSS Source

**Bước 1:** Tìm feed URL (không phải webpage URL)

**Bước 2:** Test feed:
```bash
python3 -c "import feedparser; print(len(feedparser.parse('URL').entries))"
```

**Bước 3:** Thêm vào `config.py`:
```python
'rss': [
    # ... existing sources ...
    {'name': 'New Source', 'url': 'https://example.com/feed/', 
     'priority': 'high', 'enabled': True}
]
```

**Bước 4:** Test scrape:
```bash
./venv-3.12/bin/python scrape.py
```

---

## Keywords Configuration

### 3-tier system

| Tier | Weight | Usage |
|------|--------|-------|
| Tier 1 | 100 | Breaking news, major events |
| Tier 2 | 70 | Emerging trends |
| Tier 3 | 40 | General topics |
| Negative | -50 | Spam filter |

### Thêm keyword mới

```python
'tier_1': {
    'keywords': ['existing', 'keywords', 'NEW_KEYWORD'],
    'weight': 100
}
```

---

## Troubleshooting

### Scrape return 0 items

1. Kiểm tra RSS URLs có phải feed URL không
2. Kiểm tra `enabled: True` trong config
3. Kiểm tra time window (48h có thể quá ngắn)

### Brief không gửi Telegram

1. Kiểm tra `TELEGRAM_BOT_TOKEN` và `TELEGRAM_CHAT_ID`
2. Kiểm tra bot có quyền gửi message không
3. Kiểm tra `OUTPUT_SETTINGS['telegram']['enabled']`

### Link không clickable

1. Đảm bảo `url` field có trong scraped data
2. Đảm bảo format: `[text](url)` trong markdown
3. Telegram parse_mode phải là `MARKDOWN`

---

## Contact

Nếu gặp lỗi không giải quyết được, check:
1. Logs trong archive/
2. SKILL.md đầy đủ
3. Hỏi Julius (system owner)
