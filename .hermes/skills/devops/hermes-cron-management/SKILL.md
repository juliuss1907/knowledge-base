---
name: hermes-cron-management
description: Create and manage recurring Hermes cron jobs at specific wall-clock times. Uses a bootstrap pattern to work around the limitation that cron expressions are unsupported (require croniter package that doesn't work reliably).
category: devops
---

# Hermes Cron Management

Workflow for creating recurring Hermes cron jobs that run at specific wall-clock times.

## The problem

`hermes cron create` with cron expressions like `"0 23 * * *"` fails with:
```
Cron expressions require 'croniter' package. Install with: pip install croniter
```

The code (`cron/jobs.py` line 150-166) DOES support cron expressions, but it gates on `HAS_CRONITER` from `import croniter`. Even after installing `croniter` in both the venv (where hermes-agent lives) AND globally (`--break-system-packages`), the Python runtime used by the Hermes scheduler process cannot resolve `croniter`.

The `every 1d` / `every 1440m` interval format works for recurring but starts counting from creation time — to anchor it at 23:00, you'd need to create the job at exactly 23:00.

## Solution: Use system crontab (recommended)

The Hermes cron scheduler is unreliable for daily wall-clock jobs. Use Linux `crontab` instead:

```bash
crontab -e
```

Add these entries:

```cron
# Knowledge Base Validation Pipeline
0  23 * * * cd ~/knowledge-base && hermes cron run 3c3b96dbdea6  # Output Validator
15 23 * * * cd ~/knowledge-base && hermes cron run 44412beced6c  # Format Validator
30 23 * * * cd ~/knowledge-base && hermes cron run bbcdaf907f0a  # Hygiene Inspector
```

### How this works

1. Each Hermes job is a **one-shot** with ISO timestamp `2026-05-14T23:00:00+07:00` (repeat=1)
2. Linux cron triggers `hermes cron run <job_id>` at the exact time
3. After the job completes (one-shot, repeat limit reached), it auto-deletes
4. No recurring state to manage — Linux cron IS the recurrence

### Recreating daily

Since jobs self-destruct after running, you need to recreate them daily. The simplest approach: create a wrapper script that creates 3 one-shot jobs for today, then runs them.

```bash
#!/bin/bash
# ~/knowledge-base/.hermes/scripts/daily-validation.sh
NOW=$(date +%Y-%m-%d)
hermes cron create --schedule "${NOW}T23:00:00+07:00" --repeat 1 --skill output-validator ...
hermes cron create --schedule "${NOW}T23:15:00+07:00" --repeat 1 --skill format-validator ...
hermes cron create --schedule "${NOW}T23:30:00+07:00" --repeat 1 --skill hygiene-inspector ...
```

Then in crontab: `0 22 * * * /path/to/daily-validation.sh` (creates jobs 1h before they fire).

## Alternative: `every 1440m` with caveat

If you must use Hermes scheduler (e.g., gateway restart persistence):

```python
cronjob(
    action="create",
    name="KB Output Validator Daily",
    schedule="every 1440m",   # 24h recurring — first run: NOW + 24h
    repeat=None,               # forever
    deliver="origin",
    skills=["output-validator"],
    prompt="..."
)
```

**Caveat:** First run is 24h from creation time. If created at 15:50, it runs daily at 15:50, not 23:00. To anchor at a specific time, you must create the job at exactly that time (e.g., wake up at 23:00 and create it).

## Knowledge Base validation pipeline

Three validators chạy tuần tự mỗi tối, mỗi job cách nhau 15 phút:

| Giờ | Job | Skill |
|---|---|---|
| 23:00 | KB Output Validator Daily | output-validator |
| 23:15 | KB Format Validator Daily | format-validator |
| 23:30 | KB Hygiene Inspector Daily | hygiene-inspector |

All three use `opencode/glm-5.1` to avoid dependency on Google API (which may have leaked key issues).

## Cron list

```bash
cronjob(action="list")
```

Returns all jobs with IDs, names, schedules, and statuses.

## Removing jobs

```bash
cronjob(action="remove", job_id="<id>")
```

Common scenario: job created at wrong time → `remove` it → recalculate timestamp → recreate.

## Model format

Models must be specified as objects, not strings:

```python
model={"provider": "opencode", "model": "glm-5.1"}
```

String format like `"opencode/glm-5.1"` will result in `model: null` in the created job.

## Pitfalls

- **Cron expressions will NEVER work in Hermes** — the `HAS_CRONITER` check fails because the scheduler's Python runtime (not the venv, not system Python) cannot import `croniter`. Don't waste time trying to install it.
- **`every 1d` != daily at fixed time** — it's 24h from creation. Only use if you can create the job at the exact desired hour.
- **One-shot jobs are fragile** — they self-destruct after running. If the gateway restarts before they fire, they're lost. Always check `cronjob(action="list")` after restarts.
- **Timestamp must be in the future** — ISO timestamps in the past will cause the job to fire immediately or never.
- **`repeat=1` is one-shot** — if you want a one-shot, specify `repeat=1`. Without `repeat`, a one-shot schedule auto-sets `repeat=1` anyway.
- **Timezone must be explicit** — use `+07:00` for Vietnam time, not UTC.
- **Bootstrap pattern is NOT recommended** — the bootstrap job itself is a one-shot that dies if gateway restarts. When it fails, no recurring job exists and you don't know it failed. Use system crontab instead.
