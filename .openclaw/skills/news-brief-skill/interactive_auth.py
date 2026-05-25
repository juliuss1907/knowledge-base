#!/usr/bin/env python3
"""Interactive auth - all in one step"""
import asyncio
from telethon import TelegramClient
from config import TELEGRAM_API_ID, TELEGRAM_API_HASH

PHONE = '+84869161860'

async def main():
    client = TelegramClient('hermes_session', TELEGRAM_API_ID, TELEGRAM_API_HASH)
    
    await client.connect()
    
    if await client.is_user_authorized():
        me = await client.get_me()
        print(f"✅ Already authorized: {me.first_name} (@{me.username})")
        await client.disconnect()
        return
    
    # Send code
    sent = await client.send_code_request(PHONE)
    print(f"📱 Code sent to {PHONE}")
    print("⚡ OTP expires in 60 seconds - enter NOW!")
    
    # Get code from user
    import sys
    code = input("\n🔑 Enter OTP: ").strip()
    print(f"Verifying {code}...")
    
    try:
        await client.sign_in(PHONE, code, phone_code_hash=sent.phone_code_hash)
        me = await client.get_me()
        print(f"✅ SUCCESS: {me.first_name} (@{me.username})")
    except Exception as e:
        print(f"❌ FAILED: {e}")
    finally:
        await client.disconnect()

asyncio.run(main())
