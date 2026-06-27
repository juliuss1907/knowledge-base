import os
import yaml
import re
from datetime import datetime
from collections import defaultdict

# --- Configuration ---
RAW_DIRS = ['wiki/sources', 'wiki/concepts']
TAG_DIR = 'wiki/tag'
TOPIC_DIR = 'wiki/topic'
TAGS_FILE = 'TAGS.md'
MASTER_TAG_FILE = 'wiki/tag/tag.md'
MEMORY_FILE = '.openclaw/MEMORY.md'

def load_taxonomy():
    with open(TAGS_FILE, 'r', encoding='utf-8') as f:
        content = f.read()
    
    pool_a = set()
    pool_b = set()
    
    # Extract Pool A
    section_a = re.search(r'## 2\. Pool A — Main-tags.*?\| Tag \| Description\n\|---|---\|\n(.*?)\n\n', content, re.S)
    if section_a:
        for line in section_a.group(1).split('\n'):
            if line.startswith('|'):
                tag = line.split('|')[1].strip().replace('#', '')
                pool_a.add(tag)
                
    # Extract Pool B
    section_b = re.search(r'## 3\. Pool B — Sub-tags.*?\| Tag \| Description\n\|---|---\|\n(.*?)\n\n', content, re.S)
    if section_b:
        for line in section_b.group(1).split('\n'):
            if line.startswith('|'):
                tag = line.split('|')[1].strip().replace('#', '')
                pool_b.add(tag)
                
    return pool_a, pool_b

def extract_slug(path):
    filename = os.path.basename(path)
    slug = filename.replace('.md', '')
    if slug.startswith('src_'):
        slug = slug[4:]
    return slug

def derive_title(slug):
    return ' '.join(word.capitalize() for word in slug.split('-'))

def parse_frontmatter(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.S)
    if not match:
        return None, "No frontmatter found"
    
    try:
        data = yaml.safe_load(match.group(1))
        if not data:
            return None, "Empty frontmatter"
        
        # Required fields
        required = ['type', 'main_tag', 'sub_tags', 'topic']
        for field in required:
            if field not in data:
                return None, f"Missing field: {field}"
        
        return data, None
    except Exception as e:
        return None, f"YAML parse error: {str(e)}"

def main():
    pool_a, pool_b = load_taxonomy()
    wiki_files = []
    invalid_tags_log = []
    errors_log = []
    
    # 1. Scan Wiki Files
    all_paths = []
    for d in RAW_DIRS:
        if os.path.exists(d):
            for root, _, files in os.walk(d):
                for f in files:
                    if f.endswith('.md'):
                        all_paths.append(os.path.join(root, f))
    
    all_paths.sort()
    
    for path in all_paths:
        data, err = parse_frontmatter(path)
        if err:
            errors_log.append(f"[FRONTMATTER ERROR] {path}: {err}")
            continue
            
        slug = extract_slug(path)
        main_tag = data['main_tag']
        sub_tags = data['sub_tags']
        if isinstance(sub_tags, str):
            sub_tags = [sub_tags]
            
        # Validate main_tag
        if main_tag not in pool_a:
            invalid_tags_log.append(f"[INVALID TAG] {path}: main_tag={main_tag}")
            valid_main = None
        else:
            valid_main = main_tag
            
        # Validate sub_tags
        valid_subs = []
        for st in sub_tags:
            if st not in pool_b:
                invalid_tags_log.append(f"[INVALID TAG] {path}: sub_tag={st}")
            else:
                valid_subs.append(st)
        
        wiki_files.append({
            'path': path,
            'type': data['type'],
            'main_tag': main_tag,
            'valid_main': valid_main,
            'sub_tags': sub_tags,
            'valid_subs': valid_subs,
            'topic': data['topic'],
            'slug': slug
        })

    # 2. Group by Tag
    tag_index = defaultdict(lambda: {'concepts': [], 'sources': []})
    for f in wiki_files:
        # Main tag
        if f['valid_main']:
            tag = f['valid_main']
            if f['type'] == 'concept':
                tag_index[tag]['concepts'].append(f)
            else:
                tag_index[tag]['sources'].append(f)
        
        # Sub tags
        for st in f['valid_subs']:
            if f['type'] == 'concept':
                tag_index[st]['concepts'].append(f)
            else:
                tag_index[st]['sources'].append(f)
    
    # Sort files
    for tag in tag_index:
        tag_index[tag]['concepts'].sort(key=lambda x: x['slug'])
        tag_index[tag]['sources'].sort(key=lambda x: x['slug'])

    # 3. Co-occurrence
    co_occurrence = defaultdict(int)
    for f in wiki_files:
        all_tags = []
        if f['valid_main']: all_tags.append(f['valid_main'])
        all_tags.extend(f['valid_subs'])
        
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
        if f['type'] == 'concept':
            topic_index[topic]['concepts'].append(f)
        else:
            topic_index[topic]['sources'].append(f)
            
    for topic in topic_index:
        topic_index[topic]['concepts'].sort(key=lambda x: x['slug'])
        topic_index[topic]['sources'].sort(key=lambda x: x['slug'])

    # 5. Topic Overlap
    topic_overlap = defaultdict(int)
    topic_list = list(topic_index.keys())
    for i in range(len(topic_list)):
        t1 = topic_list[i]
        files1 = set([f['path'] for f in topic_index[t1]['concepts'] + topic_index[t1]['sources']])
        for j in range(i + 1, len(topic_list)):
            t2 = topic_list[j]
            files2 = set([f['path'] for f in topic_index[t2]['concepts'] + topic_index[t2]['sources']])
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
    today = datetime.now().strftime('%Y-%m-%d')
    os.makedirs(TAG_DIR, exist_ok=True)
    for tag, data in tag_index.items():
        all_items = []
        for f in data['concepts']:
            all_items.append((f['slug'], derive_title(f['slug']), 'concept'))
        for f in data['sources']:
            all_items.append((f['slug'], derive_title(f['slug']), 'source'))
        all_items.sort(key=lambda x: x[0])
        
        header = f"""---
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

- Total files: {len(all_items)}
- Sources: {len(data['sources'])}
- Concepts: {len(data['concepts'])}
- Last updated: {today}

## Files with this tag

"""
        
        body = ""
        for slug, title, ftype in all_items:
            body += f"- [[{slug}]] — {title} ({ftype})\n"
            
        footer = ""
        if tag in tag_co_occur:
            footer += "\n## Co-occurring tags\n\n"
            for other_tag, count in tag_co_occur[tag]:
                unit = "co-occurrence" if count == 1 else "co-occurrences"
                footer += f"- [[{other_tag}]] — {count} {unit}\n"
                
        content = header + body + footer
        
        with open(os.path.join(TAG_DIR, f"{tag}.md"), 'w', encoding='utf-8') as f:
            f.write(content)

    # 7. Write Topic Indexes
    os.makedirs(TOPIC_DIR, exist_ok=True)
    for topic, data in topic_index.items():
        content = f\"# Topic: {topic}\\n\\nAuto-generated index of all content with topic `{topic}`.\\n\\nLast updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\\n\\n---\\n\\n## Concepts ({len(data['concepts'])})\\n\\n\"
        for f in data['concepts']:
            main = f['main_tag']
            subs = ', '.join([f\"#{s}\" for s in f['sub_tags']])
            content += f\"- [[{f['slug']}]] — main: #{main}, sub: [{subs}]\\n\"
        
        content += f\"\\n## Sources ({len(data['sources'])})\\n\\n\"
        for f in data['sources']:
            main = f['main_tag']
            subs = ', '.join([f\"#{s}\" for s in f['sub_tags']])
            content += f\"- [[{f['slug']}]] — main: #{main}, sub: [{subs}]\\n\"
            
        if topic in topic_related:
            content += \"\\n## Related topics\\n\\n\"
            content += f\"Topics that share concepts/sources with `{topic}`:\\n\"
            for other_topic, count in topic_related[topic]:
                content += f\"- `{other_topic}` ({count} shared files)\\n\"
                
        with open(os.path.join(TOPIC_DIR, f\"{topic}.md\"), 'w', encoding='utf-8') as f:
            f.write(content)

    # 8. Update tag.md
    if os.path.exists(MASTER_TAG_FILE):
        with open(MASTER_TAG_FILE, 'r', encoding='utf-8') as f:
            master_content = f.read()
        
        # Update Items
        # This is a simplified update. We'll regenerate the Items section.
        # Let's just focus on updating Stats first as per workflow.
        
        tag_counts = {}
        for tag in tag_index:
            tag_counts[tag] = len(tag_index[tag]['concepts']) + len(tag_index[tag]['sources'])
        
        top_3 = sorted(tag_counts.items(), key=lambda x: -x[1])[:3]
        most_used = ', '.join([f"#{t} ({c})" for t, c in top_3])
        
        total_tags = len(tag_index)
        main_tags_count = len(pool_a)
        sub_tags_count = total_tags - main_tags_count
        
        stats_section = f\"## Stats\\n\\n- Total tags: {total_tags}\\n- Main tags: {main_tags_count}\\n- Sub tags: {sub_tags_count}\\n- Most used: {most_used}\\n- Last updated: {today}\\n\"
        
        if '## Stats' in master_content:
            # Replace stats section
            start = master_content.find('## Stats')
            end = master_content.find('## Items')
            if end != -1:
                master_content = master_content[:start] + stats_section + master_content[end:]
            else:
                master_content = master_content[:start] + stats_section
        
        with open(MASTER_TAG_FILE, 'w', encoding='utf-8') as f:
            f.write(master_content)

    # 9. Cleanup Orphans
    deleted_tags = []
    if os.path.exists(TAG_DIR):
        for f in os.listdir(TAG_DIR):
            if f.endswith('.md'):
                tag = f.replace('.md', '')
                if tag != 'tag' and tag not in tag_index:
                    os.remove(os.path.join(TAG_DIR, f))
                    deleted_tags.append(tag)
                    
    deleted_topics = []
    if os.path.exists(TOPIC_DIR):
        for f in os.listdir(TOPIC_DIR):
            if f.endswith('.md'):
                topic = f.replace('.md', '')
                if topic not in topic_index:
                    os.remove(os.path.join(TOPIC_DIR, f))
                    deleted_topics.append(topic)

    # 10. Log to Memory
    log_entry = f\"\\n## {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} — Indexed\\n\\n\"
    log_entry += f\"- **Scanned:** {len(wiki_files)} files ({len([f for f in wiki_files if f['type'] == 'concept'])} concepts + {len([f for f in wiki_files if f['type'] == 'source'])} sources)\\n\"
    log_entry += f\"- **Tags indexed:** {len(tag_index)} ({len(pool_a)} main-tags + {len(tag_index) - len(pool_a)} sub-tags)\\n\"
    log_entry += f\"- **Topics indexed:** {len(topic_index)}\\n\"
    log_entry += f\"- **Orphans deleted:** {len(deleted_tags)} tag indexes + {len(deleted_topics)} topic indexes\\n\"
    if invalid_tags_log:
        log_entry += f\"- **Invalid tags found:** {len(invalid_tags_log)} (see details below)\\n\"
        for line in invalid_tags_log:
            log_entry += f\"  - {line}\\n\"
    if errors_log:
        log_entry += f\"- **Errors:** {len(errors_log)} files skipped due to invalid frontmatter\\n\"
        for line in errors_log:
            log_entry += f\"  - {line}\\n\"

    with open(MEMORY_FILE, 'a', encoding='utf-8') as f:
        f.write(log_entry)
        
    print(f\"SUCCESS: Scanned {len(wiki_files)} files. Tags: {len(tag_index)}, Topics: {len(topic_index)}. Orphans deleted: {len(deleted_tags)} tags, {len(deleted_topics)} topics.\")
    if invalid_tags_log:
        print(f\"WARNING: Found {len(invalid_tags_log)} invalid tags.\")
    if errors_log:
        print(f\"ERROR: {len(errors_log)} files had frontmatter errors.\")

if __name__ == '__main__':
    main()
