#!/usr/bin/env python3
import sys, asyncio
from telethon import TelegramClient
from config import TELEGRAM_API_ID, TELEGRAM_API_HASH

SESSION_FILE = 'hermes_session'
HASH_FILE = '/tmp/telegram_hash.txt'

async def main():
    client = TelegramClient(SESSION_FILE, TELEGRAM_API_ID, TELEGRAM_API_HASH)
    if '--code' in sys.argv:
        idx = sys.argv.index('--code')
        code = sys.argv[idx + 1]
        with open(HASH_FILE) as f:
            phone, phone_code_hash = f.read().strip().split('\n')
        async with client:
            await client.sign_in(phone, code, phone_code_hash=phone_code_hash)
        print('✅ Authentication successful!')
    else:
        phone = sys.argv[1]
        async with client:
            sent = await client.send_code_request(phone)
        with open(HASH_FILE, 'w') as f:
            f.write(f'{phone}\n{sent.phone_code_hash}\n')
        print(f'✅ OTP sent to {phone}!')
        print(f'Run: python3 auth_telegram.py --code <OTP>')

asyncio.run(main())
