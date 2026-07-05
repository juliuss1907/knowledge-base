import os
import yaml
import re
from datetime import datetime
from collections import defaultdict

# Configuration
SOURCES_DIR = 'wiki/sources/'
CONCEPTS_DIR = 'wiki/concepts/'
TAG_DIR = 'wiki/tag/'
TOPIC_DIR = 'wiki/topic/'
TAGS_FILE = 'TAGS.md'

# Tag Whitelists
POOL_A = {'ai', 'crypto', 'tech', 'productivity', 'system', 'economic', 'politic', 'health', 'investment'}
POOL_B = {'hack', 'tools', 'automation', 'vibecode', 'research', 'tutorial', 'opinion', 'news', 'defi', 'perpdex', 'layer1', 'layer2', 'law', 'coding', 'psychology', 'health', 'ai', 'system', 'geopolitics'}

def extract_frontmatter(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            match = re.search(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
            if match:
                return yaml.safe_load(match.group(1))
    except Exception as e:
        print(f"[ERROR] {filepath}: {e}")
    return None

def derive_title(slug):
    # Remove src_ prefix for sources
    slug = slug.replace('src_', '')
    # Replace hyphens with spaces, title case
    return ' '.join(word.capitalize() for word in slug.split('-'))

def run_indexing():
    all_files_data = []
    
    # 1. Scan and Extract
    dirs = [SOURCES_DIR, CONCEPTS_DIR]
    for d in dirs:
        if not os.path.exists(d): continue
        for filename in sorted(os.listdir(d)):
            if filename.endswith('.md'):
                path = os.path.join(d, filename)
                fm = extract_frontmatter(path)
                if not fm:
                    print(f"[WARNING] {path}: No valid frontmatter")
                    continue
                
                # Basic validation of required fields
                if not all(k in fm for k in ('type', 'main_tag', 'sub_tags', 'topic')):
                    print(f"[ERROR] {path}: Missing required frontmatter fields")
                    continue
                
                slug = filename[:-3]
                all_files_data.append({
                    'path': path,
                    'slug': slug,
                    'type': fm['type'],
                    'main_tag': fm['main_tag'],
                    'sub_tags': fm['sub_tags'] if isinstance(fm['sub_tags'], list) else [fm['sub_tags']],
                    'topic': fm['topic']
                })

    # 2. Validate and Group by Tag
    tag_index = defaultdict(lambda: {'concepts': [], 'sources': []})
    invalid_tags_found = []
    
    for file in all_files_data:
        # Validate main_tag
        main = file['main_tag']
        if main not in POOL_A:
            invalid_tags_found.append(f"{file['path']}: main_tag={main}")
            # Still index under main_tag if it's used, but mark as invalid (per workflow, we don't create the index file for it if it's a new tag, but the workflow is a bit ambiguous. I'll stick to: index it in the file, but if a tag is completely missing from POOL_A/B, I won't create a dedicated index file for it unless it's already in POOL_A/B).
        
        # We index it anyway in the mapping
        if file['type'] == 'concept':
            tag_index[main]['concepts'].append(file)
        else:
            tag_index[main]['sources'].append(file)
            
        # Validate sub_tags
        for sub in file['sub_tags']:
            if sub not in POOL_B:
                invalid_tags_found.append(f"{file['path']}: sub_tag={sub}")
            
            if file['type'] == 'concept':
                tag_index[sub]['concepts'].append(file)
            else:
                tag_index[sub]['sources'].append(file)

    # 3. Group by Topic
    topic_index = defaultdict(lambda: {'concepts': [], 'sources': []})
    for file in all_files_data:
        topic = file['topic']
        if file['type'] == 'concept':
            topic_index[topic]['concepts'].append(file)
        else:
            topic_index[topic]['sources'].append(file)

    # 4. Co-occurrence
    co_occurrence = defaultdict(int)
    for file in all_files_data:
        tags = [file['main_tag']] + file['sub_tags']
        # De-duplicate just in case
        tags = list(set(tags))
        for i in range(len(tags)):
            for j in range(i + 1, len(tags)):
                pair = tuple(sorted([tags[i], tags[j]]))
                co_occurrence[pair] += 1

    tag_co_occur = {}
    for tag in tag_index.keys():
        pairs = []
        for (t1, t2), count in co_occurrence.items():
            if t1 == tag: pairs.append((t2, count))
            elif t2 == tag: pairs.append((t1, count))
        tag_co_occur[tag] = sorted(pairs, key=lambda x: -x[1])[:5]

    # 5. Topic Overlap
    topic_overlap = defaultdict(int)
    topics = list(topic_index.keys())
    for i in range(len(topics)):
        for j in range(i + 1, len(topics)):
            t1, t2 = topics[i], topics[j]
            files1 = set([f['path'] for f in topic_index[t1]['concepts'] + topic_index[t1]['sources']])
            files2 = set([f['path'] for f in topic_index[t2]['concepts'] + topic_index[t2]['sources']])
            shared = len(files1 & files2)
            if shared > 0:
                topic_overlap[tuple(sorted([t1, t2]))] = shared

    topic_related = {}
    for topic in topic_index.keys():
        pairs = []
        for (t1, t2), count in topic_overlap.items():
            if t1 == topic: pairs.append((t2, count))
            elif t2 == topic: pairs.append((t1, count))
        topic_related[topic] = sorted(pairs, key=lambda x: -x[1])[:5]

    # 6. Sort everything
    for tag in tag_index:
        tag_index[tag]['concepts'].sort(key=lambda x: x['slug'])
        tag_index[tag]['sources'].sort(key=lambda x: x['slug'])
    for topic in topic_index:
        topic_index[topic]['concepts'].sort(key=lambda x: x['slug'])
        topic_index[topic]['sources'].sort(key=lambda x: x['slug'])

    # 7. Write Tag Indexes
    os.makedirs(TAG_DIR, exist_ok=True)
    today = datetime.now().strftime('%Y-%m-%d')
    
    written_tags = set()
    for tag, data in tag_index.items():
        # Only create index file if tag is in POOL_A or POOL_B
        if tag not in POOL_A and tag not in POOL_B:
            continue
            
        written_tags.add(tag)
        content = f"""---
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

- Total files: {len(data['concepts']) + len(data['sources'])}
- Sources: {len(data['sources'])}
- Concepts: {len(data['concepts'])}
- Last updated: {today}

## Files with this tag

"""
        all_items = []
        for f in data['concepts']:
            all_items.append((f['slug'], derive_title(f['slug']), 'concept'))
        for f in data['sources']:
            all_items.append((f['slug'], derive_title(f['slug']), 'source'))
        
        all_items.sort(key=lambda x: x[0])
        for slug, title, ftype in all_items:
            content += f"- [[{slug}]] — {title} ({ftype})\n"
        
        co_occur = tag_co_occur.get(tag, [])
        if co_occur:
            content += "\n## Co-occurring tags\n\n"
            for other_tag, count in co_occur:
                unit = "co-occurrence" if count == 1 else "co-occurrences"
                content += f"- [[{other_tag}]] — {count} {unit}\n"
        
        with open(os.path.join(TAG_DIR, f"{tag}.md"), 'w', encoding='utf-8') as f:
            f.write(content)

    # 8. Write Topic Indexes
    os.makedirs(TOPIC_DIR, exist_ok=True)
    for topic, data in topic_index.items():
        content = f"""---
type: index
scope: topic
parent: "[[topic]]"
topic: {topic}
auto_generated: true
last_updated: {today}
---

# Topic: {topic}

Auto-generated index of all content with topic `{topic}`.

Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

---

## Concepts ({len(data['concepts'])})

"""
        for file in data['concepts']:
            main = file['main_tag']
            subs = ', '.join([f"#{s}" for s in file['sub_tags']])
            content += f"- [[{file['slug']}]] — main: #{main}, sub: [{subs}]\n"
        
        content += f"\n## Sources ({len(data['sources'])})\n\n"
        for file in data['sources']:
            main = file['main_tag']
            subs = ', '.join([f"#{s}" for s in file['sub_tags']])
            content += f"- [[{file['slug']}]] — main: #{main}, sub: [{subs}]\n"
        
        related = topic_related.get(topic, [])
        if related:
            content += "\n## Related topics\n\n"
            content += f"Topics that share concepts/sources with `{topic}`:\n"
            for other_topic, count in related:
                content += f"- `{other_topic}` ({count} shared files)\n"
        
        with open(os.path.join(TOPIC_DIR, f"{topic}.md"), 'w', encoding='utf-8') as f:
            f.write(content)

    # 9. Cleanup Orphans
    deleted_tags = []
    if os.path.exists(TAG_DIR):
        for filename in os.listdir(TAG_DIR):
            if filename == 'tag.md': continue
            tag = filename[:-3]
            if tag not in written_tags:
                os.remove(os.path.join(TAG_DIR, filename))
                deleted_tags.append(tag)
    
    deleted_topics = []
    if os.path.exists(TOPIC_DIR):
        for filename in os.listdir(TOPIC_DIR):
            topic = filename[:-3]
            if topic not in topic_index:
                os.remove(os.path.join(TOPIC_DIR, filename))
                deleted_topics.append(topic)

    # 10. Report results
    print(f"SCAN_RESULTS|{len(all_files_data)}|{len(tag_index)}|{len(topic_index)}|{len(deleted_tags)}|{len(deleted_topics)}|{len(invalid_tags_found)}")
    for inv in invalid_tags_found:
        print(f"INVALID_TAG|{inv}")

if __name__ == "__main__":
    run_indexing()
