# Format Validation — 2026-08-28

**Status:** approved
**Issues found:** 391
**Created:** 2026-08-28 23:15:58
**Validator:** format-validator
**Files checked:** 984 (548 concepts + 185 sources + 34 indexes + 217 topics)
**ERRORs**: 0
**WARNINGS**: 391
**INFOS:** 0
**Total issues**: 391
Files checked: 984
Total issues: 391

Δ from 2026-08-27 23:15 run (applied 2026-08-28 12:16): **0 net change** (391→391), **0 ERRORs** (flat at 0 — clean streak day 12), **391 WARNINGs (flat)**, **0 files** (984→984 — no wiki files added; 2 raw articles ingested today 20:45/21:10 but not yet compiled, wiki layer unchanged), **268 unique broken targets (flat — day 4 at 268 after exiting the 269 plateau 08-22→08-25)**, **Top-20 list identical** (same slugs, same counts — game-theory 10, confirmation-bias 8, deep-work 5, etc.). Composition exact-zero-flat, not churned: individual broken wikilinks 372→372 (flat), forward-reference groups 19→19 (flat). 0 new files contributed **0 broken wikilinks** (Output Validator 23:10 confirmed 0 new source/concept files since the 08-27 run). Net: wiki layer static (raw grows +2, uncompiled), backlog frozen.

---

## Issue Summary

All 391 issues are **WARNING** severity — broken wikilinks (forward-references to uncompiled concepts):

| Category | Count | Description |
|---|---|---|
| Individual broken wikilinks | 372 | Links to concepts/sources that don't exist yet |
| Forward-reference groups | 19 | Files with 4-9 broken links each, summarized as single entries |
| Unique broken targets | 268 | Distinct concept/source slugs referenced but not compiled |

**No ERRORs, no INFOS.** Frontmatter, sections, naming, markdown syntax all compliant across 984 files.

| Files checked | Concepts | Sources | Indexes | Topics |
|---|---|---|---|---|
| 984 | 548 | 185 | 34 | 217 |

---

## Top 20 Broken Targets

These are the most frequently referenced concepts/sources that don't exist yet:

| # | Target | Count |
|---|---|---|
| 1 | `[[game-theory]]` | 10 |
| 2 | `[[confirmation-bias]]` | 8 |
| 3 | `[[deep-work]]` | 5 |
| 4 | `[[ai-coding-agents]]` | 5 |
| 5 | `[[career-design]]` | 5 |
| 6 | `[[decision-making]]` | 5 |
| 7 | `[[attention-economy]]` | 3 |
| 8 | `[[ai-hype-vs-reality]]` | 3 |
| 9 | `[[economic-inequality]]` | 3 |
| 10 | `[[intellectual-humility]]` | 3 |
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

## Forward-Reference Groups (19)

Files carrying 4-9 forward-references each (summarized as single WARNING entries):

- wiki/concepts/third-order-thinking.md: 6
- wiki/concepts/thought-experiment.md: 6
- wiki/sources/src_11-minutes-hack-github.md: 4
- wiki/sources/src_ai-future-skills.md: 4
- wiki/sources/src_code-as-agent-harness-arxiv-2605-18747.md: 6
- wiki/sources/src_farnam-street-mental-models-biology-series.md: 6
- wiki/sources/src_farnam-street-mental-models-systems-thinking.md: 6
- wiki/sources/src_feedback-loops-mental-model.md: 4
- wiki/sources/src_fs-blog-mental-models.md: 7
- wiki/sources/src_global-macro-investing.md: 4
- wiki/sources/src_hermes-polymarket-btc-trading-agent.md: 4
- wiki/sources/src_incentives-hidden-forces.md: 6
- wiki/sources/src_mental-models-of-art.md: 9
- wiki/sources/src_mental-models-of-economics.md: 9
- wiki/sources/src_probabilistic-thinking.md: 6
- wiki/sources/src_the-cost-of-discretion.md: 4
- wiki/sources/src_the-seed-and-the-machine.md: 4
- wiki/sources/src_thought-experiment.md: 9
- wiki/sources/src_tribute-system-new-world-order.md: 4

---

## Escalations

None.

Standing note (one line, not an escalation): 268 unique broken targets — flat day 4 at 268 after exiting the 269 plateau (08-22→08-25). Composition frozen: exact-zero-flat with identical Top-20, same individual/forward/Files-checked splits. This is the "no compilation happened" variant — Ingest added 2 raw articles today (20:45/21:10) but Compile Agent hasn't produced wiki files from them yet, so the validated layer is byte-identical and the backlog neither drains nor accumulates. Compile Agent's next target priority: `[[game-theory]]` (10 refs) and `[[deep-work]]` (5 refs, most cited uncompiled concept).

---

## Verification

Checklist of steps taken this run:

- [x] validate.py run from KB root (exit 0) — 984 files scanned in one pass
- [x] parse_issues.py statistics extracted (391W, 0E, 0I, 268 unique targets)
- [x] Git reconciliation vs 2026-08-27 23:15 baseline: +0 wiki files added (2 raw articles ingested 20:45/21:10, not compiled), 0 concepts/sources, 0 deleted, 0 merges
- [x] New-file link check: no new wiki files → 0 new broken wikilinks
- [x] Top-20 comparison vs 2026-08-27 23:15 report: identical — same slugs, same counts. Exact-zero-flat.
- [x] Previous report Status header checked: 08-27 23:15 format report shows `applied` → already reflected as ✅ APPLIED in _action-required.md, no reconcile needed
