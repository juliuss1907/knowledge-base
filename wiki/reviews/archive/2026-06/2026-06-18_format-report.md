# Format Validation — 2026-06-18

**Status:** approved
**Approved by:** Julius
**Issues found:** 17 (11 ERROR, 6 WARNING, 0 INFO)
**Files checked:** 530
**Created:** 2026-06-18 23:19:15
**Validator:** format-validator

**Files by type:** {'index': 30, 'concept': 300, 'source': 92, 'topic': 108}

---

## Issue 1: sub_tags: tag "crypto" not in Pool B

**File:** wiki/concepts/ai-lab-crypto-analogy.md
**Severity:** ERROR
**Category:** Frontmatter
**Issue:** sub_tags: tag "crypto" not in Pool B
**Current:** `crypto`
**Expected:** Use one of: ['ai', 'automation', 'coding', 'defi', 'hack', 'health', 'law', 'layer1', 'layer2', 'news', 'opinion', 'perpdex', 'psychology', 'research', 'system', 'tools', 'tutorial', 'vibecode']

---

## Issue 2: sub_tags: tag "crypto" not in Pool B

**File:** wiki/concepts/altcoin-frenzy-pattern.md
**Severity:** ERROR
**Category:** Frontmatter
**Issue:** sub_tags: tag "crypto" not in Pool B
**Current:** `crypto`
**Expected:** Use one of: ['ai', 'automation', 'coding', 'defi', 'hack', 'health', 'law', 'layer1', 'layer2', 'news', 'opinion', 'perpdex', 'psychology', 'research', 'system', 'tools', 'tutorial', 'vibecode']

---

## Issue 3: sub_tags: tag "crypto" not in Pool B

**File:** wiki/concepts/infrastructure-capex-cycle.md
**Severity:** ERROR
**Category:** Frontmatter
**Issue:** sub_tags: tag "crypto" not in Pool B
**Current:** `crypto`
**Expected:** Use one of: ['ai', 'automation', 'coding', 'defi', 'hack', 'health', 'law', 'layer1', 'layer2', 'news', 'opinion', 'perpdex', 'psychology', 'research', 'system', 'tools', 'tutorial', 'vibecode']

---

## Issue 4: Missing required section: "Related concepts"

**File:** wiki/concepts/infrastructure-capex-cycle.md
**Severity:** ERROR
**Category:** Sections
**Issue:** Missing required section: "Related concepts"
**Expected:** Add "## Related concepts" section

---

## Issue 5: Missing required section: "Sources"

**File:** wiki/concepts/infrastructure-capex-cycle.md
**Severity:** ERROR
**Category:** Sections
**Issue:** Missing required section: "Sources"
**Expected:** Add "## Sources" section

---

## Issue 6: sub_tags: tag "crypto" not in Pool B

**File:** wiki/sources/src_l1-blockchain-ai-lab-comparison.md
**Severity:** ERROR
**Category:** Frontmatter
**Issue:** sub_tags: tag "crypto" not in Pool B
**Current:** `crypto`
**Expected:** Use one of: ['ai', 'automation', 'coding', 'defi', 'hack', 'health', 'law', 'layer1', 'layer2', 'news', 'opinion', 'perpdex', 'psychology', 'research', 'system', 'tools', 'tutorial', 'vibecode']

---

## Issue 7: scope must be raw/wiki/context, got "tag"

**File:** wiki/tag/tag.md
**Severity:** ERROR
**Category:** Frontmatter
**Issue:** scope must be raw/wiki/context, got "tag"
**Current:** `tag`
**Expected:** Use valid scope

---

## Issue 8: auto_generated must be false

**File:** wiki/tag/tag.md
**Severity:** ERROR
**Category:** Frontmatter
**Issue:** auto_generated must be false
**Current:** `True`
**Expected:** Set auto_generated: false

---

## Issue 9: Missing required section: "Overview"

**File:** wiki/tag/tag.md
**Severity:** ERROR
**Category:** Sections
**Issue:** Missing required section: "Overview"
**Expected:** Add "## Overview" section

---

## Issue 10: Missing required section: "Sub-indexes"

**File:** wiki/tag/tag.md
**Severity:** ERROR
**Category:** Sections
**Issue:** Missing required section: "Sub-indexes"
**Expected:** Add "## Sub-indexes" section

---

## Issue 11: Missing required section: "Notes"

**File:** wiki/tag/tag.md
**Severity:** ERROR
**Category:** Sections
**Issue:** Missing required section: "Notes"
**Expected:** Add "## Notes" section

---

## Issue 12: parent: unquoted wikilink parsed as list (YAML ambiguity)

**File:** raw/articles/articles.md
**Severity:** WARNING
**Category:** Frontmatter
**Issue:** parent: unquoted wikilink parsed as list (YAML ambiguity)
**Current:** `[['raw']]`
**Expected:** Use quoted format: parent: "[[target]]"

---

## Issue 13: parent: unquoted wikilink parsed as list (YAML ambiguity)

**File:** raw/papers/papers.md
**Severity:** WARNING
**Category:** Frontmatter
**Issue:** parent: unquoted wikilink parsed as list (YAML ambiguity)
**Current:** `[['raw']]`
**Expected:** Use quoted format: parent: "[[target]]"

---

## Issue 14: parent: unquoted wikilink parsed as list (YAML ambiguity)

**File:** raw/posts/posts.md
**Severity:** WARNING
**Category:** Frontmatter
**Issue:** parent: unquoted wikilink parsed as list (YAML ambiguity)
**Current:** `[['raw']]`
**Expected:** Use quoted format: parent: "[[target]]"

---

## Issue 15: parent: unquoted wikilink parsed as list (YAML ambiguity)

**File:** raw/repos/repos.md
**Severity:** WARNING
**Category:** Frontmatter
**Issue:** parent: unquoted wikilink parsed as list (YAML ambiguity)
**Current:** `[['raw']]`
**Expected:** Use quoted format: parent: "[[target]]"

---

## Issue 16: parent: unquoted wikilink parsed as list (YAML ambiguity)

**File:** raw/videos/videos.md
**Severity:** WARNING
**Category:** Frontmatter
**Issue:** parent: unquoted wikilink parsed as list (YAML ambiguity)
**Current:** `[['raw']]`
**Expected:** Use quoted format: parent: "[[target]]"

---

## Issue 17: parent: unquoted wikilink parsed as list (YAML ambiguity)

**File:** raw/websites/websites.md
**Severity:** WARNING
**Category:** Frontmatter
**Issue:** parent: unquoted wikilink parsed as list (YAML ambiguity)
**Current:** `[['raw']]`
**Expected:** Use quoted format: parent: "[[target]]"

---
