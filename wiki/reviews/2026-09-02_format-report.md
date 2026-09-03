# Format Validation — 2026-09-02

**Status:** approved
**Issues found:** 398
**Created:** 2026-09-02 23:16:44
**Validator:** format-validator
**Files checked:** 1032 (571 concepts + 196 sources + 34 indexes + 231 topics)
**ERRORs**: 0
**WARNINGS**: 398
**INFOS:** 0
**Total issues**: 398
Files checked: 1032
Total issues: 398

Δ from 2026-09-01 23:15 run (pending approval — prior run): **+2 net** (396→398), **0 ERRORs** (0→0 — clean ERROR streak day 2 at 0), **+2 WARNINGs** (396→398), **+5 new wiki files** (1027→1032 — Google Cloud agent-sandbox cluster compiled 08:04: 4 concepts `agent-sandbox-runtimes`, `isolation-spectrum`, `sandbox-state-forking`, `network-egress-default-deny` + 1 source `src_google-cloud-agent-sandbox-runtimes`), **271 unique broken targets (+1 — `prompt-injection` entered the pool at 2 refs, day 1 at 271)**, **Top-20 identical** (same slugs, same counts, same order — all 20 rows match 09-01). Composition: individual broken 377→379 (+2 — both are `[[prompt-injection]]` in new concepts), forward-ref groups 19→19 (flat), other warnings 0→0 (flat). The +2 WARNINGs come ENTIRELY from the 5 newly compiled files — each adds one broken wikilink to the same single new target `prompt-injection`, which is the exact forward-ref Output Validator 09-02 WARNING 1 flagged (referenced in 2 concepts, no concept/source/raw exists to resolve it). Net: the only change is the new cluster contributing 2 forward-references to one uncompiled target; the pre-existing backlog is byte-identical.

| Metric | 09-01 | 09-02 | Delta |
|---|---|---|---|
| Files checked | 1027 | 1032 | +5 |
| Total issues | 396 | 398 | +2 |
| ERRORs | 0 | 0 | 0 |
| WARNINGs | 396 | 398 | +2 |
| Unique broken targets | 270 | 271 | +1 |
| Individual broken | 377 | 379 | +2 |
| Forward-ref groups | 19 | 19 | 0 |
| Other warnings | 0 | 0 | 0 |

---

## Issue Summary

**Clean ERROR streak continues (day 2 at 0 ERRORs).** No structural violations, no missing fields, no naming errors, no YAML issues. All 398 issues are WARNINGs and every one is a broken wikilink (forward-reference to an uncompiled concept/source).

The 5 new files (Google Cloud agent-sandbox cluster, compiled 08:04 today) each pass format compliance cleanly — correct frontmatter, sections, naming, and markdown. Their only contribution to the issue count is 2 forward-references to `[[prompt-injection]]` (in `agent-sandbox-runtimes.md` + `network-egress-default-deny.md`). That target has no compiled concept, no source, and no raw material anywhere in the KB — a forward-reference with no natural path to resolve. This is exactly Output Validator 09-02 WARNING 1. Recommendation: compile a `prompt-injection` concept when a suitable source arrives, or have Fix Agent drop the 2 links.

| Category | Count | Description |
|---|---|---|
| Individual broken wikilinks | 379 | Links to concepts/sources that don't exist yet |
| Forward-reference groups | 19 | Files with 4-9 broken links each, summarized as single entries |
| Other warnings | 0 | No other warning categories |
| Unique broken targets | 271 | Distinct concept/source slugs referenced but not compiled |

| Files checked | Concepts | Sources | Indexes | Topics |
|---|---|---|---|---|
| 1032 | 571 | 196 | 34 | 231 |

---

## Top 20 Broken Targets

| # | Target | Count |
|---|---|---|
| 1 | `[[game-theory]]` | 10 |
| 2 | `[[confirmation-bias]]` | 8 |
| 3 | `[[deep-work]]` | 5 |
| 4 | `[[ai-coding-agents]]` | 5 |
| 5 | `[[career-design]]` | 5 |
| 6 | `[[decision-making]]` | 5 |
| 7 | `[[attention-economy]]` | 3 |
| 8 | `[[ai-assisted-development]]` | 3 |
| 9 | `[[ai-hype-vs-reality]]` | 3 |
| 10 | `[[economic-inequality]]` | 3 |
| 11 | `[[intellectual-humility]]` | 3 |
| 12 | `[[naval-ravikant]]` | 3 |
| 13 | `[[risk-parity]]` | 3 |
| 14 | `[[second-law-of-thermodynamics]]` | 3 |
| 15 | `[[homeostasis]]` | 3 |
| 16 | `[[saying-no]]` | 3 |
| 17 | `[[cognitive-dissonance]]` | 3 |
| 18 | `[[power-imbalance]]` | 3 |
| 19 | `[[stoicism]]` | 3 |
| 20 | `[[first-order-thinking]]` | 3 |

**Top-20 identical to 09-01** — same slugs, same counts, same order. No targets entered, none fell off. The new unique target `prompt-injection` (2 refs) sits just below the Top-20 cutoff (3 refs).

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

Identical set to 09-01 — no new forward-reference groups formed, none resolved.

---

## New Files This Run

**+5 new wiki files** compiled at 08:04 today (Google Cloud agent-sandbox cluster), verified via `git log --diff-filter=A -- wiki/concepts wiki/sources wiki/tag wiki/topic` since 2026-09-01 23:20:

- `wiki/concepts/agent-sandbox-runtimes.md`
- `wiki/concepts/isolation-spectrum.md`
- `wiki/concepts/sandbox-state-forking.md`
- `wiki/concepts/network-egress-default-deny.md`
- `wiki/sources/src_google-cloud-agent-sandbox-runtimes.md`

This is the raw file `raw/posts/2026-09-01_google-cloud-agent-sandbox-runtimes.md` (ingested 09-01 17:13, flagged as uncompiled in the 09-01 report) finally being compiled. All 5 pass format compliance cleanly. Zero deletions (no merges), zero topic/tag files added.

---

## Escalations

No new escalations this run. No structural violations, no ERRORs, no spec conflicts, no systematic issues.

Forward-reference backlog note (standing, non-escalation): unique broken targets rose to **271** (+1, day 1) — the first increase since the 270 plateau (day 2 on 09-01). The rise is fully explained by the new cluster's single `prompt-injection` forward-ref, not by any regression. Compile Agent's target priority unchanged: `[[game-theory]]` (10 refs) and `[[confirmation-bias]]` (8 refs) remain the most-referenced uncompiled concepts. No raw files sitting uncompiled as of this run.

---

## Verification

Checklist of steps taken this run:

- [x] validate.py run from KB root (exit 0) — 1032 files scanned in one pass
- [x] parse_issues.py statistics extracted (0E + 398W + 0I, 271 unique targets, 379 individual + 19 groups)
- [x] Git reconciliation vs 2026-09-01 23:15 baseline: +5 wiki files added (4 concepts + 1 source, compiled 08:04), 0 deleted, 0 merges, 0 topics/tags
- [x] New broken links traced: both +2 WARNINGs are `[[prompt-injection]]` in agent-sandbox-runtimes.md + network-egress-default-deny.md — matches Output Validator 09-02 WARNING 1 (same target, same 2 files)
- [x] Top-20 comparison vs 2026-09-01 report: identical (all 20 rows match)
- [x] Forward-ref groups vs 09-01: identical 19 groups
- [x] Previous report Status header checked: 09-01 format report shows `pending` + `🔍 PENDING` row in _action-required → no reconcile needed
- [x] Output Validator 09-02 (23:09) row preserved in _action-required.md during rewrite
- [x] YAML edge cases handled (datetime.date, unquoted [[wikilinks]])
- [x] File-count delta reconciled via git log --diff-filter=A/D (not mtime)
- [x] context/USER.md skipped (read-only, no frontmatter expected)
- [x] Topics dispatched by scope:topic (not index-spec.md)
- [x] Tag files cross-checked: 0 unquoted-parent false positives
