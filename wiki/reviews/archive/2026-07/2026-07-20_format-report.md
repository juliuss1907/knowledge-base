# Format Validation — 2026-07-20

**Status:** applied
**Applied by:** Fix Agent
**Applied at:** 2026-07-21 08:40
**Approved by:** Julius
**Issues found:** 318
**ERRORs:** 0
**WARNINGS**: 318
**INFOS:** 0
**Created:** 2026-07-20 23:16
**Validator:** format-validator
**Files checked:** 796
**Total issues**: 318
Files checked: 796
Total issues: 318

> **Δ from 07-19 (previous):** -6 total (-5 ERROR, -1 WARNING). All 5 ERRORs from 07-17/07-18/07-19 resolved by Fix Agent on 07-20 (3 missing sections + 2 long slugs fixed). 1 wikilink WARNING also resolved.
> **Δ from 07-14 (approved):** +12 WARNING, +27 files (+17 concepts, +5 sources, +5 topics). 0 ERRORs maintained — clean streak continues since 07-14 baseline.

---

## Summary

| Metric | Value | Δ from 07-19 | Δ from 07-14 |
|---|---|---|---|
| Files checked | 796 | 0 | +27 |
| Concepts | 444 | 0 | +17 |
| Sources | 148 | 0 | +5 |
| Indexes | 33 | 0 | 0 |
| Topics | 171 | 0 | +5 |
| **Total issues** | **318** | **-6** | **+12** |
| ERRORs | 0 | -5 | 0 |
| WARNINGs | 318 | -1 | +12 |
| Unique broken targets | 198 | — | — |

### Issue breakdown

| Category | Count | Details |
|---|---|---|
| **Broken wikilinks** | 318 | Forward references to uncompiled concepts + 2 raw file references |
| ├─ Individual links | 295 | Each listed with file + target |
| ├─ Forward-ref groups | 21 | Batched with `N broken wikilinks (forward-references)` summary |
| └─ Raw file references | 2 | `original` field points to raw file that exists but validator resolution failed (false positive — see Escalations) |
| **Frontmatter** | 0 | All required fields present and valid |
| **Sections** | 0 | All required sections present |
| **Naming** | 0 | All filenames and slugs valid |
| **Markdown syntax** | 0 | All code blocks, lists, emphasis valid |
| **ERRORs** | **0** | Zero structure/format violations |

---

## Top 20 Broken Wikilink Targets

| # | Target | Files |
|---|---|---|
| 1 | `[[game-theory]]` | 10 |
| 2 | `[[confirmation-bias]]` | 8 |
| 3 | `[[src_you-just-hired-a-million-bad-employees-a16z.md]]` | 5 |
| 4 | `[[ai-coding-agents]]` | 5 |
| 5 | `[[career-design]]` | 5 |
| 6 | `[[decision-making]]` | 5 |
| 7 | `[[deep-work]]` | 4 |
| 8 | `[[ai-hype-vs-reality]]` | 3 |
| 9 | `[[economic-inequality]]` | 3 |
| 10 | `[[critical-thinking]]` | 3 |
| 11 | `[[naval-ravikant]]` | 3 |
| 12 | `[[risk-parity]]` | 3 |
| 13 | `[[second-law-of-thermodynamics]]` | 3 |
| 14 | `[[saying-no]]` | 3 |
| 15 | `[[power-imbalance]]` | 3 |
| 16 | `[[src_why-the-math-mafia-is-doing-well-jesse-zhang.md]]` | 3 |
| 17 | `[[first-order-thinking]]` | 3 |
| 18 | `[[breaking-point]]` | 2 |
| 19 | `[[momentum]]` | 2 |
| 20 | `[[multi-agent-systems]]` | 2 |

*…and 178 more unique targets (each referenced 1×). Full list in issues.txt.*

---

## Top 10 Files by Warning Count

| # | File | Broken links |
|---|---|---|
| 1 | `wiki/concepts/collaborative-thinking.md` | 5 |
| 2 | `wiki/concepts/probabilistic-thinking.md` | 5 |
| 3 | `wiki/concepts/feedback-loops.md` | 4 |
| 4 | `wiki/concepts/hanlons-razor.md` | 4 |
| 5 | `wiki/concepts/meaning-through-work.md` | 4 |
| 6 | `wiki/concepts/occams-broom.md` | 4 |
| 7 | `wiki/concepts/occams-razor.md` | 4 |
| 8 | `wiki/concepts/systematic-trading.md` | 4 |
| 9 | `wiki/concepts/vibe-coding.md` | 4 |
| 10 | `wiki/concepts/activation-energy.md` | 3 |

---

## Forward-Reference Groups (21)

These files have 4–9 broken wikilinks each, batched into summary groups:

| # | File | Count |
|---|---|---|
| 1 | `wiki/sources/src_mental-models-of-art.md` | 9 |
| 2 | `wiki/sources/src_mental-models-of-economics.md` | 9 |
| 3 | `wiki/sources/src_thought-experiment.md` | 9 |
| 4 | `wiki/sources/src_fs-blog-mental-models.md` | 7 |
| 5 | `wiki/concepts/third-order-thinking.md` | 6 |
| 6 | `wiki/concepts/thought-experiment.md` | 6 |
| 7 | `wiki/sources/src_code-as-agent-harness-arxiv-2605-18747.md` | 6 |
| 8 | `wiki/sources/src_farnam-street-mental-models-biology-series.md` | 6 |
| 9 | `wiki/sources/src_farnam-street-mental-models-systems-thinking.md` | 6 |
| 10 | `wiki/sources/src_incentives-hidden-forces.md` | 6 |

*11 more groups with 4 broken links each (see raw output for full list).*

---

## Issue: Raw file `original` wikilink resolution false positives

**Severity:** WARNING
**Category:** Frontmatter

Two source files have `original` frontmatter fields the validator flags as "raw file not found", but the raw files actually exist:

| Source file | `original` value | Raw file path | Status |
|---|---|---|---|
| `src_you-just-hired-a-million-bad-employees-a16z.md` | `[[2026-07-15_you-just-hired-a-million-bad-employees-a16z.md]]` | `raw/articles/2026-07-15_you-just-hired-a-million-bad-employees-a16z.md` | ✅ Exists |
| `src_why-the-math-mafia-is-doing-well-jesse-zhang.md` | `[[2026-07-14_why-the-math-mafia-is-doing-well-jesse-zhang.md]]` | `raw/articles/2026-07-14_why-the-math-mafia-is-doing-well-jesse-zhang.md` | ✅ Exists |

These are **false positives** — the validator's `original` field resolution doesn't search raw subdirectories. Same root cause as the documented pitfall "Source-body raw-file wikilinks need raw-subdir resolution" but applied to the `original` frontmatter field.

**Suggested fix:** Update `validate.py` `check_original_wikilink()` to search raw subdirectories (same logic as source-body wikilink resolution).

---

## Verification

- [x] Validation script ran cleanly (0 errors reading files)
- [x] All 796 files parsed successfully
- [x] Zero structure violations (ERRORs) — all required sections, frontmatter fields, naming conventions conform to format-spec.md
- [x] 5 ERRORs from previous 3 reports (07-17, 07-18, 07-19) confirmed resolved by Fix Agent
- [x] 318 WARNINGs are all broken wikilinks — expected forward references to uncompiled concepts
- [x] 2 raw file `original` references verified — files exist, false positive

---

## Escalations

None — no ambiguous rules, spec conflicts, or systematic violations detected beyond expected forward-reference wikilinks.

The 2 raw file `original` field WARNINGs are false positives, not escalations (known validator limitation documented in pitfalls).
