# Action Required — Pending Reports

> Consolidated list of pending Hermes validation reports
> Updated automatically after each validation run
> Julius reviews this file to approve/reject fixes

**Last updated:** 2026-05-27 00:05 — Format validation complete (20 issues)

---

## Summary

**Pending reports:** 2

**Status:**
- ✅ Output Validator — 2026-05-24: approved
- ✅ Format Validator — 2026-05-24: approved
- ✅ Hygiene Inspector — 2026-05-24: approved
- ✅ Output Validator — 2026-05-22: approved
- ✅ Format Validator — 2026-05-22: approved
- ✅ Hygiene Inspector — 2026-05-22: approved
- 🔴 Format Validator — 2026-05-26: pending
- 🔴 Output Validator — 2026-05-26: pending

**Resolved reports:**
- [x] Output Validator — 2026-05-14 (4 issues)
- [x] Format Validator — 2026-05-14 (3 issues)
- [x] Format Validator — 2026-05-17 (5 issues)
- [x] Hygiene Inspector — 2026-05-14 (14 issues)
- [x] Hygiene Inspector — 2026-05-17 (20 issues)
- [x] Hygiene Inspector — 2026-05-20 (6 issues)
- [x] Output Validator — 2026-05-21 (11 issues)
- [x] Format Validator — 2026-05-21 (20 issues)
- [x] Hygiene Inspector — 2026-05-21 (9 issues)
- [x] Hygiene Inspector — 2026-05-22 (3 ERROR + 2 issues)
- [x] Format Validator — 2026-05-22 (11 WARNING)
- [x] Output Validator — 2026-05-22 (16 issues)
- [x] Format Validator — 2026-05-24 (2 ERROR resolved + 3 WARNING)
- [x] Hygiene Inspector — 2026-05-24 (1 ERROR + 1 INFO)
- [x] Output Validator — 2026-05-24 (all 20 issues)

---

## Critical Issues (Fix Immediately)

- **Output 2026-05-26:** 2 ERROR — Definition too short (static-website-blind-spot, ai-augmented-systems-thinking) → expand to 2-3 sentences
- **Format 2026-05-26:** 17 ERROR — Systematic template deviation in 4 new files, 16 YAML quoting issues in L3 tag files
- **Output 2026-05-24:** 1 ERROR (11 broken wikilinks) → systematic, requires Compile Agent re-run
- **Output 2026-05-24:** Systematic issues → requires Compile Agent template fix

---

## Warnings (Can Fix Later)

- **Output 2026-05-26:** 4 WARNING — Summary too short (×2), section name mismatch (×2), empty sections + dangling references (×2)
- **Format 2026-05-26:** 3 WARNING — Stats mismatch in tag.md, field order in 4 new files
- Hygiene 2026-05-22: 1 WARNING — `.gitkeep` naming in `wiki/topic/`
- Hygiene 2026-05-22: 1 INFO — `raw/raw.md` spec gap

---

## Pending Reports

### 1. Format Validation — 2026-05-26

**File:** [2026-05-26_format-report.md](2026-05-26_format-report.md)
**Status:** pending
**Created:** 2026-05-27 00:05
**Issues:** 20 (17 ERROR, 3 WARNING, 0 INFO)
**Files affected:** 22 (2 sources + 2 concepts + 16 L3 tags + 1 L2 index + 1 L3 tag)

**Summary:**
- 17 critical format issues: systematic template deviation in 4 new files (2026-05-26 compilation), 16 YAML quoting issues in L3 tag files
- 3 warnings: tag.md stats mismatch, field order in new files
- **Systematic:** Compile Agent used wrong template — needs SKILL.md update

**Actions:**
- `approve format` — approve this report
- `reject format` — reject this report
- `show format` — show full report details

---

### 2. Output Validation — 2026-05-26

**File:** [2026-05-26_output-report.md](2026-05-26_output-report.md)
**Status:** pending
**Created:** 2026-05-26 22:00
**Issues:** 6 (2 ERROR, 4 WARNING, 0 INFO)
**Files affected:** 4 (2 sources + 2 concepts — all new)

**Summary:**
- 2 critical quality issues: definitions too short (1 sentence each)
- 4 improvements needed: summaries too short (×2), section name mismatch (×2), empty sections + dangling references (×2)

**Actions:**
- `approve output` — approve this report
- `reject output` — reject this report
- `show output` — show full report details

---

---

## Recently Applied

- [x] Hygiene Inspector — 2026-05-22: memory/ → .openclaw/memory/, RAW_BACKLOG.md deleted, wiki/reviews/HEARTBEAT.md removed
- [x] Format Validator — 2026-05-22: extra sections ×3, YAML syntax ×3, legacy fields ×2, field order ×2
- [x] Output Validator — 2026-05-22: Empty Original excerpts, Empty Notes systematic, Too many key points ×6, Broken wikilinks ×17

---

## Commands

**To approve a report:**
approve output
approve format
approve hygiene

**To view full report:**
show output
show format
show hygiene

**To apply approved fixes:**
openclaw fix apply