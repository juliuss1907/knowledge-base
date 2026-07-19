# Action Required — Report Status

> Consolidated list of Hermes validation reports and approval state
> Updated automatically after each validation run
> Julius reviews this file to approve/reject fixes

**Last updated:** 2026-07-19 23:15

---

## Summary

**Pending reports awaiting review:** 12
**Last batch applied:** 6 reports (07-12 + 07-13) **APPLIED** 2026-07-14 by Fix Agent
**Latest approved:** Format 07-14 — approved 2026-07-15 (306W forward-ref wikilinks, 0 ERRORs)

| Status | Date | Report | Issues | Summary |
|---|---|---|---|---|---|
| ✅ APPROVED | 07-14 | Format | 306W | Broken wikilinks (forward-refs). 0 ERRORs. Cleanest run ever. Approved 2026-07-15. |
| ✅ CLEAN | 07-14 | Hygiene | 0 | No violations. 51,831 paths. All recurring issues resolved. |
| 🔍 PENDING | 07-15 | Hygiene | 4 (2E+1W+1I) | Recurring root folders: memory/ and state/. Regression from clean 07-14. |
| 🔍 PENDING | 07-15 | Format | 313W | Broken wikilinks (forward-refs). 0 ERRORs. Clean streak continues. |
| 🔍 PENDING | 07-15 | Output | 4 (3W+1I) | 4 new files. Double-i typos (11 instances). 3 fwd-ref wikilinks. 1 low key-ideas. |
| 🔍 PENDING | 07-16 | Output | 1 (1W) | 6 new files. New "ngườI" capital-I typo variant (5 instances). All files well-formed. |
| 🔍 PENDING | 07-16 | Format | 319W | Broken wikilinks (forward-refs). 0 ERRORs. Three-day clean streak. +11 files. |
| 🔍 PENDING | 07-16 | Hygiene | 4 (2E+1W+1I) | Recurring root folders: memory/ and state/. Identical to 07-15. |
| 🔍 PENDING | 07-17 | Format | 324 (5E+319W) | 5 ERRORs: 3 missing sections, 2 slug > 50. Clean streak broken. |
| 🔍 PENDING | 07-17 | Hygiene | 4 (2E+1W+1I) | Recurring root folders: memory/ and state/. Identical to 07-15/07-16. |
| 🔍 PENDING | 07-18 | Output | 5 (1E+4W+0I) | 14 new files. Capital-I typo exploded (237+ instances). 1 truncated concept. 1 broken wikilink. |
| 🔍 PENDING | 07-18 | Format | 324 (5E+319W) | Identical to 07-17. 0 change. Same 5 ERRORs persist. |
| 🔍 PENDING | 07-18 | Hygiene | 4 (2E+1W+1I) | Recurring root folders: memory/ and state/. Fourth identical run. |
| 🔍 PENDING | 07-19 | Format | 324 (5E+319W) | Identical to 07-17/07-18. Third consecutive plateau. Same 5 ERRORs persist unfixed. |

---

## Pending Reports

### Format 2026-07-14 (✅ APPROVED 2026-07-15)

- **Report:** `wiki/reviews/2026-07-14_format-report.md`
- **Summary:** 306 WARNINGs — all broken wikilinks (forward-references to uncompiled concepts). 0 ERRORs, 0 INFOs across 769 files. All structural issues from June resolved. Cleanest format report in KB history.
- **Delta vs 07-13:** -9 WARNINGs, +11 files. Same forward-ref pattern, slightly improved.
- **Actions needed:** None — all issues are expected forward-references that resolve as KB grows. Approved.

### 🔍 Format Validation — 2026-07-15 (23:15)

- **Report:** `wiki/reviews/2026-07-15_format-report.md`
- **Summary:** 313 WARNINGs (all broken wikilinks — forward-references). 0 ERRORs, 0 INFOs across 774 files. Zero structural format violations. 1 raw-file wikilink resolution issue in `src_why-the-math-mafia-is-doing-well-jesse-zhang.md`.
- **Delta vs 07-14:** +7 WARNINGs, +5 files (+3 concepts, +1 source, +1 topic). Same forward-ref pattern.
- **Actions needed:** None — all wikilinks are expected forward-references. The single raw-file link may be a data-entry issue in the source's `original` field.
- **Status:** pending

### Hygiene 2026-07-14 (✅ CLEAN)

- **Report:** `wiki/reviews/2026-07-14_hygiene-report.md`
- **Summary:** 0 issues across 51,831 paths. KB structure fully compliant with folder-structure.md v1.2. All previously recurring issues (HEARTBEAT leak, state/, memory/, selected_concepts.txt) resolved.
- **Actions needed:** None. Report is informational only.

### 🔍 Output Validation — 2026-07-15 (23:10)

- **Report:** `wiki/reviews/2026-07-15_output-report.md`
- **Summary:** 4 issues (0 ERROR, 3 WARNING, 1 INFO). 4 new files (1 source + 3 concepts). Systemic double-i typos across all 4 files (11 instances). 3 broken forward-reference wikilinks. 1 file with only 4 key ideas.
- **Actions needed:** Fix Agent should run sed for double-i + hook-above typos. Forward-ref wikilinks are expected — no action unless concepts won't be compiled.
- **Status:** pending

### 🔍 Output Validation — 2026-07-16 (23:10)

- **Report:** `wiki/reviews/2026-07-16_output-report.md`
- **Summary:** 1 issue (0 ERROR, 1 WARNING, 0 INFO). 6 new files (1 source + 5 concepts). New typo variant: "ngườI" with capital I instead of lowercase i after "ờ" — 5 instances across 2 files. Third variant of the same Compile Agent root cause (after double-i and spacing merge). All 6 files structurally complete with adequate definitions and key ideas.
- **Actions needed:** Run sed to fix "ngườI" → "người" in 2 files. Recommend reviewing Compile Agent prompt to fix root cause of systematic diacritic errors.
- **Status:** pending

### 🔍 Hygiene Validation — 2026-07-15 (23:30)

- **Report:** `wiki/reviews/2026-07-15_hygiene-report.md`
- **Summary:** 4 issues (2 ERROR, 1 WARNING, 1 INFO) across 51,845 paths. Regression from clean 07-14 baseline.
  - **`memory/` at root** (ERROR): Recurring root folder — 7th occurrence since 07-03. Contains `2026-07-15.md`. Process-level leak: a writer targets `memory/` instead of `.openclaw/memory/`.
  - **`state/` at root** (ERROR): Recurring empty directory — 3rd recurrence since original 06-25 resolution. Process recreates an empty `state/` at KB root.
  - **`memory/2026-07-15.md`** (WARNING): Orphan file inside non-whitelisted root folder. Should be in `.openclaw/memory/`.
  - **Empty `state/`** (INFO): Redundant with ERROR above.
- **Delta vs 07-14:** +4 issues (07-14 was clean at 0 issues)
- **Actions needed:** Move `memory/2026-07-15.md` to `.openclaw/memory/`, then `rmdir memory/ state/`. Identify and fix the process(es) creating these root folders — file deletions are transient without process fixes.
- **Status:** pending

### 🔍 Hygiene Validation — 2026-07-16 (23:30)

- **Report:** `wiki/reviews/2026-07-16_hygiene-report.md`
- **Summary:** 4 issues (2 ERROR, 1 WARNING, 1 INFO) across 51,861 paths. Identical to 07-15 baseline — no new violations, no regressions, no resolutions.
  - **`memory/` at root** (ERROR): Recurring root folder — 8th occurrence since 07-03. Contains `2026-07-15.md`. Process-level leak: a writer targets `memory/` instead of `.openclaw/memory/`.
  - **`state/` at root** (ERROR): Recurring empty directory — 4th recurrence since original 06-25 resolution. Process recreates an empty `state/` at KB root.
  - **`memory/2026-07-15.md`** (WARNING): Orphan file inside non-whitelisted root folder. Should be in `.openclaw/memory/`.
  - **Empty `state/`** (INFO): Redundant with ERROR above.
- **Delta vs 07-15:** 0 change (same 4 issues, paths_checked +16 from report file writes).
- **Actions needed:** Move `memory/2026-07-15.md` to `.openclaw/memory/`, then `rmdir memory/ state/`. Identify and fix the process(es) creating these root folders — file deletions are transient without process fixes.
- **Status:** pending

### 🔍 Format Validation — 2026-07-16 (23:15)

- **Report:** `wiki/reviews/2026-07-16_format-report.md`
- **Summary:** 319 WARNINGs (all broken wikilinks — forward-references). 0 ERRORs, 0 INFOs across 780 files. Three-day clean streak with zero structural format violations. 199 unique broken targets across 296 individual + 21 summary-group WARNINGs. 2 raw-file original link issues persist from 07-15.
- **Delta vs 07-14 (approved):** +13 WARNINGs, +11 files (+7 concepts, +2 sources, +2 topics). Same forward-ref pattern.
- **Actions needed:** None — all wikilinks are expected forward-references. Raw-file links are transient ingest timing issues.
- **Status:** pending

### 🔍 Format Validation — 2026-07-17 (23:15)

- **Report:** `wiki/reviews/2026-07-17_format-report.md`
- **Summary:** 324 issues (5 ERROR, 319 WARNING, 0 INFO) across 796 files. **Clean streak broken.** 3 concepts missing required sections (2× Key ideas, 1× Sources). 2 source slugs exceed 50-char limit. 319 forward-ref wikilinks (expected, no action). 2 raw-file original link issues persist.
- **Delta vs 07-14 (approved):** +5 ERROR, +13 WARNING, +27 files (+17 concepts, +5 sources, +5 topics).
- **Actions needed:** 
  - 🔴 Add `## Key ideas` to `destination-vs-vehicle.md` and `social-attraction.md`
  - 🔴 Add `## Sources` to `psychic-energy.md`
  - 🟡 Shorten 2 source slugs (`src_is-there-anything-left-to-build-in-crypto-wintermute.md` → 52 chars, `src_the-5-laws-of-people-who-never-chase-gabriel-reality.md` → 52 chars)
  - 🟢 Forward-ref wikilinks — no action
- **Status:** pending

### 🔍 Hygiene Validation — 2026-07-17 (23:30)

- **Report:** `wiki/reviews/2026-07-17_hygiene-report.md`
- **Summary:** 4 issues (2 ERROR, 1 WARNING, 1 INFO) across 51,883 paths. Identical to 07-15 and 07-16 baseline — no new violations, no regressions, no resolutions. Third consecutive run with the same 4 issues.
  - **`memory/` at root** (ERROR): Recurring root folder — 9th occurrence since 07-03. Contains `2026-07-15.md`. Process-level leak: a writer targets `memory/` instead of `.openclaw/memory/`.
  - **`state/` at root** (ERROR): Recurring empty directory — 5th recurrence since original 06-25 resolution. Process recreates an empty `state/` at KB root.
  - **`memory/2026-07-15.md`** (WARNING): Orphan file inside non-whitelisted root folder. Should be in `.openclaw/memory/`.
  - **Empty `state/`** (INFO): Redundant with ERROR above.
- **Delta vs 07-16:** 0 change (same 4 issues, paths_checked +22 from report/action file writes).
- **Actions needed:** Move `memory/2026-07-15.md` to `.openclaw/memory/`, then `rmdir memory/ state/`. Identify and fix the process(es) creating these root folders — file deletions are transient without process fixes.
- **Status:** pending

### 🔍 Output Validation — 2026-07-18 (23:09)

- **Report:** `wiki/reviews/2026-07-18_output-report.md`
- **Summary:** 5 issues (1 ERROR, 4 WARNING, 0 INFO) across 592 files. 14 new files from 2026-07-17 batch (3 sources + 11 concepts). Capital-I typo mở rộng nghiêm trọng — 237+ instances trên toàn bộ 14 file mới, không chỉ giới hạn ở "ngườI" như báo cáo 07-16 mà ảnh hưởng đến MỌI từ tiếng Việt kết thúc bằng lowercase-i sau nguyên âm. 1 ERROR: `psychic-energy.md` truncated — thiếu Sources và Notes. 1 broken wikilink: `[[crypto-ai-stacking]]` không tồn tại. Tất cả file có cấu trúc sections đầy đủ.
- **Actions needed:**
  - 🔴 Re-compile `psychic-energy.md` (truncated)
  - 🔴 Fix hoặc remove broken wikilink `[[crypto-ai-stacking]]` trong `src_is-there-anything-left-to-build-in-crypto-wintermute.md`
  - 🟡 Chạy sed script mở rộng để fix 237+ capital-I instances trên toàn bộ 14 file (script trong report)
  - 🟡 Escalate Compile Agent prompt — root cause của capital-I đang ngày càng nghiêm trọng, ảnh hưởng đến tất cả batch mới
- **Status:** pending

### 🔍 Format Validation — 2026-07-19 (23:15)

- **Report:** `wiki/reviews/2026-07-19_format-report.md`
- **Summary:** 324 issues (5 ERROR, 319 WARNING, 0 INFO) across 796 files. **Identical to 07-17 and 07-18 — third consecutive day at plateau.** No files added or removed since 07-17. Same 5 ERRORs persist unfixed (3 missing sections, 2 slug > 50). 319 forward-ref wikilinks (same targets). 2 raw-file original link issues persist. This is a stable plateau — the KB hasn't changed in 3 days.
- **Delta vs 07-18 (previous):** 0 — fully identical results.
- **Delta vs 07-14 (approved):** +5 ERROR, +13 WARNING, +27 files (+17 concepts, +5 sources, +5 topics).
- **Actions needed:**
  - 🔴 Add `## Key ideas` to `destination-vs-vehicle.md` and `social-attraction.md`
  - 🔴 Add `## Sources` to `psychic-energy.md` (also flagged as truncated in Output 07-18)
  - 🟡 Shorten 2 source slugs exceeding 50-char limit
  - 🟢 Forward-ref wikilinks — no action
- **Status:** pending

### 🔍 Format Validation — 2026-07-18 (23:16)

- **Report:** `wiki/reviews/2026-07-18_format-report.md`
- **Summary:** 324 issues (5 ERROR, 319 WARNING, 0 INFO) across 796 files. **Identical to 07-17 — 0 change.** No files added or removed since yesterday. Same 5 ERRORs persist unfixed (3 missing sections, 2 slug > 50). 319 forward-ref wikilinks (same targets). 2 raw-file original link issues persist. This is a stable plateau — the KB hasn't changed, so the issues haven't changed.
- **Delta vs 07-17 (previous):** 0 — fully identical results.
- **Delta vs 07-14 (approved):** +5 ERROR, +13 WARNING, +27 files (+17 concepts, +5 sources, +5 topics).
- **Actions needed:**
  - 🔴 Add `## Key ideas` to `destination-vs-vehicle.md` and `social-attraction.md`
  - 🔴 Add `## Sources` to `psychic-energy.md` (also flagged as truncated in Output 07-18)
  - 🟡 Shorten 2 source slugs exceeding 50-char limit
  - 🟢 Forward-ref wikilinks — no action
- **Status:** pending

---

### 🔍 Hygiene Validation — 2026-07-18 (23:30)

- **Report:** `wiki/reviews/2026-07-18_hygiene-report.md`
- **Summary:** 4 issues (2 ERROR, 1 WARNING, 1 INFO) across 51,889 paths. Identical to 07-15, 07-16, and 07-17 baseline — fourth consecutive run with the same 4 issues.
  - **`memory/` at root** (ERROR): Recurring root folder — 10th occurrence since 07-03. Contains `2026-07-15.md`. Process-level leak: a writer targets `memory/` instead of `.openclaw/memory/`.
  - **`state/` at root** (ERROR): Recurring empty directory — 6th recurrence since original 06-25 resolution. Process recreates an empty `state/` at KB root.
  - **`memory/2026-07-15.md`** (WARNING): Orphan file inside non-whitelisted root folder. Should be in `.openclaw/memory/`.
  - **Empty `state/`** (INFO): Redundant with ERROR above.
- **Delta vs 07-17:** 0 change (same 4 issues, paths_checked +6 from report/action file writes).
- **Actions needed:** Move `memory/2026-07-15.md` to `.openclaw/memory/`, then `rmdir memory/ state/`. Identify and fix the process(es) creating these root folders — file deletions are transient without process fixes. **Fourth consecutive identical run — root cause is process-level, not file-level.**
- **Status:** pending

---

## Applied Reports

### Batch 2026-07-12 + 2026-07-13 (APPLIED 2026-07-14)

- ✅ Format 07-12: 307 WARNINGs — forward-ref wikilinks, no action needed
- ✅ Format 07-13: 315 WARNINGs — forward-ref wikilinks, no action needed
- ✅ Output 07-12: Removed broken `[[forgetting-curve]]` wikilink from `spacing-effect.md`
- ✅ Output 07-13: Removed 3 broken wikilinks:
  - `[[delayed-gratification]]` from `goal-announcement-trap.md`, `intrinsic-motivation.md`, `src_the-art-of-being-overlooked-stay-silent.md`
  - `[[onchain-loyalty-programs]]` from `arcade-tokens.md`, `token-economic-mechanics.md`, `src_the-most-underrated-token-type.md`
  - `[[utility-tokens]]` from `arcade-tokens.md`, `token-economic-mechanics.md`
- ✅ Hygiene 07-12: `selected_concepts.txt` already cleaned (not present)
- ✅ Hygiene 07-13: `selected_concepts.txt` already cleaned (not present)

**12 fixes applied (6 wikilink removals), 0 errors, 0 skipped.**

### All previous batches (APPLIED)

Tất cả các batch từ 2026-06-19 đến 2026-07-11 đã được applied. Xem MEMORY.md để biết chi tiết lịch sử.
