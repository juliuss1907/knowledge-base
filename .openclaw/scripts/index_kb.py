import os
import re
import yaml
import datetime
from collections import defaultdict

def derive_title(slug):
    if not slug: return "Untitled"
    # Remove src_ prefix if present
    clean_slug = slug.replace('src_', '')
    return ' '.join(word.capitalize() for word in clean_slug.split('-'))

def load_tags():
    allowed = {'main': [], 'sub': []}
    try:
        with open('TAGS.md', 'r', encoding='utf-8') as f:
            content = f.read()
            # Find Pool A
            pool_a_match = re.search(r'## 2\. Pool A.*?\| Tag \| Description\s*\|(.*?)(?=\n\n|##)', content, re.DOTALL)
            if pool_a_match:
                lines = pool_a_match.group(1).strip().split('\n')
                for line in lines:
                    if line.startswith('|'):
                        tag = line.split('|')[1].strip().strip('#')
                        allowed['main'].append(tag)
            
            # Find Pool B
            pool_b_match = re.search(r'## 3\. Pool B.*?\| Tag \| Description\s*\|(.*?)(?=\n\n|##)', content, re.DOTALL)
            if pool_b_match:
                lines = pool_b_match.group(1).strip().split('\n')
                for line in lines:
                    if line.startswith('|'):
                        tag = line.split('|')[1].strip().strip('#')
                        allowed['sub'].append(tag)
    except Exception as e:
        print(f"Error loading TAGS.md: {e}")
    return allowed

def parse_frontmatter(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
            if not content.startswith('---'):
                return None
            match = re.match(r'^---\s*(.*?)\s*---\s*', content, re.DOTALL)
            if not match:
                return None
            return yaml.safe_load(match.group(1))
    except Exception:
        return None

def get_slug(path):
    filename = os.path.basename(path)
    return filename.replace('.md', '')

def main():
    now = datetime.datetime.now()
    today_str = now.strftime('%Y-%m-%d')
    timestamp = now.strftime('%Y-%m-%d %H:%M:%S')
    
    allowed_tags = load_tags()
    print(f"Allowed tags loaded: {allowed_tags}")
    wiki_dirs = ['wiki/sources', 'wiki/concepts']
    files_data = []
    
    # 1. Scan
    for d in wiki_dirs:
        if not os.path.exists(d): continue
        for f in sorted(os.listdir(d)):
            if not f.endswith('.md'): continue
            path = os.path.join(d, f)
            fm = parse_frontmatter(path)
            if not fm:
                print(f"[WARNING] {path}: No frontmatter found")
                continue
            
            # Required fields
            if 'main_tag' not in fm or 'sub_tags' not in fm or 'topic' not in fm:
                print(f"[ERROR] {path}: Missing required frontmatter fields")
                continue
            
            files_data.append({
                'path': path,
                'type': fm.get('type', 'unknown'),
                'main_tag': fm['main_tag'],
                'sub_tags': fm['sub_tags'] if isinstance(fm['sub_tags'], list) else [fm['sub_tags']],
                'topic': fm['topic'],
                'slug': get_slug(path)
            })

    # 2. Validate Tags
    invalid_tags_log = []
    valid_files = []
    for f in files_data:
        invalid = False
        # Main tag
        if f['main_tag'] not in allowed_tags['main']:
            invalid_tags_log.append(f"[INVALID TAG] {f['path']}: main_tag={f['main_tag']}")
            f['invalid_main'] = True
            invalid = True
        else:
            f['invalid_main'] = False
            
        # Sub tags
        f['invalid_subs'] = []
        for st in f['sub_tags']:
            if st not in allowed_tags['sub']:
                invalid_tags_log.append(f"[INVALID TAG] {f['path']}: sub_tag={st}")
                f['invalid_subs'].append(st)
                invalid = True
        
        valid_files.append(f)

    # 3. Tag Mapping
    tag_index = defaultdict(lambda: {'concepts': [], 'sources': []})
    for f in valid_files:
        # Main tag
        if not f['invalid_main']:
            t = f['main_tag']
            if f['type'] == 'concept': tag_index[t]['concepts'].append(f)
            else: tag_index[t]['sources'].append(f)
        
        # Sub tags
        for st in f['sub_tags']:
            if st not in f['invalid_subs']:
                if f['type'] == 'concept': tag_index[st]['concepts'].append(f)
                else: tag_index[st]['sources'].append(f)

    # Sort tag files
    for t in tag_index:
        tag_index[t]['concepts'].sort(key=lambda x: x['slug'])
        tag_index[t]['sources'].sort(key=lambda x: x['slug'])

    # 4. Co-occurrence
    co_occurrence = defaultdict(int)
    for f in valid_files:
        all_tags = [f['main_tag']] + f['sub_tags']
        # Only count valid tags for co-occurrence? 
        # Workflow says "all tags for this file", but we should probably stick to valid ones
        # based on the "only index tags that exist in TAGS.md" rule.
        valid_tags_in_file = []
        if not f['invalid_main']: valid_tags_in_file.append(f['main_tag'])
        for st in f['sub_tags']:
            if st not in f['invalid_subs']: valid_tags_in_file.append(st)
            
        for i, t1 in enumerate(valid_tags_in_file):
            for t2 in valid_tags_in_file[i+1:]:
                pair = tuple(sorted([t1, t2]))
                co_occurrence[pair] += 1

    tag_co_occur = {}
    for t in tag_index:
        pairs = [(other, count) for (t1, t2), count in co_occurrence.items() 
                 if t in (t1, t2) and (other := t2 if t1 == t else t1)]
        tag_co_occur[t] = sorted(pairs, key=lambda x: -x[1])[:5]

    # 5. Topic Mapping
    topic_index = defaultdict(lambda: {'concepts': [], 'sources': []})
    for f in valid_files:
        t = f['topic']
        if f['type'] == 'concept': topic_index[t]['concepts'].append(f)
        else: topic_index[t]['sources'].append(f)
    
    for t in topic_index:
        topic_index[t]['concepts'].sort(key=lambda x: x['slug'])
        topic_index[t]['sources'].sort(key=lambda x: x['slug'])

    # 6. Topic Overlap
    topic_overlap = defaultdict(int)
    topics = list(topic_index.keys())
    for i, t1 in enumerate(topics):
        files1 = set([f['path'] for f in topic_index[t1]['concepts'] + topic_index[t1]['sources']])
        for t2 in topics[i+1:]:
            files2 = set([f['path'] for f in topic_index[t2]['concepts'] + topic_index[t2]['sources']])
            shared = len(files1 & files2)
            if shared > 0:
                topic_overlap[tuple(sorted([t1, t2]))] = shared

    topic_related = {}
    for t in topic_index:
        pairs = [(other, count) for (t1, t2), count in topic_overlap.items() 
                 if t in (t1, t2) and (other := t2 if t1 == t else t1)]
        topic_related[t] = sorted(pairs, key=lambda x: -x[1])[:5]

    # 7. Write Tag Indexes
    os.makedirs('wiki/tag', exist_ok=True)
    for tag, data in tag_index.items():
        all_items = []
        for f in data['concepts']:
            all_items.append((f['slug'], derive_title(f['slug']), 'concept'))
        for f in data['sources']:
            all_items.append((f['slug'], derive_title(f['slug']), 'source'))
        all_items.sort(key=lambda x: x[0])
        
        content = f"---\ntype: index\nlevel: 3\nscope: tag\nparent: [[tag]]\ntag: {tag}\nauto_generated: true\nlast_updated: {today_str}\n---\n\n"
        content += f"# Tag: #{tag}\n\n## Parent\n\n- [[tag]]\n\n## Stats\n\n"
        content += f"- Total files: {len(data['concepts']) + len(data['sources'])}\n"
        content += f"- Sources: {len(data['sources'])}\n"
        content += f"- Concepts: {len(data['concepts'])}\n"
        content += f"- Last updated: {today_str}\n\n## Files with this tag\n\n"
        
        for slug, title, ftype in all_items:
            content += f"- [[{slug}]] — {title} ({ftype})\n"
        
        co_occur = tag_co_occur.get(tag, [])
        if co_occur:
            content += "\n## Co-occurring tags\n\n"
            for other_tag, count in co_occur:
                unit = "co-occurrence" if count == 1 else "co-occurrences"
                content += f"- [[{other_tag}]] — {count} {unit}\n"
        
        with open(f'wiki/tag/{tag}.md', 'w', encoding='utf-8') as f:
            f.write(content)

    # 8. Write Topic Indexes
    os.makedirs('wiki/topic', exist_ok=True)
    for topic, data in topic_index.items():
        content = f"# Topic: {topic}\n\nAuto-generated index of all content with topic `{topic}`.\n\nLast updated: {timestamp}\n\n---\n\n"
        content += f"## Concepts ({len(data['concepts'])})\n\n"
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
            for other_topic, count in related:
                content += f"- `{other_topic}` ({count} shared files)\n"
        
        with open(f'wiki/topic/{topic}.md', 'w', encoding='utf-8') as f:
            f.write(content)

    # 8.5 Update tag.md
    tag_master_path = 'wiki/tag/tag.md'
    os.makedirs('wiki/tag', exist_ok=True)
    
    # Read TAGS.md for descriptions
    tag_descriptions = {}
    try:
        with open('TAGS.md', 'r', encoding='utf-8') as f:
            for line in f:
                if line.startswith('| #') or line.startswith('| #'):
                    parts = line.split('|')
                    if len(parts) >= 3:
                        tag_name = parts[1].strip().strip('#')
                        desc = parts[2].strip()
                        tag_descriptions[tag_name] = desc
    except: pass

    # Load current tag.md
    tag_master_content = ""
    if os.path.exists(tag_master_path):
        with open(tag_master_path, 'r', encoding='utf-8') as f:
            tag_master_content = f.read()
    else:
        # Basic template
        tag_master_content = "# Tags\n\n## Stats\n\n## Items\n\n### Main Tags (Pool A)\n\n### Sub Tags (Pool B)\n"

    # Update Stats
    total_tags = len(tag_index)
    main_tags_count = len(allowed_tags['main'])
    sub_tags_count = total_tags - main_tags_count
    
    # Calculate most used
    tag_counts = []
    for tag, data in tag_index.items():
        tag_counts.append((len(data['concepts']) + len(data['sources']), tag))
    tag_counts.sort(key=lambda x: -x[0])
    top_3 = tag_counts[:3]
    most_used_str = ", ".join([f"#{t} ({c})" for c, t in top_3])
    
    stats_section = f"## Stats\n\n- Total tags: {total_tags}\n- Main tags: {main_tags_count}\n- Sub tags: {sub_tags_count}\n- Most used: {most_used_str}\n- Last updated: {today_str}\n"
    
    # Replace stats section
    if "## Stats" in tag_master_content:
        tag_master_content = re.sub(r'## Stats.*?## Items', stats_section + "\n\n## Items", tag_master_content, flags=re.DOTALL)
    else:
        tag_master_content = stats_section + "\n\n" + tag_master_content

    # Update Items
    # First, clear existing items under pools and regenerate
    # To keep it simple and consistent with workflow:
    # We'll identify the pool sections and rebuild the list.
    
    def rebuild_pool(content, pool_name, tags_to_add):
        section_start = content.find(f"### {pool_name}")
        if section_start == -1:
            content += f"\n\n### {pool_name}\n\n"
            section_start = content.rfind(f"### {pool_name}")
        
        # Find end of section (next ### or end of file)
        next_section = content.find("### ", section_start + 1)
        if next_section == -1:
            body = content[section_start + len(f"### {pool_name}"):]
            section_end = len(content)
        else:
            body = content[section_start + len(f"### {pool_name}"):next_section]
            section_end = next_section
        
        # Build new list
        new_list = "\n\n"
        for t in sorted(tags_to_add):
            desc = tag_descriptions.get(t, "[description]")
            new_list += f"- [[{t}]] — {desc}\n"
        
        return content[:section_start] + f"### {pool_name}" + new_list + content[section_end:]

    tag_master_content = rebuild_pool(tag_master_content, "Main Tags (Pool A)", [t for t in tag_index if t in allowed_tags['main']])
    tag_master_content = rebuild_pool(tag_master_content, "Sub Tags (Pool B)", [t for t in tag_index if t in allowed_tags['sub']])
    
    with open(tag_master_path, 'w', encoding='utf-8') as f:
        f.write(tag_master_content)

    # 9. Orphan Cleanup
    orphaned_tags = []
    if os.path.exists('wiki/tag'):
        for f in os.listdir('wiki/tag'):
            if f == 'tag.md' or not f.endswith('.md'): continue
            tag = f.replace('.md', '')
            if tag not in tag_index:
                orphaned_tags.append(f)
                os.remove(os.path.join('wiki/tag', f))
                
    orphaned_topics = []
    if os.path.exists('wiki/topic'):
        for f in os.listdir('wiki/topic'):
            if not f.endswith('.md'): continue
            topic = f.replace('.md', '')
            if topic not in topic_index:
                orphaned_topics.append(f)
                os.remove(os.path.join('wiki/topic', f))

    # 10. Log to Memory
    memo_entry = f"## {timestamp} — Indexed\n\n"
    memo_entry += f"- **Scanned:** {len(valid_files)} total files\n"
    memo_entry += f"- **Tags indexed:** {len(tag_index)} ({len(allowed_tags['main'])} main + {len(tag_index)-len(allowed_tags['main'])} sub)\n"
    memo_entry += f"- **Topics indexed:** {len(topic_index)}\n"
    memo_entry += f"- **Orphans deleted:** {len(orphaned_tags)} tag indexes + {len(orphaned_topics)} topic indexes\n"
    
    if invalid_tags_log:
        memo_entry += f"- **Invalid tags found:** {len(invalid_tags_log)}\n"
        for log in invalid_tags_log:
            memo_entry += f"  - {log}\n"
    else:
        memo_entry += f"- **Invalid tags found:** 0\n"

    with open('.openclaw/MEMORY.md', 'a', encoding='utf-8') as f:
        f.write("\n\n" + memo_entry)

    print(f"Index completed. {len(tag_index)} tags, {len(topic_index)} topics. {len(orphaned_tags)} tags cleaned.")

if __name__ == '__main__':
    main()
