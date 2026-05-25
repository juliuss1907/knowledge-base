#!/usr/bin/env python3
from telethon import TelegramClient
from config import TELEGRAM_API_ID, TELEGRAM_API_HASH

print("Authenticating Telegram client...")
print(f"API ID: {TELEGRAM_API_ID}")
print(f"API Hash: {TELEGRAM_API_HASH[:10]}...")

client = TelegramClient('hermes_session', TELEGRAM_API_ID, TELEGRAM_API_HASH)

print("Starting client...")
print("Please enter your phone number when prompted (format: +84xxxxxxxxxx)")

client.start()

print("✅ Authentication successful!")
print("Session saved.")