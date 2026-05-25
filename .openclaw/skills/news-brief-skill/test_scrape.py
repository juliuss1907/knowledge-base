#!/usr/bin/env python3
"""Test scrape - minimal version"""
import asyncio
import json
from datetime import datetime, timedelta
from telethon import TelegramClient
from config import TELEGRAM_API_ID, TELEGRAM_API_HASH, TOPICS

SESSION_FILE = 'hermes_session'
TIME_WINDOW_HOURS = 48

async def scrape_telegram():
    """Scrape Telegram channels"""
    client = TelegramClient(SESSION_FILE, TELEGRAM_API_ID, TELEGRAM_API_HASH)
    
    results = []
    cutoff_time = datetime.now() - timedelta(hours=TIME_WINDOW_HOURS)
    
    async with client:
        for topic_key, topic_config in TOPICS.items():
            if not topic_config.get('enabled', False):
                continue
                
            print(f"📱 Scraping topic: {topic_config['display_name']}")
            
            for source in topic_config.get('sources', {}).get('telegram', []):
                if not source.get('enabled', True):
                    continue
                    
                username = source['username']
                try:
                    entity = await client.get_entity(username)
                    
                    async for message in client.iter_messages(entity, limit=20):
                        if message.date.replace(tzinfo=None) < cutoff_time:
                            break
                            
                        if message.text:
                            results.append({
                                'topic': topic_key,
                                'source': username,
                                'source_name': source.get('name', username),
                                'text': message.text[:500],
                                'date': message.date.isoformat(),
                                'views': getattr(message, 'views', 0),
                                'forwards': getattr(message, 'forwards', 0)
                            })
                            
                    print(f"  ✅ @{username}: {len([r for r in results if r['source'] == username])} messages")
                    
                except Exception as e:
                    print(f"  ❌ @{username}: {e}")
    
    # Save results
    output_file = f"test_scrape_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"\n📊 Total scraped: {len(results)} messages")
    print(f"💾 Saved to: {output_file}")
    
    return results

if __name__ == '__main__':
    print("=" * 60)
    print("🧪 Testing Telegram Scrape")
    print("=" * 60)
    print()
    
    results = asyncio.run(scrape_telegram())
    
    if results:
        print("\n✅ Scrape test PASSED!")
    else:
        print("\n⚠️  No messages found (channels may be empty or private)")
