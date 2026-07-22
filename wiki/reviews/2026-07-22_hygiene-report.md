# Hygiene Inspection — 2026-07-22

**Status:** pending
**Issues found:** 1
**Created:** 2026-07-22 23:35:00
**Validator:** hygiene-inspector

**Paths checked:** 51944

---

## Issue 1: Draft filename uses `src_` prefix + underscore

**Path:** `wiki/drafts/src_is-there-anything-left-to-build-in-crypto-wintermute-backup-2026-07-20.md`
**Severity:** WARNING
**Category:** Naming
**Issue:** Draft filename does not follow lowercase-hyphen convention. File uses `src_` prefix (a sources/ naming pattern) and contains an underscore after `src`.
**Current:** `src_is-there-anything-left-to-build-in-crypto-wintermute-backup-2026-07-20.md`
**Expected:** `<lowercase-hyphen-slug>.md` (e.g., `is-there-anything-left-to-build-in-crypto-wintermute-backup-2026-07-20.md`)
**Suggested fix:** Rename to remove `src_` prefix and replace underscore with hyphen. Note: this is a Fix Agent backup file — cosmetic only. Can rename or leave as-is.

---

## Summary

| Metric | Value |
|---|---|
| **ERRORs** | 0 |
| **WARNINGs** | 1 |
| **INFOs** | 0 |
| **Issue rate** | 0.002% (1/51944) |

**Zero structural violations.** The single WARNING is a cosmetic naming issue on a Fix Agent backup file in `wiki/drafts/` — same file flagged on 2026-07-21. The `src_` prefix (a `wiki/sources/` naming convention) and underscore were preserved from the original source filename when the backup was created.

**Notable:**
- `memory/` root folder — absent. First clean run since 07-02 where it does not appear. Resolution appears permanent post-Fix-Agent bulk apply (07-21).
- `state/` root folder — absent. Resolved since 07-20 bulk apply.
- `wiki/reviews/HEARTBEAT.md` — absent. No heartbeat leak this run.
- `raw/.last_heartbeat` — absent.
- All root-level items conform to whitelist.
- All wiki/ subfolders conform.
- All raw/ subfolders and content files conform.

**Clean streak:** 2 days of 0 ERRORs (07-21 → 07-22).
