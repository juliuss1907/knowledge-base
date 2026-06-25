# Format Validation — 2026-06-25

**Status:** approved
**Approved by:** Julius — 2026-06-25 16:03 +07
**Issues found:** 345 in-scope issues (`463` raw script findings minus `118` out-of-scope topic-file false positives)
**Created:** 2026-06-25 15:53
**Validator:** format-validator

> **Context:** Manual re-run on VPS. `TAGS.md` re-read before validation. Current Pool B includes `ai`, `system`, and `geopolitics` as valid sub-tags.
> **Scope note:** Current validator script still scans `wiki/topic/*.md` and reports missing frontmatter there. Per current validation scope, topic files are out of scope for format-spec checks, so those `118` ERRORs are excluded from the actionable count below.

---

## Summary

| Metric | Value |
|---|---:|
| Raw script findings | 463 |
| Raw ERRORs | 126 |
| Raw WARNINGs | 337 |
| Excluded topic-file false positives | 118 ERROR |
| **In-scope ERRORs** | **8** |
| **In-scope WARNINGs** | **337** |
| **In-scope total** | **345** |

---

## ERROR Categories (8)

### 1. Code blocks missing language tags — 8 files

**Severity:** ERROR  
**Category:** Markdown

**Affected files:**
1. `wiki/concepts/ai-coach-prompting.md`
2. `wiki/concepts/content-generation-workflow.md`
3. `wiki/concepts/dollar-as-rent-payment.md`
4. `wiki/concepts/existential-vacuum.md`
5. `wiki/concepts/expert-knowledge-extraction.md`
6. `wiki/concepts/trading-addiction-cycle.md`
7. `wiki/concepts/x-search-tool.md`
8. `wiki/sources/src_petrodollar-system-analysis.md`

**Issue:** Fenced code blocks use bare ``` without language identifier.

**Suggested fix:** Add explicit language tags such as `bash`, `python`, `yaml`, `json`, or `text`.

---

## WARNING Categories (337)

### 2. Broken wikilinks / forward references — 312

**Severity:** WARNING  
**Category:** Markdown

**Issue:** Concepts and sources link to targets not yet compiled. This remains the dominant warning class.

**Representative missing targets with repeated references:**
- `[[game-theory]]`
- `[[confirmation-bias]]`
- `[[decision-making]]`
- `[[pareto-principle]]`
- `[[deep-work]]`

**Assessment:** Systemic forward-reference pattern. Not a per-file format failure.

---

### 3. Unquoted `parent` wikilinks in tag frontmatter — 23 files

**Severity:** WARNING  
**Category:** Frontmatter

**Affected scope:** `wiki/tag/*.md`

**Issue:** `parent: [[tag]]` is parsed by YAML as a list, not a string. Expected format is quoted: `parent: "[[tag]]"`.

**Affected files:**
`ai.md`, `automation.md`, `coding.md`, `crypto.md`, `defi.md`, `economic.md`, `geopolitics.md`, `hack.md`, `health.md`, `investment.md`, `law.md`, `layer1.md`, `news.md`, `opinion.md`, `politic.md`, `productivity.md`, `psychology.md`, `research.md`, `system.md`, `tech.md`, `tools.md`, `tutorial.md`, `vibecode.md`.

**Assessment:** Carry-over spec conflict between generated index output and frontmatter parsing expectations.

---

### 4. Field order mismatch — 1 file

**Severity:** WARNING  
**Category:** Frontmatter

**File:** `wiki/sources/src_dan-koe-workflow-analysis-markus.md`

---

### 5. Broken `original` raw-file reference — 1 file

**Severity:** WARNING  
**Category:** Frontmatter

**File:** `wiki/sources/src_map-is-not-territory.md`

**Issue:** `original: "[[2026-06-03_map-is-not-territory]]"` points to a raw file that does not exist.

---

## Excluded From Actionable Count

### Topic files scanned by script — 118 false positives

**Raw script behavior:** reports `wiki/topic/*.md` as `No frontmatter: Missing opening ---`.

**Why excluded:** Current KB validation scope treats `wiki/topic/*.md` as out of scope for format-spec validation. This is a validator-scope problem, not a new content regression.

---

## Verdict

**REVISE** — 8 direct format errors remain, plus 337 warnings dominated by forward references and tag-frontmatter quoting.

## Verification

```bash
test -f "wiki/reviews/2026-06-25_format-report.md" && echo "✅ Report written"
```