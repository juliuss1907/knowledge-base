# Output Validation — 2026-05-22

**Status:** approved 2026-05-24
**Issues found:** 16 (0 ERROR, 8 WARNING, 8 INFO)
**Created:** 2026-05-22 23:10:00
**Validator:** output-validator

**Files checked:** 95 (17 sources + 78 concepts)
**New files validated in-depth:** 27 (8 sources + 19 concepts)
**Existing files quick-scanned:** 68 (9 sources + 59 concepts) — systematic issues only

**Note:** 4 issues from 2026-05-21 report resolved (default-mode-network, dunbar-number, evolutionary-mismatch key ideas; hunter-gatherer-lifestyle typo). 7 issues unresolved or worsened.

---

## Issue 1: Empty Original excerpts section (persistent from 2026-05-21)

**File:** wiki/sources/src_hermes-xurl-skill-guide.md
**Severity:** WARNING
**Dimension:** Completeness
**Issue:** `## Original excerpts` section header present but no content follows. Flagged yesterday, not yet fixed.
**Evidence:**
```
## Original excerpts
```
(empty — line 47, end of file)
**Suggested fix:** Add excerpt from the original X post or remove empty section.

---

## Issue 2: Empty Notes sections — 15 new concept files (persistent pattern from 2026-05-21)

**File:** wiki/concepts/*.md (15 new concept files)
**Severity:** WARNING
**Dimension:** Completeness
**Issue:** All 15 newly compiled concept files have an empty `## Notes` section. Combined with 34 existing concept files, this totals 49 concept files with empty Notes — a systematic template artifact.
**Evidence (15 new files):**
```
wiki/concepts/ai-legal-personhood.md
wiki/concepts/agency-law.md
wiki/concepts/agentic-commerce.md
wiki/concepts/ai-white-collar-automation.md
wiki/concepts/atomic-mac-agent.md
wiki/concepts/default-mode-network.md
wiki/concepts/dunbar-number.md
wiki/concepts/evolutionary-mismatch.md
wiki/concepts/hermes-agent.md
wiki/concepts/hunter-gatherer-lifestyle.md
wiki/concepts/polymarket.md
wiki/concepts/productivity-wage-gap.md
wiki/concepts/six-stage-research-pipeline.md
wiki/concepts/supply-chain-attack.md
wiki/concepts/team-pcp-hacker-group.md
wiki/concepts/vs-code-marketplace-security.md
wiki/concepts/x-api-oauth2.md
wiki/concepts/xurl-cli.md
```
All have: `## Notes` followed by nothing.
**Suggested fix:** Remove empty Notes section from template when no content exists, or populate with relevant annotations.

---

## Issue 3: Too many key points — 23 (maximum 10 recommended)

**File:** wiki/sources/src_11-minutes-hack-github.md
**Severity:** WARNING
**Dimension:** Completeness
**Issue:** Key points section has 23 bullet points (was 11 yesterday — got worse after recompilation). Maximum recommended is 10.
**Evidence:**
```
23 bullet points from "3,800 internal repos" through "Các mục tiêu trước: Trivy, Kics, Fake Bitwarden/cli..."
```
**Suggested fix:** Consolidate related points — merge the 3 TeamPCP timeline bullet points into one, combine the malware statistics into one, merge the exfiltration channels.

---

## Issue 4: Too many key points — 21 (maximum 10 recommended)

**File:** wiki/sources/src_ai-will-destroy-world-economy.md
**Severity:** WARNING
**Dimension:** Completeness
**Issue:** Key points section has 21 bullet points (was 11 yesterday — got worse after recompilation). Maximum recommended is 10.
**Evidence:**
```
21 bullet points from "Mustafa Suleyman (CEO Microsoft AI)..." through "Lời khuyên: Người xây dựng AI..."
```
**Suggested fix:** Consolidate: merge the 3 crisis-mechanism points into one, merge the two Fed/options points, combine UBI-related items.

---

## Issue 5: Broken wikilinks — 17 missing concept files

**File:** Multiple source and concept files (8 sources + 6 concepts affected)
**Severity:** WARNING
**Dimension:** Completeness
**Issue:** Source and concept files reference 17 concept files that don't exist yet in `wiki/concepts/`. This grew from 13 missing concepts yesterday.

**Evidence by referencing file:**

From `wiki/sources/src_11-minutes-hack-github.md`:
- [[orphan-commit-attack]], [[dns-tunneling]], [[dead-drop-communication]], [[github-security]]

From `wiki/sources/src_ai-will-destroy-world-economy.md`:
- [[ubi-universal-basic-income]], [[economic-inequality]], [[financial-crisis-2008-comparison]]

From `wiki/sources/src_hermes-polymarket-btc-trading-agent.md`:
- [[prediction-markets]], [[crypto-trading-bots]], [[self-learning-agents]], [[bittensor]]

From `wiki/sources/src_hermes-xurl-skill-guide.md`:
- [[supergrok-subscription]], [[nous-research]]

From `wiki/concepts/ai-legal-personhood.md`:
- [[dao-legal-structure]]

From `wiki/concepts/hermes-agent.md`:
- [[self-learning-agents]], [[mcp-model-context-protocol]]

From `wiki/concepts/polymarket.md`:
- [[prediction-markets]], [[crypto-trading-bots]], [[bittensor]]

From `wiki/concepts/zero-member-llc.md`:
- [[dao-legal-structure]], [[smart-contracts]]

From `wiki/concepts/agentic-commerce.md`:
- [[autonomous-agents]]

**Suggested fix:** Compile the 17 missing concept files or remove unreferenced wikilinks. Consider whether compile-agent should handle transitive concept compilation.

---

## Issue 6: Empty Notes sections — 34 existing concept files (systematic pattern)

**File:** 34 existing concept files across wiki/concepts/
**Severity:** INFO
**Dimension:** Completeness
**Issue:** 34 existing concept files (compiled before 2026-05-22) also have empty `## Notes` sections. Combined with the 15 new files, this totals 49 concept files with empty Notes — a Compile Agent template artifact affecting ~63% of concept files.

**Evidence:** All files from `user-md-configuration.md` through `hermes-operator-role.md`. Note that some concept files like `ai-legal-personhood.md` and `zero-member-llc.md` have Notes at end-of-file without trailing newline (the section header is present at the very end of the file), confirming this is a template artifact.

**Suggested fix:** Update Compile Agent template to conditionally include `## Notes` only when there is content to annotate.

---

## Issue 7: Empty Original excerpts — 1 source file

**File:** wiki/sources/src_hermes-xurl-skill-guide.md
**Severity:** INFO
**Dimension:** Completeness
**Issue:** `## Original excerpts` section has no excerpt content while all other source files contain at least one excerpt.
**Suggested fix:** Add an excerpt from the original X Developers post or remove the empty section.

---

## Issue 8: Too many key points in existing source files — 4 files

**File:** wiki/sources/src_how-ai-productivity-fails.md, src_how-some-people-become-unrecognizable.md, src_active-vs-lazy-thinking.md, src_what-comes-after-systems-thinking.md
**Severity:** INFO
**Dimension:** Completeness
**Issue:** These 4 existing source files exceed the recommended 10 key points maximum:
- `src_how-ai-productivity-fails.md`: 13 key points
- `src_how-some-people-become-unrecognizable.md`: 11 key points
- `src_active-vs-lazy-thinking.md`: 11 key points
- `src_what-comes-after-systems-thinking.md`: 11 key points

**Suggested fix:** Consolidate related points in each file to stay within 5-10 range.

---

## Issue 9: Empty Original excerpts in src_1-month-with-hermes — only ">" quotes, no narrative

**File:** wiki/sources/src_1-month-with-hermes-ive-been-using-wrong.md
**Severity:** INFO
**Dimension:** Coherence
**Issue:** The Original excerpts section contains two standalone quotes without context or attribution framing, unlike other source files which provide richer excerpts.
**Evidence:**
```
> "You have to steer the AI. Not let it steer you."
> "Use the AI to augment learning. Not the other way around."
```
**Suggested fix:** Add brief context for each quote (e.g., where in the article they appear, what they illustrate).

---

## Issue 10: Source file title casing inconsistency

**File:** wiki/sources/src_ai-will-destroy-world-economy.md
**Severity:** INFO
**Dimension:** Coherence
**Issue:** Title is all lowercase: "ai will destroy the world economy" — inconsistent with other source files that use title case (e.g., "Don't Sign In With Google", "The Agent's Legal Body").
**Suggested fix:** Capitalize to "AI Will Destroy the World Economy" for consistency.

---

## Issue 11: Missing trailing newline — 3 concept files

**File:** wiki/concepts/productivity-wage-gap.md, wiki/concepts/ai-legal-personhood.md, wiki/concepts/zero-member-llc.md
**Severity:** INFO
**Dimension:** Completeness
**Issue:** These 3 concept files are missing a trailing newline at end of file. The `## Notes` header sits at the very last line without a newline, causing the file to end without a proper line terminator.
**Suggested fix:** Add trailing newline. This may be a Compile Agent template issue for files with empty Notes.

---

## Issue 12: Summary section borderline short — 1 concept file

**File:** wiki/concepts/six-stage-research-pipeline.md
**Severity:** INFO
**Dimension:** Completeness
**Issue:** The Definition section is only 1 sentence (minimum 2 required for concepts). "Pipeline 6 giai đoạn kết hợp nhiều tools để tạo comprehensive research report: x_search → Cookie MCP → Browser CDP → DeepSeek → Hindsight → Report."
**Evidence:** Definition is one sentence summarizing the pipeline stages without explaining what kind of output it produces or why it matters.
**Suggested fix:** Split into 2 sentences: one describing the pipeline, one describing its purpose and value.

---

## Issue 13: Key points mix bullets with subsections inconsistently

**File:** wiki/concepts/ai-legal-personhood.md
**Severity:** INFO
**Dimension:** Coherence
**Issue:** Key ideas section uses H3 subheadings (### Vấn đề hiện tại, ### Giải pháp, ### Cơ chế hoạt động) instead of consistent bullet format. This deviates from most concept files which use flat bullet lists.
**Suggested fix:** Either convert to flat bullets or establish a consistent subsection convention for all concept files.

---

## Issue 14: Mixed Vietnamese/English in header

**File:** wiki/concepts/polymarket.md
**Severity:** INFO
**Dimension:** Vietnamese
**Issue:** The file uses both English and Vietnamese interchangeably in bullet points (e.g., "Prediction market: Người dùng mua YES/NO tokens..." mixes English terms mid-sentence). While technical terms in English are acceptable, the mixing pattern is inconsistent with other concept files.
**Suggested fix:** Standardize on Vietnamese descriptions with English terms in parentheticals, or use consistent style.

---

## Issue 15: Definition formatting — code keywords vs plain text

**File:** wiki/concepts/agentic-commerce.md
**Severity:** INFO
**Dimension:** Vietnamese
**Issue:** Key ideas section uses nested sub-bullets under numbered items, creating a deep hierarchy that may not render well in Obsidian. The `>` blockquote in "Lớp quan trọng nhất" subsection is also unusual for a Key ideas section.
**Suggested fix:** Flatten to standard bullet format for consistency with other concept files.

---

## Issue 16: ai-legal-personhood — frontmatter source reference with .md extension

**File:** wiki/concepts/ai-legal-personhood.md
**Severity:** INFO
**Dimension:** Factual
**Issue:** Frontmatter sources list references `src_aaron-wright-ai-agents-legal-body` without the `.md` extension: `[[wiki/sources/src_aaron-wright-ai-agents-legal-body]]`. Most other concept files include the `.md` extension in source wikilinks. While Obsidian resolves both, this is inconsistent.

**Evidence:**
```yaml
sources:
  - [[wiki/sources/src_aaron-wright-ai-agents-legal-body]]
```
vs most files:
```yaml
sources:
  - [[wiki/sources/src_were-not-supposed-to-live-like-this.md]]
```
**Suggested fix:** Add `.md` extension for consistency.

---

## Summary

| Severity | Count | Files affected |
|---|---|---|
| ERROR | 0 | — |
| WARNING | 8 | 25 files |
| INFO | 8 | 53 files |

**Top issues by type:**
1. **Empty Notes sections** — 49 concept files (63% of all concepts), systematic Compile Agent template artifact
2. **Too many key points** — 6 source files exceed the 10-point maximum (23, 21, 13, 11×3)
3. **Broken wikilinks** — 17 missing concept files referenced across 14 files
4. **Empty Original excerpts** — 1 source file (persistent from yesterday)

**Changes from yesterday:**
- ✅ **FIXED:** default-mode-network.md, dunbar-number.md, evolutionary-mismatch.md — key ideas now 6/7/8 (was 4 each)
- ✅ **FIXED:** hunter-gatherer-lifestyle.md — "tiếng" typo corrected
- ❌ **UNRESOLVED:** Empty Original excerpts in src_hermes-xurl-skill-guide.md
- ❌ **WORSE:** src_11-minutes-hack-github.md key points: 11 → 23
- ❌ **WORSE:** src_ai-will-destroy-world-economy.md key points: 11 → 21
- ❌ **UNRESOLVED:** Broken wikilinks — 13 → 17 missing concepts
- ❌ **UNRESOLVED:** Empty Notes pattern — now 49 total files (was 14)

**Overall quality assessment: Good.** No ERROR-level issues. The key ideas completeness issues from yesterday were well-fixed by Kara. The main concern is the worsening key points count in two source files (recompilation made them more detailed but less structured) and the growing empty Notes pattern. The broken wikilink list also expanded from 13 to 17 missing concepts, indicating new source files were compiled without their transitive concept dependencies.
