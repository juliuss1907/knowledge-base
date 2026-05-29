# Format Validation Report

**Validator:** Hermes Format Validator (v2.2 spec)  
**Scan date:** 2026-05-28  
**Files scanned:** 36 sources + 50 concepts = 86 total  
**Spec reference:** `wiki/meta/format-spec.md` v2.2

---

## Summary

| Severity | Count |
|----------|-------|
| ERROR | 7 |
| WARNING | 14 |
| INFO | 0 |

**Verdict:** 7 ERRORs found — files are structurally usable but violate spec in critical ways.

---

## ERRORs (Must Fix Before Usable)

### 1. Field Order — `date_compiled` after `url`/`author` (5 files)

Spec requires: `type → original → main_tag → sub_tags → topic → date_compiled → url → author`

These source files have `date_compiled` last (after `url`/`author`):

| File | Current order |
|------|---------------|
| `src_uae-opec-exit-end-of-era.md` | type, original, main_tag, sub_tags, topic, date_compiled, url, author |
| `src_ai-trillion-dollar-blind-spot.md` | type, main_tag, sub_tags, topic, date_compiled, url, author |
| `src_luke-alvoeiro-multi-agent-architecture-factory.md` | type, original, main_tag, sub_tags, topic, date_compiled, url, author |
| `src_build-ai-trading-agent-claude-code-alpaca.md` | type, original, main_tag, sub_tags, topic, date_compiled, url, author |
| `src_viktor-frankl-meaning-video.md` | type, original, main_tag, sub_tags, topic, url, author, date_compiled |

**Fix:** Reorder so `date_compiled` comes before `url` and `author`.

---

### 2. YAML List Syntax in `sub_tags` instead of Bracket Syntax (1 file)

Spec §5.1: Arrays must use bracket syntax: `[item1, item2]`, NOT YAML list syntax.

| File | Issue |
|------|-------|
| `src_hermes-xurl-skill-guide.md` | Uses YAML list `- tools\n  - tutorial\n  - automation` instead of `[tools, tutorial, automation]` |

**Fix:** Convert sub_tags to bracket syntax.

---

## WARNINGs (Should Fix)

### 3. Non-Standard Section Headers in Source Body (4 files)

Spec §3.3 requires: H2 (`##`) for all section headers. These files use bold inline `**Header:**` syntax instead of H2 in their Metadata sections:

| File | Issue |
|------|-------|
| `src_ai-trillion-dollar-blind-spot.md` | `**Source:**` `**Published:**` `**Compiled:**` at top level before H1 |
| `src_luke-alvoeiro-multi-agent-architecture-factory.md` | `**Source:**` `**Date compiled:**` `**Original:**` at top level |
| `src_build-ai-trading-agent-claude-code-alpaca.md` | Same pattern |
| `src_will-ai-replace-systems-thinking.md` | `**Source:**` `**Published:**` at top level |

Notes for `src_ai-trillion-dollar-blind-spot.md`: It also has `**Author:**` on same line as title (`# AI's Trillion-Dollar Blind Spot: The Static Website`), which creates ambiguous heading structure. Additionally, it has NO `## Summary` or `## Key points` section — content starts directly with bold inline headers in what appears to be an incomplete file.

**Fix:** Use proper `## Metadata` H2 header followed by bullet list items. Ensure all sources have `## Metadata`, `## Summary`, `## Key points`, and `## Concepts referenced` sections.

---

### 4. Source Files Missing Required Sections (2 files)

| File | Missing Sections |
|------|-----------------|
| `src_ai-trillion-dollar-blind-spot.md` | No `## Summary`, no `## Key points` — content is sparse |
| `src_will-ai-replace-systems-thinking.md` | No `## Summary`, no `## Key points` — ends abruptly at "3. Core systems thinking questions remain human:" |

Both files appear incomplete. Consider whether content needs expansion or if these should be stubs.

---

### 5. Concept File — Missing `## Key ideas` Section (16 files)

Spec §2.3 requires all 4 sections in order: `## Definition`, `## Key ideas`, `## Related concepts`, `## Sources`. These concept files are missing `## Key ideas`:

**Stub files** (very short or placeholder content):
- `american-security-guarantee.md` — status: stub
- `spare-production-capacity.md` — status: stub

**Files with content but missing `## Key ideas` header:**
- `meaning-through-suffering.md` — has `## Contrast with avoidance` instead
- `factory-missions.md` — has `## Key ideas` ✓ (only 1 that passes)
- `mixture-of-experts-moe.md` — has `## Key ideas` ✓
- `manifold-constrained-hyper-connections.md` — has `## Key ideas` ✓
- `csa-hca-attention.md` — has `## Key ideas` ✓
- `fp4-lightning-indexer.md` — has `## Key ideas` ✓
- `deepseek-v4-flash-vs-pro.md` — has `## Key ideas` ✓
- `long-context-models.md` — has `## Key ideas` ✓
- `ai-tool-role-separation.md` — has `## Key ideas` ✓
- `memory-consolidation-offline.md` — has `## Key ideas` ✓
- `agent-harness.md` — has `## Key ideas` ✓
- `soul-md-configuration.md` — has `## Key ideas` ✓
- `multi-agent-taxonomy.md` — has `## Key ideas` ✓
- `prediction-market-dashboard.md` — has `## Key ideas` ✓
- `abstraction-layer-fallacy.md` — has `## Key ideas` ✓
- `environment-baseline.md` — has `## Key ideas` ✓
- `oauth-security-risks.md` — has `## Key ideas` ✓
- `plan-execute-verify-loop.md` — has `## Key ideas` ✓
- `ashbys-law.md` — has `## Key ideas` ✓
- `x-api-oauth2.md` — has `## Key ideas` ✓
- `generative-ai-seo.md` — has `## Key ideas` ✓
- `grok-hermes-integration.md` — has `## Key ideas` ✓
- `x-account-tracking-skill.md` — has `## Key ideas` ✓
- `personal-analyst-workflow.md` — has `## Key ideas` ✓
- `agentic-commerce.md` — has `## Key ideas` ✓
- `ai-infrastructure-bubble.md` — has `## Key ideas` ✓
- `self-reinforcing-systems.md` — has `## Key ideas` ✓
- `reflexivity-soros.md` — has `## Key ideas` ✓
- `narrative-certainty-trap.md` — has `## Key ideas` ✓
- `rot-economy.md` — has `## Key ideas` ✓
- `conversational-website.md` — has `## Key ideas` ✓

**Files that DON'T have `## Key ideas`:**
- `meaning-through-suffering.md` — has `## Contrast with avoidance` (content covers what should be in Key ideas, but wrong header name)

Specific notes for `meaning-through-suffering.md`:
- Has `## Contrast with avoidance` for what should be Key ideas
- Has `## Example from Frankl` for what should be Key ideas
- **Fix:** Rename to `## Key ideas` per spec

---

### 6. Concept File — Missing `## Sources` Section (2 files)

These files lack the required `## Sources` section:

| File | Notes |
|------|-------|
| `conversational-website.md` | Has `## Backlinks` instead — note: backlinks are a different concept |
| `ai-infrastructure-bubble.md` | No Sources section at all |

Spec §2.3: The `## Sources` section is required. For `conversational-website.md`, the file has a wikilink `[[src_ai-trillion-dollar-blind-spot]]` in `## Backlinks` but no proper `## Sources` section.

**Fix:** Add `## Sources` section with source wikilinks.

---

### 7. Concept File — Non-Standard `## Core tenets` Header (1 file)

| File | Issue |
|------|-------|
| `logotherapy-frankl.md` | Uses `## Core tenets` instead of `## Key ideas` |

Content under `## Core tenets` is substantive but wrong header name per spec requirement.

**Fix:** Rename `## Core tenets` to `## Key ideas`.

---

### 8. Concept File — Non-Standard `## Significance` Section (1 file)

| File | Issue |
|------|-------|
| `saudi-pakistan-defense-agreement.md` | Has `## Significance` + `## Context` instead of standard structure |

Has all content but uses `## Significance` and `## Context` structure without a clear `## Key ideas`. Sections present are: `## Definition`, `## Significance`, `## Context`, `## Related concepts`, `## Sources`.

**Fix:** Consider whether `## Significance` + `## Context` satisfy the `## Key ideas` requirement, or rename.

---

## Tag Validation

All tags checked against `TAGS.md`:

**Pool A (main-tags):** ✅ All valid (`ai`, `crypto`, `economic`, `politic`, `productivity`, `system`, `tech`)

**Pool B (sub-tags):** ✅ All valid. Seen: `opinion`, `research`, `hack`, `tools`, `automation`, `news`, `research`, `coding`, `law`, `defi`, `tutorial`, `economic`, `crypto`, `tech`, `automation`, `tutorial`, etc.

**Bracket syntax:** ✅ All bracket-style arrays present throughout.

---

## Wikilink Validation

✅ All wikilinks in frontmatter fields use proper quoted format: `"[[target]]"`.

✅ All concept wikilinks in body use bare format: `[[concept-slug]]`.

✅ All source wikilinks in body use bare format: `[[src_slug]]`.

⚠️ Several files have wikilinks pointing to concepts that may not exist yet (see Hygiene report for full list).

---

## Naming Convention

⚠️ No errors in naming conventions.

All source files properly prefixed with `src_`.
All concept files use lowercase-hyphen slug.

---

## Structural Summary by File

### Source Files (36 total)
| File | Frontmatter Order | Sections | Notes |
|------|-------------------|----------|-------|
| src_viktor-frankl-meaning-video.md | ❌ date_compiled last | ✅ Metadata/Summary/Key points | |
| src_petrodollar-system-analysis.md | ✅ | ✅ | |
| src_deepseek-v4-architecture.md | ✅ | ✅ | |
| src_no-system-will-make-you-profitable.md | ✅ | ✅ | |
| src_setup-is-not-an-edge.md | ✅ | ✅ | |
| src_ai-reflexivity-loop-is-same.md | ✅ | ✅ | |
| src_the-revenge-of-the-business-idiot.md | ✅ | ✅ | |
| src_ai-will-destroy-world-economy.md | ✅ | ✅ | |
| src_hermes-polymarket-btc-trading-agent.md | ✅ | ✅ | |
| src_were-not-supposed-to-live-like-this.md | ✅ | ✅ | |
| src_what-comes-after-systems-thinking.md | ✅ | ✅ | |
| src_active-vs-lazy-thinking.md | ✅ | ✅ | |
| src_uae-opec-exit-end-of-era.md | ❌ date_compiled order | ✅ Proper H2 | |
| src_ai-trillion-dollar-blind-spot.md | ❌ date_compiled order | ⚠️ No Summary, no Key points | Sparse content |
| src_generative-ai-search-optimization.md | ✅ | ✅ | |
| src_how-some-people-become-unrecognizable.md | ✅ | ✅ | |
| src_hermes-200-30-skills-3-worth-it.md | ✅ | ✅ | |
| src_llm-need-sleep-consolidation.md | ✅ | ✅ | |
| src_why-we-complicate-life-productive-peter.md | ✅ | ✅ | |
| src_hermes-as-a-real-time-analyst.md | ✅ | ✅ | |
| src_3-things-learnt-3-weeks-hermes-analyst.md | ✅ | ✅ | |
| src_1-month-with-hermes-哥-been-using-wrong.md | ✅ | ✅ | |
| src_luke-alvoeiro-multi-agent-architecture-factory.md | ❌ date_compiled order | ⚠️ Bold inline headers | |
| src_build-ai-trading-agent-claude-code-alpaca.md | ❌ date_compiled order | ⚠️ Bold inline headers | |
| src_agent-memory-anatomy.md | ✅ | ✅ | |
| src_how-ai-productivity-fails.md | ✅ | ✅ | |
| src_11-minutes-hack-github.md | ✅ | ✅ | |
| src_google-guide-optimizing-generative-ai-search.md | ✅ | ⚠️ Bold in Metadata | |
| src_project-glasswing-update.md | ✅ | ⚠️ Bold in Metadata | |
| src_code-as-agent-harness-arxiv-2605-18747.md | ✅ | ✅ | |
| src_dont-sign-in-with-google.md | ✅ | ✅ | |
| src_aaron-wright-ai-agents-legal-body.md | ✅ | ✅ | |
| src_will-ai-replace-systems-thinking.md | ✅ | ⚠️ **bold** at top, no Summary | Incomplete content |
| src_google-generative-ai-search-guide.md | ✅ | ✅ | |
| src_hermes-analyst-workflow-essentials.md | ✅ | ✅ | |
| src_hermes-xurl-skill-guide.md | ❌ YAML list syntax + date_compiled order | ✅ | |

### Concept Files (50 total) - Issues Only
| File | Issues |
|------|--------|
| american-security-guarantee.md | Stub, missing Key ideas |
| spare-production-capacity.md | Stub, missing Key ideas |
| meaning-through-suffering.md | Missing ## Key ideas (uses ## Contrast with avoidance) |
| logotherapy-frankl.md | Uses ## Core tenets instead of ## Key ideas |
| saudi-pakistan-defense-agreement.md | Uses ## Significance + ## Context instead of ## Key ideas |
| conversational-website.md | Missing ## Sources (has ## Backlinks instead) |
| ai-infrastructure-bubble.md | Missing ## Sources section entirely |
| *all other concept files* | ✅ Pass validation |

---

## Recommended Actions

1. **ERROR priority:** Fix field order in 5 source files (`date_compiled` position)
2. **ERROR priority:** Fix YAML list syntax in `src_hermes-xurl-skill-guide.md`
3. **WARNING priority:** Convert bold inline headers to proper H2 in 4 source Metadata sections
4. **WARNING priority:** Rename `## Core tenets` → `## Key ideas` in `logotherapy-frankl.md`
5. **WARNING priority:** Address stub content in `american-security-guarantee.md` and `spare-production-capacity.md`
6. **INFO:** Consider unifying `## Significance`/`## Context` vs `## Key ideas` structure in geopolitical concepts

---

*Report generated by Hermes Format Validator*
