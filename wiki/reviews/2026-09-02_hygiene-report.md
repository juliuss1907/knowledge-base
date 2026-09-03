# Hygiene Inspection — 2026-09-02

**Status:** approved
**Issues found:** 12
**Created:** 2026-09-02 23:36:28
**Validator:** hygiene-inspector
**Validator version:** 1.25

**Paths checked:** 56011

---

## Issue 1: Known root orphan: openclaw-workspace-state.json

**Path:** openclaw-workspace-state.json
**Severity:** ERROR
**Category:** Orphan
**Issue:** Known root orphan: openclaw-workspace-state.json
**Current:** openclaw-workspace-state.json (69 bytes, mtime 2026-08-24 10:00, no fresh write)
**Expected:** Should be in OpenClaw runtime state home (.openclaw/ or ~/.openclaw/) — 11th consecutive run flagged (08-22 → 09-02). Root cause CONFIRMED in vendor source (SKILL.md v1.21 pitfall #9): OpenClaw treats any dir with AGENTS.md as a workspace; state path resolves CWD-relative by design (dist/workspace-DkQ7irPD.js). .gitignore guard holds the repo clean (untracked + ignored) — only the disk-level orphan persists.
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

## Issue 3: Repos file naming: owner segment has uppercase

**Path:** raw/repos/2026-08-30_MengTo_threeui.md
**Severity:** WARNING
**Category:** Naming
**Issue:** Repos file naming: owner segment has uppercase — slug rules require lowercase
**Current:** 2026-08-30_MengTo_threeui.md (owner segment `MengTo` has uppercase)
**Expected:** YYYY-MM-DD_<owner>_<repo>.md with lowercase owner (folder-structure.md §8 slug rules: lowercase only)
**Suggested fix:** Rename to 2026-08-30_mengto_threeui.md (or add a folder-structure.md exception for GitHub owner casing)

---

## Issue 4: Repos file naming: owner segment has uppercase

**Path:** raw/repos/2026-08-30_PostHog_posthog.md
**Severity:** WARNING
**Category:** Naming
**Issue:** Repos file naming: owner segment has uppercase — slug rules require lowercase
**Current:** 2026-08-30_PostHog_posthog.md (owner segment `PostHog` has uppercase)
**Expected:** YYYY-MM-DD_<owner>_<repo>.md with lowercase owner (folder-structure.md §8 slug rules: lowercase only)
**Suggested fix:** Rename to 2026-08-30_posthog_posthog.md (or add a folder-structure.md exception for GitHub owner casing)

---

## Issue 5: Backup file in wiki/drafts/ violates naming convention

**Path:** wiki/drafts/2026-08-30_anthropic-cybersecurity-skills-backup-2026-09-01.md
**Severity:** WARNING
**Category:** Naming
**Issue:** Draft filename: lowercase-hyphen only
**Current:** 2026-08-30_anthropic-cybersecurity-skills-backup-2026-09-01.md (date-prefix + underscore + `-backup-` suffix)
**Expected:** <lowercase-hyphen-slug>.md (folder-structure.md §8)
**Suggested fix:** Move backups out of wiki/drafts/ (or rename to lowercase-hyphen slug); draft zone is for rejected files awaiting review

---

## Issue 6: Backup file in wiki/drafts/ violates naming convention

**Path:** wiki/drafts/2026-08-30_archify-backup-2026-09-01.md
**Severity:** WARNING
**Category:** Naming
**Issue:** Draft filename: lowercase-hyphen only
**Current:** 2026-08-30_archify-backup-2026-09-01.md (date-prefix + underscore + `-backup-` suffix)
**Expected:** <lowercase-hyphen-slug>.md (folder-structure.md §8)
**Suggested fix:** Move backups out of wiki/drafts/ (or rename to lowercase-hyphen slug); draft zone is for rejected files awaiting review

---

## Issue 7: Backup file in wiki/drafts/ violates naming convention

**Path:** wiki/drafts/2026-08-30_impeccable-backup-2026-09-01.md
**Severity:** WARNING
**Category:** Naming
**Issue:** Draft filename: lowercase-hyphen only
**Current:** 2026-08-30_impeccable-backup-2026-09-01.md (date-prefix + underscore + `-backup-` suffix)
**Expected:** <lowercase-hyphen-slug>.md (folder-structure.md §8)
**Suggested fix:** Move backups out of wiki/drafts/ (or rename to lowercase-hyphen slug); draft zone is for rejected files awaiting review

---

## Issue 8: Backup file in wiki/drafts/ violates naming convention

**Path:** wiki/drafts/2026-08-30_openviking-backup-2026-09-01.md
**Severity:** WARNING
**Category:** Naming
**Issue:** Draft filename: lowercase-hyphen only
**Current:** 2026-08-30_openviking-backup-2026-09-01.md (date-prefix + underscore + `-backup-` suffix)
**Expected:** <lowercase-hyphen-slug>.md (folder-structure.md §8)
**Suggested fix:** Move backups out of wiki/drafts/ (or rename to lowercase-hyphen slug); draft zone is for rejected files awaiting review

---

## Issue 9: Backup file in wiki/drafts/ violates naming convention

**Path:** wiki/drafts/2026-08-30_posthog-backup-2026-09-01.md
**Severity:** WARNING
**Category:** Naming
**Issue:** Draft filename: lowercase-hyphen only
**Current:** 2026-08-30_posthog-backup-2026-09-01.md (date-prefix + underscore + `-backup-` suffix)
**Expected:** <lowercase-hyphen-slug>.md (folder-structure.md §8)
**Suggested fix:** Move backups out of wiki/drafts/ (or rename to lowercase-hyphen slug); draft zone is for rejected files awaiting review

---

## Issue 10: Backup file in wiki/drafts/ violates naming convention

**Path:** wiki/drafts/2026-08-30_threeui-backup-2026-09-01.md
**Severity:** WARNING
**Category:** Naming
**Issue:** Draft filename: lowercase-hyphen only
**Current:** 2026-08-30_threeui-backup-2026-09-01.md (date-prefix + underscore + `-backup-` suffix)
**Expected:** <lowercase-hyphen-slug>.md (folder-structure.md §8)
**Suggested fix:** Move backups out of wiki/drafts/ (or rename to lowercase-hyphen slug); draft zone is for rejected files awaiting review

---

## Issue 11: Backup file in wiki/drafts/ violates naming convention

**Path:** wiki/drafts/src_ai-engineering-skills-map-building-deploying-ai-applications-backup-2026-09-01.md
**Severity:** WARNING
**Category:** Naming
**Issue:** Draft filename: lowercase-hyphen only
**Current:** src_ai-engineering-skills-map-building-deploying-ai-applications-backup-2026-09-01.md (src_ prefix + `-backup-` suffix)
**Expected:** <lowercase-hyphen-slug>.md (folder-structure.md §8)
**Suggested fix:** Move backups out of wiki/drafts/ (or rename to lowercase-hyphen slug); draft zone is for rejected files awaiting review

---

## Issue 12: Backup file in wiki/drafts/ violates naming convention

**Path:** wiki/drafts/src_ai-engineering-skills-map-software-engineering-fundamentals-backup-2026-09-01.md
**Severity:** WARNING
**Category:** Naming
**Issue:** Draft filename: lowercase-hyphen only
**Current:** src_ai-engineering-skills-map-software-engineering-fundamentals-backup-2026-09-01.md (src_ prefix + `-backup-` suffix)
**Expected:** <lowercase-hyphen-slug>.md (folder-structure.md §8)
**Suggested fix:** Move backups out of wiki/drafts/ (or rename to lowercase-hyphen slug); draft zone is for rejected files awaiting review

---

## Summary

| Metric | Value |
|---|---|
| Total paths checked | 56011 |
| Total issues | 12 |
| ERROR | 2 |
| WARNING | 10 |
| INFO | 0 |
| Truncated | No (within 20-issue limit) |

**Recurring issues (carried forward, NOT re-escalated):**
- `openclaw-workspace-state.json` — 11th consecutive run (08-22 → 09-02), root cause confirmed in vendor source (pitfall #9)
- `wiki/HEARTBEAT.md` — 7th consecutive run (08-26 → 09-02), symlink to .openclaw/HEARTBEAT.md

**Progress — RESOLVED:**
- **`raw/repos/` naming [SYSTEMATIC VIOLATION] from 08-31/09-01 is RESOLVED.** All 6 repos files renamed to include the owner segment on 2026-09-01 (git commit `2ba955d1`, 10:02) — e.g. `2026-08-30_impeccable.md` → `2026-08-30_juliuss1907_impeccable.md`. 4 of 6 now fully compliant. 2 residual WARNINGs (Issues 3-4) remain: `MengTo` and `PostHog` owner segments preserve GitHub casing → violates lowercase slug rule. Fix Agent đã xử lý rename chính; chỉ còn 2 file cần lowercase hóa owner.

**New issues this run:**
- 8 `*-backup-2026-09-01.md` files in `wiki/drafts/` (Issues 5-12) — created by Fix Agent at 09:57 on 2026-09-01 as backups during the repos + slug renames. All violate the drafts naming convention (date-prefix/underscore/`-backup-` suffix, and `src_` prefix on 2 files). [SYSTEMATIC VIOLATION] escalated below.

**Clean streaks:**
- `memory/` + `state/` absent — 10th consecutive clean run
- No empty directories — 0 INFO

**Delta from 09-01 (pending):** 8→12 issues, 2→2 ERROR, 6→10 WARNING, paths 55989→56011 (+22). +8 WARNINGs (draft backups) −6 repos WARNINGs (renamed, resolved) + 2 residual repos casing WARNINGs = net +4. 0 new ERRORs.

---

## Escalation

```
[SYSTEMATIC VIOLATION] Naming — wiki/drafts/ backup files (Fix Agent 09-01 rename operation)
Pattern: 8/8 backup files created by Fix Agent at 09:57 on 2026-09-01 during the repos + slug
         renames violate the wiki/drafts/ naming convention (<lowercase-hyphen-slug>.md):
         - 6 files use date-prefix + underscore + '-backup-2026-09-01' suffix
           (e.g. 2026-08-30_impeccable-backup-2026-09-01.md)
         - 2 files use 'src_' prefix + '-backup-2026-09-01' suffix
           (e.g. src_ai-engineering-skills-map-building-deploying-ai-applications-backup-2026-09-01.md)
Likely cause: Fix Agent leaves pre-rename backup copies inside wiki/drafts/ (the drafts zone is
              intended for rejected files awaiting review, not backup storage).
Recommendation: Update Fix Agent SKILL.md to (a) place pre-rename backups outside the KB or in a
                dedicated backup location (not wiki/drafts/), or (b) clean up backup files after
                the rename is verified. Current 8 files: Fix Agent archives or removes them once
                the renames are confirmed good.
Note: distinct from the raw/repos/ naming violation (now RESOLVED) — different zone, different
      process (Fix Agent backups vs Ingest Agent naming). First escalation of this pattern.
```

Note: `openclaw-workspace-state.json` and `wiki/HEARTBEAT.md` are NOT re-escalated — both are documented recurring leaks with confirmed root causes (SKILL.md pitfall #9 for the state file; process-level symlink mirror for HEARTBEAT). The `raw/repos/` naming violation escalated 08-31/09-01 is RESOLVED (renamed 09-01) and is NOT re-escalated. `[SYSTEMATIC VIOLATION]` above is the first escalation of the new Fix Agent backup-naming pattern.
