# Hygiene Inspection — 2026-08-29

**Status:** approved
**Issues found:** 2
**Created:** 2026-08-29 23:31:00
**Validator:** hygiene-inspector
**Validator version:** 1.23

**Paths checked:** 55940

---

## Issue 1: Known root orphan: openclaw-workspace-state.json

**Path:** openclaw-workspace-state.json
**Severity:** ERROR
**Category:** Orphan
**Issue:** Known root orphan: openclaw-workspace-state.json
**Current:** openclaw-workspace-state.json (69 bytes, mtime 2026-08-24 10:00, no fresh write)
**Expected:** Should be in OpenClaw runtime state home (.openclaw/ or ~/.openclaw/) — 8th consecutive run flagged (08-22 → 08-29). Root cause CONFIRMED in vendor source (SKILL.md v1.21 pitfall #9): OpenClaw treats any dir with AGENTS.md as a workspace; state path resolves CWD-relative by design (dist/workspace-DkQ7irPD.js). .gitignore guard holds the repo clean (untracked + ignored) — only the disk-level orphan persists.
**Suggested fix:** STOP re-deleting (proven futile x3). Fix = redirect writer output path OR wait for OpenClaw SQLite workspace-state refactor. See references/common-patterns.md.

---

## Issue 2: HEARTBEAT.md leaked into wiki/ root (new variant — recurring process leak)

**Path:** wiki/HEARTBEAT.md
**Severity:** ERROR
**Category:** Orphan
**Issue:** HEARTBEAT.md leaked into wiki/ root (new variant — recurring process leak)
**Current:** wiki/HEARTBEAT.md (symlink → ../../.openclaw/HEARTBEAT.md)
**Expected:** HEARTBEAT.md belongs in .hermes/ or .openclaw/; file deletion is transient — the writing process must be fixed
**Suggested fix:** Identify and fix the process writing HEARTBEAT.md to wiki/; then delete this file.

---

## Summary

| Metric | Value |
|---|---|
| Total paths checked | 55940 |
| Total issues | 2 |
| ERROR | 2 |
| WARNING | 0 |
| INFO | 0 |
| Truncated | No (within 20-issue limit) |

**Recurring issues:**
- `openclaw-workspace-state.json` — 8th consecutive run (08-22 → 08-29), root cause confirmed in vendor source
- `wiki/HEARTBEAT.md` — 4th consecutive run (08-26 → 08-29), symlink to .openclaw/HEARTBEAT.md

**Clean streaks:**
- `memory/` + `state/` absent — 7th consecutive clean run
- No naming violations — 0 WARNING
- No empty directories — 0 INFO