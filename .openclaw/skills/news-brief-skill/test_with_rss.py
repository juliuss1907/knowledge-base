#!/usr/bin/env python3
"""
Test news brief skill with RSS feeds only (no browser/telegram needed)
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import feedparser
from datetime import datetime, timezone
import json


def test_rss_scrape():
    """Scrape crypto RSS feeds"""
    
    print("🚀 Testing RSS-only scrape...")
    print("="*60)
    
    # RSS feeds config
    feeds = [
        {
            'topic_id': 'crypto',
            'topic_name': 'Crypto',
            'name': 'CoinDesk',
            'url': 'https://www.coindesk.com/arc/outboundfeeds/rss/',
            'priority': 'high'
        },
        {
            'topic_id': 'crypto', 
            'topic_name': 'Crypto',
            'name': 'Decrypt',
            'url': 'https://decrypt.co/feed',
            'priority': 'high'
        }
    ]
    
    all_items = []
    
    for feed_config in feeds:
        print(f"\n📡 Scraping {feed_config['name']}...")
        
        try:
            feed = feedparser.parse(feed_config['url'])
            
            if feed.bozo:
                print(f"  ⚠ Parse warning: {feed.bozo_exception}")
            
            print(f"  ✓ Got {len(feed.entries)} entries")
            
            for entry in feed.entries[:10]:  # Limit to 10 per feed
                try:
                    # Extract pubDate
                    pub_date = None
                    if hasattr(entry, 'published_parsed') and entry.published_parsed:
                        pub_date = datetime(*entry.published_parsed[:6], tzinfo=timezone.utc)
                    elif hasattr(entry, 'updated_parsed') and entry.updated_parsed:
                        pub_date = datetime(*entry.updated_parsed[:6], tzinfo=timezone.utc)
                    else:
                        pub_date = datetime.now(timezone.utc)
                    
                    # Build item
                    title = entry.get('title', '')[:200]
                    summary = entry.get('description', '')[:300]
                    
                    # Clean HTML from summary
                    import re
                    summary = re.sub(r'<[^>]+>', '', summary)
                    
                    item = {
                        'title': title,
                        'summary': summary,
                        'link': entry.get('link', ''),
                        'source': 'rss',
                        'topic_id': feed_config['topic_id'],
                        'topic_name': feed_config['topic_name'],
                        'timestamp': pub_date.isoformat(),
                        'engagement': {
                            'type': 'authority',
                            'value': 30  # High authority for CoinDesk/Decrypt
                        },
                        'source_name': feed_config['name']
                    }
                    
                    all_items.append(item)
                    
                except Exception as e:
                    print(f"  Error parsing entry: {e}")
                    continue
                
        except Exception as e:
            print(f"  ✗ Failed to fetch {feed_config['name']}: {e}")
            continue
    
    print("\n" + "="*60)
    print(f"✅ RSS scrape complete: {len(all_items)} items")
    
    return all_items


def save_test_data(items):
    """Save to JSON for synthesize"""
    
    os.makedirs('.state', exist_ok=True)
    
    timestamp = datetime.now().strftime('%Y-%m-%d_%H%M')
    filename = f'.state/raw-rss-{timestamp}.json'
    
    data = {
        'scraped_at': datetime.now(timezone.utc).isoformat(),
        'total_items': len(items),
        'topic_counts': {'crypto': len(items)},
        'sources': {
            'RSS': len(items)
        },
        'items': items
    }
    
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f"💾 Saved to: {filename}")
    return filename


if __name__ == '__main__':
    items = test_rss_scrape()
    
    if items:
        json_file = save_test_data(items)
        
        print(f"\n🎯 Ready for synthesize!")
        print(f"   JSON file: {json_file}")
        print(f"\n   Run synthesize with:")
        print(f"   cd /home/julius/julius-workspace/.hermes/skills/news-brief-skill")
        print(f"   ./venv-3.11/bin/python synthesize.py")
    else:
        print("\n❌ No items scraped")
        sys.exit(1)