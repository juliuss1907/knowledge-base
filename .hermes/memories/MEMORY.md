KB gitignore: .hermes/auth/, .hermes/auth.json, .hermes/channel_directory.json, .hermes/state.db*, .hermes/logs/, .hermes/sessions/, .hermes/cron/, .obsidian/graph.json, .obsidian/workspace.json. Đã clean git history.
§
Scan raw/ compiled_to: grep -rn 'compiled_to.*\[\[\[' raw/ — finds quoted wikilinks. Patterns: `"[[...]]"` (quotes), `"[[wiki/sources/...]]"` (wrong path), `"[[src_....md]]"` (with .md extension). Use cat -A or xxd to detect hidden chars when terminal output looks clean but file seems wrong.
§
Máy chính working dir: /home/julius/julius-workspace/knowledge-base (KHÁC với VPS: /home/julius/knowledge-base). Obsidian Git plugin trên máy chính auto-sync cạnh tranh lock với git CLI thủ công — cần tắt Obsidian hoặc plugin trước khi chạy git merge/push. Micro editor để lại backup MERGE_MSG ở ~/.config/micro/backups/ — mỗi merge sẽ prompt [r]ecover/[i]gnore/[a]bort, chọn 'i'.
§
Validation pipeline (cron trên VPS, interval 24h): Kara compile 08:00 (kimi-k2.5), index 21:00 (gemma-4-31b). Connor validate 23:00 Output / 23:15 Format / 23:30 Hygiene (all glm-5.1 via opencode). Job IDs: d48e30a9a963, d14687442111, f1ff44c008e2.
§
Connor (Hermes) QUY TẮC CỨNG: KHÔNG tự sửa file trong wiki/concepts/. Chỉ validate + report. Việc sửa lỗi (compile lại, format, hygiene) thuộc về Kara (Compile Agent). Connor chỉ ghi verdict vào wiki/reviews/, không được patch/sửa bất kỳ concept file nào.
§
Empty `## Notes` section trong concept files là intentional — Julius đã thiết lập Compile Agent template như vậy. Output validator không nên flag empty Notes section.
§
Obsidian display quirk: frontmatter fields (original, sources, compiled_to) cần format `"[[wikilink]]"` (quotes) để Obsidian hiển thị đúng. Wikilinks trong body content dùng bare format `[[wikilink]]`. Đây là lý do format-spec và compile-agent cần quoted format.
§
_approval-log.md đã bị xóa intentional (commit 9948ccc). Cross-machine approval contract không cần nữa. KHÔNG tạo lại hay flag missing.