KB gitignore: .hermes/auth/, .hermes/auth.json, .hermes/channel_directory.json, .hermes/state.db*, .hermes/logs/, .hermes/sessions/, .hermes/cron/, .obsidian/graph.json, .obsidian/workspace.json. Đã clean git history.
§
Julius syncs knowledge-base between 2 machines via Obsidian Git plugin. Máy chính: auto-commit 5min, auto-pull 30s, auto-push OFF. VPS: auto-push ON. mergeStrategy="", syncMethod="merge". After force pushes: `git fetch && git reset --hard origin/master`. Máy chính SSH, VPS HTTPS. Paths: VPS=/home/julius/knowledge-base, máy chính=/home/julius/julius-workspace/knowledge-base.
§
On this VPS, Hermes cron `create` with cron expression (`0 15 * * *`) fails with "Cron expressions require 'croniter' package" even after installing croniter in venv. Workaround: use interval format like `24h` instead. First run is calculated from creation time, so create it at the desired start time.
§
Máy chính working dir: /home/julius/julius-workspace/knowledge-base (KHÁC với VPS: /home/julius/knowledge-base). Obsidian Git plugin trên máy chính auto-sync cạnh tranh lock với git CLI thủ công — cần tắt Obsidian hoặc plugin trước khi chạy git merge/push. Micro editor để lại backup MERGE_MSG ở ~/.config/micro/backups/ — mỗi merge sẽ prompt [r]ecover/[i]gnore/[a]bort, chọn 'i'.
§
Validation pipeline (2026-05-14): Kara compile 08:00 (kimi-k2.5), index 21:00 (gemma-4-31b). Connor validate 23:00 Output / 23:15 Format / 23:30 Hygiene (all glm-5.1 via opencode). Cron jobs created on VPS via `hermes cron create` — cron expressions work on VPS (croniter available). Hermes gateway scheduler auto-fires, no Linux crontab needed. Job IDs: d48e30a9a963, d14687442111, f1ff44c008e2.
§
Connor (Hermes) QUY TẮC CỨNG: KHÔNG tự sửa file trong wiki/concepts/. Chỉ validate + report. Việc sửa lỗi (compile lại, format, hygiene) thuộc về Kara (Compile Agent). Connor chỉ ghi verdict vào wiki/reviews/, không được patch/sửa bất kỳ concept file nào.
§
X News Brief — model quá nhẹ: glm-5.1 scrape 50 items (210KB, 34 msg) xong hết context, chỉ trả summary metadata 361 chars thay vì brief format. Fix: model mạnh hơn (deepseek-v4-pro) hoặc tách scrape/synthesize.