#!/usr/bin/env python3
"""Quick auth with 2-step process"""
import asyncio
from telethon import TelegramClient
from config import TELEGRAM_API_ID, TELEGRAM_API_HASH

PHONE = '+84869161860'

async def send_code():
    """Step 1: Send code"""
    client = TelegramClient('hermes_session', TELEGRAM_API_ID, TELEGRAM_API_HASH)
    await client.connect()
    
    if await client.is_user_authorized():
        print("ALREADY_AUTH")
        await client.disconnect()
        return None
    
    result = await client.send_code_request(PHONE)
    await client.disconnect()
    return result.phone_code_hash

async def verify_code(code, phone_code_hash):
    """Step 2: Verify code"""
    client = TelegramClient('hermes_session', TELEGRAM_API_ID, TELEGRAM_API_HASH)
    await client.connect()
    
    try:
        await client.sign_in(PHONE, code, phone_code_hash=phone_code_hash)
        me = await client.get_me()
        print(f"SUCCESS:{me.first_name}:{me.username}")
    except Exception as e:
        print(f"FAILED:{e}")
    finally:
        await client.disconnect()

if __name__ == '__main__':
    import sys
    if len(sys.argv) == 1:
        # Send code
        hash = asyncio.run(send_code())
        if hash:
            print(f"CODE_SENT:{hash}")
    elif len(sys.argv) == 3 and sys.argv[1] == '--verify':
        # Verify code
        code = sys.argv[2]
        import os
        hash = os.environ.get('PHONE_CODE_HASH', '')
        asyncio.run(verify_code(code, hash))
