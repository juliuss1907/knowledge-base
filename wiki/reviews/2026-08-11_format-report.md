# Format Validation — 2026-08-11

**Status:** pending
**Issues found:** 477
**Created:** 2026-08-11 23:15
**Validator:** format-validator
**Files checked:** 921 (524 concepts + 168 sources + 34 indexes + 195 topics)
**ERRORs**: 50
**WARNINGS**: 427
**INFOS:** 0
**Total issues**: 477
Files checked: 921
Total issues: 477

Δ from 2026-08-10 (approved): +27 files (+16 concepts, +6 sources, −2 indexes, +7 topics), +45 total issues (432→477), +48 ERRORs (2→50), −3 WARNINGs (430→427)

---

| Files checked | Concepts | Sources | Indexes | Topics |
|---|---|---|---|---|
| 921 | 524 | 168 | 34 | 195 |

## Issues Found: 477

| Severity | Count | Category |
|---|---|---|
| ERROR | **50** | 49 tag files missing required sections + 1 slug too long |
| WARNING | **427** | 407 individual broken wikilinks + 20 forward-reference summary groups |
| INFO | **0** | — |

### Delta Details

| Metric | 2026-08-10 (approved) | 2026-08-11 | Δ |
|---|---|---|---|
| Files | 894 | 921 | **+27** |
| Concepts | 508 | 524 | +16 |
| Sources | 162 | 168 | +6 |
| Indexes | 36 | 34 | −2 |
| Topics | 188 | 195 | +7 |
| ERRORs | 2 | 50 | **+48** |
| WARNINGs | 430 | 427 | −3 |
| Total issues | 432 | 477 | **+45** |

**Positive delta (issues resolved):**
- Previous 2 ERRORs (missing `## Co-occurring tags` in `layer2.md` and `perpdex.md`) — FIXED

**Negative delta (new issues):**
- 48 new ERRORs: 24 tag files lost `## Parent` and `## Files with this tag` sections after Index Agent regeneration; 1 new source file has slug exceeding 50 chars
- 3 WARNINGs removed (net −3 from 430→427) — slight improvement in broken wikilink count despite file growth

---

## ERRORs (50)

### 1. Tag files missing required sections (49 ERRORs)

**Severity:** ERROR
**Category:** Sections
**Pattern:** 24 tag index files at `wiki/tag/*.md` are missing `## Parent` and `## Files with this tag` sections. Additionally, `wiki/tag/tag.md` (Tầng 2) is missing `## Notes`.

**Likely cause:** Index Agent regenerated these files without including the required sections per index-spec.md.

**Affected files (24 × 2 ERRORs = 48):**

| File | Missing Sections |
|---|---|
| `wiki/tag/ai.md` | `## Parent`, `## Files with this tag` |
| `wiki/tag/automation.md` | `## Parent`, `## Files with this tag` |
| `wiki/tag/coding.md` | `## Parent`, `## Files with this tag` |
| `wiki/tag/crypto.md` | `## Parent`, `## Files with this tag` |
| `wiki/tag/defi.md` | `## Parent`, `## Files with this tag` |
| `wiki/tag/economic.md` | `## Parent`, `## Files with this tag` |
| `wiki/tag/geopolitics.md` | `## Parent`, `## Files with this tag` |
| `wiki/tag/hack.md` | `## Parent`, `## Files with this tag` |
| `wiki/tag/health.md` | `## Parent`, `## Files with this tag` |
| `wiki/tag/investment.md` | `## Parent`, `## Files with this tag` |
| `wiki/tag/law.md` | `## Parent`, `## Files with this tag` |
| `wiki/tag/layer1.md` | `## Parent`, `## Files with this tag` |
| `wiki/tag/news.md` | `## Parent`, `## Files with this tag` |
| `wiki/tag/opinion.md` | `## Parent`, `## Files with this tag` |
| `wiki/tag/politic.md` | `## Parent`, `## Files with this tag` |
| `wiki/tag/productivity.md` | `## Parent`, `## Files with this tag` |
| `wiki/tag/psychology.md` | `## Parent`, `## Files with this tag` |
| `wiki/tag/research.md` | `## Parent`, `## Files with this tag` |
| `wiki/tag/strategy.md` | `## Parent`, `## Files with this tag` |
| `wiki/tag/system.md` | `## Parent`, `## Files with this tag` |
| `wiki/tag/tech.md` | `## Parent`, `## Files with this tag` |
| `wiki/tag/tools.md` | `## Parent`, `## Files with this tag` |
| `wiki/tag/tutorial.md` | `## Parent`, `## Files with this tag` |
| `wiki/tag/vibecode.md` | `## Parent`, `## Files with this tag` |

**Additional:**
| `wiki/tag/tag.md` | `## Notes` |

**Suggested fix:** Update Index Agent to include `## Parent`, `## Files with this tag` (Tầng 3), and `## Notes` (Tầng 2) sections in generated tag index files. Fix Agent to regenerate these 25 files with the missing sections.

### 2. Source slug exceeds 50 characters (1 ERROR)

**Severity:** ERROR
**Category:** Naming
**File:** `wiki/sources/src_how-to-get-maximum-results-with-minimum-effort-game-theory.md`
**Issue:** Slug is 58 characters, exceeds the 50-character limit defined in format-spec.md §3.1
**Current:** `src_how-to-get-maximum-results-with-minimum-effort-game-theory`
**Expected:** Slug ≤ 50 chars (e.g., `src_how-to-get-max-results-min-effort-game-theory` or `src_max-results-min-effort-game-theory`)
**Suggested fix:** Rename file to a shorter slug. Requires updating all backlinks in concepts that reference this source.

---

## WARNINGs (427)

### 3. Broken wikilinks — individual (407 WARNINGs)

**Severity:** WARNING
**Category:** Markdown
**Description:** 407 individual broken wikilinks across concepts and sources. These are links to targets that do not exist as concept files, source files, or raw files.

**Top 20 broken targets (by frequency):**

| Target | Count | Notes |
|---|---|---|
| `[[game-theory]]` | 10 | Uncompiled concept |
| `[[src_agent-memory-7-types-substack.md]]` | 8 | Source not ingested/compiled |
| `[[confirmation-bias]]` | 8 | Uncompiled concept |
| `[[src_you-just-hired-a-million-bad-employees-a16z.md]]` | 5 | Source not ingested/compiled |
| `[[src_the-let-them-theory-gabriel-reality.md]]` | 5 | Source not ingested/compiled |
| `[[ai-coding-agents]]` | 5 | Uncompiled concept |
| `[[src_how-to-remember-everything-you-read-dan-koe.md]]` | 5 | Source not ingested/compiled |
| `[[career-design]]` | 5 | Uncompiled concept |
| `[[decision-making]]` | 5 | Uncompiled concept |
| `[[deep-work]]` | 4 | Uncompiled concept |
| `[[src_cuoc-ua-xem-ai-khong-i-lui-curiositypocket.md]]` | 4 | Source not ingested/compiled |
| `[[src_introducing-backsearch-gr-inc.md]]` | 3 | Source not ingested/compiled |
| `[[src_monid-ai-agent-tool-platform.md]]` | 3 | Source not ingested/compiled |
| `[[attention-economy]]` | 3 | Uncompiled concept |
| `[[ai-hype-vs-reality]]` | 3 | Uncompiled concept |
| `[[economic-inequality]]` | 3 | Uncompiled concept |
| `[[critical-thinking]]` | 3 | Uncompiled concept |
| `[[naval-ravikant]]` | 3 | Uncompiled concept |
| `[[risk-parity]]` | 3 | Uncompiled concept |
| `[[second-law-of-thermodynamics]]` | 3 | Uncompiled concept |

**276 unique broken targets** across 407 instances. Majority are forward-references to concepts not yet compiled or sources not yet ingested.

**Top 10 files by warning count:**

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

**Suggested fix:** These are forward-references to uncompiled concepts and uningested sources. Fix Agent should compile the missing concepts and ingest the missing sources. Alternatively, if these are genuinely not planned, the wikilinks should be removed from the referencing files.

### 4. Broken wikilinks — forward-reference summary groups (20 WARNINGs)

**Severity:** WARNING
**Category:** Markdown
**Description:** 20 files have groups of broken wikilinks summarized as forward-reference batches. These are files where all broken links point to the same category of missing content (uncompiled concepts or uningested sources).

**Affected files:**

| File | Broken links |
|---|---|
| `wiki/sources/src_thought-experiment.md` | 9 |
| `wiki/sources/src_mental-models-of-art.md` | 9 |
| `wiki/sources/src_mental-models-of-economics.md` | 9 |
| `wiki/sources/src_fs-blog-mental-models.md` | 7 |
| `wiki/sources/src_farnam-street-mental-models-biology-series.md` | 6 |
| `wiki/sources/src_farnam-street-mental-models-systems-thinking.md` | 6 |
| `wiki/sources/src_code-as-agent-harness-arxiv-2605-18747.md` | 6 |
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

**Suggested fix:** These are all forward-references to concepts not yet compiled. Fix Agent should compile the referenced concepts when the source material is available.

---

## Verification

- [x] Validated 921 files (524 concepts + 168 sources + 34 indexes + 195 topics)
- [x] 0 files with parse errors
- [x] ERRORs: 50 (49 tag section + 1 naming)
- [x] WARNINGs: 427 (407 individual + 20 forward-reference groups)
- [x] INFOs: 0
- [x] Report written to `wiki/reviews/2026-08-11_format-report.md`
- [x] Delta compared against 2026-08-10 (approved) baseline

## Escalations

### [SYSTEMATIC VIOLATION] — 24 tag files missing sections after Index Agent regeneration

**Pattern:** 24 tag files at `wiki/tag/*.md` are missing `## Parent` and `## Files with this tag` sections. `wiki/tag/tag.md` is missing `## Notes`. All 25 files have `auto_generated: true` and `last_updated: 2026-08-11`, indicating they were regenerated by Index Agent today.

**Likely cause:** Index Agent's SKILL.md does not include these sections in its output template. The previous versions (which had these sections) were overwritten.

**Recommendation:** Update `.openclaw/skills/index-agent/SKILL.md` to include `## Parent`, `## Files with this tag`, and `## Notes` sections in the tag index generation template.