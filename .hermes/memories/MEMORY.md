KB gitignore/untrack patterns (đã thiết lập 2026-05-12):
- Hermes runtime: .hermes/auth/, .hermes/auth.json, .hermes/channel_directory.json, .hermes/state.db*, .hermes/logs/, .hermes/sessions/, .hermes/cron/
- Obsidian UI config: .obsidian/graph.json, .obsidian/workspace.json
Tất cả đã bị xóa khỏi git history (filter-branch) hoặc untrack (git rm --cached).
§
Julius syncs knowledge-base between 2 machines via Obsidian Git plugin. Máy chính: auto-commit 5min, auto-pull 30s, auto-push OFF. VPS: auto-push ON. mergeStrategy="", syncMethod="merge". After force pushes: `git fetch && git reset --hard origin/master`. Máy chính SSH, VPS HTTPS. Paths: VPS=/home/julius/knowledge-base, máy chính=/home/julius/julius-workspace/knowledge-base.
§
On this VPS, Hermes cron `create` with cron expression (`0 15 * * *`) fails with "Cron expressions require 'croniter' package" even after installing croniter in venv. Workaround: use interval format like `24h` instead. First run is calculated from creation time, so create it at the desired start time.
§
Máy chính working dir: /home/julius/julius-workspace/knowledge-base (KHÁC với VPS: /home/julius/knowledge-base). Obsidian Git plugin trên máy chính auto-sync cạnh tranh lock với git CLI thủ công — cần tắt Obsidian hoặc plugin trước khi chạy git merge/push. Micro editor để lại backup MERGE_MSG ở ~/.config/micro/backups/ — mỗi merge sẽ prompt [r]ecover/[i]gnore/[a]bort, chọn 'i'.
§
Validation pipeline (2026-05-14): Kara compile 08:00 (kimi-k2.5), index 21:00 (gemma-4-31b). Connor validate 23:00 Output / 23:15 Format / 23:30 Hygiene (all glm-5.1 via opencode). Cron jobs created on VPS via `hermes cron create` — cron expressions work on VPS (croniter available). Hermes gateway scheduler auto-fires, no Linux crontab needed. Job IDs: d48e30a9a963, d14687442111, f1ff44c008e2.