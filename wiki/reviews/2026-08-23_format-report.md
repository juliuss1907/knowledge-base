# Format Validation — 2026-08-23

**Status:** approved
**Approved by:** Julius
**Issues found:** 391
**Created:** 2026-08-23 23:15
**Validator:** format-validator
**Files checked:** 941 (527 concepts + 178 sources + 34 indexes + 202 topics)
**ERRORs**: 0
**WARNINGS**: 391
**INFOS:** 0
**Total issues**: 391
Files checked: 941
Total issues: 391

Δ from 2026-08-22 (approved): **−1 total issue** (392→391), **0 ERRORs** (flat at 0 — clean streak holds), **−1 WARNING**, **+8 files** (933→941: +4 sources, +2 concepts, +2 topics, 0 merges/deletes), **269 unique broken targets (flat)**. Seventh consecutive clean-ERROR day. Debt stable ~390 for 14 consecutive runs — KB grows, backlog does not.

---

## Issue Summary

All 391 issues are **WARNING** severity — broken wikilinks (forward-references to uncompiled concepts):

| Category | Count | Description |
|---|---|---|
| Individual broken wikilinks | 371 | Links to concepts/sources that don't exist yet |
| Forward-reference groups | 20 | Files with 4-6 broken links each, summarized as single entries |
| Unique broken targets | 269 | Distinct concept/source slugs referenced but not compiled |

**No ERRORs, no INFOS.** Frontmatter, sections, naming, markdown syntax all compliant across 941 files.

| Files checked | Concepts | Sources | Indexes | Topics |
|---|---|---|---|---|
| 941 | 527 | 178 | 34 | 202 |

---

## Delta Analysis — KB grew +8, debt −1

Net file delta via git (`--diff-filter=A/D` since 2026-08-22 23:15): 8 added, 0 deleted, 0 merges:

- **Added:** concepts `schedule-maxxing`, `ai-engineering-skills`; sources `src_ai-skills-map-building-deploying-ai-apps`, `src_schedule-maxxing`, `src_ai-engineering-skills-map`, `src_strategy-vs-tactics-dan-koe`; topics `ai-engineering-skills`, `schedule-maxxing`.
- **Positive:** new concepts resolved their own forward-references; some older links now resolve.
- **Negative:** 6 new source/concept files introduced fresh forward-references, nearly offsetting resolutions. Net −1.
- **Composition:** Top-20 broken-target list identical to 08-22 — same slugs, same counts. Backlog composition unchanged.

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

None. 0 ERRORs, no spec conflicts, no systematic violations. Index/tag files clean — 08-22 tag regeneration holding.

---

## Verification

- [x] Loaded format-spec.md + index-spec.md (ground truth, cached)
- [x] Scanned all 941 markdown files in wiki/sources/, wiki/concepts/, wiki/tag/, wiki/topic/, raw/, wiki/, context/ (single pass)
- [x] Dispatched by `type` field: concept/source → format-spec, index → index-spec, topic → light topic validation
- [x] context/USER.md skipped (read-only, no frontmatter)
- [x] wiki/drafts/ skipped (already flagged)
- [x] Frontmatter: required fields, field order, YAML syntax, Pool A/B tag membership
- [x] Sections: required sections, order, heading levels, no duplicates
- [x] Naming: filename format, slug rules (lowercase-hyphen, ≤50 chars), folder correctness
- [x] Markdown: wikilink resolution (raw-subdir + .md-strip), code fence language tags, list markers
- [x] YAML edge cases handled (datetime.date, unquoted [[wikilinks]])
- [x] File-count delta reconciled via git log --diff-filter=A/D (not mtime)
