# Ingest Agent — Complete Workflow

Detailed step-by-step process for ingesting external content into the raw/ layer.

---

## Overview

This workflow covers the complete ingestion process from content identification to file creation. The Ingest Agent follows this sequence for every piece of content, whether triggered automatically or invoked manually.

---

## Step 1: Identify Content Type

Determine which of the 6 content types applies:

| Type | Indicators |
|---|---|
| `article` | Blog post, news article, long-form content with author |
| `post` | Social media post (X/Twitter, LinkedIn, threads) |
| `video` | YouTube, Vimeo, or other video platform links |
| `paper` | Academic paper, arXiv, research publication |
| `repo` | GitHub, GitLab repository |
| `website` | Tool landing page, product page, documentation site |

**Decision logic:**
- URL contains `youtube.com`, `vimeo.com` → `video`
- URL contains `github.com`, `gitlab.com` → `repo`
- URL contains `arxiv.org`, ends with `.pdf`, has DOI → `paper`
- URL is social platform (twitter.com, x.com, linkedin.com) → `post`
- URL is blog/news domain with article path → `article`
- Everything else → `website`

**If ambiguous:** Ask Julius which type to use.

---

## Step 2: Fetch Content

### For articles

```bash
# Try curl first
curl -L -A "Mozilla/5.0" "${url}" > temp.html

# Extract main content (strip nav, ads, footer)
# Use readability heuristics or extract <article> tag
```

**Fallback:** If curl fails or returns paywall, ask Julius to provide content manually.

### For posts (X/Twitter)

```bash
# If URL is provided, fetch via curl
curl -L "${url}" > temp.html

# Extract tweet text, thread if multi-part
# Preserve @mentions and #hashtags as plain text
```

**Note:** X/Twitter may require authentication. If fetch fails, ask Julius to paste content.

### For videos

```bash
# Extract video ID from URL
# Fetch metadata via yt-dlp or API if available
yt-dlp --skip-download --write-info-json "${url}"

# If transcript available, fetch it
yt-dlp --skip-download --write-auto-sub --sub-lang en "${url}"
```

**Fallback:** If yt-dlp not available, extract title and description from page HTML.

### For papers

```bash
# If arXiv URL, fetch via API
curl "https://export.arxiv.org/api/query?id_list=${arxiv_id}" > metadata.xml

# If PDF URL, download and convert to markdown (if possible)
curl -L "${url}" > paper.pdf
# Note: PDF→MD conversion requires external tool, may not be available
```

**Fallback:** Extract abstract and metadata from landing page HTML.

### For repos

```bash
# Fetch README via GitHub API or raw URL
curl -L "https://raw.githubusercontent.com/${owner}/${repo}/main/README.md" > readme.md

# Fetch repo metadata
curl -L "https://api.github.com/repos/${owner}/${repo}" > metadata.json
```

**Fallback:** Clone repo shallowly if API fails:
```bash
git clone --depth 1 "${url}" temp_repo
cat temp_repo/README.md
```

### For websites

```bash
# Fetch landing page
curl -L -A "Mozilla/5.0" "${url}" > temp.html

# Extract main content (hero section, features, description)
```

---

## Step 3: Extract Metadata

From fetched content, extract:

| Field | Source |
|---|---|
| `title` | `<title>` tag, `<h1>`, or og:title meta tag |
| `author` | `<meta name="author">`, byline, or @username for posts |
| `date_published` | `<meta property="article:published_time">`, or date in URL |
| `source` | Domain name (e.g., `anthropic.com`, `twitter.com`) |
| `url` | Original URL provided by user |

**Date parsing:**
- Try ISO 8601 format first: `YYYY-MM-DD`
- Parse common formats: `May 4, 2026`, `04/05/2026`, `2026-05-04T10:30:00Z`
- If unparseable, use `date_ingested` as fallback

**Missing metadata:**
- `title` missing → use first 50 chars of content as title
- `author` missing → use `[unknown]`
- `date_published` missing → use `date_ingested`

---

## Step 4: Generate Slug

Transform title into URL-safe slug:

```python
# Pseudocode
slug = title.lower()
slug = slug.replace(' ', '-')
slug = re.sub(r'[^a-z0-9-]', '', slug)  # Remove non-alphanumeric except hyphens
slug = re.sub(r'-+', '-', slug)          # Collapse multiple hyphens
slug = slug[:50]                         # Truncate to 50 chars
slug = slug.strip('-')                   # Remove leading/trailing hyphens
```

**Examples:**
- `"Claude Code Skills Guide"` → `claude-code-skills-guide`
- `"DeFi Hack: $10M Stolen from Curve Pool"` → `defi-hack-10m-stolen-from-curve-pool`
- `"AI Safety & Alignment Research"` → `ai-safety-alignment-research`

**Collision handling:**
Check if `raw/<type>/YYYY-MM-DD_<slug>.md` exists:
- If exists → append `-2`: `YYYY-MM-DD_<slug>-2.md`
- If that exists → append `-3`, and so on

---

## Step 5: Clean Content

Remove unwanted elements before writing:

### For articles
- Strip `<script>`, `<style>`, `<nav>`, `<footer>`, `<aside>` tags
- Remove ads, social share buttons, comment sections
- Preserve `<article>`, `<main>`, or content within `.post-content` class
- Convert HTML to markdown:
  - `<h1>` → `# `
  - `<h2>` → `## `
  - `<p>` → paragraph
  - `<a href="...">` → `[text](url)`
  - `<code>` → `` `code` ``
  - `<pre><code>` → ` ```language\ncode\n``` `

### For posts
- Keep original formatting (line breaks, @mentions, #hashtags)
- If thread, concatenate with `---` separator between tweets
- Preserve URLs as markdown links

### For videos
- Store transcript as-is if available
- If no transcript, write summary from description

### For papers
- Keep abstract, introduction, conclusion
- Preserve section headings
- Keep citations as plain text or markdown links

### For repos
- Keep README.md content as-is
- Preserve code blocks and formatting

### For websites
- Extract hero section, features list, pricing if relevant
- Remove navigation, footer, cookie banners

---

## Step 6: Construct Frontmatter

Build YAML frontmatter with extracted metadata:

```yaml
---
type: <article|post|video|paper|repo|website>
title: <extracted or generated title>
url: <original URL>
author: <extracted author or [unknown]>
date_published: YYYY-MM-DD
date_ingested: YYYY-MM-DD  # Today's date
status: unprocessed
source: <domain or platform>
---
```

**Validation before writing:**
- [ ] `type` is one of 6 allowed values
- [ ] `title` is non-empty string
- [ ] `date_ingested` is today's date in YYYY-MM-DD format
- [ ] `status` is exactly `unprocessed`
- [ ] All dates are valid YYYY-MM-DD format

---

## Step 7: Write File

Construct final file path:

```
raw/<type>/YYYY-MM-DD_<slug>.md
```

Where:
- `<type>` is one of: `articles`, `posts`, `videos`, `papers`, `repos`, `websites`
- `YYYY-MM-DD` is `date_published` if known, else `date_ingested`
- `<slug>` is generated from title (max 50 chars)

**Write operation:**

```bash
cat > "raw/${type}/${date}_${slug}.md" << 'EOF'
---
type: ${type}
title: ${title}
url: ${url}
author: ${author}
date_published: ${date_published}
date_ingested: ${date_ingested}
status: unprocessed
source: ${source}
---

${cleaned_content}
EOF
```

**Verify after write:**
```bash
# Check file exists
test -f "raw/${type}/${date}_${slug}.md" && echo "✓ File created"

# Check frontmatter is valid YAML
head -n 20 "raw/${type}/${date}_${slug}.md" | grep -q "^---$" && echo "✓ Frontmatter valid"

# Check status field
grep -q "status: unprocessed" "raw/${type}/${date}_${slug}.md" && echo "✓ Status set"
```

---

## Step 8: Log to Memory

Append entry to `.openclaw/MEMORY.md`:

```markdown
## YYYY-MM-DD HH:MM:SS — Ingested

- **File:** raw/<type>/YYYY-MM-DD_<slug>.md
- **Source:** <url>
- **Type:** <type>
- **Title:** <title>
```

**Do not log:**
- Full content (too verbose)
- Author or metadata (already in file)

---

## Step 9: Confirm to User

Return confirmation message:

```
✓ Ingested: raw/<type>/YYYY-MM-DD_<slug>.md
  Title: <title>
  Source: <source>
  Status: unprocessed (ready for compilation)
```

**Do NOT:**
- Automatically trigger Compile Agent
- Move or modify the file after creation
- Add tags or process content further

The file now waits in `raw/` with `status: unprocessed` until Compile Agent processes it.

---

## Error Handling

### Fetch failures

| Error | Action |
|---|---|
| 404 Not Found | Ask Julius to verify URL |
| 403 Forbidden / Paywall | Ask Julius to provide content manually |
| Timeout | Retry once with 30s timeout, then escalate |
| SSL error | Try with `--insecure` flag, warn Julius |

### Metadata extraction failures

| Missing field | Fallback |
|---|---|
| `title` | Use first 50 chars of content |
| `author` | Use `[unknown]` |
| `date_published` | Use `date_ingested` |
| `source` | Extract domain from URL |

### Write failures

| Error | Action |
|---|---|
| Permission denied | Check `raw/<type>/` exists and is writable |
| Disk full | Report to Julius, cannot proceed |
| Invalid filename | Sanitize slug further, retry |

---

## Edge Cases

### Multi-part threads (X/Twitter)

If post is part of a thread:
1. Fetch all tweets in thread
2. Concatenate with `---` separator
3. Use first tweet's date as `date_published`
4. Title from first tweet

### Video without transcript

If transcript unavailable:
1. Use video description as content
2. Add note: `[Transcript not available]`
3. Summarize key points from description if possible

### Paper behind paywall

If paper PDF is paywalled:
1. Fetch abstract from landing page
2. Add note: `[Full text not available]`
3. Include DOI or arXiv ID for reference

### Repo without README

If repo has no README.md:
1. Use repo description from GitHub API
2. List main files/directories
3. Add note: `[No README found]`

### Content in non-English language

If content is not English or Vietnamese:
1. Store original content as-is
2. Add `language: <code>` to frontmatter (e.g., `language: zh`)
3. Flag in MEMORY.md for Julius to review
4. Do NOT attempt auto-translation (Compile Agent handles this)

---

## Performance Considerations

### Batch ingestion

When ingesting multiple items:
1. Process sequentially (avoid parallel writes to same folder)
2. Log all items to MEMORY.md in one append operation
3. Confirm batch completion with count

### Large content

If content exceeds 100KB:
1. Proceed with ingestion (no size limit for raw files)
2. Note in MEMORY.md: `[Large file: XXX KB]`
3. Compile Agent will handle chunking if needed

### Rate limiting

If fetching from same domain repeatedly:
1. Add 1-second delay between requests
2. Respect `robots.txt` if present
3. Use polite User-Agent string

---

## Security Considerations

### URL validation

Before fetching:
```bash
# Check URL is HTTP/HTTPS
echo "${url}" | grep -qE '^https?://' || exit 1

# Avoid localhost/private IPs (SSRF protection)
echo "${url}" | grep -qE '(localhost|127\.0\.0\.1|192\.168\.|10\.|172\.(1[6-9]|2[0-9]|3[01]))' && exit 1
```

### Content sanitization

- Strip `<script>` tags completely (XSS risk)
- Escape special characters in frontmatter values
- Do not execute any code found in content

### Credential handling

- Never log API keys or tokens to MEMORY.md
- If URL contains credentials, strip them before logging
- Warn Julius if content requires authentication

---

## Workflow Summary (Quick Reference)

```
1. Identify type (article/post/video/paper/repo/website)
   ↓
2. Fetch content (curl/API/git)
   ↓
3. Extract metadata (title/author/date/source)
   ↓
4. Generate slug (lowercase-hyphen, max 50 chars)
   ↓
5. Clean content (strip ads/nav, convert to markdown)
   ↓
6. Construct frontmatter (YAML with required fields)
   ↓
7. Write file (raw/<type>/YYYY-MM-DD_<slug>.md)
   ↓
8. Log to MEMORY.md (timestamp + filename + source)
   ↓
9. Confirm to user (filename + status)
```

**Total time per item:** 5-30 seconds depending on content size and fetch method.
