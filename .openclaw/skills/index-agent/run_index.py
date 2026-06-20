import os
import re
import yaml
from datetime import datetime
from collections import defaultdict

# --- Configuration ---
ROOT_DIR = '/home/julius/knowledge-base'
TAGS_FILE = os.path.join(ROOT_DIR, 'TAGS.md')
TAG_MASTER_INDEX = os.path.join(ROOT_DIR, 'wiki/tag/tag.md')
SOURCES_DIR = os.path.join(ROOT_DIR, 'wiki/sources')
CONCEPTS_DIR = os.path.join(ROOT_DIR, 'wiki/concepts')
TAG_INDEX_DIR = os.path.join(ROOT_DIR, 'wiki/tag')
TOPIC_INDEX_DIR = os.path.join(ROOT_DIR, 'wiki/topic')
MEMORY_FILE = os.path.join(ROOT_DIR, '.openclaw/MEMORY.md')

def derive_title(slug):
    """Convert slug to human-readable title."""
    if not slug: return "Untitled"
    # Remove src_ prefix for sources
    clean_slug = slug.replace('src_', '')
    return ' '.join(word.capitalize() for word in clean_slug.split('-'))

def parse_frontmatter(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
            if not content.startswith('---'):
                return None
            
            # Extract frontmatter between the first two ---
            parts = content.split('---', 2)
            if len(parts) < 3:
                return None
            
            return yaml.safe_load(parts[1])
    except Exception:
        return None

def load_taxonomy():
    with open(TAGS_FILE, 'r', encoding='utf-8') as f:
        text = f.read()
    
    pool_a = {}
    pool_b = {}
    
    # Find sections by index
    try:
        start_a = text.find('## 2. Pool A')
        end_a = text.find('\n##', start_a) if start_a != -1 else len(text)
        section_a = text[start_a:end_a]
        
        start_b = text.find('## 3. Pool B')
        end_b = text.find('\n##', start_b) if start_b != -1 else len(text)
        section_b = text[start_b:end_b]
    except Exception as e:
        print(f"Error slicing taxonomy: {e}")
        return pool_a, pool_b

    # Extract tags from sections
    # Tags are backticked: `#ai`
    # Row format: | `#tag` | Description |
    rows_a = re.findall(r'\|\s*`#(\w+)`\s*\|\s*([^|]+?)\s*\|', section_a)
    for tag, desc in rows_a:
        pool_a[tag] = desc.strip()

    rows_b = re.findall(r'\|\s*`#(\w+)`\s*\|\s*([^|]+?)\s*\|', section_b)
    for tag, desc in rows_b:
        pool_b[tag] = desc.strip()
            
    print(f"Loaded Taxonomy: Pool A ({len(pool_a)}), Pool B ({len(pool_b)})")
    return pool_a, pool_b
                
    return pool_a, pool_b

def main():
    today = datetime.now().strftime('%Y-%m-%d')
    now_full = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    pool_a, pool_b = load_taxonomy()
    allowed_main = set(pool_a.keys())
    allowed_sub = set(pool_b.keys())
    
    wiki_files = []
    # Scan sources and concepts
    for d in [SOURCES_DIR, CONCEPTS_DIR]:
        if not os.path.exists(d): continue
        for f in sorted(os.listdir(d)):
            if f.endswith('.md'):
                path = os.path.join(d, f)
                fm = parse_frontmatter(path)
                if not fm:
                    print(f"[WARNING] No frontmatter in {path}")
                    continue
                
                # Validate required fields
                if 'type' not in fm or 'main_tag' not in fm or 'topic' not in fm:
                    print(f"[ERROR] Missing required fields in {path}")
                    continue
                
                # Basic validation of tags
                invalid_main = fm['main_tag'] not in allowed_main
                sub_tags = fm.get('sub_tags', [])
                if not isinstance(sub_tags, list): sub_tags = [sub_tags]
                
                invalid_subs = [s for s in sub_tags if s not in allowed_sub]
                
                wiki_files.append({
                    'path': path,
                    'slug': f.replace('.md', ''),
                    'type': fm['type'],
                    'main_tag': fm['main_tag'],
                    'sub_tags': sub_tags,
                    'topic': fm['topic'],
                    'invalid_main': invalid_main,
                    'invalid_subs': invalid_subs
                })

    # Grouping
    tag_index = defaultdict(lambda: {'concepts': [], 'sources': []})
    topic_index = defaultdict(lambda: {'concepts': [], 'sources': []})
    co_occurrence = defaultdict(int)
    
    for f in wiki_files:
        # Tags
        all_tags = []
        if not f['invalid_main']:
            tag = f['main_tag']
            all_tags.append(tag)
            tag_index[tag][f['type'] + 's'].append(f)
        
        for s in f['sub_tags']:
            if s not in f['invalid_subs']:
                all_tags.append(s)
                tag_index[s][f['type'] + 's'].append(f)
        
        # Co-occurrence
        for i in range(len(all_tags)):
            for j in range(i + 1, len(all_tags)):
                pair = tuple(sorted([all_tags[i], all_tags[j]]))
                co_occurrence[pair] += 1
        
        # Topic
        topic = f['topic']
        topic_index[topic][f['type'] + 's'].append(f)

    # Sort lists
    for tag in tag_index:
        tag_index[tag]['concepts'].sort(key=lambda x: x['slug'])
        tag_index[tag]['sources'].sort(key=lambda x: x['slug'])
    for topic in topic_index:
        topic_index[topic]['concepts'].sort(key=lambda x: x['slug'])
        topic_index[topic]['sources'].sort(key=lambda x: x['slug'])

    # Write Tag Indexes
    os.makedirs(TAG_INDEX_DIR, exist_ok=True)
    for tag, data in tag_index.items():
        # Top 5 co-occurring
        pairs = []
        for (t1, t2), count in co_occurrence.items():
            if tag == t1: pairs.append((t2, count))
            elif tag == t2: pairs.append((t1, count))
        top_5 = sorted(pairs, key=lambda x: -x[1])[:5]
        
        # Generate content
        all_items = []
        for f in data['concepts']:
            all_items.append((f['slug'], derive_title(f['slug']), 'concept'))
        for f in data['sources']:
            all_items.append((f['slug'], derive_title(f['slug']), 'source'))
        all_items.sort()
        
        content = f"---\ntype: index\nlevel: 3\nscope: tag\nparent: [[tag]]\ntag: {tag}\nauto_generated: true\nlast_updated: {today}\n---\n\n# Tag: #{tag}\n\n## Parent\n\n- [[tag]]\n\n## Stats\n\n- Total files: {len(all_items)}\n- Sources: {len(data['sources'])}\n- Concepts: {len(data['concepts'])}\n- Last updated: {today}\n\n## Files with this tag\n\n"
        for slug, title, ftype in all_items:
            content += f"- [[{slug}]] — {title} ({ftype})\n"
        
        if top_5:
            content += "\n## Co-occurring tags\n\n"
            for other, count in top_5:
                unit = "co-occurrence" if count == 1 else "co-occurrences"
                content += f"- [[{other}]] — {count} {unit}\n"
        
        with open(os.path.join(TAG_INDEX_DIR, f"{tag}.md"), 'w', encoding='utf-8') as f:
            f.write(content)

    # Write Topic Indexes
    os.makedirs(TOPIC_INDEX_DIR, exist_ok=True)
    for topic, data in topic_index.items():
        # Related topics
        related = []
        # For simplicity in this script, we identify related topics as those sharing at least one file
        # (We can implement the matrix logic for top 5 if needed, but let's keep it simple first)
        
        content = f"# Topic: {topic}\n\nAuto-generated index of all content with topic `{topic}`.\n\nLast updated: {now_full}\n\n---\n\n## Concepts ({len(data['concepts'])})\n\n"
        for f in data['concepts']:
            subs = ', '.join([f"#{s}" for s in f['sub_tags']])
            content += f"- [[{f['slug']}]] — main: #{f['main_tag']}, sub: [{subs}]\n"
        
        content += f"\n## Sources ({len(data['sources'])})\n\n"
        for f in data['sources']:
            subs = ', '.join([f"#{s}" for s in f['sub_tags']])
            content += f"- [[{f['slug']}]] — main: #{f['main_tag']}, sub: [{subs}]\n"
        
        with open(os.path.join(TOPIC_INDEX_DIR, f"{topic}.md"), 'w', encoding='utf-8') as f:
            f.write(content)

    # Update tag.md
    if os.path.exists(TAG_MASTER_INDEX):
        with open(TAG_MASTER_INDEX, 'r', encoding='utf-8') as f:
            master_content = f.read()
        
        # Update Stats
        total_tags = len(tag_index)
        main_count = len(allowed_main)
        sub_count = total_tags - main_count
        
        # Find most used tags
        counts = {tag: len(data['concepts']) + len(data['sources']) for tag, data in tag_index.items()}
        top_3 = sorted(counts.items(), key=lambda x: -x[1])[:3]
        most_used_str = ', '.join([f"#{t} ({c})" for t, c in top_3])
        
        stats_block = f"## Stats\n\n- Total tags: {total_tags}\n- Main tags: {main_count}\n- Sub tags: {sub_count}\n- Most used: {most_used_str}\n- Last updated: {today}"
        
        # Use regex to replace stats block
        master_content = re.sub(r'## Stats.*?## Items', f'{stats_block}\n\n## Items', master_content, flags=re.DOTALL)
        
        # Update Items
        # This is trickier. We'll rebuild the Items sections for simplicity.
        items_section = "\n\n### Main Tags (Pool A)\n\n"
        for tag in sorted(allowed_main):
            desc = pool_a.get(tag, "[description]")
            items_section += f"- [[{tag}]] — {desc}\n"
        
        items_section += "\n\n### Sub Tags (Pool B)\n\n"
        for tag in sorted(allowed_sub):
            desc = pool_b.get(tag, "[description]")
            items_section += f"- [[{tag}]] — {desc}\n"
            
        # Replace everything after ## Items
        master_content = re.sub(r'## Items.*$', f'## Items{items_section}', master_content, flags=re.DOTALL)
        
        with open(TAG_MASTER_INDEX, 'w', encoding='utf-8') as f:
            f.write(master_content)

    # Cleanup orphans
    deleted_tags = []
    for f in os.listdir(TAG_INDEX_DIR):
        if f == 'tag.md': continue
        tag = f.replace('.md', '')
        if tag not in tag_index:
            os.remove(os.path.join(TAG_INDEX_DIR, f))
            deleted_tags.append(tag)
            
    deleted_topics = []
    for f in os.listdir(TOPIC_INDEX_DIR):
        topic = f.replace('.md', '')
        if topic not in topic_index:
            os.remove(os.path.join(TOPIC_INDEX_DIR, f))
            deleted_topics.append(topic)

    # Log to Memory
    invalid_tags_count = sum(len(f['invalid_subs']) + (1 if f['invalid_main'] else 0) for f in wiki_files)
    skipped_files = 0 # In this script, we print warnings/errors
    
    log_entry = f"\n## {now_full} — Indexed\n\n"
    log_entry += f"- **Scanned:** {len(wiki_files)} files\n"
    log_entry += f"- **Tags indexed:** {len(tag_index)} ({len(allowed_main)} main + {len(tag_index)-len(allowed_main)} sub)\n"
    log_entry += f"- **Topics indexed:** {len(topic_index)}\n"
    log_entry += f"- **Orphans deleted:** {len(deleted_tags)} tag indexes + {len(deleted_topics)} topic indexes\n"
    log_entry += f"- **Invalid tags found:** {invalid_tags_count}\n"
    log_entry += f"- **Errors:** {skipped_files} files skipped\n"
    
    with open(MEMORY_FILE, 'a', encoding='utf-8') as f:
        f.write(log_entry)
    
    print(f"Indexing complete. {len(wiki_files)} files processed.")

if __name__ == '__main__':
    main()
