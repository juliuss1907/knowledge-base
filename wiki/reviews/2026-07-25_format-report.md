# Format Validation — 2026-07-25

**Status:** pending
**Issues found:** 336
**ERRORs**: 0
**WARNINGS**: 336
**INFOS:** 0
**Created:** 2026-07-25 23:15
**Validator:** format-validator
**Files checked:** 829
**Total issues**: 336
Files checked: 829
Total issues: 336

> **Δ from 07-24 (previous, approved/applied):** +1 file (828→829), -1 issue (337→336). +1 index file added. ✅ The 1 ERROR from 07-24 (`wiki/tag/psychology.md` missing `## Co-occurring tags`) has been resolved by the Fix Agent batch applied 2026-07-25. WARNING count unchanged at 336. File breakdown: Concepts 466, Sources 153, Indexes 34 (+1), Topics 176 — unchanged except +1 index.
>
> **Δ from 07-20 (last approved baseline):** +33 files (796→829), +18 issues (318→336). -1 ERROR (1→0), +18 WARNING (318→336). The single ERROR has been fixed; all remaining issues are broken wikilinks.

---

## Files checked

| Files checked | Concepts | Sources | Indexes | Topics |
|---|---|---|---|---|
| 829 | 466 | 153 | 34 | 176 |

---

## Summary

All 336 warnings are **broken wikilinks** — forward-references to concepts not yet compiled. Zero ERRORs, zero structural/frontmatter/section violations. The KB format is structurally clean; the only outstanding issues are content gaps (missing linked concepts).

### Breakdown

| Category | Count |
|---|---|
| Individual broken wikilinks | 313 |
| Forward-reference summary groups | 21 |
| Other warnings (original field) | 2 |
| **Total** | **336** |

---

## Top 20 Broken Targets (by reference count)

These are the concepts most frequently linked-to but not yet compiled:

| # | Target | Refs | Files affected |
|---|---|---|---|
| 1 | `[[game-theory]]` | 10 | nash-equilibrium, reciprocity, zero-sum-game, greshams-law, incentives-mental-model, ultimatum-game, negotiation, repeated-games, mutually-assured-destruction, and 1 source |
| 2 | `[[confirmation-bias]]` | 8 | hanlons-razor, map-is-not-territory, occams-broom, perspective-bias, framing-mental-model, occams-razor, galilean-relativity, and 1 source |
| 3 | `[[src_you-just-hired-a-million-bad-employees-a16z.md]]` | 5 | 100x-token, ai-evals, ai-transformation, token-looping, tokenmaxxing |
| 4 | `[[ai-coding-agents]]` | 5 | context-window-management, cross-agent-workflow, handoff-skill, session-separation, and 1 source |
| 5 | `[[career-design]]` | 5 | ikigai-unbundling, job-scoring-framework, job-worth-doing, and 2 sources |
| 6 | `[[decision-making]]` | 5 | opportunity-cost, probabilistic-thinking, recognizing-life-signals, second-order-thinking, and 1 source |
| 7 | `[[deep-work]]` | 4 | cognitive-load-theory, focus, speed-vs-velocity, and 1 source |
| 8 | `[[attention-economy]]` | 3 | ai-dependency, brain-rot, cognitive-load-theory |
| 9 | `[[ai-hype-vs-reality]]` | 3 | ai-impression-of-work, rot-economy, and 1 source |
| 10 | `[[economic-inequality]]` | 3 | ai-white-collar-automation, productivity-wage-gap, and 1 source |
| 11 | `[[critical-thinking]]` | 3 | collaborative-thinking, occams-broom, occams-razor |
| 12 | `[[naval-ravikant]]` | 3 | discipline-as-freedom, habit-automation, and 1 source |
| 13 | `[[risk-parity]]` | 3 | diversification-strategy, holy-grail-investing, and 1 source |
| 14 | `[[second-law-of-thermodynamics]]` | 3 | entropy, thermodynamics, and 1 source |
| 15 | `[[homeostasis]]` | 3 | feedback-loops, iatrogenics, and 1 source |
| 16 | `[[saying-no]]` | 3 | focus, speed-vs-velocity, and 1 source |
| 17 | `[[power-imbalance]]` | 3 | hypergamy, relationship-dynamics, and 1 source |
| 18 | `[[src_why-the-math-mafia-is-doing-well-jesse-zhang.md]]` | 3 | math-mafia, olympiad-to-founder-pipeline, quant-finance-culture |
| 19 | `[[first-order-thinking]]` | 3 | second-order-thinking, and 2 sources |
| 20 | `[[breaking-point]]` | 2 | activation-energy, and 1 source |

**211 unique broken targets** across the entire KB — nearly all are forward-references to uncompiled concepts.

---

## Top 10 Files by Broken Link Count

| File | Broken links |
|---|---|
| `wiki/concepts/probabilistic-thinking.md` | 5 |
| `wiki/concepts/collaborative-thinking.md` | 5 |
| `wiki/concepts/hanlons-razor.md` | 4 |
| `wiki/concepts/feedback-loops.md` | 4 |
| `wiki/concepts/meaning-through-work.md` | 4 |
| `wiki/concepts/occams-broom.md` | 4 |
| `wiki/concepts/occams-razor.md` | 4 |
| `wiki/concepts/systematic-trading.md` | 4 |
| `wiki/concepts/vibe-coding.md` | 4 |
| `wiki/sources/src_mental-models-of-economics.md` | 9 (summary group) |

---

## Forward-Reference Summary Groups (21 groups)

These files have ≥4 broken wikilinks each, consolidated into summary entries:

| File | Broken count | Note |
|---|---|---|
| `wiki/sources/src_mental-models-of-economics.md` | 9 | Forward-references to uncompiled concepts |
| `wiki/sources/src_mental-models-of-art.md` | 9 | Forward-references to uncompiled concepts |
| `wiki/sources/src_thought-experiment.md` | 9 | Forward-references to uncompiled concepts |
| `wiki/sources/src_fs-blog-mental-models.md` | 7 | Forward-references to uncompiled concepts |
| `wiki/concepts/thought-experiment.md` | 6 | Forward-references to uncompiled concepts |
| `wiki/concepts/third-order-thinking.md` | 6 | Forward-references to uncompiled concepts |
| `wiki/sources/src_farnam-street-mental-models-systems-thinking.md` | 6 | Forward-references to uncompiled concepts |
| `wiki/sources/src_farnam-street-mental-models-biology-series.md` | 6 | Forward-references to uncompiled concepts |
| `wiki/sources/src_code-as-agent-harness-arxiv-2605-18747.md` | 6 | Forward-references to uncompiled concepts |
| `wiki/sources/src_probabilistic-thinking.md` | 6 | Forward-references to uncompiled concepts |
| `wiki/sources/src_incentives-hidden-forces.md` | 6 | Forward-references to uncompiled concepts |
| ... and 10 more groups (4 links each) | — | Various sources and concepts |

---

## Other Warnings (2)

These are known false positives documented in [format-validator pitfalls](.hermes/skills/format-validator/SKILL.md#source-body-raw-file-wikilinks-need-raw-subdir-resolution):

1. `wiki/sources/src_why-the-math-mafia-is-doing-well-jesse-zhang.md` — `original` wikilink `[[2026-07-14_why-the-math-mafia-is-doing-well-jesse-zhang.md]]` flagged as "raw file not found" (file exists under `raw/articles/`)
2. `wiki/sources/src_you-just-hired-a-million-bad-employees-a16z.md` — `original` wikilink `[[2026-07-15_you-just-hired-a-million-bad-employees-a16z.md]]` flagged as "raw file not found" (file exists under `raw/articles/`)

---

## Verification

- ✅ `validate.py` ran successfully — 0 read errors
- ✅ All 829 files parsed and validated
- ✅ 0 ERRORs — structural compliance is clean
- ✅ All 336 WARNINGs are broken wikilinks (forward-references) — no new violation types
- ✅ The 1 ERROR from 07-24 (psychology.md Co-occurring tags) has been resolved
- ✅ Ground truth: `wiki/meta/format-spec.md` unchanged since last run
- ✅ `wiki/meta/index-spec.md` unchanged since last run

---

## Escalations

### [PERSISTENT FALSE POSITIVE] — original field raw-subdir resolution

**Issue:** The validator's `check_original_wikilink()` function flags 2 source files for "raw file not found" because it doesn't search raw subdirectories. Both raw files exist under `raw/articles/`.

**Files:** `src_why-the-math-mafia-is-doing-well-jesse-zhang.md`, `src_you-just-hired-a-million-bad-employees-a16z.md`

**Status:** Known limitation documented in SKILL.md pitfalls. Same issue persists since 07-20.

**Recommendation:** Update `validate.py` to apply raw-subdir resolution to `check_original_wikilink()`, matching the fix already applied to source-body wikilink validation.
