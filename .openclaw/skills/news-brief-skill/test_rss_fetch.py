#!/usr/bin/env python3
import feedparser
from datetime import datetime, timedelta

url = "https://techcrunch.com/category/artificial-intelligence/feed/"

print(f"Fetching: {url}")
feed = feedparser.parse(url)

print(f"Feed title: {feed.feed.get('title', 'N/A')}")
print(f"Entries: {len(feed.entries)}")
print()

cutoff = datetime.now() - timedelta(hours=48)

for entry in feed.entries[:5]:
    title = entry.get('title', 'N/A')
    link = entry.get('link', 'N/A')
    
    pub_date = None
    if hasattr(entry, 'published_parsed') and entry.published_parsed:
        pub_date = datetime(*entry.published_parsed[:6])
    
    print(f"Title: {title[:60]}...")
    print(f"Link: {link}")
    if pub_date:
        print(f"Date: {pub_date}")
        print(f"Within 48h: {pub_date > cutoff}")
    print()
