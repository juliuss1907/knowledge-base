import os
import yaml
import re
from datetime import datetime
from collections import defaultdict

# --- CONFIGURATION ---
WORKSPACE_ROOT = "/home/julius/knowledge-base"
TAGS_FILE = os.path.join(WORKSPACE_ROOT, "TAGS.md")
WIKI_SOURCES = os.path.join(WORKSPACE_ROOT, "wiki/sources")
WIKI_CONCEPTS = os.path.join(WORKSPACE_ROOT, "wiki/concepts")
WIKI_TAGS_DIR = os.path.join(WORKSPACE_ROOT, "wiki/tag")
WIKI_TOPICS_DIR = os.path.join(WORKSPACE_ROOT, "wiki/topic")
TAG_MASTER_FILE = os.path.join(WIKI_TAGS_DIR, "tag.md")
MEMORY_FILE = os.path.join(WORKSPACE_ROOT, ".openclaw/MEMORY.md")

def derive_title(slug):
    # Remove 'src_' prefix for sources
    clean_slug = slug.replace('src_', '')
    return ' '.join(word.capitalize() for word in clean_slug.split('-'))

def parse_frontmatter(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
        match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
        if not match:
            return None
        try:
            return yaml.safe_load(match.group(1))
        except yaml.YAMLError:
            return None

def load_tags_taxonomy():
    allowed = {'main': [], 'sub': []}
    if not os.path.exists(TAGS_FILE):
        return allowed
    with open(TAGS_FILE, 'r', encoding='utf-8') as f:
        for line in f:
            if '| `#ai`' in line: allowed['main'].append('ai')
            elif '| `#crypto`' in line: allowed['main'].append('crypto')
            elif '| `#tech`' in line: allowed['main'].append('tech')
            elif '| `#productivity`' in line: allowed['main'].append('productivity')
            elif '| `#system`' in line: allowed['main'].append('system')
            elif '| `#economic`' in line: allowed['main'].append('economic')
            elif '| `#politic`' in line: allowed['main'].append('politic')
            
            # Sub tags logic
            if '| `#hack`' in line: allowed['sub'].append('hack')
            elif '| `#tools`' in line: allowed['sub'].append('tools')
            elif '| `#automation`' in line: allowed['sub'].append('automation')
            elif '| `#vibecode`' in line: allowed['sub'].append('vibecode')
            elif '| `#research`' in line: allowed['sub'].append('research')
            elif '| `#tutorial`' in line: allowed['sub'].append('tutorial')
            elif '| `#opinion`' in line: allowed['sub'].append('opinion')
            elif '| `#news`' in line: allowed['sub'].append('news')
            elif '| `#defi`' in line: allowed['sub'].append('defi')
            elif '| `#perpdex`' in line: allowed['sub'].append('perpdex')
            elif '| `#layer1`' in line: allowed['sub'].append('layer1')
            elif '| `#layer2`' in line: allowed['sub'].append('layer2')
    
    # Fallback if parsing failed
    if not allowed['main']:
        allowed['main'] = ['ai', 'crypto', 'tech', 'productivity', 'system', 'economic', 'politic']
    if not allowed['sub']:
        allowed['sub'] = ['hack', 'tools', 'automation', 'vibecode', 'research', 'tutorial', 'opinion', 'news', 'defi', 'perpdex', 'layer1', 'layer2']
    return allowed

def main():
    allowed_tags = load_tags_taxonomy()
    files_data = []
    errors = 0
    invalid_tags_found = []

    # 1. Scan
    for directory in [WIKI_SOURCES, WIKI_CONCEPTS]:
        if not os.path.exists(directory): continue
        for filename in sorted(os.listdir(directory)):
            if not filename.endswith('.md'): continue
            path = os.path.join(directory, filename)
            fm = parse_frontmatter(path)
            if not fm:
                errors += 1
                continue
            
            slug = filename[:-3]
            main_tag = fm.get('main_tag')
            sub_tags = fm.get('sub_tags', [])
            topic = fm.get('topic')
            
            if not main_tag or not topic:
                errors += 1
                continue

            # Validate tags
            invalid_main = False
            if main_tag not in allowed_tags['main']:
                invalid_tags_found.append(f"{path}: main_tag={main_tag}")
                invalid_main = True
            
            invalid_subs = []
            for st in sub_tags:
                if st not in allowed_tags['sub']:
                    invalid_tags_found.append(f"{path}: sub_tag={st}")
                    invalid_subs.append(st)

            files_data.append({
                'path': path,
                'slug': slug,
                'type': fm.get('type', 'source' if 'sources' in path else 'concept'),
                'main_tag': main_tag,
                'sub_tags': sub_tags,
                'topic': topic,
                'invalid_main': invalid_main,
                'invalid_subs': invalid_subs
            })

    # 2. Group by Tag
    tag_index = defaultdict(lambda: {'concepts': [], 'sources': []})
    co_occurrence = defaultdict(int)
    
    for f in files_data:
        all_tags_for_file = []
        
        if not f['invalid_main']:
            tag = f['main_tag']
            tag_index[tag][f['type'] + 's'].append(f)
            all_tags_for_file.append(tag)
            
        for st in f['sub_tags']:
            if st not in f['invalid_subs']:
                tag_index[st][f['type'] + 's'].append(f)
                all_tags_for_file.append(st)
        
        # Co-occurrence
        all_tags_for_file.sort()
        for i in range(len(all_tags_for_file)):
            for j in range(i + 1, len(all_tags_for_file)):
                pair = tuple(sorted([all_tags_for_file[i], all_tags_for_file[j]]))
                co_occurrence[pair] += 1

    # 3. Group by Topic
    topic_index = defaultdict(lambda: {'concepts': [], 'sources': []})
    for f in files_data:
        topic_index[f['topic']][f['type'] + 's'].append(f)

    # Topic Overlap
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

    # 4. Write Tag Indexes
    os.makedirs(WIKI_TAGS_DIR, exist_ok=True)
    today = datetime.now().strftime('%Y-%m-%d')
    
    for tag, data in tag_index.items():
        # Co-occurring tags top 5
        pairs = []
        for (t1, t2), count in co_occurrence.items():
            if tag == t1: pairs.append((t2, count))
            elif tag == t2: pairs.append((t1, count))
        top_5_co = sorted(pairs, key=lambda x: -x[1])[:5]

        all_items = []
        for f in data['concepts']: all_items.append((f['slug'], derive_title(f['slug']), 'concept'))
        for f in data['sources']: all_items.append((f['slug'], derive_title(f['slug']), 'source'))
        all_items.sort()

        content = f"---\ntype: index\nlevel: 3\nscope: tag\nparent: [[tag]]\ntag: {tag}\nauto_generated: true\nlast_updated: {today}\n---\n\n# Tag: #{tag}\n\n## Parent\n\n- [[tag]]\n\n## Stats\n\n- Total files: {len(all_items)}\n- Sources: {len(data['sources'])}\n- Concepts: {len(data['concepts'])}\n- Last updated: {today}\n\n## Files with this tag\n\n"
        for slug, title, ftype in all_items:
            content += f"- [[{slug}]] — {title} ({ftype})\n"
        
        if top_5_co:
            content += "\n## Co-occurring tags\n\n"
            for other, count in top_5_co:
                unit = "co-occurrence" if count == 1 else "co-occurrences"
                content += f"- [[{other}]] — {count} {unit}\n"
        
        with open(os.path.join(WIKI_TAGS_DIR, f"{tag}.md"), 'w', encoding='utf-8') as f:
            f.write(content)

    # 5. Write Topic Indexes
    os.makedirs(WIKI_TOPICS_DIR, exist_ok=True)
    for topic, data in topic_index.items():
        # Related topics top 5
        pairs = []
        for (t1, t2), count in topic_overlap.items():
            if topic == t1: pairs.append((t2, count))
            elif topic == t2: pairs.append((t1, count))
        top_5_rel = sorted(pairs, key=lambda x: -x[1])[:5]

        content = f"# Topic: {topic}\n\nAuto-generated index of all content with topic `{topic}`.\n\nLast updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n---\n\n## Concepts ({len(data['concepts'])})\n\n"
        for f in sorted(data['concepts'], key=lambda x: x['slug']):
            subs = ', '.join([f"#{s}" for s in f['sub_tags']])
            content += f"- [[{f['slug']}]] — main: #{f['main_tag']}, sub: [{subs}]\n"
        
        content += f"\n## Sources ({len(data['sources'])})\n\n"
        for f in sorted(data['sources'], key=lambda x: x['slug']):
            subs = ', '.join([f"#{s}" for s in f['sub_tags']])
            content += f"- [[{f['slug']}]] — main: #{f['main_tag']}, sub: [{subs}]\n"
        
        if top_5_rel:
            content += "\n## Related topics\n\nTopics that share concepts/sources with `{topic}`:\n"
            for other, count in top_5_rel:
                content += f"- `{other}` ({count} shared files)\n"
        
        with open(os.path.join(WIKI_TOPICS_DIR, f"{topic}.md"), 'w', encoding='utf-8') as f:
            f.write(content)

    # 6. Update tag.md
    if os.path.exists(TAG_MASTER_FILE):
        with open(TAG_MASTER_FILE, 'r', encoding='utf-8') as f:
            master_content = f.read()
        
        # Update Stats
        total_tags = len(tag_index)
        main_tags_count = len(allowed_tags['main'])
        sub_tags_count = total_tags - main_tags_count
        
        # Calculate most used
        tag_counts = []
        for tag, data in tag_index.items():
            tag_counts.append((len(data['concepts']) + len(data['sources']), tag))
        tag_counts.sort(key=lambda x: -x[0])
        most_used = ", ".join([f"#{t} ({c})" for c, t in tag_counts[:3]])
        
        stats_block = f"## Stats\n\n- Total tags: {total_tags}\n- Main tags: {main_tags_count}\n- Sub tags: {sub_tags_count}\n- Most used: {most_used}\n- Last updated: {today}"
        
        if "## Stats" in master_content:
            master_content = re.sub(r'## Stats.*?(?=## Items|$)', stats_block, master_content, flags=re.DOTALL)
        else:
            master_content = "## Stats\n\n" + stats_block + "\n\n" + master_content
        
        # Update Items
        for tag in sorted(tag_index.keys()):
            if f"- [[{tag}]]" not in master_content:
                # Get description from TAGS.md
                desc = "[description]"
                if os.path.exists(TAGS_FILE):
                    with open(TAGS_FILE, 'r', encoding='utf-8') as tf:
                        for line in tf:
                            if f'| `#{tag}`' in line:
                                desc = line.split('|')[-1].strip()
                                break
                
                pool = "Main Tags (Pool A)" if tag in allowed_tags['main'] else "Sub Tags (Pool B)"
                if f"### {pool}" in master_content:
                    master_content = master_content.replace(f"### {pool}", f"### {pool}\n- [[{tag}]] — {desc}")
        
        with open(TAG_MASTER_FILE, 'w', encoding='utf-8') as f:
            f.write(master_content)

    # 7. Cleanup Orphans
    orphaned_tags = 0
    for filename in os.listdir(WIKI_TAGS_DIR):
        if filename == 'tag.md' or not filename.endswith('.md'): continue
        tag = filename[:-3]
        if tag not in tag_index:
            os.remove(os.path.join(WIKI_TAGS_DIR, filename))
            orphaned_tags += 1
            
    orphaned_topics = 0
    for filename in os.listdir(WIKI_TOPICS_DIR):
        if not filename.endswith('.md'): continue
        topic = filename[:-3]
        if topic not in topic_index:
            os.remove(os.path.join(WIKI_TOPICS_DIR, filename))
            orphaned_topics += 1

    # 8. Summary
    summary = (
        f"## {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} — Indexed\n\n"
        f"- **Scanned:** {len([f for f in files_data if f['type'] == 'concept'])} concepts + "
        f"{len([f for f in files_data if f['type'] == 'source'])} sources = {len(files_data)} total files\n"
        f"- **Tags indexed:** {len(tag_index)} ({len(allowed_tags['main'])} main-tags + {len(tag_index) - len(allowed_tags['main'])} sub-tags)\n"
        f"- **Topics indexed:** {len(topic_index)}\n"
        f"- **Orphans deleted:** {orphaned_tags} tag indexes + {orphaned_topics} topic indexes\n"
        f"- **Invalid tags found:** {len(invalid_tags_found)}\n"
        f"- **Errors:** {errors} files skipped\n"
    )
    
    if invalid_tags_found:
        summary += "\n### Invalid Tag Details\n"
        for it in invalid_tags_found:
            summary += f"- {it}\n"

    print(summary)

if __name__ == "__main__":
    main()
