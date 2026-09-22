# Format Validation — 2026-09-22

**Status:** pending
**Issues found:** 405
**Created:** 2026-09-22 23:15:12
**Validator:** format-validator
**Files checked:** 1103 (600 concepts + 210 sources + 34 indexes + 259 topics)
**ERRORs**: 1
**WARNINGS**: 404
**INFOS:** 0
**Total issues**: 405
Files checked: 1103
Total issues: 405

Δ from 2026-09-21 23:16 run (pending — prior run): **0 net change.** 1103 files identical. 405 issues identical (1E+404W). 273 unique broken targets flat. Top-20 targets identical slugs and counts. Zero wiki files added or removed since 09-21 (git log --diff-filter=A/D empty). Pipeline idle — no compilation today. Both axes: total flat (405→405), ERROR 1→1 (same slug carry-forward), WARNING 404→404, individual broken 385→385, forward-ref groups 19→19, unique targets 273→273.

---

| Files checked | Concepts | Sources | Indexes | Topics |
|---|---|---|---|---|
| 1103 | 600 | 210 | 34 | 259 |

---

## Issue 1: Slug exceeds 50 characters

**File:** wiki/sources/src_why-youve-lost-your-curiosity-and-how-to-get-it-back.md
**Severity:** ERROR
**Category:** Naming
**Issue:** Slug `why-youve-lost-your-curiosity-and-how-to-get-it-back` is 52 characters (limit 50)
**Current:** 52 characters
**Expected:** ≤ 50 characters per format-spec.md naming rules
**Suggested fix:** Rename slug to ≤50 chars, e.g. `why-youve-lost-curiosity-how-to-get-back`, and update all internal wikilinks.

**Note:** Carry-forward from 2026-09-21 — Fix Agent has not yet acted.

---

## Forward-Reference Groups (19)

| File | Broken refs |
|---|---|
| wiki/concepts/third-order-thinking.md | 6 |
| wiki/concepts/thought-experiment.md | 6 |
| wiki/sources/src_11-minutes-hack-github.md | 4 |
| wiki/sources/src_ai-future-skills.md | 4 |
| wiki/sources/src_code-as-agent-harness-arxiv-2605-18747.md | 6 |
| wiki/sources/src_farnam-street-mental-models-biology-series.md | 6 |
| wiki/sources/src_farnam-street-mental-models-systems-thinking.md | 6 |
| wiki/sources/src_feedback-loops-mental-model.md | 4 |
| wiki/sources/src_fs-blog-mental-models.md | 7 |
| wiki/sources/src_global-macro-investing.md | 4 |
| wiki/sources/src_hermes-polymarket-btc-trading-agent.md | 4 |
| wiki/sources/src_incentives-hidden-forces.md | 6 |
| wiki/sources/src_mental-models-of-art.md | 9 |
| wiki/sources/src_mental-models-of-economics.md | 9 |
| wiki/sources/src_probabilistic-thinking.md | 6 |
| wiki/sources/src_the-cost-of-discretion.md | 4 |
| wiki/sources/src_the-seed-and-the-machine.md | 4 |
| wiki/sources/src_thought-experiment.md | 9 |
| wiki/sources/src_tribute-system-new-world-order.md | 4 |

---

## Top 20 Broken Targets

| Target | Count |
|---|---|
| [[game-theory]] | 10 |
| [[confirmation-bias]] | 8 |
| [[deep-work]] | 5 |
| [[ai-coding-agents]] | 5 |
| [[career-design]] | 5 |
| [[decision-making]] | 5 |
| [[attention-economy]] | 3 |
| [[ai-assisted-development]] | 3 |
| [[ai-hype-vs-reality]] | 3 |
| [[economic-inequality]] | 3 |
| [[intellectual-humility]] | 3 |
| [[network-effects]] | 3 |
| [[goal-setting]] | 3 |
| [[naval-ravikant]] | 3 |
| [[risk-parity]] | 3 |
| [[second-law-of-thermodynamics]] | 3 |
| [[homeostasis]] | 3 |
| [[saying-no]] | 3 |
| [[cognitive-dissonance]] | 3 |
| [[power-imbalance]] | 3 |

Top-20 identical to 09-21 — same 20 targets, same counts, same order.

---

## Verification

- [x] validate.py run from KB root — 0 errors reading, 405 issues parsed
- [x] parse_issues.py — ERROR 1, WARNING 404, INFO 0; 385 individual + 19 groups = 404; 273 unique targets
- [x] Prior report (09-21) is pending — used as baseline (same file count = no fix applied)
- [x] Git reconciliation — 0 files added, 0 deleted since 09-21 run
- [x] ERROR is same slug as 09-21 — carry-forward (Fix Agent hasn't acted)
- [x] Top-20 identical to 09-21 — same slugs, same counts, same order

---

## Escalations

No new escalations. The single ERROR (slug >50 chars) is a carry-forward from 09-21 — Fix Agent action pending. Forward-reference backlog is static (pipeline idle, no compilation). Unique target plateau at 273 (flat since 09-17, when 09-16 approved). `[[game-theory]]` (10 refs) and `[[confirmation-bias]]` (8 refs) remain top uncompiled targets.
