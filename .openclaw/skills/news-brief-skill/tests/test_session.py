#!/usr/bin/env python3
"""Test if Telegram session is valid"""
import asyncio
from telethon import TelegramClient
from config import TELEGRAM_API_ID, TELEGRAM_API_HASH

SESSION_FILE = 'hermes_session'

async def main():
    client = TelegramClient(SESSION_FILE, TELEGRAM_API_ID, TELEGRAM_API_HASH)
    try:
        await client.connect()
        if await client.is_user_authorized():
            me = await client.get_me()
            print(f"✅ Session valid!")
            print(f"User: {me.first_name} {me.last_name or ''} (@{me.username})")
            print(f"ID: {me.id}")
            return True
        else:
            print("❌ Session exists but not authorized")
            return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False
    finally:
        await client.disconnect()

if __name__ == '__main__':
    result = asyncio.run(main())
    exit(0 if result else 1)
