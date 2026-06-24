# Approval Log

> Cross-machine approval contract giữa VPS (Connor validation) và máy chính (Fix Agent).
> Mỗi entry ghi lại scope chính xác Julius đã approve — Fix Agent chỉ apply đúng những gì trong file này.

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

### Status: PENDING approval

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
