KB gitignore: .hermes/auth/, .hermes/auth.json, .hermes/channel_directory.json, .hermes/state.db*, .hermes/logs/, .hermes/sessions/, .hermes/cron/, .obsidian/graph.json, .obsidian/workspace.json. Đã clean git history.
§
Scan raw/ compiled_to: grep -rn 'compiled_to.*\[\[\[' raw/. Patterns cần chú ý: quoted wikilinks, wrong path, .md extension. Dùng cat -A/xxd khi terminal nhìn sạch mà file sai.
§
Máy chính: /home/julius/julius-workspace/knowledge-base. VPS: /home/julius/knowledge-base. Obsidian Git plugin cạnh tranh lock với git CLI — tắt Obsidian trước merge/push. Micro backups MERGE_MSG ở ~/.config/micro/backups/.
§
Validation pipeline (cron VPS, 24h): Kara compile 08:00 → index 21:00 → Connor validate 23:00 Output/Format/Hygiene. Job IDs: d48e, d146, f1ff.
§
Connor (Hermes) QUY TẮC CỨNG: KHÔNG tự sửa file trong wiki/concepts/. Chỉ validate + report. Việc sửa lỗi (compile lại, format, hygiene) thuộc về Kara (Compile Agent). Connor chỉ ghi verdict vào wiki/reviews/, không được patch/sửa bất kỳ concept file nào.
§
Empty `## Notes` section trong concept files là intentional — Julius đã thiết lập Compile Agent template như vậy. Output validator không nên flag empty Notes section.
§
Obsidian display quirk: frontmatter fields (original, sources, compiled_to) cần format `"[[wikilink]]"` (quotes) để Obsidian hiển thị đúng. Wikilinks trong body content dùng bare format `[[wikilink]]`. Đây là lý do format-spec và compile-agent cần quoted format.
§
_approval-log.md đã bị xóa intentional (commit 9948ccc). Cross-machine approval contract không cần nữa. KHÔNG tạo lại hay flag missing.
§
Raw sub-index convention: raw/<category>/<category>.md với frontmatter type:index level:2 scope:<category> parent:"[[raw]]". Phải update raw/raw.md (sub-indexes) + hygiene scan-script (RAW_SUBFOLDERS) + validator scope lists. Không tạo thư mục riêng ở root.
§
OpenClaw (Kara) config: ~/.openclaw/openclaw.json. `openclaw configure` wizard overwrites manual edits — set model/reserveTokensFloor qua wizard. Kara heartbeat/session writer tái tạo memory//state/ ở root KB thay vì .openclaw/memory/ — systemic (lần 3+).