#!/usr/bin/env python3
"""Final auth with copy-paste prompt"""
import asyncio
from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError
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
    
    sent = await client.send_code_request(PHONE)
    print(f"=" * 60)
    print(f"📱 Code sent to: {PHONE}")
    print(f"=" * 60)
    print(f"\n⏰ Check Telegram app for the code")
    print(f"⚠️  Enter the EXACT code shown in Telegram\n")
    
    code = input("🔑 Enter the 5-digit code from Telegram: ").strip()
    print(f"\n📝 Code entered: '{code}'")
    print(f"📊 Code length: {len(code)} characters")
    
    try:
        await client.sign_in(PHONE, code, phone_code_hash=sent.phone_code_hash)
        me = await client.get_me()
        print(f"\n✅ AUTHENTICATION SUCCESSFUL!")
        print(f"👤 User: {me.first_name} {me.last_name or ''}")
        print(f"📱 Username: @{me.username}")
        print(f"🆔 ID: {me.id}")
    except Exception as e:
        print(f"\n❌ Authentication failed: {e}")
        print(f"\n💡 Tips:")
        print(f"   - Make sure you're entering the latest code")
        print(f"   - Code expires after 60 seconds")
        print(f"   - Check if you have 2FA enabled on your account")
    finally:
        await client.disconnect()

asyncio.run(main())
