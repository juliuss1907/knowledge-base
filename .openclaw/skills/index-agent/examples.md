# Index Agent — Example Index Files

Sample outputs for tag and topic indexes. Use these as reference when generating indexes.

---

## Example 1: Main-tag Index (#ai)

**File:** `wiki/tag/ai.md`

```markdown
# Tag: #ai

Auto-generated index of all content tagged with `#ai`.

Last updated: 2026-05-07 21:00:15

---

## Concepts (12)

- [[agent-skills]] — main: #ai, sub: [#tools, #automation], topic: agent-skills-pattern
- [[claude-code]] — main: #ai, sub: [#tools, #vibecode], topic: claude-code-workflow
- [[context-window-management]] — main: #ai, sub: [#research], topic: llm-context-optimization
- [[llm-knowledge-base]] — main: #ai, sub: [#tools, #automation], topic: kb-architecture
- [[progressive-disclosure]] — main: #ai, sub: [#tools], topic: agent-skills-pattern
- [[prompt-injection]] — main: #ai, sub: [#hack, #research], topic: llm-security
- [[rag-pipeline]] — main: #ai, sub: [#tools, #tutorial], topic: rag-implementation
- [[skill-description-pattern]] — main: #ai, sub: [#tools], topic: agent-skills-pattern
- [[three-level-loading]] — main: #ai, sub: [#tools], topic: agent-skills-pattern
- [[transformer-architecture]] — main: #ai, sub: [#research], topic: transformer-architecture
- [[vibe-coding]] — main: #ai, sub: [#vibecode, #opinion], topic: ai-assisted-development
- [[zero-shot-prompting]] — main: #ai, sub: [#tutorial], topic: prompt-engineering

## Sources (18)

- [[src_anthropic-claude-code]] — main: #ai, sub: [#tools, #news], topic: claude-code-workflow
- [[src_anthropic-extended-thinking]] — main: #ai, sub: [#tools, #news], topic: extended-thinking
- [[src_bibek-skill-md-pattern]] — main: #ai, sub: [#tools, #tutorial], topic: agent-skills-pattern
- [[src_cursor-ai-editor]] — main: #ai, sub: [#tools], topic: cursor-editor
- [[src_karpathy-llm-intro]] — main: #ai, sub: [#tutorial], topic: llm-introduction
- [[src_openai-gpt4-turbo]] — main: #ai, sub: [#tools, #news], topic: gpt4-turbo-release
- [[src_prompt-injection-attacks]] — main: #ai, sub: [#hack, #research], topic: llm-security
- [[src_rag-best-practices]] — main: #ai, sub: [#tutorial], topic: rag-implementation
- [[src_vaswani-attention]] — main: #ai, sub: [#research], topic: transformer-architecture
- [[src_vibe-coding-manifesto]] — main: #ai, sub: [#vibecode, #opinion], topic: ai-assisted-development
- [[src_anthropic-sdk-python]] — main: #ai, sub: [#tools, #tutorial], topic: anthropic-sdk
- [[src_claude-api-guide]] — main: #ai, sub: [#tools, #tutorial], topic: claude-api
- [[src_llm-context-limits]] — main: #ai, sub: [#research], topic: llm-context-optimization
- [[src_openai-embeddings]] — main: #ai, sub: [#tools, #tutorial], topic: embeddings
- [[src_prompt-engineering-guide]] — main: #ai, sub: [#tutorial], topic: prompt-engineering
- [[src_rag-chunking-strategies]] — main: #ai, sub: [#tutorial], topic: rag-implementation
- [[src_semantic-search]] — main: #ai, sub: [#tools, #tutorial], topic: semantic-search
- [[src_zero-shot-learning]] — main: #ai, sub: [#research, #tutorial], topic: prompt-engineering

## Co-occurring tags

Tags that frequently appear with `#ai`:
- `#tools` (15 files)
- `#tutorial` (8 files)
- `#research` (6 files)
- `#vibecode` (3 files)
- `#hack` (2 files)
```

**Notes:**
- 12 concepts + 18 sources = 30 total files with `#ai`
- Co-occurrence shows `#tools` is most common pairing (15 files)
- All wikilinks use double brackets `[[slug]]`
- Metadata inline after each link

---

## Example 2: Sub-tag Index (#hack)

**File:** `wiki/tag/hack.md`

```markdown
# Tag: #hack

Auto-generated index of all content tagged with `#hack`.

Last updated: 2026-05-07 21:00:15

---

## Concepts (3)

- [[curve-pool-exploit]] — main: #crypto, sub: [#hack, #defi, #news], topic: curve-pool-exploit
- [[prompt-injection]] — main: #ai, sub: [#hack, #research], topic: llm-security
- [[reentrancy-attack]] — main: #crypto, sub: [#hack, #defi], topic: smart-contract-security

## Sources (5)

- [[src_curve-exploit-analysis]] — main: #crypto, sub: [#hack, #defi, #news], topic: curve-pool-exploit
- [[src_defi-hacks-2026]] — main: #crypto, sub: [#hack, #defi], topic: defi-security
- [[src_prompt-injection-attacks]] — main: #ai, sub: [#hack, #research], topic: llm-security
- [[src_reentrancy-explained]] — main: #crypto, sub: [#hack, #defi, #tutorial], topic: smart-contract-security
- [[src_smart-contract-exploits]] — main: #crypto, sub: [#hack, #defi], topic: smart-contract-security

## Co-occurring tags

Tags that frequently appear with `#hack`:
- `#defi` (4 files)
- `#crypto` (4 files)
- `#research` (2 files)
- `#news` (2 files)
- `#tutorial` (1 file)
```

**Notes:**
- Cross-domain tag: appears with both `#ai` and `#crypto` main-tags
- Smaller index (8 files total) compared to main-tag indexes
- Co-occurrence shows strong correlation with `#defi` (4/8 files)

---

## Example 3: Topic Index (claude-code-workflow)

**File:** `wiki/topic/claude-code-workflow.md`

```markdown
# Topic: claude-code-workflow

Auto-generated index of all content with topic `claude-code-workflow`.

Last updated: 2026-05-07 21:00:15

---

## Concepts (2)

- [[claude-code]] — main: #ai, sub: [#tools, #vibecode]
- [[vibe-coding]] — main: #ai, sub: [#vibecode, #opinion]

## Sources (3)

- [[src_anthropic-claude-code]] — main: #ai, sub: [#tools, #news]
- [[src_claude-code-daily-workflow]] — main: #ai, sub: [#tools, #tutorial]
- [[src_claude-code-tips]] — main: #ai, sub: [#tools, #tutorial]

## Related topics

Topics that share concepts/sources with `claude-code-workflow`:
- `ai-assisted-development` (2 shared files)
- `agent-skills-pattern` (1 shared file)
- `cursor-editor` (1 shared file)
```

**Notes:**
- Topic groups related content (2 concepts + 3 sources)
- Related topics show overlap (shared files)
- All files in this topic have `#ai` as main-tag (domain consistency)

---

## Example 4: Topic Index with High Overlap (defi-security)

**File:** `wiki/topic/defi-security.md`

```markdown
# Topic: defi-security

Auto-generated index of all content with topic `defi-security`.

Last updated: 2026-05-07 21:00:15

---

## Concepts (4)

- [[curve-pool-exploit]] — main: #crypto, sub: [#hack, #defi, #news]
- [[flash-loan-attack]] — main: #crypto, sub: [#hack, #defi]
- [[reentrancy-attack]] — main: #crypto, sub: [#hack, #defi]
- [[smart-contract-audit]] — main: #crypto, sub: [#defi, #tutorial]

## Sources (6)

- [[src_curve-exploit-analysis]] — main: #crypto, sub: [#hack, #defi, #news]
- [[src_defi-hacks-2026]] — main: #crypto, sub: [#hack, #defi]
- [[src_flash-loan-explained]] — main: #crypto, sub: [#hack, #defi, #tutorial]
- [[src_reentrancy-explained]] — main: #crypto, sub: [#hack, #defi, #tutorial]
- [[src_smart-contract-exploits]] — main: #crypto, sub: [#hack, #defi]
- [[src_solidity-security-guide]] — main: #crypto, sub: [#defi, #tutorial]

## Related topics

Topics that share concepts/sources with `defi-security`:
- `smart-contract-security` (5 shared files)
- `curve-pool-exploit` (2 shared files)
- `defi-protocols` (2 shared files)
- `ethereum-security` (1 shared file)
```

**Notes:**
- Larger topic (10 files total)
- High overlap with `smart-contract-security` (5 shared files)
- All files have `#crypto` main-tag + `#defi` sub-tag (strong domain focus)

---

## Example 5: Empty Tag Index (edge case)

**File:** `wiki/tag/perpdex.md`

```markdown
# Tag: #perpdex

Auto-generated index of all content tagged with `#perpdex`.

Last updated: 2026-05-07 21:00:15

---

## Concepts (0)

No concepts tagged with `#perpdex` yet.

## Sources (1)

- [[src_hyperliquid-review]] — main: #crypto, sub: [#perpdex, #tools], topic: hyperliquid-review

## Co-occurring tags

Tags that frequently appear with `#perpdex`:
- `#crypto` (1 file)
- `#tools` (1 file)

(Insufficient data for meaningful co-occurrence analysis)
```

**Notes:**
- Valid index even with minimal content (1 file)
- Co-occurrence section notes insufficient data
- This tag may become orphaned if the single source is deleted

---

## Example 6: Tag Index After Orphan Cleanup

**Before cleanup:**
```
wiki/tag/
├── ai.md
├── crypto.md
├── deprecated.md  ← orphan (no files use this tag)
├── hack.md
├── old-tag.md     ← orphan (tag removed from TAGS.md)
└── tools.md
```

**After cleanup:**
```
wiki/tag/
├── ai.md
├── crypto.md
├── hack.md
└── tools.md
```

**MEMORY.md log:**
```markdown
## 2026-05-07 21:00:15 — Orphan cleanup
- Deleted tag indexes: [deprecated, old-tag]
- Reason: No wiki files currently use these tags
```

---

## Example 7: Co-occurrence Analysis Detail

**Scenario:** 10 files in wiki, tag distribution:

| File | main_tag | sub_tags |
|---|---|---|
| file1 | #ai | [#tools, #tutorial] |
| file2 | #ai | [#tools, #automation] |
| file3 | #ai | [#tools, #research] |
| file4 | #crypto | [#defi, #hack] |
| file5 | #crypto | [#defi, #tools] |
| file6 | #crypto | [#defi, #layer2] |
| file7 | #tech | [#tools, #automation] |
| file8 | #tech | [#tools, #tutorial] |
| file9 | #productivity | [#tools, #automation] |
| file10 | #system | [#automation] |

**Co-occurrence matrix:**

| Pair | Count |
|---|---|
| (#ai, #tools) | 3 |
| (#ai, #tutorial) | 1 |
| (#ai, #automation) | 1 |
| (#ai, #research) | 1 |
| (#crypto, #defi) | 3 |
| (#crypto, #hack) | 1 |
| (#crypto, #tools) | 1 |
| (#crypto, #layer2) | 1 |
| (#tech, #tools) | 2 |
| (#tech, #automation) | 1 |
| (#tech, #tutorial) | 1 |
| (#productivity, #tools) | 1 |
| (#productivity, #automation) | 1 |
| (#tools, #tutorial) | 2 |
| (#tools, #automation) | 4 |
| (#tools, #research) | 1 |
| (#defi, #hack) | 1 |
| (#defi, #tools) | 1 |
| (#defi, #layer2) | 1 |

**Resulting co-occurrence in `wiki/tag/tools.md`:**
```markdown
## Co-occurring tags

Tags that frequently appear with `#tools`:
- `#automation` (4 files)
- `#ai` (3 files)
- `#tech` (2 files)
- `#tutorial` (2 files)
- `#crypto` (1 file)
```

---

## Example 8: Topic Overlap Analysis Detail

**Scenario:** 3 topics with shared files:

**Topic A (rag-implementation):**
- Files: [file1, file2, file3, file4]

**Topic B (llm-context-optimization):**
- Files: [file3, file4, file5]

**Topic C (semantic-search):**
- Files: [file4, file6]

**Overlap calculation:**
- A ∩ B = {file3, file4} → 2 shared files
- A ∩ C = {file4} → 1 shared file
- B ∩ C = {file4} → 1 shared file

**Resulting related topics in `wiki/topic/rag-implementation.md`:**
```markdown
## Related topics

Topics that share concepts/sources with `rag-implementation`:
- `llm-context-optimization` (2 shared files)
- `semantic-search` (1 shared file)
```

---

## Format Consistency Rules

All index files follow these patterns:

### Header
```markdown
# Tag: #<tag>
# Topic: <topic>

Auto-generated index of all content tagged with/with topic `...`.

Last updated: YYYY-MM-DD HH:MM:SS

---
```

### Sections
1. `## Concepts (N)` — always present, even if N=0
2. `## Sources (N)` — always present, even if N=0
3. `## Co-occurring tags` (tag indexes only) — omit if <2 files
4. `## Related topics` (topic indexes only) — omit if no overlap

### Wikilinks
- Format: `[[slug]]` (double brackets, no extension)
- Metadata: ` — main: #<tag>, sub: [#<tag>, ...], topic: <topic>`
- Order: alphabetical by slug within each section

### Co-occurrence format
```markdown
- `#<tag>` (N files)
```
- Backticks around tag
- Count in parentheses
- Top 5 by frequency, descending

### Related topics format
```markdown
- `<topic>` (N shared files)
```
- Backticks around topic
- Count in parentheses
- Top 5 by overlap, descending

---

## Edge Cases

### No concepts for a tag
```markdown
## Concepts (0)

No concepts tagged with `#<tag>` yet.
```

### No sources for a tag
```markdown
## Sources (0)

No sources tagged with `#<tag>` yet.
```

### Insufficient co-occurrence data
```markdown
## Co-occurring tags

Tags that frequently appear with `#<tag>`:
- `#<other>` (1 file)

(Insufficient data for meaningful co-occurrence analysis)
```

### No related topics
```markdown
## Related topics

No topics share files with `<topic>` yet.
```

---

## Validation Checklist

Before considering an index file complete, verify:

- [ ] File exists in correct folder (`wiki/tag/` or `wiki/topic/`)
- [ ] Filename matches tag/topic slug exactly
- [ ] Header format correct (# Tag: or # Topic:)
- [ ] Last updated timestamp present
- [ ] Both Concepts and Sources sections present
- [ ] Wikilinks use double brackets `[[slug]]`
- [ ] Metadata format consistent (main, sub, topic)
- [ ] Co-occurrence/related sections present if applicable
- [ ] No empty sections (use "No X yet" if count is 0)
- [ ] Alphabetical order within sections
