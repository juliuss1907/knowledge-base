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
TAG_MASTER_FILE = os.path.join(ROOT, "wiki/tag/tag.md")
MEMORY_FILE = os.path.join(ROOT, ".openclaw/MEMORY.md")

POOL_A = ['ai', 'crypto', 'tech', 'productivity', 'system', 'economic', 'politic', 'health', 'investment']
POOL_B = ['hack', 'tools', 'automation', 'vibecode', 'research', 'tutorial', 'opinion', 'news', 'defi', 'perpdex', 'layer1', 'layer2', 'law', 'coding', 'psychology', 'health', 'ai', 'system', 'geopolitics']

def derive_title(slug):
    # Remove src_ prefix if present
    clean_slug = slug.replace('src_', '')
    return ' '.join(word.capitalize() for word in clean_slug.split('-'))

def parse_frontmatter(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
        match = re.search(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
        if not match:
            return None
        try:
            return yaml.safe_load(match.group(1))
        except Exception:
            return None

def main():
    today = datetime.now().strftime('%Y-%m-%d')
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    files_data = []
    errors = []
    invalid_tags = []
    
    # Step 1: Scan Wiki Files
    search_dirs = [(SOURCES_DIR, 'source'), (CONCEPTS_DIR, 'concept')]
    for directory, ftype in search_dirs:
        if not os.path.exists(directory):
            continue
        for filename in sorted(os.listdir(directory)):
            if not filename.endswith('.md'):
                continue
            path = os.path.join(directory, filename)
            fm = parse_frontmatter(path)
            if not fm:
                errors.append(f"[WARNING] {path}: No valid frontmatter")
                continue
            
            # Basic Validation
            main_tag = fm.get('main_tag')
            sub_tags = fm.get('sub_tags', [])
            topic = fm.get('topic')
            
            if not main_tag or not topic:
                errors.append(f"[ERROR] {path}: Missing required fields (main_tag or topic)")
                continue
            
            if not isinstance(sub_tags, list):
                sub_tags = []

            # Tag Validation
            invalid_main = False
            if main_tag not in POOL_A:
                invalid_tags.append(f"[INVALID TAG] {path}: main_tag={main_tag}")
                invalid_main = True
            
            invalid_subs = []
            for st in sub_tags:
                if st not in POOL_B:
                    invalid_tags.append(f"[INVALID TAG] {path}: sub_tag={st}")
                    invalid_subs.append(st)
            
            slug = filename[:-3]
            files_data.append({
                'path': path,
                'slug': slug,
                'type': ftype,
                'main_tag': main_tag,
                'sub_tags': sub_tags,
                'topic': topic,
                'invalid_main': invalid_main,
                'invalid_subs': invalid_subs
            })

    # Step 3 & 4: Tag Indexing and Co-occurrence
    tag_index = defaultdict(lambda: {'concepts': [], 'sources': []})
    co_occurrence = defaultdict(int)
    
    for f in files_data:
        # Valid tags only for indexing
        current_file_tags = []
        if not f['invalid_main']:
            tag = f['main_tag']
            tag_index[tag][f'{"concepts" if f["type"] == "concept" else "sources"}'].append(f)
            current_file_tags.append(tag)
        
        for st in f['sub_tags']:
            if st not in f['invalid_subs']:
                tag = st
                tag_index[tag][f'{"concepts" if f["type"] == "concept" else "sources"}'].append(f)
                current_file_tags.append(tag)
        
        # Co-occurrence (all tags, including invalid ones if present in frontmatter)
        # Actually, the workflow says "Build co-occurrence matrix" - usually this is for valid tags.
        # Let's use valid tags only to avoid polluting index.
        current_file_tags = sorted(list(set(current_file_tags)))
        for i in range(len(current_file_tags)):
            for j in range(i + 1, len(current_file_tags)):
                pair = tuple(sorted([current_file_tags[i], current_file_tags[j]]))
                co_occurrence[pair] += 1

    # Step 5 & 6: Topic Indexing and Overlap
    topic_index = defaultdict(lambda: {'concepts': [], 'sources': []})
    for f in files_data:
        topic = f['topic']
        topic_index[topic][f'{"concepts" if f["type"] == "concept" else "sources"}'].append(f)

    # Topic Overlap
    topic_overlap = defaultdict(int)
    topics = sorted(topic_index.keys())
    for i in range(len(topics)):
        t1 = topics[i]
        files1 = {f['path'] for f in topic_index[t1]['concepts'] + topic_index[t1]['sources']}
        for j in range(i + 1, len(topics)):
            t2 = topics[j]
            files2 = {f['path'] for f in topic_index[t2]['concepts'] + topic_index[t2]['sources']}
            shared = len(files1 & files2)
            if shared > 0:
                topic_overlap[tuple(sorted([t1, t2]))] = shared

    # Step 7: Write Tag Index Files
    os.makedirs(TAG_INDEX_DIR, exist_ok=True)
    for tag, data in tag_index.items():
        # Top 5 co-occurring
        pairs = []
        for (t1, t2), count in co_occurrence.items():
            if tag == t1: pairs.append((t2, count))
            elif tag == t2: pairs.append((t1, count))
        top_5_co = sorted(pairs, key=lambda x: -x[1])[:5]
        
        # Content
        all_items = []
        for f in data['concepts']:
            all_items.append((f['slug'], derive_title(f['slug']), 'concept'))
        for f in data['sources']:
            all_items.append((f['slug'], derive_title(f['slug']), 'source'))
        all_items.sort()
        
        content = f"---\ntype: index\nlevel: 3\nscope: tag\nparent: [[tag]]\ntag: {tag}\nauto_generated: true\nlast_updated: {today}\n---\n\n# Tag: #{tag}\n\n## Parent\n\n- [[tag]]\n\n## Stats\n\n- Total files: {len(all_items)}\n- Sources: {len(data['sources'])}\n- Concepts: {len(data['concepts'])}\n- Last updated: {today}\n\n## Files with this tag\n\n"
        for slug, title, ftype in all_items:
            content += f"- [[{slug}]] — {title} ({ftype})\n"
        
        if top_5_co:
            content += "\n## Co-occurring tags\n\n"
            for other_tag, count in top_5_co:
                unit = "co-occurrence" if count == 1 else "co-occurrences"
                content += f"- [[{other_tag}]] — {count} {unit}\n"
        
        with open(os.path.join(TAG_INDEX_DIR, f"{tag}.md"), 'w', encoding='utf-8') as f:
            f.write(content)

    # Step 8: Write Topic Index Files
    os.makedirs(TOPIC_INDEX_DIR, exist_ok=True)
    for topic, data in topic_index.items():
        # Top 5 related
        pairs = []
        for (t1, t2), count in topic_overlap.items():
            if topic == t1: pairs.append((t2, count))
            elif topic == t2: pairs.append((t1, count))
        top_5_rel = sorted(pairs, key=lambda x: -x[1])[:5]
        
        content = f"# Topic: {topic}\n\nAuto-generated index of all content with topic `{topic}`.\n\nLast updated: {timestamp}\n\n---\n\n## Concepts ({len(data['concepts'])})\n\n"
        for f in sorted(data['concepts'], key=lambda x: x['slug']):
            subs = ', '.join([f"#{s}" for s in f['sub_tags']])
            content += f"- [[{f['slug']}]] — main: #{f['main_tag']}, sub: [{subs}]\n"
        
        content += f"\n## Sources ({len(data['sources'])})\n\n"
        for f in sorted(data['sources'], key=lambda x: x['slug']):
            subs = ', '.join([f"#{s}" for s in f['sub_tags']])
            content += f"- [[{f['slug']}]] — main: #{f['main_tag']}, sub: [{subs}]\n"
        
        if top_5_rel:
            content += "\n## Related topics\n\n"
            content += f"Topics that share concepts/sources with `{topic}`:\n"
            for other_topic, count in top_5_rel:
                content += f"- `{other_topic}` ({count} shared files)\n"
        
        with open(os.path.join(TOPIC_INDEX_DIR, f"{topic}.md"), 'w', encoding='utf-8') as f:
            f.write(content)

    # Step 8.5: Update tag.md
    if os.path.exists(TAG_MASTER_FILE):
        with open(TAG_MASTER_FILE, 'r', encoding='utf-8') as f:
            master_content = f.read()
        
        # Update Items
        with open(TAGS_FILE, 'r', encoding='utf-8') as f:
            tags_text = f.read()
        
        for tag in sorted(tag_index.keys()):
            if f"- [[{tag}]]" not in master_content:
                # Find description in TAGS.md
                desc_match = re.search(rf"\| `#{tag}` \| (.*?)\|", tags_text)
                desc = desc_match.group(1).strip() if desc_match else "[description]"
                
                pool = "Main Tags (Pool A)" if tag in POOL_A else "Sub Tags (Pool B)"
                header = f"### {pool}"
                if header in master_content:
                    # Insert after header
                    parts = master_content.split(header)
                    # This is a bit naive, we want to insert it at the start of the list under the header
                    # but for simplicity in this script, we'll just append a line.
                    # A better way is using a regex replace.
                    master_content = master_content.replace(header, f"{header}\n- [[{tag}]] — {desc}")
        
        # Update Stats
        total_tags = len(tag_index)
        main_tags_count = len([t for t in tag_index if t in POOL_A])
        sub_tags_count = total_tags - main_tags_count
        
        tag_counts = {}
        for tag in tag_index:
            tag_counts[tag] = len(tag_index[tag]['concepts']) + len(tag_index[tag]['sources'])
        
        top_3 = sorted(tag_counts.items(), key=lambda x: -x[1])[:3]
        most_used = ', '.join([f"#{t} ({c})" for t, c in top_3])
        
        stats_block = f"## Stats\n\n- Total tags: {total_tags}\n- Main tags: {main_tags_count}\n- Sub tags: {sub_tags_count}\n- Most used: {most_used}\n- Last updated: {today}"
        
        # Replace Stats section
        if "## Stats" in master_content:
            master_content = re.sub(r'## Stats.*? (## Items|$) ', stats_block + '\n\n', master_content, flags=re.DOTALL)
        else:
            master_content = stats_block + '\n\n' + master_content
            
        with open(TAG_MASTER_FILE, 'w', encoding='utf-8') as f:
            f.write(master_content)

    # Step 9: Cleanup Orphans
    orphaned_tags = []
    if os.path.exists(TAG_INDEX_DIR):
        for filename in os.listdir(TAG_INDEX_DIR):
            if filename == 'tag.md' or not filename.endswith('.md'): continue
            tag = filename[:-3]
            if tag not in tag_index:
                orphaned_tags.append(tag)
                os.remove(os.path.join(TAG_INDEX_DIR, filename))
                
    orphaned_topics = []
    if os.path.exists(TOPIC_INDEX_DIR):
        for filename in os.listdir(TOPIC_INDEX_DIR):
            if not filename.endswith('.md'): continue
            topic = filename[:-3]
            if topic not in topic_index:
                orphaned_topics.append(topic)
                os.remove(os.path.join(TOPIC_INDEX_DIR, filename))

    # Step 10: Log to Memory
    scanned_concepts = len([f for f in files_data if f['type'] == 'concept'])
    scanned_sources = len([f for f in files_data if f['type'] == 'source'])
    
    log_entry = f"## {timestamp} — Indexed\n\n"
    log_entry += f"- **Scanned:** {scanned_concepts} concepts + {scanned_sources} sources = {len(files_data)} total files\n"
    log_entry += f"- **Tags indexed:** {len(tag_index)} ({len([t for t in tag_index if t in POOL_A])} main-tags + {len([t for t in tag_index if t in POOL_B])} sub-tags)\n"
    log_entry += f"- **Topics indexed:** {len(topic_index)}\n"
    log_entry += f"- **Orphans deleted:** {len(orphaned_tags)} tag indexes + {len(orphaned_topics)} topic indexes\n"
    log_entry += f"- **Invalid tags found:** {len(invalid_tags)}\n"
    log_entry += f"- **Errors:** {len(errors)} files skipped\n\n"
    
    if invalid_tags:
        log_entry += "### Invalid Tag Details\n"
        log_entry += "\n".join(invalid_tags) + "\n\n"
        
    with open(MEMORY_FILE, 'a', encoding='utf-8') as f:
        f.write(log_entry)

    print(f"Success: {len(files_data)} files processed. Tags: {len(tag_index)}, Topics: {len(topic_index)}.")
    print(f"Orphans deleted: {len(orphaned_tags)} tags, {len(orphaned_topics)} topics.")
    print(f"Invalid tags: {len(invalid_tags)}, Errors: {len(errors)}.")

if __name__ == '__main__':
    main()
