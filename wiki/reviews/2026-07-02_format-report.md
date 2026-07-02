# Format Validation — 2026-07-02

**Status:** pending
**Issues found:** 340 (6 ERROR, 334 WARNING, 0 INFO)
**Created:** 2026-07-02 23:15:11 +0700
**Validator:** format-validator
**Scope:** Full KB — 670 files (376 concepts + 121 sources + 33 indexes + 140 topics)

---

## Delta from last approved (2026-07-01 23:15)

| Metric | 2026-07-01 (APPROVED) | 2026-07-02 | Delta |
|---|---|---|---|
| Scope | 665 files | 670 files | **+5** |
| ERROR | 1 | 6 | **+5** |
| WARNING | 311 | 334 | **+23** |
| INFO | 0 | 0 | 0 |

**Positive delta (issues resolved):**
- ✅ **Topic files clean** — 140 topic files pass light validation, no regression (stable since 07-01 resolution)
- ✅ **Tag file sections resolved** — 69 tag-file section ERRORs from 06-29 remain resolved (confirmed stable through 3 consecutive runs)

**Negative delta (new/regression):**
- 🔴 **+5 new ERRORs on `wiki/tag/tag.md`**: scope mismatch, auto_generated flag, missing 3 required sections (## Overview, ## Sub-indexes, ## Notes). These were not flagged in 07-01 — possible validator scope expansion or file modification.
- 🔴 **Pre-approved exception**: `src_youre-being-trained-for-a-world-that-no-longer-exists.md` — slug 53 chars. Julius approved this exception on 2026-07-02.

**WARNING delta:**
- ⚠️ **+23 WARNING**: parent unquoted wikilinks in `wiki/tag/*.md` frontmatter — YAML parses `parent: [[tag]]` as nested list instead of string. This is a known cross-spec conflict (index-spec.md shows unquoted, format-spec.md §9 requires quoted). Previously filtered out as known pattern — now surfaced as warnings.
- ⚠️ **Broken wikilinks stable**: 290 individual + 21 forward-reference groups (same as 07-01). 194 unique targets unchanged.

**Files growth:** +5 files since 07-01 (+2 concepts, +1 source, +1 index, +1 topic)

---

## Summary

2 vấn đề mới cần chú ý:
1. **5 ERROR trên `wiki/tag/tag.md`** — file index gốc của toàn bộ tag system bị lệch format. Cần xác nhận đây là validator scope mở rộng (kiểm tra chặt hơn) hay file bị sửa sai format.
2. **23 WARNING unquoted wikilinks** — `wiki/tag/*.md` dùng `parent: [[tag]]` không quote. Đây là cross-spec conflict đã biết giữa index-spec.md và format-spec.md §9.

1 ERROR slug-too-long đã được Julius approved exception, không cần action.

Broken wikilinks — 290 forward references ổn định, không thay đổi từ 07-01.

---

## Issue 1: tag/tag.md — scope mismatch

**File:** `wiki/tag/tag.md`
**Severity:** ERROR
**Category:** Frontmatter
**Issue:** `scope` field should be `raw/wiki/context` (listing all covered zones), but got `tag`
**Current:** `scope: tag`
**Expected:** `scope: raw/wiki/context`
**Suggested fix:** Update `scope` to cover all zones OR clarify if index-spec.md §4 allows narrower scope for level-2 index files

---

## Issue 2: tag/tag.md — auto_generated flag

**File:** `wiki/tag/tag.md`
**Severity:** ERROR
**Category:** Frontmatter
**Issue:** `auto_generated` should be `false` for manually maintained index, but got `true`
**Current:** `auto_generated: true`
**Expected:** `auto_generated: false`
**Suggested fix:** Change `auto_generated` to `false`. This file is maintained by Index Agent but its structure (Stats, Items sections) is hand-curated per index-spec.md §4.

---

## Issue 3: tag/tag.md — Missing required sections

**File:** `wiki/tag/tag.md`
**Severity:** ERROR (×3)
**Category:** Sections
**Issue:** Missing 3 required sections for level-2 index files per index-spec.md §4
**Missing sections:**
- `## Overview` — description of what this index covers
- `## Sub-indexes` — list of sub-index pages (all `wiki/tag/<tag>.md` files)
- `## Notes` — curator annotations
**Suggested fix:** Add the three missing sections per index-spec.md §4. If these were previously present and got removed, escalate to Index Agent regression.

---

## Issue 4: Slug exceeds 50-character limit (PRE-APPROVED EXCEPTION)

**File:** `wiki/sources/src_youre-being-trained-for-a-world-that-no-longer-exists.md`
**Severity:** ~~ERROR~~ → **APPROVED EXCEPTION**
**Category:** Naming
**Issue:** Source file slug is 53 characters, exceeding the 50-character limit
**Current:** `src_youre-being-trained-for-a-world-that-no-longer-exists` (53 chars)
**Expected:** Slug ≤ 50 characters
**Status:** Julius approved exception on 2026-07-02 — no action needed. Carried over from 07-01 report.

---

## Issue 5: Systematic — Unquoted wikilinks in tag file frontmatter

**Files:** 23 files in `wiki/tag/*.md`
**Severity:** WARNING
**Category:** Frontmatter
**Issue:** `parent: [[tag]]` without quotes. YAML parser interprets the leading `[` as a flow sequence start, producing `{'parent': [['tag']]}` (nested list) instead of the string `'[[tag]]'`.

**Files affected:**
`wiki/tag/ai.md`, `wiki/tag/automation.md`, `wiki/tag/coding.md`, `wiki/tag/crypto.md`, `wiki/tag/defi.md`, `wiki/tag/economic.md`, `wiki/tag/geopolitics.md`, `wiki/tag/hack.md`, `wiki/tag/health.md`, `wiki/tag/investment.md`, `wiki/tag/law.md`, `wiki/tag/layer1.md`, `wiki/tag/news.md`, `wiki/tag/opinion.md`, `wiki/tag/politic.md`, `wiki/tag/productivity.md`, `wiki/tag/psychology.md`, `wiki/tag/research.md`, `wiki/tag/system.md`, `wiki/tag/tech.md`, `wiki/tag/tools.md`, `wiki/tag/tutorial.md`, `wiki/tag/vibecode.md`

**Current:** `parent: [[ai]]` (unquoted in YAML frontmatter)
**Expected:** `parent: "[[ai]]"` (quoted, per format-spec.md §9)
**Suggested fix:** Update index-spec.md to show quoted format, then Fix Agent wraps all 23 `parent` values in quotes.

**[SPEC CONFLICT]**: `index-spec.md` shows unquoted `parent: [[tag]]` but `format-spec.md` §9 note requires quoted wikilinks in frontmatter (`"[[...]]"`). One spec needs to yield. Recommend updating index-spec.md.

---

## Issue 6: Broken wikilinks — Stable backlog (290 individual + 21 groups)

**Severity:** WARNING (311 total, stable from 07-01)
**Category:** Markdown
**Issue:** 290 individual broken wikilinks + 21 forward-reference summary groups across concepts and sources. These are forward-references to concepts not yet compiled — expected in a growing KB.

**Top 10 broken targets:**
| Target | Occurrences |
|---|---|
| `[[game-theory]]` | 10 |
| `[[confirmation-bias]]` | 8 |
| `[[pareto-principle]]` | 6 |
| `[[ai-coding-agents]]` | 5 |
| `[[career-design]]` | 5 |
| `[[decision-making]]` | 5 |
| `[[deep-work]]` | 4 |
| `[[ai-hype-vs-reality]]` | 3 |
| `[[economic-inequality]]` | 3 |
| `[[critical-thinking]]` | 3 |

**194 unique broken targets total** — unchanged from 07-01 and 06-30.

**Top 5 files by warning count:**
| File | Warnings |
|---|---|
| `wiki/concepts/collaborative-thinking.md` | 5 |
| `wiki/concepts/probabilistic-thinking.md` | 5 |
| `wiki/concepts/feedback-loops.md` | 4 |
| `wiki/concepts/hanlons-razor.md` | 4 |
| `wiki/concepts/meaning-through-work.md` | 4 |

These will auto-resolve when target concepts are compiled. No action needed.

---

## KB Format Health

| Metric | Value |
|---|---|
| Files checked | 670 |
| ERROR rate | 0.90% (6/670) — 5 on 1 index file + 1 pre-approved |
| ERROR rate (excluding pre-approved) | 0.75% (5/670) |
| WARNING rate | 49.9% (334/670) — nearly all are forward-reference broken wikilinks |
| Actual structural issues | 28 (5 ERRORs + 23 unquoted wikilink WARNINGs) |
| KB format health score | **99.1%** (excl. forward-ref broken wikilinks) |

---

## Escalation

### [SPEC CONFLICT] Unquoted wikilinks in YAML frontmatter

```
Issue: index-spec.md shows `parent: [[tag]]` without quotes
format-spec.md §9 requires quoted wikilinks in frontmatter: `"[[tag]]"`
Impact: 23 tag files flagged as WARNING
Recommendation: Update index-spec.md examples to show quoted format,
then Fix Agent wraps all parent values in quotes.
```

---

**Report complete.** Review at `wiki/reviews/_action-required.md`
**Commands:** `approve format` hoặc `show format`
