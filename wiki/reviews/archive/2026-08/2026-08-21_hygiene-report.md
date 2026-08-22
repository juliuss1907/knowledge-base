# Hygiene Inspection — 2026-08-21

**Status:** applied
**Approved by:** Julius
**Issues found:** 19
**Created:** 2026-08-21 23:30:42
**Applied:** 2026-08-22 14:40 by fix-agent (OpenClaw)
**Validator:** hygiene-inspector

**Paths checked:** 53611

---

## Issue 1: Recurring root folder not in whitelist: memory/

**Path:** memory
**Severity:** ERROR
**Category:** Orphan
**Issue:** Recurring root folder `memory/` not in whitelist. Resurfaced for the 5th time in 8 days (08-14, 08-16, 08-17, 08-21; absent 08-15 single-orphan regression). Now holds **16 files** (was 6 on 08-17) — 13 OpenClaw session logs + 3 heartbeat/fetch-status artifacts. All 16 files are **git-tracked** (confirmed via `git ls-files memory/` → 16 entries, `git check-ignore` → not ignored), so the leak persists across auto `vault backup` commits (~every 5-10 min). Process-level leak, not a stray artifact.
**Current:** `memory/` with `2026-08-17-1325.md`, `-1327.md`, `-1329.md`, `2026-08-17-fetch-status.md`, `2026-08-17-heartbeat-ok.md`, `2026-08-17-heartbeat-poll.md`, `2026-08-18-0141.md`, `2026-08-19-1251.md`, `-1252.md`, `-1303.md`, `-1304.md`, `-1305.md`, `2026-08-19-heartbeat-ok.md`, `2026-08-21-0256.md`, `-1333.md`, `2026-08-21-heartbeat-check.md`
**Expected:** `memory/` does not belong at KB root — memory logs go to `.openclaw/memory/` only (AGENTS.md §4.4, folder-structure.md v1.2 §2). `memory/` was migrated to `.openclaw/memory/` in v1.2.
**Suggested fix:** Root-cause fix — redirect the writing process output path from KB root `memory/` to `.openclaw/memory/`, then `git rm -r memory/` + commit. File deletion alone is a stopgap (files are git-tracked and recreated each run; `vault backup` re-commits them).

---

## Issue 2: Recurring root folder not in whitelist: state/

**Path:** state
**Severity:** ERROR
**Category:** Orphan
**Issue:** Recurring root folder `state/` not in whitelist. Resurfaced for the 5th time in 8 days (08-14 through 08-17 consecutively, now 08-21). Currently empty, not git-tracked (untracked phantom dir). Same empty-directory pattern every run.
**Current:** `state/` (empty directory)
**Expected:** No `state/` folder at KB root — not in folder-structure.md whitelist (allowed top-level: `.git`, `.obsidian`, `.openclaw`, `.hermes`, `context`, `raw`, `wiki`, `scripts`)
**Suggested fix:** `rmdir state/` (stopgap). Identify and fix the process recreating it, or move state inside `.hermes/` if it holds real runtime state.

---

## Issue 3: Path not classified by any rule

**Path:** memory/2026-08-17-1325.md
**Severity:** WARNING
**Category:** Path
**Issue:** File under the orphaned `memory/` root folder — not classified by any rule (direct consequence of Issue 1). OpenClaw session log dated 2026-08-17.
**Current:** `memory/2026-08-17-1325.md`
**Expected:** Should be in a known location — belongs in `.openclaw/memory/` (OpenClaw session log)
**Suggested fix:** Resolve Issue 1 (fix writing process path, then remove `memory/`).

---

## Issue 4: Path not classified by any rule

**Path:** memory/2026-08-17-1327.md
**Severity:** WARNING
**Category:** Path
**Issue:** File under the orphaned `memory/` root folder — not classified by any rule (direct consequence of Issue 1). OpenClaw session log dated 2026-08-17.
**Current:** `memory/2026-08-17-1327.md`
**Expected:** Should be in a known location — belongs in `.openclaw/memory/`
**Suggested fix:** Resolve Issue 1 (fix writing process path, then remove `memory/`).

---

## Issue 5: Path not classified by any rule

**Path:** memory/2026-08-17-1329.md
**Severity:** WARNING
**Category:** Path
**Issue:** File under the orphaned `memory/` root folder — not classified by any rule (direct consequence of Issue 1). OpenClaw session log dated 2026-08-17.
**Current:** `memory/2026-08-17-1329.md`
**Expected:** Should be in a known location — belongs in `.openclaw/memory/`
**Suggested fix:** Resolve Issue 1 (fix writing process path, then remove `memory/`).

---

## Issue 6: Path not classified by any rule

**Path:** memory/2026-08-17-fetch-status.md
**Severity:** WARNING
**Category:** Path
**Issue:** File under the orphaned `memory/` root folder — not classified by any rule (direct consequence of Issue 1). Fetch-status artifact dated 2026-08-17.
**Current:** `memory/2026-08-17-fetch-status.md`
**Expected:** Should be in a known location — belongs in `.openclaw/memory/` (fetch-status artifact)
**Suggested fix:** Resolve Issue 1 (fix writing process path, then remove `memory/`).

---

## Issue 7: Path not classified by any rule

**Path:** memory/2026-08-17-heartbeat-ok.md
**Severity:** WARNING
**Category:** Path
**Issue:** File under the orphaned `memory/` root folder — not classified by any rule (direct consequence of Issue 1). Heartbeat artifact dated 2026-08-17.
**Current:** `memory/2026-08-17-heartbeat-ok.md`
**Expected:** Should be in a known location — belongs in `.openclaw/memory/`
**Suggested fix:** Resolve Issue 1 (fix writing process path, then remove `memory/`).

---

## Issue 8: Path not classified by any rule

**Path:** memory/2026-08-17-heartbeat-poll.md
**Severity:** WARNING
**Category:** Path
**Issue:** File under the orphaned `memory/` root folder — not classified by any rule (direct consequence of Issue 1). Heartbeat-poll artifact dated 2026-08-17.
**Current:** `memory/2026-08-17-heartbeat-poll.md`
**Expected:** Should be in a known location — belongs in `.openclaw/memory/`
**Suggested fix:** Resolve Issue 1 (fix writing process path, then remove `memory/`).

---

## Issue 9: Path not classified by any rule

**Path:** memory/2026-08-18-0141.md
**Severity:** WARNING
**Category:** Path
**Issue:** File under the orphaned `memory/` root folder — not classified by any rule (direct consequence of Issue 1). OpenClaw session log dated 2026-08-18.
**Current:** `memory/2026-08-18-0141.md`
**Expected:** Should be in a known location — belongs in `.openclaw/memory/`
**Suggested fix:** Resolve Issue 1 (fix writing process path, then remove `memory/`).

---

## Issue 10: Path not classified by any rule

**Path:** memory/2026-08-19-1251.md
**Severity:** WARNING
**Category:** Path
**Issue:** File under the orphaned `memory/` root folder — not classified by any rule (direct consequence of Issue 1). OpenClaw session log dated 2026-08-19.
**Current:** `memory/2026-08-19-1251.md`
**Expected:** Should be in a known location — belongs in `.openclaw/memory/`
**Suggested fix:** Resolve Issue 1 (fix writing process path, then remove `memory/`).

---

## Issue 11: Path not classified by any rule

**Path:** memory/2026-08-19-1252.md
**Severity:** WARNING
**Category:** Path
**Issue:** File under the orphaned `memory/` root folder — not classified by any rule (direct consequence of Issue 1). OpenClaw session log dated 2026-08-19.
**Current:** `memory/2026-08-19-1252.md`
**Expected:** Should be in a known location — belongs in `.openclaw/memory/`
**Suggested fix:** Resolve Issue 1 (fix writing process path, then remove `memory/`).

---

## Issue 12: Path not classified by any rule

**Path:** memory/2026-08-19-1303.md
**Severity:** WARNING
**Category:** Path
**Issue:** File under the orphaned `memory/` root folder — not classified by any rule (direct consequence of Issue 1). OpenClaw session log dated 2026-08-19.
**Current:** `memory/2026-08-19-1303.md`
**Expected:** Should be in a known location — belongs in `.openclaw/memory/`
**Suggested fix:** Resolve Issue 1 (fix writing process path, then remove `memory/`).

---

## Issue 13: Path not classified by any rule

**Path:** memory/2026-08-19-1304.md
**Severity:** WARNING
**Category:** Path
**Issue:** File under the orphaned `memory/` root folder — not classified by any rule (direct consequence of Issue 1). OpenClaw session log dated 2026-08-19.
**Current:** `memory/2026-08-19-1304.md`
**Expected:** Should be in a known location — belongs in `.openclaw/memory/`
**Suggested fix:** Resolve Issue 1 (fix writing process path, then remove `memory/`).

---

## Issue 14: Path not classified by any rule

**Path:** memory/2026-08-19-1305.md
**Severity:** WARNING
**Category:** Path
**Issue:** File under the orphaned `memory/` root folder — not classified by any rule (direct consequence of Issue 1). OpenClaw session log dated 2026-08-19.
**Current:** `memory/2026-08-19-1305.md`
**Expected:** Should be in a known location — belongs in `.openclaw/memory/`
**Suggested fix:** Resolve Issue 1 (fix writing process path, then remove `memory/`).

---

## Issue 15: Path not classified by any rule

**Path:** memory/2026-08-19-heartbeat-ok.md
**Severity:** WARNING
**Category:** Path
**Issue:** File under the orphaned `memory/` root folder — not classified by any rule (direct consequence of Issue 1). Heartbeat artifact dated 2026-08-19.
**Current:** `memory/2026-08-19-heartbeat-ok.md`
**Expected:** Should be in a known location — belongs in `.openclaw/memory/`
**Suggested fix:** Resolve Issue 1 (fix writing process path, then remove `memory/`).

---

## Issue 16: Path not classified by any rule

**Path:** memory/2026-08-21-0256.md
**Severity:** WARNING
**Category:** Path
**Issue:** File under the orphaned `memory/` root folder — not classified by any rule (direct consequence of Issue 1). OpenClaw session log dated 2026-08-21.
**Current:** `memory/2026-08-21-0256.md`
**Expected:** Should be in a known location — belongs in `.openclaw/memory/`
**Suggested fix:** Resolve Issue 1 (fix writing process path, then remove `memory/`).

---

## Issue 17: Path not classified by any rule

**Path:** memory/2026-08-21-1333.md
**Severity:** WARNING
**Category:** Path
**Issue:** File under the orphaned `memory/` root folder — not classified by any rule (direct consequence of Issue 1). OpenClaw session log dated 2026-08-21.
**Current:** `memory/2026-08-21-1333.md`
**Expected:** Should be in a known location — belongs in `.openclaw/memory/`
**Suggested fix:** Resolve Issue 1 (fix writing process path, then remove `memory/`).

---

## Issue 18: Path not classified by any rule

**Path:** memory/2026-08-21-heartbeat-check.md
**Severity:** WARNING
**Category:** Path
**Issue:** File under the orphaned `memory/` root folder — not classified by any rule (direct consequence of Issue 1). Heartbeat-check artifact dated 2026-08-21.
**Current:** `memory/2026-08-21-heartbeat-check.md`
**Expected:** Should be in a known location — belongs in `.openclaw/memory/`
**Suggested fix:** Resolve Issue 1 (fix writing process path, then remove `memory/`).

---

## Issue 19: Empty directory

**Path:** state
**Severity:** INFO
**Category:** Orphan
**Issue:** Empty directory `state/` — duplicate signal of Issue 2 (empty-directory check fires alongside root-folder whitelist check for the same path).
**Current:** `state/` (empty)
**Expected:** Non-empty directory or removed
**Suggested fix:** Resolve Issue 2 (`rmdir state/`).

---

## Summary

**Total issues:** 19 (2 ERROR, 16 WARNING, 1 INFO)
**Paths checked:** 53611
**Report limit:** 20 (not truncated)

**Delta from 2026-08-17 (previous hygiene report):** +10 issues (9→19), +33 paths checked (53578→53611). `memory/` grew 6→16 files (+10 WARNINGs, all git-tracked) across 08-18, 08-19, 08-21. `state/` unchanged (still empty phantom). No new folder types, no naming violations — entire delta is orphan accumulation.

---

## Escalation

```
[SYSTEMATIC VIOLATION]
Pattern: `memory/` + `state/` root orphans have resurfaced in 5 of the last 6 hygiene runs (08-14: 4 issues, 08-15: 2 issues [memory absent — single-orphan regression], 08-16: 4 issues, 08-17: 9 issues, 08-21: 19 issues). 08-11→08-13 was a 3-run clean streak; every run since has re-leaked.
Likely cause: OpenClaw session/heartbeat/fetch writer emits to KB root `memory/` instead of `.openclaw/memory/`. Evidence: 16 files in `memory/` are all git-tracked (`git ls-files memory/` 16 entries, `git check-ignore` → not ignored), created across 5 calendar days (08-17 through 08-21), and survive `vault backup` auto-commits (~every 5 min, e.g. 29c8cefa 23:31:06). `state/` is an empty untracked phantom recreated even when deleted.
Recommendation: Root-cause fix — redirect the writer output path from KB root `memory/` → `.openclaw/memory/`, then `git rm -r memory/` + commit (deletion alone is futile — git-tracked files are resurrected). `rmdir state/` for the phantom. Until the writer path is fixed, every hygiene run will re-flag and accumulate.
```

```
[STRUCTURE CHANGE]
No whitelist change detected in this run. Previous delta (08-17→08-21) is orphan accumulation only, not a spec change.
```
