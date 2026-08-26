# Hygiene Inspection — 2026-08-26

**Status:** pending
**Issues found:** 2
**Created:** 2026-08-26 23:30:59
**Validator:** hygiene-inspector

**Paths checked:** 55884

---

## Issue 1: Known root orphan — openclaw-workspace-state.json

**Path:** openclaw-workspace-state.json
**Severity:** ERROR
**Category:** Orphan
**Issue:** Known root orphan: openclaw-workspace-state.json (LẦN 5 LIÊN TIẾP — 08-22 → 08-26)
**Current:** openclaw-workspace-state.json at KB root
**Expected:** OpenClaw runtime state home (.openclaw/ hoặc ~/.openclaw/)
**Suggested fix:** KHÔNG xóa lại file — deletion proven futile x3 (recycle < 1h nhanh nhất). Root cause ĐÃ CONFIRM trong vendor source (SKILL.md v1.21 pitfall #9): OpenClaw coi mọi thư mục chứa `AGENTS.md` là workspace, state path resolve CWD-relative by design (`dist/workspace-DkQ7irPD.js`, package 2026.7.1-2) → writer ghi vào KB root mỗi session bootstrap. Git-level SẠCH: file untracked + `.gitignore` guard hiệu lực; chỉ disk-level orphan persists. Chọn 1 trong 2: (1) redirect writer output path về `.openclaw/` hoặc `~/.openclaw/`, hoặc (2) chờ OpenClaw update mang SQLite workspace-state refactor. KHÔNG re-escalate `[SYSTEMATIC VIOLATION]` — tham chiếu pitfall #9.

---

## Issue 2: HEARTBEAT.md leaked into wiki/ root

**Path:** wiki/HEARTBEAT.md
**Severity:** ERROR
**Category:** Orphan
**Issue:** HEARTBEAT.md leaked into wiki/ root (recurring process leak — tái diễn sau khi sạch ở 08-25)
**Current:** wiki/HEARTBEAT.md
**Expected:** HEARTBEAT.md belongs in .hermes/ hoặc .openclaw/
**Suggested fix:** Identify and fix the process writing HEARTBEAT.md to wiki/; rồi xóa file. File deletion là transient — process-writing phải được fix ở gốc. File này git-untracked + gitignored (không vào commit).
