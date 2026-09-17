#!/usr/bin/env python3
"""
Format Validator script for Knowledge Base V2.
Runs against format-spec.md and index-spec.md rules.

Usage: python3 format_validator.py
Outputs: wiki/reviews/YYYY-MM-DD_format-report.md
"""

import os, re, yaml
from datetime import datetime, date
from pathlib import Path

KB_ROOT = Path('/home/julius/knowledge-base')

# Read TAGS.md to get Pool A and Pool B tags
# (Hardcoded here for speed; in production, parse TAGS.md tables)
POOL_A = ['ai', 'crypto', 'economic', 'politic', 'productivity', 'system', 'tech']
POOL_B = ['automation', 'coding', 'defi', 'hack', 'health', 'layer1', 'layer2', 'law', 'news', 'opinion', 'perpdex', 'psychology', 'research', 'tools', 'tutorial', 'vibecode']

issues = []
files_checked = []

def parse_frontmatter(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    if not content.startswith('---'):
        return None, None, 'missing frontmatter'
    end = content.find('\n---', 3)
    if end == -1:
        return None, None, 'invalid frontmatter delimiter'
    try:
        fm = yaml.safe_load(content[3:end])
    except yaml.YAMLError as e:
        return None, None, f'YAML error: {e}'
    body = content[end+4:]
    return fm, body, None

def is_valid_date(s):
    if isinstance(s, (datetime, date)):
        return 2000 <= s.year <= 2030
    if isinstance(s, str):
        try:
            d = datetime.strptime(s, '%Y-%m-%d')
            return 2000 <= d.year <= 2030
        except ValueError:
            return False
    return False

def is_valid_slug(s, max_len=50):
    return isinstance(s, str) and len(s) <= max_len and not re.search(r'[^a-z0-9\-\u00C0-\u1EF9]', s)

def extract_sections(body):
    return [line[3:].strip() for line in body.split('\n') if line.startswith('## ')]

def check_headings(body):
    return [line[1:].strip() for line in body.split('\n') if line.startswith('# ') and not line.startswith('## ')]

# Build file list
all_files = []
for dir_path in [KB_ROOT / 'wiki/sources', KB_ROOT / 'wiki/concepts', KB_ROOT / 'wiki/tag']:
    for f in dir_path.glob('*.md'):
        all_files.append(f)
for root_idx in [KB_ROOT / 'raw/raw.md', KB_ROOT / 'wiki/wiki.md', KB_ROOT / 'context/context.md']:
    if root_idx.exists():
        all_files.append(root_idx)
for sub_idx in [KB_ROOT / 'raw/articles/articles.md', KB_ROOT / 'raw/posts/posts.md', KB_ROOT / 'raw/videos/videos.md',
                KB_ROOT / 'raw/papers/papers.md', KB_ROOT / 'raw/repos/repos.md', KB_ROOT / 'raw/websites/websites.md',
                KB_ROOT / 'wiki/tag/tag.md']:
    if sub_idx.exists():
        all_files.append(sub_idx)
all_files = list(set(all_files))

# Cross-reference sets for broken wikilink detection
concept_files = set([f.name for f in (KB_ROOT / 'wiki/concepts').glob('*.md')])
source_files = set([f.name for f in (KB_ROOT / 'wiki/sources').glob('*.md')])

for fpath in sorted(all_files):
    rel_path = str(fpath.relative_to(KB_ROOT))
    files_checked.append(rel_path)
    fm, body, err = parse_frontmatter(fpath)
    if err:
        issues.append({'file': rel_path, 'severity': 'ERROR', 'category': 'Frontmatter', 'issue': f'Frontmatter parse error: {err}', 'current': 'missing or invalid', 'expected': 'Valid YAML with type field'})
        continue
    if not fm or 'type' not in fm:
        issues.append({'file': rel_path, 'severity': 'ERROR', 'category': 'Frontmatter', 'issue': 'Missing type field', 'current': 'none', 'expected': 'concept | source | index'})
        continue
    ftype = fm.get('type')
    if ftype == 'concept':
        slug = fpath.name[:-3]
        if not is_valid_slug(slug, 50):
            issues.append({'file': rel_path, 'severity': 'ERROR', 'category': 'Naming', 'issue': f'Invalid slug: {slug}', 'current': slug, 'expected': 'lowercase-hyphen, max 50'})
        req = ['type', 'status', 'main_tag', 'sub_tags', 'topic', 'sources', 'last_updated']
        for r in req:
            if r not in fm:
                issues.append({'file': rel_path, 'severity': 'ERROR', 'category': 'Frontmatter', 'issue': f'Missing {r}', 'current': 'missing', 'expected': f'{r} present'})
        if fm.get('status') not in ['draft', 'reviewed', 'needs-revision']:
            issues.append({'file': rel_path, 'severity': 'ERROR', 'category': 'Frontmatter', 'issue': f"Bad status: {fm.get('status')}", 'current': fm.get('status'), 'expected': 'draft | reviewed | needs-revision'})
        if fm.get('main_tag') not in POOL_A:
            issues.append({'file': rel_path, 'severity': 'ERROR', 'category': 'Frontmatter', 'issue': f"Bad main_tag: {fm.get('main_tag')}", 'current': fm.get('main_tag'), 'expected': f'one of {POOL_A}'})
        st = fm.get('sub_tags')
        if isinstance(st, list):
            if len(st) < 1 or len(st) > 3:
                issues.append({'file': rel_path, 'severity': 'ERROR', 'category': 'Frontmatter', 'issue': f'Bad sub_tags count: {len(st)}', 'current': len(st), 'expected': '1-3'})
            for t in st:
                if t not in POOL_B:
                    issues.append({'file': rel_path, 'severity': 'ERROR', 'category': 'Frontmatter', 'issue': f'Bad sub_tag: {t}', 'current': t, 'expected': f'one of {POOL_B}'})
        elif not isinstance(st, list):
            issues.append({'file': rel_path, 'severity': 'ERROR', 'category': 'Frontmatter', 'issue': 'sub_tags not list', 'current': type(st).__name__, 'expected': 'list'})
        if not is_valid_date(fm.get('last_updated')):
            issues.append({'file': rel_path, 'severity': 'ERROR', 'category': 'Frontmatter', 'issue': f"Bad last_updated: {fm.get('last_updated')}", 'current': fm.get('last_updated'), 'expected': 'YYYY-MM-DD'})
        sections = extract_sections(body)
        req_sections = ['Definition', 'Key ideas', 'Related concepts', 'Sources']
        for rs in req_sections:
            if rs not in sections:
                issues.append({'file': rel_path, 'severity': 'ERROR', 'category': 'Sections', 'issue': f'Missing section: {rs}', 'current': f'Sections: {sections}', 'expected': str(req_sections)})
        # Check required section order only (allow extra sections)
        req_indices = [sections.index(rs) for rs in req_sections if rs in sections]
        if req_indices != sorted(req_indices):
            issues.append({'file': rel_path, 'severity': 'WARNING', 'category': 'Sections', 'issue': 'Required section order mismatch', 'current': str(sections), 'expected': str(req_sections)})
        h1s = check_headings(body)
        if len(h1s) != 1:
            issues.append({'file': rel_path, 'severity': 'ERROR', 'category': 'Markdown', 'issue': f'H1 count: {len(h1s)}', 'current': len(h1s), 'expected': '1'})
        # Markdown links instead of wikilinks
        bad_links = re.findall(r'\[([^\]]+)\]\([^)]+\)', body)
        for bl in bad_links:
            if not bl.startswith('http') and not bl.startswith('!'):
                issues.append({'file': rel_path, 'severity': 'ERROR', 'category': 'Markdown', 'issue': f'Markdown link: [{bl}]', 'current': f'[{bl}](...)', 'expected': '[[slug]]'})
        # Broken wikilinks
        for wl in re.findall(r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]', body):
            target = wl.strip()
            expected = f"{target}.md"
            if target.startswith('src_'):
                if expected not in source_files:
                    issues.append({'file': rel_path, 'severity': 'WARNING', 'category': 'Markdown', 'issue': f'Broken wikilink to source: {target}', 'current': target, 'expected': f'File {expected} exists'})
            else:
                if expected not in concept_files:
                    issues.append({'file': rel_path, 'severity': 'WARNING', 'category': 'Markdown', 'issue': f'Broken wikilink to concept: {target}', 'current': target, 'expected': f'File {expected} exists'})
    elif ftype == 'source':
        if not fpath.name.startswith('src_'):
            issues.append({'file': rel_path, 'severity': 'ERROR', 'category': 'Naming', 'issue': 'Missing src_ prefix', 'current': fpath.name, 'expected': 'src_<slug>.md'})
        slug = fpath.name[4:-3]
        if not is_valid_slug(slug, 50):
            issues.append({'file': rel_path, 'severity': 'ERROR', 'category': 'Naming', 'issue': f'Invalid slug: {slug}', 'current': slug, 'expected': 'lowercase-hyphen, max 50'})
        req = ['type', 'original', 'main_tag', 'sub_tags', 'topic', 'date_compiled']
        for r in req:
            if r not in fm:
                issues.append({'file': rel_path, 'severity': 'ERROR', 'category': 'Frontmatter', 'issue': f'Missing {r}', 'current': 'missing', 'expected': f'{r} present'})
        if fm.get('main_tag') not in POOL_A:
            issues.append({'file': rel_path, 'severity': 'ERROR', 'category': 'Frontmatter', 'issue': f"Bad main_tag: {fm.get('main_tag')}", 'current': fm.get('main_tag'), 'expected': f'one of {POOL_A}'})
        st = fm.get('sub_tags')
        if isinstance(st, list):
            if len(st) < 1 or len(st) > 3:
                issues.append({'file': rel_path, 'severity': 'ERROR', 'category': 'Frontmatter', 'issue': f'Bad sub_tags count: {len(st)}', 'current': len(st), 'expected': '1-3'})
            for t in st:
                if t not in POOL_B:
                    issues.append({'file': rel_path, 'severity': 'ERROR', 'category': 'Frontmatter', 'issue': f'Bad sub_tag: {t}', 'current': t, 'expected': f'one of {POOL_B}'})
        elif not isinstance(st, list):
            issues.append({'file': rel_path, 'severity': 'ERROR', 'category': 'Frontmatter', 'issue': 'sub_tags not list', 'current': type(st).__name__, 'expected': 'list'})
        if not is_valid_date(fm.get('date_compiled')):
            issues.append({'file': rel_path, 'severity': 'ERROR', 'category': 'Frontmatter', 'issue': f"Bad date_compiled: {fm.get('date_compiled')}", 'current': fm.get('date_compiled'), 'expected': 'YYYY-MM-DD'})
        sections = extract_sections(body)
        req_sections = ['Metadata', 'Summary', 'Key points', 'Concepts referenced']
        for rs in req_sections:
            if rs not in sections:
                issues.append({'file': rel_path, 'severity': 'ERROR', 'category': 'Sections', 'issue': f'Missing section: {rs}', 'current': f'Sections: {sections}', 'expected': str(req_sections)})
        req_indices = [sections.index(rs) for rs in req_sections if rs in sections]
        if req_indices != sorted(req_indices):
            issues.append({'file': rel_path, 'severity': 'WARNING', 'category': 'Sections', 'issue': 'Required section order mismatch', 'current': str(sections), 'expected': str(req_sections)})
        h1s = check_headings(body)
        if len(h1s) != 1:
            issues.append({'file': rel_path, 'severity': 'ERROR', 'category': 'Markdown', 'issue': f'H1 count: {len(h1s)}', 'current': len(h1s), 'expected': '1'})
        bad_links = re.findall(r'\[([^\]]+)\]\([^)]+\)', body)
        for bl in bad_links:
            if not bl.startswith('http') and not bl.startswith('!'):
                issues.append({'file': rel_path, 'severity': 'ERROR', 'category': 'Markdown', 'issue': f'Markdown link: [{bl}]', 'current': f'[{bl}](...)', 'expected': '[[slug]]'})
        for wl in re.findall(r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]', body):
            target = wl.strip()
            expected = f"{target}.md"
            if target.startswith('src_'):
                if expected not in source_files:
                    issues.append({'file': rel_path, 'severity': 'WARNING', 'category': 'Markdown', 'issue': f'Broken wikilink to source: {target}', 'current': target, 'expected': f'File {expected} exists'})
            else:
                if expected not in concept_files:
                    issues.append({'file': rel_path, 'severity': 'WARNING', 'category': 'Markdown', 'issue': f'Broken wikilink to concept: {target}', 'current': target, 'expected': f'File {expected} exists'})
    elif ftype == 'index':
        level = fm.get('level')
        if level == 1:
            req = ['type', 'level', 'scope', 'auto_generated', 'last_updated']
            for r in req:
                if r not in fm:
                    issues.append({'file': rel_path, 'severity': 'ERROR', 'category': 'Frontmatter', 'issue': f'Missing {r}', 'current': 'missing', 'expected': f'{r} present'})
            if fm.get('scope') not in ['raw', 'wiki', 'context']:
                issues.append({'file': rel_path, 'severity': 'ERROR', 'category': 'Frontmatter', 'issue': f"Bad scope: {fm.get('scope')}", 'current': fm.get('scope'), 'expected': 'raw | wiki | context'})
            if fm.get('auto_generated') is not False:
                issues.append({'file': rel_path, 'severity': 'ERROR', 'category': 'Frontmatter', 'issue': f"Bad auto_generated: {fm.get('auto_generated')}", 'current': fm.get('auto_generated'), 'expected': 'false'})
            if not is_valid_date(fm.get('last_updated')):
                issues.append({'file': rel_path, 'severity': 'ERROR', 'category': 'Frontmatter', 'issue': f"Bad last_updated: {fm.get('last_updated')}", 'current': fm.get('last_updated'), 'expected': 'YYYY-MM-DD'})
            sections = extract_sections(body)
            for rs in ['Overview', 'Sub-indexes', 'Notes']:
                if rs not in sections:
                    issues.append({'file': rel_path, 'severity': 'ERROR', 'category': 'Sections', 'issue': f'Missing section: {rs}', 'current': f'Sections: {sections}', 'expected': 'Overview, Sub-indexes, Notes'})
            h1s = check_headings(body)
            if len(h1s) != 1:
                issues.append({'file': rel_path, 'severity': 'ERROR', 'category': 'Markdown', 'issue': f'H1 count: {len(h1s)}', 'current': len(h1s), 'expected': '1'})
        elif level == 2:
            req = ['type', 'level', 'scope', 'parent', 'auto_generated', 'items_managed_by', 'last_updated']
            for r in req:
                if r not in fm:
                    issues.append({'file': rel_path, 'severity': 'ERROR', 'category': 'Frontmatter', 'issue': f'Missing {r}', 'current': 'missing', 'expected': f'{r} present'})
            if fm.get('scope') not in ['articles', 'posts', 'websites', 'videos', 'papers', 'repos', 'tags']:
                issues.append({'file': rel_path, 'severity': 'ERROR', 'category': 'Frontmatter', 'issue': f"Bad scope: {fm.get('scope')}", 'current': fm.get('scope'), 'expected': 'articles | posts | websites | videos | papers | repos | tags'})
            if fm.get('auto_generated') is not False:
                issues.append({'file': rel_path, 'severity': 'ERROR', 'category': 'Frontmatter', 'issue': f"Bad auto_generated: {fm.get('auto_generated')}", 'current': fm.get('auto_generated'), 'expected': 'false'})
            if fm.get('items_managed_by') not in ['ingest-agent', 'index-agent']:
                issues.append({'file': rel_path, 'severity': 'ERROR', 'category': 'Frontmatter', 'issue': f"Bad items_managed_by: {fm.get('items_managed_by')}", 'current': fm.get('items_managed_by'), 'expected': 'ingest-agent | index-agent'})
            if not is_valid_date(fm.get('last_updated')):
                issues.append({'file': rel_path, 'severity': 'ERROR', 'category': 'Frontmatter', 'issue': f"Bad last_updated: {fm.get('last_updated')}", 'current': fm.get('last_updated'), 'expected': 'YYYY-MM-DD'})
            sections = extract_sections(body)
            for rs in ['Overview', 'Parent', 'Stats', 'Items', 'Notes']:
                if rs not in sections:
                    issues.append({'file': rel_path, 'severity': 'ERROR', 'category': 'Sections', 'issue': f'Missing section: {rs}', 'current': f'Sections: {sections}', 'expected': 'Overview, Parent, Stats, Items, Notes'})
            h1s = check_headings(body)
            if len(h1s) != 1:
                issues.append({'file': rel_path, 'severity': 'ERROR', 'category': 'Markdown', 'issue': f'H1 count: {len(h1s)}', 'current': len(h1s), 'expected': '1'})
        elif level == 3:
            req = ['type', 'level', 'scope', 'parent', 'tag', 'auto_generated', 'last_updated']
            for r in req:
                if r not in fm:
                    issues.append({'file': rel_path, 'severity': 'ERROR', 'category': 'Frontmatter', 'issue': f'Missing {r}', 'current': 'missing', 'expected': f'{r} present'})
            if fm.get('scope') != 'tag':
                issues.append({'file': rel_path, 'severity': 'ERROR', 'category': 'Frontmatter', 'issue': f"Bad scope: {fm.get('scope')}", 'current': fm.get('scope'), 'expected': 'tag'})
            if fm.get('parent') not in ['[[tag]]', [['tag']]]:
                issues.append({'file': rel_path, 'severity': 'ERROR', 'category': 'Frontmatter', 'issue': f"Bad parent: {fm.get('parent')}", 'current': fm.get('parent'), 'expected': '[[tag]]'})
            if fm.get('tag') != fpath.stem:
                issues.append({'file': rel_path, 'severity': 'ERROR', 'category': 'Frontmatter', 'issue': f"Bad tag: {fm.get('tag')}", 'current': fm.get('tag'), 'expected': fpath.stem})
            if fm.get('auto_generated') is not True:
                issues.append({'file': rel_path, 'severity': 'ERROR', 'category': 'Frontmatter', 'issue': f"Bad auto_generated: {fm.get('auto_generated')}", 'current': fm.get('auto_generated'), 'expected': 'true'})
            if not is_valid_date(fm.get('last_updated')):
                issues.append({'file': rel_path, 'severity': 'ERROR', 'category': 'Frontmatter', 'issue': f"Bad last_updated: {fm.get('last_updated')}", 'current': fm.get('last_updated'), 'expected': 'YYYY-MM-DD'})
            sections = extract_sections(body)
            for rs in ['Parent', 'Stats', 'Files with this tag', 'Co-occurring tags']:
                if rs not in sections:
                    issues.append({'file': rel_path, 'severity': 'ERROR', 'category': 'Sections', 'issue': f'Missing section: {rs}', 'current': f'Sections: {sections}', 'expected': 'Parent, Stats, Files with this tag, Co-occurring tags'})
            h1s = check_headings(body)
            if len(h1s) != 1:
                issues.append({'file': rel_path, 'severity': 'ERROR', 'category': 'Markdown', 'issue': f'H1 count: {len(h1s)}', 'current': len(h1s), 'expected': '1'})
        else:
            issues.append({'file': rel_path, 'severity': 'ERROR', 'category': 'Frontmatter', 'issue': f'Unknown level: {level}', 'current': level, 'expected': '1, 2, or 3'})
    else:
        issues.append({'file': rel_path, 'severity': 'ERROR', 'category': 'Frontmatter', 'issue': f'Unknown type: {ftype}', 'current': ftype, 'expected': 'concept | source | index'})

# Summarize
error_count = len([i for i in issues if i['severity'] == 'ERROR'])
warning_count = len([i for i in issues if i['severity'] == 'WARNING'])
info_count = len([i for i in issues if i['severity'] == 'INFO'])

# Report limit: 20 issues per day, ERROR prioritized
severity_order = {'ERROR': 0, 'WARNING': 1, 'INFO': 2}
sorted_issues = sorted(issues, key=lambda x: severity_order.get(x['severity'], 3))
report_issues = sorted_issues[:20]

report_date = datetime.now().strftime('%Y-%m-%d')
report_path = KB_ROOT / f'wiki/reviews/{report_date}_format-report.md'
report_path.parent.mkdir(parents=True, exist_ok=True)

lines = [
    f"# Format Validation \u2014 {report_date}",
    "",
    f"**Status:** {'pending' if issues else 'complete'}",
    f"**Issues found:** {len(issues)} (shown: {len(report_issues)})",
    f"**Created:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
    f"**Validator:** format-validator",
    "",
    f"- **ERROR:** {error_count}",
    f"- **WARNING:** {warning_count}",
    f"- **INFO:** {info_count}",
    f"- **Files checked:** {len(files_checked)}",
    "",
]
if len(issues) > 20:
    lines.append(f"> **Note:** Only first 20 issues shown (ERROR prioritized). Full scan found {len(issues)} total issues.")
    lines.append("")
for idx, issue in enumerate(report_issues, 1):
    lines.extend(["---", "", f"## Issue {idx}: {issue['issue']}", "",
                  f"**File:** {issue['file']}", f"**Severity:** {issue['severity']}",
                  f"**Category:** {issue['category']}", f"**Issue:** {issue['issue']}",
                  f"**Current:** {issue['current']}", f"**Expected:** {issue['expected']}", ""])
if not issues:
    lines.extend(["No format issues found. All files compliant.", ""])

with open(report_path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))

print(f"Report: {report_path}")
print(f"Total: {len(issues)} issues (ERROR {error_count}, WARNING {warning_count}, INFO {info_count})")
