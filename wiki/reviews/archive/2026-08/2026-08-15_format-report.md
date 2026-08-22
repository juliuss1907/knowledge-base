# Format Validation — 2026-08-15

**Status:** applied
**Approved by:** Julius
**Approved date:** 2026-08-16
**Issues found:** 391
**Created:** 2026-08-15 23:15
**Applied:** 2026-08-22 14:40 by fix-agent (OpenClaw)
**Validator:** format-validator
**Files checked:** 921 (524 concepts + 168 sources + 34 indexes + 195 topics)
**ERRORs**: 0
**WARNINGS**: 391
**INFOS:** 0
**Total issues**: 391
Files checked: 921
Total issues: 391

Δ from 2026-08-14 (approved): −36 total issues (427→391), but **all 36 removed are validator corrections, not Fix Agent fixes** — the `.md.md` double-extension false positive (described below) was removed from the validator, eliminating 36 spurious warnings (8 unique `src_*.md` targets). **Net genuine change: 0** — the genuine broken-wikilink pool is unchanged (391 WARNINGs, 268 unique broken targets in both runs).

---

## Issue Summary

All 391 issues are **WARNING** severity — broken wikilinks (forward-references to concepts not yet compiled):

| Category | Count | Description |
|---|---|---|
| Individual broken wikilinks | 371 | Links to concepts/sources that don't exist yet |
| Forward-reference groups | 20 | Files with 4-9 broken links each, summarized as single entries |
| Unique broken targets | 268 | Distinct concept/source slugs referenced but not compiled |

**No ERRORs, no INFOS.** Third consecutive clean ERROR run (08-13, 08-14, 08-15; the 50 ERRORs from 08-11/08-12 were resolved by Fix Agent on 08-13 and have stayed resolved).

**Validator fix applied this run:** `scripts/validate.py` was patched to strip the `.md` extension from wikilink targets before existence checks in both the concept-body and source-body broken-wikilink blocks. The `original` field check already stripped `.md`, but the two body checks did not — so `[[src_foo.md]]` was probed as `src_foo.md.md` and falsely flagged. This removed 36 false positives across 8 targets (`src_agent-memory-7-types-substack.md`, `src_you-just-hired-a-million-bad-employees-a16z.md`, etc.). No wiki content files were modified (validator is read-only).

| Files checked | Concepts | Sources | Indexes | Topics |
|---|---|---|---|---|
| 921 | 524 | 168 | 34 | 195 |

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

> **Note:** Unlike prior reports, no `src_*.md` targets appear in the top-20. Those 8 targets were validator false positives (the `.md.md` bug), now correctly resolved.

---

## Forward-Reference Groups (20 files)

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
| `wiki/concepts/systematic-trading.md` | 4 |
| `wiki/concepts/vibe-coding.md` | 4 |
| `wiki/concepts/activation-energy.md` | 3 |

---

## Verification

- [x] Script `validate.py` completed — 921 files scanned, 0 read errors
- [x] All 391 issues are WARNING-level broken wikilinks (forward-references)
- [x] No ERRORs, no INFOS, no frontmatter/structure/naming/code-fence issues
- [x] Validator patched to strip `.md` extension in body wikilink checks — removed 36 false positives (the `.md.md` bug, previously only patched in the `original` field check)
- [x] 0 ERRORs — third consecutive clean ERROR run (08-13, 08-14, 08-15)
- [x] Genuine broken-wikilink pool unchanged vs 08-14 (391 WARNINGs, 268 unique targets) — reported drop of −36 is entirely validator correction
- [x] No systemic format violations detected
- [x] Delta computed against approved 08-14 baseline

---

## Escalations

**No escalations this run (no format violations requiring Fix Agent).** All 391 WARNINGs are forward-references — concepts/sources linked but not yet compiled. These are expected in a growing KB and resolve naturally as Compile Agent processes more raw files.

**Validator script updated (not a wiki-file escalation):** `scripts/validate.py` concept-body (line ~207) and source-body (line ~347) broken-wikilink blocks now strip a trailing `.md` extension before existence checks, matching the `original` field check. Root cause of the 36 false positives was the known `.md.md` double-extension bug — the skill's SKILL.md pitfall documented the fix entry point only in the `original` field; the two body-check sites had been missed. No wiki content files were touched.

**Status note:** The genuine broken-wikilink count has been stable at ~390-430 WARNINGs for 9 consecutive days (08-07 through 08-15), indicating a steady state where new cross-links are added at roughly the same rate as concepts are compiled. The apparent week-long jump from 427→391 is the validator correction, not an actual KB improvement.