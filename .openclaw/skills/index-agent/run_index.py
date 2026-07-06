import os
import re
import yaml
from datetime import datetime
from collections import defaultdict

# --- CONFIG ---
WIKI_SOURCES = 'wiki/sources/'
WIKI_CONCEPTS = 'wiki/concepts/'
TAG_DIR = 'wiki/tag/'
TOPIC_DIR = 'wiki/topic/'
TAGS_FILE = 'TAGS.md'
MASTER_TAG_FILE = 'wiki/tag/tag.md'
MEMORY_FILE = '.openclaw/MEMORY.md'

# Pools derived from TAGS.md
POOL_A = {'ai', 'crypto', 'tech', 'productivity', 'system', 'economic', 'politic', 'health', 'investment'}
POOL_B = {'hack', 'tools', 'automation', 'vibecode', 'research', 'tutorial', 'opinion', 'news', 'defi', 'perpdex', 'layer1', 'layer2', 'law', 'coding', 'psychology', 'health', 'ai', 'system', 'geopolitics'}

def derive_title(slug):
    # Convert slug to human-readable title
    # Remove src_ prefix if present
    slug = slug.replace('src_', '')
    return ' '.join(word.capitalize() for word in slug.split('-'))

def parse_frontmatter(content):
    # Extract frontmatter between first two ---
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if not match:
        return None
    try:
        return yaml.safe_load(match.group(1))
    except Exception:
        return None

def main():
    today = datetime.now().strftime('%Y-%m-%d')
    now_str = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # 1. Scan Files
    wiki_files = []
    errors = 0
    warnings = 0
    invalid_tags_count = 0
    
    for folder in [WIKI_SOURCES, WIKI_CONCEPTS]:
        if not os.path.exists(folder):
            continue
        for filename in sorted(os.listdir(folder)):
            if filename.endswith('.md'):
                path = os.path.join(folder, filename)
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    fm = parse_frontmatter(content)
                    if not fm:
                        print(f"[WARNING] {path}: No valid frontmatter found")
                        warnings += 1
                        continue
                    
                    # Validation
                    valid = True
                    main_tag = fm.get('main_tag')
                    sub_tags = fm.get('sub_tags', [])
                    topic = fm.get('topic')
                    
                    if not main_tag or not topic:
                        print(f"[ERROR] {path}: Missing main_tag or topic")
                        errors += 1
                        continue
                    
                    if not isinstance(sub_tags, list):
                        sub_tags = []
                    
                    # Check Pool A
                    if main_tag not in POOL_A:
                        print(f"[INVALID TAG] {path}: main_tag={main_tag} not in Pool A")
                        invalid_tags_count += 1
                        # We still index it but might flag it
                    
                    # Check Pool B
                    invalid_subs = [t for t in sub_tags if t not in POOL_B]
                    if invalid_subs:
                        print(f"[INVALID TAG] {path}: sub_tags={invalid_subs} not in Pool B")
                        invalid_tags_count += 1

                    wiki_files.append({
                        'path': path,
                        'slug': filename[:-3],
                        'type': 'concept' if 'concepts' in path else 'source',
                        'main_tag': main_tag,
                        'sub_tags': sub_tags,
                        'topic': topic,
                        'invalid_main': main_tag not in POOL_A,
                        'invalid_subs': invalid_subs
                    })

    # 2. Group by Tag
    tag_index = defaultdict(lambda: {'concepts': [], 'sources': []})
    for f in wiki_files:
        # Main tag
        if not f['invalid_main']:
            tag = f['main_tag']
            key = 'concepts' if f['type'] == 'concept' else 'sources'
            tag_index[tag][key].append(f)
        
        # Sub tags
        for tag in f['sub_tags']:
            if tag not in f['invalid_subs']:
                key = 'concepts' if f['type'] == 'concept' else 'sources'
                tag_index[tag][key].append(f)

    # Sort lists
    for tag in tag_index:
        tag_index[tag]['concepts'].sort(key=lambda x: x['slug'])
        tag_index[tag]['sources'].sort(key=lambda x: x['slug'])

    # 3. Co-occurrence
    co_occurrence = defaultdict(int)
    for f in wiki_files:
        all_tags = [f['main_tag']] + f['sub_tags']
        all_tags = sorted(list(set(all_tags)))
        for i in range(len(all_tags)):
            for j in range(i + 1, len(all_tags)):
                pair = tuple(sorted([all_tags[i], all_tags[j]]))
                co_occurrence[pair] += 1

    tag_co_occur = {}
    for tag in tag_index:
        pairs = []
        for (t1, t2), count in co_occurrence.items():
            if tag == t1: pairs.append((t2, count))
            elif tag == t2: pairs.append((t1, count))
        
        pairs.sort(key=lambda x: -x[1])
        tag_co_occur[tag] = pairs[:5]

    # 4. Group by Topic
    topic_index = defaultdict(lambda: {'concepts': [], 'sources': []})
    for f in wiki_files:
        topic = f['topic']
        key = 'concepts' if f['type'] == 'concept' else 'sources'
        topic_index[topic][key].append(f)
    
    for topic in topic_index:
        topic_index[topic]['concepts'].sort(key=lambda x: x['slug'])
        topic_index[topic]['sources'].sort(key=lambda x: x['slug'])

    # 5. Topic Overlap
    topic_overlap = defaultdict(int)
    topics = list(topic_index.keys())
    for i in range(len(topics)):
        t1 = topics[i]
        files1 = {f['path'] for f in topic_index[t1]['concepts'] + topic_index[t1]['sources']}
        for j in range(i + 1, len(topics)):
            t2 = topics[j]
            files2 = {f['path'] for f in topic_index[t2]['concepts'] + topic_index[t2]['sources']}
            shared = len(files1 & files2)
            if shared > 0:
                topic_overlap[tuple(sorted([t1, t2]))] = shared

    topic_related = {}
    for topic in topic_index:
        pairs = []
        for (t1, t2), count in topic_overlap.items():
            if topic == t1: pairs.append((t2, count))
            elif topic == t2: pairs.append((t1, count))
        
        pairs.sort(key=lambda x: -x[1])
        topic_related[topic] = pairs[:5]

    # 6. Write Tag Indexes
    os.makedirs(TAG_DIR, exist_ok=True)
    for tag, data in tag_index.items():
        all_items = []
        for f in data['concepts']:
            all_items.append((f['slug'], derive_title(f['slug']), 'concept'))
        for f in data['sources']:
            all_items.append((f['slug'], derive_title(f['slug']), 'source'))
        all_items.sort(key=lambda x: x[0])
        
        co_occur_list = tag_co_occur.get(tag, [])
        co_occur_text = ""
        if co_occur_list:
            co_occur_text = "\n## Co-occurring tags\n\n"
            for other, count in co_occur_list:
                unit = "co-occurrence" if count == 1 else "co-occurrences"
                co_occur_text += f"- [[{other}]] — {count} {unit}\n"
        
        content = f'''---
type: index
level: 3
scope: tag
parent: "[[tag]]"
tag: {tag}
auto_generated: true
last_updated: {today}
---

# Tag: #{tag}

## Parent

- [[tag]]

## Stats

- Total files: {len(all_items)}
- Sources: {len(data['sources'])}
- Concepts: {len(data['concepts'])}
- Last updated: {today}

## Files with this tag

'''
        for slug, title, ftype in all_items:
            content += f"- [[{slug}]] — {title} ({ftype})\n"
        
        content += co_occur_text
        
        with open(os.path.join(TAG_DIR, f"{tag}.md"), 'w', encoding='utf-8') as f:
            f.write(content)

    # 7. Write Topic Indexes
    os.makedirs(TOPIC_DIR, exist_ok=True)
    for topic, data in topic_index.items():
        content = f'''---
type: index
scope: topic
parent: "[[topic]]"
topic: {topic}
auto_generated: true
last_updated: {today}
---

# Topic: {topic}

Auto-generated index of all content with topic `{topic}`.

Last updated: {now_str}

---

## Concepts ({len(data['concepts'])})

'''
        for f in data['concepts']:
            subs = ', '.join([f"#{s}" for s in f['sub_tags']])
            content += f"- [[{f['slug']}]] — main: #{f['main_tag']}, sub: [{subs}]\n"
        
        content += f"\n## Sources ({len(data['sources'])})\n\n"
        for f in data['sources']:
            subs = ', '.join([f"#{s}" for s in f['sub_tags']])
            content += f"- [[{f['slug']}]] — main: #{f['main_tag']}, sub: [{subs}]\n"
        
        related = topic_related.get(topic, [])
        if related:
            content += "\n## Related topics\n\n"
            content += f"Topics that share concepts/sources with `{topic}`:\n"
            for other, count in related:
                content += f"- `{other}` ({count} shared files)\n"
        
        with open(os.path.join(TOPIC_DIR, f"{topic}.md"), 'w', encoding='utf-8') as f:
            f.write(content)

    # 8. Update Master Tag Index (wiki/tag/tag.md)
    if os.path.exists(MASTER_TAG_FILE):
        with open(MASTER_TAG_FILE, 'r', encoding='utf-8') as f:
            master_content = f.read()
        
        # Update items
        tags_found = set(tag_index.keys())
        
        # Simple way: find Pool A and Pool B sections and rebuild them
        # Or use the workflow's logic of appending. Let's use a more robust rebuild for Stats.
        
        # Get descriptions from TAGS.md
        descriptions = {}
        with open(TAGS_FILE, 'r', encoding='utf-8') as f:
            for line in f:
                if '| `# ' in line or '| `' in line:
                    # Very crude table parsing
                    parts = line.split('|')
                    if len(parts) >= 3:
                        tag_raw = parts[1].strip().replace('#', '').replace('`', '')
                        desc = parts[2].strip()
                        descriptions[tag_raw] = desc

        # Rebuild Stats
        total_tags = len(tags_found)
        main_count = len(tags_found & POOL_A)
        sub_count = total_tags - main_count
        
        tag_counts = {}
        for tag in tags_found:
            count = len(tag_index[tag]['concepts']) + len(tag_index[tag]['sources'])
            tag_counts[tag] = count
        
        top_3 = sorted(tag_counts.items(), key=lambda x: -x[1])[:3]
        most_used = ', '.join([f"#{t} ({c})" for t, c in top_3])
        
        stats_block = f'''## Stats

- Total tags: {total_tags}
- Main tags: {main_count}
- Sub tags: {sub_count}
- Most used: {most_used}
- Last updated: {today}
'''
        # Replace stats section
        if '## Stats' in master_content and '## Items' in master_content:
            start = master_content.find('## Stats')
            end = master_content.find('## Items')
            master_content = master_content[:start] + stats_block + master_content[end:]
        
        # Update items
        # We'll just ensure all currently active tags are listed.
        # Since the workflow says "append new tags", we check existence.
        for tag in tags_found:
            if f"- [[{tag}]]" not in master_content:
                pool = "Main Tags (Pool A)" if tag in POOL_A else "Sub Tags (Pool B)"
                desc = descriptions.get(tag, "[description]")
                entry = f"- [[{tag}]] — {desc}"
                
                # Insert after the pool header
                pattern = f"### {pool}"
                if pattern in master_content:
                    idx = master_content.find(pattern) + len(pattern)
                    master_content = master_content[:idx] + "\n" + entry + master_content[idx:]

        with open(MASTER_TAG_FILE, 'w', encoding='utf-8') as f:
            f.write(master_content)

    # 9. Orphan Cleanup
    orphaned_tags = []
    for filename in os.listdir(TAG_DIR):
        if filename == 'tag.md' or not filename.endswith('.md'): continue
        tag = filename[:-3]
        if tag not in tag_index:
            orphaned_tags.append(tag)
            os.remove(os.path.join(TAG_DIR, filename))
            
    orphaned_topics = []
    for filename in os.listdir(TOPIC_DIR):
        if not filename.endswith('.md'): continue
        topic = filename[:-3]
        if topic not in topic_index:
            orphaned_topics.append(topic)
            os.remove(os.path.join(TOPIC_DIR, filename))

    # Final Summary for output
    print(f"SUMMARY|{len(wiki_files)}|{len(tag_index)}|{len(topic_index)}|{len(orphaned_tags)}|{len(orphaned_topics)}|{invalid_tags_count}|{errors}")

if __name__ == '__main__':
    main()
