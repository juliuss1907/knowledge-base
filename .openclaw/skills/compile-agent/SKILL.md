---
name: compile-agent
description: Compiles raw content from raw/ into structured wiki knowledge. Use when user says "compile new files", "process raw", "compile [filename]", "compile all unprocessed", or on daily 08:00 cron trigger. Reads raw/<type>/*.md files with status:unprocessed, generates wiki/sources/src_*.md (per-source notes) and wiki/concepts/*.md (knowledge atoms), assigns tags from TAGS.md, then updates raw file status to processed.
when_to_use: Daily 08:00 batch run for all unprocessed raw files, or on-demand when user explicitly requests compilation. Also triggered after re-compile commands during migration.
disable-model-invocation: false
user-invocable: true
allowed-tools: Read Write Edit Grep Glob Bash(date *)
---

# Compile Agent

Transforms raw content into structured wiki knowledge — the heart of the KB pipeline.

## Role

Read unprocessed files in `raw/`, produce two outputs in `wiki/`:

1. **Source note** (`wiki/sources/src_<slug>.md`) — distilled summary of the original content with metadata, key points, and tags.
2. **Concept notes** (`wiki/concepts/<concept>.md`) — knowledge atoms extracted from the source. Create new concept files or update existing ones if they already exist.

Then mark the raw file as `status: processed`.

## When to use

- Daily 08:00 cron — process all `raw/**/*.md` with `status: unprocessed`
- On-demand: "compile [filename]", "compile all new", "compile raw/articles/*"
- After migration — bulk re-compile of all raw files
- After tag taxonomy update — when Julius confirms re-tagging

## Quick start

For each unprocessed raw file:

1. **Read** raw file + frontmatter
2. **Summarize** — extract key points and generate summary (keep original language)
3. **Extract concepts** — identify 1-5 knowledge atoms worth their own concept file (create even from first source if content has depth)
4. **Assign tags** — pick 1 main-tag + 1-3 sub-tags from `TAGS.md`. Propose new tag if needed (do NOT auto-add)
5. **Write source note** → `wiki/sources/src_<slug>.md`
6. **Write/update concept notes** → `wiki/concepts/<concept-slug>.md`
7. **Update raw frontmatter** → `status: processed`, add `compiled_at: YYYY-MM-DD`
8. **Log** to `.openclaw/MEMORY.md`

## Critical rules

### Language handling
- **Keep original language** — do NOT auto-translate
- Source notes and concept notes use the same language as the raw content
- If Julius needs translation, he will request it separately: "translate [file] to Vietnamese"
- Preserve technical terms in English regardless of content language (e.g., "embedding", "fine-tuning", "prompt injection")

### Tag assignment
- **Always** read `TAGS.md` first to know current taxonomy
- **Never** invent tags not in TAGS.md
- If content needs a tag that doesn't exist → use proposal flow (see Escalation)
- Apply exactly **1 main-tag** (Pool A) + **1-3 sub-tags** (Pool B) + **1 topic** (free-form slug)

### Source vs Concept distinction
- **Source note** = "what this specific article/video/paper says" (1 source = 1 file)
- **Concept note** = "what we know about X across all sources" (1 concept = 1 file, multiple sources cited)

If 3 raw files all discuss `prompt-injection`, there are 3 source notes but only 1 concept file `prompt-injection.md` (updated cumulatively).

### Concept extraction threshold
Create a concept file if the content has **sufficient depth** to stand alone as a knowledge atom, even from the first source. Examples:
- ✅ Technical concepts: "Transformer architecture", "RAG pipeline", "DeFi exploit"
- ✅ Methodologies: "Vibe coding", "Progressive disclosure", "Agent skills pattern"
- ✅ Tools/products: "Claude Code", "Cursor", "OpenClaw"
- ❌ Trivial mentions: passing reference without explanation
- ❌ Generic terms: "AI", "blockchain" (too broad, use as tags instead)

### Re-compile behavior
If user requests "re-compile [filename]" for a file with `status: processed`:
- **Stop** and ask: "This file is already processed. Re-compile will regenerate source note and merge into concepts. Confirm? (yes/no)"
- If yes → proceed with re-compile (preserve Julius's `## Notes` in concepts)
- If no → skip

## Frontmatter schemas

### Source note (`wiki/sources/src_<slug>.md`)
```yaml
---
type: source
original: [[raw/<type>/YYYY-MM-DD_<slug>.md]]
main_tag: <pool-a>
sub_tags: [<pool-b>, ...]
topic: <slug>
date_ingested: YYYY-MM-DD
date_compiled: YYYY-MM-DD
url: <optional, from raw>
author: <optional, from raw>
---
```

### Concept note (`wiki/concepts/<concept-slug>.md`)
```yaml
---
type: concept
status: draft
main_tag: <pool-a>
sub_tags: [<pool-b>, ...]
topic: <slug>
sources:
  - [[wiki/sources/src_<slug-1>]]
  - [[wiki/sources/src_<slug-2>]]
last_updated: YYYY-MM-DD
---
```

Full schema details in `wiki/meta/format-spec.md`.

## Required sections

### Source note body
1. `# <Original title>`
2. `## Metadata` — author, date, URL, source platform
3. `## Summary` — 3-5 sentence summary (same language as source)
4. `## Key points` — bullet list (5-10 items)
5. `## Concepts referenced` — wikilinks to concept files: `[[concept-slug]]`
6. `## Original excerpts` (optional) — key quotes worth preserving

### Concept note body
1. `# <Concept name>`
2. `## Definition` — 2-3 sentence definition (same language as source)
3. `## Key ideas` — main points about this concept
4. `## Related concepts` — wikilinks: `[[other-concept]]`
5. `## Sources` — wikilinks to source files (auto-maintained)
6. `## Notes` (optional) — Julius's annotations (preserved across re-compiles)

## Constraints

### Write zones
- **Allowed:** `wiki/sources/`, `wiki/concepts/`, `wiki/drafts/` (for unclear cases)
- **Allowed (Edit):** Update raw file frontmatter only — never modify body
- **Forbidden:** `wiki/tag/`, `wiki/topic/`, `wiki/reviews/`, `wiki/meta/`

### Forbidden actions
- ❌ Deleting any raw file
- ❌ Adding tags not in `TAGS.md`
- ❌ Modifying raw file body (frontmatter status update only)
- ❌ Auto-translating content (Julius requests translation separately)
- ❌ Re-compiling processed files without explicit user confirmation

### Existing concept handling
When a concept file already exists:
- **Read** existing content first
- **Append** new source to `sources:` list in frontmatter
- **Merge** new key ideas into `## Key ideas` (avoid duplicates)
- **Preserve** `## Notes` section (Julius's annotations) — never overwrite
- **Update** `last_updated` date

## Escalation (propose to Julius)

Block compilation and ask Julius when:

### Tag proposal
Content needs a tag not in `TAGS.md`:
```
[TAG PROPOSAL]
Pool: A (main-tag) | B (sub-tag)
Proposed: #<new-tag>
Reason: <1-2 sentences>
File context: raw/<type>/<filename>
Closest existing tag: <fallback>
```

### Concept ambiguity
Cannot decide if content warrants a new concept file:
```
[CONCEPT PROPOSAL]
Source: raw/<type>/<filename>
Proposed concept: <concept-name>
Why uncertain: <reason>
Decision needed: create new | merge into <existing> | skip
```

### Language note
If content is in a rare language (not EN/VI/ZH/JA/ES/FR/DE):
```
[LANGUAGE NOTE]
Source: raw/<type>/<filename>
Language: <code>
Note: Content preserved in original language. Translation available on request.
```

→ Move to `wiki/drafts/` if language makes concept extraction unclear.

## Details

For complete process including extraction heuristics, merge logic, and error handling, see:
- [workflow.md](workflow.md) — step-by-step compilation process
- [tagging-rules.md](tagging-rules.md) — how to assign tags from TAGS.md
- [examples.md](examples.md) — sample input → output transformations
- [reference.md](reference.md) — frontmatter schemas and validation rules

## Post-compile

After successful compilation of one raw file:

1. **Verify outputs:** all written files have valid frontmatter
2. **Update raw frontmatter:**
   ```yaml
   status: processed
   compiled_at: YYYY-MM-DD
   ```
3. **Log to MEMORY.md:**
   ```markdown
   ## YYYY-MM-DD HH:MM:SS — Compiled
   - Raw: raw/<type>/<filename>
   - Source note: wiki/sources/src_<slug>.md
   - Concepts: [<concept-1>, <concept-2>, ...]
   - Tags applied: main=<x>, sub=[<y>, <z>], topic=<t>
  ```
4. **Do NOT trigger** Index Agent — runs separately at 21:00

## Batch behavior

When processing multiple files:
- Process **sequentially** (avoid race conditions on shared concept files)
- After each file, save state — if interrupted, resume from next unprocessed
- Report progress every 10 files: `Compiled X/Y, Z concepts created/updated`
- On error: skip file, log to MEMORY.md, continue batch
- Final summary: count compiled, count failed, list of new concepts, list of tag proposals

## Failure modes

| Issue | Action |
|---|---|
| Raw file missing required frontmatter | Skip + log error + flag for Julius |
| Tag proposal pending Julius approval | Move file to `wiki/drafts/`, status stays `unprocessed` |
| Existing concept file has merge conflict | Save new version to `wiki/drafts/<concept>-merge.md`, alert Julius |
| Disk full | Stop batch, alert Julius |
| Re-compile request for processed file | Ask confirmation before proceeding |
