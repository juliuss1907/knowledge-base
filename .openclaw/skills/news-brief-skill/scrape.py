#!/usr/bin/env python3
"""
News Brief Scraper - Full version
Scrapes Telegram channels, RSS feeds, and websites
"""
import asyncio
import json
import os
import sys
from datetime import datetime, timedelta
from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError
import feedparser
import requests
from config import (
    TELEGRAM_API_ID, TELEGRAM_API_HASH,
    TOPICS, GLOBAL_SETTINGS
)

SESSION_FILE = 'hermes_session'
TIME_WINDOW_HOURS = GLOBAL_SETTINGS['time_window']['hours']

def get_timestamp_filename():
    """Generate timestamped filename"""
    return f"raw-{datetime.now().strftime('%Y%m%d-%H%M%S')}.json"

async def scrape_telegram_topic(client, topic_key, topic_config, cutoff_time):
    """Scrape Telegram channels for a topic"""
    results = []
    sources = topic_config.get('sources', {}).get('telegram', [])
    
    for source in sources:
        if not source.get('enabled', True):
            continue
        
        username = source['username']
        try:
            entity = await client.get_entity(username)
            
            async for message in client.iter_messages(entity, limit=50):
                msg_time = message.date.replace(tzinfo=None)
                if msg_time < cutoff_time:
                    break
                
                if message.text and len(message.text) > 50:
                    # Build message URL
                    if hasattr(entity, 'username') and entity.username:
                        url = f"https://t.me/{entity.username}/{message.id}"
                    else:
                        url = ""
                    
                    results.append({
                        'topic': topic_key,
                        'source_type': 'telegram',
                        'source': username,
                        'source_name': source.get('name', username),
                        'text': message.text,
                        'date': message.date.isoformat(),
                        'views': getattr(message, 'views', 0) or 0,
                        'forwards': getattr(message, 'forwards', 0) or 0,
                        'url': url
                    })
            
            print(f"  ✅ @{username}: {len([r for r in results if r['source'] == username])} messages")
            
        except Exception as e:
            print(f"  ❌ @{username}: {str(e)[:50]}")
    
    return results

async def scrape_telegram():
    """Scrape all Telegram channels"""
    print("\n📱 Scraping Telegram channels...")
    
    client = TelegramClient(SESSION_FILE, TELEGRAM_API_ID, TELEGRAM_API_HASH)
    await client.connect()
    
    if not await client.is_user_authorized():
        print("❌ Not authorized! Run: python3 telegram_auth.py")
        await client.disconnect()
        return []
    
    cutoff_time = datetime.now() - timedelta(hours=TIME_WINDOW_HOURS)
    all_results = []
    
    for topic_key, topic_config in TOPICS.items():
        if not topic_config.get('enabled', False):
            continue
        
        print(f"\n🔹 {topic_config.get('display_name', topic_key)}")
        
        results = await scrape_telegram_topic(
            client, topic_key, topic_config, cutoff_time
        )
        all_results.extend(results)
    
    await client.disconnect()
    return all_results

def scrape_rss_topic(topic_key, topic_config, cutoff_time):
    """Scrape RSS feeds for a topic"""
    results = []
    sources = topic_config.get('sources', {}).get('rss', [])
    
    for source in sources:
        if not source.get('enabled', True):
            continue
        
        try:
            feed = feedparser.parse(source['url'])
            
            for entry in feed.entries[:20]:
                # Parse published date
                pub_date = None
                if hasattr(entry, 'published_parsed') and entry.published_parsed:
                    pub_date = datetime(*entry.published_parsed[:6])
                elif hasattr(entry, 'updated_parsed') and entry.updated_parsed:
                    pub_date = datetime(*entry.updated_parsed[:6])
                
                if not pub_date or pub_date < cutoff_time:
                    continue
                
                # Combine title and summary
                text = entry.get('title', '')
                if hasattr(entry, 'summary'):
                    text += "\n\n" + entry.summary
                
                if len(text) > 50:
                    results.append({
                        'topic': topic_key,
                        'source_type': 'rss',
                        'source': source['name'],
                        'source_name': source['name'],
                        'text': text[:1000],
                        'date': pub_date.isoformat(),
                        'views': 0,
                        'forwards': 0,
                        'url': entry.get('link', source['url'])
                    })
            
            print(f"  ✅ {source['name']}: {len([r for r in results if r['source'] == source['name']])} items")
            
        except Exception as e:
            print(f"  ❌ {source['name']}: {str(e)[:50]}")
    
    return results

def scrape_rss():
    """Scrape all RSS feeds"""
    print("\n📡 Scraping RSS feeds...")
    
    cutoff_time = datetime.now() - timedelta(hours=TIME_WINDOW_HOURS)
    all_results = []
    
    for topic_key, topic_config in TOPICS.items():
        if not topic_config.get('enabled', False):
            continue
        
        rss_sources = topic_config.get('sources', {}).get('rss', [])
        if not rss_sources:
            continue
        
        print(f"\n🔹 {topic_config.get('display_name', topic_key)}")
        
        results = scrape_rss_topic(topic_key, topic_config, cutoff_time)
        all_results.extend(results)
    
    return all_results

def save_results(results):
    """Save scraped results to JSON file"""
    if not results:
        return None
    
    filename = get_timestamp_filename()
    
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    
    return filename

def main():
    print("=" * 60)
    print("🔍 News Brief Scraper")
    print("=" * 60)
    print(f"⏰ Time window: {TIME_WINDOW_HOURS} hours")
    print()
    
    all_results = []
    
    # Scrape Telegram
    telegram_results = asyncio.run(scrape_telegram())
    all_results.extend(telegram_results)
    
    # Scrape RSS
    rss_results = scrape_rss()
    all_results.extend(rss_results)
    
    # Summary
    print("\n" + "=" * 60)
    print(f"📊 Total scraped: {len(all_results)} items")
    
    # Group by topic
    by_topic = {}
    for r in all_results:
        topic = r.get('topic', 'unknown')
        by_topic[topic] = by_topic.get(topic, 0) + 1
    
    for topic, count in by_topic.items():
        print(f"   • {topic}: {count}")
    
    # Group by source type
    by_type = {}
    for r in all_results:
        st = r.get('source_type', 'unknown')
        by_type[st] = by_type.get(st, 0) + 1
    
    print(f"\nBy source type:")
    for st, count in by_type.items():
        print(f"   • {st}: {count}")
    
    # Save results
    if all_results:
        filename = save_results(all_results)
        print(f"\n💾 Saved to: {filename}")
        print("\n✅ Scrape complete!")
        print(f"\nNext step: python3 synthesize.py")
    else:
        print("\n⚠️  No items scraped")
        print("   Channels may be empty or private")

if __name__ == '__main__':
    main()
