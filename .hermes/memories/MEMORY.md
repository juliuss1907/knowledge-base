KB gitignore patterns for Hermes runtime (đã thiết lập 2026-05-12): .hermes/auth/, .hermes/auth.json, .hermes/channel_directory.json, .hermes/state.db*, .hermes/logs/, .hermes/sessions/, .hermes/cron/. Các file này đã bị xóa khỏi git history bằng filter-branch và sẽ không còn bị track.
§
Julius syncs knowledge-base between 2 machines (VPS + main machine) via Obsidian Git plugin with auto-commit/push/pull. After force pushes, the other machine must run `git fetch origin && git reset --hard origin/master` — normal pull won't work.
§
On this VPS, Hermes cron `create` with cron expression (`0 15 * * *`) fails with "Cron expressions require 'croniter' package" even after installing croniter in venv. Workaround: use interval format like `24h` instead. First run is calculated from creation time, so create it at the desired start time.
§
Daily validation pipeline schedule (finalized 2026-05-12):
- 08:00 OpenClaw Kara: Compile raw → wiki (model: ollama/kimi-k2.5:cloud)
- 21:00 OpenClaw Kara: Index tag/topic (model: google/gemma-4-31b-it)
- 23:00 Hermes Connor: Output Validator — quality check (model: opencode/glm-5.1)
- 23:15 Hermes Connor: Format Validator — structure check (model: opencode/glm-5.1)
- 23:30 Hermes Connor: Hygiene Inspector — folder check (model: opencode/glm-5.1)
OpenClaw cron managed separately via `openclaw cron` (Go-based). Hermes cron managed via `hermes cron` / cronjob tool (Python-based, requires croniter package). When creating Hermes cron jobs, use model object format `{provider: "opencode", model: "glm-5.1"}`.