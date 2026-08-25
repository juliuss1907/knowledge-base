# Format Validation — 2026-08-24

**Status:** approved
**Approved by:** Julius
**Issues found:** 391
**Created:** 2026-08-24 23:16
**Validator:** format-validator
**Files checked:** 944 (529 concepts + 179 sources + 34 indexes + 202 topics)
**ERRORs**: 0
**WARNINGS**: 391
**INFOS:** 0
**Total issues**: 391
Files checked: 944
Total issues: 391

Δ from 2026-08-23 (approved): **0 net change** (391→391), **0 ERRORs** (flat at 0 — clean streak holds, eighth consecutive day), **391 WARNINGs (flat)**, **+3 files** (941→944: +2 concepts, +1 source, 0 merges/deletes), **269 unique broken targets (flat, third consecutive day)**, **Top-20 list identical to 08-23 with identical counts**. New writing-craft cluster (read-widely-write-well, reading-brain-vs-digital-brain, src_the-golden-rule-for-becoming-a-better-writer) contributes zero broken wikilinks — all internal churn nets to exactly zero. Debt stable ~390 for 15 consecutive runs — KB grows, backlog does not.

---

## Issue Summary

All 391 issues are **WARNING** severity — broken wikilinks (forward-references to uncompiled concepts):

| Category | Count | Description |
|---|---|---|
| Individual broken wikilinks | 371 | Links to concepts/sources that don't exist yet |
| Forward-reference groups | 20 | Files with 4-6 broken links each, summarized as single entries |
| Unique broken targets | 269 | Distinct concept/source slugs referenced but not compiled |

**No ERRORs, no INFOS.** Frontmatter, sections, naming, markdown syntax all compliant across 944 files.

| Files checked | Concepts | Sources | Indexes | Topics |
|---|---|---|---|---|
| 944 | 529 | 179 | 34 | 202 |

---

## Delta Analysis — KB grew +3, debt exactly flat

Net file delta via git (`--diff-filter=A/D` since 2026-08-23 23:15): 3 added, 0 deleted, 0 merges:

- **Added:** concepts `read-widely-write-well`, `reading-brain-vs-digital-brain`; source `src_the-golden-rule-for-becoming-a-better-writer`.
- **Flat composition:** total issues, ERROR/WARNING split, unique broken targets (269), and the full Top-20 list (same slugs, same counts, same order) are all identical to 08-23. This is the second exact-composition-match day in a row.
- **New files:** zero new broken wikilinks introduced; zero new warnings attributed to the writing-craft cluster. Note: no new topic files for this batch yet (topics flat at 202) — Index Agent may not have processed them at scan time; not a format violation.
- **Reading:** legitimate flat outcome in a growing KB — new files are clean, backlog movement was purely internal and netted to zero. Do not read trend into ±0.

---

## Top 20 Broken Targets

These are the most frequently referenced concepts/sources that don't exist yet:

| # | Target | Count |
|---|---|---|
| 1 | `[[game-theory]]` | 10 |
| 2 | `[[confirmation-bias]]` | 8 |
| 3 | `[[ai-coding-agents]]` | 5 |
| 4 | `[[career-design]]` | 5 |
| 5 | `[[decision-making]]` | 5 |
| 6 | `[[deep-work]]` | 4 |
| 7 | `[[attention-economy]]` | 3 |
| 8 | `[[ai-hype-vs-reality]]` | 3 |
| 9 | `[[economic-inequality]]` | 3 |
| 10 | `[[critical-thinking]]` | 3 |
| 11 | `[[naval-ravikant]]` | 3 |
| 12 | `[[risk-parity]]` | 3 |
| 13 | `[[second-law-of-thermodynamics]]` | 3 |
| 14 | `[[homeostasis]]` | 3 |
| 15 | `[[saying-no]]` | 3 |
| 16 | `[[cognitive-dissonance]]` | 3 |
| 17 | `[[power-imbalance]]` | 3 |
| 18 | `[[stoicism]]` | 3 |
| 19 | `[[first-order-thinking]]` | 3 |
| 20 | `[[breaking-point]]` | 2 |

---

## Q: Are these WARNINGs actionable?

No. All 391 WARNINGs are forward-references — links to slugs Compile Agent has not compiled yet. They resolve naturally as raw backlog is processed. No Fix Agent action required.

**No structural or format violations detected.**

---

## Escalations

None. Zero ERRORs for the eighth consecutive run; no systematic violations; no spec conflicts detected this run.

---

## Verification

- [x] Loaded ground truth: `wiki/meta/format-spec.md` + `wiki/meta/index-spec.md` rules cached in validator script
- [x] Scanned all markdown: `wiki/sources/`, `wiki/concepts/`, `wiki/tag/`, `wiki/topic/`, `raw/`, `context/` (944 content files)
- [x] Dispatched by `type` field (concept/source/index; topic files light validation; `context/USER.md` skipped)
- [x] Checked frontmatter fields/order/YAML, section structure/order, naming/slug rules, markdown/wikilinks
- [x] Wikilink resolution incl. `.md`-strip and raw-subdir glob fallback
- [x] Parsed results via `parse_issues.py`; reconciled file counts via git (`--diff-filter=A/D`) against approved 08-23 baseline
