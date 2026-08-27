# Hygiene Inspection — 2026-08-27

**Status:** approved
**Issues found:** 2
**Created:** 2026-08-27 19:18:00
**Validator:** hygiene-inspector

**Paths checked:** 55902

---

## Issue 1: Known root orphan — openclaw-workspace-state.json

**Path:** openclaw-workspace-state.json
**Severity:** ERROR
**Category:** Orphan
**Issue:** Known root orphan: openclaw-workspace-state.json (LẦN 6 LIÊN TIẾP — 08-22 → 08-27)
**Current:** openclaw-workspace-state.json at KB root (69 bytes, mtime 2026-08-24 10:00 — không có write mới)
**Expected:** OpenClaw runtime state home (.openclaw/ hoặc ~/.openclaw/)
**Suggested fix:** KHÔNG xóa lại file — deletion proven futile x3 (recycle < 1h nhanh nhất, 08-24). Root cause ĐÃ CONFIRM trong vendor source (SKILL.md v1.21 pitfall #9): OpenClaw coi mọi thư mục chứa `AGENTS.md` là workspace, state path resolve CWD-relative by design (`dist/workspace-DkQ7irPD.js`, package 2026.7.1-2) → writer ghi vào KB root mỗi session bootstrap. Git-level SẠCH: file untracked + `.gitignore` guard hiệu lực (`git check-ignore` xác nhận ignored); chỉ disk-level orphan persists. Chọn 1 trong 2: (1) redirect writer output path về `.openclaw/` hoặc `~/.openclaw/`, hoặc (2) chờ OpenClaw update mang SQLite workspace-state refactor. KHÔNG re-escalate `[SYSTEMATIC VIOLATION]` — tham chiếu pitfall #9.

---

## Issue 2: HEARTBEAT.md leaked into wiki/ root

**Path:** wiki/HEARTBEAT.md
**Severity:** ERROR
**Category:** Orphan
**Issue:** HEARTBEAT.md leaked into wiki/ root — recurring process leak, tái diễn lần 2 liên tiếp (08-26, 08-27) sau khi sạch ở 08-25
**Current:** wiki/HEARTBEAT.md — symlink → `../../.openclaw/HEARTBEAT.md` (tạo 2026-08-26 17:01)
**Expected:** HEARTBEAT.md belongs in `.hermes/` hoặc `.openclaw/`; symlink đúng chỉ tồn tại ở root (`HEARTBEAT.md` → `.openclaw/HEARTBEAT.md`)
**Suggested fix:** Process-level fix — xác định process tạo symlink HEARTBEAT.md vào `wiki/` (có thể là công cụ đồng bộ symlink root-level, hoặc Obsidian sync). File này **untracked + gitignored** (`git ls-files -s` rỗng, `.gitignore:78` HEARTBEAT.md) → không vào commit, xóa working copy là transient nếu writer còn active. Xóa file đơn thuần không đủ — phải fix process tạo symlink này.
