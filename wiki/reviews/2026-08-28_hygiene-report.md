# Hygiene Inspection — 2026-08-28

**Status:** pending
**Issues found:** 2
**Created:** 2026-08-28 23:31:00
**Validator:** hygiene-inspector

**Paths checked:** 55918

---

## Issue 1: Known root orphan: openclaw-workspace-state.json

**Path:** openclaw-workspace-state.json
**Severity:** ERROR
**Category:** Orphan
**Issue:** `openclaw-workspace-state.json` at KB root — LẦN 7 LIÊN TIẾP (08-22 → 08-28).
**Current:** File at KB root (69 bytes, mtime 2026-08-24 10:00 — không có write mới ngày 08-28)
**Expected:** OpenClaw runtime state belongs in `.openclaw/` or `~/.openclaw/`. Root cause CONFIRMED in vendor source (SKILL.md v1.21 pitfall #9): OpenClaw treats any dir containing `AGENTS.md` as a workspace; state path resolves CWD-relative by design (`dist/workspace-DkQ7irPD.js`). Git-level SẠCH: untracked + `.gitignore` guard hiệu lực (`.gitignore:88-89`). Chỉ disk-level orphan persists.
**Suggested fix:** KHÔNG xóa file lần 8 — deletion proven futile x3 (recycle < 1h nhanh nhất). KHÔNG re-escalate `[SYSTEMATIC VIOLATION]` theo pitfall #9. Chỉ còn 2 lựa chọn gốc-rễ: (1) redirect writer output path về `.openclaw/` hoặc `~/.openclaw/`, hoặc (2) chờ OpenClaw update mang SQLite workspace-state refactor.

---

## Issue 2: HEARTBEAT.md leaked into wiki/ root

**Path:** wiki/HEARTBEAT.md
**Severity:** ERROR
**Category:** Orphan
**Issue:** `wiki/HEARTBEAT.md` — symlink → `../../.openclaw/HEARTBEAT.md`, tái diễn lần 3 liên tiếp (08-26, 08-27, 08-28) sau khi sạch ở 08-25.
**Current:** Symlink at `wiki/HEARTBEAT.md` (created 2026-08-26 17:01). Untracked + gitignored (`.gitignore`), không vào commit.
**Expected:** HEARTBEAT.md belongs in `.hermes/` or `.openclaw/` or at root (as the whitelisted symlink). The `wiki/` variant is a process-level leak — some sync tool mirrors the root-level `HEARTBEAT.md` symlink into `wiki/`.
**Suggested fix:** Cần process-level fix: xác định process tạo symlink HEARTBEAT vào wiki/ trước khi xóa — file deletion là transient nếu writer còn active. File deletion đơn thuần không hiệu quả.