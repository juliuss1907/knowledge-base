#!/usr/bin/env python3
from config import TOPICS

print("RSS Sources Check:")
print("=" * 50)

for k, v in TOPICS.items():
    rss = v.get('sources', {}).get('rss', [])
    if rss:
        print(f"\n{k}: {len(rss)} RSS source(s)")
        for r in rss:
            enabled = r.get('enabled', True)
            status = '✅' if enabled else '❌'
            print(f"  {status} {r.get('name', 'unknown')}")
    else:
        print(f"\n{k}: No RSS sources")
