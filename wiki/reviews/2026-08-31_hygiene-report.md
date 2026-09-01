# Hygiene Inspection — 2026-08-31

**Status:** approved
**Issues found:** 8
**Created:** 2026-08-31 23:35:07
**Validator:** hygiene-inspector
**Validator version:** 1.24

**Paths checked:** 55987

---

## Issue 1: Known root orphan: openclaw-workspace-state.json

**Path:** openclaw-workspace-state.json
**Severity:** ERROR
**Category:** Orphan
**Issue:** Known root orphan: openclaw-workspace-state.json
**Current:** openclaw-workspace-state.json (69 bytes, mtime 2026-08-24 10:00, no fresh write)
**Expected:** Should be in OpenClaw runtime state home (.openclaw/ or ~/.openclaw/) — 9th consecutive run flagged (08-22 → 08-31). Root cause CONFIRMED in vendor source (SKILL.md v1.21 pitfall #9): OpenClaw treats any dir with AGENTS.md as a workspace; state path resolves CWD-relative by design (dist/workspace-DkQ7irPD.js). .gitignore guard holds the repo clean (untracked + ignored) — only the disk-level orphan persists.
**Suggested fix:** STOP re-deleting (proven futile x3). Fix = redirect writer output path OR wait for OpenClaw SQLite workspace-state refactor. See references/common-patterns.md.

---

## Issue 2: HEARTBEAT.md leaked into wiki/ root (new variant — recurring process leak)

**Path:** wiki/HEARTBEAT.md
**Severity:** ERROR
**Category:** Orphan
**Issue:** HEARTBEAT.md leaked into wiki/ root (new variant — recurring process leak)
**Current:** wiki/HEARTBEAT.md (symlink → ../../.openclaw/HEARTBEAT.md, created 08-26 17:01)
**Expected:** HEARTBEAT.md belongs in .hermes/ or .openclaw/; file deletion is transient — the writing process must be fixed
**Suggested fix:** Identify and fix the process writing HEARTBEAT.md to wiki/; then delete this file.

---

## Issue 3: Repos file naming: expected YYYY-MM-DD_<owner>_<repo>.md

**Path:** raw/repos/2026-08-30_anthropic-cybersecurity-skills.md
**Severity:** WARNING
**Category:** Naming
**Issue:** Repos file naming: expected YYYY-MM-DD_<owner>_<repo>.md
**Current:** 2026-08-30_anthropic-cybersecurity-skills.md (single slug segment)
**Expected:** YYYY-MM-DD_<owner>_<repo>.md (two slug segments separated by underscore)
**Suggested fix:** Rename to match repos convention, e.g. 2026-08-30_anthropic_cybersecurity-skills.md

---

## Issue 4: Repos file naming: expected YYYY-MM-DD_<owner>_<repo>.md

**Path:** raw/repos/2026-08-30_archify.md
**Severity:** WARNING
**Category:** Naming
**Issue:** Repos file naming: expected YYYY-MM-DD_<owner>_<repo>.md
**Current:** 2026-08-30_archify.md (single slug segment)
**Expected:** YYYY-MM-DD_<owner>_<repo>.md (two slug segments separated by underscore)
**Suggested fix:** Rename to match repos convention, e.g. 2026-08-30_<owner>_archify.md

---

## Issue 5: Repos file naming: expected YYYY-MM-DD_<owner>_<repo>.md

**Path:** raw/repos/2026-08-30_impeccable.md
**Severity:** WARNING
**Category:** Naming
**Issue:** Repos file naming: expected YYYY-MM-DD_<owner>_<repo>.md
**Current:** 2026-08-30_impeccable.md (single slug segment)
**Expected:** YYYY-MM-DD_<owner>_<repo>.md (two slug segments separated by underscore)
**Suggested fix:** Rename to match repos convention, e.g. 2026-08-30_<owner>_impeccable.md

---

## Issue 6: Repos file naming: expected YYYY-MM-DD_<owner>_<repo>.md

**Path:** raw/repos/2026-08-30_openviking.md
**Severity:** WARNING
**Category:** Naming
**Issue:** Repos file naming: expected YYYY-MM-DD_<owner>_<repo>.md
**Current:** 2026-08-30_openviking.md (single slug segment)
**Expected:** YYYY-MM-DD_<owner>_<repo>.md (two slug segments separated by underscore)
**Suggested fix:** Rename to match repos convention, e.g. 2026-08-30_<owner>_openviking.md

---

## Issue 7: Repos file naming: expected YYYY-MM-DD_<owner>_<repo>.md

**Path:** raw/repos/2026-08-30_posthog.md
**Severity:** WARNING
**Category:** Naming
**Issue:** Repos file naming: expected YYYY-MM-DD_<owner>_<repo>.md
**Current:** 2026-08-30_posthog.md (single slug segment)
**Expected:** YYYY-MM-DD_<owner>_<repo>.md (two slug segments separated by underscore)
**Suggested fix:** Rename to match repos convention, e.g. 2026-08-30_<owner>_posthog.md

---

## Issue 8: Repos file naming: expected YYYY-MM-DD_<owner>_<repo>.md

**Path:** raw/repos/2026-08-30_threeui.md
**Severity:** WARNING
**Category:** Naming
**Issue:** Repos file naming: expected YYYY-MM-DD_<owner>_<repo>.md
**Current:** 2026-08-30_threeui.md (single slug segment)
**Expected:** YYYY-MM-DD_<owner>_<repo>.md (two slug segments separated by underscore)
**Suggested fix:** Rename to match repos convention, e.g. 2026-08-30_<owner>_threeui.md

---

## Summary

| Metric | Value |
|---|---|
| Total paths checked | 55987 |
| Total issues | 8 |
| ERROR | 2 |
| WARNING | 6 |
| INFO | 0 |
| Truncated | No (within 20-issue limit) |

**Recurring issues:**
- `openclaw-workspace-state.json` — 9th consecutive run (08-22 → 08-31), root cause confirmed in vendor source
- `wiki/HEARTBEAT.md` — 5th consecutive run (08-26 → 08-31), symlink to .openclaw/HEARTBEAT.md

**New issues this run:**
- 6 raw/repos files from 08-30 ingest batch violate naming convention (single slug instead of `<owner>_<repo>`)

**Clean streaks:**
- `memory/` + `state/` absent — 8th consecutive clean run
- No empty directories — 0 INFO

---

## Escalation

```
[SYSTEMATIC VIOLATION] Naming — raw/repos/ batch (08-30 ingest)
Pattern: 6/6 repos files in the 08-30 batch use single-slug names (2026-08-30_<repo>.md)
         instead of the folder-structure.md convention YYYY-MM-DD_<owner>_<repo>.md
         (precedent: 2026-06-27_aiskilloftheweek_personal-mba-generator-skill.md,
         2026-06-27_aiskilloftheweek_sop-writer-skill.md — both correct 2-segment).
Likely cause: Ingest Agent did not apply the repos two-segment naming rule for this batch.
Recommendation: Update Ingest Agent SKILL.md to enforce <owner>_<repo> for raw/repos/;
                Fix Agent renames the 6 files to include the owner segment.
```

Note: `openclaw-workspace-state.json` and `wiki/HEARTBEAT.md` are NOT re-escalated — both are documented recurring leaks with confirmed root causes (SKILL.md pitfall #9 for the state file; process-level symlink mirror for HEARTBEAT). `[SYSTEMATIC VIOLATION]` above applies only to the new repos naming pattern.
