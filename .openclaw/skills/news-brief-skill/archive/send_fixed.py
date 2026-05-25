#!/usr/bin/env python3
"""Send fixed brief to Telegram"""
import asyncio
from telegram import Bot
from config import OUTPUT_SETTINGS

TELEGRAM_BOT_TOKEN = OUTPUT_SETTINGS['telegram']['bot_token']
TELEGRAM_CHAT_ID = OUTPUT_SETTINGS['telegram']['chat_id']

async def main():
    bot = Bot(token=TELEGRAM_BOT_TOKEN)
    
    # Read the fixed brief
    with open('/home/julius/julius-workspace/personal/2026-05-25/brief_1151.md', 'r') as f:
        brief = f.read()
    
    # Send as plain text
    await bot.send_message(
        chat_id=TELEGRAM_CHAT_ID,
        text=brief
        # No parse_mode
    )
    
    print("✅ Fixed brief sent!")

asyncio.run(main())
