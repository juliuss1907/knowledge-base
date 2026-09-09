# Format Validation — 2026-09-09

**Status:** pending
**Issues found:** 398
**Created:** 2026-09-09 23:15:49
**Validator:** format-validator
**Files checked:** 1038 (571 concepts + 196 sources + 36 indexes + 235 topics)
**ERRORs**: 0
**WARNINGS**: 398
**INFOS:** 0
**Total issues**: 398
Files checked: 1038
Total issues: 398

Δ from 2026-09-08 23:36 run (pending — prior run): 0 net change on every axis — total 398→398, ERROR 0→0, WARNING 398→398, individual broken 379→379, forward-ref groups 19→19, unique targets 271→271, Top-20 identical. KB grew +2 files (`wiki/tag/layer2.md` + `wiki/tag/perpdex.md` — Index Agent tag regeneration at 21:05, vault backup commit `ce0f3214`; 0 concepts/sources compiled). Pipeline idle day 7 (09-03→09-09). New tag files contribute 0 broken wikilinks. Exact-zero-flat, pipeline-idle variant.

---

| Files checked | Concepts | Sources | Indexes | Topics |
|---|---|---|---|---|
| 1038 | 571 | 196 | 36 | 235 |

## Top Violations

### Broken Wikilinks — Top 20 Targets

| Rank | Target | Count |
|---|---|---|
| 1 | [[game-theory]] | 10 |
| 2 | [[confirmation-bias]] | 8 |
| 3 | [[deep-work]] | 5 |
| 3 | [[ai-coding-agents]] | 5 |
| 3 | [[career-design]] | 5 |
| 3 | [[decision-making]] | 5 |
| 7 | [[attention-economy]] | 3 |
| 7 | [[ai-assisted-development]] | 3 |
| 7 | [[ai-hype-vs-reality]] | 3 |
| 7 | [[economic-inequality]] | 3 |
| 7 | [[intellectual-humility]] | 3 |
| 7 | [[naval-ravikant]] | 3 |
| 7 | [[risk-parity]] | 3 |
| 7 | [[second-law-of-thermodynamics]] | 3 |
| 7 | [[homeostasis]] | 3 |
| 7 | [[saying-no]] | 3 |
| 7 | [[cognitive-dissonance]] | 3 |
| 7 | [[power-imbalance]] | 3 |
| 7 | [[stoicism]] | 3 |
| 7 | [[first-order-thinking]] | 3 |

### Top Files by Warning Count

| File | Warnings |
|---|---|
| wiki/concepts/probabilistic-thinking.md | 5 |
| wiki/concepts/collaborative-thinking.md | 4 |
| wiki/concepts/feedback-loops.md | 4 |
| wiki/concepts/hanlons-razor.md | 4 |
| wiki/concepts/meaning-through-work.md | 4 |
| wiki/concepts/systematic-trading.md | 4 |
| wiki/concepts/vibe-coding.md | 4 |
| wiki/concepts/activation-energy.md | 3 |
| wiki/concepts/ai-alignment.md | 3 |
| wiki/concepts/ai-dependency.md | 3 |

### Forward-Reference Groups (19)

| File | Broken Links |
|---|---|
| wiki/sources/src_mental-models-of-economics.md | 9 |
| wiki/sources/src_mental-models-of-art.md | 9 |
| wiki/sources/src_thought-experiment.md | 9 |
| wiki/sources/src_fs-blog-mental-models.md | 7 |
| wiki/concepts/third-order-thinking.md | 6 |
| wiki/concepts/thought-experiment.md | 6 |
| wiki/sources/src_code-as-agent-harness-arxiv-2605-18747.md | 6 |
| wiki/sources/src_farnam-street-mental-models-biology-series.md | 6 |
| wiki/sources/src_farnam-street-mental-models-systems-thinking.md | 6 |
| wiki/sources/src_incentives-hidden-forces.md | 6 |
| wiki/sources/src_probabilistic-thinking.md | 6 |
| wiki/sources/src_11-minutes-hack-github.md | 4 |
| wiki/sources/src_ai-future-skills.md | 4 |
| wiki/sources/src_feedback-loops-mental-model.md | 4 |
| wiki/sources/src_global-macro-investing.md | 4 |
| wiki/sources/src_hermes-polymarket-btc-trading-agent.md | 4 |
| wiki/sources/src_the-cost-of-discretion.md | 4 |
| wiki/sources/src_the-seed-and-the-machine.md | 4 |
| wiki/sources/src_tribute-system-new-world-order.md | 4 |

### Backlog Breakdown

| Category | Count | Notes |
|---|---|---|
| Individual broken wikilinks | 379 | Forward-references to uncompiled concepts |
| Forward-reference summary groups | 19 | Files with 4+ broken links grouped |
| Unique broken targets | 271 | Distinct concept slugs not yet in KB |
| Other warnings | 0 | No structural, naming, or YAML issues |

## Escalations

**Standing note (day 7):** Pipeline idle since 09-02. No concepts or sources compiled in 7 days. Backlog frozen at 398 WARNINGs — all forward-references to uncompiled concepts. Backlog will not drain until Compile Agent resumes processing raw files.

**No new escalations.** The 09-08 Hygiene escalation (migration marker + dangling HEARTBEAT + repos casing + backup files) carries forward unchanged.

## Verification

- [x] validate.py completed successfully (exit 0, 1038 files, 398 issues)
- [x] parse_issues.py extracted statistics (379 individual + 19 groups, 271 unique targets)
- [x] Top-20 broken targets identified and listed
- [x] Forward-reference groups enumerated (19 groups)
- [x] Delta computed against prior run (09-08 pending, 0 net change)
- [x] Report written to wiki/reviews/2026-09-09_format-report.md
