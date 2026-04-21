---
type: raw
source_type: article
source_url: https://heeki.medium.com/using-spec-driven-development-with-claude-code-4a1ebe5d9f29
date_ingested: 2026-04-21
tags: [#coding, #ai]
status: unprocessed
---
# Spec-Driven Development with Claude Code

## Tóm tắt

Tác giả (solutions architect) chia sẻ cách dùng spec-driven development khi làm việc với Claude Code để tránh tech debt từ "vibe coding."

## Ba mức độ spec-driven development

- **spec-first:** Viết spec kỹ trước, rồi dùng trong workflow AI-assisted
- **spec-anchored:** Giữ spec sau khi xong task, để maintain và evolve
- **spec-as-source:** Chỉ edit spec, human không bao giờ chạm code trực tiếp

Tác giả tự nhận nghiêng về "spec-once" (viết spec lúc bắt đầu rồi quên đi), nhưng thấy giá trị thực sự là buộc mình phải suy nghĩ sâu về requirements.

## Quy trình cụ thể

1. Đọc documentation, cho Claude Code ingest cùng context
2. Suy nghĩ kỹ về cách build — chia thành sub-projects và phases
3. Viết tất cả thành specification, review kỹ trước khi bắt đầu
4. Build stepwise trong từng phần nhỏ, dễ test

## Tips khi dùng Claude Code

- **Context window:** Default 200k tokens (Pro). Muốn 1M phải qua Bedrock + custom header, nhưng Claude Code không hỗ trợ header đó.
- **Model usage:** Opus 4.6 hết quota rất nhanh. Sonnet 4.6 thoải mái hơn.
- **Clarifying questions:** Dùng selectable inputs để trả lời nhanh.
- **Trust building:** Ban đầu chọn "yes" cho từng action, dần dần trust và auto-allow.
- **Multiple sessions:** Dùng tmux để chạy nhiều Claude Code song song.

## Bài học rút ra

1. **Planning đầu tư sẽ hoàn vốn** — ít phải course correct hơn
2. **Build nhỏ, test sớm** — stacking PRs, mỗi cái nhỏ dễ review
3. **Flexibility cần thiết** — công cụ mới còn preview thì phải tìm workarounds
4. **Security sớm** — thêm OAuth2 cuối phải redeploy cả stack
5. **Cập nhật docs thường xuyên** — mỗi lần tweak design thì update spec

## Links

- Birgitta Böckeler's blog: https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html
- AgentCore CLI: https://github.com/aws/agentcore-cli
- Stacked PRs: https://stacking.dev/