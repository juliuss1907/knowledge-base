#!/usr/bin/env python3
import sys
import asyncio
from telethon import TelegramClient
from config import TELEGRAM_API_ID, TELEGRAM_API_HASH

SESSION_FILE = 'hermes_session'
HASH_FILE = '/tmp/telegram_hash.txt'

async def send_code(phone):
    client = TelegramClient(SESSION_FILE, TELEGRAM_API_ID, TELEGRAM_API_HASH)
    await client.connect()
    
    if await client.is_user_authorized():
        print("Already authenticated!")
        await client.disconnect()
        return True
    
    print(f"Sending OTP to {phone}...")
    result = await client.send_code_request(phone)
    
    # Save phone_code_hash
    with open(HASH_FILE, 'w') as f:
        f.write(f"{phone}\n{result.phone_code_hash}")
    
    print(f"✅ OTP sent to {phone}!")
    print(f"Run: python auth_telegram.py --code <OTP>")
    await client.disconnect()
    return False

async def login_with_code(code):
    # Read phone and hash from file
    try:
        with open(HASH_FILE, 'r') as f:
            phone = f.readline().strip()
            phone_code_hash = f.readline().strip()
    except FileNotFoundError:
        print("Error: No pending authentication found. Run first: python auth_telegram.py <phone>")
        return False
    
    client = TelegramClient(SESSION_FILE, TELEGRAM_API_ID, TELEGRAM_API_HASH)
    await client.connect()
    
    try:
        await client.sign_in(phone, code, phone_code_hash=phone_code_hash)
        print("✅ Authentication successful!")
        print("Session saved.")
        await client.disconnect()
        
        # Clean up hash file
        import os
        os.remove(HASH_FILE)
        return True
    except Exception as e:
        print(f"Error: {e}")
        await client.disconnect()
        return False

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage:")
        print("  Step 1: python auth_telegram.py +84869161860")
        print("  Step 2: python auth_telegram.py --code 12345")
        sys.exit(1)
    
    if sys.argv[1] == '--code':
        if len(sys.argv) < 3:
            print("Error: Please provide OTP code")
            sys.exit(1)
        code = sys.argv[2]
        asyncio.run(login_with_code(code))
    else:
        phone = sys.argv[1]
        asyncio.run(send_code(phone))
