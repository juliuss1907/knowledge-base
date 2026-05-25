#!/usr/bin/env python3
"""Debug RSS scraping"""
import feedparser
from datetime import datetime, timedelta

url = "https://techcrunch.com/category/artificial-intelligence/feed/"
source_name = "TechCrunch AI"
cutoff_time = datetime.now() - timedelta(hours=48)

print(f"Testing RSS: {source_name}")
print(f"Cutoff time: {cutoff_time}")
print()

feed = feedparser.parse(url)
print(f"Feed parsed: {len(feed.entries)} entries")

results = []

for entry in feed.entries[:20]:
    # Parse published date
    pub_date = None
    if hasattr(entry, 'published_parsed') and entry.published_parsed:
        pub_date = datetime(*entry.published_parsed[:6])
    elif hasattr(entry, 'updated_parsed') and entry.updated_parsed:
        pub_date = datetime(*entry.updated_parsed[:6])
    
    if not pub_date:
        print(f"  ❌ No date for: {entry.get('title', 'N/A')[:40]}")
        continue
    
    print(f"  Entry: {entry.get('title', 'N/A')[:40]}...")
    print(f"    Date: {pub_date}")
    print(f"    After cutoff: {pub_date > cutoff_time}")
    
    if pub_date < cutoff_time:
        print(f"    → Skipped (too old)")
        continue
    
    # Combine title and summary
    text = entry.get('title', '')
    if hasattr(entry, 'summary'):
        text += "\n\n" + entry.summary
    
    if len(text) > 50:
        results.append({
            'topic': 'tech',
            'source_type': 'rss',
            'source': source_name,
            'source_name': source_name,
            'text': text[:1000],
            'date': pub_date.isoformat(),
            'views': 0,
            'forwards': 0,
            'url': entry.get('link', url)
        })
        print(f"    → Added!")
    else:
        print(f"    → Skipped (text too short: {len(text)} chars)")

print(f"\n✅ Total: {len(results)} items")
