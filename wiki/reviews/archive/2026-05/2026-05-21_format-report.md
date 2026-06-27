# Format Validation — 2026-05-21

**Status:** pending
**Issues found:** 20 (3 ERROR, 17 WARNING, 0 INFO)
**Files checked:** 95 (78 concepts + 17 sources)
**Created:** 2026-05-21 23:15:00
**Validator:** format-validator

---

## Issue 1: Invalid sub_tag — `economic` is Pool A (main-tag), not Pool B

**File:** wiki/concepts/ai-white-collar-automation.md
**Severity:** ERROR
**Category:** Frontmatter
**Issue:** `sub_tags: [economic, opinion]` — `economic` is a Pool A main-tag, not a Pool B sub-tag. The file already has `main_tag: ai`, so `economic` cannot be used as a sub-tag. The Compile Agent misclassified it.
**Current:** `sub_tags: [economic, opinion]`
**Expected:** Replace `economic` with a valid Pool B tag (e.g., `research` or `news` for economic analysis content)
**Suggested fix:** Change `economic` to `research` (the content analyzes a forecast/discussion) → `sub_tags: [research, opinion]`

---

## Issue 2: Invalid sub_tag — `economic` is Pool A (main-tag), not Pool B

**File:** wiki/sources/src_ai-will-destroy-world-economy.md
**Severity:** ERROR
**Category:** Frontmatter
**Issue:** `sub_tags: [economic, opinion]` — same misclassification as Issue 1. `economic` is Pool A only. The source is a social media post with commentary.
**Current:** `sub_tags: [economic, opinion]`
**Expected:** Replace `economic` with a valid Pool B tag
**Suggested fix:** Change `economic` to `news` (it's a reaction to current events) → `sub_tags: [news, opinion]`

---

## Issue 3: Code block missing language tag

**File:** wiki/concepts/x-search-tool.md
**Severity:** ERROR
**Category:** Markdown
**Issue:** A fenced code block (` ``` `) has no language tag specified. format-spec.md §4.2 requires all code blocks to specify a language.
**Current:** ` ``` ` (bare)
**Expected:** ` ```yaml `, ` ```python `, etc.
**Suggested fix:** Identify the code block content and add the appropriate language tag (likely `yaml` or `bash`)

---

## Issue 4: Section case — "Key Ideas" should be "Key ideas"

**File:** wiki/concepts/agency-law.md
**Severity:** WARNING
**Category:** Sections
**Issue:** Section header is `## Key Ideas` (capital I), but format-spec.md §2.3 specifies `## Key ideas` (lowercase i).
**Current:** `## Key Ideas`
**Expected:** `## Key ideas`
**Suggested fix:** Change `## Key Ideas` → `## Key ideas`

---

## Issue 5: Section case — "Related Concepts" should be "Related concepts"

**File:** wiki/concepts/agency-law.md
**Severity:** WARNING
**Category:** Sections
**Issue:** Section header is `## Related Concepts` (capital C), but format-spec.md §2.3 specifies `## Related concepts` (lowercase c).
**Current:** `## Related Concepts`
**Expected:** `## Related concepts`
**Suggested fix:** Change `## Related Concepts` → `## Related concepts`

---

## Issue 6: Section case — "Key Ideas" should be "Key ideas"

**File:** wiki/concepts/agentic-commerce.md
**Severity:** WARNING
**Category:** Sections
**Issue:** Same as Issue 4 — `## Key Ideas` uses uppercase I.
**Current:** `## Key Ideas`
**Expected:** `## Key ideas`
**Suggested fix:** Change `## Key Ideas` → `## Key ideas`

---

## Issue 7: Section case — "Related Concepts" should be "Related concepts"

**File:** wiki/concepts/agentic-commerce.md
**Severity:** WARNING
**Category:** Sections
**Issue:** Same as Issue 5 — `## Related Concepts` uses uppercase C.
**Current:** `## Related Concepts`
**Expected:** `## Related concepts`
**Suggested fix:** Change `## Related Concepts` → `## Related concepts`

---

## Issue 8: Section case — "Key Ideas" should be "Key ideas"

**File:** wiki/concepts/ai-legal-personhood.md
**Severity:** WARNING
**Category:** Sections
**Issue:** Same pattern — `## Key Ideas` should be `## Key ideas`.
**Current:** `## Key Ideas`
**Expected:** `## Key ideas`
**Suggested fix:** Change `## Key Ideas` → `## Key ideas`

---

## Issue 9: Section case — "Related Concepts" should be "Related concepts"

**File:** wiki/concepts/ai-legal-personhood.md
**Severity:** WARNING
**Category:** Sections
**Issue:** Same pattern — `## Related Concepts` should be `## Related concepts`.
**Current:** `## Related Concepts`
**Expected:** `## Related concepts`
**Suggested fix:** Change `## Related Concepts` → `## Related concepts`

---

## Issue 10: Section case — "Key Ideas" should be "Key ideas"

**File:** wiki/concepts/zero-member-llc.md
**Severity:** WARNING
**Category:** Sections
**Issue:** Same pattern — `## Key Ideas` should be `## Key ideas`.
**Current:** `## Key Ideas`
**Expected:** `## Key ideas`
**Suggested fix:** Change `## Key Ideas` → `## Key ideas`

---

## Issue 11: Section case — "Related Concepts" should be "Related concepts"

**File:** wiki/concepts/zero-member-llc.md
**Severity:** WARNING
**Category:** Sections
**Issue:** Same pattern — `## Related Concepts` should be `## Related concepts`.
**Current:** `## Related Concepts`
**Expected:** `## Related concepts`
**Suggested fix:** Change `## Related Concepts` → `## Related concepts`

---

## Issue 12: Deprecated `date_ingested` field still present

**File:** wiki/sources/src_11-minutes-hack-github.md
**Severity:** WARNING
**Category:** Frontmatter
**Issue:** File contains `date_ingested: 2026-05-20` alongside `date_compiled: 2026-05-21`. format-spec.md v2.0 replaced `date_ingested` with `date_compiled` — the old field is deprecated. This source file also wraps `original` in wikilink brackets (see Issue 14).
**Current:** Both `date_ingested` and `date_compiled` present
**Expected:** Only `date_compiled: 2026-05-21`
**Suggested fix:** Remove `date_ingested` line, keep `date_compiled`

---

## Issue 13: `original` field uses wikilink syntax — use bare path

**File:** wiki/sources/src_1-month-with-hermes-ive-been-using-wrong.md
**Severity:** WARNING
**Category:** Frontmatter
**Issue:** `original: [[2026-05-18_1-month-with-hermes-ive-been-using-wrong]]` wraps the path in wikilink brackets. format-spec.md §3.2 specifies `original` should be a bare path string. The target file exists but the format is non-standard.
**Current:** `original: "[[2026-05-18_1-month-with-hermes-ive-been-using-wrong]]"`
**Expected:** `original: raw/articles/2026-05-18_1-month-with-hermes-ive-been-using-wrong.md`

---

## Issue 14: `original` field uses wikilink syntax — use bare path

**File:** wiki/sources/src_11-minutes-hack-github.md
**Severity:** WARNING
**Category:** Frontmatter
**Issue:** `original: "[[raw/posts/2026-05-20_the-smart-ape-11-minutes-hack-github.md]]"` wraps path in wikilink brackets.
**Current:** `original: "[[raw/posts/2026-05-20_the-smart-ape-11-minutes-hack-github.md]]"`
**Expected:** `original: raw/posts/2026-05-20_the-smart-ape-11-minutes-hack-github.md`

---

## Issue 15: `original` field uses wikilink syntax — use bare path

**File:** wiki/sources/src_ai-will-destroy-world-economy.md
**Severity:** WARNING
**Category:** Frontmatter
**Issue:** `original: "[[raw/posts/2026-05-20_the-smart-ape-ai-destroy-world-economy.md]]"`
**Current:** Wikilink-wrapped path
**Expected:** Bare path: `raw/posts/2026-05-20_the-smart-ape-ai-destroy-world-economy.md`

---

## Issue 16: `original` field uses wikilink syntax — use bare path

**File:** wiki/sources/src_dont-sign-in-with-google.md
**Severity:** WARNING
**Category:** Frontmatter
**Issue:** `original: "[[raw/posts/2026-05-19_dont-sign-in-with-google.md]]"`
**Current:** Wikilink-wrapped path
**Expected:** Bare path: `raw/posts/2026-05-19_dont-sign-in-with-google.md`

---

## Issue 17: `original` field uses wikilink syntax — use bare path

**File:** wiki/sources/src_hermes-polymarket-btc-trading-agent.md
**Severity:** WARNING
**Category:** Frontmatter
**Issue:** `original: "[[raw/posts/2026-05-20_0xmovez-hermes-polymarket-btc-trading-agent.md]]"`
**Current:** Wikilink-wrapped path
**Expected:** Bare path: `raw/posts/2026-05-20_0xmovez-hermes-polymarket-btc-trading-agent.md`

---

## Issue 18: `original` field uses wikilink syntax — use bare path

**File:** wiki/sources/src_hermes-xurl-skill-guide.md
**Severity:** WARNING
**Category:** Frontmatter
**Issue:** `original: "[[raw/posts/2026-05-20_xdevelopers-hermes-xurl-skill-guide.md]]"`
**Current:** Wikilink-wrapped path
**Expected:** Bare path: `raw/posts/2026-05-20_xdevelopers-hermes-xurl-skill-guide.md`

---

## Issue 19: `original` field uses wikilink syntax — use bare path

**File:** wiki/sources/src_were-not-supposed-to-live-like-this.md
**Severity:** WARNING
**Category:** Frontmatter
**Issue:** `original: "[[raw/articles/2026-05-20_juliachristina-were-not-supposed-to-live-like-this.md]]"`
**Current:** Wikilink-wrapped path
**Expected:** Bare path: `raw/articles/2026-05-20_juliachristina-were-not-supposed-to-live-like-this.md`

---

## Issue 20: Section case — "Key Points" should be "Key points" and "Concepts Referenced" should be "Concepts referenced"

**File:** wiki/sources/src_aaron-wright-ai-agents-legal-body.md
**Severity:** WARNING
**Category:** Sections
**Issue:** Section headers use title case instead of sentence case: `## Key Points` and `## Concepts Referenced`. format-spec.md §3.3 specifies `## Key points` and `## Concepts referenced`.
**Current:** `## Key Points` + `## Concepts Referenced`
**Expected:** `## Key points` + `## Concepts referenced`
**Suggested fix:** Change both headers to sentence case

---

## Systemic Note

**Pattern: 4 concept files share identical section case issues** (`Key Ideas` → `Key ideas`, `Related Concepts` → `Related concepts`). These 4 files (`agency-law`, `agentic-commerce`, `ai-legal-personhood`, `zero-member-llc`) were all compiled from the same source (`src_aaron-wright-ai-agents-legal-body`) — likely a single Compile Agent run. The Compile Agent skill should be updated to enforce sentence case for section headers.

**Pattern: 7 source files use wikilink syntax in the `original` field.** All 7 were compiled recently (2026-05-19 to 2026-05-21). The Compile Agent skill should specify bare paths for the `original` field.

**Pattern: 9 source files retain deprecated `date_ingested` field.** format-spec.md v2.0 (2026-05-09) replaced this with `date_compiled`, but Compile Agent still emits both. Update compile-agent/SKILL.md to stop emitting `date_ingested`.

**Index files:** All 14 `wiki/tag/*.md` (Tầng 3), index files (`raw/raw.md`, `wiki/wiki.md`, `context/context.md`, `raw/articles/articles.md`, `raw/posts/posts.md`, `wiki/tag/tag.md`) pass format compliance — no issues found.

**Slug validation:** All 78 concept slugs and 17 source slugs pass length and character checks. No uppercase detected in any slug.
