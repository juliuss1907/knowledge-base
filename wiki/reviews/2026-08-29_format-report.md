# Format Validation — 2026-08-29

**Status:** approved
**Issues found:** 415
**Created:** 2026-08-29 23:15:58
**Validator:** format-validator
**Files checked:** 994 (554 concepts + 187 sources + 34 indexes + 219 topics)
**ERRORs**: 0
**WARNINGS**: 415
**INFOS:** 0
**Total issues**: 415
Files checked: 994
Total issues: 415

Δ from 2026-08-28 23:15 run (pending): **+24 total issues** (391→415), **0 ERRORs** (flat at 0 — clean streak day 13), **+24 WARNINGs** (391→415), **+10 files** (984→994), **268 unique broken targets (flat — day 5 at 268)**, **Top-20 identical** (same slugs, same counts — game-theory 10, confirmation-bias 8, deep-work 5, etc.). Composition **churned, not exact-zero-flat**: individual broken wikilinks 372→372 (flat), forward-reference groups 19→19 (flat), but **24 NEW "other warnings"** appeared — unquoted `parent: [[tag]]` in 24 wiki/tag/*.md files (Index Agent regeneration at 08-29 21:10 changed `parent: "[[tag]]"` to `parent: [[tag]]`, which YAML parses as a nested list). The genuine broken-wikilink backlog is frozen at 268 unique targets; the +24 is a new frontmatter-format warning class from a known cross-spec conflict (index-spec.md shows unquoted, format-spec.md §9 requires quoted). 10 new files (6 concepts + 2 sources + 2 topics) contributed **0 new broken wikilinks**.

---

## Issue Summary

All 415 issues are **WARNING** severity — broken wikilinks (forward-references to uncompiled concepts) and frontmatter format warnings:

| Category | Count | Description |
|---|---|---|
| Individual broken wikilinks | 372 | Links to concepts/sources that don't exist yet |
| Forward-reference groups | 19 | Files with 4-9 broken links each, summarized as single entries |
| Other warnings | 24 | Unquoted `parent: [[tag]]` in tag file frontmatter (YAML parses as nested list) |
| Unique broken targets | 268 | Distinct concept/source slugs referenced but not compiled |

**No ERRORs, no INFOS.** Frontmatter, sections, naming, markdown syntax all compliant across 994 files — except for the 24 unquoted-wikilink warnings in tag files.

| Files checked | Concepts | Sources | Indexes | Topics |
|---|---|---|---|---|
| 994 | 554 | 187 | 34 | 219 |

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

## New Warnings: Unquoted `parent: [[tag]]` in Tag Files (24)

Index Agent regenerated all 24 wiki/tag/*.md files at 2026-08-29 21:10, changing `parent: "[[tag]]"` (quoted, valid) to `parent: [[tag]]` (unquoted, YAML parses as nested list). This is a known cross-spec conflict: index-spec.md shows the unquoted form while format-spec.md §9 requires quoted wikilinks in frontmatter (`"[[...]]"`).

Affected files:
- wiki/tag/ai.md, wiki/tag/automation.md, wiki/tag/coding.md, wiki/tag/crypto.md, wiki/tag/defi.md, wiki/tag/economic.md, wiki/tag/geopolitics.md, wiki/tag/hack.md, wiki/tag/health.md, wiki/tag/investment.md, wiki/tag/law.md, wiki/tag/layer1.md, wiki/tag/news.md, wiki/tag/opinion.md, wiki/tag/politic.md, wiki/tag/productivity.md, wiki/tag/psychology.md, wiki/tag/research.md, wiki/tag/strategy.md, wiki/tag/system.md, wiki/tag/tech.md, wiki/tag/tools.md, wiki/tag/tutorial.md, wiki/tag/vibecode.md

---

## New Files This Run (10)

Compiled since 2026-08-28 23:15:

| Type | File |
|---|---|
| Concept | creator-economy |
| Concept | design-process |
| Concept | digital-renaissance |
| Concept | new-renaissance-man |
| Concept | one-human-business |
| Concept | prototype-gravity |
| Source | src_how-i-design-with-ai |
| Source | src_we-are-in-the-middle-of-the-digital-renaissance |
| Topic | ai-design-workflow |
| Topic | digital-renaissance |

All 10 new files contributed **0 new broken wikilinks** to the backlog.

---

## Escalations

**[SPEC CONFLICT] — unquoted `parent: [[tag]]` in 24 tag files**
Issue: Index Agent regenerated tag files at 08-29 21:10 with `parent: [[tag]]` (unquoted), matching index-spec.md's format. But format-spec.md §9 requires quoted wikilinks in frontmatter: `"[[...]]"`. This creates 24 WARNINGs. Recommend: clarify which spec is authoritative — either update index-spec.md to show quoted format, or add a format-spec.md exception for tag file `parent` field.

Standing note (one line, not an escalation): 268 unique broken targets — flat day 5 at 268 after exiting the 269 plateau (08-22→08-25). The broken-wikilink backlog is frozen; the +24 issue count increase is entirely from the tag-file unquoted-wikilink warnings, not new confusion debt. Compile Agent's next target priority: `[[game-theory]]` (10 refs) and `[[confirmation-bias]]` (8 refs).

---

## Verification

Checklist of steps taken this run:

- [x] validate.py run from KB root (exit 0) — 994 files scanned in one pass
- [x] parse_issues.py statistics extracted (415W, 0E, 0I, 268 unique targets)
- [x] Git reconciliation vs 2026-08-28 23:15 baseline: +10 wiki files added (6 concepts + 2 sources + 2 topics), 0 deleted, 0 merges
- [x] New-file link check: 10 new files contributed 0 new broken wikilinks
- [x] Top-20 comparison vs 2026-08-28 23:15 report: identical — same slugs, same counts
- [x] Unquoted-wikilink regression traced to Index Agent tag file regeneration at 08-29 21:10 (commit b6512994)
- [x] Previous report Status header checked: 08-28 format report shows `pending` → no reconcile needed
- [x] YAML edge cases handled (datetime.date, unquoted [[wikilinks]])
- [x] File-count delta reconciled via git log --diff-filter=A/D (not mtime)
- [x] context/USER.md skipped (read-only, no frontmatter expected)