# Hygiene Inspection — 2026-08-01

**Status:** pending
**Issues found:** 1
**Created:** 2026-08-01 23:30
**Validator:** hygiene-inspector

**Paths checked:** 53,472

---

## Issue 1: Leftover index file in raw/websites/ from tools/ migration

**Path:** raw/websites/tools.md
**Severity:** WARNING
**Category:** Naming
**Issue:** Leftover index file from `raw/tools/` migration. Fix Agent moved the old `raw/tools/tools.md` index to `raw/websites/` during the 08-01 morning fix batch (07-30 + 08-01 hygiene reports), but this file is the level-2 index for the now-removed `raw/tools/` subfolder. It does not follow the `YYYY-MM-DD_<slug>.md` naming convention required for raw content files.
**Current:** `raw/websites/tools.md` — a level-2 index file with YAML frontmatter (`type: index`, `scope: tools`), listing 2 items that are already tracked in `raw/websites/websites.md`
**Expected:** Raw content files must follow `YYYY-MM-DD_<slug>.md` convention. Index files belong in their own subfolder; this one's subfolder no longer exists.
**Suggested fix:** Merge any unique items into `raw/websites/websites.md` (if any), then delete `raw/websites/tools.md`. Fix Agent should update its migration procedure to handle leftover index files when removing a raw subfolder.

---

## Summary

| Dimension | Status |
|---|---|
| Path whitelist | ✅ Clean |
| Naming conventions | ⚠️ 1 WARNING |
| Orphan detection | ✅ Clean |

**Result:** Near-clean run. 1 WARNING is a Fix Agent migration leftover — not a structural defect. The `memory/` and `state/` root folders remain resolved (absent since 07-21). No HEARTBEAT leaks detected.

---
