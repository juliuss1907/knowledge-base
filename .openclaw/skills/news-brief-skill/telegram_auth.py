#!/usr/bin/env python3
"""
Telegram Authentication Script for News Brief Skill
Run: python3 telegram_auth.py
"""
import asyncio
import sys
from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError, PhoneCodeInvalidError

# Telegram API Credentials
TELEGRAM_API_ID = 35676903
TELEGRAM_API_HASH = 'bd6c6e8b4eeee4d88d210aa29e45601e'
PHONE = '+84869161860'
SESSION_FILE = 'hermes_session'

async def main():
    print("=" * 60)
    print("🔐 Telegram Authentication for News Brief Skill")
    print("=" * 60)
    print()
    
    # Create client
    client = TelegramClient(SESSION_FILE, TELEGRAM_API_ID, TELEGRAM_API_HASH)
    await client.connect()
    
    # Check if already authorized
    if await client.is_user_authorized():
        me = await client.get_me()
        print(f"✅ Already authenticated!")
        print(f"👤 User: {me.first_name} {me.last_name or ''}")
        print(f"📱 Username: @{me.username}")
        await client.disconnect()
        return 0
    
    # Step 1: Send verification code
    print(f"📱 Sending verification code to: {PHONE}")
    try:
        sent = await client.send_code_request(PHONE)
        print(f"✅ Code sent successfully!")
        print()
        print("⚠️  IMPORTANT: Code expires in 60 seconds!")
        print("📲 Check your Telegram app for the code...")
        print()
    except Exception as e:
        print(f"❌ Failed to send code: {e}")
        await client.disconnect()
        return 1
    
    # Step 2: Get code from user
    try:
        code = input("🔑 Enter the 5-digit code from Telegram: ").strip()
        
        if not code.isdigit() or len(code) != 5:
            print(f"❌ Invalid code format. Expected 5 digits.")
            await client.disconnect()
            return 1
        
        print(f"\n📝 Verifying code: {code}")
        print("⏳ Please wait...")
        
        # Step 3: Sign in
        await client.sign_in(PHONE, code, phone_code_hash=sent.phone_code_hash)
        
        # Success!
        me = await client.get_me()
        print()
        print("=" * 60)
        print("✅ AUTHENTICATION SUCCESSFUL!")
        print("=" * 60)
        print(f"👤 Name: {me.first_name} {me.last_name or ''}")
        print(f"📱 Username: @{me.username}")
        print(f"🆔 ID: {me.id}")
        print(f"📁 Session saved to: {SESSION_FILE}.session")
        print()
        print("You can now run: python3 scrape.py")
        
        await client.disconnect()
        return 0
        
    except PhoneCodeInvalidError:
        print("\n❌ Invalid code!")
        print("💡 Tips:")
        print("   - Make sure you entered the code correctly")
        print("   - Code expires after 60 seconds")
        print("   - Run this script again to get a new code")
        await client.disconnect()
        return 1
        
    except SessionPasswordNeededError:
        print("\n🔒 Two-factor authentication required!")
        password = input("Enter your 2FA password: ").strip()
        try:
            await client.sign_in(password=password)
            me = await client.get_me()
            print(f"\n✅ Authenticated: {me.first_name} (@{me.username})")
            await client.disconnect()
            return 0
        except Exception as e:
            print(f"\n❌ 2FA failed: {e}")
            await client.disconnect()
            return 1
            
    except Exception as e:
        print(f"\n❌ Authentication failed: {e}")
        await client.disconnect()
        return 1

if __name__ == '__main__':
    result = asyncio.run(main())
    sys.exit(result)
