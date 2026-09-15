# Format Validation — 2026-09-15

**Status:** pending
**Issues found:** 402
**Created:** 2026-09-15 23:16:21
**Validator:** format-validator
**Files checked:** 1060 (582 concepts + 200 sources + 34 indexes + 244 topics)
**ERRORs**: 0
**WARNINGS**: 402
**INFOS:** 0
**Total issues**: 402

Files checked: 1060
Total issues: 402

Δ from 2026-09-14 23:15 run (pending — prior run): 0 net change — total 402→402, ERROR 0→0, WARNING 402→402, individual broken 383→383 (flat), forward-ref groups 19→19 (flat), unique targets 272→272 (flat). Top-20 broken targets identical. No wiki files added or removed since 09-14 (git log --diff-filter=A/D returned empty). Pipeline idle — exact-zero-flat with zero wiki layer change. Unique target plateau holds at 272 for 2nd consecutive run (day 2 at 272).

---

| Files checked | Concepts | Sources | Indexes | Topics |
|---|---|---|---|---|
| 1060 | 582 | 200 | 34 | 244 |

## Issue 1: Forward-Reference Broken Wikilinks (WARNING)

**Severity:** WARNING
**Category:** Markdown
**Scope:** 272 unique broken targets across 106 concept files (383 individual + 19 group entries = 402 total)

Forward-references to concepts not yet compiled into wiki files. Compile Agent has not produced these files; no Fix Agent action needed. Pipeline backlog — resolve by compiling referenced concepts.

**Top 20 broken targets:**

| Target | References |
|---|---|
| `[[game-theory]]` | 10 |
| `[[confirmation-bias]]` | 8 |
| `[[deep-work]]` | 5 |
| `[[ai-coding-agents]]` | 5 |
| `[[career-design]]` | 5 |
| `[[decision-making]]` | 5 |
| `[[attention-economy]]` | 3 |
| `[[ai-assisted-development]]` | 3 |
| `[[ai-hype-vs-reality]]` | 3 |
| `[[economic-inequality]]` | 3 |
| `[[intellectual-humility]]` | 3 |
| `[[network-effects]]` | 3 |
| `[[goal-setting]]` | 3 |
| `[[naval-ravikant]]` | 3 |
| `[[risk-parity]]` | 3 |
| `[[second-law-of-thermodynamics]]` | 3 |
| `[[homeostasis]]` | 3 |
| `[[saying-no]]` | 3 |
| `[[cognitive-dissonance]]` | 3 |
| `[[power-imbalance]]` | 3 |

**Forward-reference groups (19):**

| File | Count |
|---|---|
| `wiki/concepts/third-order-thinking.md` | 6 |
| `wiki/concepts/thought-experiment.md` | 6 |
| `wiki/sources/src_11-minutes-hack-github.md` | 4 |
| `wiki/sources/src_ai-future-skills.md` | 4 |
| `wiki/sources/src_code-as-agent-harness-arxiv-2605-18747.md` | 6 |
| `wiki/sources/src_farnam-street-mental-models-biology-series.md` | 6 |
| `wiki/sources/src_farnam-street-mental-models-systems-thinking.md` | 6 |
| `wiki/sources/src_feedback-loops-mental-model.md` | 4 |
| `wiki/sources/src_fs-blog-mental-models.md` | 7 |
| `wiki/sources/src_global-macro-investing.md` | 4 |
| `wiki/sources/src_hermes-polymarket-btc-trading-agent.md` | 4 |
| `wiki/sources/src_incentives-hidden-forces.md` | 6 |
| `wiki/sources/src_mental-models-of-art.md` | 9 |
| `wiki/sources/src_mental-models-of-economics.md` | 9 |
| `wiki/sources/src_probabilistic-thinking.md` | 6 |
| `wiki/sources/src_the-cost-of-discretion.md` | 4 |
| `wiki/sources/src_the-seed-and-the-machine.md` | 4 |
| `wiki/sources/src_thought-experiment.md` | 9 |
| `wiki/sources/src_tribute-system-new-world-order.md` | 4 |

## Escalations

No structural violations detected. Forward-reference backlog is a pipeline artifact (uncompiled concepts), not a format error. Unique target count flat at 272 — no new targets resolved and no new targets introduced. Pipeline idle since 09-14 (zero wiki files added/removed). KB layer static.

## Verification

- [x] Ran validate.py from KB root
- [x] Full issue analysis via grep on /tmp/issues_full.txt
- [x] Read prior report (09-14) status: pending
- [x] Verified zero file delta via git log (empty --diff-filter=A/D)
- [x] Wrote report to wiki/reviews/2026-09-15_format-report.md
- [x] Updated _action-required.md with 🔍 PENDING row
- [x] Updated MEMORY.md with validation entry
- [x] Will run verify_integrity.py
- [x] Will run ad-hoc verification script
