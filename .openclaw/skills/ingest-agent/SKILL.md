---
name: ingest-agent
description: Ingests external content into raw/ layer. Use when user says "ingest this article", "save this post", "add this to KB", "ingest [URL]", or provides content to store. Handles articles, posts, videos, papers, repos, and websites. Creates properly formatted raw/<type>/YYYY-MM-DD_<slug>.md files with frontmatter.
when_to_use: Daily monitoring of sources, on-demand when user shares links or content, or when Julius says "ingest" followed by a URL or content description.
disable-model-invocation: false
user-invocable: true
allowed-tools: Write Bash(curl *) Bash(git *)
---

# Ingest Agent

Receives external content and stores it in the `raw/` layer with proper structure and metadata.

## Role

Transform external content (articles, social posts, videos, papers, repos, websites) into structured markdown files in `raw/<type>/` with complete frontmatter. This is the entry point for all knowledge into the KB.

## When to use

- User shares a URL and asks to save it
- User pastes content and says "add this to KB"
- Daily monitoring detects new content from tracked sources
- Julius explicitly says "ingest [URL or description]"

## Quick start

1. **Identify content type** — article, post, video, paper, repo, or website
2. **Extract metadata** — title, author, date, URL, source
3. **Generate slug** — lowercase-hyphen from title
4. **Create file** — `raw/<type>/YYYY-MM-DD_<slug>.md`
5. **Write frontmatter + content** — follow format in [reference.md](reference.md)
6. **Verify** — file exists, frontmatter valid, status set to `unprocessed`

## Frontmatter schema

Every raw file must include:

```yaml
---
type: <article|post|video|paper|repo|website>
title: <original title>
url: <source URL>
author: <author name or handle>
date_published: YYYY-MM-DD
date_ingested: YYYY-MM-DD
status: unprocessed
source: <domain or platform name>
---
```

**Required fields:** `type`, `title`, `date_ingested`, `status`

**Optional but recommended:** `url`, `author`, `date_published`, `source`

## Content extraction rules

### Articles
- Fetch full text via curl or reader mode
- Strip ads, navigation, footers
- Preserve headings, lists, code blocks
- Keep inline links

### Posts (X, threads, LinkedIn)
- Capture full thread if multi-part
- Preserve @mentions and #hashtags as plain text
- Include engagement metrics in frontmatter if available

### Videos
- Extract title, description, transcript if available
- Store video URL in frontmatter
- Summarize key points if transcript exists

### Papers
- Prefer markdown conversion over PDF
- Extract abstract, authors, publication venue
- Store DOI or arXiv ID in frontmatter

### Repos
- Capture README.md content
- Extract repo description, stars, language
- Store GitHub/GitLab URL

### Websites
- Store landing page content or tool description
- Capture pricing, features if relevant
- Note if requires signup/API key

## File naming

Pattern: `YYYY-MM-DD_<slug>.md`

- **YYYY-MM-DD** — `date_published` if known, else `date_ingested`
- **slug** — lowercase, hyphens, max 50 chars, derived from title

Examples:
- `2026-05-04_claude-code-skills-guide.md`
- `2026-05-03_defi-hack-curve-pool.md`
- `2026-05-02_anthropic-releases-opus-5.md`

## Constraints

### Write zones
- **Allowed:** `raw/<type>/` only
- **Forbidden:** `wiki/`, `.openclaw/`, `.hermes/`, root files

### Validation
Before writing, check:
- [ ] Content type matches one of 6 allowed types
- [ ] Slug is unique (no duplicate filename in target folder)
- [ ] Frontmatter includes all required fields
- [ ] Date format is YYYY-MM-DD
- [ ] Status is `unprocessed`

### Error handling
- **Duplicate slug:** Append `-2`, `-3`, etc.
- **Missing metadata:** Use placeholder `[unknown]` and flag in MEMORY.md
- **Fetch failure:** Retry once, then ask Julius for manual input
- **Invalid content type:** Ask Julius which type to use

## Escalation

Ask Julius when:
- Content doesn't fit any of the 6 types
- URL requires authentication or paywall bypass
- Content is in a language other than English/Vietnamese
- Metadata is ambiguous (e.g., multiple authors, unclear date)

## Details

For complete workflow including fetch strategies, content cleaning, and edge case handling, see:
- [workflow.md](workflow.md) — step-by-step ingestion process
- [examples.md](examples.md) — sample raw files for each content type
- [reference.md](reference.md) — frontmatter field definitions

## Post-ingest

After writing the file:
1. Confirm: `Ingested: raw/<type>/YYYY-MM-DD_<slug>.md`
2. Log to `.openclaw/MEMORY.md`: timestamp, filename, source URL
3. Do NOT compile — Compile Agent handles that separately
