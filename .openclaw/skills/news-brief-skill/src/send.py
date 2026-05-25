#!/usr/bin/env python3
"""
Send brief to Telegram
"""
import asyncio
import os
import sys
from datetime import datetime
from telegram import Bot
from telegram.constants import ParseMode
from config import OUTPUT_SETTINGS

async def send_brief(brief_text=None, markdown_file=None):
    """Send brief to Telegram"""
    
    # Get config
    bot_token = OUTPUT_SETTINGS['telegram']['bot_token']
    chat_id = OUTPUT_SETTINGS['telegram']['chat_id']
    
    if not bot_token or not chat_id:
        print("❌ Telegram config missing!")
        return False
    
    # Load brief from file if not provided
    if not brief_text and markdown_file:
        if os.path.exists(markdown_file):
            with open(markdown_file, 'r', encoding='utf-8') as f:
                brief_text = f.read()
        else:
            print(f"❌ File not found: {markdown_file}")
            return False
    
    if not brief_text:
        print("❌ No brief content!")
        return False
    
    # Send to Telegram
    try:
        bot = Bot(token=bot_token)
        
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
        
        # Send messages
        for i, msg in enumerate(messages):
            if i > 0:
                await asyncio.sleep(1)  # Rate limit
            
            await bot.send_message(
                chat_id=chat_id,
                text=msg,
                parse_mode=ParseMode.MARKDOWN
            )
        
        print(f"✅ Sent {len(messages)} message(s) to Telegram")
        return True
        
    except Exception as e:
        print(f"❌ Failed to send: {e}")
        return False

def main():
    print("=" * 60)
    print("📤 Sending Brief to Telegram")
    print("=" * 60)
    print()
    
    # Find latest brief file
    base_path = OUTPUT_SETTINGS['markdown']['path']
    date_str = datetime.now().strftime('%Y-%m-%d')
    date_path = os.path.join(base_path, date_str)
    
    if len(sys.argv) > 1:
        # Use provided file
        markdown_file = sys.argv[1]
    else:
        # Find latest .md file
        if os.path.exists(date_path):
            md_files = [f for f in os.listdir(date_path) if f.endswith('.md')]
            if md_files:
                latest = sorted(md_files)[-1]
                markdown_file = os.path.join(date_path, latest)
            else:
                print(f"❌ No markdown files in {date_path}")
                return
        else:
            print(f"❌ Directory not found: {date_path}")
            return
    
    print(f"📄 File: {markdown_file}")
    print()
    
    # Send
    result = asyncio.run(send_brief(markdown_file=markdown_file))
    
    if result:
        print("✅ Done!")
    else:
        print("❌ Failed!")

if __name__ == '__main__':
    main()
