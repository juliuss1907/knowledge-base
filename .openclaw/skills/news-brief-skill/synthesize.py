#!/usr/bin/env python3
"""
News Brief Synthesizer - Full version with fixed Markdown formatting
Generates brief from scraped data and sends to Telegram
"""
import json
import os
import re
import sys
import asyncio
from datetime import datetime, timedelta
from collections import defaultdict
from config import TOPICS, GLOBAL_SETTINGS, OUTPUT_SETTINGS
from telegram import Bot
from telegram.constants import ParseMode

# Import telegram credentials from config
TELEGRAM_BOT_TOKEN = OUTPUT_SETTINGS['telegram']['bot_token']
TELEGRAM_CHAT_ID = OUTPUT_SETTINGS['telegram']['chat_id']

def find_latest_scrape_file():
    """Find the most recent scrape file"""
    json_files = [f for f in os.listdir('.') if f.startswith('raw-') and f.endswith('.json')]
    if not json_files:
        # Fallback to test files
        json_files = [f for f in os.listdir('.') if f.startswith('test_scrape_') and f.endswith('.json')]
    
    if not json_files:
        return None
    
    # Sort by modification time
    latest = max(json_files, key=lambda f: os.path.getmtime(f))
    return latest

def load_scraped_data(filepath=None):
    """Load scraped data from JSON file"""
    if not filepath:
        filepath = find_latest_scrape_file()
    
    if not filepath or not os.path.exists(filepath):
        print(f"❌ No scrape file found")
        return []
    
    print(f"📂 Loading: {filepath}")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def score_message(msg, topic_config):
    """Score a message based on keywords and engagement"""
    text = msg.get('text', '').lower()
    score = 0
    matched_keywords = []
    
    keywords = topic_config.get('keywords', {})
    
    # Tier 1 keywords (highest priority)
    for kw in keywords.get('tier_1', {}).get('keywords', []):
        if kw.lower() in text:
            score += keywords['tier_1']['weight']
            matched_keywords.append(kw)
    
    # Tier 2 keywords
    for kw in keywords.get('tier_2', {}).get('keywords', []):
        if kw.lower() in text:
            score += keywords['tier_2']['weight']
            matched_keywords.append(kw)
    
    # Tier 3 keywords
    for kw in keywords.get('tier_3', {}).get('keywords', []):
        if kw.lower() in text:
            score += keywords['tier_3']['weight']
            matched_keywords.append(kw)
    
    # Negative keywords
    for kw in keywords.get('negative', {}).get('keywords', []):
        if kw.lower() in text:
            score += keywords['negative']['weight']
    
    # Engagement bonus
    views = msg.get('views', 0)
    forwards = msg.get('forwards', 0)
    
    if views > 10000:
        score += 20
    elif views > 5000:
        score += 15
    elif views > 1000:
        score += 10
    
    if forwards > 100:
        score += 10
    elif forwards > 50:
        score += 5
    
    # Recency bonus
    msg_date_str = msg.get('date', datetime.now().isoformat())
    msg_date = datetime.fromisoformat(msg_date_str.replace('Z', '+00:00'))
    now = datetime.now(msg_date.tzinfo) if msg_date.tzinfo else datetime.now()
    hours_old = (now - msg_date).total_seconds() / 3600
    
    if hours_old <= 3:
        score += 10
    elif hours_old <= 6:
        score += 7
    elif hours_old <= 12:
        score += 3
    
    return score, matched_keywords

def clean_text_for_markdown(text):
    """Clean text for safe Markdown display - remove problematic characters"""
    if not text:
        return ""
    
    # Replace newlines with spaces
    text = text.replace('\n', ' ').replace('\r', ' ')
    
    # Remove multiple spaces
    text = ' '.join(text.split())
    
    # Remove markdown links that might be malformed [text](url)
    text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', text)
    
    # Remove bare URLs
    text = re.sub(r'https?://\S+', '', text)
    
    # Remove markdown formatting characters
    text = text.replace('*', '').replace('_', '').replace('`', '')
    text = text.replace('[', '').replace(']', '').replace('(', '').replace(')', '')
    
    return text.strip()

def truncate_text(text, max_length=150):
    """Truncate text to max length, preserving words"""
    text = clean_text_for_markdown(text)
    
    if len(text) <= max_length:
        return text
    
    # Try to cut at word boundary
    truncated = text[:max_length]
    last_space = truncated.rfind(' ')
    
    if last_space > max_length * 0.8:
        return truncated[:last_space] + '...'
    else:
        return truncated + '...'

def generate_brief(messages):
    """Generate news brief in Vietnamese with clean formatting"""
    if not messages:
        return None
    
    now = datetime.now()
    
    # Group by topic and score
    topic_messages = defaultdict(list)
    
    for msg in messages:
        topic = msg.get('topic', 'unknown')
        topic_config = TOPICS.get(topic, {})
        
        if not topic_config.get('enabled', False):
            continue
        
        score, keywords = score_message(msg, topic_config)
        min_score = topic_config.get('selection', {}).get('worth_reading', {}).get('min_score', 40)
        
        if score >= min_score:
            topic_messages[topic].append({
                **msg,
                'score': score,
                'keywords': keywords
            })
    
    # Sort by score descending
    for topic in topic_messages:
        topic_messages[topic].sort(key=lambda x: x['score'], reverse=True)
    
    # Generate brief with clean formatting
    lines = []
    lines.append("📰 TIN TỨC TỔNG HỢP")
    lines.append(f"{now.strftime('%H:%M %d/%m/%Y')}")
    lines.append("")
    lines.append("━━━━━━━━━━━━━━")
    lines.append("")
    
    # Top Stories (cross-topic, highest scores)
    all_scored = []
    for topic, msgs in topic_messages.items():
        for msg in msgs[:3]:
            all_scored.append({
                'topic': topic,
                **msg
            })
    
    all_scored.sort(key=lambda x: x['score'], reverse=True)
    
    if all_scored:
        lines.append("🔥 TIN NÓNG")
        for msg in all_scored[:5]:
            text = truncate_text(msg['text'], 140)
            source = msg.get('source_name', msg.get('source', 'Unknown'))
            # Plain text, no markdown
            lines.append(f"• {text} ({source})")
        lines.append("")
        lines.append("━━━━━━━━━━━━━━")
        lines.append("")
    
    # Per-topic sections
    for topic_key, topic_config in TOPICS.items():
        if not topic_config.get('enabled', False):
            continue
        
        msgs = topic_messages.get(topic_key, [])
        if not msgs:
            continue
        
        icon = topic_config.get('icon', '📌')
        name = topic_config.get('display_name', topic_key)
        max_items = topic_config.get('selection', {}).get('worth_reading', {}).get('max', 5)
        
        lines.append(f"{icon} {name.upper()} — ĐANG ĐỌC")
        
        for msg in msgs[:max_items]:
            text = truncate_text(msg['text'], 140)
            source = msg.get('source_name', msg.get('source', 'Unknown'))
            # Plain text, no markdown formatting
            lines.append(f"• {text} ({source})")
        
        lines.append("")
    
    lines.append("━━━━━━━━━━━━━━")
    lines.append(f"Được tạo bởi Hermes · {len(messages)} tin đã xử lý")
    
    return '\n'.join(lines)

def save_markdown(brief_text, session='brief'):
    """Save brief to markdown file"""
    base_path = OUTPUT_SETTINGS['markdown']['path']
    date_str = datetime.now().strftime('%Y-%m-%d')
    time_str = datetime.now().strftime('%H%M')
    
    # Create directory
    date_path = os.path.join(base_path, date_str)
    os.makedirs(date_path, exist_ok=True)
    
    # Save file
    filename = f"{session}_{time_str}.md"
    filepath = os.path.join(date_path, filename)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(brief_text)
    
    return filepath

async def send_to_telegram(brief_text):
    """Send brief to Telegram using plain text"""
    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
        print("❌ Telegram not configured")
        return False
    
    try:
        bot = Bot(token=TELEGRAM_BOT_TOKEN)
        
        # Split long messages (Telegram limit: 4096 chars)
        max_length = 4000
        messages = []
        
        if len(brief_text) <= max_length:
            messages.append(brief_text)
        else:
            # Split by sections
            lines = brief_text.split('\n')
            current = ""
            
            for line in lines:
                if len(current) + len(line) + 1 > max_length:
                    messages.append(current)
                    current = line + '\n'
                else:
                    current += line + '\n'
            
            if current:
                messages.append(current)
        
        # Send messages (plain text, no markdown parsing)
        for i, msg in enumerate(messages):
            if i > 0:
                await asyncio.sleep(1)
            
            # Use no parse_mode or HTML with proper escaping
            await bot.send_message(
                chat_id=TELEGRAM_CHAT_ID,
                text=msg
                # No parse_mode - plain text
            )
        
        print(f"✅ Sent {len(messages)} message(s) to Telegram")
        return True
        
    except Exception as e:
        print(f"❌ Failed to send: {e}")
        return False

def main():
    print("=" * 60)
    print("📝 News Brief Synthesizer")
    print("=" * 60)
    print()
    
    # Load data
    messages = load_scraped_data()
    print(f"📊 Loaded {len(messages)} messages")
    print()
    
    if not messages:
        print("⚠️  No messages to process")
        return
    
    # Generate brief
    brief = generate_brief(messages)
    
    if not brief:
        print("⚠️  No brief generated (no matching messages)")
        return
    
    # Print brief
    print(brief)
    print()
    
    # Save to file
    filepath = save_markdown(brief)
    print(f"💾 Saved to: {filepath}")
    print()
    
    # Send to Telegram
    if OUTPUT_SETTINGS['telegram']['enabled']:
        print("📤 Sending to Telegram...")
        result = asyncio.run(send_to_telegram(brief))
        
        if result:
            print("✅ Brief delivered!")
        else:
            print("⚠️  Failed to send to Telegram")
    
    print()
    print("=" * 60)
    print("✅ Done!")

if __name__ == '__main__':
    main()
