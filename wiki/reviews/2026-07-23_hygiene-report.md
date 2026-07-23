# Hygiene Inspection — 2026-07-23

**Status:** pending
**Issues found:** 1
**Created:** 2026-07-23 23:35:00
**Validator:** hygiene-inspector

**Paths checked:** 51,963

---

## Issue 1: Draft backup file uses underscores

**Path:** wiki/drafts/src_is-there-anything-left-to-build-in-crypto-wintermute-backup-2026-07-20.md
**Severity:** WARNING
**Category:** Naming
**Issue:** Draft filename uses `src_` prefix and underscores instead of lowercase-hyphen slug
**Current:** `src_is-there-anything-left-to-build-in-crypto-wintermute-backup-2026-07-20.md`
**Expected:** `<lowercase-hyphen-slug>.md`
**Suggested fix:** Rename to use lowercase-hyphen only (e.g., `src-is-there-anything-left-to-build-in-crypto-wintermute-backup-2026-07-20.md`), or leave as-is (cosmetic WARNING-level, backup file)

**Note:** This is the same draft backup file flagged on 07-20, 07-21, and 07-22. Created by Fix Agent bulk apply on 07-20. Renaming is optional — backup files are transient.

---

## Summary

| Severity | Count |
|---|---|
| ERROR | 0 |
| WARNING | 1 |
| INFO | 0 |
| **Total** | **1** |

**Issue rate:** 0.002% (1 / 51,963 paths)

**Status by zone:**

| Zone | Status |
|---|---|
| Root level | ✅ Clean — no orphans or unwhitelisted files |
| context/ | ✅ Clean — exactly context.md + USER.md |
| raw/ | ✅ Clean — all 6 subfolders compliant |
| wiki/meta/ | ✅ Clean — exactly 3 files |
| wiki/sources/ | ✅ Clean — all src_<slug>.md |
| wiki/concepts/ | ✅ Clean — all lowercase-hyphen slugs |
| wiki/tag/ | ✅ Clean |
| wiki/topic/ | ✅ Clean |
| wiki/drafts/ | ⚠ 1 WARNING — backup file naming |
| wiki/reviews/ | ✅ Clean — all reports canonical |
| Agent homes | ✅ Clean — no user content leaks |
| Root folders | ✅ Clean — `memory/` and `state/` remain absent since 07-21 |

---

## Delta from 2026-07-22

- **Paths:** +19 (51,944 → 51,963) — compilation activity on 07-23
- **Issues:** 0 net change (1 → 1) — same draft backup WARNING
- **Root orphans:** `memory/` and `state/` remain resolved for third consecutive day

---

## Recurring issues resolved

- `memory/` root folder — absent since 07-21 (3 consecutive clean runs). Resolution appears permanent after Fix Agent removed the folder and moved contents to `.openclaw/memory/` on 07-20.
- `state/` root folder — absent since 07-20 (no recurrence).
- `wiki/reviews/HEARTBEAT.md` — absent since 06-28-2026.
- `raw/.last_heartbeat` — absent.

---

**End of report**
