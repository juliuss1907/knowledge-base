# Index Agent — Complete Workflow

Detailed step-by-step process for maintaining tag and topic indexes.

---

## Overview

This workflow scans all wiki files, extracts tags and topics, and generates index files:
- **Input:** All files in `wiki/sources/` + `wiki/concepts/`
- **Output:** Index files in `wiki/tag/` + `wiki/topic/`
- **Side effect:** Delete orphaned index files

Total time: 5-60 seconds depending on wiki size (100-1000 files).

---

## Step 1: Scan Wiki Files

### 1.1 Find all wiki content files

```bash
# Find all markdown files in sources and concepts
find wiki/sources/ wiki/concepts/ -name "*.md" -type f
```

**Expected count:**
- `wiki/sources/`: ~80-200 files (one per raw file compiled)
- `wiki/concepts/`: ~50-150 files (knowledge atoms)
- Total: ~130-350 files typical

**Sort order:**
- Alphabetical by path (for consistent processing)

### 1.2 Read frontmatter from each file

For each file found:

```bash
# Extract frontmatter (between first two --- markers)
sed -n '/^---$/,/^---$/p' <file> | sed '1d;$d'
```

**Parse YAML fields:**
- `type` — must be `source` or `concept`
- `main_tag` — single tag from Pool A
- `sub_tags` — array of 1-3 tags from Pool B
- `topic` — free-form slug

**Validation:**
- If frontmatter missing → skip file, log warning
- If YAML invalid → skip file, log error
- If required fields missing → skip file, log error

**Build in-memory structure:**
```python
# Pseudocode
files = []
for file in wiki_files:
    frontmatter = parse_yaml(file)
    if valid(frontmatter):
        files.append({
            'path': file,
            'type': frontmatter['type'],
            'main_tag': frontmatter['main_tag'],
            'sub_tags': frontmatter['sub_tags'],
            'topic': frontmatter['topic'],
            'slug': extract_slug(file)
        })
```

---

## Step 2: Validate Tags Against Taxonomy

### 2.1 Load TAGS.md

```bash
cat TAGS.md
```

**Parse:**
- Pool A tags (7 main-tags)
- Pool B tags (12 sub-tags)

**Build whitelist:**
```python
allowed_tags = {
    'main': ['ai', 'crypto', 'tech', 'productivity', 'system', 'economic', 'politic'],
    'sub': ['hack', 'tools', 'automation', 'vibecode', 'research', 'tutorial', 
            'opinion', 'news', 'defi', 'perpdex', 'layer1', 'layer2']
}
```

### 2.2 Check each file's tags

For each file in memory:

```python
# Check main_tag
if file['main_tag'] not in allowed_tags['main']:
    log_error(f"[INVALID TAG] {file['path']}: main_tag={file['main_tag']}")
    file['invalid_main'] = True

# Check sub_tags
for tag in file['sub_tags']:
    if tag not in allowed_tags['sub']:
        log_error(f"[INVALID TAG] {file['path']}: sub_tag={tag}")
        file['invalid_subs'] = file.get('invalid_subs', []) + [tag]
```

**Action on invalid tags:**
- Log to MEMORY.md
- Do NOT create index file for invalid tag
- Still include file in valid tag indexes

---

## Step 3: Group Files by Tag

### 3.1 Build tag → files mapping

```python
tag_index = {}

for file in files:
    # Add to main_tag index
    if not file.get('invalid_main'):
        main = file['main_tag']
        if main not in tag_index:
            tag_index[main] = {'concepts': [], 'sources': []}
        
        if file['type'] == 'concept':
            tag_index[main]['concepts'].append(file)
        else:
            tag_index[main]['sources'].append(file)
    
    # Add to sub_tags indexes
    for tag in file['sub_tags']:
        if tag not in file.get('invalid_subs', []):
            if tag not in tag_index:
                tag_index[tag] = {'concepts': [], 'sources': []}
            
            if file['type'] == 'concept':
                tag_index[tag]['concepts'].append(file)
            else:
                tag_index[tag]['sources'].append(file)
```

**Result:**
```python
tag_index = {
    'ai': {
        'concepts': [file1, file2, ...],
        'sources': [file10, file11, ...]
    },
    'tools': {
        'concepts': [file3, file4, ...],
        'sources': [file12, file13, ...]
    },
    ...
}
```

### 3.2 Sort files within each tag

For each tag's file lists:

```python
# Sort concepts alphabetically by slug
tag_index[tag]['concepts'].sort(key=lambda f: f['slug'])

# Sort sources alphabetically by slug
tag_index[tag]['sources'].sort(key=lambda f: f['slug'])
```

---

## Step 4: Calculate Co-occurrence

### 4.1 Build co-occurrence matrix

For each pair of tags, count how many files have both:

```python
co_occurrence = {}

for file in files:
    # Get all tags for this file (main + subs)
    file_tags = [file['main_tag']] + file['sub_tags']
    
    # For each pair of tags in this file
    for i, tag1 in enumerate(file_tags):
        for tag2 in file_tags[i+1:]:
            pair = tuple(sorted([tag1, tag2]))
            co_occurrence[pair] = co_occurrence.get(pair, 0) + 1
```

**Result:**
```python
co_occurrence = {
    ('ai', 'tools'): 15,      # 15 files have both #ai and #tools
    ('ai', 'automation'): 8,
    ('crypto', 'defi'): 12,
    ('crypto', 'hack'): 5,
    ...
}
```

### 4.2 Build per-tag co-occurrence lists

For each tag, find top 5 co-occurring tags:

```python
tag_co_occur = {}

for tag in tag_index.keys():
    # Find all pairs involving this tag
    pairs = [(other, count) for (t1, t2), count in co_occurrence.items() 
             if tag in (t1, t2) and (other := t2 if t1 == tag else t1)]
    
    # Sort by count descending, take top 5
    top_5 = sorted(pairs, key=lambda x: -x[1])[:5]
    tag_co_occur[tag] = top_5
```

**Result:**
```python
tag_co_occur = {
    'ai': [('tools', 15), ('automation', 8), ('research', 6), ...],
    'crypto': [('defi', 12), ('hack', 5), ('layer2', 4), ...],
    ...
}
```

---

## Step 5: Group Files by Topic

### 5.1 Build topic → files mapping

```python
topic_index = {}

for file in files:
    topic = file['topic']
    if topic not in topic_index:
        topic_index[topic] = {'concepts': [], 'sources': []}
    
    if file['type'] == 'concept':
        topic_index[topic]['concepts'].append(file)
    else:
        topic_index[topic]['sources'].append(file)
```

**Result:**
```python
topic_index = {
    'claude-code-skills': {
        'concepts': [file1, file2],
        'sources': [file10, file11, file12]
    },
    'defi-hack-curve-pool': {
        'concepts': [file3],
        'sources': [file13]
    },
    ...
}
```

### 5.2 Sort files within each topic

```python
for topic in topic_index:
    topic_index[topic]['concepts'].sort(key=lambda f: f['slug'])
    topic_index[topic]['sources'].sort(key=lambda f: f['slug'])
```

---

## Step 6: Calculate Topic Overlap

### 6.1 Build topic overlap matrix

For each pair of topics, count shared files:

```python
topic_overlap = {}

for topic1 in topic_index:
    files1 = set([f['path'] for f in topic_index[topic1]['concepts'] + 
                                    topic_index[topic1]['sources']])
    
    for topic2 in topic_index:
        if topic1 >= topic2:  # Avoid duplicates
            continue
        
        files2 = set([f['path'] for f in topic_index[topic2]['concepts'] + 
                                        topic_index[topic2]['sources']])
        
        shared = len(files1 & files2)
        if shared > 0:
            pair = tuple(sorted([topic1, topic2]))
            topic_overlap[pair] = shared
```

### 6.2 Build per-topic related topics lists

For each topic, find top 5 related topics:

```python
topic_related = {}

for topic in topic_index.keys():
    # Find all pairs involving this topic
    pairs = [(other, count) for (t1, t2), count in topic_overlap.items() 
             if topic in (t1, t2) and (other := t2 if t1 == topic else t1)]
    
    # Sort by count descending, take top 5
    top_5 = sorted(pairs, key=lambda x: -x[1])[:5]
    topic_related[topic] = top_5
```

---

## Step 7: Write Tag Index Files

For each tag in `tag_index`:

### 7.1 Generate file content

```python
def generate_tag_index(tag, data, co_occur, all_files):
    """Generate level 3 tag index per index-spec.md §5."""
    
    today = datetime.now().strftime('%Y-%m-%d')
    
    # Frontmatter
    content = f"""---
type: index
level: 3
scope: tag
parent: [[tag]]
tag: {tag}
auto_generated: true
last_updated: {today}
---

# Tag: #{tag}

## Parent

- [[tag]]

## Stats

- Total files: {len(data['concepts']) + len(data['sources'])}
- Sources: {len(data['sources'])}
- Concepts: {len(data['concepts'])}
- Last updated: {today}

## Files with this tag

"""
    
    # Merge concepts + sources, sort alphabetically
    all_items = []
    for f in data['concepts']:
        title = derive_title(f['slug'])  # Convert slug to Title Case
        all_items.append((f['slug'], title, 'concept'))
    for f in data['sources']:
        title = derive_title(f['slug'].replace('src_', ''))
        all_items.append((f['slug'], title, 'source'))
    
    all_items.sort(key=lambda x: x[0])  # Alphabetical by slug
    
    for slug, title, ftype in all_items:
        content += f"- [[{slug}]] — {title} ({ftype})\n"
    
    # Co-occurring tags (new format)
    if co_occur:
        content += "\n## Co-occurring tags\n\n"
        for other_tag, count in co_occur:
            unit = "co-occurrence" if count == 1 else "co-occurrences"
            content += f"- [[{other_tag}]] — {count} {unit}\n"
    
    return content


def derive_title(slug):
    """Convert slug to human-readable title."""
    # Replace hyphens with spaces, title case
    return ' '.join(word.capitalize() for word in slug.split('-'))
```

### 7.2 Write file

```bash
# File path
wiki/tag/<tag>.md

# Write operation
cat > "wiki/tag/${tag}.md" << 'EOF'
<generated content>
EOF
```

### 7.3 Verify

```bash
# Check file exists
test -f "wiki/tag/${tag}.md" && echo "✓ Tag index created: ${tag}"

# Check file not empty
[ -s "wiki/tag/${tag}.md" ] && echo "✓ Tag index has content"
```

---

## Step 8: Write Topic Index Files

For each topic in `topic_index`:

### 8.1 Generate file content

```python
def generate_topic_index(topic, data, related):
    content = f"""# Topic: {topic}

Auto-generated index of all content with topic `{topic}`.

Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

---

## Concepts ({len(data['concepts'])})

"""
    
    # Add concept links
    for file in data['concepts']:
        main = file['main_tag']
        subs = ', '.join([f"#{s}" for s in file['sub_tags']])
        content += f"- [[{file['slug']}]] — main: #{main}, sub: [{subs}]\n"
    
    content += f"\n## Sources ({len(data['sources'])})\n\n"
    
    # Add source links
    for file in data['sources']:
        main = file['main_tag']
        subs = ', '.join([f"#{s}" for s in file['sub_tags']])
        content += f"- [[{file['slug']}]] — main: #{main}, sub: [{subs}]\n"
    
    # Add related topics section
    if related:
        content += "\n## Related topics\n\n"
        content += f"Topics that share concepts/sources with `{topic}`:\n"
        for other_topic, count in related:
            content += f"- `{other_topic}` ({count} shared files)\n"
    
    return content
```

### 8.2 Write file

```bash
# File path
wiki/topic/<topic>.md

# Write operation
cat > "wiki/topic/${topic}.md" << 'EOF'
<generated content>
EOF
```

---
## Step 8.5: Update tag.md Master Index

After writing all tag index files, update `wiki/tag/tag.md`:

### 8.5.1 Append new tags to Items section

```bash
if ! grep -q "^\- \[\[${tag}\]\]" wiki/tag/tag.md; then
    if grep -q "^${tag}$" <(echo "$main_tags"); then
        pool="Main Tags (Pool A)"
    else
        pool="Sub Tags (Pool B)"
    fi

    description=$(grep "^| \`#${tag}\`" TAGS.md | cut -d'|' -f3 | xargs)

    sed -i "/^### ${pool}$/a\\
- [[${tag}]] — ${description}" wiki/tag/tag.md
fi
```

**Entry format:**
```markdown
- [[tag]] — Description from TAGS.md
```

### 8.5.2 Update Stats section in tag.md

```bash
total_tags=$(ls wiki/tag/*.md 2>/dev/null | grep -v "tag.md" | wc -l)
main_tags_count=7
sub_tags_count=$((total_tags - main_tags_count))

declare -A tag_counts
for tag_file in wiki/tag/*.md; do
    tag=$(basename "$tag_file" .md)
    if [ "$tag" != "tag" ]; then
        count=$(grep -c "^\- \[\[" "$tag_file" 2>/dev/null || echo 0)
        tag_counts[$tag]=$count
    fi
done

top_3=$(for tag in "${!tag_counts[@]}"; do
    echo "${tag_counts[$tag]} $tag"
done | sort -rn | head -3)

most_used=""
while read -r count tag; do
    most_used="${most_used}#${tag} (${count}), "
done <<< "$top_3"
most_used=${most_used%, }

cat > temp_stats << EOF
## Stats

- Total tags: ${total_tags}
- Main tags: ${main_tags_count}
- Sub tags: ${sub_tags_count}
- Most used: ${most_used}
- Last updated: $(date +%Y-%m-%d)
EOF

sed -i '/^## Stats$/,/^## Items$/{//!d}' wiki/tag/tag.md
sed -i '/^## Stats$/r temp_stats' wiki/tag/tag.md
rm temp_stats
```

### 8.5.3 Verify update

```bash
grep -q "Last updated: $(date +%Y-%m-%d)" wiki/tag/tag.md && echo "✓ tag.md Stats updated"

for tag in "${!tag_index[@]}"; do
    grep -q "^\- \[\[${tag}\]\]" wiki/tag/tag.md || echo "⚠ Missing: ${tag}"
done
```

**Error handling:**
- If tag.md doesn't exist → create from template (see `index-spec.md` Section 9.3)
- If Stats section malformed → regenerate entire Stats section
- If tag description not found in TAGS.md → use placeholder "[description]"

## Step 9: Clean Up Orphaned Index Files

### 9.1 Find orphaned tag indexes

```bash
# List all existing tag index files
existing_tag_files=$(ls wiki/tag/*.md 2>/dev/null | xargs -n1 basename | sed 's/.md$//')

# Compare with current tags
for tag_file in $existing_tag_files; do
    if ! grep -q "^${tag_file}$" <(echo "$current_tags"); then
        echo "Orphan: wiki/tag/${tag_file}.md"
    fi
done
```

**Orphan criteria:**
- Index file exists in `wiki/tag/`
- But no wiki files currently use that tag

### 9.2 Find orphaned topic indexes

```bash
# List all existing topic index files
existing_topic_files=$(ls wiki/topic/*.md 2>/dev/null | xargs -n1 basename | sed 's/.md$//')

# Compare with current topics
for topic_file in $existing_topic_files; do
    if ! grep -q "^${topic_file}$" <(echo "$current_topics"); then
        echo "Orphan: wiki/topic/${topic_file}.md"
    fi
done
```

### 9.3 Delete orphans

```bash
# Delete orphaned tag indexes
for orphan in $orphaned_tag_files; do
    rm "wiki/tag/${orphan}.md"
    echo "Deleted orphan: wiki/tag/${orphan}.md"
done

# Delete orphaned topic indexes
for orphan in $orphaned_topic_files; do
    rm "wiki/topic/${orphan}.md"
    echo "Deleted orphan: wiki/topic/${orphan}.md"
done
```

**Log deletions:**
```markdown
## YYYY-MM-DD HH:MM:SS — Orphan cleanup
- Deleted tag indexes: [<tag1>, <tag2>, ...]
- Deleted topic indexes: [<topic1>, <topic2>, ...]
```

---

## Step 10: Log to Memory

### 10.1 Append to MEMORY.md

```markdown
## YYYY-MM-DD HH:MM:SS — Indexed

- **Scanned:** X concepts + Y sources = Z total files
- **Tags indexed:** A (B main-tags + C sub-tags)
- **Topics indexed:** T
- **Orphans deleted:** N tag indexes + M topic indexes
- **Invalid tags found:** P (see details above)
- **Errors:** Q files skipped due to invalid frontmatter
```

**Example:**
```markdown
## 2026-05-07 21:00:15 — Indexed

- **Scanned:** 85 concepts + 120 sources = 205 total files
- **Tags indexed:** 15 (7 main-tags + 8 sub-tags)
- **Topics indexed:** 42
- **Orphans deleted:** 2 tag indexes + 3 topic indexes
- **Invalid tags found:** 1 (wiki/concepts/old-concept.md has #deprecated)
- **Errors:** 0 files skipped
```

---

## Error Handling

### Missing frontmatter

```
[WARNING] wiki/sources/src_old-file.md
Issue: No frontmatter found
Action: Skipped, not included in any index
```

### Invalid YAML

```
[ERROR] wiki/concepts/broken-concept.md
Issue: Cannot parse YAML frontmatter (line 5: unexpected character)
Action: Skipped, not included in any index
```

### Invalid tag

```
[INVALID TAG] wiki/concepts/test-concept.md
Tag: #experimental (not in TAGS.md)
Action: File indexed under valid tags only, #experimental index not created
```

### Disk full

```
[FATAL ERROR] Disk full
Action: Stop indexing, alert Julius
```

→ Do not continue, risk incomplete indexes.

### Permission denied

```
[ERROR] Cannot write to wiki/tag/
Issue: Permission denied
Action: Stop indexing, alert Julius
```

---

## Validation Checklist

Before marking index run complete:

- [ ] All tag index files exist in `wiki/tag/`
- [ ] All topic index files exist in `wiki/topic/`
- [ ] No orphaned index files remain
- [ ] All index files have valid structure
- [ ] MEMORY.md entry added
- [ ] No files written outside `wiki/tag/` and `wiki/topic/`

---

## Performance Optimization

### Caching

```python
# Cache TAGS.md in memory (read once)
allowed_tags = load_tags_once()

# Cache frontmatter during scan (don't re-read)
file_cache = {}
for file in wiki_files:
    file_cache[file] = parse_frontmatter(file)
```

### Batch writes

```python
# Write all tag indexes in one pass
for tag, data in tag_index.items():
    write_tag_index(tag, data)

# Write all topic indexes in one pass
for topic, data in topic_index.items():
    write_topic_index(topic, data)
```

### Parallel processing (future)

```python
# Scan files in parallel (read-only, safe)
with ThreadPoolExecutor(max_workers=4) as executor:
    futures = [executor.submit(parse_file, f) for f in wiki_files]
    results = [f.result() for f in futures]
```

---

## Performance Benchmarks

Typical index times by wiki size:

| Files | Tags | Topics | Scan | Co-occur | Write | Total |
|---|---|---|---|---|---|---|
| 100 | 10 | 20 | 2s | 1s | 2s | 5s |
| 250 | 12 | 35 | 5s | 2s | 3s | 10s |
| 500 | 15 | 50 | 10s | 5s | 5s | 20s |
| 1000 | 18 | 80 | 20s | 15s | 10s | 45s |

**Bottlenecks:**
- Co-occurrence calculation (O(n²) tag pairs)
- Topic overlap calculation (O(n²) topic pairs)
- Writing many small files (I/O bound)

---

## Related Documentation

- [SKILL.md](SKILL.md) — Index Agent overview
- [examples.md](examples.md) — sample index files
- [reference.md](reference.md) — index file format specification
