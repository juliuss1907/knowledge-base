import os
import re
import yaml
from datetime import datetime
from collections import defaultdict

# --- Configuration ---
ROOT = "/home/julius/knowledge-base"
TAGS_FILE = os.path.join(ROOT, "TAGS.md")
SOURCES_DIR = os.path.join(ROOT, "wiki/sources")
CONCEPTS_DIR = os.path.join(ROOT, "wiki/concepts")
TAG_INDEX_DIR = os.path.join(ROOT, "wiki/tag")
TOPIC_INDEX_DIR = os.path.join(ROOT, "wiki/topic")
MASTER_TAG_FILE = os.path.join(ROOT, "wiki/tag/tag.md")
MEMORY_FILE = os.path.join(ROOT, ".openclaw/MEMORY.md")

def derive_title(slug):
    """Convert slug to human-readable title."""
    # Remove 'src_' prefix for sources
    clean_slug = slug.replace('src_', '')
    return ' '.join(word.capitalize() for word in clean_slug.split('-'))

def load_taxonomy():
    """Parse TAGS.md to get allowed tags and their descriptions."""
    with open(TAGS_FILE, 'r', encoding='utf-8') as f:
        content = f.read()
    
    main_tags = {}
    sub_tags = {}
    
    current_pool = None
    lines = content.split('\n')
    
    for line in lines:
        stripped = line.strip()
        if not stripped: continue
        
        if "## 2. Pool A" in line:
            current_pool = 'A'
            continue
        elif "## 3. Pool B" in line:
            current_pool = 'B'
            continue
        elif line.startswith('##'):
            current_pool = None
            continue
            
        if current_pool and line.startswith('|'):
            if 'Tag' in line and 'Description' in line:
                continue
            parts = [p.strip() for p in line.split('|')]
            if len(parts) >= 3:
                tag = parts[1].replace('#', '')
                desc = parts[2]
                if current_pool == 'A':
                    main_tags[tag] = desc
                else:
                    sub_tags[tag] = desc
                    
    return main_tags, sub_tags

def get_frontmatter(path):
    """Extract YAML frontmatter from a markdown file."""
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if match:
        try:
            return yaml.safe_load(match.group(1))
        except yaml.YAMLError:
            return None
    return None

def run_indexing():
    print("Starting Index Agent run...")
    
    main_taxonomy, sub_taxonomy = load_taxonomy()
    all_allowed_tags = {**main_taxonomy, **sub_taxonomy}
    
    files_data = []
    errors = 0
    invalid_tags_found = []
    
    # 1. Scan files
    for directory in [SOURCES_DIR, CONCEPTS_DIR]:
        if not os.path.exists(directory):
            continue
        for filename in sorted(os.listdir(directory)):
            if filename.endswith(".md"):
                path = os.path.join(directory, filename)
                slug = filename[:-3]
                fm = get_frontmatter(path)
                
                if not fm:
                    print(f"[ERROR] Missing or invalid frontmatter in {path}")
                    errors += 1
                    continue
                
                # Extract fields
                f_type = fm.get('type')
                main_tag = fm.get('main_tag')
                sub_tags = fm.get('sub_tags', [])
                topic = fm.get('topic')
                
                if not all([f_type, main_tag, topic]):
                    print(f"[ERROR] Missing required fields in {path}")
                    errors += 1
                    continue
                
                # Validate tags
                if main_tag not in main_taxonomy:
                    invalid_tags_found.append(f"{path}: main_tag={main_tag}")
                
                invalid_subs = []
                if isinstance(sub_tags, list):
                    for st in sub_tags:
                        if st not in sub_taxonomy:
                            invalid_subs.append(st)
                            invalid_tags_found.append(f"{path}: sub_tag={st}")
                
                files_data.append({
                    'path': path,
                    'slug': slug,
                    'type': f_type,
                    'main_tag': main_tag,
                    'sub_tags': sub_tags if isinstance(sub_tags, list) else [],
                    'topic': topic,
                    'invalid_main': main_tag not in main_taxonomy,
                    'invalid_subs': invalid_subs
                })

    # 2. Build Mappings
    tag_index = defaultdict(lambda: {'concepts': [], 'sources': []})
    topic_index = defaultdict(lambda: {'concepts': [], 'sources': []})
    
    for f in files_data:
        # Topic mapping
        if f['type'] == 'concept':
            topic_index[f['topic']]['concepts'].append(f)
        else:
            topic_index[f['topic']]['sources'].append(f)
            
        # Tag mapping
        # Main tag
        if not f['invalid_main']:
            t = f['main_tag']
            if f['type'] == 'concept':
                tag_index[t]['concepts'].append(f)
            else:
                tag_index[t]['sources'].append(f)
        
        # Sub tags
        for st in f['sub_tags']:
            if st not in f['invalid_subs']:
                if f['type'] == 'concept':
                    tag_index[st]['concepts'].append(f)
                else:
                    tag_index[st]['sources'].append(f)

    # 3. Co-occurrence and Overlap
    co_occurrence = defaultdict(int)
    for f in files_data:
        all_f_tags = [f['main_tag']] + f['sub_tags']
        all_f_tags = [t for t in all_f_tags if t in all_allowed_tags]
        for i in range(len(all_f_tags)):
            for j in range(i + 1, len(all_f_tags)):
                pair = tuple(sorted([all_f_tags[i], all_f_tags[j]]))
                co_occurrence[pair] += 1
                
    tag_co_occur = {}
    for tag in tag_index:
        pairs = [(other, count) for (t1, t2), count in co_occurrence.items() 
                 if tag in (t1, t2) and (other := t2 if t1 == tag else t1)]
        tag_co_occur[tag] = sorted(pairs, key=lambda x: -x[1])[:5]

    topic_overlap = defaultdict(int)
    for t1 in topic_index:
        files1 = set([f['path'] for f in topic_index[t1]['concepts'] + topic_index[t1]['sources']])
        for t2 in topic_index:
            if t1 >= t2: continue
            files2 = set([f['path'] for f in topic_index[t2]['concepts'] + topic_index[t2]['sources']])
            shared = len(files1 & files2)
            if shared > 0:
                topic_overlap[tuple(sorted([t1, t2]))] = shared
                
    topic_related = {}
    for topic in topic_index:
        pairs = [(other, count) for (t1, t2), count in topic_overlap.items() 
                 if topic in (t1, t2) and (other := t2 if t1 == topic else t1)]
        topic_related[topic] = sorted(pairs, key=lambda x: -x[1])[:5]

    # 4. Write Tag Indexes
    os.makedirs(TAG_INDEX_DIR, exist_ok=True)
    today = datetime.now().strftime('%Y-%m-%d')
    
    for tag, data in tag_index.items():
        all_items = []
        for f in data['concepts']:
            all_items.append((f['slug'], derive_title(f['slug']), 'concept'))
        for f in data['sources']:
            all_items.append((f['slug'], derive_title(f['slug']), 'source'))
        all_items.sort()
        
        content = f"---\ntype: index\nlevel: 3\nscope: tag\nparent: [[tag]]\ntag: {tag}\nauto_generated: true\nlast_updated: {today}\n---\n\n# Tag: #{tag}\n\n## Parent\n\n- [[tag]]\n\n## Stats\n\n- Total files: {len(all_items)}\n- Sources: {len(data['sources'])}\n- Concepts: {len(data['concepts'])}\n- Last updated: {today}\n\n## Files with this tag\n\n"
        
        for slug, title, ftype in all_items:
            content += f"- [[{slug}]] — {title} ({ftype})\n"
            
        if tag in tag_co_occur:
            content += "\n## Co-occurring tags\n\n"
            for other_tag, count in tag_co_occur[tag]:
                unit = "co-occurrence" if count == 1 else "co-occurrences"
                content += f"- [[{other_tag}]] — {count} {unit}\n"
                
        with open(os.path.join(TAG_INDEX_DIR, f"{tag}.md"), 'w', encoding='utf-8') as f:
            f.write(content)

    # 5. Write Topic Indexes
    os.makedirs(TOPIC_INDEX_DIR, exist_ok=True)
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
            for other_topic, count in topic_related[topic]:
                content += f"- `{other_topic}` ({count} shared files)\n"
                
        with open(os.path.join(TOPIC_INDEX_DIR, f"{topic}.md"), 'w', encoding='utf-8') as f:
            f.write(content)

    # 6. Update Master tag.md
    if os.path.exists(MASTER_TAG_FILE):
        with open(MASTER_TAG_FILE, 'r', encoding='utf-8') as f:
            master_content = f.read()
        
        # Update Stats
        total_tags = len(tag_index)
        main_count = len(main_taxonomy)
        sub_count = total_tags - main_count
        
        # Find top 3 most used
        tag_counts = {tag: len(data['concepts']) + len(data['sources']) for tag, data in tag_index.items()}
        top_3 = sorted(tag_counts.items(), key=lambda x: -x[1])[:3]
        most_used_str = ", ".join([f"#{t} ({c})" for t, c in top_3])
        
        stats_block = f"## Stats\n\n- Total tags: {total_tags}\n- Main tags: {main_count}\n- Sub tags: {sub_count}\n- Most used: {most_used_str}\n- Last updated: {today}"
        
        # Replace Stats section
        master_content = re.sub(r'## Stats.*?## Items', stats_block + '\n\n## Items', master_content, flags=re.DOTALL)
        
        # Update Items
        for tag, desc in all_allowed_tags.items():
            entry = f"- [[{tag}]] — {desc}"
            if entry not in master_content:
                pool = "Main Tags (Pool A)" if tag in main_taxonomy else "Sub Tags (Pool B)"
                pattern = rf"(### {re.escape(pool)}.*?)(?:\n\n|###|$)"
                match = re.search(pattern, master_content, flags=re.DOTALL)
                if match:
                    start, end = match.span()
                    master_content = master_content[:end] + f"\n{entry}" + master_content[end:]
        
        with open(MASTER_TAG_FILE, 'w', encoding='utf-8') as f:
            f.write(master_content)
    else:
        print(f"[WARNING] {MASTER_TAG_FILE} not found. Skipping master update.")

    # 7. Orphan Cleanup
    deleted_tags = []
    for filename in os.listdir(TAG_INDEX_DIR):
        if filename == "tag.md": continue
        tag = filename[:-3]
        if tag not in tag_index:
            os.remove(os.path.join(TAG_INDEX_DIR, filename))
            deleted_tags.append(tag)
            
    deleted_topics = []
    for filename in os.listdir(TOPIC_INDEX_DIR):
        if filename.endswith(".md"):
            topic = filename[:-3]
            if topic not in topic_index:
                os.remove(os.path.join(TOPIC_INDEX_DIR, filename))
                deleted_topics.append(topic)

    # 8. Log to Memory
    log_entry = f"\n## {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} — Indexed\n\n"
    log_entry += f"- **Scanned:** {len(files_data)} total files\n"
    log_entry += f"- **Tags indexed:** {len(tag_index)} ({len(main_taxonomy)} main + {len(tag_index)-len(main_taxonomy)} sub)\n"
    log_entry += f"- **Topics indexed:** {len(topic_index)}\n"
    log_entry += f"- **Orphans deleted:** {len(deleted_tags)} tag indexes + {len(deleted_topics)} topic indexes\n"
    log_entry += f"- **Invalid tags found:** {len(invalid_tags_found)}\n"
    log_entry += f"- **Errors:** {errors} files skipped\n"
    
    if invalid_tags_found:
        log_entry += "\n### Invalid Tag Details\n"
        for it in invalid_tags_found:
            log_entry += f"- {it}\n"

    with open(MEMORY_FILE, 'a', encoding='utf-8') as f:
        f.write(log_entry)

    print("Indexing complete.")
    return {
        "scanned": len(files_data),
        "tags": len(tag_index),
        "topics": len(topic_index),
        "orphans_tag": len(deleted_tags),
        "orphans_topic": len(deleted_topics),
        "invalid": len(invalid_tags_found),
        "errors": errors
    }

if __name__ == "__main__":
    run_indexing()
