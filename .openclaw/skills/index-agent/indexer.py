import os
import re
import yaml
from datetime import datetime
from collections import defaultdict

# --- CONFIGURATION ---
SOURCES_DIR = 'wiki/sources/'
CONCEPTS_DIR = 'wiki/concepts/'
TAGS_DIR = 'wiki/tag/'
TOPICS_DIR = 'wiki/topic/'
TAGS_FILE = 'TAGS.md'
TAG_MASTER_FILE = 'wiki/tag/tag.md'
MEMORY_FILE = '.openclaw/MEMORY.md'

POOL_A = ['ai', 'crypto', 'tech', 'productivity', 'system', 'economic', 'politic', 'health', 'investment']
POOL_B = ['hack', 'tools', 'automation', 'vibecode', 'research', 'tutorial', 'opinion', 'news', 'defi', 'perpdex', 'layer1', 'layer2', 'law', 'coding', 'psychology', 'health', 'ai', 'system', 'geopolitics']

def derive_title(slug):
    # Remove src_ prefix
    clean_slug = slug.replace('src_', '')
    # Replace hyphens with spaces and title case
    return ' '.join(word.capitalize() for word in clean_slug.split('-'))

def parse_frontmatter(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
            match = re.search(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
            if not match:
                return None
            return yaml.safe_load(match.group(1))
    except Exception as e:
        print(f"[ERROR] {path}: {e}")
        return None

def run_indexing():
    files_data = []
    invalid_tags_found = []
    errors_skipped = 0
    
    # 1. Scan Wiki Files
    all_files = []
    for d in [SOURCES_DIR, CONCEPTS_DIR]:
        if os.path.exists(d):
            for f in os.listdir(d):
                if f.endswith('.md'):
                    all_files.append(os.path.join(d, f))
    
    all_files.sort()
    
    for path in all_files:
        fm = parse_frontmatter(path)
        if not fm:
            errors_skipped += 1
            continue
        
        # Basic validation
        if 'main_tag' not in fm or 'sub_tags' not in fm or 'topic' not in fm:
            errors_skipped += 1
            continue
            
        # Tag Validation
        main_tag = fm.get('main_tag')
        sub_tags = fm.get('sub_tags', [])
        if not isinstance(sub_tags, list):
            sub_tags = [sub_tags] if sub_tags else []
            
        invalid_main = False
        if main_tag not in POOL_A:
            invalid_tags_found.append(f"{path}: main_tag={main_tag}")
            invalid_main = True
            
        invalid_subs = []
        for st in sub_tags:
            if st not in POOL_B:
                invalid_tags_found.append(f"{path}: sub_tag={st}")
                invalid_subs.append(st)
        
        slug = os.path.basename(path).replace('.md', '')
        
        files_data.append({
            'path': path,
            'slug': slug,
            'type': 'concept' if 'concepts' in path else 'source',
            'main_tag': main_tag,
            'sub_tags': sub_tags,
            'topic': fm.get('topic'),
            'invalid_main': invalid_main,
            'invalid_subs': invalid_subs
        })

    # 2. Group by Tag
    tag_index = defaultdict(lambda: {'concepts': [], 'sources': []})
    for f in files_data:
        # Main tag
        if not f['invalid_main']:
            tag = f['main_tag']
            if f['type'] == 'concept':
                tag_index[tag]['concepts'].append(f)
            else:
                tag_index[tag]['sources'].append(f)
        
        # Sub tags
        for st in f['sub_tags']:
            if st not in f['invalid_subs']:
                if f['type'] == 'concept':
                    tag_index[st]['concepts'].append(f)
                else:
                    tag_index[st]['sources'].append(f)
    
    # Sort within tags
    for tag in tag_index:
        tag_index[tag]['concepts'].sort(key=lambda x: x['slug'])
        tag_index[tag]['sources'].sort(key=lambda x: x['slug'])

    # 3. Co-occurrence
    co_occurrence = defaultdict(int)
    for f in files_data:
        all_f_tags = []
        if not f['invalid_main']: all_f_tags.append(f['main_tag'])
        for st in f['sub_tags']:
            if st not in f['invalid_subs']: all_f_tags.append(st)
        
        all_f_tags = sorted(list(set(all_f_tags)))
        for i in range(len(all_f_tags)):
            for j in range(i+1, len(all_f_tags)):
                pair = tuple(sorted([all_f_tags[i], all_f_tags[j]]))
                co_occurrence[pair] += 1
                
    tag_co_occur = {}
    for tag in tag_index:
        pairs = []
        for (t1, t2), count in co_occurrence.items():
            if tag == t1: pairs.append((t2, count))
            elif tag == t2: pairs.append((t1, count))
        tag_co_occur[tag] = sorted(pairs, key=lambda x: -x[1])[:5]

    # 4. Group by Topic
    topic_index = defaultdict(lambda: {'concepts': [], 'sources': []})
    for f in files_data:
        topic = f['topic']
        if not topic: continue
        if f['type'] == 'concept':
            topic_index[topic]['concepts'].append(f)
        else:
            topic_index[topic]['sources'].append(f)
            
    for topic in topic_index:
        topic_index[topic]['concepts'].sort(key=lambda x: x['slug'])
        topic_index[topic]['sources'].sort(key=lambda x: x['slug'])

    # 5. Topic Overlap
    topic_overlap = defaultdict(int)
    sorted_topics = sorted(topic_index.keys())
    for i in range(len(sorted_topics)):
        t1 = sorted_topics[i]
        files1 = {f['path'] for f in topic_index[t1]['concepts'] + topic_index[t1]['sources']}
        for j in range(i+1, len(sorted_topics)):
            t2 = sorted_topics[j]
            files2 = {f['path'] for f in topic_index[t2]['concepts'] + topic_index[t2]['sources']}
            overlap = len(files1 & files2)
            if overlap > 0:
                topic_overlap[tuple(sorted([t1, t2]))] = overlap
                
    topic_related = {}
    for topic in topic_index:
        pairs = []
        for (t1, t2), count in topic_overlap.items():
            if topic == t1: pairs.append((t2, count))
            elif topic == t2: pairs.append((t1, count))
        topic_related[topic] = sorted(pairs, key=lambda x: -x[1])[:5]

    # 6. Write Tag Files
    os.makedirs(TAGS_DIR, exist_ok=True)
    today = datetime.now().strftime('%Y-%m-%d')
    
    for tag, data in tag_index.items():
        items = []
        for f in data['concepts']:
            items.append((f['slug'], derive_title(f['slug']), 'concept'))
        for f in data['sources']:
            items.append((f['slug'], derive_title(f['slug']), 'source'))
        items.sort()
        
        content = f"---\ntype: index\nlevel: 3\nscope: tag\nparent: [[tag]]\ntag: {tag}\nauto_generated: true\nlast_updated: {today}\n---\n\n# Tag: #{tag}\n\n## Parent\n\n- [[tag]]\n\n## Stats\n\n- Total files: {len(items)}\n- Sources: {len(data['sources'])}\n- Concepts: {len(data['concepts'])}\n- Last updated: {today}\n\n## Files with this tag\n\n"
        for slug, title, ftype in items:
            content += f"- [[{slug}]] — {title} ({ftype})\n"
        
        if tag in tag_co_occur:
            content += "\n## Co-occurring tags\n\n"
            for other, count in tag_co_occur[tag]:
                unit = "co-occurrence" if count == 1 else "co-occurrences"
                content += f"- [[{other}]] — {count} {unit}\n"
        
        with open(os.path.join(TAGS_DIR, f"{tag}.md"), 'w', encoding='utf-8') as f:
            f.write(content)

    # 7. Write Topic Files
    os.makedirs(TOPICS_DIR, exist_ok=True)
    for topic, data in topic_index.items():
        content = f"# Topic: {topic}\n\nAuto-generated index of all content with topic `{topic}`.\n\nLast updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n---\n\n## Concepts ({len(data['concepts'])})\n\n"
        for f in data['concepts']:
            subs = ', '.join([f"#{s}" for s in f['sub_tags']])
            content += f"- [[{f['slug']}]] — main: #{f['main_tag']}, sub: [{subs}]\n"
        
        content += f"\n## Sources ({len(data['sources'])})\n\n"
        for f in data['sources']:
            subs = ', '.join([f"#{s}" for s in f['sub_tags']])
            content += f"- [[{f['slug']}]] — main: #{f['main_tag']}, sub: [{subs}]\n"
            
        if topic in topic_related:
            content += "\n## Related topics\n\n"
            content += f"Topics that share concepts/sources with `{topic}`:\n"
            for other, count in topic_related[topic]:
                content += f"- `{other}` ({count} shared files)\n"
                
        with open(os.path.join(TOPICS_DIR, f"{topic}.md"), 'w', encoding='utf-8') as f:
            f.write(content)

    # 8. Update tag.md
    # For the sake of a script, we'll read it and replace the Stats section
    if os.path.exists(TAG_MASTER_FILE):
        with open(TAG_MASTER_FILE, 'r', encoding='utf-8') as f:
            master_content = f.read()
        
        # Update Stats
        total_tags = len(tag_index)
        main_count = len([t for t in tag_index if t in POOL_A])
        sub_count = total_tags - main_count
        
        # Calculate most used
        usage = []
        for tag, data in tag_index.items():
            usage.append((tag, len(data['concepts']) + len(data['sources'])))
        usage.sort(key=lambda x: -x[1])
        top_3 = ", ".join([f"#{t} ({c})" for t, c in usage[:3]])
        
        stats_block = f"## Stats\n\n- Total tags: {total_tags}\n- Main tags: {main_count}\n- Sub tags: {sub_count}\n- Most used: {top_3}\n- Last updated: {today}"
        
        # Regex to replace Stats section (from ## Stats to ## Items)
        master_content = re.sub(r'## Stats\n\n.*?(?=## Items)', stats_block, master_content, flags=re.DOTALL)
        
        # Update Items section - this is trickier in Python without complex regex. 
        # We will just ensure the items are there if we can.
        # In a real scenario, we'd parse and rebuild.
        
        with open(TAG_MASTER_FILE, 'w', encoding='utf-8') as f:
            f.write(master_content)

    # 9. Cleanup Orphans
    deleted_tags = []
    for f in os.listdir(TAGS_DIR):
        if f == 'tag.md': continue
        tag = f.replace('.md', '')
        if tag not in tag_index:
            os.remove(os.path.join(TAGS_DIR, f))
            deleted_tags.append(tag)
            
    deleted_topics = []
    for f in os.listdir(TOPICS_DIR):
        if f == 'tag.md': continue
        topic = f.replace('.md', '')
        if topic not in topic_index:
            os.remove(os.path.join(TOPICS_DIR, f))
            deleted_topics.append(topic)

    # 10. Log to Memory
    with open(MEMORY_FILE, 'a', encoding='utf-8') as f:
        f.write(f"\n## {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} — Indexed\n\n")
        f.write(f"- **Scanned:** {len([x for x in files_data if x['type'] == 'concept'])} concepts + {len([x for x in files_data if x['type'] == 'source'])} sources = {len(files_data)} total files\n")
        f.write(f"- **Tags indexed:** {len(tag_index)} ({len([t for t in tag_index if t in POOL_A])} main-tags + {len([t for t in tag_index if t not in POOL_A])} sub-tags)\n")
        f.write(f"- **Topics indexed:** {len(topic_index)}\n")
        f.write(f"- **Orphans deleted:** {len(deleted_tags)} tag indexes + {len(deleted_topics)} topic indexes\n")
        f.write(f"- **Invalid tags found:** {len(invalid_tags_found)}\n")
        f.write(f"- **Errors:** {errors_skipped} files skipped\n")
    
    print(f"Indexing complete. Scanned {len(files_data)} files. {len(tag_index)} tags, {len(topic_index)} topics.")
    print(f"Invalid tags: {len(invalid_tags_found)}, Skipped: {errors_skipped}")

if __name__ == '__main__':
    run_indexing()
