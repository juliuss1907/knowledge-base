# Format Validation — 2026-08-17

**Status:** approved
**Approved by:** Julius
**Issues found:** 393
**Created:** 2026-08-17 23:16
**Validator:** format-validator
**Files checked:** 923 (525 concepts + 169 sources + 34 indexes + 195 topics)
**ERRORs**: 0
**WARNINGS**: 393
**INFOS:** 0
**Total issues**: 393
Files checked: 923
Total issues: 393

Δ from 2026-08-16 (approved): **0 net change** — identical totals across every axis (393 total issues, 393 WARNING, 0 ERROR, 923 files, 525 concepts, 169 sources, 270 unique broken targets). No KB growth since yesterday (same file counts), so no new forward-references were added. No regressions, no new structural/format violations. Fifth consecutive clean ERROR run.

---

## Issue Summary

All 393 issues are **WARNING** severity — broken wikilinks (forward-references to uncompiled concepts):

| Category | Count | Description |
|---|---|---|
| Individual broken wikilinks | 373 | Links to concepts/sources that don't exist yet |
| Forward-reference groups | 20 | Files with 4-9 broken links each, summarized as single entries |
| Unique broken targets | 270 | Distinct concept/source slugs referenced but not compiled |

**No ERRORs, no INFOS.** Fifth consecutive clean ERROR run (08-13 through 08-17; the 50 ERRORs from 08-11/08-12 were resolved by Fix Agent on 08-13 and have stayed resolved).

| Files checked | Concepts | Sources | Indexes | Topics |
|---|---|---|---|---|
| 923 | 525 | 169 | 34 | 195 |

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

All 20 top targets are identical to the 08-16 run — no shift in the forward-reference backlog composition.

---

## Q: Are these WARNINGs actionable?

No. All 393 WARNINGs are forward-references — wikilinks pointing at concept slugs that Compile Agent has not yet compiled. They resolve naturally as more raw files are processed. This is expected debt in a growing KB and does not require Fix Agent action.

**No structural or format violations were detected.**

---

## Escalations

No escalations. No [FORMAT UNCERTAINTY], no [SPEC CONFLICT], no [SYSTEMATIC VIOLATION].

Recent-run context: the 08-15 `.md`-strip validator fix remains stable — no `.md.md`-style false positives have resurfaced, and today's flat count (identical to 08-16) confirms the methodology is consistent.

---

## Verification

This report was produced by the format-validator pipeline:

1. **Spec load** — read `wiki/meta/format-spec.md` (ground truth for concept/source files) and `wiki/meta/index-spec.md` (for index/topic files). Both present.
2. **Full scan** — ran `scripts/validate.py` from KB root; parsed all 923 markdown files (525 concepts + 169 sources + 34 indexes + 195 topics).
3. **Dispatch** — routed by `type`/`scope`/`level` fields with path-derived tier cross-checking. 0 files skipped for type errors, 0 files failed to parse.
4. **Issue parse** — `scripts/parse_issues.py` confirmed 393 total issues: 0 ERROR, 393 WARNING, 0 INFO.
5. **Delta** — compared against the most recent APPROVED report (08-16): 0 net change.
6. **Report written** — this file, `wiki/reviews/2026-08-17_format-report.md`.
7. **Cross-file integrity** — will be confirmed via `verify_integrity.py`.

No wiki content files were modified.