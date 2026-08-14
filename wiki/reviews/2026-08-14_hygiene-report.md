# Hygiene Inspection — 2026-08-14

**Status:** issues-found
**Issues found:** 2 ERROR, 1 WARNING, 1 INFO
**Created:** 2026-08-14 23:31:59
**Validator:** hygiene-inspector

**Paths checked:** 53,559

---

## Summary

⚠️ **Violations detected — recurring root orphan folders surfaced again after 4 clean runs.**

The `memory/` and `state/` root folders — both previously resolved (absent on 07-20 ~ 08-13) — reappeared. `memory/` now contains a session log file that demonstrates the process-level leak is active.

---

## Issue 1: Recurring root folder — `memory/`

**Path:** `memory/`
**Severity:** ERROR
**Category:** Orphan
**Issue:** Recurring root folder not in whitelist
**Current:** `memory/` present at KB root, containing `2026-08-14-0153.md`
**Expected:** Memory logs belong in `.openclaw/memory/` only (per AGENTS.md 4.4 and folder-structure.md v1.2)
**Suggested fix:** Process-level fix — the writing process targets `memory/` instead of `.openclaw/memory/`. Move contents and `rmdir memory/`; correct the writing process output path.

---

## Issue 2: Recurring root folder — `state/`

**Path:** `state/`
**Severity:** ERROR
**Category:** Orphan
**Issue:** Recurring root folder not in whitelist
**Current:** `state/` empty directory present at KB root
**Expected:** Not in whitelist — previously resolved 2026-06-27; move inside `.hermes/` or `.openclaw/` if needed, otherwise `rmdir`
**Suggested fix:** `rmdir state/`

---

## Issue 3: Unclassified file inside `memory/`

**Path:** `memory/2026-08-14-0153.md`
**Severity:** WARNING
**Category:** Path
**Issue:** Path not classified by any rule (content file leaked into root-level `memory/`)
**Current:** OpenClaw session log (created 2026-08-14 08:54) sitting at `memory/2026-08-14-0153.md`
**Expected:** `Memory`-type content belongs in `.openclaw/memory/`
**Suggested fix:** Move to `.openclaw/memory/`; this is a downstream symptom of the `memory/` writing-process leak (Issue 1)

---

## Issue 4: Empty directory

**Path:** `state/`
**Severity:** INFO
**Category:** Orphan
**Issue:** Empty directory
**Current:** `state/` has no contents
**Expected:** Non-empty directory or removed
**Suggested fix:** `rmdir state/`

---

## Comparison with Prior Runs

| Date | Issues | Status |
|---|---|---|
| 2026-08-14 | 4 (2E+1W+1I) | ⚠️ Checked |
| 2026-08-13 | 0 | ✅ Clean |
| 2026-08-12 | 0 | ✅ Clean |
| 2026-08-11 | 0 | ✅ Clean |
| 2026-08-10 | 5 (3E+1W+1I) | Checked |
| 2026-08-09 | 3 (2E+1I) | Checked |
| 2026-08-08 | 3 (2E+1I) | Checked |

**Trend:** 3-consecutive-clean streak broken. `memory/` and `state/` resurfaced. The `memory/` leak reappears despite prior Fix Agent deletion — confirming it is a **process-level leak** (a runtime process writes session/summary logs to KB root `memory/` instead of `.openclaw/memory/`). File/folder deletion alone will not resolve it.

---

## Escalation

```
[SYSTEMATIC VIOLATION]
Pattern: memory/ root folder resurfaced AGAIN — first reincidence since 07-21.
The 2026-08-14-0153.md file (created 08:54 today) proves the OpenClaw/session-writing
process targets KB root 'memory/' instead of '.openclaw/memory/'.
Likely cause: The writing process output path is still pointing at KB root.
Recommendation: This needs a process-level fix, not another file deletion.
Correct the memory-log writer to emit to .openclaw/memory/. A scheduled rmdir
(like Fix Agent applies) is only a stopgap.
```

Related note: `state/` is gitignored and reappears as an empty directory — needs an `rmdir` but the process creating it should be identified.

---

## Notes

- No path-whitelist violations elsewhere
- No naming convention violations in `raw/`, `wiki/`, `context/`
- No HEARTBEAT leak in `wiki/`, `wiki/reviews/`, or `raw/` this run
- Archive structure in `wiki/reviews/archive/` clean
- Remaining 2 issues are the two root orphan folders; the WARNING and INFO are their contents/downstream artifacts