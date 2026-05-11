# Format Validator — Examples

Sample format validation reports and common structural issues with fixes.

---

## Overview

This document provides real-world examples of Format Validator reports and demonstrates how to fix common format issues. Format Validator checks **structure only** (frontmatter, sections, naming, markdown syntax), not content quality.

---

## Example 1: Complete Validation Report

### Sample report structure

```markdown
# Format Validation — 2026-05-09

**Status:** pending
**Issues found:** 12 (5 ERROR, 5 WARNING, 2 INFO)
**Created:** 2026-05-09 22:30:15
**Validator:** format-validator

**Files checked:** 127

---

## Issue 1: Missing required field

**File:** wiki/concepts/rag-system.md
**Severity:** ERROR
**Category:** Frontmatter
**Issue:** Missing required field: last_updated
**Current:** Field not present
**Expected:** last_updated: YYYY-MM-DD
**Suggested fix:** Add last_updated field to frontmatter

---

## Issue 2: Invalid YAML syntax

**File:** wiki/concepts/embedding.md
**Severity:** ERROR
**Category:** Frontmatter
**Issue:** Invalid YAML syntax
**Current:** sub_tags: [tools automation]
**Expected:** sub_tags: [tools, automation]
**Suggested fix:** Add comma between array items

---

## Issue 3: Missing required section

**File:** wiki/concepts/vector-db.md
**Severity:** ERROR
**Category:** Sections
**Issue:** Missing required section: Definition
**Current:** Key ideas, Related concepts, Sources
**Expected:** Must include ## Definition
**Suggested fix:** Add ## Definition section

---

## Issue 4: Section order incorrect

**File:** wiki/concepts/prompt-engineering.md
**Severity:** WARNING
**Category:** Sections
**Issue:** Section order does not match format-spec.md
**Current:** Key ideas, Definition, Related concepts, Sources
**Expected:** Definition, Key ideas, Related concepts, Sources
**Suggested fix:** Reorder sections to match format-spec.md

---

## Issue 5: Slug contains invalid characters

**File:** wiki/concepts/RAG_System.md
**Severity:** ERROR
**Category:** Naming
**Issue:** Slug contains invalid characters
**Current:** RAG_System
**Expected:** lowercase-hyphen-format
**Suggested fix:** Rename to rag-system.md

---

## Issue 6: Field order incorrect

**File:** wiki/sources/src_anthropic-claude.md
**Severity:** WARNING
**Category:** Frontmatter
**Issue:** Field order does not match format-spec.md
**Current:** type, main_tag, original, sub_tags, topic, date_compiled
**Expected:** type, original, main_tag, sub_tags, topic, date_compiled
**Suggested fix:** Reorder fields to match format-spec.md

---

## Issue 7: Section uses wrong heading level

**File:** wiki/concepts/llm-security.md
**Severity:** ERROR
**Category:** Sections
**Issue:** Section uses wrong heading level: Key ideas
**Current:** ### Key ideas
**Expected:** ## Key ideas
**Suggested fix:** Use H2 (##) for all sections

---

## Issue 8: Internal link should use wikilink

**File:** wiki/concepts/rag-workflow.md
**Severity:** WARNING
**Category:** Markdown
**Issue:** Internal link should use wikilink syntax
**Current:** [embedding](wiki/concepts/embedding.md)
**Expected:** [[embedding]]
**Suggested fix:** Use [[slug]] for internal links

---

## Issue 9: Code block missing language tag

**File:** wiki/sources/src_python-tutorial.md
**Severity:** INFO
**Category:** Markdown
**Issue:** Code block 1 missing language tag
**Current:** ```
**Expected:** ```python or ```bash
**Suggested fix:** Add language tag after ```

---

## Issue 10: Tag not found in TAGS.md

**File:** wiki/concepts/new-concept.md
**Severity:** ERROR
**Category:** Frontmatter
**Issue:** main_tag not in TAGS.md Pool A
**Current:** main_tag: machine-learning
**Expected:** Tag must exist in TAGS.md
**Suggested fix:** Use existing tag from Pool A or propose new tag

---

## Issue 11: Inconsistent bullet markers

**File:** wiki/sources/src_best-practices.md
**Severity:** INFO
**Category:** Markdown
**Issue:** Inconsistent bullet list markers
**Current:** Uses: -, *, +
**Expected:** Use - for all bullet lists
**Suggested fix:** Standardize on - for bullets

---

## Issue 12: Slug too long

**File:** wiki/concepts/comprehensive-guide-to-retrieval-augmented-generation-systems.md
**Severity:** WARNING
**Category:** Naming
**Issue:** Slug too long
**Current:** 67 characters
**Expected:** Max 50 characters
**Suggested fix:** Shorten slug to 50 characters or less
```

---

## Example 2: Frontmatter Issues

### Issue 2.1: Missing required field

**Before (ERROR):**
```yaml
---
type: concept
status: draft
main_tag: ai
sub_tags: [tools, automation]
topic: rag-system
sources:
  - [[wiki/sources/src_rag-intro]]
---
```

**After (FIXED):**
```yaml
---
type: concept
status: draft
main_tag: ai
sub_tags: [tools, automation]
topic: rag-system
sources:
  - [[wiki/sources/src_rag-intro]]
last_updated: 2026-05-09
---
```

---

### Issue 2.2: Invalid YAML syntax

**Before (ERROR):**
```yaml
---
type: concept
status: draft
main_tag: ai
sub_tags: [tools automation research]
topic: rag-system
sources:
  - [[wiki/sources/src_rag-intro]]
last_updated: 2026-05-09
---
```

**After (FIXED):**
```yaml
---
type: concept
status: draft
main_tag: ai
sub_tags: [tools, automation, research]
topic: rag-system
sources:
  - [[wiki/sources/src_rag-intro]]
last_updated: 2026-05-09
---
```

---

### Issue 2.3: Field order incorrect

**Before (WARNING):**
```yaml
---
type: concept
main_tag: ai
status: draft
topic: rag-system
sub_tags: [tools, automation]
sources:
  - [[wiki/sources/src_rag-intro]]
last_updated: 2026-05-09
---
```

**After (FIXED):**
```yaml
---
type: concept
status: draft
main_tag: ai
sub_tags: [tools, automation]
topic: rag-system
sources:
  - [[wiki/sources/src_rag-intro]]
last_updated: 2026-05-09
---
```

---

### Issue 2.4: Wrong field type

**Before (ERROR):**
```yaml
---
type: concept
status: draft
main_tag: ai
sub_tags: tools, automation
topic: rag-system
sources:
  - [[wiki/sources/src_rag-intro]]
last_updated: 2026-05-09
---
```

**After (FIXED):**
```yaml
---
type: concept
status: draft
main_tag: ai
sub_tags: [tools, automation]
topic: rag-system
sources:
  - [[wiki/sources/src_rag-intro]]
last_updated: 2026-05-09
---
```

---

### Issue 2.5: Invalid date format

**Before (ERROR):**
```yaml
---
type: concept
status: draft
main_tag: ai
sub_tags: [tools, automation]
topic: rag-system
sources:
  - [[wiki/sources/src_rag-intro]]
last_updated: 09/05/2026
---
```

**After (FIXED):**
```yaml
---
type: concept
status: draft
main_tag: ai
sub_tags: [tools, automation]
topic: rag-system
sources:
  - [[wiki/sources/src_rag-intro]]
last_updated: 2026-05-09
---
```

---

### Issue 2.6: Tag not in TAGS.md

**Before (ERROR):**
```yaml
---
type: concept
status: draft
main_tag: machine-learning
sub_tags: [deep-learning, neural-networks]
topic: rag-system
sources:
  - [[wiki/sources/src_rag-intro]]
last_updated: 2026-05-09
---
```

**After (FIXED):**
```yaml
---
type: concept
status: draft
main_tag: ai
sub_tags: [research, tools]
topic: rag-system
sources:
  - [[wiki/sources/src_rag-intro]]
last_updated: 2026-05-09
---
```

---

### Issue 2.7: Too many sub_tags

**Before (ERROR):**
```yaml
---
type: concept
status: draft
main_tag: ai
sub_tags: [tools, automation, research, tutorial]
topic: rag-system
sources:
  - [[wiki/sources/src_rag-intro]]
last_updated: 2026-05-09
---
```

**After (FIXED):**
```yaml
---
type: concept
status: draft
main_tag: ai
sub_tags: [tools, automation, research]
topic: rag-system
sources:
  - [[wiki/sources/src_rag-intro]]
last_updated: 2026-05-09
---
```

---

### Issue 2.8: Tag uses # prefix in frontmatter

**Before (ERROR):**
```yaml
---
type: concept
status: draft
main_tag: #ai
sub_tags: [#tools, #automation]
topic: rag-system
sources:
  - [[wiki/sources/src_rag-intro]]
last_updated: 2026-05-09
---
```

**After (FIXED):**
```yaml
---
type: concept
status: draft
main_tag: ai
sub_tags: [tools, automation]
topic: rag-system
sources:
  - [[wiki/sources/src_rag-intro]]
last_updated: 2026-05-09
---
```

---

## Example 3: Section Structure Issues

### Issue 3.1: Missing required section

**Before (ERROR):**
```markdown
---
type: concept
status: draft
main_tag: ai
sub_tags: [tools]
topic: rag-system
sources:
  - [[wiki/sources/src_rag-intro]]
last_updated: 2026-05-09
---

# RAG System

## Key ideas

- Improves accuracy
- Uses vector search

## Related concepts

- [[embedding]]

## Sources

- [[wiki/sources/src_rag-intro]]
```

**After (FIXED):**
```markdown
---
type: concept
status: draft
main_tag: ai
sub_tags: [tools]
topic: rag-system
sources:
  - [[wiki/sources/src_rag-intro]]
last_updated: 2026-05-09
---

# RAG System

## Definition

RAG (Retrieval-Augmented Generation) is a technique that enhances LLM responses by retrieving relevant documents before generation.

## Key ideas

- Improves accuracy
- Uses vector search

## Related concepts

- [[embedding]]

## Sources

- [[wiki/sources/src_rag-intro]]
```

---

### Issue 3.2: Section order incorrect

**Before (WARNING):**
```markdown
# RAG System

## Key ideas

- Improves accuracy
- Uses vector search

## Definition

RAG is a technique for improving LLM responses.

## Related concepts

- [[embedding]]

## Sources

- [[wiki/sources/src_rag-intro]]
```

**After (FIXED):**
```markdown
# RAG System

## Definition

RAG is a technique for improving LLM responses.

## Key ideas

- Improves accuracy
- Uses vector search

## Related concepts

- [[embedding]]

## Sources

- [[wiki/sources/src_rag-intro]]
```

---

### Issue 3.3: Wrong heading level

**Before (ERROR):**
```markdown
# RAG System

### Definition

RAG is a technique for improving LLM responses.

### Key ideas

- Improves accuracy
- Uses vector search
```

**After (FIXED):**
```markdown
# RAG System

## Definition

RAG is a technique for improving LLM responses.

## Key ideas

- Improves accuracy
- Uses vector search
```

---

### Issue 3.4: Duplicate section

**Before (ERROR):**
```markdown
# RAG System

## Definition

RAG is a technique for improving LLM responses.

## Key ideas

- Improves accuracy
- Uses vector search

## Key ideas

- Reduces hallucinations
- Requires document corpus
```

**After (FIXED):**
```markdown
# RAG System

## Definition

RAG is a technique for improving LLM responses.

## Key ideas

- Improves accuracy
- Uses vector search
- Reduces hallucinations
- Requires document corpus
```

---

### Issue 3.5: Multiple H1 headers

**Before (ERROR):**
```markdown
# RAG System

## Definition

RAG is a technique for improving LLM responses.

# Key Concepts

## Embedding

Embedding converts text to vectors.
```

**After (FIXED):**
```markdown
# RAG System

## Definition

RAG is a technique for improving LLM responses.

## Key ideas

- Embedding converts text to vectors
- Vector search finds similar content
```

---

## Example 4: Naming Convention Issues

### Issue 4.1: Slug contains invalid characters

**Before (ERROR):**
```
wiki/concepts/RAG_System.md
```

**After (FIXED):**
```
wiki/concepts/rag-system.md
```

---

### Issue 4.2: Missing src_ prefix

**Before (ERROR):**
```
wiki/sources/anthropic-claude.md
```

**After (FIXED):**
```
wiki/sources/src_anthropic-claude.md
```

---

### Issue 4.3: Slug too long

**Before (WARNING):**
```
wiki/concepts/comprehensive-guide-to-retrieval-augmented-generation-systems-and-best-practices.md
```

**After (FIXED):**
```
wiki/concepts/rag-systems-guide.md
```

---

### Issue 4.4: File in wrong folder

**Before (ERROR):**
```
wiki/concepts/src_anthropic-claude.md
```

**After (FIXED):**
```
wiki/sources/src_anthropic-claude.md
```

---

### Issue 4.5: Slug uses uppercase

**Before (WARNING):**
```
wiki/concepts/RAG-System.md
```

**After (FIXED):**
```
wiki/concepts/rag-system.md
```

---

### Issue 4.6: Slug uses spaces

**Before (ERROR):**
```
wiki/concepts/rag system.md
```

**After (FIXED):**
```
wiki/concepts/rag-system.md
```

---

## Example 5: Markdown Syntax Issues

### Issue 5.1: Internal link uses markdown syntax

**Before (WARNING):**
```markdown
RAG systems use [embeddings](wiki/concepts/embedding.md) for semantic search.
```

**After (FIXED):**
```markdown
RAG systems use [[embedding]] for semantic search.
```

---

### Issue 5.2: Code block missing language tag

**Before (INFO):**
````markdown
## Example

```
def search(query):
    return results
```
````

**After (FIXED):**
````markdown
## Example

```python
def search(query):
    return results
```
````

---

### Issue 5.3: Inconsistent bullet markers

**Before (INFO):**
```markdown
## Key ideas

- First point
* Second point
+ Third point
- Fourth point
```

**After (FIXED):**
```markdown
## Key ideas

- First point
- Second point
- Third point
- Fourth point
```

---

### Issue 5.4: Wikilink has spaces around brackets

**Before (ERROR):**
```markdown
See [[ embedding ]] for more details.
```

**After (FIXED):**
```markdown
See [[embedding]] for more details.
```

---

### Issue 5.5: Broken wikilink

**Before (ERROR):**
```markdown
Related: [[non-existent-concept]]
```

**After (FIXED):**
```markdown
Related: [[embedding]]
```

Or create the missing file:
```bash
touch wiki/concepts/non-existent-concept.md
```

---

### Issue 5.6: Setext headers used

**Before (ERROR):**
```markdown
Definition
==========

RAG is a technique...

Key ideas
---------

- Point 1
- Point 2
```

**After (FIXED):**
```markdown
## Definition

RAG is a technique...

## Key ideas

- Point 1
- Point 2
```

---

## Example 6: Multi-Category Issues

### Complex case: Multiple format issues in one file

**Before (5 ERROR, 3 WARNING):**

```markdown
---
type: concept
main_tag: ai
status: draft
sub_tags: tools automation
topic: RAG_System
sources:
  - [[wiki/sources/src_rag-intro]]
last_updated: 09/05/2026
---

# RAG System

### Key ideas

* Improves accuracy
+ Uses vector search
- Reduces hallucinations

Definition
==========

RAG is a technique.

## Related concepts

See [embedding](wiki/concepts/embedding.md) for details.

## Sources

- [[wiki/sources/src_rag-intro]]
```

**Issues found:**
1. ERROR (Frontmatter): Field order incorrect
2. ERROR (Frontmatter): sub_tags wrong type (not array)
3. ERROR (Frontmatter): Invalid date format
4. ERROR (Naming): Slug contains invalid characters (RAG_System)
5. ERROR (Sections): Missing required section (Definition not H2)
6. WARNING (Sections): Section order incorrect
7. WARNING (Markdown): Internal link should use wikilink
8. INFO (Markdown): Inconsistent bullet markers

---

**After (FIXED):**

```markdown
---
type: concept
status: draft
main_tag: ai
sub_tags: [tools, automation]
topic: rag-system
sources:
  - [[wiki/sources/src_rag-intro]]
last_updated: 2026-05-09
---

# RAG System

## Definition

RAG is a technique for improving LLM responses by retrieving relevant documents.

## Key ideas

- Improves accuracy
- Uses vector search
- Reduces hallucinations

## Related concepts

See [[embedding]] for details.

## Sources

- [[wiki/sources/src_rag-intro]]
```

**File renamed:** `RAG_System.md` → `rag-system.md`

---

## Example 7: Source File Format Issues

### Issue 7.1: Missing original field

**Before (ERROR):**
```yaml
---
type: source
main_tag: ai
sub_tags: [tools]
topic: claude-code
date_compiled: 2026-05-09
---
```

**After (FIXED):**
```yaml
---
type: source
original: raw/articles/2026-05-01_anthropic-claude-code.md
main_tag: ai
sub_tags: [tools]
topic: claude-code
date_compiled: 2026-05-09
---
```

---

### Issue 7.2: Wrong section names for source file

**Before (ERROR):**
```markdown
# Anthropic Claude Code

## Definition

Claude Code is...

## Key ideas

- Point 1
- Point 2
```

**After (FIXED):**
```markdown
# Anthropic Claude Code

## Metadata

- **Source type:** Article
- **Published:** 2026-05-01
- **Author:** Anthropic

## Summary

Anthropic công bố Claude Code...

## Key points

- Point 1
- Point 2

## Concepts referenced

- [[claude-code-workflow]]
```

---

## Example 8: Edge Cases

### Case 8.1: Empty sources array

**Before (WARNING):**
```yaml
---
type: concept
status: draft
main_tag: ai
sub_tags: [tools]
topic: new-concept
sources: []
last_updated: 2026-05-09
---
```

**After (FIXED):**
```yaml
---
type: concept
status: draft
main_tag: ai
sub_tags: [tools]
topic: new-concept
sources:
  - [[wiki/sources/src_reference]]
last_updated: 2026-05-09
---
```

---

### Case 8.2: Vietnamese diacritics in slug (allowed)

**Valid:**
```
wiki/concepts/tối-ưu-hóa-context.md
```

This is **allowed** per format-spec.md Section 2.1.

---

### Case 8.3: Optional fields present

**Valid:**
```yaml
---
type: source
original: raw/articles/2026-05-01_anthropic-claude.md
main_tag: ai
sub_tags: [tools]
topic: claude-code
date_compiled: 2026-05-09
url: https://anthropic.com/claude-code
author: Anthropic
---
```

Optional fields `url` and `author` are allowed.

---

## Example 9: Systematic Issues

### Pattern: Multiple files with same issue

**Detected pattern:**
```
20 files have field order incorrect
Likely cause: Compile Agent not following format-spec.md field order
```

**Report includes:**
```markdown
[SYSTEMATIC ISSUE]
Pattern: 20 files have frontmatter field order incorrect
Files affected: rag-system.md, embedding.md, vector-db.md, ...
Likely cause: Compile Agent not following format-spec.md
Recommendation: Update compile-agent/SKILL.md to enforce field order
```

---

## Example 10: Report Actions

### Julius approves report

**Telegram command:**
```
approve format
```

**Result:**
- Report status: pending → approved
- Entry moves to "Recently Applied" in _action-required.md
- Fix Agent can now apply fixes

---

### Julius rejects report

**Telegram command:**
```
reject format
```

**Result:**
- Report status: pending → rejected
- Entry removed from _action-required.md
- Report archived to wiki/reviews/archive/

---

### Julius requests details

**Telegram command:**
```
show format
```

**Result:**
- Full report sent to Telegram
- Or link to wiki/reviews/2026-05-09_format-report.md

---

## Related Documentation

- [SKILL.md](SKILL.md) — Format Validator overview
- [workflow.md](workflow.md) — Step-by-step validation process
- [wiki/meta/format-spec.md](../../wiki/meta/format-spec.md) — Ground truth format rules

---

**End of examples.md**
