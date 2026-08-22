# Format Validation — 2026-08-22

**Status:** pending
**Issues found:** 392
**Created:** 2026-08-22 23:15
**Validator:** format-validator
**Files checked:** 933 (525 concepts + 174 sources + 34 indexes + 200 topics)
**ERRORs**: 0
**WARNINGS**: 392
**INFOS:** 0
**Total issues**: 392
Files checked: 933
Total issues: 392

Δ from 2026-08-21 (approved, applied 2026-08-22 14:40 by Fix Agent): **−74 total issues** (466→392), **−73 ERRORs** (73→0), **−1 WARNING** (393→392), **+9 files** (924→933: +5 sources, +4 topics, +2 concepts added, −2 concepts merged), **−1 unique broken target** (270→269). Clean ERROR streak RESTORED — Fix Agent's 08-22 tag-file regeneration (24 L3 tag files + tag.md rewrite) fully resolved the 73 ERROR regression from 08-21. First clean ERROR run since 08-17.

---

## Issue Summary

All 392 issues are **WARNING** severity — broken wikilinks (forward-references to uncompiled concepts):

| Category | Count | Description |
|---|---|---|
| Individual broken wikilinks | 372 | Links to concepts/sources that don't exist yet |
| Forward-reference groups | 20 | Files with 4-9 broken links each, summarized as single entries |
| Unique broken targets | 269 | Distinct concept/source slugs referenced but not compiled |

**No ERRORs, no INFOS.** Sixth clean ERROR run in last 7 days (08-13 through 08-17, then 08-22; the 73 ERRORs from 08-21 were an Index Agent regression, resolved same-day by Fix Agent on 08-22).

| Files checked | Concepts | Sources | Indexes | Topics |
|---|---|---|---|---|
| 933 | 525 | 174 | 34 | 200 |

---

## Delta Analysis — KB grew, debt flat

KB grew by 9 net files today (+5 sources, +4 topics, +2 concepts, −2 merged concepts) yet total issues **dropped** by 1:

- **Positive:** `[[strategic-thinking]]` and `[[neuroplasticity]]` forward-references resolved by today's 2 new concepts; 2 concept merges (costly-signaling→costly-signal, identity-detachment→identity-transformation) re-pointed backlinks.
- **Negative:** 5 new sources added a small number of new forward-references, offsetting most of the resolved ones. Net −1.
- **Composition:** Top-20 broken-target list identical to 08-21 — no shift in backlog composition.

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

---

## Q: Are these WARNINGs actionable?

No. All 392 WARNINGs are forward-references — wikilinks pointing at concept slugs that Compile Agent has not yet compiled. They resolve naturally as more raw files are processed. This is expected debt in a growing KB and does not require Fix Agent action.

**No structural or format violations were detected.** Frontmatter, sections, naming, and markdown syntax all compliant across 933 files.

---

## Escalations

None. No ERRORs, no spec conflicts, no systematic violations. Fix Agent's 08-22 tag-file regeneration verified clean — index-spec §5.3 sections present in all 24 L3 tag files, tag.md L2 frontmatter complete.

---

## Verification

- [x] Loaded format-spec.md + index-spec.md (ground truth, cached)
- [x] Scanned all 933 markdown files in wiki/sources/, wiki/concepts/, wiki/tag/, wiki/topic/, raw/, wiki/, context/ (single pass)
- [x] Dispatched by `type` field: concept/source → format-spec, index → index-spec, topic → light topic validation
- [x] context/USER.md skipped (read-only, no frontmatter)
- [x] wiki/drafts/ skipped (already flagged)
- [x] Frontmatter: required fields, field order, YAML syntax, Pool A/B tag membership
- [x] Sections: required sections, order, heading levels, no duplicates
- [x] Naming: filename format, slug rules (lowercase-hyphen, ≤50 chars), folder correctness
- [x] Markdown: wikilink resolution (raw-subdir + .md-strip), code fence language tags, list markers
- [x] YAML edge cases handled (datetime.date, unquoted [[wikilinks]])
- [x] Report limit: 20 actionable issues — N/A (0 ERRORs; WARNINGs summarized, not itemized)
