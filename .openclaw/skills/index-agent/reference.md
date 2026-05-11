# Index Agent — Index File Format Reference

Complete specification for tag and topic index file formats.

---

## Overview

Index files are auto-generated markdown files that list all wiki content associated with a specific tag or topic. They serve as navigation hubs in Obsidian's graph view.

**Two types:**
- **Tag indexes** (`wiki/tag/<tag>.md`) — group by tag
- **Topic indexes** (`wiki/topic/<topic>.md`) — group by topic

---

## Tag Index Format

### File naming

**Pattern:** `wiki/tag/<tag>.md`

**Rules:**
- `<tag>` is the tag name without `#` prefix
- Lowercase only
- Hyphens allowed (e.g., `layer1.md`, `layer2.md`)
- No spaces, no special characters

**Examples:**
- `wiki/tag/ai.md`
- `wiki/tag/tools.md`
- `wiki/tag/layer2.md`

### File structure

```markdown
# Tag: #<tag>

Auto-generated index of all content tagged with `#<tag>`.

Last updated: YYYY-MM-DD HH:MM:SS

---

## Concepts (N)

<list of concept files>

## Sources (N)

<list of source files>

## Co-occurring tags

<list of frequently co-occurring tags>
```

### Section 1: Header

```markdown
# Tag: #<tag>
```

**Rules:**
- H1 heading (single `#`)
- Format: `Tag: #<tag>` (with hash prefix)
- Tag name matches filename

**Example:**
```markdown
# Tag: #ai
```

### Section 2: Description line

```markdown
Auto-generated index of all content tagged with `#<tag>`.
```

**Rules:**
- Plain text, no formatting
- Includes tag with `#` prefix in backticks
- Ends with period

### Section 3: Timestamp

```markdown
Last updated: YYYY-MM-DD HH:MM:SS
```

**Rules:**
- Format: `YYYY-MM-DD HH:MM:SS` (24-hour time)
- Updated every time index is regenerated
- Uses local timezone

**Example:**
```markdown
Last updated: 2026-05-07 21:00:15
```

### Section 4: Separator

```markdown
---
```

**Rules:**
- Three hyphens
- Blank line before and after

### Section 5: Concepts list

```markdown
## Concepts (N)

- [[concept-slug-1]] — main: #<main>, sub: [#<sub1>, #<sub2>], topic: <topic>
- [[concept-slug-2]] — main: #<main>, sub: [#<sub1>], topic: <topic>
...
```

**Rules:**
- H2 heading with count in parentheses
- Count = number of concept files with this tag
- If count is 0: `No concepts tagged with `#<tag>` yet.`
- Alphabetical order by slug
- Each line: wikilink + metadata

**Wikilink format:**
- `[[slug]]` — double brackets, no path, no extension
- Slug is filename without `.md`

**Metadata format:**
- ` — main: #<tag>, sub: [#<tag1>, #<tag2>], topic: <topic>`
- Space-em dash-space before metadata
- Main-tag with `#` prefix
- Sub-tags in square brackets, comma-separated, with `#` prefix
- Topic without `#` prefix (not a tag)

**Example:**
```markdown
## Concepts (3)

- [[progressive-disclosure]] — main: #ai, sub: [#tools], topic: agent-skills-pattern
- [[rag-pipeline]] — main: #ai, sub: [#tools, #tutorial], topic: rag-implementation
- [[vibe-coding]] — main: #ai, sub: [#vibecode, #opinion], topic: ai-assisted-development
```

**Empty case:**
```markdown
## Concepts (0)

No concepts tagged with `#ai` yet.
```

### Section 6: Sources list

```markdown
## Sources (N)

- [[src_slug-1]] — main: #<main>, sub: [#<sub1>, #<sub2>], topic: <topic>
- [[src_slug-2]] — main: #<main>, sub: [#<sub1>], topic: <topic>
...
```

**Rules:**
- Same format as Concepts section
- Count = number of source files with this tag
- If count is 0: `No sources tagged with `#<tag>` yet.`
- Alphabetical order by slug
- Source slugs start with `src_` prefix

**Example:**
```markdown
## Sources (5)

- [[src_anthropic-claude-code]] — main: #ai, sub: [#tools, #news], topic: claude-code-workflow
- [[src_bibek-skill-md-pattern]] — main: #ai, sub: [#tools, #tutorial], topic: agent-skills-pattern
- [[src_cursor-ai-editor]] — main: #ai, sub: [#tools], topic: cursor-editor
- [[src_karpathy-llm-intro]] — main: #ai, sub: [#tutorial], topic: llm-introduction
- [[src_vaswani-attention]] — main: #ai, sub: [#research], topic: transformer-architecture
```

### Section 7: Co-occurring tags

```markdown
## Co-occurring tags

Tags that frequently appear with `#<tag>`:
- `#<other-tag-1>` (X files)
- `#<other-tag-2>` (Y files)
- `#<other-tag-3>` (Z files)
...
```

**Rules:**
- H2 heading
- Intro line: `Tags that frequently appear with `#<tag>`:`
- List top 5 co-occurring tags by frequency
- Format: backticks around tag, count in parentheses
- Descending order by count
- Omit section if <2 total files with this tag

**Co-occurrence definition:**
- Two tags co-occur if they appear in the same file
- Count = number of files containing both tags
- Includes both main-tag and sub-tag co-occurrences

**Example:**
```markdown
## Co-occurring tags

Tags that frequently appear with `#ai`:
- `#tools` (15 files)
- `#tutorial` (8 files)
- `#research` (6 files)
- `#vibecode` (3 files)
- `#hack` (2 files)
```

**Insufficient data case:**
```markdown
## Co-occurring tags

Tags that frequently appear with `#perpdex`:
- `#crypto` (1 file)

(Insufficient data for meaningful co-occurrence analysis)
```

---

## Topic Index Format

### File naming

**Pattern:** `wiki/topic/<topic>.md`

**Rules:**
- `<topic>` is the topic slug
- Lowercase only
- Hyphens for spaces
- Max 50 characters
- No special characters

**Examples:**
- `wiki/topic/claude-code-workflow.md`
- `wiki/topic/defi-security.md`
- `wiki/topic/rag-implementation.md`

### File structure

```markdown
# Topic: <topic>

Auto-generated index of all content with topic `<topic>`.

Last updated: YYYY-MM-DD HH:MM:SS

---

## Concepts (N)

<list of concept files>

## Sources (N)

<list of source files>

## Related topics

<list of topics with shared files>
```

### Section 1: Header

```markdown
# Topic: <topic>
```

**Rules:**
- H1 heading (single `#`)
- Format: `Topic: <topic>` (no hash prefix)
- Topic name matches filename

**Example:**
```markdown
# Topic: claude-code-workflow
```

### Section 2: Description line

```markdown
Auto-generated index of all content with topic `<topic>`.
```

**Rules:**
- Plain text, no formatting
- Includes topic in backticks (no `#` prefix)
- Ends with period

### Section 3: Timestamp

Same as tag index.

### Section 4: Separator

Same as tag index.

### Section 5: Concepts list

```markdown
## Concepts (N)

- [[concept-slug-1]] — main: #<main>, sub: [#<sub1>, #<sub2>]
- [[concept-slug-2]] — main: #<main>, sub: [#<sub1>]
...
```

**Rules:**
- Same as tag index, but **no topic in metadata** (redundant)
- Format: `[[slug]] — main: #<tag>, sub: [#<tag1>, #<tag2>]`
- Alphabetical order by slug

**Example:**
```markdown
## Concepts (2)

- [[claude-code]] — main: #ai, sub: [#tools, #vibecode]
- [[vibe-coding]] — main: #ai, sub: [#vibecode, #opinion]
```

### Section 6: Sources list

```markdown
## Sources (N)

- [[src_slug-1]] — main: #<main>, sub: [#<sub1>, #<sub2>]
- [[src_slug-2]] — main: #<main>, sub: [#<sub1>]
...
```

**Rules:**
- Same as Concepts, no topic in metadata
- Alphabetical order by slug

**Example:**
```markdown
## Sources (3)

- [[src_anthropic-claude-code]] — main: #ai, sub: [#tools, #news]
- [[src_claude-code-daily-workflow]] — main: #ai, sub: [#tools, #tutorial]
- [[src_claude-code-tips]] — main: #ai, sub: [#tools, #tutorial]
```

### Section 7: Related topics

```markdown
## Related topics

Topics that share concepts/sources with `<topic>`:
- `<related-topic-1>` (X shared files)
- `<related-topic-2>` (Y shared files)
- `<related-topic-3>` (Z shared files)
...
```

**Rules:**
- H2 heading
- Intro line: `Topics that share concepts/sources with `<topic>`:`
- List top 5 related topics by overlap
- Format: backticks around topic, count in parentheses
- Descending order by shared file count
- Omit section if no overlap with other topics

**Overlap definition:**
- Two topics are related if they share at least one file
- Count = number of files present in both topics
- Includes both concepts and sources

**Example:**
```markdown
## Related topics

Topics that share concepts/sources with `claude-code-workflow`:
- `ai-assisted-development` (2 shared files)
- `agent-skills-pattern` (1 shared file)
- `cursor-editor` (1 shared file)
```

**No overlap case:**
```markdown
## Related topics

No topics share files with `claude-code-workflow` yet.
```

---

## Metadata Format Specification

### Main-tag field

**Format:** `main: #<tag>`

**Rules:**
- Exactly one tag
- Tag must be from Pool A (TAGS.md)
- Hash prefix required
- Lowercase only

**Valid:**
- `main: #ai`
- `main: #crypto`
- `main: #tech`

**Invalid:**
- `main: ai` (missing hash)
- `main: #AI` (uppercase)
- `main: #ai, #crypto` (multiple tags)

### Sub-tags field

**Format:** `sub: [#<tag1>, #<tag2>, ...]`

**Rules:**
- Square brackets required (even for single tag)
- 1-3 tags (minimum 1, maximum 3)
- Tags must be from Pool B (TAGS.md)
- Hash prefix required for each tag
- Comma-separated with space after comma
- Lowercase only

**Valid:**
- `sub: [#tools]`
- `sub: [#tools, #tutorial]`
- `sub: [#hack, #defi, #news]`

**Invalid:**
- `sub: #tools` (missing brackets)
- `sub: [tools]` (missing hash)
- `sub: [#tools,#tutorial]` (no space after comma)
- `sub: [#a, #b, #c, #d]` (too many tags)

### Topic field

**Format:** `topic: <slug>`

**Rules:**
- No hash prefix (not a tag)
- Lowercase-hyphen format
- Max 50 characters
- No special characters

**Valid:**
- `topic: claude-code-workflow`
- `topic: defi-security`
- `topic: rag-implementation`

**Invalid:**
- `topic: #claude-code-workflow` (has hash)
- `topic: Claude Code Workflow` (spaces, uppercase)
- `topic: claude_code_workflow` (underscores)

---

## Sorting Rules

### Alphabetical sorting

All file lists within index files are sorted alphabetically by slug:

**Concepts:**
```markdown
- [[agent-skills]]
- [[claude-code]]
- [[progressive-disclosure]]
- [[rag-pipeline]]
- [[vibe-coding]]
```

**Sources:**
```markdown
- [[src_anthropic-claude-code]]
- [[src_bibek-skill-md-pattern]]
- [[src_cursor-ai-editor]]
- [[src_karpathy-llm-intro]]
```

**Rules:**
- Case-insensitive sort (treat uppercase as lowercase)
- Hyphens sort before letters
- Numbers sort before letters
- `src_` prefix does not affect sort order within sources section

### Frequency sorting

Co-occurring tags and related topics are sorted by frequency (descending):

**Co-occurring tags:**
```markdown
- `#tools` (15 files)      ← highest count first
- `#tutorial` (8 files)
- `#research` (6 files)
- `#vibecode` (3 files)
- `#hack` (2 files)        ← lowest count last
```

**Related topics:**
```markdown
- `ai-assisted-development` (5 shared files)  ← highest overlap first
- `agent-skills-pattern` (3 shared files)
- `cursor-editor` (1 shared file)             ← lowest overlap last
```

**Tie-breaking:**
- If counts are equal, sort alphabetically by tag/topic name

---

## Count Accuracy

### Concept/Source counts

Counts in section headers must match the number of items listed:

**Correct:**
```markdown
## Concepts (3)

- [[concept-1]]
- [[concept-2]]
- [[concept-3]]
```

**Incorrect:**
```markdown
## Concepts (5)    ← count says 5

- [[concept-1]]
- [[concept-2]]
- [[concept-3]]   ← only 3 items listed
```

### Co-occurrence counts

Counts in parentheses must match actual file overlap:

**Correct:**
```markdown
- `#tools` (15 files)  ← exactly 15 files have both this tag and #tools
```

**Incorrect:**
```markdown
- `#tools` (15 files)  ← count is wrong, actual overlap is 12
```

---

## Whitespace Rules

### Blank lines

**Required blank lines:**
- After header (before description)
- Before and after separator `---`
- After each section heading
- After intro lines in co-occurrence/related sections

**No blank lines:**
- Between list items
- Between metadata fields

**Example:**
```markdown
# Tag: #ai

Auto-generated index...

Last updated: ...

---

## Concepts (3)

- [[concept-1]] — ...
- [[concept-2]] — ...
- [[concept-3]] — ...

## Sources (5)
```

### Indentation

**No indentation:**
- All content is left-aligned
- No tabs or spaces before list items
- No indentation for nested structures

---

## Special Characters

### Allowed characters

**In slugs:**
- Lowercase letters: `a-z`
- Numbers: `0-9`
- Hyphens: `-`

**In metadata:**
- Hash: `#` (for tags only)
- Square brackets: `[` `]` (for sub-tags array)
- Comma: `,` (for sub-tags separator)
- Colon: `:` (for field separator)
- Backticks: `` ` `` (for inline code)
- Parentheses: `(` `)` (for counts)

### Forbidden characters

**In slugs:**
- Spaces
- Underscores (except `src_` prefix)
- Special characters: `!@#$%^&*()+={}[]|\\:;"'<>,.?/`

**In tags:**
- Spaces
- Uppercase letters
- Special characters (except hyphen)

---

## Validation Rules

Before writing an index file, verify:

### Structure validation
- [ ] File has H1 header with correct format
- [ ] Description line present
- [ ] Timestamp present and valid format
- [ ] Separator `---` present
- [ ] All required sections present (Concepts, Sources)
- [ ] Optional sections present if applicable

### Content validation
- [ ] All wikilinks use double brackets `[[slug]]`
- [ ] All slugs are valid (lowercase-hyphen)
- [ ] All tags have `#` prefix
- [ ] All sub-tags in square brackets
- [ ] All counts match actual list lengths
- [ ] All lists sorted correctly

### Metadata validation
- [ ] Main-tag is from Pool A
- [ ] Sub-tags are from Pool B
- [ ] Sub-tags count is 1-3
- [ ] Topic has no `#` prefix
- [ ] No duplicate entries in lists

---

## Error Cases

### Malformed wikilink

**Wrong:**
```markdown
- [concept-slug] — ...           ← single brackets
- [[concept-slug.md]] — ...      ← includes extension
- [[wiki/concepts/slug]] — ...   ← includes path
```

**Right:**
```markdown
- [[concept-slug]] — ...
```

### Missing metadata

**Wrong:**
```markdown
- [[concept-slug]]               ← no metadata
```

**Right:**
```markdown
- [[concept-slug]] — main: #ai, sub: [#tools], topic: example
```

### Invalid tag format

**Wrong:**
```markdown
- [[slug]] — main: ai, sub: [tools]           ← missing hashes
- [[slug]] — main: #ai, sub: #tools           ← sub-tags not in brackets
- [[slug]] — main: #ai, sub: [#tools,#hack]   ← no space after comma
```

**Right:**
```markdown
- [[slug]] — main: #ai, sub: [#tools, #hack]
```

---

## File Size Considerations

### Typical sizes

| Wiki size | Files per tag | Index file size |
|---|---|---|
| Small | 5-20 | 1-3 KB |
| Medium | 20-50 | 3-8 KB |
| Large | 50-100 | 8-15 KB |
| Very large | 100+ | 15-30 KB |

### Performance impact

- Index files are read by Obsidian on graph view load
- Large index files (>50 KB) may slow graph rendering
- Consider splitting very large tags into sub-categories if >200 files

---

## Related Documentation

- [SKILL.md](SKILL.md) — Index Agent overview
- [workflow.md](workflow.md) — Step-by-step indexing process
- [examples.md](examples.md) — Sample index files
- `TAGS.md` (root) — Tag taxonomy (source of truth)
- `wiki/meta/format-spec.md` — Wiki file format specification
