# Action Required — Report Status

> Consolidated list of Hermes validation reports and approval state
> Updated automatically after each validation run
> Julius reviews this file to approve/reject fixes

**Last updated:** 2026-08-01 (Connor — validation run, 3 new reports)

---

## Summary

**Pending reports awaiting review:** 4
**Fix queue:** 0 (all applied)
**Last batch applied:** 10 reports (07-21 through 07-24) **APPLIED** 2026-07-25 by Fix Agent

| Status | Date | Type | Issues | Action |
|---|---|---|---|---|
| ✅ APPROVED | 07-30 | Format | 411 (0E+411W) | Review [wiki/reviews/2026-07-30_format-report.md](2026-07-30_format-report.md) |
| ✅ APPROVED | 07-30 | Output | 5+ (1E+2W+3 systemic) | Review [wiki/reviews/2026-07-30_output-report.md](2026-07-30_output-report.md) |
| 🔍 PENDING | 08-01 | Format | 438 (5E+433W) | Review [wiki/reviews/2026-08-01_format-report.md](2026-08-01_format-report.md) |
| 🔍 PENDING | 08-01 | Output | 4+ (0E+2W+3 systemic) | Review [wiki/reviews/2026-08-01_output-report.md](2026-08-01_output-report.md) |
| 🔍 PENDING | 08-01 | Hygiene | 5 (4E+1W) | Review [wiki/reviews/2026-08-01_hygiene-report.md](2026-08-01_hygiene-report.md) |
| 🔍 PENDING | 07-30 | Hygiene | 3 (3E) | Review [wiki/reviews/2026-07-30_hygiene-report.md](2026-07-30_hygiene-report.md) |
| ✅ APPLIED | 07-26 | Format | 357 (0E+357W) | Applied by Fix Agent 2026-07-30 — no fixes needed (forward-refs only) |
| ✅ APPROVED | 07-26 | Output | 5 (1E+2W+1I+forward) | Approved by Julius 27/07/2026 — tự sửa. |
| ✅ APPLIED | 07-26 | Hygiene | 0 (clean) | Applied by Fix Agent 2026-07-30 — no fixes needed (clean run) |
| ✅ APPROVED | 07-25 | Format | 336 (0E+336W) | Approved by Julius 26/07/2026 — all WARNINGs are forward-reference broken wikilinks (content gap, not structural errors). No fixes needed. |
| ✅ APPLIED | 07-25 | Hygiene | 3 (1E+2W) | Applied by Fix Agent 2026-07-26 — moved memory/, renamed draft file |
| ✅ APPLIED | 07-26 | Output | 2 (1E+1I) | Applied by Fix Agent 2026-07-26 — fixed dropped-i typos in 6 files |
| ✅ APPLIED | 07-24 | Format | 337 (1E+336W) | Applied by Fix Agent 2026-07-25 |
| ✅ APPLIED | 07-23 | Format | 337 (1E+336W) | Applied by Fix Agent 2026-07-25 |
| ✅ APPLIED | 07-22 | Format | 318W | Applied by Fix Agent 2026-07-25 |
| ✅ APPLIED | 07-21 | Format | 318W | Applied by Fix Agent 2026-07-25 |
| ✅ APPLIED | 07-21 | Output | 5 (1E+2W+2I) | Applied by Fix Agent 2026-07-25 |
| ✅ APPLIED | 07-21 | Hygiene | 1W | Applied by Fix Agent 2026-07-25 |
| ✅ APPLIED | 07-22 | Hygiene | 1W | Applied by Fix Agent 2026-07-25 |
| ✅ APPLIED | 07-23 | Output | 4 (1E+2W+1I) | Applied by Fix Agent 2026-07-25 |
| ✅ APPLIED | 07-23 | Hygiene | 1W | Applied by Fix Agent 2026-07-25 |
| ✅ APPLIED | 07-24 | Hygiene | 1W | Applied by Fix Agent 2026-07-25 |

---

## Pending Reports

### ✅ Format Validation — 2026-07-30
- **Report:** `wiki/reviews/2026-07-30_format-report.md`
- **Summary:** 411 WARNINGs (all broken wikilinks — forward-references), 0 ERRORs. +28 files vs 07-26 (867 total). 0 ERROR streak: 9 consecutive days. New batch (memory theory) introduces `.md` suffix in source wikilinks (~11 instances). Clean structural quality.
- **Actions needed:** None — all WARNINGs are content gaps. Recommend APPROVE.
- **Status:** approved

### ✅ Output Validation — 2026-07-30
- **Report:** `wiki/reviews/2026-07-30_output-report.md`
- **Summary:** 5+ issues: 1 ERROR (dropped-i typos lần 6 — 5 new files), 2 WARNING (1-sentence definitions: 493/495, <5 key points: 86), 3 systemic patterns (ngưởi recurrence, 1-sentence defs, draft ratio 66%).
- **Actions needed:** Fix Agent sửa dropped-i typos (5 files). Compile Agent cần update prompt cho Definition ≥2 câu, Key ideas ≥5.
- **Status:** approved

### 🔍 Format Validation — 2026-08-01

- **Report:** 
- **Summary:** 5 ERRORs + 433 WARNINGs. ⚠️ 0-ERROR streak BROKEN (was 9 days). 5 ERRORs are Pool A tags (tech, economic) used as sub_tags — Compile Agent regression. 3 WARNINGs for extra frontmatter fields (field, core_industry). New semiconductor batch with 9 concepts.
- **Actions needed:** Fix Agent sửa sub_tags (tech/economic → Pool B), remove extra fields. Compile Agent kiểm tra workflow.md.
- **Status:** pending

### 🔍 Output Validation — 2026-08-01

- **Report:** 
- **Summary:** 2 WARNING + systemic. Double-i typos có 5 instances MỚI từ batch semiconductor. Người spacing merge có 4 instances mới. Dropped-i tồn đọng từ 07-30 chưa được Fix Agent sửa. 502/504 concepts definition 1 câu.
- **Actions needed:** Fix Agent sửa double-i + spacing-merge mới + dropped-i tồn đọng.
- **Status:** pending

### 🔍 Hygiene Inspection — 2026-08-01

- **Report:** 
- **Summary:** 4 ERRORs + 1 WARNING.  QUAY LẠI (lần 8) sau 3 run sạch — chứa memory/2026-07-31.md.  vẫn chưa được resolve từ 07-30 re-run. 3 ERRORs cho raw/tools/.
- **Actions needed:** Julius quyết định raw/tools/. Move memory/ → .openclaw/memory/. Trace root cause.
- **Status:** pending

---

### 🔍 Hygiene Inspection — 2026-07-30 (23:30 re-run)

- **Report:** `wiki/reviews/2026-07-30_hygiene-report.md`
- **Summary:** 3 ERRORs — `raw/tools/` is an unlisted raw subfolder with 3 files (tools.md index + 2 content files). Naming is correct; the folder just isn't in folder-structure.md v1.2 whitelist (which lists only 6 raw subfolders). Previous ERROR (`state/` root folder) has been resolved — absent from this scan.
- **Delta from earlier 07-30 run:** `state/` ✅ resolved. `raw/tools/` 🔍 newly surfaced (was hidden by permissive scan script template that included `tools` in `RAW_SUBFOLDERS`).
- **Type:** [SPEC CONFLICT] — folder exists with valid compiled content but whitelist was never updated.
- **Actions needed:** Julius decides: (A) update `folder-structure.md` §6 to add `tools/` as raw subfolder #7, or (B) move files to an existing approved subfolder.
- **Status:** pending

---

### ✅ Format Validation — 2026-07-26

- **Report:** `wiki/reviews/archive/2026-07/2026-07-26_format-report.md`
- **Summary:** 357 WARNINGs (353 forward-reference broken wikilinks + 4 false-positive original-field warnings), 0 ERRORs. +10 files vs 07-25 (839 total), +21 WARNINGs (336→357). Clean structural quality — no frontmatter, section, naming, or code block issues. 0 ERROR streak: 07-22 through 07-26.
- **Delta from 07-25 (approved):** +10 files, +21 issues. +6 concepts, +2 sources, +2 topics.
- **Actions taken:** None — all WARNINGs are forward-references (content gaps) or validator false positives. No fixes required.
- **Status:** ✅ APPLIED by Fix Agent 2026-07-30 (no fixes needed)

---

### ✅ Output Validation — 2026-07-26 (23:14) — APPROVED

- **Report:** `wiki/reviews/2026-07-26_output-report.md`
- **Summary:** 5 issues (1 ERROR system-level + 2 WARNING + 1 INFO, plus a systemic forward-reference wikilinks issue covering 13 instances). Rerun after morning report (11:31) already applied. Net-new findings: forward-reference wikilinks in 6/6 concept files, code-switching in 2 concepts, short summary in 1 source.
- **Actions needed:** Julius sẽ tự sửa.
- **Status:** approved

---

### ✅ Hygiene Inspection — 2026-07-26 (23:30)

- **Report:** `wiki/reviews/archive/2026-07/2026-07-26_hygiene-report.md`
- **Summary:** ✅ Clean run. 0 issues across 51,997 paths. All validation dimensions pass (path whitelist, naming conventions, orphan detection). Prior recurring issues resolved: `memory/` root folder absent third consecutive run (07-24, 07-25, 07-26), `state/` root folder absent seventh consecutive run. +53 paths from yesterday — all compliant.
- **Actions taken:** None — clean run, no fixes required.
- **Status:** ✅ APPLIED by Fix Agent 2026-07-30 (no fixes needed)

---

## ✅ Approved — 2026-07-25 / 2026-07-26 (Julius)

### ✅ Format Validation — 2026-07-25

**Summary:** 336 WARNINGs (all broken wikilinks), 0 ERRORs. +1 file (829 total), -1 issue vs 07-24. The 07-24 ERROR (psychology.md Co-occurring tags) resolved by Fix Agent batch.

**Verdict:** APPROVED. All WARNINGs are forward-references — content gap, not structural errors. No format fixes required.

---

### ✅ Hygiene Inspection — 2026-07-25

**Summary:** 1 ERROR + 2 WARNINGs. ERROR is the recurring `memory/` root folder (7th flag — process-level fix needed: OpenClaw writes memory logs to `memory/` instead of `.openclaw/memory/`). 1 WARNING for orphan file inside `memory/`, 1 WARNING for draft naming (`src_` prefix in drafts).

**Verdict:** ✅ APPLIED by Fix Agent 2026-07-26.
- ✅ ERROR — Moved `memory/2026-07-26.md` to `.openclaw/memory/`, removed `memory/` folder
- ✅ WARNING — Renamed draft file to drop `src_` prefix

---

### ✅ Output Validation — 2026-07-26

**Summary:** 1 ERROR + 1 INFO. ERROR is dropped-i typos (variant 5) in 6/8 new files (~10 instances). INFO for "thay v" word fragment.

**Verdict:** ✅ APPLIED by Fix Agent 2026-07-26.
- ✅ Fixed dropped-i typos in 6 files (~10 instances): `thờ điểm` → `thờii điểm`, `ngườ dùng` → `ngườii dùng`, `thờ gian` → `thờii gian`, `thay v ` → `thay vì`

---

## Applied — 2026-07-25 (Fix Agent Batch)

### Summary
- **Format fixes:** Added `## Co-occurring tags` to wiki/tag/psychology.md
- **Typo fixes:** 100+ instances of double-i and dropped-i typos fixed across 24 files
- **Content fixes:** Title casing, key idea consolidation, key idea expansion

### Files Modified
- wiki/tag/psychology.md
- 11 files with double-i typo fixes
- 13 files with dropped-i typo fixes
- presence.md (title casing)
- second-order-thinking.md (consolidated key ideas)
- learned-helplessness.md (+1 key idea)
- learning-through-retrieval.md (+1 key idea)
- protoge-effect.md (+1 key idea)

### Full Details
See `.openclaw/MEMORY.md` entry: 2026-07-25 09:15 — Applied Fixes (Batch 07-21 to 07-24)

---

## Applied — 2026-07-26 (Fix Agent)

### Summary
- **Hygiene fixes:** Moved `memory/2026-07-26.md` to `.openclaw/memory/`, removed `memory/` folder, renamed draft file
- **Output fixes:** Fixed dropped-i typos (~10 instances) in 6 files

### Files Modified (Hygiene)
- Moved: `memory/2026-07-26.md` → `.openclaw/memory/2026-07-26.md`
- Removed: `memory/` folder (empty)
- Renamed: `wiki/drafts/src_is-there-anything-left-to-build-in-crypto-wintermute-backup-2026-07-20.md` → `is-there-anything-left-to-build-in-crypto-wintermute-backup-2026-07-20.md`

### Files Modified (Output)
- `wiki/sources/src_introducing-backsearch-gr-inc.md` — 2 typos fixed
- `wiki/sources/src_monid-ai-agent-tool-platform.md` — 1 typo fixed
- `wiki/concepts/agent-backtesting.md` — 1 typo fixed
- `wiki/concepts/frozen-corpus-search.md` — 1 typo fixed
- `wiki/concepts/pay-per-call-pricing.md` — 3 typos fixed
- `wiki/concepts/point-in-time-data.md` — 3 typos fixed

### Reports Archived
- `wiki/reviews/archive/2026-07/2026-07-25_hygiene-report.md`
- `wiki/reviews/archive/2026-07/2026-07-26_output-report.md`

---

## Applied — 2026-07-30 (Fix Agent)

### Summary
- **Format fixes:** None — 357 WARNINGs were all forward-reference broken wikilinks (content gaps) or validator false positives. No structural issues.
- **Hygiene fixes:** None — clean run (0 issues).

### Reports Archived
- `wiki/reviews/archive/2026-07/2026-07-26_format-report.md`
- `wiki/reviews/archive/2026-07/2026-07-26_hygiene-report.md`

---

## History

All reports from 07-21 through 07-24 have been applied. See archive at `wiki/reviews/archive/2026-07/` for original report files.

Previous reports (07-21 through 07-25) ✅ APPROVED by Julius and ✅ APPLIED by Fix Agent.

---

*System status: 4 reports pending — Format (08-01), Output (08-01), Hygiene (07-30, 08-01). All prior reports ✅ APPLIED.*
