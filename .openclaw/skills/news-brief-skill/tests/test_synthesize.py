#!/usr/bin/env python3
"""
News Brief Synthesizer - Generate brief from scraped data
"""
import json
import os
import re
from datetime import datetime
from collections import defaultdict
from config import TOPICS, GLOBAL_SETTINGS, OUTPUT_SETTINGS

def load_scraped_data():
    """Load latest scraped data"""
    json_files = [f for f in os.listdir('.') if f.startswith('test_scrape_') and f.endswith('.json')]
    if not json_files:
        return []
    
    latest_file = sorted(json_files)[-1]
    print(f"📂 Loading: {latest_file}")
    
    with open(latest_file, 'r') as f:
        return json.load(f)

def score_message(msg, topic_config):
    """Score a message based on keywords"""
    text = msg.get('text', '').lower()
    score = 0
    matched_keywords = []
    
    keywords = topic_config.get('keywords', {})
    
    # Tier 1 keywords
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
    if views > 10000:
        score += 20
    elif views > 1000:
        score += 10
    
    return score, matched_keywords

def truncate_text(text, max_length=200):
    """Truncate text to max length"""
    if len(text) <= max_length:
        return text
    return text[:max_length].rsplit(' ', 1)[0] + '...'

def generate_brief(messages):
    """Generate news brief"""
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
        
        if score >= 40:  # min_score
            topic_messages[topic].append({
                **msg,
                'score': score,
                'keywords': keywords
            })
    
    # Sort by score
    for topic in topic_messages:
        topic_messages[topic].sort(key=lambda x: x['score'], reverse=True)
    
    # Generate brief text
    lines = []
    lines.append("📰 *TIN TỨC TỔNG HỢP*")
    lines.append(f"{now.strftime('%H:%M %d/%m/%Y')}")
    lines.append("")
    lines.append("━━━━━━━━━━━━━━")
    lines.append("")
    
    # Top stories (highest scored across all topics)
    all_scored = []
    for topic, msgs in topic_messages.items():
        all_scored.extend(msgs[:3])  # Top 3 from each topic
    
    all_scored.sort(key=lambda x: x['score'], reverse=True)
    
    if all_scored[:5]:
        lines.append("🔥 *TIN NÓNG*")
        for msg in all_scored[:5]:
            text = truncate_text(msg['text'], 150)
            source = msg.get('source_name', msg.get('source', 'Unknown'))
            lines.append(f"• {text} _({source})_")
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
        
        lines.append(f"{icon} *{name.upper()} — ĐANG ĐỌC*")
        
        for msg in msgs[:5]:  # Top 5 per topic
            text = truncate_text(msg['text'], 150)
            source = msg.get('source_name', msg.get('source', 'Unknown'))
            score = msg.get('score', 0)
            lines.append(f"• {text} _({source}, score:{score})_")
        
        lines.append("")
    
    lines.append("━━━━━━━━━━━━━━")
    lines.append(f"Được tạo bởi Hermes · {len(messages)} tin")
    
    return '\n'.join(lines)

def save_markdown(brief_text, session='test'):
    """Save brief to markdown file"""
    import os
    
    base_path = OUTPUT_SETTINGS['markdown']['path']
    date_str = datetime.now().strftime('%Y-%m-%d')
    
    # Create directory
    date_path = os.path.join(base_path, date_str)
    os.makedirs(date_path, exist_ok=True)
    
    # Save file
    filename = f"{session}.md"
    filepath = os.path.join(date_path, filename)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(brief_text)
    
    return filepath

def main():
    print("=" * 60)
    print("📝 Synthesizing News Brief")
    print("=" * 60)
    print()
    
    # Load data
    messages = load_scraped_data()
    print(f"📊 Loaded {len(messages)} messages")
    print()
    
    # Generate brief
    brief = generate_brief(messages)
    
    if not brief:
        print("❌ No brief generated (no matching messages)")
        return
    
    # Print brief
    print(brief)
    print()
    
    # Save to file
    filepath = save_markdown(brief, 'test')
    print(f"💾 Saved to: {filepath}")
    
    print()
    print("✅ Synthesize complete!")

if __name__ == '__main__':
    main()
