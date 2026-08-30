# Format Validation — 2026-08-30

**Status:** pending
**Issues found:** 415
**Created:** 2026-08-30 23:15:58
**Validator:** format-validator
**Files checked:** 994 (554 concepts + 187 sources + 34 indexes + 219 topics)
**ERRORs**: 0
**WARNINGS**: 415
**INFOS:** 0
**Total issues**: 415
Files checked: 994
Total issues: 415

Δ from 2026-08-29 23:15 run (pending): **0 net change** (415→415), **0 ERRORs** (flat at 0 — clean streak day 14), **415 WARNINGs (flat)**, **0 files** (994→994 — NO wiki files added; 8 raw files ingested today 09:07/13:58–14:53 but not yet compiled, wiki layer unchanged), **268 unique broken targets (flat — day 6 at 268)**, **Top-20 list identical** (same slugs, same counts — game-theory 10, confirmation-bias 8, deep-work 5, etc.). Composition exact-zero-flat, not churned: individual broken wikilinks 372→372 (flat), forward-reference groups 19→19 (flat), other warnings 24→24 (flat — the unquoted `parent: [[tag]]` set unchanged, day 2). 0 new files contributed **0 broken wikilinks** (Output Validator 23:09 confirmed 0 new source/concept files since the 08-29 run). Net: wiki layer static (raw grows +8, uncompiled), backlog frozen.

| Metric | 08-29 | 08-30 | Delta |
|---|---|---|---|
| Files checked | 994 | 994 | 0 |
| Total issues | 415 | 415 | 0 |
| ERRORs | 0 | 0 | 0 |
| WARNINGs | 415 | 415 | 0 |
| Unique broken targets | 268 | 268 | 0 |
| Individual broken | 372 | 372 | 0 |
| Forward-ref groups | 19 | 19 | 0 |
| Other warnings | 24 | 24 | 0 |

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

## New Files This Run (0)

No wiki files added since 2026-08-29 23:15 (git `--diff-filter=A` on wiki/ returns empty). Ingest added **8 raw files** today but Compile Agent has not produced wiki files from them:

| Type | File |
|---|---|
| Raw article | 2026-08-30_ai-engineering-skills-map-building-deploying-ai-applications |
| Raw article | 2026-08-30_ai-engineering-skills-map-software-engineering-fundamentals |
| Raw repo | 2026-08-30_openviking |
| Raw repo | 2026-08-30_anthropic-cybersecurity-skills |
| Raw repo | 2026-08-30_posthog |
| Raw repo | 2026-08-30_threeui |
| Raw repo | 2026-08-30_impeccable |
| Raw repo | 2026-08-30_archify |

0 wiki files → **0 new broken wikilinks**. This is the "no compilation happened" variant (same as 08-28): the validated wiki layer is byte-identical; the backlog neither drains nor accumulates.

---

## Escalations

**[SPEC CONFLICT] — unquoted `parent: [[tag]]` in 24 tag files (day 2, unchanged)**
Issue: Index Agent regenerated tag files at 08-29 21:10 with `parent: [[tag]]` (unquoted), matching index-spec.md's format. But format-spec.md §9 requires quoted wikilinks in frontmatter: `"[[...]]"`. This creates 24 WARNINGs, still present today with the identical file set (24/24). Recommend: clarify which spec is authoritative — either update index-spec.md to show quoted format, or add a format-spec.md exception for tag file `parent` field. Not re-escalated as new — carrying forward the open escalation from 08-29.

Standing note (one line, not an escalation): 268 unique broken targets — flat day 6 at 268 after exiting the 269 plateau (08-22→08-25). The broken-wikilink backlog is frozen; the 415 issue count is stable. Compile Agent's next target priority: `[[game-theory]]` (10 refs) and `[[confirmation-bias]]` (8 refs). 8 raw files (2 ai-engineering articles + 6 repos) are sitting uncompiled — the next Compile run should clear part of this backlog.

---

## Verification

Checklist of steps taken this run:

- [x] validate.py run from KB root (exit 0) — 994 files scanned in one pass
- [x] parse_issues.py statistics extracted (415W, 0E, 0I, 268 unique targets)
- [x] Git reconciliation vs 2026-08-29 23:15 baseline: +0 wiki files added, 0 deleted, 0 merges; +8 raw files (2 articles + 6 repos) uncompiled
- [x] New-file link check: 0 new wiki files → 0 new broken wikilinks (trivially satisfied)
- [x] Top-20 comparison vs 2026-08-29 23:15 report: identical — same slugs, same counts
- [x] Unquoted-wikilink warning set compared: 24/24 identical files, unchanged
- [x] Previous report Status header checked: 08-29 format report shows `pending` → no reconcile needed
- [x] Output Validator 23:09 run corroborates: 0 new source/concept files ("nothing compiled today")
- [x] YAML edge cases handled (datetime.date, unquoted [[wikilinks]])
- [x] File-count delta reconciled via git log --diff-filter=A/D (not mtime)
- [x] context/USER.md skipped (read-only, no frontmatter expected)
