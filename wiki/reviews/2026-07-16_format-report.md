# Format Validation — 2026-07-16

**Status:** pending
**Issues found:** 319
**Created:** 2026-07-16 23:15
**Validator:** format-validator

> **Context:** Evening run. Previous approved baseline: 2026-07-14 (approved, 306 WARNINGs, 0 ERRORs). KB continues to grow with zero structural format violations.
> **Δ from 07-14 (approved):** +13 WARNINGs, +11 files (+7 concepts, +2 sources, +2 topics). Clean streak continues — zero ERRORs. All 319 issues are broken wikilinks (forward-references).

---

## Summary

| Metric | Value | Δ from 07-14 (approved) |
|---|---|---|
| Files checked | 780 | +11 |
| Concepts | 434 | +7 |
| Sources | 145 | +2 |
| Indexes | 33 | — |
| Topics | 168 | +2 |
| **Total issues** | **319** | **+13** |
| **ERRORs** | **0** | — |
| **WARNINGs** | **319** | **+13** |
| **INFOs** | **0** | — |

---

## Issue Breakdown

| Category | Count | Type |
|---|---|---|
| Broken wikilinks (individual) | 296 | WARNING |
| Forward-reference summary groups | 21 | WARNING |
| Raw-file original link resolution | 2 | WARNING |
| **Total** | **319** | **All WARNINGs** |

### Broken wikilinks analysis

- **199 unique broken targets** across 319 WARNINGs
- **21 summary groups** (files with 4+ broken links condensed to single WARNING)
- **296 individual broken wikilinks** in files with ≤5 broken links

#### Top 20 broken targets

| Target | Refs | Notes |
|---|---|---|
| `[[game-theory]]` | 10× | Core concept, forward-ref |
| `[[confirmation-bias]]` | 8× | Common bias ref, forward-ref |
| `[[src_you-just-hired-a-million-bad-employees-a16z.md]]` | 5× | Source file forward-ref |
| `[[ai-coding-agents]]` | 5× | Recurring forward-ref |
| `[[career-design]]` | 5× | New batch forward-ref |
| `[[decision-making]]` | 5× | Core concept forward-ref |
| `[[deep-work]]` | 4× | Productivity ref |
| `[[ai-hype-vs-reality]]` | 3× | Multiple files |
| `[[economic-inequality]]` | 3× | Recurring forward-ref |
| `[[critical-thinking]]` | 3× | Core skill ref |
| `[[naval-ravikant]]` | 3× | Person entity ref |
| `[[risk-parity]]` | 3× | Finance ref |
| `[[second-law-of-thermodynamics]]` | 3× | Physics ref |
| `[[saying-no]]` | 3× | Productivity ref |
| `[[power-imbalance]]` | 3× | Social dynamics ref |
| `[[src_why-the-math-mafia-is-doing-well-jesse-zhang.md]]` | 3× | Source file forward-ref |
| `[[first-order-thinking]]` | 3× | Mental model ref |
| `[[breaking-point]]` | 2× | Activation energy ref |
| `[[momentum]]` | 2× | Physics ref |
| `[[multi-agent-systems]]` | 2× | Agent architecture ref |

#### Top 10 files by warning count

| File | Warnings |
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

### Raw-file original link warnings (2 instances)

These are not broken wikilinks in the body — they are the `original` frontmatter field pointing to a raw file that doesn't exist under `raw/`:

| # | File | Missing raw target |
|---|---|---|
| 1 | `wiki/sources/src_why-the-math-mafia-is-doing-well-jesse-zhang.md` | `raw/**/2026-07-14_why-the-math-mafia-is-doing-well-jesse-zhang.md` |
| 2 | `wiki/sources/src_you-just-hired-a-million-bad-employees-a16z.md` | `raw/**/2026-07-15_you-just-hired-a-million-bad-employees-a16z.md` |

Both were flagged in 07-15 report. Issue persists — raw files have not been ingested yet or were ingested with different filenames.

---

## Forward-reference summary groups (21 files)

21 files have 4+ broken wikilinks each, condensed to single summary WARNINGs. These are all expected forward-references to concepts not yet compiled. Largest groups:

| File | Count |
|---|---|
| `wiki/concepts/thought-experiment.md` | 6 |
| `wiki/concepts/third-order-thinking.md` | 6 |
| `wiki/sources/src_code-as-agent-harness-arxiv-2605-18747.md` | 6 |
| `wiki/sources/src_farnam-street-mental-models-biology-series.md` | 6 |
| `wiki/sources/src_farnam-street-mental-models-systems-thinking.md` | 6 |
| `wiki/sources/src_incentives-hidden-forces.md` | 6 |
| `wiki/sources/src_probabilistic-thinking.md` | 6 |
| `wiki/sources/src_fs-blog-mental-models.md` | 7 |
| `wiki/sources/src_mental-models-of-art.md` | 9 |
| `wiki/sources/src_mental-models-of-economics.md` | 9 |
| `wiki/sources/src_thought-experiment.md` | 9 |

---

## Delta from 2026-07-14 (last approved)

| Metric | 07-14 | 07-16 | Δ |
|---|---|---|---|
| Files checked | 769 | 780 | **+11** |
| Concepts | 427 | 434 | **+7** |
| Sources | 143 | 145 | **+2** |
| Topics | 165 | 168 | **+3** |
| Total issues | 306 | 319 | **+13 WARNINGs** |
| ERRORs | 0 | 0 | **0** |
| Unique broken targets | ~190 | 199 | **+9** |

**Assessment:** KB grew by 11 files. All 319 issues are forward-reference broken wikilinks — the expected artifact of a growing knowledge graph where concepts are compiled progressively. Zero structural format violations (no frontmatter errors, no section errors, no naming errors, no markdown syntax errors). The 2 raw-file original link issues persist from 07-15.

**Clean streak:** 3 consecutive days (07-14, 07-15, 07-16) with zero ERRORs. This is the new normal.

---

## Actions needed

**None required.** All 319 WARNINGs are expected forward-reference broken wikilinks that resolve organically as concepts are compiled and added to the KB. The 2 raw-file original link issues are transient — they resolve when the corresponding raw files are ingested.

No frontmatter errors. No section structure violations. No naming convention violations. No markdown syntax errors.

---

## Escalations

_No escalations required._ Zero format violations across 780 files. KB format health is excellent.

---

## Verification

```
✅ Report written: wiki/reviews/2026-07-16_format-report.md
✅ _action-required.md updated with today's entry
✅ MEMORY.md logged
✅ Telegram notification sent
```

**Validator:** format-validator (Hermes-VPS)
**Run time:** 2026-07-16 23:15 ICT
**Script:** `.hermes/skills/format-validator/scripts/validate.py`
