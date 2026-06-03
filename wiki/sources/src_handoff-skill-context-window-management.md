---
type: source
original: "[[2026-06-02_handoff-skill-context-window-management]]"
main_tag: ai
sub_tags: [tools, automation, coding]
topic: ai-coding-context-handoff
date_compiled: 2026-06-03
url: https://www.youtube.com/watch?v=dtAJ2dOd3ko
author: Unknown
---

# Handoff Skill — Context Window Management for AI Coding Agents

## Metadata

- **Author:** Unknown
- **Published:** 2026-06-02
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=dtAJ2dOd3ko
- **Type:** video

## Summary

Video giải thích Handoff Skill — một skill tùy chỉnh để quản lý context window khi làm việc với AI coding agents. Khi session coding kéo dài, context window đầy lên và chất lượng output giảm mạnh ("dumb zone"). Mặc dù Claude Code có 1M tokens context, thực tế chỉ ~120K tokens còn "thông minh". Giải pháp: thay vì tóm tắt compact, hãy hand off từng phần context cụ thể sang các session tách riêng, tập trung.

## Key points

- Session coding dài làm đầy context window → chất lượng output giảm nghiêm trọng ("dumb zone")
- Claude Code có 1M token context nhưng chỉ ~120K tokens là giới hạn thực tế cho phản hồi "thông minh"
- Giải pháp cũ — Compact: Tóm tắt conversation hiện tại → reset context, nhưng vẫn 1 session duy nhất, tích lũy "sediment"
- Giải pháp mới — Handoff Skill: Lấy 1 phần context cụ thể (1 bug fix, 1 feature) → chuyển sang session riêng, session gốc giữ sạch

## 3 Usage Patterns

### 🔀 Handoff when grilled
- Trong quá trình planning, phát hiện task ngoài scope → handoff sang session khác, giữ main flow sạch

### 🧪 Handoff for prototyping
- UI phức tạp/thử nghiệm cần thiết → đẩy sang session prototype riêng (~169K tokens!), handoff lại khi xong

### 🔄 Cross-agent handoff
- Vì là markdown, có thể truyền từ Claude Code → Codex → Copilot CLI, cho phép adversarial review qua nhiều agents khác nhau

## Skill Principles

1. **Lưu handoff file trong temp directory** — xóa khi xong, không làm bẩn codebase
2. **Bao gồm suggested skills cho session mới**
3. **Không duplicate content từ artifacts khác** — chỉ dùng pointers
4. **Redact thông tin nhạy cảm** (API keys, passwords)
5. **Luôn viết rõ purpose cho session tiếp theo**

## Concepts referenced

- [[context-window-management]]
- [[handoff-skill]]
- [[ai-coding-agents]]
- [[session-separation]]
- [[cross-agent-workflow]]
- [[compact-vs-handoff]]

## Original excerpts

> "A great video about context management techniques for AI coding agents — instead of stuffing everything into one session until it gets confused, split into multiple focused sessions using markdown files as bridges."
