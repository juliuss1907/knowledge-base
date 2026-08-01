# Hygiene Inspection — 2026-07-30 (23:30)

**Status:** approved
**Approved by:** Julius
**Approved date:** 2026-08-01
**Issues found:** 3 (3 ERROR)
**Created:** 2026-07-30 23:32 ICT
**Validator:** hygiene-inspector

**Paths checked:** 53,443
**Delta from earlier 07-30 run:** +7 paths

---

## Summary

| Severity | Count |
|---|---|
| ERROR | 3 |
| WARNING | 0 |
| INFO | 0 |

---

## Issue 1–3: [SPEC CONFLICT] `raw/tools/` — Unlisted raw subfolder

**Path:** `raw/tools/`
**Severity:** ERROR
**Category:** Path
**Issue:** `raw/tools/` is not in folder-structure.md v1.2 whitelist. The spec permits exactly 6 raw subfolders: `articles`, `posts`, `websites`, `videos`, `papers`, `repos`. `tools` is not one of them.

| # | File | Date |
|---|---|---|
| 1 | `raw/tools/tools.md` | 2026-07-26 |
| 2 | `raw/tools/2026-07-25_introducing-backsearch-gr-inc.md` | 2026-07-26 |
| 3 | `raw/tools/2026-07-25_monid-ai-agent-tool-platform.md` | 2026-07-26 |

**Current:** 3 files in `raw/tools/` — index + 2 content files. Content appears to be compiled (sources exist in `wiki/sources/`).

**Expected:** Either:
- A) Add `tools` to folder-structure.md raw subfolder whitelist (v1.2 → v1.3) and update the scan script
- B) Move files to an existing subfolder (e.g., `raw/articles/` or `raw/websites/`)

**Suggested fix:** This is a [SPEC CONFLICT]. The folder was created intentionally (Julius or an agent), contains valid compiled content, but the whitelist was not updated. Recommendation: update `folder-structure.md` §6 to add `tools/` as the 7th raw subfolder, add `raw/tools/tools.md` to the index whitelist, and update the scan script's `RAW_SUBFOLDERS` set. All 3 files have correct naming conventions — only the folder itself needs whitelist approval.

---

## Resolved from earlier 07-30 run

- ✅ `state/` root folder — **RESOLVED**. Absent from this scan. Removed between earlier 07-30 run and now.

---

## ✅ Passing

- ✅ No `memory/` at root — 7th consecutive clean run (07-24 through 07-30)
- ✅ No `state/` at root — resolved
- ✅ All wiki/ paths compliant with folder-structure.md
- ✅ All other raw/ paths compliant
- ✅ No .bak/.tmp/.swp files
- ✅ No orphan files outside write zones
- ✅ No duplicate files
- ✅ File naming conventions followed
- ✅ No leaked agent artifacts at root
- ✅ No HEARTBEAT leaks in wiki/reviews/ or raw/
- ✅ `.openclaw/`, `.hermes/` folders clean
- ✅ 53,443 paths validated

---

## Recurring Issues Tracker

| Issue | First Seen | Last Seen | Status |
|---|---|---|---|
| `memory/` at root | 06-19 | 07-26 | ✅ Resolved (7 consecutive clean runs) |
| `state/` at root | Pre-06-27 | 07-30 (earlier) | ✅ Resolved (absent this scan) |
| `raw/tools/` unlisted subfolder | 07-30 (now) | 07-30 (now) | 🔍 New — [SPEC CONFLICT] |
| `random_concepts.txt` | 06-22 | 06-22 | ✅ Resolved |
| `index_kb.py` | 06-22 | 06-22 | ✅ Resolved |

---

## Verdict

**REVISE** — 3 ERRORs for `raw/tools/` unlisted subfolder. Not a hygiene emergency — files are correctly named and placed logically. This is a [SPEC CONFLICT]: the folder-structure.md whitelist needs updating to reflect the actual structure.

**Action item:** Julius should decide: (A) update `folder-structure.md` to add `tools/` as a 7th raw subfolder, or (B) move files to an existing approved subfolder. Either path resolves all 3 ERRORs.
