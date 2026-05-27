# Output Validation — 2026-05-27

**Status:** approved 2026-05-27
**Issues found:** 11
**Created:** 2026-05-27 22:00:00
**Validator:** output-validator

**Files checked:** 123 (24 sources + 99 concepts)
**New/modified since last validation:** 11 files (1 today + 10 yesterday)

---

## Issue 1: Duplicate `## Notes` section

**File:** wiki/concepts/cynefin-framework.md
**Severity:** ERROR
**Dimension:** Coherence
**Issue:** File contains two identical `## Notes` sections at lines 45 and 47. Duplicate section headers create ambiguity and may confuse wiki tools.
**Evidence:**
```
45|## Notes
46|
47|## Notes
```
**Suggested fix:** Remove the duplicate `## Notes` at line 47 (empty section).

---

## Issue 2: Missing `## Original excerpts` section in 3 source files

**File:** wiki/sources/src_ai-trillion-dollar-blind-spot.md, wiki/sources/src_will-ai-replace-systems-thinking.md, wiki/sources/src_aaron-wright-ai-agents-legal-body.md
**Severity:** ERROR
**Dimension:** Completeness
**Issue:** Three source files are missing the required `## Original excerpts` section. All other 21 source files include this section. Without original excerpts, readers cannot verify claims against the source material.
**Evidence:**
- `src_ai-trillion-dollar-blind-spot.md`: sections end at `## Concepts referenced` (line 50), no excerpts
- `src_will-ai-replace-systems-thinking.md`: sections end at `## Concepts referenced` (line 43), no excerpts
- `src_aaron-wright-ai-agents-legal-body.md`: has `## Original Excerpts` (capital E, wrong case) on line 42 — section header is wrong, but content exists
**Suggested fix:** Add `## Original excerpts` section with relevant quotes for the 2 missing files. Fix case in src_aaron-wright-ai-agents-legal-body.md from `## Original Excerpts` → `## Original excerpts`.

---

## Issue 3: Dangling wikilinks to non-existent concepts

**File:** wiki/concepts/ai-augmented-systems-thinking.md, wiki/concepts/human-judgment-ai.md, wiki/sources/src_will-ai-replace-systems-thinking.md
**Severity:** ERROR
**Dimension:** Coherence
**Issue:** Multiple files reference wikilinks to concepts that do not exist in `wiki/concepts/`:
- `[[systems-thinking]]` — referenced by ai-augmented-systems-thinking.md (line 42)
- `[[second-order-effects]]` — referenced by src_will-ai-replace-systems-thinking.md (line 47) and human-judgment-ai.md (line 20)
**Evidence:**
```
// ai-augmented-systems-thinking.md line 42:
- [[systems-thinking]]

// src_will-ai-replace-systems-thinking.md line 47:
- [[second-order-effects]]

// human-judgment-ai.md line 20:
- [[second-order-effects]]
```
**Suggested fix:** Either create stub concept files for `systems-thinking` and `second-order-effects`, or remove the dangling wikilinks and replace with plain text references.

---

## Issue 4: Summary still too short — 1 non-empty sentence (2 source files, NOT FIXED from 2026-05-26 report)

**File:** wiki/sources/src_ai-trillion-dollar-blind-spot.md, wiki/sources/src_will-ai-replace-systems-thinking.md
**Severity:** WARNING
**Dimension:** Completeness
**Issue:** Summaries contain only 1 substantive sentence each (requirement: 3–5 sentences). These were flagged as Issue 3 and Issue 4 in the 2026-05-26 output report but were not fixed.
**Evidence:**
- `src_ai-trillion-dollar-blind-spot.md` Summary (only 1 sentence of actual content spanning 2 lines):
  > Companies are racing to embed AI into their products while ignoring the most critical customer touchpoint: the static landing page. The traditional website cannot have conversations or adapt to context, creating high friction for potential customers trying to determine product relevance.

- `src_will-ai-replace-systems-thinking.md` Summary (only 1 sentence of actual content):
  > AI will not replace systems thinking, but it will fundamentally change how systems thinking is practiced. The article argues that AI is a powerful assistant for pattern recognition and complexity processing, but cannot replace human judgment on questions of boundaries, incentives, tradeoffs, and values.
**Suggested fix:** Expand each summary to 3–5 sentences. Add key conclusions, implications, or call to action.

---

## Issue 5: Section name mismatch — `## Related Concepts` (capital C)

**File:** wiki/concepts/static-website-blind-spot.md
**Severity:** WARNING
**Dimension:** Coherence
**Issue:** Uses `## Related Concepts` (capital C) instead of the standard `## Related concepts` (lowercase c) used by 98 other concept files. This was flagged as Issue 5 in 2026-05-26 report but was NOT fixed.
**Evidence:**
```
46|## Related Concepts
```
**Suggested fix:** Rename to `## Related concepts`.

---

## Issue 6: Non-standard section `## Related content` in source file

**File:** wiki/sources/src_luke-alvoeiro-multi-agent-architecture-factory.md
**Severity:** WARNING
**Dimension:** Coherence
**Issue:** Source file contains a non-standard section `## Related content` (line 52) not present in any other source file. Standard source file sections are: Metadata, Summary, Key points, Concepts referenced, Original excerpts.
**Evidence:**
```
52|## Related content
```
**Suggested fix:** Remove the section or merge content into `## Concepts referenced` or `## Original excerpts`.

---

## Issue 7: Empty Backlinks and Notes sections (NOT FIXED from 2026-05-26)

**File:** wiki/concepts/static-website-blind-spot.md, wiki/concepts/ai-augmented-systems-thinking.md
**Severity:** WARNING
**Dimension:** Completeness
**Issue:** Both concept files have empty `## Backlinks` and `## Notes` sections. These were flagged as Issue 6 in the 2026-05-26 report but remain unfixed.
**Evidence:**
```
## Backlinks

## Notes
```
**Suggested fix:** Populate Backlinks with inbound references or remove empty sections.

---

## Issue 8: New stub concept — definition too short (1 sentence)

**File:** wiki/concepts/ai-productivity.md
**Severity:** WARNING
**Dimension:** Completeness
**Issue:** New concept file created today (May 27) with status: stub and only 1-sentence definition. It also lacks a `## Key ideas` section, leaving the concept underdeveloped.
**Evidence:**
```
16|AI Productivity là việc sử dụng AI để tăng cường năng suất cá nhân và tổ chức, bao gồm cả khả năng xử lý thông tin nhanh hơn, tự động hóa tác vụ lặp lại, và hỗ trợ ra quyết định.
```
**Suggested fix:** Expand definition to 2–3 sentences. Add `## Key ideas` section with 3–5 key points drawn from the linked source `src_how-ai-productivity-fails`.

---

## Issue 9: Stub concepts missing `## Key ideas` sections (5 files)

**File:** wiki/concepts/human-judgment-ai.md, wiki/concepts/generative-ai-seo.md, wiki/concepts/conversational-website.md, wiki/concepts/ai-powered-discovery.md, wiki/concepts/ai-productivity.md
**Severity:** INFO
**Dimension:** Completeness
**Issue:** Five concept files with status: stub have only a `## Definition` and `## Related concepts` — all lack a `## Key ideas` section. While stubs are acceptable as placeholders, they should ideally have at least 2–3 key ideas.
**Evidence:** All five files have the same minimal structure: Definition → Related concepts → Sources → Backlinks → Notes. No Key ideas section.
**Suggested fix:** Add `## Key ideas` section with 2–5 key points from linked sources, or mark with explicit "TODO" in Notes.

---

## Issue 10: Wrong case — `## Original Excerpts` (capital E)

**File:** wiki/sources/src_aaron-wright-ai-agents-legal-body.md
**Severity:** INFO
**Dimension:** Coherence
**Issue:** Uses `## Original Excerpts` (capital E) instead of the standard `## Original excerpts` (lowercase e) used by all other source files.
**Evidence:**
```
42|## Original Excerpts
```
**Suggested fix:** Rename to `## Original excerpts` for consistency.

---

## Issue 11: ai-productivity.md has dangling link to itself via ai-augmented-systems-thinking

**File:** wiki/concepts/ai-productivity.md
**Severity:** INFO
**Dimension:** Coherence
**Issue:** `ai-productivity.md` links to `[[ai-augmented-systems-thinking]]` in Related concepts, and `ai-augmented-systems-thinking.md` links back to `[[ai-productivity]]` — but the references are circular without substantive content backing either direction.
**Evidence:**
- ai-productivity.md line 20: `- [[ai-augmented-systems-thinking]]`
- ai-augmented-systems-thinking.md line 44: `- [[ai-productivity]]`
**Suggested fix:** Acceptable for now (mutual references are normal). Flag for review once both concepts have developed Key ideas.

---

## Summary

| Severity | Count | Notes |
|----------|-------|-------|
| ERROR | 3 | Duplicate Notes, missing Original excerpts (3 files), dangling wikilinks |
| WARNING | 5 | Short summaries (unfixed), section name mismatch (unfixed), non-standard section, empty sections (unfixed), short definition |
| INFO | 3 | Stubs missing Key ideas (5 files), wrong case, circular ref |

**Key observation:** 4 out of 6 issues from the 2026-05-26 report remain unfixed (Issues 3, 4, 5, 6 from that report are still present). Fix Agent has not yet processed those.

**Systematic concern:** New source files from May 26 compilation are missing `## Original excerpts` — may indicate Compile Agent prompt issue.
