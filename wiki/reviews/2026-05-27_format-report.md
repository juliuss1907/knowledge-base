# Format Report — 2026-05-27

**Validator:** Hermes Format Validator  
**Ground truth:** `wiki/meta/format-spec.md` v2.0 (2026-05-09)  
**Scope:** `wiki/concepts/*.md` (50 files) + `wiki/sources/*.md` (30 files)  
**Severity:** ERROR = blocks compilation | WARNING = should fix | INFO = suggestion  

---

## Summary

| Category | Files Scanned | ERRORS | WARNINGS | INFOs |
|----------|---------------|--------|----------|-------|
| Concepts | 50 | 1 | 2 | ~50 |
| Sources | 30 | 21 | 0 | ~20 |
| **Total** | **80** | **22** | **2** | **~70** |

---

## Concept Files — Issues

### ERRORs

#### 1. `systems-thinking.md` — Malformed sources array (line 9)
**Problem:** `sources:` contains malformed wikilink with trailing `[]`
```yaml
sources:
  - [[src_what-comes-after-systems-thinking]]
  - [[src_will-ai-replace-systems-thinking]] []
```
**Expected:** Valid wikilinks only  
**Fix:** Remove `[]` from second source entry

---

### WARNINGs

#### 2. `active-thinking.md` — Non-standard sub_tags syntax (lines 5-6)
**Problem:** Uses YAML list syntax instead of bracket syntax
```yaml
sub_tags:
  - opinion
```
**Expected:** `sub_tags: [opinion]` (bracket syntax per spec §5.1)  
**Fix:** Convert to bracket syntax

#### 3. `active-thinking.md` — sources is string not array (line 8)
**Problem:** sources is `"[[src_active-vs-lazy-thinking]]"` (string)
**Expected:** sources should be array `[[src_active-vs-lazy-thinking]]` (per spec §2.2)  
**Fix:** Change to array format

#### 4. `validation-contract.md` — Non-standard sub_tags syntax (lines 5-6)
**Problem:** Uses YAML list syntax instead of bracket syntax
```yaml
sub_tags:
  - automation
```
**Expected:** `sub_tags: [automation]` (bracket syntax per spec §5.1)  
**Fix:** Convert to bracket syntax

---

### INFOs (Non-blocking)

#### 5. `## Backlinks` sections (most concept files)
**Observation:** Many concept files have `## Backlinks` sections (e.g., `static-website-blind-spot.md`, `ai-augmented-systems-thinking.md`, `ai-productivity.md`, `conversational-website.md`, `generative-ai-seo.md`, `ai-powered-discovery.md`, `agency-law.md`, `ai-vulnerability-discovery.md`)  
**Spec says:** Only Definition, Key ideas, Related concepts, Sources, Notes  
**Note:** Not an error — Backlinks is practical Obsidian feature but not in spec. Julius may want to update spec to include it.

#### 6. `<!-- Free space for Julius -->` comments
**Observation:** `static-website-blind-spot.md` (line 64), `ai-augmented-systems-thinking.md` (line 59) contain this comment  
**Note:** Not in spec but harmless — could add as optional element in spec

#### 7. `## Opportunity` section in `static-website-blind-spot.md`
**Observation:** Has `## Opportunity` section between Key ideas and Related concepts  
**Spec says:** Order must be Definition → Key ideas → Related concepts → Sources → Notes  
**Note:** Section order deviates from spec

#### 8. `## When to Apply` / `## Limitations` sections in `ai-augmented-systems-thinking.md`
**Observation:** Custom sections between Key ideas and Related concepts  
**Note:** Section order deviates from spec

#### 9. `###` subsections in `agency-law.md` and `zero-member-llc.md`
**Observation:** `agency-law.md` has H3 subsections (Mô hình Principal-Agent, Ưu điểm, Giới hạn, So sánh, Khi nào dùng...)  
**Spec says (§4.1):** Subsections must be H3, no skipping levels — these are correctly H3, so compliant

#### 10. Code blocks
**Observation:** `x-search-tool.md` has YAML code block (lines 38-43) with proper ` ```yaml ` tag  
**Note:** Compliant — code blocks correctly specify language

---

## Source Files — Issues

### ERRORs (21 files)

#### Pattern: `original:` field is path/URL instead of wikilink

The spec (§3.2) requires `original:` to be a wikilink pointing to a raw file:
```yaml
original: [[YYYY-MM-DD_<slug>]]
```

Many sources use either:
- **Raw path:** `original: raw/articles/2026-05-14_how-ai-productivity-fails.md`
- **External URL:** `original: https://open.substack.com/...`
- **Wikilink with `.md`:** `original: [[2026-05-22_luke-alvoeiro...md]]`

Files with path-style `original:` (not wikilink):
| File | Line | `original:` value |
|------|------|-------------------|
| `src_aaron-wright-ai-agents-legal-body.md` | 3 | `raw/articles/2026-05-17_aaron-wright-ai-agents-legal-body.md` |
| `src_how-ai-productivity-fails.md` | 3 | `raw/articles/2026-05-14_how-ai-productivity-fails.md` |
| `src_hermes-as-a-real-time-analyst.md` | 3 | `raw/articles/2026-05-18_hermes-as-a-real-time-analyst.md` |
| `src_1-month-with-hermes-ive-been-using-wrong.md` | 3 | `raw/articles/2026-05-18_1-month-with-hermes-ive-been-using-wrong.md` |
| `src_hermes-analyst-workflow-essentials.md` | 3 | `raw/articles/2026-05-18_hermes-analyst-workflow-essentials.md` |
| `src_hermes-200-30-skills-3-worth-it.md` | 3 | `raw/articles/2026-05-18_hermes-200-30-skills-3-worth-it.md` |
| `src_how-some-people-become-unrecognizable.md` | 3 | `raw/articles/2026-05-14_how-some-people-become-unrecognizable.md` |
| `src_google-guide-optimizing-generative-ai-search.md` | 3 | `raw/articles/2026-05-18_google-guide-optimizing-generative-ai-search.md` |
| `src_were-not-supposed-to-live-like-this.md` | 3 | `raw/articles/2026-05-20_juliachristina-were-not-supposed-to-live-like-this.md` |
| `src_hermes-polymarket-btc-trading-agent.md` | 3 | `raw/posts/2026-05-20_0xmovez-hermes-polymarket-btc-trading-agent.md` |
| `src_hermes-xurl-skill-guide.md` | 3 | `raw/posts/2026-05-20_xdevelopers-hermes-xurl-skill-guide.md` |
| `src_3-things-learnt-3-weeks-hermes-analyst.md` | 3 | `raw/articles/2026-05-18_3-things-learnt-3-weeks-hermes-analyst.md` |
| `src_active-vs-lazy-thinking.md` | 3 | `raw/articles/2026-05-12_active-vs-lazy-thinking.md` |
| `src_what-comes-after-systems-thinking.md` | 3 | `raw/articles/2026-04-02_what-comes-after-systems-thinking.md` |
| `src_dont-sign-in-with-google.md` | 3 | `raw/posts/2026-05-19_dont-sign-in-with-google.md` |
| `src_ai-will-destroy-world-economy.md` | 3 | `raw/posts/2026-05-20_the-smart-ape-ai-destroy-world-economy.md` |
| `src_11-minutes-hack-github.md` | 3 | `raw/posts/2026-05-20_the-smart-ape-11-minutes-hack-github.md` |

Files with URL-style `original:`:
| File | Line | `original:` value |
|------|------|-------------------|
| `src_will-ai-replace-systems-thinking.md` | 3 | `https://open.substack.com/pub/pmresearcher/p/will-ai-replace-systems-thinking` |
| `src_ai-trillion-dollar-blind-spot.md` | 3 | `https://x.com/SuyashKarn2/status/2057099123413946617` |

Files with wikilink containing `.md` extension:
| File | Line | `original:` value |
|------|------|-------------------|
| `src_luke-alvoeiro-multi-agent-architecture-factory.md` | 3 | `[[2026-05-22_luke-alvoeiro-multi-agent-architecture-factory.md]]` |
| `src_code-as-agent-harness-arxiv-2605-18747.md` | 3 | `[[2026-05-22_code-as-agent-harness-arxiv-2605-18747.md]]` |

**Expected format:** `original: [[YYYY-MM-DD_slug]]` (no `.md` extension, no `raw/` prefix)

---

### INFOs (Non-blocking)

#### 11. `## Original excerpts` section (most source files)
**Observation:** Most source files have `## Original excerpts` section (e.g., `src_google-generative-ai-search-guide.md`, `src_hermes-xurl-skill-guide.md`, `src_will-ai-replace-systems-thinking.md`, etc.)  
**Spec says:** Only Metadata, Summary, Key points, Concepts referenced  
**Note:** Not an error — practical for referencing raw content but not in spec. Julius may want to update spec.

#### 12. Non-standard metadata format in some sources
**Observation:** `src_will-ai-replace-systems-thinking.md` and `src_ai-trillion-dollar-blind-spot.md` use inline metadata format:
```markdown
**Source:** PM Researcher (Substack)  
**Published:** 2025-05-24  
```
Instead of structured `## Metadata` section with bullet points  
**Note:** Not in spec but common pattern

---

## Field Order — Compliance

### Concept files (per spec §2.2 field order)
| File | type | status | main_tag | sub_tags | topic | sources | last_updated | Issue |
|------|------|--------|----------|----------|-------|---------|--------------|-------|
| `petrodollar-system.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| `ai-trading-agent.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| `memory-consolidation-offline.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| `llm-sleep.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| `systems-thinking.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | Malformed sources |
| `static-website-blind-spot.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| `ai-augmented-systems-thinking.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| `ai-productivity.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| `human-judgment-ai.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| `generative-ai-seo.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| `conversational-website.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| `ai-powered-discovery.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| `hedonic-treadmill.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| `stoic-control-dichotomy.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| `paradox-of-effort.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| `memory-reconstruction.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| `glymphatic-system.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| `second-order-effects.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| `cynefin-framework.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| `rot-economy.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| `ai-impression-of-work.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| `business-idiot-archetype.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| `prospective-memory-gap.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| `memory-extraction-timing.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| `consolidation-offline-processing.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| `autobiographical-memory-systems.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| `agent-memory-taxonomy.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| `agency-law.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| `ai-vulnerability-discovery.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| `x-bookmark-prioritization.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| `active-thinking.md` | ✅ | ✅ | ✅ | ⚠️ | ✅ | ⚠️ | ✅ | sub_tags YAML list, sources string |
| `zero-member-llc.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| `xurl-cli.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| `x-search-tool.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| `x-api-oauth2.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| `x-account-tracking-skill.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| `vs-code-marketplace-security.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| `validation-contract.md` | ✅ | ✅ | ✅ | ⚠️ | ✅ | ✅ | ✅ | sub_tags YAML list |
| `user-md-configuration.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| `token-theft-attack.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| `team-pcp-hacker-group.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| `taste-holders.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| `systems-thinking-limitations.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| `supply-chain-attack.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| `sso-single-point-of-failure.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| `soul-md-configuration.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| `skill-atrophy.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| `six-stage-research-pipeline.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| `shift-left-testing.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| `hermes-agent.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| `productivity-wage-gap.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| `negative-compounding.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| `hunter-gatherer-lifestyle.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| `information-compression.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| `last30days-skill.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — |

---

## Section Headers — Compliance

### Concept files (per spec §2.3)
**Required order:** Definition → Key ideas → Related concepts → Sources → Notes

Most concept files follow the required order. Common deviations:
- `static-website-blind-spot.md`: Has `## Opportunity` between Key ideas and Related concepts
- `ai-augmented-systems-thinking.md`: Has `## When to Apply` and `## Limitations` between Key ideas and Related concepts
- Many files have `## Backlinks` (not in spec but practical Obsidian feature)
- `x-search-tool.md` has proper H2 sections with a code block

### Source files (per spec §3.3)
**Required order:** Metadata → Summary → Key points → Concepts referenced

Most source files follow this order and include optional `## Original excerpts`. No errors detected.

---

## Wikilinks — Compliance

### Correct wikilink format
- Concepts use `[[concept-slug]]` correctly
- Sources use `[[src_slug]]` correctly
- No spaces around brackets observed

### Issues
- `systems-thinking.md` line 9: Malformed wikilink `[[src_will-ai-replace-systems-thinking]] []`
- Most `original:` fields in sources use raw paths or URLs instead of wikilinks (see ERRORs above)

---

## Code Blocks — Compliance

Only one code block found:
- `x-search-tool.md` lines 38-43: ` ```yaml ` with proper language tag

**Compliant:** Code blocks specify language, use lowercase.

---

## Recommendations

### Must Fix (ERRORs)
1. **Fix `systems-thinking.md` sources array** — remove `[]` from second entry
2. **Update `original:` field in 21 source files** — convert to wikilink format `[[YYYY-MM-DD_slug]]`

### Should Fix (WARNINGs)
3. **Convert `sub_tags` to bracket syntax** in `active-thinking.md` and `validation-contract.md`
4. **Fix `sources` to array format** in `active-thinking.md`

### Consider (INFOs)
5. **Update format-spec.md** to include `## Backlinks` section (if Julius wants to formally support it)
6. **Update format-spec.md** to include `## Original excerpts` section in sources (if Julius wants to formally support it)
7. **Update format-spec.md** to clarify `original:` field format — should it point to raw files (path) or use wikilinks?

---

**Report generated:** 2026-05-28  
**Next action:** OpenClaw Fix Agent (after Julius approves this report)