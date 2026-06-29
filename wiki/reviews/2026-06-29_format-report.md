# Format Validation — 2026-06-29

**Status:** pending
**Issues found:** 386 (69 ERROR, 317 WARNING, 0 INFO)
**Created:** 2026-06-29 23:15:00 +0700
**Validator:** format-validator
**Scope:** Full KB — 628 files (357 concepts + 111 sources + 33 indexes + 127 topics)

---

## Delta from last approved (2026-06-28 23:15)

| Metric | 2026-06-28 (APPROVED) | 2026-06-29 | Delta |
|---|---|---|---|
| Scope | 623 files | 628 files | **+5** |
| ERROR | 127 | 69 | **-58** |
| WARNING | 315 | 317 | +2 |
| INFO | 0 | 0 | 0 |

**Positive delta (issues resolved):**
- ✅ **126 topic-file frontmatter ERROR → GONE** — Fix Agent added YAML frontmatter to all `wiki/topic/*.md` files
- ✅ **1 slug-too-long ERROR → GONE** — `src_give-me-14-minutes-and-ill-destroy-your-procrastination-forever.md` renamed or removed
- ✅ 8 code-block language-tag ERRORs from 06-26 remain resolved (confirmed no regression)

**Negative delta (new issues):**
- 🔴 **69 new ERROR**: `wiki/tag/*.md` — 23 tag index files each missing 3 required sections (`## Parent`, `## Stats`, `## Files with this tag`)
- ⚠️ +2 WARNING: net change in broken wikilinks (5 new files introduced new forward references)

**Files growth:** +5 files since 06-28 (357 concepts + 111 sources today vs 354 concepts + 110 sources on 06-28)

---

## [SYSTEMATIC VIOLATION] Tag index files missing required sections

**Pattern:** 23/23 tag index files under `wiki/tag/` are missing three required section headings per `index-spec.md` §5 (Level 3 index format):

- `## Parent`
- `## Stats`
- `## Files with this tag`

**Likely cause:** Index Agent generates tag files without these sections. Previous validation runs focused on frontmatter fixes (`level: 3` field — resolved in 06-28). Now that frontmatter is compliant, section structure validation surfaces this gap.

**Affected tags (23 files):**
`ai`, `automation`, `coding`, `crypto`, `defi`, `economic`, `geopolitics`, `hack`, `health`, `investment`, `law`, `layer1`, `news`, `opinion`, `politic`, `productivity`, `psychology`, `research`, `system`, `tech`, `tools`, `tutorial`, `vibecode`

**Recommendation:** Update `index-agent/SKILL.md` to include `## Parent`, `## Stats`, and `## Files with this tag` sections in tag index file template.

**Escalation:** `[SYSTEMATIC VIOLATION]` — 23/23 files share the same structural gap. This is a template issue, not individual file errors.

---

## Issue Group 1: Missing required sections in tag index files (69 ERROR)

**Category:** Sections
**Severity:** ERROR
**Count:** 69 (23 files × 3 missing sections)

**Current:** Tag files have `# <tag>` heading and content, but lack `## Parent`, `## Stats`, `## Files with this tag` sections.

**Expected:** Per `index-spec.md` §5, Level 3 tag indexes must include these three H2 sections.

**Files affected (all 23):**

| Tag file | Missing sections |
|---|---|
| `wiki/tag/ai.md` | Parent, Stats, Files with this tag |
| `wiki/tag/automation.md` | Parent, Stats, Files with this tag |
| `wiki/tag/coding.md` | Parent, Stats, Files with this tag |
| `wiki/tag/crypto.md` | Parent, Stats, Files with this tag |
| `wiki/tag/defi.md` | Parent, Stats, Files with this tag |
| `wiki/tag/economic.md` | Parent, Stats, Files with this tag |
| `wiki/tag/geopolitics.md` | Parent, Stats, Files with this tag |
| `wiki/tag/hack.md` | Parent, Stats, Files with this tag |
| `wiki/tag/health.md` | Parent, Stats, Files with this tag |
| `wiki/tag/investment.md` | Parent, Stats, Files with this tag |
| `wiki/tag/law.md` | Parent, Stats, Files with this tag |
| `wiki/tag/layer1.md` | Parent, Stats, Files with this tag |
| `wiki/tag/news.md` | Parent, Stats, Files with this tag |
| `wiki/tag/opinion.md` | Parent, Stats, Files with this tag |
| `wiki/tag/politic.md` | Parent, Stats, Files with this tag |
| `wiki/tag/productivity.md` | Parent, Stats, Files with this tag |
| `wiki/tag/psychology.md` | Parent, Stats, Files with this tag |
| `wiki/tag/research.md` | Parent, Stats, Files with this tag |
| `wiki/tag/system.md` | Parent, Stats, Files with this tag |
| `wiki/tag/tech.md` | Parent, Stats, Files with this tag |
| `wiki/tag/tools.md` | Parent, Stats, Files with this tag |
| `wiki/tag/tutorial.md` | Parent, Stats, Files with this tag |
| `wiki/tag/vibecode.md` | Parent, Stats, Files with this tag |

**Suggested fix:** Add three H2 sections to each tag file:
```markdown
## Parent

[[tag]]

## Stats

- **Files:** N
- **Last updated:** YYYY-MM-DD

## Files with this tag

- [[concept-slug]]
- ...
```

---

## Issue Group 2: Broken wikilinks — 290 forward references (WARNING)

**Category:** Markdown
**Severity:** WARNING
**Count:** 290 individual broken wikilinks + 21 grouped forward-reference summaries

**Total unique broken targets:** 194

**Top 20 most-referenced missing targets:**

| Count | Target |
|---|---|
| 10 | `[[game-theory]]` |
| 8 | `[[confirmation-bias]]` |
| 6 | `[[pareto-principle]]` |
| 5 | `[[ai-coding-agents]]` |
| 5 | `[[career-design]]` |
| 5 | `[[decision-making]]` |
| 4 | `[[deep-work]]` |
| 3 | `[[ai-hype-vs-reality]]` |
| 3 | `[[economic-inequality]]` |
| 3 | `[[critical-thinking]]` |
| 3 | `[[naval-ravikant]]` |
| 3 | `[[risk-parity]]` |
| 3 | `[[second-law-of-thermodynamics]]` |
| 3 | `[[saying-no]]` |
| 3 | `[[power-imbalance]]` |
| 3 | `[[first-order-thinking]]` |
| +178 | other unique targets (each with 1-2 references) |

**Analysis:** These are forward-references to concepts not yet compiled in the KB. This is expected in a growing knowledge base. The top 3 targets (`game-theory`, `confirmation-bias`, `pareto-principle`) would be high-value compile candidates.

**Delta from 06-28:** 194 unique targets (was 194) — stable, no new systemic linking pattern detected. +2 WARNING from 5 new files adding minor forward references.

---

## Issue Group 3: Original raw-file wikilinks not found (6 WARNING)

**Category:** Frontmatter
**Severity:** WARNING

| File | Missing raw reference |
|---|---|
| `wiki/sources/src_code-as-agent-harness-arxiv-2605-18747.md` | `[[2026-05-22_code-as-agent-harness-arxiv-2605-18747]]` |
| `wiki/sources/src_llm-need-sleep-consolidation.md` | `[[2026-05-27_llm-need-sleep-consolidation]]` |
| `wiki/sources/src_personal-mba-generator-skill.md` | `[[2026-06-27_personal-mba-generator-skill]]` |
| `wiki/sources/src_petrodollar-system-analysis.md` | `[[2026-05-28_petrodollar-system-analysis]]` |
| `wiki/sources/src_sop-writer-skill.md` | `[[2026-06-27_sop-writer-skill]]` |
| `wiki/sources/src_thermodynamics.md` | `[[2026-06-04_thermodynamics]]` |

**Analysis:** 6 source files reference raw files that don't exist at the expected path. These may be:
- Raw files ingested but stored under a different `raw/` subdirectory
- Raw files that were renamed after source compilation
- Raw files never ingested

**Suggested fix:** For each, verify the raw file exists under some `raw/<subdir>/` path and update the `original` field, or remove the broken reference.

**Delta from 06-28:** 6 issues (was 4) — `src_personal-mba-generator-skill.md` and `src_sop-writer-skill.md` are new since 06-28.

---

## Passed checks (no issues found)

- ✅ **Frontmatter required fields** — all concept, source, index, and topic files have valid YAML frontmatter with required fields
- ✅ **Field order** — no field order violations detected
- ✅ **YAML syntax** — no parse errors (4 errors from 06-26 batch resolved)
- ✅ **Section structure (concepts/sources)** — all concept and source files have required sections in correct order
- ✅ **Heading levels** — H1 for title, H2 for sections in all content files
- ✅ **Naming conventions** — all filenames comply with slug rules (no files exceed 50-char limit)
- ✅ **Code block language tags** — no missing language tags (8 errors from 06-26 resolved and confirmed)
- ✅ **File placement** — all files in correct folders (concepts in wiki/concepts/, sources in wiki/sources/)
- ✅ **Topic file format** — all 127 topic files now have valid frontmatter (126 frontmatter errors from 06-28 resolved)
- ✅ **Tag file frontmatter** — all 23 tag files have valid YAML with `level: 3` field (23 errors from 06-27 resolved)

---

## Summary

KB format health is improving. Two major systematic issues from prior reports are now fully resolved:
1. **Topic file frontmatter** (126 ERROR, 06-28) → GONE
2. **Code block language tags** (8 ERROR, 06-26) → GONE

The remaining 69 ERROR are a single systematic pattern: tag index files need section structure updated per `index-spec.md` §5. This is a template fix — once Index Agent generates `## Parent`, `## Stats`, and `## Files with this tag` sections, all 69 errors resolve simultaneously.

Broken wikilinks (317 WARNING) remain stable — forward references in a growing KB. No new systemic linking problems detected.

**Recommendation:** Prioritize the tag-file section template fix in `index-agent/SKILL.md` to clear the 69 remaining ERRORs. Broken wikilinks and original references are lower priority.

---

## Escalations

### [SYSTEMATIC VIOLATION] Tag index files missing sections

```
[SYSTEMATIC VIOLATION]
Pattern: 23/23 wiki/tag/*.md files missing ## Parent, ## Stats, ## Files with this tag
Likely cause: Index Agent template does not include these sections
Recommendation: Update index-agent/SKILL.md tag file template to include all required sections per index-spec.md §5
```
