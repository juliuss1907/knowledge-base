# Format Validation — 2026-08-31

**Status:** pending
**Issues found:** 399
**Created:** 2026-08-31 23:15:41
**Validator:** format-validator
**Files checked:** 1027 (567 concepts + 195 sources + 34 indexes + 231 topics)
**ERRORs**: 3
**WARNINGS**: 396
**INFOS:** 0
**Total issues**: 399
Files checked: 1027
Total issues: 399

Δ from 2026-08-30 23:15 run (pending): **−16 net** (415→399), **3 ERRORs** (0→3 — CLEAN STREAK BROKEN, was day 14 at 0 ERRORs), **396 WARNINGs (−19)**, **+33 files** (994→1027: 13 concepts + 8 sources + 12 topics), **270 unique broken targets (+2, from 268)**, **Top-20 shifted**: `ai-assisted-development` (3x) entered at #8, `breaking-point` (2x) fell off. Composition: individual broken 372→377 (+5), forward-ref groups 19→19 (flat), **other warnings 24→0 (−24)** — the unquoted-parent `parent: [[tag]]` set was FIXED (tag files regenerated with quoted `"[[tag]]"`). This is the entire source of the WARNING drop: 24 fixed, 5 new added from 21 new content files. 3 new ERRORs on 3 newly compiled source files — 2 slug-length violations, 1 missing section. Net: KB grows (33 wiki files), backlog churns downward (total −16) but ERRORs re-appear after 14-day clean streak.

| Metric | 08-30 | 08-31 | Delta |
|---|---|---|---|
| Files checked | 994 | 1027 | +33 |
| Total issues | 415 | 399 | −16 |
| ERRORs | 0 | 3 | +3 |
| WARNINGs | 415 | 396 | −19 |
| Unique broken targets | 268 | 270 | +2 |
| Individual broken | 372 | 377 | +5 |
| Forward-ref groups | 19 | 19 | 0 |
| Other warnings | 24 | 0 | −24 |

---

## Issue Summary

Three new ERRORs break the 14-day clean streak. All 3 ERRORs are on newly compiled source files from today's batch:

| # | File | Severity | Category | Issue |
|---|---|---|---|---|
| 1 | `src_ai-engineering-skills-map-building-deploying-ai-applications.md` | ERROR | Naming | Slug exceeds 50 chars (60 chars) |
| 2 | `src_ai-engineering-skills-map-software-engineering-fundamentals.md` | ERROR | Naming | Slug exceeds 50 chars (59 chars) |
| 3 | `src_impeccable.md` | ERROR | Sections | Missing required section: `## Key points` |

The 396 WARNINGs are all broken wikilinks (forward-references to uncompiled concepts/sources):

| Category | Count | Description |
|---|---|---|
| Individual broken wikilinks | 377 | Links to concepts/sources that don't exist yet |
| Forward-reference groups | 19 | Files with 4-9 broken links each, summarized as single entries |
| Other warnings | 0 | Unquoted-parent issue RESOLVED (24→0) |
| Unique broken targets | 270 | Distinct concept/source slugs referenced but not compiled |

**Other warnings resolved:** The 24 unquoted `parent: [[tag]]` warnings in tag files are gone — tag files were regenerated with quoted `parent: "[[tag]]"`. This is a positive fix; the corresponding [SPEC CONFLICT] escalation from days 08-28 through 08-30 is now resolved.

| Files checked | Concepts | Sources | Indexes | Topics |
|---|---|---|---|---|
| 1027 | 567 | 195 | 34 | 231 |

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

**Top-20 shift:** `[[ai-assisted-development]]` (3x) entered at #8 — new forward-ref from today's compiled files. `[[breaking-point]]` (2x) fell off the list. Top-7 slugs and counts are identical to the 08-30 report.

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

Identical set to 08-30 — no new forward-reference groups formed, none resolved.

---

## New Files This Run (33)

**13 concepts** (compiled 08-31 08:22–08:27):
- ai-frontend-design-guidance, ai-observability, ai-security-tools, architecture-as-code, code-visualization, context-database, cybersecurity-skills-library, design-systems, frontend-design-agent, product-analytics, progressive-disclosure, self-driving-products, ui-component-library

**8 sources** (compiled 08-31 08:22–08:32):
- src_ai-engineering-skills-map-building-deploying-ai-applications, src_ai-engineering-skills-map-software-engineering-fundamentals, src_anthropic-cybersecurity-skills, src_archify, src_impeccable, src_openviking, src_posthog, src_threeui

**12 topic pages** (auto-generated 08-31 22:04):
- agent-context-database, agent-context-optimization, ai-cybersecurity-skills-library, ai-frontend-design-guidance, ai-observability, ai-security-tools, architecture-as-code, code-visualization, design-systems, product-analytics-tools, self-driving-products, ui-component-library

**Zero deletions** (no merges). **24 tag files** modified (parent field re-quoted — see Escalations).

---

## Escalations

**[RESOLVED] [SPEC CONFLICT] — unquoted `parent: [[tag]]` in 24 tag files**
The 24 unquoted-parent warnings that appeared on 08-28 (Index Agent regenerated tag files with `parent: [[tag]]` unquoted, violating format-spec.md §9 which requires `"[[...]]"`) have been **RESOLVED** — all 24 tag files now use properly quoted `parent: "[[tag]]"`. The 24 corresponding WARNINGs are gone (0→0). This escalation is closed. Recommend updating index-spec.md to show quoted format to prevent recurrence when Index Agent regenerates.

**3 new ERRORs on newly compiled source files — Compile Agent quality issue**
- `src_ai-engineering-skills-map-building-deploying-ai-applications.md`: slug 60 chars (limit 50)
- `src_ai-engineering-skills-map-software-engineering-fundamentals.md`: slug 59 chars (limit 50)
- `src_impeccable.md`: missing `## Key points` section

These are Compile Agent violations on today's batch. The slug-length issue is a Compile Agent naming rule; the missing section is a structural rule. Both should be fixable by Fix Agent.

Standing note (one line, not an escalation): 270 unique broken targets — day 2 at 270 (was 268 for 6 days, 269 for 4 days before that). The broken-wikilink backlog is slowly growing as new files add references. Compile Agent's next target priority: `[[game-theory]]` (10 refs) and `[[confirmation-bias]]` (8 refs). 0 raw files sitting uncompiled as of 22:04 (all 8 from 08-30 have been compiled).

---

## Verification

Checklist of steps taken this run:

- [x] validate.py run from KB root (exit 0) — 1027 files scanned in one pass
- [x] parse_issues.py statistics extracted (3E + 396W + 0I, 270 unique targets)
- [x] Git reconciliation vs 2026-08-30 23:15 baseline: +33 wiki files added (13 concepts + 8 sources + 12 topics), 0 deleted, 0 merges; 24 tag files modified (parent re-quoted)
- [x] New-file link check: 21 new content files contributed 5 new individual broken wikilinks + 1 new unique target reached top-20 (`ai-assisted-development`)
- [x] Top-20 comparison vs 2026-08-30 report: top-7 identical; `ai-assisted-development` entered at #8, `breaking-point` fell off
- [x] Unquoted-wikilink warning set: 24→0 — all resolved
- [x] Previous report Status header checked: 08-30 format report shows `pending` → no reconcile needed
- [x] Output Validator 08-31 run (23:04) confirms 21 new source/concept files compiled today
- [x] YAML edge cases handled (datetime.date, unquoted [[wikilinks]])
- [x] File-count delta reconciled via git log --diff-filter=A/D (not mtime)
- [x] context/USER.md skipped (read-only, no frontmatter expected)
- [x] Topics dispatched by scope:topic (not index-spec.md)
- [x] Tag files cross-checked: 24 files had quoted parent; no unquoted-parent false positives