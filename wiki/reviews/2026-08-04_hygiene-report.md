# Hygiene Inspection — 2026-08-04

**Status:** pending
**Issues found:** 3 (1 ERROR, 1 WARNING, 1 INFO)
**Created:** 2026-08-04 23:30
**Validator:** hygiene-inspector

**Paths checked:** 53,482

**Severity breakdown:** 1 ERROR · 1 WARNING · 1 INFO

---

## Delta from 2026-08-03

Δ = 0 (identical results). Same 3 issues: `state/` root folder (ERROR + INFO), `raw/websites/tools.md` naming (WARNING). KB is static — no files or folders added, changed, or removed since 08-03.

---

## Issue 1: Recurring root folder — state/

**Path:** `state/`
**Severity:** ERROR
**Category:** Orphan
**Issue:** Recurring root folder not in whitelist: state/
**Current:** `state/` (empty directory, recreated 2026-08-02)
**Expected:** `state/` is not in root whitelist. Only `.git`, `.obsidian`, `.openclaw`, `.hermes`, `context`, `raw`, `wiki`, `scripts` are allowed.
**Suggested fix:** `rmdir state/` + investigate what process recreates it. Previously resolved 2026-06-27, recreated 2026-07-02, resolved again, then recreated 2026-08-02. Pattern: sporadic recreation (~monthly).

---

## Issue 2: Leftover index file from raw/tools/ migration

**Path:** `raw/websites/tools.md`
**Severity:** WARNING
**Category:** Naming
**Issue:** Raw content filename does not match convention
**Current:** `tools.md` (no date prefix)
**Expected:** `YYYY-MM-DD_<slug>.md`
**Suggested fix:** Verify `tools.md` items are already tracked in `raw/websites/websites.md`, then delete `raw/websites/tools.md`. Update Fix Agent migration procedure to handle leftover index files when moving content between raw subfolders.

**Context:** This file has persisted since the 2026-08-01 Fix Agent batch that moved `raw/tools/` content to `raw/websites/`. The old index file was moved along with content files but does not follow the naming convention for content files. Flagged on 08-01, 08-03, 08-04 — 3rd consecutive run.

---

## Issue 3: Empty directory — state/

**Path:** `state/`
**Severity:** INFO
**Category:** Orphan
**Issue:** Empty directory
**Current:** `state/` (no files or subdirectories)
**Expected:** Non-empty directory or removed
**Suggested fix:** `rmdir state/`

---

## Systemic notes

- **`state/` recurrence:** This folder has been recreated approximately monthly (06-27 resolved → 07-02 recreated → resolved → 08-02 recreated). The creating process has not been identified. Recommend adding a watch on root-level folder creation or auditing cron/agent configs for `state/` as an output path.
- **`tools.md` staleness:** 3rd consecutive run with this issue. Fix Agent migration procedure should include a cleanup step for leftover index files when removing a raw subfolder. The 08-01 batch moved files but left the index behind.

---

## All clear

- ✅ No `memory/` root folder — absent since 07-26 resolution
- ✅ No HEARTBEAT leaks — `wiki/reviews/HEARTBEAT.md` and `raw/.last_heartbeat` absent
- ✅ Agent homes clean — no user content in `.openclaw/` or `.hermes/`
- ✅ All wiki/ subfolders compliant — concepts, sources, tag, topic, drafts, meta paths valid
- ✅ All raw/ subfolders compliant — articles, posts, websites, videos, papers, repos paths valid
- ✅ Archive structure valid — all archived reports in `YYYY-MM/` subfolders
- ✅ Context folder compliant — exactly `context.md` + `USER.md`
- ✅ Root-level whitelist compliant — no orphan files at root
- ✅ Naming conventions — all wiki/ files follow slug rules
