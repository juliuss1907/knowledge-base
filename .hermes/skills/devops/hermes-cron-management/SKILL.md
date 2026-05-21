---
name: hermes-cron-management
description: Create and manage recurring Hermes cron jobs at specific wall-clock times. Cron expressions work via hermes cron create CLI, but NOT via the cronjob tool (HAS_CRONITER=False in that runtime).
category: devops
---

# Hermes Cron Management

Guide to creating recurring daily Hermes cron jobs that fire at specific wall-clock times.

## The key discovery

**`cronjob` tool ≠ `hermes cron create` CLI.** They run in different Python processes:

| Method | Cron expressions | Works? |
|---|---|---|
| `cronjob` tool (from agent) | `"0 23 * * *"` | ❌ FAILS — `HAS_CRONITER=False` in agent's Python runtime |
| `hermes cron create` CLI (on VPS/machine) | `"0 23 * * *"` | ✅ WORKS — VPS Hermes has `croniter` in its venv |

The `cronjob` tool's runtime cannot import `croniter` (even after installing it into the hermes venv). But running `hermes cron create` directly on the VPS terminal DOES work because the CLI uses the correct venv where `croniter` is installed.

## For users: How to create recurring daily jobs

Run these commands directly on the **VPS terminal** (not through the agent):

```bash
cd ~/knowledge-base

# Output Validator — 23:00 daily
hermes cron create \
  --name "Output Validator" \
  --deliver origin \
  --skill output-validator \
  "0 23 * * *" \
  "Chạy Output Validator: đọc toàn bộ wiki/sources/*.md và wiki/concepts/*.md, validate content quality theo 4 dimensions. Viết report, gửi Telegram. Read-only. Giới hạn top 20 issues."

# Format Validator — 23:15 daily
hermes cron create \
  --name "Format Validator" \
  --deliver origin \
  --skill format-validator \
  "15 23 * * *" \
  "Chạy Format Validator: đọc format-spec.md và toàn bộ wiki, validate format compliance 4 categories. Viết report, gửi Telegram. Read-only. Giới hạn top 20 issues."

# Hygiene Inspector — 23:30 daily
hermes cron create \
  --name "Hygiene Inspector" \
  --deliver origin \
  --skill hygiene-inspector \
  "30 23 * * *" \
  "Chạy Hygiene Inspector: đọc folder-structure.md, scan toàn bộ cây thư mục, validate 3 dimensions. Viết report, gửi Telegram. Read-only. Giới hạn top 20 issues."
```

**No Linux crontab needed.** Hermes scheduler handles recurrence automatically. Jobs persist in `~/.hermes/cron/jobs.json`.

## For agents: What you CAN and CANNOT do

### ✅ You CAN do via `cronjob` tool:
- `cronjob(action="list")` — check existing jobs
- `cronjob(action="remove", job_id="...")` — delete jobs
- `cronjob(action="create", schedule="<ISO timestamp>", repeat=1)` — one-shot jobs
- `cronjob(action="create", schedule="every 1440m")` — recurring with interval (but first run is NOW + 24h, not anchored)

### ❌ You CANNOT do via `cronjob` tool:
- `cronjob(action="create", schedule="0 23 * * *")` — will fail with "Cron expressions require 'croniter'"
- `cronjob(action="create", schedule="every day at 23:00")` — invalid duration format

### Workaround when user needs recurring daily jobs:
1. Tell user to run `hermes cron create` commands directly on VPS terminal
2. OR: create one-shot jobs for today, then remind user to recreate tomorrow
3. OR: use `every 1440m` and accept the 24h-from-now timing (not anchored to specific hour)

## Verifying jobs are active

```bash
# On VPS
hermes cron status   # Must show "Gateway is running"
hermes cron list     # Show all jobs with next run times
```

If gateway is NOT running, start it: `hermes gateway start` (or however the VPS starts Hermes).

## Removing old/duplicate jobs

```bash
hermes cron remove <job_id>
```

Common scenario: after creating recurring cron jobs, old one-shot jobs with same name still exist. Always `hermes cron list` and remove duplicates.

## Knowledge Base validation pipeline

Three validators chạy tuần tự mỗi tối:

| Giờ | Job | Skill | Model |
|---|---|---|---|
| 23:00 | Output Validator | output-validator | opencode/glm-5.1 |
| 23:15 | Format Validator | format-validator | opencode/glm-5.1 |
| 23:30 | Hygiene Inspector | hygiene-inspector | opencode/glm-5.1 |

All use model from skill's frontmatter (no `--model` flag on `hermes cron create`).

## Pitfalls

- **`cronjob` tool ≠ `hermes cron create`** — even if `croniter` is installed in the hermes venv, the agent's `cronjob` tool uses a different Python process that cannot import it. Don't try to install `croniter` via the agent — just tell the user to use the CLI.
- **Cron sessions don't run in KB root by default** — validation jobs that reference relative paths (e.g., `wiki/meta/format-spec.md`) will fail with FATAL if the session's working directory is wrong. **Always prepend `cd /home/julius/knowledge-base &&` to every KB validation cron prompt.** This was the root cause of Format Validator FATAL on 2026-05-20.
- **To fix existing cron prompts**: use `hermes cron edit <job_id> --prompt "cd /home/julius/knowledge-base && <original prompt>"` on the VPS terminal. Note: editing prompt with `--schedule` at the same time requires croniter — do them in separate commands if needed.
- **Job IDs are machine-specific** — jobs created via `cronjob` tool go to `~/.hermes/cron/jobs.json` on the CURRENT machine. If you're on the main machine, the VPS won't see them. Always create jobs directly on the machine where the scheduler runs.
- **`cronjob` tool list shows current machine only** — use `hermes cron list` on the target machine to see what's actually scheduled.
- **`--model` flag not available** — `hermes cron create` doesn't have a `--model` flag. Model is determined by the skill's SKILL.md frontmatter.
- **`--deliver` defaults to `local` for CLI-created jobs** — when creating jobs from VPS terminal (not from within a chat), the default delivery is `local` (save to file only, no Telegram). Always explicitly add `--deliver origin` to `hermes cron create`. If you forgot, fix with `hermes cron edit <job_id> --deliver origin`.
- **`hermes cron edit` can fix deliver after creation** — `hermes cron edit <job_id> --deliver origin` changes the delivery target without recreating the job.
- **Editing schedule may require separate commands** — when using `hermes cron edit` with both `--schedule` and `--prompt`, cron expression parsing may fail even on VPS. Safer to update schedule and prompt in separate `hermes cron edit` calls.
- **Stale one-shot jobs accumulate** — after creating recurring cron jobs, old one-shot duplicates may persist. Always `hermes cron list` and remove them.
- **`jobs.json` is in `.gitignore`** — cron job definitions are NOT synced between machines. Each machine manages its own cron independently via Hermes scheduler.

## Maintenance: Cleaning up _action-required.md

After validating, old reports accumulate in `wiki/reviews/_action-required.md`. To prevent Kara (Fix Agent) from processing stale issues:

1. Mark all pre-target-date reports as resolved in the Summary section
2. Remove their entries from Critical Issues, Warnings, Info, and Pending Reports sections
3. Add them to Recently Applied with date of resolution
4. Update `Pending reports:` count and `Last updated:` timestamp

This keeps the action file focused on only the current pending work.
