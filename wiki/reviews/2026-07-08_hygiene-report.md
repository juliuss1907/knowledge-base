# Hygiene Inspection — 2026-07-08

**Status:** pending
**Issues found:** 3
**Created:** 2026-07-08 23:30:00 +0700
**Validator:** hygiene-inspector

**Paths checked:** 51,724

---

## Issue 1: memory/ folder at root level (recurring — lần 5)

**Path:** `memory/`
**Severity:** ERROR
**Category:** Path
**Issue:** Folder not in root whitelist — recurring orphan
**Current:** `memory/` directory at knowledge base root
**Expected:** Root folders limited to: `.git`, `.obsidian`, `.openclaw`, `.hermes`, `context`, `raw`, `wiki`, `scripts`
**Suggested fix:** Move all contents to `.openclaw/memory/`, then `rmdir memory/`

**Recurrence history:**
- 07-03: First detected (with `2026-07-03.md` inside)
- 07-04: Still present (same file, unchanged)
- 07-05: Resolved (KB 100% clean — Julius approved Fix Agent action)
- 07-06: Reappeared (3rd occurrence, new file `compilation-log.md`)
- 07-07: Still present (4th occurrence, `compilation-log.md` same file, no new content)
- 07-08: **Still present (5th occurrence, +1 new file `2026-07-08.md`)**

**Root cause:** Process(es) writing to `memory/` path instead of `.openclaw/memory/`. File deletion alone is transient — the writing process must be identified and its output path corrected.

**⚠️ ESCALATION — 5th occurrence in 6 days:** File cleanup resolves nothing. The `memory/` folder was migrated to `.openclaw/memory/` in folder-structure.md v1.2 (2026-05-17), but at least one process (compile agent, memory logging, or cron job) still targets the old path.

---

## Issue 2: memory/2026-07-08.md — content file in orphaned folder

**Path:** `memory/2026-07-08.md`
**Severity:** WARNING
**Category:** Path
**Issue:** New memory/state file created today inside the orphaned `memory/` folder
**Current:** `memory/2026-07-08.md` (3,074 bytes — session memory for Jul 6-8)
**Expected:** This file should be in `.openclaw/memory/2026-07-08.md`
**Suggested fix:** `mv memory/2026-07-08.md .openclaw/memory/2026-07-08.md`

**Note:** This is a new file (dated today). The same process that creates daily memory dumps is writing to `memory/` instead of `.openclaw/memory/`. Content includes ingestion activity (Jul 6-7), compile activity (Jul 7-8), Index Agent status, Hermes report summaries, and system state.

---

## Issue 3: memory/compilation-log.md — compile log in orphaned folder

**Path:** `memory/compilation-log.md`
**Severity:** WARNING
**Category:** Path
**Issue:** Compilation log persists in orphaned `memory/` folder — unchanged since 07-06
**Current:** `memory/compilation-log.md` (last modified Jul 6 08:16, 1,059 bytes)
**Expected:** This file should be in `.openclaw/memory/compilation-log.md`
**Suggested fix:** `mv memory/compilation-log.md .openclaw/memory/compilation-log.md`

**Carry-over from 07-06 and 07-07:** Same file, no new content. The compile agent (OpenClaw) wrote this log to the old `memory/` path during the Jul 6 08:00 compilation run.

---

## Clean zones (no issues)

- ✅ **context/** — 100% compliant (2 files: context.md, USER.md)
- ✅ **raw/** — all 6 subfolders compliant, all content files follow naming conventions
- ✅ **wiki/meta/** — 3 files present (format-spec.md, folder-structure.md, index-spec.md)
- ✅ **wiki/sources/** — all `src_` prefixed, lowercase-hyphen slugs
- ✅ **wiki/concepts/** — all lowercase-hyphen slugs
- ✅ **wiki/tag/** — all compliant
- ✅ **wiki/topic/** — all compliant
- ✅ **wiki/drafts/** — all compliant
- ✅ **wiki/reviews/** — all reports follow canonical naming
- ✅ **wiki/reviews/archive/** — all archived reports in YYYY-MM/ subfolders
- ✅ **Root symlinks** — HEARTBEAT.md, IDENTITY.md, SOUL.md, TOOLS.md, USER.md all present
- ✅ **HEARTBEAT leak** — resolved for 10 days (since 06-28)
- ✅ **state/** — resolved, not present
- ✅ **scripts/** — compliant

---

## Delta from 2026-07-07 (PENDING — 2 issues)

| Metric | 07-07 | 07-08 | Δ |
|---|---|---|---|
| Total issues | 2 | 3 | +1 |
| ERROR | 1 | 1 | 0 |
| WARNING | 1 | 2 | +1 |
| INFO | 0 | 0 | 0 |
| Paths checked | 51,715 | 51,724 | +9 |

**Change:** +1 new file `memory/2026-07-08.md` appeared (daily memory log). `memory/` folder and `compilation-log.md` unchanged from 07-07.

**KB structure health: 99.994%** (3/51,724 paths with issues, down from 99.996% on 07-07)

---

## Recommended actions

1. **Immediate (Fix Agent):** `mv memory/2026-07-08.md .openclaw/memory/` → `mv memory/compilation-log.md .openclaw/memory/` → `rmdir memory/`
2. **🚨 Process fix (Julius):** Identify and fix the process(es) writing to `memory/` path instead of `.openclaw/memory/`. Likely candidates:
   - OpenClaw compile agent output path
   - Hermes memory logging cron job
   - Heartbeat/session snapshot script
3. **Prevention:** Add `memory/` to `.gitignore` so any future process leakage doesn't create tracked files

---

**Report:** `wiki/reviews/2026-07-08_hygiene-report.md`
