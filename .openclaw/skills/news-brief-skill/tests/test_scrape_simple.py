#!/usr/bin/env python3
"""Test scraper with thefeed + RSS only (no Telegram)"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from scrape_thefeed import scrape_thefeed
from scrape_rss import scrape_rss
from merge import merge_and_dedup_multi, filter_by_time_window, sort_by_timestamp
from datetime import datetime, timezone
from config import STATE_DIR, TIME_WINDOW_HOURS
import json


def test_full_scrape():
    """Run scrape with thefeed + RSS"""
    
    print("=" * 60)
    print(f"TEST SCRAPE (thefeed + RSS) - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)
    
    all_items = []
    source_stats = {}
    
    # 1. Scrape thefeed
    print("\n🌐 Scraping thefeed.today...")
    try:
        thefeed_items = scrape_thefeed()
        all_items.extend(thefeed_items)
        source_stats['thefeed'] = len(thefeed_items)
        print(f"  ✓ Got {len(thefeed_items)} items")
    except Exception as e:
        print(f"  ✗ thefeed error: {e}")
        import traceback
        traceback.print_exc()
        source_stats['thefeed'] = 0
    
    # 2. Scrape RSS
    print("\n📡 Scraping RSS feeds...")
    try:
        rss_items = scrape_rss()
        all_items.extend(rss_items)
        source_stats['rss'] = len(rss_items)
        print(f"  ✓ Got {len(rss_items)} items")
    except Exception as e:
        print(f"  ✗ RSS error: {e}")
        import traceback
        traceback.print_exc()
        source_stats['rss'] = 0
    
    if not all_items:
        print("\n❌ No items scraped")
        return
    
    # 3. Merge and dedup
    print("\n⚙️  Processing...")
    unique_items = merge_and_dedup_multi(all_items)
    print(f"  After dedup: {len(unique_items)} items")
    
    # 4. Filter by time
    recent_items = filter_by_time_window(unique_items, hours=TIME_WINDOW_HOURS)
    print(f"  After {TIME_WINDOW_HOURS}h filter: {len(recent_items)} items")
    
    # 5. Sort by timestamp
    sorted_items = sort_by_timestamp(recent_items)
    
    # 6. Save JSON
    os.makedirs(STATE_DIR, exist_ok=True)
    timestamp = datetime.now().strftime('%Y-%m-%d_%H%M')
    filename = f"{STATE_DIR}/raw-{timestamp}.json"
    
    # Count by topic
    topic_counts = {}
    for item in sorted_items:
        topic_id = item.get('topic_id', 'unknown')
        topic_counts[topic_id] = topic_counts.get(topic_id, 0) + 1
    
    data = {
        'scraped_at': datetime.now(timezone.utc).isoformat(),
        'total_items': len(sorted_items),
        'topic_counts': topic_counts,
        'sources': source_stats,
        'items': sorted_items
    }
    
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2, default=str)
    
    print("\n" + "=" * 60)
    print("✅ SCRAPE COMPLETE!")
    print(f"   JSON saved: {filename}")
    print(f"   Total items: {len(sorted_items)}")
    print(f"   Sources: {source_stats}")
    print("\nNext: Run synthesize.py")
    print("=" * 60)
    
    return filename


if __name__ == '__main__':
    try:
        json_file = test_full_scrape()
        print(f"\n🎯 Success! Ready for synthesize phase.")
        print(f"   Run: ./venv-3.11/bin/python synthesize.py")
    except Exception as e:
        print(f"\n❌ Test failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)