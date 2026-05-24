# Format Validation — 2026-05-24

**Status:** pending
**Issues found:** 5 substantive (2 ERROR, 3 WARNING) + 75 INFO (systematic)
**Created:** 2026-05-24 08:30:00
**Validator:** format-validator

---

## Summary

| Metric | Count |
|---|---|
| Files checked | 114 (22 sources + 92 concepts) |
| Total issues | 80 (2 ERROR, 3 WARNING, 75 INFO) |
| ERRORs | 2 |
| WARNINGs | 3 |
| INFOs | 75 (systematic: full-path wikilinks) |

**Key finding:** 75 concepts use full `wiki/sources/` paths in the `sources` field instead of bare slugs. This is a systematic issue from the Compile Agent. Additionally, 2 concepts have `sources` as a string instead of YAML array.

---

## Issue 1: `sources` field is string, not array

**File:** wiki/concepts/active-thinking.md
**Severity:** ERROR
**Category:** Frontmatter
**Issue:** `sources` field is a quoted string instead of YAML array
**Current:** `sources: "[[src_active-vs-lazy-thinking]]"`
**Expected:** Multi-line YAML list:
```yaml
sources:
  - [[src_active-vs-lazy-thinking]]
```
**Suggested fix:** Convert `sources` to multi-line YAML array format

---

## Issue 2: `sources` field is string, not array

**File:** wiki/concepts/evolutionary-mismatch.md
**Severity:** ERROR
**Category:** Frontmatter
**Issue:** `sources` field is a quoted string instead of YAML array
**Current:** `sources: "[[src_were-not-supposed-to-live-like-this.md]]"`
**Expected:** Multi-line YAML list:
```yaml
sources:
  - [[src_were-not-supposed-to-live-like-this]]
```
**Suggested fix:** Convert `sources` to multi-line YAML array format; also strip `.md` from wikilink

---

## Issue 3: Field order incorrect

**File:** wiki/sources/src_how-ai-productivity-fails.md
**Severity:** WARNING
**Category:** Frontmatter
**Issue:** Field order does not match format-spec.md §3.2
**Current:** `type → original → main_tag → sub_tags → topic → author → url → date_compiled`
**Expected:** `type → original → main_tag → sub_tags → topic → date_compiled → url → author`
**Suggested fix:** Move `date_compiled` before `url` and `author`

---

## Issue 4: Field order incorrect

**File:** wiki/sources/src_how-some-people-become-unrecognizable.md
**Severity:** WARNING
**Category:** Frontmatter
**Issue:** Field order does not match format-spec.md §3.2
**Current:** `type → original → main_tag → sub_tags → topic → author → url → date_compiled`
**Expected:** `type → original → main_tag → sub_tags → topic → date_compiled → url → author`
**Suggested fix:** Move `date_compiled` before `url` and `author`

---

## Issue 5: Code block missing language tag

**File:** wiki/concepts/x-search-tool.md
**Severity:** WARNING
**Category:** Markdown
**Issue:** Code block missing language tag (format-spec.md §4.2)
**Current:** ` ``` ` (no language)
**Expected:** ` ```yaml ` or appropriate language tag
**Suggested fix:** Add language tag to code block

---

## Systematic Issue: Full-path wikilinks in `sources` field (75 INFO)

**Pattern:** 75 concept files use full `wiki/sources/` paths in their `sources` frontmatter field instead of bare slugs.

**Likely cause:** Compile Agent writes `[[wiki/sources/src_*.md]]` instead of `[[src_*]]`

**Example affected files (first 10 of 75):**
- `wiki/concepts/agency-law.md` — `[[wiki/sources/src_aaron-wright-ai-agents-legal-body]]` → should be `[[src_aaron-wright-ai-agents-legal-body]]`
- `wiki/concepts/agent-harness.md` — `[[wiki/sources/src_code-as-agent-harness-arxiv-2605-18747.md]]` → should be `[[src_code-as-agent-harness-arxiv-2605-18747]]`
- `wiki/concepts/agent-skill-management.md` — `[[wiki/sources/src_hermes-analyst-workflow-essentials]]`
- `wiki/concepts/agentic-commerce.md` — `[[wiki/sources/src_aaron-wright-ai-agents-legal-body]]`
- `wiki/concepts/ai-agent-setup-mistakes.md` — `[[wiki/sources/src_3-things-learnt-3-weeks-hermes-analyst]]`
- `wiki/concepts/ai-legal-personhood.md` — `[[wiki/sources/src_aaron-wright-ai-agents-legal-body]]`
- `wiki/concepts/ai-research-workflow.md` — `[[wiki/sources/src_hermes-as-a-real-time-analyst]]` (2 instances)
- `wiki/concepts/ai-tool-role-separation.md` — `[[wiki/sources/src_1-month-with-hermes-ive-been-using-wrong]]`
- `wiki/concepts/ai-white-collar-automation.md` — `[[wiki/sources/src_ai-will-destroy-world-economy.md]]`
- `wiki/concepts/atomic-mac-agent.md` — `[[wiki/sources/src_hermes-polymarket-btc-trading-agent.md]]`

**Recommendation:** Update Compile Agent skill to use bare slug wikilinks (`[[src_slug]]`) in `sources` field. Some wikilinks also include `.md` extension which should be stripped.

---

## Files with zero issues

20 out of 22 source files and 15 out of 92 concept files are fully format-compliant (no ERROR, WARNING, or INFO). Source files are generally well-formatted; the main issues are in concept files.

---

## Escalations

### Systematic wikilink format
```
[SYSTEMATIC VIOLATION]
Pattern: 75 concept files use full-path wikilinks in sources field
Likely cause: Compile Agent writes [[wiki/sources/src_*.md]] instead of [[src_*]]
Recommendation: Update compile-agent/SKILL.md to use bare slugs with no .md extension
```

### sources-as-string YAML
```
[PATTERN]
Files: wiki/concepts/active-thinking.md, wiki/concepts/evolutionary-mismatch.md
Issue: sources field written as quoted string instead of YAML list
Likely cause: Compile Agent uses inline format for single-source concepts
Fix: Always use multi-line YAML array for sources
```

---

**End of report**
