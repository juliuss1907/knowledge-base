# Hygiene Inspection — 2026-08-25

**Status:** pending
**Issues found:** 1
**Created:** 2026-08-25 23:36:11
**Validator:** hygiene-inspector

**Paths checked:** 55860

---

## Issue 1: Known root orphan — openclaw-workspace-state.json

**Path:** openclaw-workspace-state.json
**Severity:** ERROR
**Category:** Orphan
**Issue:** Known root orphan: openclaw-workspace-state.json — 4th consecutive run flagged (08-22 → 08-25)
**Current:** File exists at KB root, 69 bytes, mtime 2026-08-24 10:00 (persisting since the 08-24 runtime recreation; no new writes observed on 08-25)
**Expected:** OpenClaw runtime state home (.openclaw/ or ~/.openclaw/). ROOT CAUSE CONFIRMED (pitfall #9): OpenClaw treats any directory containing AGENTS.md as a workspace and resolves the state path CWD-relative by design (dist/workspace-DkQ7irPD.js, package 2026.7.1-2). KB root has AGENTS.md → writer legitimately writes here on every session bootstrap.
**Suggested fix:** DO NOT delete again — deletion proven futile x3 (recycle < 1h at worst). Repo hygiene already SOLVED: file untracked (`git ls-files` = empty) and guarded by `.gitignore:88-89`. Disk-level recurrence is accepted until upstream ships the SQLite workspace-state refactor. Fix options: (1) redirect writer output path, or (2) wait for upstream update. Reference: skill pitfall #9 + references/common-patterns.md.

---

## Clean areas (no issues)

- No HEARTBEAT leaks (`wiki/HEARTBEAT.md`, `wiki/reviews/HEARTBEAT.md`, `raw/.last_heartbeat` all absent) — clean streak continues
- `memory/` root folder absent — clean streak continues (since 08-22)
- `state/` root folder absent — clean streak continues (since 08-22)
- No naming violations in raw/, wiki/concepts/, wiki/sources/, wiki/tag/, wiki/topic/, wiki/drafts/
- No files at wiki/ or raw/ root level beyond whitelisted indexes
- wiki/reviews/ contains only canonical reports + whitelisted files
- No empty directories, no temporary files (.bak/.tmp/.swp/~)

---

## Escalation notes

None this run. The single ERROR is a known, documented, root-caused leak (skill SKILL.md pitfall #9, updated v1.21 2026-08-25):

> When a leak's writer is identified in vendor source with CWD-relative output, stop recommending per-file deletions — recommend either the .gitignore-guard pattern or waiting for upstream.

Per-run ERROR listing of this file is expected and correct (it IS outside the whitelist on disk); it should NOT be re-escalated as `[SYSTEMATIC VIOLATION]`.

---

## Run metadata

- Scan script: `/tmp/hygiene_scan.py` (template: skill references/scan-script.py, whitelist dictionaries in sync with folder-structure.md v1.2)
- Issue limit: 20/run — not hit (1 issue total)
- Comparison with previous run (08-24): paths 55845 → 55860 (+15); issues 1 → 1 (same single known ERROR); severity identical (1E+0W+0I)
