# Compile Agent — Examples

Concrete examples of compilation workflows. Shows input (raw file) → output (wiki files) transformations.

Last updated: 2026-05-09

---

## Overview

This document shows real-world examples of how Compile Agent transforms raw content into structured wiki knowledge.

Each example demonstrates:
- Input raw files
- Generated source notes
- Generated concept notes
- Tagging decisions
- Merge/update behavior
- Error handling

### Compilation patterns

| Input Type | Source File? | Concept File(s)? | Notes |
|---|---|---|---|
| Article (single topic) | Yes | Yes (1) | Standard case |
| Article (multiple topics) | Yes | Yes (2-4) | One source, multiple concepts |
| Video (long-form) | No | Yes (1-2) | Concept only, reference raw |
| Twitter thread | Yes | Yes (1-3) | Depends on thread depth |
| Academic paper | Yes | Yes (3-6) | Often multiple concepts |
| GitHub repo | No | Yes (1) | Concept only, link to repo |
| Website | Yes | Yes (1-2) | If substantial content |

---

# Example 1 — Article → Source + Concept

## Input

`raw/articles/2026-05-01_anthropic-claude-code.md`

```markdown
---
type: article
url: https://anthropic.com/claude-code
author: Anthropic
date_published: 2026-05-01
date_ingested: 2026-05-09
---

# Introducing Claude Code

Anthropic today announced Claude Code...
```

---

## Output 1 — Source Note

`wiki/sources/src_anthropic-claude-code.md`

```yaml
---
type: source
original: raw/articles/2026-05-01_anthropic-claude-code.md
main_tag: ai
sub_tags: [tools, tutorial]
topic: claude-code-intro
date_compiled: 2026-05-09
url: https://anthropic.com/claude-code
author: Anthropic
---
```

Key outcomes:
- Source note created
- 3 concepts extracted
- Main tag assigned: `#ai`
- Sub-tags assigned: `#tools`, `#tutorial`

---

## Output 2 — Concept Note

`wiki/concepts/claude-code-workflow.md`

```yaml
---
type: concept
status: draft
main_tag: ai
sub_tags: [tools, automation]
topic: claude-code-workflow
sources:
  - [[wiki/sources/src_anthropic-claude-code]]
last_updated: 2026-05-09
---
```

Core ideas extracted:
- Spec-driven development
- AI-assisted coding workflow
- Autonomous implementation
- Incremental verification

---

# Example 2 — Twitter Thread → Multiple Concepts

## Input

`raw/posts/2026-04-15_defi-exploit-curve.md`

Topic:
- Curve exploit
- Flashloans
- Reentrancy
- Compiler bug in Vyper

---

## Generated Concepts

Compile Agent creates:

1. `reentrancy-attacks.md`
2. `flashloan-exploits.md`
3. `compiler-security.md`
4. `defi-security-best-practices.md`

All reference the same source note.

### Tags assigned

```yaml
main_tag: crypto
sub_tags: [defi, hack, news]
topic: curve-exploit-2026-04
```

---

# Example 3 — Video → Concept Only

## Input

`raw/videos/2026-03-20_vitalik-l2-scaling.md`

Long-form YouTube transcript summary.

### Compile decision

No source note created.

Reason:
- Transcript too large
- Key insights already extracted into concept note
- Raw file is enough as provenance reference

---

## Output

`wiki/concepts/ethereum-l2-scaling-roadmap.md`

Key extracted ideas:
- Rollup-centric roadmap
- Danksharding
- Shared sequencing
- Data availability sampling
- L2 interoperability

Tags:

```yaml
main_tag: crypto
sub_tags: [layer2, research]
topic: ethereum-scaling
```

---

# Example 4 — Existing Concept Merge

## Scenario

Compile Agent processes:

`raw/articles/2026-05-10_claude-code-update.md`

But concept already exists:

`wiki/concepts/claude-code-workflow.md`

---

## Merge behavior

Agent:
- Creates new source note
- Reads existing concept file
- Appends new insights
- Deduplicates overlapping bullets
- Preserves `## Notes`
- Updates `last_updated`

### MEMORY.md log

```markdown
[2026-05-10 14:30] Updated existing concept: claude-code-workflow
- Added source: src_claude-code-update
- Merged 2 new key ideas
- No new related concepts
```

---

# Example 5 — Duplicate Source Detection

## Scenario

New raw file has same URL as existing source.

### Behavior

1. Compare URLs
2. Compare summaries/content hash
3. Decide:
   - identical → skip
   - updated → versioned source note

Example:

```markdown
Original:
src_anthropic-claude-code.md

New version:
src_anthropic-claude-code-2026-05-11.md
```

---

# Example 6 — Draft Escalation

## Scenario

Complex 50-page ZKP paper.

Compile Agent cannot confidently determine:
- concept boundaries
- decomposition strategy
- canonical topic structure

---

## Action

Creates draft:

`wiki/drafts/src_complex-zkp-paper.md`

Escalates to Julius:

```markdown
[DRAFT CREATED]
Reason: Paper covers multiple advanced ZKP systems.

Suggested concepts:
1. zkp-fundamentals
2. snark-vs-stark
3. plonk-protocol
4. zkp-applications
```

---

# Error Handling Examples

## Missing frontmatter

```markdown
[VALIDATION ERROR]
Missing required field: title
Action: skipped
```

---

## Unknown tags

```markdown
[TAG PROPOSAL]
Proposed: #mcp
Closest existing: #tools
```

---

## Merge conflict

```markdown
[MERGE CONFLICT]
Concept: progressive-disclosure
Action: saved competing version into drafts/
```

---

# Decision Rules Summary

## Create source note when:

- Content is substantial
- Source has long-term reference value
- Multiple concepts originate from same source
- Original wording matters

## Skip source note when:

- Raw content is already enough
- External media transcript is too large
- Concept captures all reusable knowledge
- Source is transient/low signal

---

# End of examples.md

