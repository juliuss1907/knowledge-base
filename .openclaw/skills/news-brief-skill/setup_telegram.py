#!/usr/bin/env python3
"""
Setup Telegram authentication for News Brief Skill
Usage: python3 setup_telegram.py
"""
import asyncio
import os
from telethon import TelegramClient
from telethon.sessions import StringSession
from config import TELEGRAM_API_ID, TELEGRAM_API_HASH

SESSION_FILE = 'hermes_session'
PHONE = '+84869161860'

async def main():
    print(f"🔐 Setting up Telegram authentication...")
    print(f"Phone: {PHONE}")
    print("-" * 50)
    
    client = TelegramClient(SESSION_FILE, TELEGRAM_API_ID, TELEGRAM_API_HASH)
    
    try:
        await client.connect()
        
        if await client.is_user_authorized():
            print("✅ Already authorized!")
            me = await client.get_me()
            print(f"User: {me.first_name} (@{me.username})")
            return
        
        print(f"📱 Sending code to {PHONE}...")
        sent = await client.send_code_request(PHONE)
        print(f"✅ Code sent! phone_code_hash: {sent.phone_code_hash[:20]}...")
        print("-" * 50)
        print("💡 IMPORTANT: The code was sent to your Telegram app.")
        print("   Check your Telegram messages (look for 'Telegram' official)")
        print("-" * 50)
        
        # Wait for user input
        code = input("\n⌨️  Enter the 5-digit code: ").strip()
        print(f"📝 Code entered: {code}")
        
        try:
            await client.sign_in(PHONE, code)
            print("✅ Authentication successful!")
            me = await client.get_me()
            print(f"User: {me.first_name} (@{me.username})")
        except Exception as e:
            print(f"❌ Sign in failed: {e}")
            print("💡 If code expired, please run this script again")
            
    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        await client.disconnect()

if __name__ == '__main__':
    asyncio.run(main())
