#!/usr/bin/env python3
"""Format Validator — validates wiki file format compliance against format-spec.md and index-spec.md.

Usage: python3 scripts/validate.py
Output: writes issue lines to stdout as SEVERITY|CATEGORY|REL_PATH|MESSAGE

Intended to be run from the knowledge-base root:
    cd /home/julius/knowledge-base
    python3 .hermes/skills/format-validator/scripts/validate.py 2>&1
"""
import os, sys, re, yaml
from datetime import date, datetime
from pathlib import Path
from collections import defaultdict

KB = Path(os.getcwd())
if not (KB / 'wiki').exists() or not (KB / 'TAGS.md').exists():
    # Try parent
    KB = Path('/home/julius/knowledge-base')

# Pool A tags (from TAGS.md v1.3 — update when TAGS.md changes)
POOL_A = {'ai', 'crypto', 'tech', 'productivity', 'system', 'economic', 'politic', 'health', 'investment'}

# Pool B tags (from TAGS.md v1.4 — update when TAGS.md changes)
POOL_B = {'hack', 'tools', 'automation', 'vibecode', 'research', 'tutorial', 'opinion', 'news',
          'defi', 'perpdex', 'layer1', 'layer2', 'law', 'coding', 'psychology', 'health', 'ai', 'system', 'geopolitics', 'strategy'}

VALID_STATUSES = {'draft', 'reviewed', 'needs-revision'}
SKIP_FILES = {'context/USER.md', 'wiki/reviews/_action-required.md'}

def parse_frontmatter(content):
    if not content.startswith('---'):
        return None, None, "Missing opening ---"
    end = content.find('\n---', 3)
    if end == -1:
        end = content.find('---', 3)
    if end == -1:
        return None, None, "Missing closing ---"
    raw = content[3:end].strip()
    try:
        fm = yaml.safe_load(raw)
    except yaml.YAMLError as e:
        return None, raw, f"Invalid YAML: {e}"
    if fm is None:
        return {}, raw, None
    if not isinstance(fm, dict):
        return None, raw, "Frontmatter is not a YAML mapping"
    return fm, raw, None

def get_heading_sections(content):
    lines = content.split('\n')
    start = 0
    if content.startswith('---'):
        end = content.find('\n---', 3)
        if end != -1:
            start = content[:end+4].count('\n')
    h1 = None
    h2s = []
    for line in lines[start:]:
        stripped = line.strip()
        if stripped.startswith('# ') and not stripped.startswith('## '):
            if h1 is None:
                h1 = stripped[2:].strip()
        elif stripped.startswith('## '):
            h2s.append(stripped[3:].strip())
    return h1, h2s

def validate_date(val):
    if isinstance(val, (date, datetime)):
        return 2000 <= val.year <= 2030
    if isinstance(val, str):
        return bool(re.match(r'^\d{4}-\d{2}-\d{2}$', val))
    return False

def codeblock_issues(body, rel):
    issues = []
    in_fence = False
    for line in body.splitlines():
        stripped = line.strip()
        if not stripped.startswith('```'):
            continue
        suffix = stripped[3:].strip()
        if not in_fence:
            if suffix == '':
                issues.append(('ERROR', 'Markdown', rel, 'Code block missing language tag'))
            elif suffix != suffix.lower():
                issues.append(('WARNING', 'Markdown', rel, f'Code block language tag uppercase: "{suffix}"'))
            in_fence = True
        else:
            in_fence = False
    return issues

def validate_concept(filepath, fm, raw_fm, content):
    issues = []
    rel = str(filepath.relative_to(KB))
    
    required = ['type', 'status', 'main_tag', 'sub_tags', 'topic', 'sources', 'last_updated']
    for field in required:
        if field not in fm:
            issues.append(('ERROR', 'Frontmatter', rel, f'Missing required field: {field}'))
    
    if 'type' in fm and fm['type'] != 'concept':
        issues.append(('ERROR', 'Frontmatter', rel, f'type is "{fm["type"]}" but file in wiki/concepts/ — should be "concept"'))
    
    if 'status' in fm and isinstance(fm['status'], str) and fm['status'] not in VALID_STATUSES:
        issues.append(('ERROR', 'Frontmatter', rel, f'status "{fm["status"]}" not in allowed values'))
    
    if 'main_tag' in fm:
        mt = fm['main_tag']
        if isinstance(mt, str) and mt not in POOL_A:
            if mt in POOL_B:
                issues.append(('ERROR', 'Frontmatter', rel, f'main_tag "{mt}" is in Pool B (sub-tag only), must be Pool A'))
            else:
                issues.append(('ERROR', 'Frontmatter', rel, f'main_tag "{mt}" not in TAGS.md Pool A'))
    
    if 'sub_tags' in fm:
        st = fm['sub_tags']
        if not isinstance(st, list):
            issues.append(('ERROR', 'Frontmatter', rel, f'sub_tags must be an array, got {type(st).__name__}'))
        else:
            if len(st) < 1:
                issues.append(('ERROR', 'Frontmatter', rel, 'sub_tags has less than 1 item (minimum 1)'))
            if len(st) > 3:
                issues.append(('ERROR', 'Frontmatter', rel, f'sub_tags has {len(st)} items (max 3)'))
            for tag in st:
                if isinstance(tag, str):
                    if tag not in POOL_B and tag not in POOL_A:
                        issues.append(('ERROR', 'Frontmatter', rel, f'sub_tags contains "{tag}" — not in TAGS.md'))
                    elif tag in POOL_A and tag not in POOL_B:
                        issues.append(('ERROR', 'Frontmatter', rel, f'sub_tags contains "{tag}" — only in Pool A, needs Pool B sub-tag'))
    
    if 'last_updated' in fm and not validate_date(fm['last_updated']):
        issues.append(('ERROR', 'Frontmatter', rel, f'last_updated not valid ISO date: {fm["last_updated"]}'))
    
    if 'topic' in fm:
        topic = fm['topic']
        if isinstance(topic, str) and len(topic) > 60:
            issues.append(('ERROR', 'Frontmatter', rel, f'topic slug exceeds 60 chars: {len(topic)} chars'))
    
    if 'sources' in fm:
        src = fm['sources']
        if isinstance(src, str):
            if src.strip() in ('', '[]', '-'):
                issues.append(('WARNING', 'Frontmatter', rel, 'sources field is empty'))
        elif isinstance(src, list):
            if len(src) == 0:
                issues.append(('WARNING', 'Frontmatter', rel, 'sources array is empty'))
            for s in src:
                if isinstance(s, str) and s.strip() == '':
                    issues.append(('WARNING', 'Frontmatter', rel, 'sources contains empty entry'))
    
    # Field order
    expected_order = ['type', 'status', 'main_tag', 'sub_tags', 'topic', 'sources', 'last_updated']
    actual_order = [k for k in fm.keys()]
    expected_present = [f for f in expected_order if f in actual_order]
    if actual_order != expected_present:
        issues.append(('WARNING', 'Frontmatter', rel, f'Field order mismatch (expected {expected_present}, got {actual_order})'))
    
    # Section structure
    h1, h2s = get_heading_sections(content)
    if h1 is None:
        issues.append(('ERROR', 'Sections', rel, 'File has no H1 title'))
    
    required_sections = ['Definition', 'Key ideas', 'Related concepts', 'Sources']
    for sec in required_sections:
        if sec not in h2s:
            issues.append(('ERROR', 'Sections', rel, f'Missing required section: ## {sec}'))
    
    # Duplicate sections
    h2_counts = {}
    for h in h2s:
        h2_counts[h] = h2_counts.get(h, 0) + 1
    for sec, count in h2_counts.items():
        if count > 1:
            issues.append(('ERROR', 'Sections', rel, f'Duplicate section "## {sec}" appears {count} times'))
    
    # Section order
    present = [s for s in required_sections if s in h2s]
    ordered = sorted(present, key=lambda s: required_sections.index(s))
    if len(present) >= 2 and present != ordered:
        issues.append(('WARNING', 'Sections', rel, f'Section order mismatch: got {present}, expected {ordered}'))
    
    # Naming
    slug = filepath.stem
    if ' ' in slug:
        issues.append(('ERROR', 'Naming', rel, f'Slug contains spaces: "{slug}"'))
    if '_' in slug:
        issues.append(('ERROR', 'Naming', rel, f'Slug contains underscores (use hyphens): "{slug}"'))
    if slug != slug.lower():
        issues.append(('WARNING', 'Naming', rel, f'Slug uses uppercase letters'))
    if len(slug) > 50:
        issues.append(('ERROR', 'Naming', rel, f'Slug exceeds 50 chars ({len(slug)} chars)'))
    
    # Body checks
    body_start = content.find('\n---', 3)
    body = content[body_start+4:] if body_start != -1 else content
    
    issues.extend(codeblock_issues(body, rel))
    
    if re.search(r'\[\[\s+[^\]]+\]\]|\[\[[^\]]+\s+\]\]', body):
        issues.append(('ERROR', 'Markdown', rel, 'Wikilink has spaces around brackets'))
    
    # Broken wikilinks (WARNING only — forward-references expected in growing KB)
    all_wikilinks = re.findall(r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]', body)
    broken = set()
    for target in all_wikilinks:
        target = target.strip()
        if '/' in target or target.startswith('..'):
            continue
        # Normalize: strip .md extension — Compile Agent often writes .md inside wikilinks.
        # Without this, '[[src_foo.md]]' is probed as 'src_foo.md.md' and falsely flagged broken.
        probe = target[:-3] if target.endswith('.md') else target
        found = False
        for d in ['wiki/concepts', 'wiki/sources', 'wiki/tag', 'wiki/topic', 'raw']:
            if (KB / d / f'{probe}.md').exists():
                found = True; break
        if not found:
            for rd in ['articles', 'posts', 'videos', 'papers', 'websites', 'repos', 'tools']:
                rdir = KB / 'raw' / rd
                if rdir.exists() and ((rdir / f'{probe}.md').exists() or list(rdir.glob(f'*_{probe}.md'))):
                    found = True; break
        if not found:
            broken.add(target)
    
    if broken:
        if len(broken) <= 5:
            for t in sorted(broken)[:5]:
                issues.append(('WARNING', 'Markdown', rel, f'Broken wikilink: [[{t}]] — target not found'))
            if len(broken) > 5:
                issues.append(('WARNING', 'Markdown', rel, f'...and {len(broken)-5} more broken wikilinks'))
        else:
            issues.append(('WARNING', 'Markdown', rel, f'{len(broken)} broken wikilinks (forward-references to uncompiled concepts)'))
    
    return issues

def validate_source(filepath, fm, raw_fm, content):
    issues = []
    rel = str(filepath.relative_to(KB))
    
    required = ['type', 'original', 'main_tag', 'sub_tags', 'topic', 'date_compiled']
    for field in required:
        if field not in fm:
            issues.append(('ERROR', 'Frontmatter', rel, f'Missing required field: {field}'))
    
    if 'type' in fm and fm['type'] != 'source':
        issues.append(('ERROR', 'Frontmatter', rel, f'type is "{fm["type"]}" but should be "source"'))
    
    if 'main_tag' in fm:
        mt = fm['main_tag']
        if isinstance(mt, str) and mt not in POOL_A:
            if mt in POOL_B:
                issues.append(('ERROR', 'Frontmatter', rel, f'main_tag "{mt}" is in Pool B, must be Pool A'))
            else:
                issues.append(('ERROR', 'Frontmatter', rel, f'main_tag "{mt}" not in TAGS.md Pool A'))
    
    if 'sub_tags' in fm:
        st = fm['sub_tags']
        if not isinstance(st, list):
            issues.append(('ERROR', 'Frontmatter', rel, f'sub_tags must be array'))
        else:
            if len(st) < 1:
                issues.append(('ERROR', 'Frontmatter', rel, 'sub_tags has less than 1 item'))
            if len(st) > 3:
                issues.append(('ERROR', 'Frontmatter', rel, f'sub_tags has {len(st)} items (max 3)'))
            for tag in st:
                if isinstance(tag, str):
                    if tag not in POOL_B and tag not in POOL_A:
                        issues.append(('ERROR', 'Frontmatter', rel, f'sub_tags contains "{tag}" — not in TAGS.md'))
                    elif tag in POOL_A and tag not in POOL_B:
                        issues.append(('ERROR', 'Frontmatter', rel, f'sub_tags contains "{tag}" — Pool A only, needs Pool B tag'))
    
    if 'date_compiled' in fm and not validate_date(fm['date_compiled']):
        issues.append(('ERROR', 'Frontmatter', rel, f'date_compiled not valid ISO date'))
    
    if 'original' in fm:
        orig = fm['original']
        if isinstance(orig, str) and orig.startswith('[['):
            target = orig[2:-2].strip()
            # Strip .md extension if present — wikilinks often include it
            if target.endswith('.md'):
                target = target[:-3]
            found = False
            for d in ['articles', 'posts', 'videos', 'papers', 'websites', 'repos', 'tools']:
                rdir = KB / 'raw' / d
                if rdir.exists():
                    # Direct match: raw/<d>/<target>.md
                    if (rdir / f'{target}.md').exists():
                        found = True; break
                    # Date-prefix match: raw/<d>/YYYY-MM-DD_<target>.md
                    if list(rdir.glob(f'*_{target}.md')):
                        found = True; break
            if not found:
                issues.append(('WARNING', 'Frontmatter', rel, f'original wikilink [[{target}]] — raw file not found'))
        elif isinstance(orig, list):
            issues.append(('WARNING', 'Frontmatter', rel, 'original: unquoted wikilink parsed as nested list (YAML)'))
    
    # Field order
    expected_order = ['type', 'original', 'main_tag', 'sub_tags', 'topic', 'date_compiled', 'url', 'author']
    actual_order = [k for k in fm.keys()]
    expected_present = [f for f in expected_order if f in actual_order]
    if actual_order != expected_present:
        issues.append(('WARNING', 'Frontmatter', rel, f'Field order mismatch'))
    
    # Sections
    h1, h2s = get_heading_sections(content)
    if h1 is None:
        issues.append(('ERROR', 'Sections', rel, 'File has no H1 title'))
    
    required_sections = ['Metadata', 'Summary', 'Key points', 'Concepts referenced']
    for sec in required_sections:
        if sec not in h2s:
            issues.append(('ERROR', 'Sections', rel, f'Missing required section: ## {sec}'))
    
    # Duplicates
    h2_counts = {}
    for h in h2s:
        h2_counts[h] = h2_counts.get(h, 0) + 1
    for sec, count in h2_counts.items():
        if count > 1:
            issues.append(('ERROR', 'Sections', rel, f'Duplicate section "## {sec}" appears {count} times'))
    
    # Section order
    present = [s for s in required_sections if s in h2s]
    ordered = sorted(present, key=lambda s: required_sections.index(s))
    if len(present) >= 2 and present != ordered:
        issues.append(('WARNING', 'Sections', rel, 'Section order mismatch'))
    
    # Naming
    slug = filepath.stem
    if not slug.startswith('src_'):
        issues.append(('ERROR', 'Naming', rel, 'Missing "src_" prefix'))
    else:
        slug_body = slug[4:]
        if ' ' in slug_body:
            issues.append(('ERROR', 'Naming', rel, 'Slug contains spaces'))
        if slug_body != slug_body.lower():
            issues.append(('WARNING', 'Naming', rel, 'Slug uses uppercase'))
        if len(slug_body) > 50:
            issues.append(('ERROR', 'Naming', rel, f'Slug exceeds 50 chars ({len(slug_body)} chars)'))
    
    # Body
    body_start = content.find('\n---', 3)
    body = content[body_start+4:] if body_start != -1 else content
    
    issues.extend(codeblock_issues(body, rel))
    
    # Broken wikilinks
    all_wikilinks = re.findall(r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]', body)
    broken = set()
    for target in all_wikilinks:
        target = target.strip()
        if '/' in target:
            continue
        # Normalize: strip .md extension — Compile Agent often writes .md inside wikilinks.
        probe = target[:-3] if target.endswith('.md') else target
        found = False
        for d in ['wiki/concepts', 'wiki/sources', 'wiki/tag', 'wiki/topic', 'raw']:
            if (KB / d / f'{probe}.md').exists():
                found = True; break
        if not found:
            for rd in ['articles', 'posts', 'videos', 'papers', 'websites', 'repos', 'tools']:
                rdir = KB / 'raw' / rd
                if rdir.exists() and ((rdir / f'{probe}.md').exists() or list(rdir.glob(f'*_{probe}.md'))):
                    found = True; break
        if not found:
            broken.add(target)
    if broken:
        if len(broken) <= 3:
            for t in sorted(broken):
                issues.append(('WARNING', 'Markdown', rel, f'Broken wikilink: [[{t}]]'))
        else:
            issues.append(('WARNING', 'Markdown', rel, f'{len(broken)} broken wikilinks (forward-references)'))
    
    return issues

def get_path_level(rel):
    """Derive expected index level from filesystem path. Returns None if path doesn't imply a specific level."""
    if rel == 'wiki/tag/tag.md':
        return 2
    if rel.startswith('wiki/tag/'):
        return 3
    if rel in ('wiki/wiki.md', 'raw/raw.md', 'context/context.md'):
        return 1
    # raw/<subtype>/<subtype>.md → Tầng 2
    parts = rel.split('/')
    if len(parts) == 3 and parts[0] == 'raw':
        fname = parts[2].replace('.md', '')
        if fname == parts[1]:
            return 2
    return None

def validate_index(filepath, fm, raw_fm, content):
    issues = []
    rel = str(filepath.relative_to(KB))
    
    level = fm.get('level')
    if level is None:
        issues.append(('ERROR', 'Frontmatter', rel, 'Missing level field for index'))
        return issues
    
    try:
        level_int = int(level)
    except (TypeError, ValueError):
        issues.append(('ERROR', 'Frontmatter', rel, f'Invalid level value: {level}'))
        return issues
    
    # Cross-check level against filesystem path — path always wins
    path_level = get_path_level(rel)
    if path_level is not None and level_int != path_level:
        issues.append(('ERROR', 'Frontmatter', rel,
            f'level field ({level_int}) contradicts filesystem path (expected {path_level})'))
        level_int = path_level  # Validate against path-derived tier, not declared level
    
    if level_int == 1:
        issues.extend(validate_index_l1(filepath, fm, content))
    elif level_int == 2:
        issues.extend(validate_index_l2(filepath, fm, content))
    elif level_int == 3:
        issues.extend(validate_index_l3(filepath, fm, content))
    else:
        issues.append(('ERROR', 'Frontmatter', rel, f'Unknown index level: {level_int}'))
    
    return issues

def validate_index_l1(filepath, fm, content):
    issues = []
    rel = str(filepath.relative_to(KB))
    
    if fm.get('type') != 'index':
        issues.append(('ERROR', 'Frontmatter', rel, 'type should be "index"'))
    if fm.get('level') != 1:
        issues.append(('ERROR', 'Frontmatter', rel, f'level should be 1, got {fm.get("level")}'))
    if fm.get('scope') not in ('raw', 'wiki', 'context'):
        issues.append(('ERROR', 'Frontmatter', rel, f'scope should be raw/wiki/context, got "{fm.get("scope")}"'))
    if fm.get('auto_generated') != False:
        issues.append(('ERROR', 'Frontmatter', rel, 'auto_generated should be false'))
    
    required = ['type', 'level', 'scope', 'auto_generated', 'last_updated']
    for f in required:
        if f not in fm:
            issues.append(('ERROR', 'Frontmatter', rel, f'Missing required field: {f}'))
    
    if 'last_updated' in fm and not validate_date(fm['last_updated']):
        issues.append(('ERROR', 'Frontmatter', rel, f'last_updated not valid ISO date'))
    
    h1, h2s = get_heading_sections(content)
    if h1 is None:
        issues.append(('ERROR', 'Sections', rel, 'File has no H1 title'))
    for sec in ['Overview', 'Sub-indexes', 'Notes']:
        if sec not in h2s:
            issues.append(('ERROR', 'Sections', rel, f'Missing required section: ## {sec}'))
    
    return issues

def validate_index_l2(filepath, fm, content):
    issues = []
    rel = str(filepath.relative_to(KB))
    
    if fm.get('type') != 'index':
        issues.append(('ERROR', 'Frontmatter', rel, 'type should be "index"'))
    if fm.get('level') != 2:
        issues.append(('ERROR', 'Frontmatter', rel, f'level should be 2, got {fm.get("level")}'))
    
    valid_scopes = ['articles', 'posts', 'websites', 'videos', 'papers', 'repos', 'tools', 'tags']
    if fm.get('scope') not in valid_scopes:
        issues.append(('ERROR', 'Frontmatter', rel, f'scope should be one of {valid_scopes}, got "{fm.get("scope")}"'))
    
    if fm.get('auto_generated') != False:
        issues.append(('ERROR', 'Frontmatter', rel, 'auto_generated should be false'))
    
    if fm.get('items_managed_by') not in ('ingest-agent', 'index-agent'):
        issues.append(('ERROR', 'Frontmatter', rel, f'items_managed_by should be ingest-agent or index-agent'))
    
    parent = fm.get('parent')
    if parent is not None:
        if isinstance(parent, list):
            issues.append(('WARNING', 'Frontmatter', rel, 'parent: unquoted [[...]] parsed as nested list — use quoted format'))
        elif isinstance(parent, str) and not parent.startswith('[['):
            issues.append(('ERROR', 'Frontmatter', rel, f'parent should be wikilink [[...]], got "{parent}"'))
    
    required = ['type', 'level', 'scope', 'parent', 'auto_generated', 'items_managed_by', 'last_updated']
    for f in required:
        if f not in fm:
            issues.append(('ERROR', 'Frontmatter', rel, f'Missing required field: {f}'))
    
    if 'last_updated' in fm and not validate_date(fm['last_updated']):
        issues.append(('ERROR', 'Frontmatter', rel, f'last_updated not valid ISO date'))
    
    h1, h2s = get_heading_sections(content)
    if h1 is None:
        issues.append(('ERROR', 'Sections', rel, 'File has no H1 title'))
    for sec in ['Overview', 'Parent', 'Stats', 'Items', 'Notes']:
        if sec not in h2s:
            issues.append(('ERROR', 'Sections', rel, f'Missing required section: ## {sec}'))
    
    return issues

def validate_index_l3(filepath, fm, content):
    issues = []
    rel = str(filepath.relative_to(KB))
    
    if fm.get('type') != 'index':
        issues.append(('ERROR', 'Frontmatter', rel, 'type should be "index"'))
    if fm.get('level') != 3:
        issues.append(('ERROR', 'Frontmatter', rel, f'level should be 3, got {fm.get("level")}'))
    if fm.get('scope') != 'tag':
        issues.append(('ERROR', 'Frontmatter', rel, f'scope should be "tag", got "{fm.get("scope")}"'))
    if fm.get('auto_generated') != True:
        issues.append(('ERROR', 'Frontmatter', rel, 'auto_generated should be true'))
    
    fname = filepath.stem
    tag_field = fm.get('tag')
    if tag_field and str(tag_field) != fname:
        issues.append(('ERROR', 'Frontmatter', rel, f'tag field "{tag_field}" does not match filename "{fname}"'))
    
    parent = fm.get('parent')
    if parent is not None:
        if isinstance(parent, list):
            issues.append(('WARNING', 'Frontmatter', rel, 'parent: unquoted wikilink parsed as list — use quoted format'))
        elif isinstance(parent, str) and parent != '[[tag]]':
            issues.append(('ERROR', 'Frontmatter', rel, f'parent should be [[tag]], got "{parent}"'))
    
    required = ['type', 'level', 'scope', 'parent', 'tag', 'auto_generated', 'last_updated']
    for f in required:
        if f not in fm:
            issues.append(('ERROR', 'Frontmatter', rel, f'Missing required field: {f}'))
    
    if 'last_updated' in fm and not validate_date(fm['last_updated']):
        issues.append(('ERROR', 'Frontmatter', rel, f'last_updated not valid ISO date'))
    
    h1, h2s = get_heading_sections(content)
    if h1 is None:
        issues.append(('ERROR', 'Sections', rel, 'File has no H1 title'))
    for sec in ['Parent', 'Stats', 'Files with this tag', 'Co-occurring tags']:
        if sec not in h2s:
            issues.append(('ERROR', 'Sections', rel, f'Missing required section: ## {sec}'))
    
    return issues

def validate_topic(filepath, fm, content):
    """Light validation for topic files (type:index, scope:topic)."""
    issues = []
    rel = str(filepath.relative_to(KB))
    
    fname = filepath.stem
    topic_field = fm.get('topic')
    if topic_field and str(topic_field) != fname:
        issues.append(('ERROR', 'Frontmatter', rel, f'topic field "{topic_field}" does not match filename "{fname}"'))
    
    if fm.get('auto_generated') != True:
        issues.append(('ERROR', 'Frontmatter', rel, 'auto_generated should be true'))
    
    if 'last_updated' in fm and not validate_date(fm['last_updated']):
        issues.append(('ERROR', 'Frontmatter', rel, f'last_updated not valid ISO date'))
    
    h1, _ = get_heading_sections(content)
    if h1 is None:
        issues.append(('ERROR', 'Sections', rel, 'File has no H1 title'))
    
    return issues


def main():
    files_to_check = []
    
    for d in ['wiki/concepts', 'wiki/sources', 'wiki/tag', 'wiki/topic']:
        p = KB / d
        if p.exists():
            files_to_check.extend(p.glob('*.md'))
    
    for f in ['wiki/wiki.md', 'raw/raw.md', 'context/context.md']:
        p = KB / f
        if p.exists():
            files_to_check.append(p)
    
    for rd in ['articles', 'posts', 'websites', 'videos', 'papers', 'repos', 'tools']:
        idx = KB / 'raw' / rd / f'{rd}.md'
        if idx.exists():
            files_to_check.append(idx)
    
    all_issues = []
    stats = {'concepts': 0, 'sources': 0, 'indexes': 0, 'topics': 0, 'errors_reading': 0}
    
    for filepath in sorted(files_to_check):
        rel = str(filepath.relative_to(KB))
        
        if rel in SKIP_FILES or 'wiki/reviews/' in rel or 'wiki/drafts/' in rel:
            continue
        if rel.startswith('raw/') and rel.endswith('.md'):
            fname = filepath.stem
            if re.match(r'^\d{4}-\d{2}-\d{2}_', fname):
                continue
            if filepath.parent.name == fname:
                pass
            elif filepath.name in ('raw.md',):
                pass
            elif 'index' not in rel.lower():
                continue
        
        try:
            content = filepath.read_text(encoding='utf-8')
        except Exception as e:
            all_issues.append(('ERROR', 'System', rel, f'Cannot read file: {e}'))
            stats['errors_reading'] += 1
            continue
        
        fm, raw_fm, fm_error = parse_frontmatter(content)
        
        if fm_error:
            if 'Missing opening' in fm_error:
                if 'context/USER.md' in rel:
                    continue
                all_issues.append(('ERROR', 'Frontmatter', rel, f'No frontmatter: {fm_error}'))
            else:
                all_issues.append(('ERROR', 'Frontmatter', rel, f'YAML parse error: {fm_error}'))
            continue
        
        if fm is None:
            all_issues.append(('ERROR', 'Frontmatter', rel, 'Cannot parse frontmatter'))
            continue
        
        file_type = fm.get('type', 'MISSING')
        file_scope = fm.get('scope', '')
        
        # Dispatch: topic files first (before index routing)
        if file_scope == 'topic' or str(filepath.parent.relative_to(KB)) == 'wiki/topic':
            issues = validate_topic(filepath, fm, content)
            stats['topics'] += 1
        elif file_type == 'concept':
            issues = validate_concept(filepath, fm, raw_fm, content)
            stats['concepts'] += 1
        elif file_type == 'source':
            issues = validate_source(filepath, fm, raw_fm, content)
            stats['sources'] += 1
        elif file_type == 'index':
            issues = validate_index(filepath, fm, raw_fm, content)
            stats['indexes'] += 1
        elif file_type == 'MISSING':
            issues = [('ERROR', 'Frontmatter', rel, 'Missing type field in frontmatter')]
        else:
            issues = [('ERROR', 'Frontmatter', rel, f'Unknown type: "{file_type}"')]
        
        all_issues.extend(issues)
    
    error_count = sum(1 for i in all_issues if i[0] == 'ERROR')
    warning_count = sum(1 for i in all_issues if i[0] == 'WARNING')
    info_count = sum(1 for i in all_issues if i[0] == 'INFO')
    
    print(f"FILES_CHECKED={len(files_to_check)}")
    print(f"CONCEPTS={stats['concepts']}")
    print(f"SOURCES={stats['sources']}")
    print(f"INDEXES={stats['indexes']}")
    print(f"TOPICS={stats['topics']}")
    print(f"ERRORS_READING={stats['errors_reading']}")
    print(f"TOTAL_ISSUES={len(all_issues)}")
    print(f"ERRORS={error_count}")
    print(f"WARNINGS={warning_count}")
    print(f"INFOS={info_count}")
    print("---ISSUES_BEGIN---")
    for sev, cat, rel, msg in all_issues:
        safe_msg = msg.replace('|', '\\|')
        print(f"{sev}|{cat}|{rel}|{safe_msg}")
    print("---ISSUES_END---")

if __name__ == '__main__':
    main()
