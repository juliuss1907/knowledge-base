# Approval Log

> Cross-machine approval contract giữa VPS (Connor validation) và máy chính (Fix Agent).
> Mỗi entry ghi lại scope chính xác Julius đã approve — Fix Agent chỉ apply đúng những gì trong file này.

---

## Entry: 2026-06-27 00:20 — Julius approves Format + Hygiene + Output

**Approved at:** 2026-06-27 00:20–00:21 +07
**Approved by:** Julius
**Scope:** Format Validator (23:15) + Hygiene Inspector (23:30) + Output Validator (23:01) — tất cả 3 báo cáo 2026-06-26

### ✅ Apply — Output Validator (0 ERROR, 2 WARNING, 1 INFO)

- Report: `wiki/reviews/2026-06-26_output-report.md`
- 3 new concepts (`experience-over-achievement`, `performative-existence`, `presence`) dùng Definition 1 câu + chỉ có 3 key ideas
- 1 phrasing issue: `src_map-is-not-territory.md` có artifact "các mô hình mental models"
- **Action for Fix Agent:** Mở rộng 3 concept mới, cleanup phrasing issue trong source

### ✅ Apply — Format Validator (4 ERROR, 310 WARNING)

- Report: `wiki/reviews/2026-06-26_format-report.md`
- Requested scope: `wiki/concepts/` + `wiki/sources/` (436 files)
- **ERROR (4):** YAML frontmatter parse failures trong batch `everything-is-a-win-when-the-goal` (4 files dùng hashtag-style tags thay vì YAML list format)
- **WARNING (310):** Broken wikilinks / forward references — backlog systemic, không cần Fix Agent xử lý từng cái
- **Delta:** Improved từ 322 → 314 (-8 issues). 8 code-block ERROR + 2 frontmatter warnings từ morning run đã resolved.
- **Action for Fix Agent:** Sửa 4 YAML parse failures trong `experience-over-achievement`, `performative-existence`, `presence`, `src_everything-is-a-win-when-the-goal`. Không cần chase 310 broken wikilink warnings.

### ✅ Apply — Hygiene Inspector (9 ERROR, 11 WARNING, 19 INFO)

- Report: `wiki/reviews/2026-06-26_hygiene-report.md`
- Full-tree scan: 920 paths checked
- **ERROR (9):** Root drift (`memory/`, `state/`), review-zone drift (`_approval-log.md`), naming violations trong `raw/papers/` (4 files), draft backup subfolders (2)
- **WARNING (11):** `.bak` temporary files trong `wiki/drafts/` (10 files), naming inconsistency
- **INFO (19):** Old review reports >30 ngày cần archive
- **Action for Fix Agent:** Cleanup root drift (xóa `memory/`, `state/` nếu empty), cleanup draft `.bak` files, sửa naming `raw/papers/`. Julius cần quyết định spec hay workflow sẽ đổi cho `_approval-log.md`.
- **Spec decision needed:** `wiki/reviews/_approval-log.md` — Julius cần chọn: whitelist vào `folder-structure.md` hoặc di chuyển artifact này ra khỏi `wiki/reviews/`.

---

## Entry: 2026-06-26 23:15 — Format Validator cron rerun

**Created at:** 2026-06-26 23:15:57 +07
**Created by:** Hermes-VPS (cron)
**Validator:** format-validator
**Scope:** Requested scope only — `wiki/concepts/*.md` + `wiki/sources/*.md` (436 files)

### Report
- `wiki/reviews/2026-06-26_format-report.md`
- Issues: 314 in requested scope (4 ERROR, 310 WARNING, 0 INFO)
- Raw script findings: 455 total, with 23 `wiki/tag/*.md` warnings and 118 `wiki/topic/*.md` errors excluded as out-of-scope for this run

### Key Findings
- 4 ERROR mới: YAML frontmatter parse failures trong `experience-over-achievement`, `performative-existence`, `presence`, và `src_everything-is-a-win-when-the-goal`
- 310 WARNING: broken wikilinks / forward references trong concepts và sources
- 8 code-block language-tag ERROR từ approved morning run đã biến mất
- 2 frontmatter warnings đơn lẻ từ approved morning run (`src_dan-koe-workflow-analysis-markus.md`, `src_map-is-not-territory.md`) đã biến mất

### Delta vs most recent approved format report
- Requested-scope total improved: 322 → 314 (-8)
- ERROR improved: 8 → 4 (-4)
- WARNING improved: 314 → 310 (-4)
- Positive: code-block issue class resolved entirely in requested scope
- Negative: new batch introduced 4 YAML parse regressions in frontmatter

### Escalations
- [SYSTEMATIC VIOLATION] 4/4 file trong batch `everything-is-a-win-when-the-goal` dùng hashtag-style tags trong YAML frontmatter, không theo `format-spec.md`
- Tag-frontmatter warnings và topic-file errors excluded again to match requested scope

### Status: PENDING approval

---

## Entry: 2026-06-26 07:12 — Julius approves all pending reports

**Approved at:** 2026-06-26
**Approved by:** Julius
**Scope:** All 4 pending validation reports — Output (2026-06-26), Format (2026-06-26 + 2026-06-25 rerun), Hygiene (2026-06-26)

### ✅ Apply — All issues from 4 reports

#### Output Validator — 2026-06-26 (4 issues)
- Report: `wiki/reviews/2026-06-26_output-report.md`
- 3 WARNING: 332 one-sentence definitions, 81 concepts with <5 key points, 9 empty `## Key ideas`
- 1 INFO: 164 concepts remain `status: draft`
- **All 4 issues approved for Fix Agent**

#### Format Validator — 2026-06-26 (322 in-scope issues)
- Report: `wiki/reviews/2026-06-26_format-report.md`
- 8 ERROR: code blocks missing language tags
- 312 WARNING: broken wikilinks / forward references
- 1 WARNING: field order mismatch in `src_dan-koe-workflow-analysis-markus.md`
- 1 WARNING: broken raw `original` reference in `src_map-is-not-territory.md`
- 23 tag-frontmatter warnings + 118 topic-file errors remain excluded from actionable count for this run
- **All 322 in-scope issues approved for Fix Agent**

#### Hygiene Inspector — 2026-06-26 (1 actionable issue)
- Report: `wiki/reviews/2026-06-26_hygiene-report.md`
- 1 ERROR: `wiki/reviews/HEARTBEAT.md` leaked into review zone
- `memory/` root finding remains excluded by scope
- **1 actionable issue approved for Fix Agent**

#### Format Validator — 2026-06-25 (23:15 rerun, 322 in-scope issues)
- Report: `wiki/reviews/2026-06-25_format-report.md`
- 8 ERROR: code blocks missing language tags
- 312 WARNING: broken wikilinks / forward references
- 1 WARNING: field order mismatch in `src_dan-koe-workflow-analysis-markus.md`
- 1 WARNING: broken raw `original` reference in `src_map-is-not-territory.md`
- 23 tag-frontmatter warnings + 118 topic-file errors remain excluded from actionable count for this run
- **All 322 in-scope issues approved for Fix Agent**

### ⏭️ Excluded

- **None** — all issues in all 4 reports approved without exclusions.

### ⚠️ Verify-first

- **None**

---

**Total scope:** 649 actionable issues across 4 reports → Fix Agent apply all.

---

## Entry: 2026-06-26 07:01 — Validation rerun

**Created at:** 2026-06-26 07:01
**Created by:** Connor (manual rerun)
**Scope:** Output + Format + Hygiene validators

### Reports
- `wiki/reviews/2026-06-26_output-report.md` — 4 issues (0 ERROR, 3 WARNING, 1 INFO)
- `wiki/reviews/2026-06-26_format-report.md` — 322 in-scope issues (8 ERROR, 314 WARNING, 0 INFO)
- `wiki/reviews/2026-06-26_hygiene-report.md` — 1 actionable issue (1 ERROR, 0 WARNING, 0 INFO)

### Key Findings
- Output: backlog-level content-depth issues unchanged — 332 one-sentence definitions, 81 concepts with <5 key points, 9 empty `## Key ideas`, 164 draft concepts
- Format: no requested-scope delta — 8 code-block language-tag errors, 312 broken wikilinks/forward references, 2 isolated frontmatter warnings
- Hygiene: `state/` và `.last-heartbeat` đã được resolve; chỉ còn `wiki/reviews/HEARTBEAT.md` là actionable hygiene error

### Delta vs last approved baseline
- Output: no change
- Format: no change in requested scope
- Hygiene: improved from 3 actionable issues to 1

### Escalations
- None beyond existing systemic backlog
- `memory/` root finding excluded again as Julius-side environment, not Kara cleanup scope

### Status: PENDING approval

---

## Entry: 2026-06-25 23:15 — Format Validator cron run

**Created at:** 2026-06-25 23:15
**Created by:** Hermes-VPS (cron)
**Validator:** format-validator
**Scope:** Requested scope only — `wiki/concepts/*.md` + `wiki/sources/*.md` (436 files)

### Report
- `wiki/reviews/2026-06-25_format-report.md`
- Issues: 322 in requested scope (8 ERROR, 314 WARNING, 0 INFO)
- Raw script findings: 463 total, with 23 `wiki/tag/*.md` warnings and 118 `wiki/topic/*.md` errors excluded as out-of-scope for this run

### Key Findings
- 8 ERROR: code blocks missing language tags (7 concepts + 1 source)
- 312 WARNING: broken wikilinks / forward references inside concepts and sources
- 1 WARNING: field order mismatch in `src_dan-koe-workflow-analysis-markus.md`
- 1 WARNING: broken `original` raw reference in `src_map-is-not-territory.md`

### Delta vs most recent approved format report
- No change in requested scope counts: 322 issues, 8 ERROR, 314 WARNING, 0 INFO
- No new categories introduced
- No previously approved requested-scope issues resolved in this rerun

### Escalations
- None for requested scope
- Note: validator script still scans `wiki/tag/*.md` and `wiki/topic/*.md`; those findings were excluded to match this cron instruction

### Status: PENDING approval

---

## Entry: 2026-06-25 16:03 — Julius approves all pending reports

**Approved at:** 2026-06-25
**Approved by:** Julius
**Scope:** All 3 pending validation reports — Output, Format, Hygiene (2026-06-25)

### ✅ Apply — All issues from 3 reports

#### Output Validator — 2026-06-25 (4 issues)
- Report: `wiki/reviews/2026-06-25_output-report.md`
- 3 WARNING + 1 INFO
- 332 concepts still have 1-sentence definitions
- 81 concepts have <5 key points
- 9 concepts have empty `## Key ideas`
- 164 concepts remain `status: draft`
- **All 4 issues approved for Fix Agent**

#### Format Validator — 2026-06-25 (345 in-scope issues)
- Report: `wiki/reviews/2026-06-25_format-report.md`
- 8 ERROR: code blocks missing language tags
- 312 WARNING: broken wikilinks / forward references
- 23 WARNING: tag files use unquoted `parent: [[tag]]` in YAML frontmatter
- 1 WARNING: field order mismatch in `src_dan-koe-workflow-analysis-markus.md`
- 1 WARNING: broken raw `original` reference in `src_map-is-not-territory.md`
- 118 topic-file frontmatter false positives excluded from actionable count
- **All 345 in-scope issues approved for Fix Agent**

#### Hygiene Inspector — 2026-06-25 (3 actionable issues)
- Report: `wiki/reviews/2026-06-25_hygiene-report.md`
- 1 ERROR: `state/` folder not in root whitelist
- 1 ERROR: `wiki/reviews/HEARTBEAT.md` leaked into review zone
- 1 WARNING: hidden root artifact `.last-heartbeat`
- 1 raw-script false positive excluded by scope: `memory/`
- **All 3 actionable issues approved for Fix Agent**

### ⏭️ Excluded

- **None** — all issues in all 3 reports approved without exclusions.

### ⚠️ Verify-first

- **None**

---

**Total scope:** 352 actionable issues across 3 reports → Fix Agent apply all.

---

## Entry: 2026-06-24 00:20 — Julius approves Format + Hygiene reports

**Approved at:** 2026-06-24
**Approved by:** Julius
**Scope:** Format Validator + Hygiene Inspector — 2026-06-23

### ✅ Apply — All 464 issues from 2 reports

#### Format Validator — 2026-06-23 (23:16, 463 issues)
- Report: `wiki/reviews/2026-06-23_format-report.md`
- ~108 ERROR: All topic files missing YAML frontmatter — systemic Index Agent issue (carry-over)
- 8 ERROR: Code blocks missing language tags (carry-over)
- ~10 ERROR: Additional frontmatter/markdown issues
- ~290 WARNING: Broken wikilinks (forward-references, expected in growing KB)
- 22 WARNING: Tag files unquoted `parent: [[tag]]` parsed as nested YAML list (SPEC CONFLICT)
- 1 WARNING: Field order mismatch
- 1 WARNING: Broken original wikilink in source frontmatter
- Delta: `main_tag: psychology` errors fully resolved (-11 ERROR); -8 ERROR, +18 WARNING overall
- **All 463 issues approved for Fix Agent**

#### Hygiene Inspector — 2026-06-23 (23:30, 1 issue)
- Report: `wiki/reviews/2026-06-23_hygiene-report.md`
- 1 ERROR: `state/` folder at root level — empty directory not in root whitelist
- Delta: `.last_heartbeat` WARNING resolved
- **1 issue approved for Fix Agent**

### ⏭️ Excluded

- **None** — all issues in both reports approved without exclusions.

### ⚠️ Verify-first

- **None**

---

**Total scope:** 464 issues across 2 reports → Fix Agent apply all.

---

## Entry: 2026-06-24 00:10 — Julius approves Output report

**Approved at:** 2026-06-24
**Approved by:** Julius
**Scope:** Output Validator — 2026-06-23 (23:10)

### ✅ Apply — All 5 issues

#### Output Validator — 2026-06-23 (23:10, 5 issues)
- Report: `wiki/reviews/2026-06-23_output-report.md`
- 1 systemic WARNING: "ngườii/đờii/lờii/rờii/thờii" typo — 52 instances across 13 new files (100% hit rate)
- 1 systemic WARNING: 17 broken wikilinks in new concepts (forward references, expected)
- 1 systemic WARNING: 1-sentence definitions across 10 new concepts (Compile Agent template, deprioritized by Julius 06-12)
- 2 INFO: Draft status on all 13 new files + 81 concepts with <5 key points (unchanged)
- **All 5 issues approved for Fix Agent**

### ⏭️ Excluded

- **None** — all issues approved without exclusions.

### ⚠️ Verify-first

- **None**

---

**Total scope:** 5 issues across 1 report → Fix Agent apply all.

---

## Entry: 2026-06-23 23:16 — Format Validator cron run

**Created at:** 2026-06-23 23:16
**Created by:** Hermes-VPS (cron)
**Validator:** format-validator
**Scope:** Full format validation — 587 files

### Report
- `wiki/reviews/2026-06-23_format-report.md`
- Issues: 463 (126 ERROR, 337 WARNING, 0 INFO)

### Key Findings
- ~108 ERROR: Topic files missing YAML frontmatter (unchanged, carry-over)
- 8 ERROR: Code blocks missing language tags (unchanged, carry-over)
- ~10 ERROR: Additional issues (truncated from stdout)
- ~290 WARNING: Broken wikilinks (forward-references)
- 22 WARNING: Unquoted `parent` YAML in tag files (SPEC CONFLICT)
- 1 WARNING: Field order mismatch
- 1 WARNING: Broken original wikilink

### Positive Delta
- ✅ `main_tag: psychology` errors (11 files) — **RESOLVED** (not present in this run)

### Escalations Carried Forward
- `[SYSTEMATIC VIOLATION]` Topic files without frontmatter — Index Agent needs update
- `[SPEC CONFLICT]` Unquoted wikilinks — index-spec.md vs format-spec.md

### Status: APPROVED (2026-06-24)

---

## Entry: 2026-06-23 00:10 — Julius approves evening update reports

**Approved at:** 2026-06-23
**Approved by:** Julius
**Scope:** 3 pending evening update reports — Output (06-22 22:00), Format (06-22 22:30), Hygiene (06-22 23:30)

### ✅ Apply — All issues from 3 reports

#### Output Validator — 2026-06-22 (22:00 Update, 5 issues)
- Report: `wiki/reviews/2026-06-22_output-report.md`
- 1 WARNING: "Ngưởi" typo — 1 file remaining (`src_tai-chinh-ca-nhan-9-ban-co-ang-thuc.md`)
- 1 WARNING: 7 broken wikilinks in new concepts (forward references, systemic)
- 3 INFO: 2 Vietnamese spacing typos + 1 missing Published date + draft status
- **All 5 issues approved for Fix Agent**

#### Format Validator — 2026-06-22 (22:30 Update, 453 issues)
- Report: `wiki/reviews/2026-06-22_format-report.md`
- ~108 ERROR: Topic files missing YAML frontmatter (systemic, unchanged from morning)
- 11 ERROR: `main_tag: psychology` — Pool B as main_tag (unchanged)
- 8 ERROR: Code blocks missing language tags (unchanged)
- 7 ERROR: Other frontmatter/markdown (minor delta)
- ~270 WARNING: Broken wikilinks (forward-references)
- 23 WARNING: Tag files unquoted `parent` YAML (SPEC CONFLICT)
- 2 WARNING: Field order mismatch + missing raw file
- Delta from morning: +2 ERROR, +1 WARNING
- **All 453 issues approved for Fix Agent**

#### Hygiene Inspector — 2026-06-22 (23:30, 1 issue)
- Report: `wiki/reviews/2026-06-22_hygiene-report.md`
- 1 WARNING: `.last_heartbeat` hidden file at root level
- **1 issue approved for Fix Agent**

### ⏭️ Excluded

- **None** — all issues in all 3 reports approved without exclusions.

### ⚠️ Verify-first

- **None**

---

**Total scope:** 459 issues across 3 evening update reports → Fix Agent apply all.

---

## Entry: 2026-06-22 14:30 — Julius approves all pending reports

**Approved at:** 2026-06-22
**Approved by:** Julius
**Scope:** All 6 pending validation reports — Output (06-19, 06-22), Format (06-19, 06-22), Hygiene (06-19, 06-22)

### ✅ Apply — All issues from 6 reports

#### Format Validator — 2026-06-22 (450 issues)
- Report: `wiki/reviews/2026-06-22_format-report.md`
- 109 ERROR: Topic files missing YAML frontmatter (systemic Index Agent)
- 11 ERROR: `main_tag: psychology` on 9 concepts + 2 sources
- 8 ERROR: Code blocks missing language tags
- 4 ERROR: `wiki/tag/tag.md` missing `parent` + `items_managed_by`
- 272 WARNING: Broken wikilinks (forward-references)
- 21 WARNING: Tag files unquoted `parent` YAML
- 2 WARNING: Field order mismatch
- 23 CRITICAL concepts with system/deep topics inside compiled_to
- **All 450 issues approved for Fix Agent**

#### Output Validator — 2026-06-22 (5 issues)
- Report: `wiki/reviews/2026-06-22_output-report.md`
- 1 systemic WARNING: 322 concepts with 1-sentence definitions
- 1 WARNING: 82 concepts with <5 key points
- 1 WARNING: "ngưởi" typo in 10 files
- 2 INFO: 154 draft concepts, mixed EN/VN language
- **All 5 issues approved for Fix Agent**

#### Hygiene Inspector — 2026-06-22 (4 issues)
- Report: `wiki/reviews/2026-06-22_hygiene-report.md`
- 4 WARNING: Archived -v2 duplicate reports
- **All 4 issues approved for Fix Agent**

#### Format Validator — 2026-06-19 (380 issues)
- Report: `wiki/reviews/2026-06-19_format-report.md`
- 109 ERROR: Topic files missing YAML frontmatter (systemic)
- 8 ERROR: Code blocks missing language tags
- 4 ERROR: `wiki/tag/tag.md` missing fields
- 21 WARNING: Tag files unquoted `parent` YAML
- ~230 WARNING: Broken wikilinks
- 2 WARNING: Field order mismatches
- **All 380 issues approved for Fix Agent**

#### Output Validator — 2026-06-19 (5 issues)
- Report: `wiki/reviews/2026-06-19_output-report.md`
- 1 systemic WARNING: 7 concepts with 1-sentence definitions
- 1 WARNING: `four-stages-market-cycle.md` only 4 key points
- 1 WARNING: "ngưởi" typo in 10 files
- 2 INFO: draft status, mixed EN/VN
- **All 5 issues approved for Fix Agent**

#### Hygiene Inspector — 2026-06-19 (4 issues)
- Report: `wiki/reviews/2026-06-19_hygiene-report.md`
- 4 WARNING: Archived -v2 duplicate reports
- **All 4 issues approved for Fix Agent**

### ⏭️ Excluded

- **None** — all issues in all 6 reports approved without exclusions.

### ⚠️ Verify-first

- **None**

---

**Total scope:** 848 issues across 6 reports → Fix Agent apply all.

---

## Entry: 2026-06-19 00:00 — Julius approves all pending reports

**Approved at:** 2026-06-19
**Approved by:** Julius
**Scope:** All 6 pending validation reports — Output (06-17, 06-18), Format (06-17, 06-18), Hygiene (06-17, 06-18)

### ✅ Apply — All issues from 6 reports

#### Output Validator — 2026-06-17 (6 issues)
- Report: `wiki/reviews/2026-06-17_output-report.md`
- 3 WARNING (systemic): Vietnamese "ngưởi" typo in 9 files, all 14 concepts status:draft, 25+ broken wikilinks
- 3 INFO: 2 files with 11 key points, 2 files missing Published date
- **All 6 issues approved for Fix Agent**

#### Output Validator — 2026-06-18 (4 issues)
- Report: `wiki/reviews/2026-06-18_output-report.md`
- 1 ERROR: `wiki/concepts/infrastructure-capex-cycle.md` truncated — missing Related concepts + Sources
- 2 WARNING: 2 concepts with 1-sentence definitions
- 1 INFO: 1 concept with 2-sentence definition
- **All 4 issues approved for Fix Agent**

#### Format Validator — 2026-06-17 (365 issues)
- Report: `wiki/reviews/2026-06-17_format-report.md`
- 11 ERROR: Code blocks missing lang tags (7 concepts + 1 source)
- 2 ERROR: `wiki/tag/tag.md` wrong level/scope (level=1, should be level=2)
- 20+ WARNING: Tag files use unquoted `parent: [[tag]]` — should be `parent: "[[tag]]"`
- 3 WARNING: Broken wikilinks in frontmatter `sources`/`original` fields
- 320 WARNING: Broken wikilinks in body (forward-references to uncompiled concepts)
- **All 365 issues approved for Fix Agent** (including all broken wikilinks — full scope, no exclusions this pass)

#### Format Validator — 2026-06-18 (17 issues)
- Report: `wiki/reviews/2026-06-18_format-report.md`
- 4 ERROR: `crypto` used as sub_tag (3 concepts + 1 source)
- 2 ERROR: `wiki/concepts/infrastructure-capex-cycle.md` missing 2 required sections
- 5 ERROR: `wiki/tag/tag.md` wrong level/scope + auto_generated + missing sections
- 6 WARNING: 6 raw sub-indexes unquoted `parent: [[raw]]`
- **All 17 issues approved for Fix Agent**

#### Hygiene Inspector — 2026-06-17 (7 issues)
- Report: `wiki/reviews/2026-06-17_hygiene-report.md`
- 1 ERROR: `RAW_BACKLOG.md` root whitelist violation
- 1 ERROR: `wiki/reviews/HEARTBEAT.md` heartbeat artifact
- 5 WARNING: 4 × `-v2` duplicate reports + `spot-check-report` in archive
- **All 7 issues approved for Fix Agent**

#### Hygiene Inspector — 2026-06-18 (7 issues)
- Report: `wiki/reviews/2026-06-18_hygiene-report.md`
- 3 ERROR: regressions + new violations
- 4 WARNING
- **All 7 issues approved for Fix Agent**

### ⏭️ Excluded

- **None** — all issues in all 6 reports approved without exclusions.

### ⚠️ Verify-first

- **None**

---

**Total scope:** 406 issues across 6 reports → Fix Agent apply all.
