# Python Verification Script Template

Use this template when the system demands a `hermes-verify-` prefixed script after writing reports or approving. The built-in bash scripts (`verify-approval-batch.sh`, etc.) have specific use cases — this Python template handles generic pending-report verification.

## Usage

Write to `/tmp/hermes-verify-<date>.py`, run with `python3`, then `rm`.

## Template

```python
#!/usr/bin/env python3
"""Verify validation reports for a specific date."""
import os
import re

KB = "/home/julius/knowledge-base"
REVIEWS = f"{KB}/wiki/reviews"
DATE = "2026-08-01"  # CHANGE THIS
TYPES = ["format", "output", "hygiene"]

pass_c = fail_c = 0

def check(label, ok):
    global pass_c, fail_c
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")
    if ok: pass_c += 1
    else: fail_c += 1

print(f"=== hermes-verify {DATE} ===\n")

# 1. Report files exist and have pending/approved status
for t in TYPES:
    p = f"{REVIEWS}/{DATE}_{t}-report.md"
    ok = os.path.isfile(p) and os.path.getsize(p) > 500
    check(f"{t} report exists", ok)
    if ok:
        with open(p) as f:
            c = f.read()[:300]
        has_status = "pending" in c.lower() or "approved" in c.lower() or "clean" in c.lower()
        check(f"{t} report has status", has_status)

# 2. Dashboard checks
dp = f"{REVIEWS}/_action-required.md"
with open(dp) as f:
    dc = f.read()

# Check pending count (use regex to skip markdown bold)
m = re.search(r'Pending reports awaiting review:\*{0,2}\s*(\d+)', dc)
if m:
    pending_count = int(m.group(1))
    check(f"dashboard pending = {pending_count}", pending_count >= 0)
else:
    check("dashboard has pending count line", False)

# Check last updated
check("dashboard has last updated", "**Last updated:**" in dc)

# Check date entries in summary table
for t in TYPES:
    check(f"dashboard has {DATE} {t} row", f"{DATE} |" in dc and t.title() in dc)

# 3. Section headings in pending/approved sections
sections = dc.count(f"### 🔍") + dc.count(f"### ✅")
check(f"dashboard has report sections", sections > 0)

print(f"\n=== {pass_c} passed, {fail_c} failed ===")
```

## Common Pitfalls

1. **Markdown bold breaks `in` checks:** `"Issues found: 411" in content` FAILS because actual text is `**Issues found:** 411`. Use regex `re.search()` or match just the label.
2. **`pending` vs `PENDING`:** The dashboard uses `🔍 PENDING` (uppercase). Report files use `**Status:** pending` (lowercase). Match case-insensitively.
3. **Clean reports:** Hygiene reports with 0 issues may use `**Status:** clean` — this is valid, not a bug.
4. **Don't use bash scripts for pending verification:** `verify-approval-batch.sh` expects `**Status:** approved` — running it on pending reports produces 100% false failures.
