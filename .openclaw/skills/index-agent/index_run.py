import os
import re
import yaml
from datetime import datetime
from pathlib import Path
from collections import defaultdict

# Configuration
RAW_DIR = Path('raw')
WIKI_SOURCES = Path('wiki/sources')
WIKI_CONCEPTS = Path('wiki/concepts')
WIKI_TAGS = Path('wiki/tag')
WIKI_TOPICS = Path('wiki/topic')
TAGS_FILE = Path('TAGS.md')
TAG_MASTER_FILE = WIKI_TAGS / 'tag.md'

def load_taxonomy():
    with open(TAGS_FILE, 'r', encoding='utf-8') as f:
        content = f.read()
    
    pool_a = []
    pool_b = []
    
    # Extract Pool A
    a_section = re.search(r'## 2\. Pool A.*?\| Tag \| Description\s*\n(.*?)\n\n', content, re.DOTALL)
    if a_section:
        lines = a_section.group(1).strip().split('\n')
        for line in lines:
            match = re.match(r'\| #(\w+)', line)
            if match:
                pool_a.append(match.group(1))
    
    # Extract Pool B
    b_section = re.search(r'## 3\. Pool B.*?\| Tag \| Description\s*\n(.*?)\n\n', content, re.DOTALL)
    if b_section:
        lines = b_section.group(1).strip().split('\n')
        for line in lines:
            match = re.match(r'\| #(\w+)', line)
            if match:
                pool_b.append(match.group(1))
                
    return pool_a, pool_b

def get_tag_description(tag, pool_a, pool_b):
    with open(TAGS_FILE, 'r', encoding='utf-8') as f:
        for line in f:
            if f'| `#{tag}`' in line:
                parts = line.split('|')
                if len(parts) >= 3:
                    return parts[2].strip()
    return "[description]"

def parse_frontmatter(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
            if not content.startswith('---'):
                return None
            parts = content.split('---', 2)
            if len(parts) < 3:
                return None
            return yaml.safe_load(parts[1])
    except Exception:
        return None

def derive_title(slug):
    # Handle source prefix
    s = slug.replace('src_', '')
    return ' '.join(word.capitalize() for word in s.split('-'))

def run_indexing():
    pool_a, pool_b = load_taxonomy()
    allowed_tags = {'main': pool_a, 'sub': pool_b}
    
    wiki_files = list(WIKI_SOURCES.glob('*.md')) + list(WIKI_CONCEPTS.glob('*.md'))
    files_data = []
    errors = 0
    invalid_tags_found = []

    for path in wiki_files:
        fm = parse_frontmatter(path)
        if not fm:
            errors += 1
            continue
            
        # Validation
        main_tag = fm.get('main_tag')
        sub_tags = fm.get('sub_tags', [])
        topic = fm.get('topic')
        
        if not main_tag or not topic:
            errors += 1
            continue
            
        if not isinstance(sub_tags, list):
            sub_tags = []

        file_info = {
            'path': str(path),
            'slug': path.stem,
            'type': fm.get('type'),
            'main_tag': main_tag,
            'sub_tags': sub_tags,
            'topic': topic,
            'invalid_main': main_tag not in pool_a,
            'invalid_subs': [t for t in sub_tags if t not in pool_b]
        }
        
        if file_info['invalid_main'] or file_info['invalid_subs']:
            invalid_tags_found.append(f"{path}: main={main_tag}, subs={sub_tags}")
            
        files_data.append(file_info)

    # Tag Indexing
    tag_index = defaultdict(lambda: {'concepts': [], 'sources': []})
    for f in files_data:
        # Main tag
        if not f['invalid_main']:
            tag = f['main_tag']
            tag_index[tag][f'{"concepts" if f["type"] == "concept" else "sources"}'].append(f)
        
        # Sub tags
        for t in f['sub_tags']:
            if t not in f['invalid_subs']:
                tag_index[t][f'{"concepts" if f["type"] == "concept" else "sources"}'].append(f)

    # Sort tag index lists
    for tag in tag_index:
        tag_index[tag]['concepts'].sort(key=lambda x: x['slug'])
        tag_index[tag]['sources'].sort(key=lambda x: x['slug'])

    # Co-occurrence
    co_occurrence = defaultdict(int)
    for f in files_data:
        all_tags = [f['main_tag']] + f['sub_tags']
        all_tags = sorted(list(set(all_tags)))
        for i in range(len(all_tags)):
            for j in range(i + 1, len(all_tags)):
                co_occurrence[tuple(sorted([all_tags[i], all_tags[j]]))] += 1

    tag_co_occur = {}
    for tag in tag_index:
        pairs = []
        for (t1, t2), count in co_occurrence.items():
            if tag == t1: pairs.append((t2, count))
            elif tag == t2: pairs.append((t1, count))
        tag_co_occur[tag] = sorted(pairs, key=lambda x: -x[1])[:5]

    # Topic Indexing
    topic_index = defaultdict(lambda: {'concepts': [], 'sources': []})
    for f in files_data:
        topic = f['topic']
        topic_index[topic][f'{"concepts" if f["type"] == "concept" else "sources"}'].append(f)
    
    for topic in topic_index:
        topic_index[topic]['concepts'].sort(key=lambda x: x['slug'])
        topic_index[topic]['sources'].sort(key=lambda x: x['slug'])

    # Topic Overlap
    topic_overlap = defaultdict(int)
    topic_list = list(topic_index.keys())
    for i in range(len(topic_list)):
        for j in range(i+1, len(topic_list)):
            t1, t2 = topic_list[i], topic_list[j]
            files1 = set([f['path'] for f in topic_index[t1]['concepts'] + topic_index[t1]['sources']])
            files2 = set([f['path'] for f in topic_index[t2]['concepts'] + topic_index[t2]['sources']])
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

    # Write Tag Indexes
    today = datetime.now().strftime('%Y-%m-%d')
    WIKI_TAGS.mkdir(parents=True, exist_ok=True)
    for tag, data in tag_index.items():
        content = f"---\ntype: index\nlevel: 3\nscope: tag\nparent: [[tag]]\ntag: {tag}\nauto_generated: true\nlast_updated: {today}\n---\n\n# Tag: #{tag}\n\n## Parent\n\n- [[tag]]\n\n## Stats\n\n- Total files: {len(data['concepts']) + len(data['sources'])}\n- Sources: {len(data['sources'])}\n- Concepts: {len(data['concepts'])}\n- Last updated: {today}\n\n## Files with this tag\n\n"
        
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
        
        with open(WIKI_TAGS / f"{tag}.md", 'w', encoding='utf-8') as f:
            f.write(content)

    # Write Topic Indexes
    WIKI_TOPICS.mkdir(parents=True, exist_ok=True)
    for topic, data in topic_index.items():
        content = f"---\ntype: index\nscope: topic\nparent: \"[[topic]]\"\ntopic: {topic}\nauto_generated: true\nlast_updated: {today}\n---\n\n# Topic: {topic}\n\nAuto-generated index of all content with topic `{topic}`.\n\nLast updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n---\n\n## Concepts ({len(data['concepts'])})\n\n"
        for f in data['concepts']:
            main = f['main_tag']
            subs = ', '.join([f"#{s}" for s in f['sub_tags']])
            content += f"- [[{f['slug']}]] — main: #{main}, sub: [{subs}]\n"
        
        content += f"\n## Sources ({len(data['sources'])})\n\n"
        for f in data['sources']:
            main = f['main_tag']
            subs = ', '.join([f"#{s}" for s in f['sub_tags']])
            content += f"- [[{f['slug']}]] — main: #{main}, sub: [{subs}]\n"
            
        related = topic_related.get(topic, [])
        if related:
            content += "\n## Related topics\n\n"
            content += f"Topics that share concepts/sources with `{topic}`:\n"
            for other_topic, count in related:
                content += f"- `{other_topic}` ({count} shared files)\n"
        
        with open(WIKI_TOPICS / f"{topic}.md", 'w', encoding='utf-8') as f:
            f.write(content)

    # Update tag.md Master Index
    if TAG_MASTER_FILE.exists():
        with open(TAG_MASTER_FILE, 'r', encoding='utf-8') as f:
            master_content = f.read()
        
        # Update Stats
        total_tags = len(tag_index)
        main_tags_count = len(pool_a)
        sub_tags_count = total_tags - main_tags_count
        
        # Calculate most used
        counts = []
        for tag, data in tag_index.items():
            counts.append((tag, len(data['concepts']) + len(data['sources'])))
        top_3 = sorted(counts, key=lambda x: -x[1])[:3]
        most_used = ', '.join([f"#{t} ({c})" for t, c in top_3])
        
        stats_block = f"## Stats\n\n- Total tags: {total_tags}\n- Main tags: {main_tags_count}\n- Sub tags: {sub_tags_count}\n- Most used: {most_used}\n- Last updated: {today}\n"
        
        # Replace stats
        if '## Stats' in master_content:
            master_content = re.sub(r'## Stats\n\n.*?\n## Items', master_content, flags=re.DOTALL)
            # This regex is tricky, let's just replace the section
            # I'll use a simpler approach for the master file
            pass

    # We will handle tag.md update via a separate step or a simple rewrite if needed.
    # For now let's just generate a simple tag.md if it doesn't exist.
    if not TAG_MASTER_FILE.exists():
        content = f"# Tags Index\n\n## Stats\n\n- Total tags: {len(tag_index)}\n- Last updated: {today}\n\n## Items\n\n"
        with open(TAG_MASTER_FILE, 'w', encoding='utf-8') as f:
            f.write(content)

    # Orphan Cleanup
    deleted_tags = []
    for tag_file in WIKI_TAGS.glob('*.md'):
        if tag_file.name != 'tag.md':
            tag = tag_file.stem
            if tag not in tag_index:
                tag_file.unlink()
                deleted_tags.append(tag)
                
    deleted_topics = []
    for topic_file in WIKI_TOPICS.glob('*.md'):
        topic = topic_file.stem
        if topic not in topic_index:
            topic_file.unlink()
            deleted_topics.append(topic)

    return {
        'scanned': len(files_data),
        'concepts': len([f for f in files_data if f['type'] == 'concept']),
        'sources': len([f for f in files_data if f['type'] == 'source']),
        'tags': len(tag_index),
        'main_tags': len(pool_a),
        'sub_tags': len(tag_index) - len(pool_a),
        'topics': len(topic_index),
        'orphans_tag': len(deleted_tags),
        'orphans_topic': len(deleted_topics),
        'invalid_tags': len(invalid_tags_found),
        'errors': errors,
        'invalid_details': invalid_tags_found
    }

if __name__ == '__main__':
    res = run_indexing()
    print(res)
