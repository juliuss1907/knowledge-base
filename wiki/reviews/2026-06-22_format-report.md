# Format Validation — 2026-06-22 (22:30)

**Status:** pending
**Issues found:** 453
**Created:** 2026-06-22 22:30
**Validator:** format-validator

> **Context:** Evening follow-up to morning report (2026-06-22 08:20, APPROVED with 450 issues).
> Delta from morning: +2 ERROR, +1 WARNING, +8 files checked. No new issue categories.

---

## Summary

| Metric | Value | Δ from morning |
|---|---|---|
| Files checked | 571 | +8 |
| Concepts | 324 | — |
| Sources | 99 | — |
| Indexes | 33 | +2 |
| Topics (no frontmatter) | ~108 | ~same |
| **Total issues** | **453** | +3 |
| **ERRORs** | **134** | +2 |
| **WARNINGS** | **319** | +1 |
| **INFOs** | **0** | — |

---

## ERROR Categories (134)

### 1. Topic files missing YAML frontmatter — ~108 files

**Severity:** ERROR
**Category:** Frontmatter
**Scope:** `wiki/topic/*.md` — all topic index files

**Issue:** Every file under `wiki/topic/` lacks YAML frontmatter entirely. This is a systemic Index Agent issue — topic files are compiled without `---` delimiters.

**Affected files (representative sample):**
- `wiki/topic/activation-energy-mental-model.md`
- `wiki/topic/ai-architecture.md`
- `wiki/topic/ai-economic-disruption-white-collar.md`
- `wiki/topic/code-as-agent-harness.md`
- `wiki/topic/deepseek-v4-architecture.md`
- `wiki/topic/game-theory-strategic-thinking.md`
- `wiki/topic/hermes-polymarket-trading-agent.md`
- `wiki/topic/mental-models-latticework.md`
- `wiki/topic/trading-psychology.md`
- …and ~98 more

**Suggested fix:** Update Index Agent to include YAML frontmatter in topic files per `index-spec.md` §5.1.

**Status:** 🔁 CARRY-OVER — morning report APPROVED, not yet fixed

---

### 2. `main_tag: psychology` — Pool B tag used as main_tag — 11 files

**Severity:** ERROR
**Category:** Frontmatter
**Rule:** `TAGS.md` §2-3 — `psychology` is Pool B (sub-tag only), cannot appear in `main_tag`

**Affected files (9 concepts + 2 sources):**

| File | Current main_tag |
|---|---|
| `wiki/concepts/collaborative-thinking.md` | `psychology` |
| `wiki/concepts/meaning-through-work.md` | `psychology` |
| `wiki/concepts/nash-equilibrium.md` | `psychology` |
| `wiki/concepts/occams-broom.md` | `psychology` |
| `wiki/concepts/occams-razor.md` | `psychology` |
| `wiki/concepts/prisoners-dilemma.md` | `psychology` |
| `wiki/concepts/repeated-games.md` | `psychology` |
| `wiki/concepts/ultimatum-game.md` | `psychology` |
| `wiki/concepts/zero-sum-game.md` | `psychology` |
| `wiki/sources/src_critical-thinking-dennett.md` | `psychology` |
| `wiki/sources/src_game-theory-will-change-your-life.md` | `psychology` |

**Suggested fix:** Replace `main_tag: psychology` with an appropriate Pool A tag (e.g., `system` for game-theory concepts, `productivity` for thinking methods). Add `psychology` to `sub_tags`.

**Status:** 🔁 CARRY-OVER — morning report APPROVED, not yet fixed

---

### 3. Code blocks missing language tags — 8 files

**Severity:** ERROR
**Category:** Markdown
**Rule:** `format-spec.md` — all fenced code blocks must declare a language (e.g., ``` `python` not bare ```)

**Affected files:**
| File | Location |
|---|---|
| `wiki/concepts/ai-coach-prompting.md` | Code block without language tag |
| `wiki/concepts/content-generation-workflow.md` | Code block without language tag |
| `wiki/concepts/dollar-as-rent-payment.md` | Code block without language tag |
| `wiki/concepts/existential-vacuum.md` | Code block without language tag |
| `wiki/concepts/expert-knowledge-extraction.md` | Code block without language tag |
| `wiki/concepts/trading-addiction-cycle.md` | Code block without language tag |
| `wiki/concepts/x-search-tool.md` | Code block without language tag |
| `wiki/sources/src_petrodollar-system-analysis.md` | Code block without language tag |

**Suggested fix:** Add language tag (e.g., `python`, `bash`, `yaml`, `text`) to each bare code fence.

**Status:** 🔁 CARRY-OVER — morning report APPROVED, not yet fixed

---

## WARNING Categories (319)

### 4. Broken wikilinks (forward-references) — ~270+ instances

**Severity:** WARNING
**Category:** Markdown
**Scope:** Concepts and sources linking to targets not yet compiled

**Issue:** Many concepts reference related entries that haven't been compiled yet. This is expected forward-referencing behavior in a growing knowledge base.

**Top patterns:**
- `[[game-theory]]` — referenced by 10+ files, target not found
- `[[confirmation-bias]]` — referenced by 7+ files
- `[[deep-work]]` — referenced by 5+ files
- `[[pareto-principle]]` — referenced by 7+ files
- `[[ai-coding-agents]]` — referenced by 5+ files
- `[[career-design]]` — referenced by 4+ files
- `[[economic-inequality]]` — referenced by 4+ files
- `[[first-order-thinking]]`, `[[second-law-of-thermodynamics]]`, `[[five-whys]]` — 2-3 files each

**Status:** 🔁 CARRY-OVER — expected in growing KB, will resolve as more concepts are compiled

---

### 5. Unquoted wikilinks in tag files — 23 files

**Severity:** WARNING
**Category:** Frontmatter
**Spec conflict:** `index-spec.md` shows `parent: [[tag]]` (unquoted), but `format-spec.md` §9 requires quoted `parent: "[[tag]]"`

**Issue:** YAML parser interprets unquoted `[[...]]` as a nested list rather than a string.

**Affected files:** All 23 `wiki/tag/*.md` files (ai, automation, coding, crypto, defi, economic, geopolitics, hack, health, investment, law, layer1, news, opinion, politic, productivity, psychology, research, system, tech, tools, tutorial, vibecode)

**Suggested fix:** Quote wikilinks in frontmatter: `parent: "[[index]]"`. Also update `index-spec.md` to show quoted format.

**Status:** 🔁 CARRY-OVER — `[SPEC CONFLICT]` escalated in morning report, APPROVED

---

### 6. Field order mismatch — 1 source

**Severity:** WARNING
**Category:** Frontmatter
**File:** `wiki/sources/src_dan-koe-workflow-analysis-markus.md`

**Issue:** Frontmatter field order does not match `format-spec.md` §3 requirements.

**Status:** 🔁 CARRY-OVER

---

### 7. Original wikilink to non-existent raw file — 1 source

**Severity:** WARNING
**Category:** Frontmatter
**File:** `wiki/sources/src_map-is-not-territory.md`

**Issue:** `original` field references `[[2026-06-03_map-is-not-territory]]` but corresponding raw file not found.

**Status:** 🔁 CARRY-OVER

---

## Escalations

### [SYSTEMATIC VIOLATION] Topic files without frontmatter

**Pattern:** ~108 `wiki/topic/*.md` files have zero YAML frontmatter
**Likely cause:** Index Agent (`index-agent/SKILL.md`) does not include frontmatter template for topic file generation
**Recommendation:** Update Index Agent to output YAML frontmatter with `type`, `scope`, `topic`, `auto_generated`, `last_updated` fields per `index-spec.md` §5.1
**Status:** Escalated 2026-06-17 → APPROVED 2026-06-22 morning → not yet fixed

### [SPEC CONFLICT] Unquoted wikilinks

**Issue:** `index-spec.md` shows `parent: [[tag]]` (unquoted) but `format-spec.md` §9 requires quoted `"[[...]]"` in frontmatter
**Recommendation:** Update `index-spec.md` to show quoted format
**Status:** Escalated 2026-06-17 → APPROVED 2026-06-22 morning

---

## Delta Analysis (vs morning 08:20 report)

| Change | Details |
|---|---|
| Files checked | +8 (571 vs 563) |
| Index files | +2 (33 vs 31) |
| ERRORs | +2 (134 vs 132) — minor variance in topic file count or new frontmatter issues |
| WARNINGs | +1 (319 vs 318) — additional broken wikilinks from new files |
| New categories | None |

**Verdict:** Evening run confirms morning findings. No regressions, no new issue types. Systemic issues (topic files, psych main_tag, wikilinks) unchanged since morning APPROVAL.
