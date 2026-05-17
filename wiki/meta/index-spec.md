# Index Specification — Knowledge Base V2

> Ground truth for index file format rules.
> Consumed by: Hermes Format Validator + OpenClaw Index/Ingest/Compile Agents.
> Changes here directly affect validation behavior and agent workflows.

**Version:** 1.0
**Last updated:** 2026-05-17

---

## 1. Scope

This spec defines the **format for index files** used as navigation hubs across the Knowledge Base.

**What this spec covers:**
- Index file identification (frontmatter `type: index`)
- Frontmatter schema per layer (1, 2, 3)
- Required sections and structure
- Stats section format
- Items section management (append rules)
- Wikilink rules between layers
- Permissions per layer

**What this spec does NOT cover:**
- Content files (concepts, sources, raw files) → see `format-spec.md`
- Folder hierarchy → see `folder-structure.md`
- Content quality of index entries → not validated (index files are metadata only)
- Topic files (`wiki/topic/<topic>.md`) — these are content aggregators, not navigation indexes (see Section 5.1)

---

## 2. Index hierarchy

### 2.1 Three-layer structure

```
Tầng 1 (Layer 1) — Root indexes
├── raw/raw.md
├── wiki/wiki.md
└── context/context.md

Tầng 2 (Layer 2) — Sub indexes
├── raw/articles/articles.md
├── raw/posts/posts.md
├── raw/websites/websites.md
├── raw/videos/videos.md
├── raw/papers/papers.md
├── raw/repos/repos.md
└── wiki/tag/tag.md

Tầng 3 (Layer 3) — Atom indexes (auto-generated)
└── wiki/tag/<tag>.md (one file per tag in TAGS.md)
```

### 2.2 Wikilink flow (graph view connectivity)

**Path 1: Raw layer top-down**
```
raw.md
  ↓
articles.md (or posts.md, websites.md, etc.)
  ↓
raw/articles/2026-05-17_<slug>.md  (raw content file)
  ↓ (via compiled_to field)
wiki/sources/src_<slug>.md
  ↓
wiki/concepts/<concept>.md
```

**Path 2: Wiki layer top-down**
```
wiki.md
  ↓
tag.md
  ↓
wiki/tag/ai.md (or other tag)
  ↓
wiki/concepts/<concept>.md  (or wiki/sources/src_<slug>.md)
```

**Path 3: Topic side-channel (no parent index)**
```
wiki/topic/<topic>.md
  ↓ (links directly to sources)
wiki/sources/src_<slug>.md
  ↓ (via original field)
raw/articles/<slug>.md
  ↓ (via parent in articles.md)
articles.md
  ↓
raw.md
```

### 2.3 Permissions overview

| Layer | Edit by | Auto-managed sections |
|---|---|---|
| Tầng 1 | Julius only | None — agents READ-ONLY |
| Tầng 2 | Julius + agents (limited) | Stats, Items |
| Tầng 3 | Index Agent | Full file (regenerated daily) |

---

## 3. Tầng 1 — Root indexes

### 3.1 Files

| File | Path | Scope |
|---|---|---|
| `raw.md` | `raw/raw.md` | Index of raw layer |
| `wiki.md` | `wiki/wiki.md` | Index of wiki layer |
| `context.md` | `context/context.md` | Index of context layer |

### 3.2 Frontmatter schema

```yaml
---
type: index
level: 1
scope: raw | wiki | context
auto_generated: false
last_updated: YYYY-MM-DD
---
```

**Field definitions:**

| Field | Type | Required | Validation |
|---|---|---|---|
| `type` | string | Yes | Must be exactly `index` |
| `level` | integer | Yes | Must be `1` |
| `scope` | enum | Yes | One of: `raw`, `wiki`, `context` |
| `auto_generated` | boolean | Yes | Must be `false` |
| `last_updated` | date | Yes | ISO format `YYYY-MM-DD` |

**Field order (required):**
1. `type`
2. `level`
3. `scope`
4. `auto_generated`
5. `last_updated`

### 3.3 Required sections (in order)

```markdown
# <Layer Title>

## Overview

## Sub-indexes

## Notes
```

**Section rules:**
- All sections required
- Use H2 (`##`) for all section headers
- Section order must match
- `## Notes` section is free space for Julius — agents must NOT modify

### 3.4 Section content rules

**Overview:** 1–3 sentences describing the layer's purpose.

**Sub-indexes:** Wikilinks to all Tầng 2 indexes within this layer. Format:
```markdown
- [[<sub-index-slug>]] — Brief description
```

**Notes:** Free-form. Agents must NOT touch.

### 3.5 Validation rules

| Severity | Issue |
|---|---|
| ERROR | Missing required frontmatter field |
| ERROR | `type` ≠ `index` |
| ERROR | `level` ≠ `1` |
| ERROR | `scope` not in allowed enum |
| ERROR | `auto_generated` ≠ `false` |
| ERROR | Missing required section |
| ERROR | Section uses wrong heading level |
| ERROR | `Sub-indexes` section contains non-wikilink entries |
| WARNING | Field order does not match spec |
| WARNING | `Sub-indexes` incomplete (missing known Tầng 2 files) |

---

## 4. Tầng 2 — Sub indexes

### 4.1 Files

| File | Path | Parent | Scope | Items managed by |
|---|---|---|---|---|
| `articles.md` | `raw/articles/articles.md` | `[[raw]]` | articles | Ingest Agent |
| `posts.md` | `raw/posts/posts.md` | `[[raw]]` | posts | Ingest Agent |
| `websites.md` | `raw/websites/websites.md` | `[[raw]]` | websites | Ingest Agent |
| `videos.md` | `raw/videos/videos.md` | `[[raw]]` | videos | Ingest Agent |
| `papers.md` | `raw/papers/papers.md` | `[[raw]]` | papers | Ingest Agent |
| `repos.md` | `raw/repos/repos.md` | `[[raw]]` | repos | Ingest Agent |
| `tag.md` | `wiki/tag/tag.md` | `[[wiki]]` | tags | Index Agent |

### 4.2 Frontmatter schema

```yaml
---
type: index
level: 2
scope: <specific-scope>
parent: [[<tầng-1-slug>]]
auto_generated: false
items_managed_by: <agent-name>
last_updated: YYYY-MM-DD
---
```

**Field definitions:**

| Field | Type | Required | Validation |
|---|---|---|---|
| `type` | string | Yes | Must be `index` |
| `level` | integer | Yes | Must be `2` |
| `scope` | enum | Yes | One of: `articles`, `posts`, `websites`, `videos`, `papers`, `repos`, `tags` |
| `parent` | wikilink | Yes | Must point to existing Tầng 1 file |
| `auto_generated` | boolean | Yes | Must be `false` |
| `items_managed_by` | string | Yes | One of: `ingest-agent`, `index-agent` |
| `last_updated` | date | Yes | ISO format `YYYY-MM-DD` |

**Field order (required):**
1. `type`
2. `level`
3. `scope`
4. `parent`
5. `auto_generated`
6. `items_managed_by`
7. `last_updated`

### 4.3 Required sections (in order)

```markdown
# <Index Title>

## Overview

## Parent

## Stats

## Items

## Notes
```

### 4.4 Section content rules

**Overview:** 1–3 sentences describing the index's purpose.

**Parent:** Single wikilink to Tầng 1 index.
```markdown
- [[raw]]
```

**Stats:** Auto-updated by responsible agent. Format defined in Section 6.

**Items:** Wikilinks to child files. Format:
```markdown
- [[<file-slug>]] — Title here (status)
```
- Sort: **newest first** (by date in slug or `last_updated`)
- For raw indexes: list raw content files (e.g., `2026-05-17_anthropic-claude`)
- For `tag.md`: list all `wiki/tag/<tag>.md` files

**Notes:** Free-form. Agents must NOT touch.

### 4.5 Items section management rules

**APPEND-only behavior:**
- Agents APPEND new entries to top of list (newest first)
- Agents NEVER remove entries
- Agents NEVER reorder existing entries
- Julius can manually remove, edit, or reorder

**Trigger conditions:**

| Index | Trigger | Action |
|---|---|---|
| `articles.md` (and 5 other raw indexes) | Ingest Agent ingests new file | Append wikilink + title + status |
| `tag.md` | Julius approves new tag → Index Agent processes | Append wikilink to new tag file |

**Format consistency:**
- All entries must use bare slug wikilinks
- All entries must include title and status
- No malformed entries (e.g., missing dash, raw text)

### 4.6 Validation rules

| Severity | Issue |
|---|---|
| ERROR | `type` ≠ `index` |
| ERROR | `level` ≠ `2` |
| ERROR | `scope` not in allowed enum |
| ERROR | `parent` not a valid wikilink |
| ERROR | `parent` points to non-existent Tầng 1 file |
| ERROR | `items_managed_by` not in allowed enum |
| ERROR | Missing required section |
| ERROR | `Stats` section missing required fields (see Section 6) |
| ERROR | `Items` section contains non-wikilink entries |
| WARNING | Items not sorted newest-first |
| WARNING | Items list incomplete (compared to actual files in folder) |
| INFO | Items count mismatch with Stats total |

---

## 5. Tầng 3 — Atom indexes

### 5.1 Scope

Only `wiki/tag/<tag>.md` is covered as an "index" in this spec.

**Note about topic files:**
`wiki/topic/<topic>.md` is auto-generated by Index Agent but is NOT an index in the navigation sense. Topic files aggregate sources sharing the same topic slug, linking directly to source files without going through a parent index. They function as content side-channels.

Topic files have their own format (defined in Index Agent skill), separate from this spec.

### 5.2 Frontmatter schema (`wiki/tag/<tag>.md`)

```yaml
---
type: index
level: 3
scope: tag
parent: [[tag]]
tag: <tag-name>
auto_generated: true
last_updated: YYYY-MM-DD
---
```

**Field definitions:**

| Field | Type | Required | Validation |
|---|---|---|---|
| `type` | string | Yes | Must be `index` |
| `level` | integer | Yes | Must be `3` |
| `scope` | string | Yes | Must be `tag` |
| `parent` | wikilink | Yes | Must be `[[tag]]` |
| `tag` | string | Yes | Tag name (no `#` prefix), must match filename |
| `auto_generated` | boolean | Yes | Must be `true` |
| `last_updated` | date | Yes | ISO format |

**Field order (required):**
1. `type`
2. `level`
3. `scope`
4. `parent`
5. `tag`
6. `auto_generated`
7. `last_updated`

### 5.3 Required sections (in order)

```markdown
# Tag: #<tag>

## Parent

## Stats

## Files with this tag

## Co-occurring tags
```

### 5.4 Section content rules

**Parent:**
```markdown
- [[tag]]
```

**Stats:** See Section 6.3.

**Files with this tag:** Wikilinks to all `wiki/sources/` and `wiki/concepts/` files containing this tag. Sort: alphabetical.
```markdown
- [[<file-slug>]] — Title (file type)
```

**Co-occurring tags:** Top 5 tags appearing together with this tag, ranked by frequency.
```markdown
- [[<tag>]] — N co-occurrences
```

### 5.5 Validation rules

| Severity | Issue |
|---|---|
| ERROR | `type` ≠ `index` |
| ERROR | `level` ≠ `3` |
| ERROR | `scope` ≠ `tag` |
| ERROR | `parent` ≠ `[[tag]]` |
| ERROR | `tag` field missing or doesn't match filename |
| ERROR | `auto_generated` ≠ `true` |
| ERROR | Missing required section |
| WARNING | Files list out of date (mismatch with actual tagged files) |
| INFO | Co-occurring tags section empty |

---

## 6. Stats section format

Stats section has standardized format per index type. Validators check exact structure.

### 6.1 Tầng 2 raw indexes (articles.md, posts.md, etc.)

```markdown
## Stats

- Total: <N> files
- By status: <X> processed, <Y> unprocessed
- By date: <A> this week, <B> this month
- Last updated: YYYY-MM-DD
```

### 6.2 Tầng 2 tag index (tag.md)

```markdown
## Stats

- Total tags: <N>
- Main tags: 7
- Sub tags: <M>
- Most used: #<tag1> (<X>), #<tag2> (<Y>), #<tag3> (<Z>)
- Last updated: YYYY-MM-DD
```

### 6.3 Tầng 3 tag files (wiki/tag/<tag>.md)

```markdown
## Stats

- Total files: <N>
- Sources: <X>
- Concepts: <Y>
- Last updated: YYYY-MM-DD
```

### 6.4 Update behavior

- Stats auto-updated by responsible agent on every run
- Update frequency: daily (matches agent schedule)
- Format must be exact (validator checks structure)
- `Last updated` reflects when Stats was regenerated, not when file was edited

### 6.5 Validation rules

| Severity | Issue |
|---|---|
| ERROR | Stats section missing |
| ERROR | Stats section format does not match spec |
| ERROR | Required Stats field missing |
| WARNING | Stats counts don't match actual file system |
| WARNING | `Last updated` more than 2 days old |

---

## 7. Wikilink rules

### 7.1 Use bare slugs

Aligns with `format-spec.md` v2.0+. Use bare slugs:

✅ Correct:
```markdown
- [[raw]]
- [[wiki]]
- [[articles]]
- [[tag]]
- [[ai]]
- [[2026-05-17_anthropic-claude]]
```

⚠️ Discouraged (still acceptable):
```markdown
- [[raw/raw]]
- [[wiki/tag/tag]]
```

❌ Wrong:
```markdown
- [[ raw ]]                    # spaces around brackets
- [text](raw.md)               # markdown link instead of wikilink
```

### 7.2 Display text optional

```markdown
- [[ai|AI / Machine Learning]]
- [[2026-05-17_anthropic-claude|Anthropic — Introducing Claude Code]]
```

### 7.3 Validation

Inherits rules from `format-spec.md` Section 6. Index Validator applies same checks.

---

## 8. Permissions matrix (full)

| File | Frontmatter | Overview | Sub-indexes/Parent | Stats | Items | Notes |
|---|---|---|---|---|---|---|
| `raw.md` | Julius | Julius | Julius | N/A | N/A | Julius |
| `wiki.md` | Julius | Julius | Julius | N/A | N/A | Julius |
| `context.md` | Julius | Julius | Julius | N/A | N/A | Julius |
| `articles.md` | Julius | Julius | Julius | Ingest Agent | Ingest Agent (append) | Julius |
| `posts.md` | Julius | Julius | Julius | Ingest Agent | Ingest Agent (append) | Julius |
| `websites.md` | Julius | Julius | Julius | Ingest Agent | Ingest Agent (append) | Julius |
| `videos.md` | Julius | Julius | Julius | Ingest Agent | Ingest Agent (append) | Julius |
| `papers.md` | Julius | Julius | Julius | Ingest Agent | Ingest Agent (append) | Julius |
| `repos.md` | Julius | Julius | Julius | Ingest Agent | Ingest Agent (append) | Julius |
| `tag.md` | Julius | Julius | Julius | Index Agent | Index Agent (append) | Julius |
| `wiki/tag/<tag>.md` | Index Agent | N/A | Index Agent | Index Agent | Index Agent | N/A |

---

## 9. Examples

### 9.1 Tầng 1 example: `raw/raw.md`

```markdown
---
type: index
level: 1
scope: raw
auto_generated: false
last_updated: 2026-05-17
---

# Raw Layer

## Overview

Ingested source material before compilation. Files đến từ external sources (articles, posts, videos, papers, repos, websites) và được Compile Agent transform thành wiki/sources/ và wiki/concepts/.

## Sub-indexes

- [[articles]] — Long-form articles, blog posts, essays
- [[posts]] — Short-form social media posts
- [[websites]] — Websites, online tools, services
- [[videos]] — Video content (YouTube, podcasts)
- [[papers]] — Academic papers, research
- [[repos]] — GitHub repositories, code projects

## Notes

<!-- Free space for Julius -->
```

### 9.2 Tầng 2 example: `raw/articles/articles.md`

```markdown
---
type: index
level: 2
scope: articles
parent: [[raw]]
auto_generated: false
items_managed_by: ingest-agent
last_updated: 2026-05-17
---

# Articles Index

## Overview

Long-form articles ingested from external sources (blogs, news sites, technical publications). Each entry links to a raw content file in this folder.

## Parent

- [[raw]]

## Stats

- Total: 42 files
- By status: 38 processed, 4 unprocessed
- By date: 5 this week, 18 this month
- Last updated: 2026-05-17

## Items

- [[2026-05-17_anthropic-claude-code]] — Introducing Claude Code (unprocessed)
- [[2026-05-16_openai-gpt5]] — GPT-5 Technical Report (processed)
- [[2026-05-15_google-gemini]] — Gemini Multi-modal Updates (processed)
...

## Notes

<!-- Free space for Julius -->
```

### 9.3 Tầng 2 example: `wiki/tag/tag.md`

```markdown
---
type: index
level: 2
scope: tags
parent: [[wiki]]
auto_generated: false
items_managed_by: index-agent
last_updated: 2026-05-17
---

# Tags Index

## Overview

Master index of all tags used across the wiki. Each entry links to a tag file (`wiki/tag/<tag>.md`) listing all files with that tag.

## Parent

- [[wiki]]

## Stats

- Total tags: 19
- Main tags: 7
- Sub tags: 12
- Most used: #ai (45), #crypto (32), #tech (28)
- Last updated: 2026-05-17

## Items

### Main Tags (Pool A)

- [[ai]] — AI / ML / LLM
- [[crypto]] — Blockchain, DeFi
- [[tech]] — Software engineering
- [[productivity]] — Workflows, KM
- [[system]] — System design
- [[economic]] — Macroeconomics
- [[politic]] — Policy, regulation

### Sub Tags (Pool B)

- [[hack]] — Exploits, vulnerabilities
- [[tools]] — Software, products
- [[automation]] — Bots, scripts
- [[vibecode]] — AI-assisted dev
- [[research]] — Academic papers
- [[tutorial]] — How-to guides
- [[opinion]] — Personal takes
- [[news]] — Recent events
- [[defi]] — DeFi protocols
- [[perpdex]] — Perpetual DEXs
- [[layer1]] — Base blockchains
- [[layer2]] — Scaling solutions

## Notes

<!-- Free space for Julius -->
```

### 9.4 Tầng 3 example: `wiki/tag/ai.md`

```markdown
---
type: index
level: 3
scope: tag
parent: [[tag]]
tag: ai
auto_generated: true
last_updated: 2026-05-17
---

# Tag: #ai

## Parent

- [[tag]]

## Stats

- Total files: 45
- Sources: 28
- Concepts: 17
- Last updated: 2026-05-17

## Files with this tag

- [[claude-code-workflow]] — Claude Code Workflow (concept)
- [[src_anthropic-claude-code]] — Anthropic Claude Code (source)
- [[src_openai-gpt5]] — OpenAI GPT-5 Report (source)
...

## Co-occurring tags

- [[tools]] — 22 co-occurrences
- [[tutorial]] — 15 co-occurrences
- [[automation]] — 12 co-occurrences
- [[research]] — 8 co-occurrences
- [[vibecode]] — 6 co-occurrences
```

---

## 10. Validation workflow

When Format Validator runs:

1. **Scan** entire `wiki/` and `raw/` and `context/` recursively
2. **For each `.md` file:**
   - Parse frontmatter
   - Read `type` field
   - Dispatch:
     - `type: concept` or `type: source` → apply `format-spec.md`
     - `type: index` → apply `index-spec.md` (this spec)
     - Other or missing → ERROR (unknown file type)
3. **For index files:**
   - Read `level` field
   - Apply level-specific rules:
     - `level: 1` → Section 3 rules
     - `level: 2` → Section 4 rules
     - `level: 3` → Section 5 rules
     - Other → ERROR (invalid level)
4. **Check:**
   - Frontmatter schema
   - Field order
   - Required sections
   - Section order
   - Stats format (Section 6)
   - Wikilink format (Section 7)
5. **Generate report** in `wiki/reviews/YYYY-MM-DD_format-report.md`

**Output Validator behavior:**
- Files with `type: index` are SKIPPED (no content quality validation)
- Output Validator focuses only on `type: concept` and `type: source`

**Hygiene Inspector behavior:**
- Index files validated for path correctness only (via `folder-structure.md`)
- Naming conventions checked (e.g., `tag.md` must exist, not `tags.md`)

---

## 11. Migration notes

Existing index files (created before this spec):
- `articles.md`, `posts.md`, `websites.md`, `videos.md`, `papers.md`, `repos.md` — currently lack frontmatter
- `context.md` — has different format

**Migration plan:**

1. **Phase 1 (manual):** Julius adds frontmatter to existing Tầng 1 + Tầng 2 files using templates from Section 9
2. **Phase 2 (Fix Agent):** Apply Hermes Format Validator reports to fix any drift
3. **Phase 3 (auto):** Ingest Agent and Index Agent take over Items/Stats management on next run

**Existing wiki/tag/<tag>.md files:**
- May need regeneration to add `parent: [[tag]]` field
- Index Agent regenerates these on next daily run after spec update

---

## 12. Change log

| Version | Date | Changes |
|---|---|---|
| 1.0 | 2026-05-17 | Initial index spec for V2 |
