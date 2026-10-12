Vault backup cron ở máy chính, KHÔNG phải VPS; không tự phục hồi sau reboot → HEAD vs origin/master là cách duy nhất check. Agent-home block đã vào .gitignore.
§
Scan raw/ compiled_to: grep -rn 'compiled_to.*\[\[\[' raw/. Chú ý quoted wikilink, wrong path, .md. Dùng cat -A/xxd khi terminal nhìn sạch mà file sai.
§
KB máy chính: /home/julius/julius-workspace/knowledge-base; VPS: /home/julius/knowledge-base. Tắt Obsidian trước merge/push.
§
Validation pipeline (cron VPS, 24h): Kara compile 08:00 → index 21:00 → Connor validate 23:00 Output/Format/Hygiene. Job IDs: d48e, d146, f1ff.
§
Connor (Hermes) QUY TẮC CỨNG: KHÔNG tự sửa file trong wiki/concepts/. Chỉ validate + report. Việc sửa lỗi (compile lại, format, hygiene) thuộc về Kara (Compile Agent). Connor chỉ ghi verdict vào wiki/reviews/, không được patch/sửa bất kỳ concept file nào.
§
Empty `## Notes` intentional (Compile Agent template) — không flag.
§
Obsidian house style: frontmatter (original, sources, compiled_to) cần `"[[wikilink]]"` có quotes; body content dùng bare `[[wikilink]]`; wikilink KHÔNG kèm `.md` (→ slug.md.md). validate.py kiểm bằng wikilink_style_issues() — body-only, frontmatter exempt.
§
_approval-log.md đã bị xóa intentional (commit 9948ccc). Cross-machine approval contract không cần nữa. KHÔNG tạo lại hay flag missing.
§
Raw sub-index convention: raw/<category>/<category>.md với frontmatter type:index level:2 scope:<category> parent:"[[raw]]". Phải update raw/raw.md (sub-indexes) + hygiene scan-script (RAW_SUBFOLDERS) + validator scope lists. Không tạo thư mục riêng ở root.
§
OpenClaw config: ~/.openclaw/openclaw.json. `configure`/`doctor --fix` overwrite manual edits. Compile Daily: 9router/oc/mimo-v2.5-free, fallback gpt-5.4/kimi.
§
Stack: node nvm v24.20.0 (default alias) + openclaw 2026.9.3. KHÔNG prepend /usr/bin vào PATH. npm i -g cần --allow-scripts. Chi tiết: skill openclaw-ops.
§
format-validator đo slug source trên thân slug (strip `src_`). Đếm theo filename sinh ERROR giả ở biên 50.
§
Curator KHÔNG patch được 5 skill user-owned: format-validator, hygiene-inspector, knowledge-base-validation, git-secret-cleanup, obsidian-git-no-conflict. Muốn sửa: `hermes curator adopt <name>`.