# Format Validation — 2026-08-13

**Status:** pending
**Issues found:** 427
**Created:** 2026-08-13 23:15
**Validator:** format-validator
**Files checked:** 921 (524 concepts + 168 sources + 34 indexes + 195 topics)
**ERRORs**: 0
**WARNINGS**: 427
**INFOS:** 0
**Total issues**: 427
Files checked: 921
Total issues: 427

Δ from 2026-08-12 (applied): -50 issues (50 ERRORs cleared — tag file sections added by Fix Agent; 427 WARNINGs unchanged — same broken wikilink pool)

---

## Issue Summary

All 427 issues are **WARNING** severity — broken wikilinks (forward-references to concepts not yet compiled):

| Category | Count | Description |
|---|---|---|
| Individual broken wikilinks | 407 | Links to concepts/sources that don't exist yet |
| Forward-reference groups | 20 | Files with 4-9 broken links each, summarized as single entries |
| Unique broken targets | 276 | Distinct concept/source slugs referenced but not compiled |

**No ERRORs, no INFOS.** The 50 ERRORs from 2026-08-12 (missing `## Parent` and `## Files with this tag` sections in tag files, missing `## Notes` in tag.md, one long slug) were fully resolved by Fix Agent on 2026-08-13.

| Files checked | Concepts | Sources | Indexes | Topics |
|---|---|---|---|---|
| 921 | 524 | 168 | 34 | 195 |

---

## Top 20 Broken Targets

These are the most frequently referenced concepts/sources that don't exist yet:

| # | Target | Count |
|---|---|---|
| 1 | `[[game-theory]]` | 10 |
| 2 | `[[src_agent-memory-7-types-substack.md]]` | 8 |
| 3 | `[[confirmation-bias]]` | 8 |
| 4 | `[[src_you-just-hired-a-million-bad-employees-a16z.md]]` | 5 |
| 5 | `[[src_the-let-them-theory-gabriel-reality.md]]` | 5 |
| 6 | `[[ai-coding-agents]]` | 5 |
| 7 | `[[src_how-to-remember-everything-you-read-dan-koe.md]]` | 5 |
| 8 | `[[career-design]]` | 5 |
| 9 | `[[decision-making]]` | 5 |
| 10 | `[[deep-work]]` | 4 |
| 11 | `[[src_cuoc-ua-xem-ai-khong-i-lui-curiositypocket.md]]` | 4 |
| 12 | `[[src_introducing-backsearch-gr-inc.md]]` | 3 |
| 13 | `[[src_monid-ai-agent-tool-platform.md]]` | 3 |
| 14 | `[[attention-economy]]` | 3 |
| 15 | `[[ai-hype-vs-reality]]` | 3 |
| 16 | `[[economic-inequality]]` | 3 |
| 17 | `[[critical-thinking]]` | 3 |
| 18 | `[[naval-ravikant]]` | 3 |
| 19 | `[[risk-parity]]` | 3 |
| 20 | `[[second-law-of-thermodynamics]]` | 3 |

---

## Forward-Reference Groups (20 files, 117 links)

The following files reference 4+ concepts/sources that haven't been compiled. These are summarized as single entries rather than listed individually.

| File | Broken links |
|---|---|
| `wiki/sources/src_mental-models-of-art.md` | 9 |
| `wiki/sources/src_mental-models-of-economics.md` | 9 |
| `wiki/sources/src_thought-experiment.md` | 9 |
| `wiki/sources/src_fs-blog-mental-models.md` | 7 |
| `wiki/sources/src_code-as-agent-harness-arxiv-2605-18747.md` | 6 |
| `wiki/sources/src_farnam-street-mental-models-biology-series.md` | 6 |
| `wiki/sources/src_farnam-street-mental-models-systems-thinking.md` | 6 |
| `wiki/sources/src_incentives-hidden-forces.md` | 6 |
| `wiki/sources/src_probabilistic-thinking.md` | 6 |
| `wiki/concepts/third-order-thinking.md` | 6 |
| `wiki/concepts/thought-experiment.md` | 6 |
| `wiki/sources/src_11-minutes-hack-github.md` | 4 |
| `wiki/sources/src_ai-future-skills.md` | 4 |
| `wiki/sources/src_critical-thinking-dennett.md` | 4 |
| `wiki/sources/src_feedback-loops-mental-model.md` | 4 |
| `wiki/sources/src_global-macro-investing.md` | 4 |
| `wiki/sources/src_hermes-polymarket-btc-trading-agent.md` | 4 |
| `wiki/sources/src_the-cost-of-discretion.md` | 4 |
| `wiki/sources/src_the-seed-and-the-machine.md` | 4 |
| `wiki/sources/src_tribute-system-new-world-order.md` | 4 |

---

## Top 10 Files by Warning Count

| File | Count |
|---|---|
| `wiki/concepts/collaborative-thinking.md` | 5 |
| `wiki/concepts/probabilistic-thinking.md` | 5 |
| `wiki/concepts/feedback-loops.md` | 4 |
| `wiki/concepts/hanlons-razor.md` | 4 |
| `wiki/concepts/meaning-through-work.md` | 4 |
| `wiki/concepts/occams-broom.md` | 4 |
| `wiki/concepts/occams-razor.md` | 4 |
| `wiki/concepts/parametric-memory.md` | 4 |
| `wiki/concepts/pay-per-call-pricing.md` | 4 |
| `wiki/concepts/prospective-memory.md` | 4 |

---

## Verification

- [x] Script `validate.py` completed — 921 files scanned, 0 read errors
- [x] All 427 issues are WARNING-level broken wikilinks (forward-references)
- [x] No ERRORs, no INFOS, no frontmatter/structure/naming/code-fence issues
- [x] 50 ERRORs from 08-12 report confirmed resolved (tag sections added by Fix Agent)
- [x] 427 WARNINGs unchanged from 08-12 — same broken wikilink pool
- [x] No systemic format violations detected
- [x] Delta computed: -50 from 08-12 (ERRORs cleared), 0 net new issues

---

## Escalations

No escalations this run. All 427 WARNINGs are forward-references — concepts/sources linked but not yet compiled. These are expected in a growing KB and resolve naturally as Compile Agent processes more raw files.

**Note:** The broken-wikilink count has been stable at 427-430 WARNINGs for 7 consecutive days (08-07 through 08-13), indicating a steady state where new cross-links are added at roughly the same rate as concepts are compiled.