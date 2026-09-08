KB gitignore: .hermes/{auth*,channel_directory.json,state.db*,logs,sessions,cron}, .obsidian/{graph.json,workspace.json}.
§
Scan raw/ compiled_to: grep -rn 'compiled_to.*\[\[\[' raw/. Patterns cần chú ý: quoted wikilinks, wrong path, .md extension. Dùng cat -A/xxd khi terminal nhìn sạch mà file sai.
§
KB máy chính: /home/julius/julius-workspace/knowledge-base; VPS: /home/julius/knowledge-base. Tắt Obsidian trước merge/push.
§
Validation pipeline (cron VPS, 24h): Kara compile 08:00 → index 21:00 → Connor validate 23:00 Output/Format/Hygiene. Job IDs: d48e, d146, f1ff.
§
Connor (Hermes) QUY TẮC CỨNG: KHÔNG tự sửa file trong wiki/concepts/. Chỉ validate + report. Việc sửa lỗi (compile lại, format, hygiene) thuộc về Kara (Compile Agent). Connor chỉ ghi verdict vào wiki/reviews/, không được patch/sửa bất kỳ concept file nào.
§
Empty `## Notes` intentional (Compile Agent template) — không flag.
§
Obsidian display quirk: frontmatter fields (original, sources, compiled_to) cần format `"[[wikilink]]"` (quotes) để Obsidian hiển thị đúng. Wikilinks trong body content dùng bare format `[[wikilink]]`. Đây là lý do format-spec và compile-agent cần quoted format.
§
_approval-log.md đã bị xóa intentional (commit 9948ccc). Cross-machine approval contract không cần nữa. KHÔNG tạo lại hay flag missing.
§
Raw sub-index convention: raw/<category>/<category>.md với frontmatter type:index level:2 scope:<category> parent:"[[raw]]". Phải update raw/raw.md (sub-indexes) + hygiene scan-script (RAW_SUBFOLDERS) + validator scope lists. Không tạo thư mục riêng ở root.
§
OpenClaw config: ~/.openclaw/openclaw.json. `openclaw configure`/`doctor --fix` overwrites manual edits. Compile Daily: 9router/oc/mimo-v2.5-free, fallback gpt-5.4/kimi.
§
Stack 09-08: node nvm v24.20.0 (default alias) + openclaw 2026.9.3. KHÔNG prepend /usr/bin vào PATH ~/.bashrc. reserveTokensFloor RETIRED → `compaction.reserveTokens` trong per-agent ~/.openclaw/agents/<id>/agent/settings.json (main + kara = 50000; default 20000). npm i -g cần --allow-scripts. Backups: openclaw.json.bak-20260902, openclaw.sqlite.bak-20260902.