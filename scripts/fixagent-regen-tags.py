#!/usr/bin/env python3
"""Fix Agent 2026-08-22 — regen 24 L3 tag files + rewrite tag.md (L2) per index-spec.md."""
import re, yaml
from pathlib import Path
from collections import defaultdict
from datetime import datetime

ROOT = Path('/home/julius/knowledge-base')
SRC, CON, TAG = ROOT/'wiki/sources', ROOT/'wiki/concepts', ROOT/'wiki/tag'
NOW_DATE = '2026-08-22'
NOW_TS = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def fm_of(p):
    m = re.match(r'^---\s*\n(.*?)\n---\s*\n', p.read_text(encoding='utf-8'), re.DOTALL)
    return yaml.safe_load(m.group(1)) if m else {}

files = []
for d, t in ((CON,'concept'), (SRC,'source')):
    for p in sorted(d.glob('*.md')):
        fm = fm_of(p)
        if not fm.get('main_tag'):
            continue
        files.append({'slug':p.stem,'type':t,
                      'title':' '.join(w.capitalize() for w in p.stem.replace('src_','').split('-')),
                      'main':fm.get('main_tag'),'subs':list(fm.get('sub_tags') or []),'topic':fm.get('topic','')})

idx = defaultdict(lambda:{'concepts':[],'sources':[]})
for f in files:
    idx[f['main']][f['type']+'s'].append(f)
    for st in f['subs']:
        idx[st][f['type']+'s'].append(f)
co = defaultdict(int)
for f in files:
    ts = [f['main']] + f['subs']
    for i,a in enumerate(ts):
        for b in ts[i+1:]:
            co[tuple(sorted((a,b)))] += 1

targets = sorted(p.stem for p in TAG.glob('*.md') if p.stem != 'tag')
print('Regenerating:', len(targets), 'tag files')

for tag in targets:
    d = idx.get(tag, {'concepts':[],'sources':[]})
    nc, ns = len(d['concepts']), len(d['sources'])
    items = [(f['slug'],f['title'],f['type'],f['main'],f['subs'],f['topic']) for f in d['concepts']+d['sources']]
    items.sort(key=lambda x:x[0])
    lines = []
    lines.append('---')
    lines.append('type: index')
    lines.append('level: 3')
    lines.append('scope: tag')
    lines.append('parent: "[[tag]]"')
    lines.append('tag: ' + tag)
    lines.append('auto_generated: true')
    lines.append('last_updated: ' + NOW_DATE)
    lines.append('---')
    lines.append('')
    lines.append('# Tag: #' + tag)
    lines.append('')
    lines.append('Auto-generated index of all content tagged with `#' + tag + '`.')
    lines.append('')
    lines.append('Last updated: ' + NOW_TS)
    lines.append('')
    lines.append('---')
    lines.append('')
    lines.append('## Parent')
    lines.append('')
    lines.append('- [[tag]]')
    lines.append('')
    lines.append('## Stats')
    lines.append('')
    lines.append('- Total files: ' + str(nc+ns))
    lines.append('- Sources: ' + str(ns))
    lines.append('- Concepts: ' + str(nc))
    lines.append('- Last updated: ' + NOW_DATE)
    lines.append('')
    lines.append('## Files with this tag')
    lines.append('')
    for slug,title,t,main,subs,topic in items:
        s = ', '.join('#'+x for x in subs)
        piece = '- [[' + slug + ']] — ' + title + ' (' + t + ', main: #' + main
        if s:
            piece += ', sub: [' + s + ']'
        if topic:
            piece += ', topic: ' + topic
        piece += ')'
        lines.append(piece)
    pairlist = [(b,n) for (a,b),n in co.items() if a==tag] + [(a,n) for (a,b),n in co.items() if b==tag]
    tops = sorted(pairlist, key=lambda x:-x[1])[:5]
    if tops:
        lines.append('')
        lines.append('## Co-occurring tags')
        lines.append('')
        lines.append('Tags that frequently appear with `#' + tag + '`:')
        lines.append('')
        for o,n in tops:
            unit = 'co-occurrence' if n == 1 else 'co-occurrences'
            lines.append('- [[' + o + ']] — ' + str(n) + ' ' + unit)
    (TAG/(tag + '.md')).write_text('\n'.join(lines) + '\n', encoding='utf-8')
print('24 L3 files written')

main_pool = ['ai','crypto','tech','productivity','system','economic','politic','health','investment']
sub_pool = ['hack','tools','automation','vibecode','research','tutorial','opinion','news','defi','perpdex','layer1','layer2','law','coding','psychology','geopolitics','strategy']
filed_main = [t for t in targets if t in main_pool]
filed_sub = [t for t in targets if t not in main_pool]
usage = {t: len(idx.get(t,{}).get('concepts',[])) + len(idx.get(t,{}).get('sources',[])) for t in targets}
top3 = sorted(usage.items(), key=lambda x:-x[1])[:3]
most_used = ', '.join('#' + t + ' (' + str(n) + ')' for t,n in top3)
main_items = '\n'.join(sorted('- [[' + t + ']]' for t in main_pool))
sub_items = '\n'.join(sorted('- [[' + t + ']]' for t in sub_pool))

tm = """---
type: index
level: 2
scope: tags
parent: "[[wiki]]"
auto_generated: false
items_managed_by: index-agent
last_updated: __D__
---

# Tag Index

Master index of all tags in the Knowledge Base.

Last updated: __TS__

---

## Overview

Master index of all tags used in the Knowledge Base. Tracks statistics, files per tag, and co-occurrence relationships across both main-tags (Pool A) and sub-tags (Pool B).

## Parent

- [[wiki]]

## Stats

- Total tags: __TT__
- Main tags: __TM__
- Sub tags: __TSB__
- Most used: __MU__
- Last updated: __D__

## Items

### Main Tags (Pool A)

__MAIN__

### Sub Tags (Pool B)

__SUB__

## Notes
"""
tm = (tm.replace('__D__', NOW_DATE).replace('__TS__', NOW_TS)
        .replace('__TT__', str(len(targets))).replace('__TM__', str(len(filed_main)))
        .replace('__TSB__', str(len(filed_sub))).replace('__MU__', most_used)
        .replace('__MAIN__', main_items).replace('__SUB__', sub_items))
(TAG/'tag.md').write_text(tm, encoding='utf-8')
print('tag.md written')
