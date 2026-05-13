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

Even after installing `croniter` in both the venv and globally (`--break-system-packages`), the error persists intermittently. The cron scheduler may use a different Python than expected.

The `24h` interval works but starts counting from creation time — to anchor it at 23:00, you'd need to create the job at exactly 23:00.

## Solution: Bootstrap pattern

Use a **one-shot timestamped job** that:
1. Fires at the exact desired hour
2. Creates the real recurring `24h` job (now anchored correctly)
3. Self-destructs

### Template

```python
cronjob(
    action="create",
    name="Bootstrap [Validator Name]",
    schedule="YYYY-MM-DDT23:00:00+07:00",   # exact ISO timestamp
    repeat=1,                                  # one-shot
    deliver="local",                           # no notification needed
    skills=["skill-name"],
    model={"provider": "opencode", "model": "glm-5.1"},
    prompt="Tạo recurring cron job tên \"KB [Name] Daily\", schedule 24h, skill [skill], deliver telegram, model opencode/glm-5.1. Prompt: \"[task description]\" Sau đó tự xóa chính job này."
)
```

### Knowledge Base validation pipeline

Three validators chạy tuần tự mỗi tối, mỗi job cách nhau 15 phút:

| Giờ | Job | Skill |
|---|---|---|
| 23:00 | KB Output Validator Daily | output-validator |
| 23:15 | KB Format Validator Daily | format-validator |
| 23:30 | KB Hygiene Inspector Daily | hygiene-inspector |

All three use `opencode/glm-5.1` to avoid dependency on Google API (which may have leaked key issues).

### Hygiene Inspector special behavior

This is the last validator — it updates `wiki/reviews/_action-required.md` with a summary of all three validators, not just its own findings. Include this in its prompt.

## Cron list

```bash
cronjob(action="list")
```

Returns all jobs with IDs, names, schedules, and statuses.

## Removing jobs

```bash
cronjob(action="remove", job_id="<id>")
```

Common scenario: bootstrap job created at wrong time → `remove` it → recalculate timestamp → recreate.

## Model format

Models must be specified as objects, not strings:

```python
model={"provider": "opencode", "model": "glm-5.1"}
```

String format like `"opencode/glm-5.1"` will result in `model: null` in the created job.

## Pitfalls

- **Bootstrap jobs are fragile** — if the gateway restarts before the bootstrap fires, the job is lost and no recurring job will exist. After gateway restarts, always check `cronjob(action="list")`.
- **Timestamp must be in the future** — ISO timestamps in the past will cause the job to fire immediately or never.
- **`repeat=1` is one-shot** — without this, the bootstrap would keep creating duplicate recurring jobs.
- **Timezone must be explicit** — use `+07:00` for Vietnam time, not UTC.
- **Stale bootstrap jobs** — if you create a bootstrap at the wrong time, remove it immediately (don't just create another). Otherwise both will fire and create duplicate recurring jobs.
- **Cron expressions don't work** — don't waste time trying `"0 23 * * *"` format. Use the bootstrap pattern.
